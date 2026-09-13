#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FounderOS aday listesi aracı.

Öğrencinin klasöründeki adaylar.csv dosyasını yönetir ve adaylar.html sayfasını üretir.
FounderOS bu betiği klasörün içinde sessizce çalıştırır; öğrenci komut görmez.
Betik satır silmez, sütun uydurmaz, her yazıştan önce yedek alır ve sayfayı yeniler.

Komutlar (hepsi klasörün içinden çalışır, ya da --klasor ile klasör verilir):
  cek --is ISKIMLIGI [--ozet] [--anahtar FOS-...] [--tut AD ...] [--kategori-disi K ...]
                            (veri servisinden çekimi indirir ve listeye ekler; anahtarı is-beyni.md'den bulur)
  ekle DOSYA [--kaynak K] [--baglayan AD] [--tut AD ...] [--kategori-disi K ...] [--yuz]
  guncelle ANAHTAR sutun=deger ... [--semt S]
  temas ANAHTAR --kanal K --sonuc "..." [--durum D] [--asama A] [--siradaki "..."] [--tarih T] [--randevu "YYYY-AA-GG SS:DD"] [--not "..."]
  sonuclar DOSYA            (sayfanın "Sonuçları kopyala" metni; her satırı temas olarak işler)
                            satır: AD | kanal | sonuç [| anahtar: değer ...]
                            sonuç: açmadı, gönderdim, istemedi, ilgilendi, randevu, sonra, cevap
                            cevapta: metin: "gelen cevabın kendisi" ve dal: fiyat|bilgi|mesgul|...
  ogren [--esik N]          (hangi gözlem ve hangi kanal cevap getiriyor; eşik altı sayılmaz)
  isaret DOSYA --isaret A   (toplu araştırmanın sonucu: is_ilani; her satır bir işletme adı.
                             reklam_veriyor elle yazılmaz, veri servisinden gelir)
  sil ANAHTAR --sebep "..."  (satırı elenme ile işaretler, silmez)
  bugun [--sayi N] [--planla] [--kanal telefon|yazı]
  yuz-sec [--sayi N] [--yorum-ust-siniri N]
                            (en çok istenen yüzü listeden seçer. Sıra: ilan verenler, reklam verenler,
                             sızıntı puanı, yorum sayısı, ulaşılabilir olanlar. Yorum sayısı üst sınırın
                             üstündekiler listenin sonuna konur. Elle işaretlenmişlere dokunmaz)
  ozet
  bul METIN
  sayfa [--kart TELEFON.md | --dosya SENARYO.json] [--nis AD] [--ogrenci-ad AD --sehir S --sistem-adi AD] [--acilis "..."] [--itiraz "..."]...
                            (Saha modu kartının söyle metni: niş kartının "Telefonda söylenecekler" bölümü ve öğrencinin adı, şehri)
  surum
"""
import argparse, csv, datetime, io, json, os, re, shutil, sys, unicodedata
from pathlib import Path

SURUM = "0.34.0"
IST = datetime.timezone(datetime.timedelta(hours=3))

SERVIS = ["kisa_ad", "ad", "telefon", "eposta", "instagram", "site", "adres", "semt",
          "yorum_sayisi", "puan", "kategori", "ipuclari", "yorum_alinti", "reklam",
          "elenme", "harita"]
EKLENEN = ["eklenme_tarihi", "kaynak", "baglayan", "yuz", "sahibi", "uygunluk", "sizinti",
           "bulgu", "kanca", "lira", "denetim_tarihi", "asama", "telefon_durumu",
           "eposta_durumu", "instagram_durumu", "video_durumu", "temas_sayisi",
           "son_temas_tarihi", "son_temas_kanali", "siradaki_hareket", "siradaki_tarih",
           "randevu_tarihi", "eposta_konu", "eposta_metni", "dm_metni",
           "son_cevap", "cevap_dali", "zincir_adimi", "acmadi_sayisi", "not"]
SUTUNLAR = SERVIS + EKLENEN
ASAMALAR = ["yeni", "temasta", "cevap verdi", "randevu", "görüşüldü", "sonra", "kapandı", "müşteri"]
DURUMLAR = ["yapılmadı", "yapıldı", "cevap geldi", "kapandı"]
# Video kanalinin bir durumu fazla: Loom videonun izlenip izlenmedigini
# soyluyor. Izlenme cevap degil ama cevaptan once elimizdeki tek isaret ve
# dorduncu gunun aramasinin sirasini o belirliyor.
VIDEO_DURUMLAR = DURUMLAR + ["izlendi"]
KANALLAR = ["telefon", "e-posta", "instagram", "video"]
KANAL_SUTUN = {"telefon": "telefon_durumu", "e-posta": "eposta_durumu",
               "instagram": "instagram_durumu", "video": "video_durumu"}
# "reklam": Meta reklam kutuphanesinden gelen satir. Veri servisi bu kaynagi
# Haritalar cekimiyle ayni listeye koyuyor; ogrenci tek liste goruyor.
KAYNAKLAR = ["haritalar", "reklam", "iş ilanı", "elle", "tanıdık", "referans"]
TARIH_SUTUN = ["eklenme_tarihi", "denetim_tarihi", "son_temas_tarihi", "siradaki_tarih"]
SAYI_SUTUN = ["uygunluk", "sizinti", "temas_sayisi"]
KILITLI = ["elenme", "eklenme_tarihi"]  # guncelle ile değişmez

KLASOR = Path(".")


def calisma():
    return KLASOR / ".founderos"


def bugun():
    return datetime.datetime.now(IST).date()


def simdi_metin():
    return datetime.datetime.now(IST).strftime("%d.%m.%Y %H:%M")


def hata(m):
    print("HATA: " + m)
    sys.exit(1)


def kucult(s):
    s = (s or "").strip()
    s = s.replace("İ", "i").replace("I", "ı")
    return s.lower()


def rakam(s):
    return re.sub(r"\D", "", s or "")


def tarih_coz(s, ad="tarih"):
    """bugün, yarın, +N, YYYY-AA-GG, GG.AA.YYYY -> YYYY-AA-GG (saat varsa korunur)."""
    s = (s or "").strip()
    if not s:
        return ""
    k = kucult(s)
    if k in ("bugün", "bugun"):
        return bugun().isoformat()
    if k in ("yarın", "yarin"):
        return (bugun() + datetime.timedelta(days=1)).isoformat()
    m = re.fullmatch(r"\+(\d{1,3})", k)
    if m:
        return (bugun() + datetime.timedelta(days=int(m.group(1)))).isoformat()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}):(\d{2}))?", s)
    if m:
        try:
            datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            hata("%s geçersiz: %s" % (ad, s))
        return s.replace("T", " ")
    m = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})(?: (\d{2}):(\d{2}))?", s)
    if m:
        t = "%s-%02d-%02d" % (m.group(3), int(m.group(2)), int(m.group(1)))
        if m.group(4):
            t += " %s:%s" % (m.group(4), m.group(5))
        return tarih_coz(t, ad)
    hata("%s anlaşılmadı: %s (bugün, yarın, +3 ya da 2026-09-15 yaz)" % (ad, s))


def telefon_normalize(t):
    r = rakam(t)
    if not r:
        return ""
    if r.startswith("0090"):
        r = r[4:]
    elif r.startswith("90") and len(r) == 12:
        r = r[2:]
    elif r.startswith("0") and len(r) == 11:
        r = r[1:]
    if len(r) != 10:
        return "+" + rakam(t) if t.strip().startswith("+") else (t or "").strip()
    return "+90" + r


# ---------- dosya ----------

def _metni_oku(p):
    """Dosyayi kodlamasi ne olursa olsun metne cevirir.
    Ogrenci csv'yi Excel'de acip kaydederse dosya Turkce Windows'ta cp1254
    oluyor ve utf-8 okuma coker. Coken arac gunu durduruyor; o yuzden sirayla
    denenir ve son care hatali baytlar atlanir."""
    ham = p.read_bytes()
    for kod in ("utf-8-sig", "utf-8", "cp1254", "latin-1"):
        try:
            return ham.decode(kod), kod
        except UnicodeDecodeError:
            continue
    return ham.decode("utf-8", "replace"), "bozuk"


def uyar(m):
    print("UYARI: " + m)


def yukle():
    p = KLASOR / "adaylar.csv"
    if not p.exists():
        return []
    metin, kodlama = _metni_oku(p)
    # Excel Turkce yerelde noktali virgulle kaydediyor. Basligi ayirici icin
    # ornekleyip dogru ayiriciyi seciyoruz.
    ilk = metin.split("\n", 1)[0]
    ayirici = ";" if ilk.count(";") > ilk.count(",") else ","
    okuyucu = csv.DictReader(io.StringIO(metin), delimiter=ayirici)
    basliklar = [b for b in (okuyucu.fieldnames or []) if b]
    bilinmeyen = [b for b in basliklar if b not in SUTUNLAR]
    if bilinmeyen:
        # Eskiden burada duruyorduk ve o gun hicbir komut calismiyordu. Artik
        # tanimadigimiz sutun yok sayilir; kendi sutunlarimizin hicbiri kaybolmaz.
        uyar("adaylar.csv'de tanınmayan sütun var, yok sayıldı: %s" % ", ".join(bilinmeyen))
    if basliklar and not any(b in SUTUNLAR for b in basliklar):
        hata("adaylar.csv okunamadı: başlık satırı tanınmıyor. Dosya başka bir programda değiştirilmiş olabilir; "
             ".founderos/yedek klasöründeki son kopyayı geri al.")
    # Eksik sutun hata degil: eski dosya yeni sutunlarla acilir, bos gelir
    # ve ilk kayitta dosyaya yazilir.
    satirlar = []
    for s in okuyucu:
        satirlar.append({k: (s.get(k) or "").strip() for k in SUTUNLAR})
    if kodlama not in ("utf-8-sig", "utf-8") or ayirici == ";":
        uyar("adaylar.csv başka bir programda kaydedilmiş görünüyor (%s, ayırıcı '%s'); düzeltilmiş hâliyle yeniden yazılacak."
             % (kodlama, ayirici))
    return satirlar


def _kilit_al(bekle=10):
    """Ayni klasorde iki komut ayni anda yazarsa biri otekinin yazdigini siliyor.
    Basit kilit: dosya varsa bekle, on saniyede acilmazsa devam et (kilit dosyasi
    bir cokmeden kalmis olabilir, gunun durmasindan iyidir)."""
    k = calisma() / "kilit"
    for _ in range(int(bekle * 10)):
        try:
            fd = os.open(str(k), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            return k
        except FileExistsError:
            try:
                if datetime.datetime.now().timestamp() - k.stat().st_mtime > 60:
                    k.unlink()
                    continue
            except OSError:
                pass
            import time as _t
            _t.sleep(0.1)
    return None


def _kilit_birak(k):
    if k:
        try:
            k.unlink()
        except OSError:
            pass


def kaydet(satirlar, sayfa_da=True):
    p = KLASOR / "adaylar.csv"
    kilit = _kilit_al()
    try:
        _kaydet_gercek(p, satirlar, sayfa_da)
    finally:
        _kilit_birak(kilit)


def _kaydet_gercek(p, satirlar, sayfa_da):
    yedek = calisma() / "yedek"
    yedek.mkdir(parents=True, exist_ok=True)
    if p.exists():
        # Yedek yalnizca icerik degisiyorsa alinir. Eskiden yazmayan komutlar da
        # yedek uretiyordu ve on komutluk bir oturum butun iyi kopyalari siliyordu.
        simdi = datetime.datetime.now(IST)
        eskiler = sorted(yedek.glob("adaylar-*.csv"))
        son = eskiler[-1] if eskiler else None
        ayni = False
        try:
            ayni = bool(son) and son.read_bytes() == p.read_bytes()
        except OSError:
            ayni = False
        if not ayni:
            shutil.copyfile(p, yedek / ("adaylar-" + simdi.strftime("%Y%m%d-%H%M%S") + ".csv"))
        # Gunun ilk kopyasi ayri saklanir ve silinmez: otuz gun geri donulebilir.
        gunluk = yedek / ("gun-" + simdi.strftime("%Y%m%d") + ".csv")
        if not gunluk.exists():
            shutil.copyfile(p, gunluk)
        for e in sorted(yedek.glob("adaylar-*.csv"))[:-30]:
            try:
                e.unlink()
            except OSError:
                pass
        for e in sorted(yedek.glob("gun-*.csv"))[:-30]:
            try:
                e.unlink()
            except OSError:
                pass
    gecici = p.with_suffix(".csv.tmp")
    # utf-8-sig: BOM'suz yazilan dosyayi Turkce Windows'ta Excel bozuk gosteriyor
    # ve ogrenci kaydedince dosya cp1254'e donuyordu.
    with io.open(gecici, "w", encoding="utf-8-sig", newline="") as f:
        y = csv.DictWriter(f, SUTUNLAR, lineterminator="\n")
        y.writeheader()
        for s in satirlar:
            y.writerow({k: s.get(k, "") for k in SUTUNLAR})
    os.replace(gecici, p)
    if sayfa_da:
        sayfa_uret(satirlar)


def nis_oku():
    p = calisma() / "sayfa.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            return {}
    return {}


def _csv_metni(satirlar):
    """Satirlari temiz csv metnine cevirir. Sayfa uretimi bozuk dosyada da calissin diye."""
    c = io.StringIO()
    y = csv.DictWriter(c, SUTUNLAR, lineterminator="\n")
    y.writeheader()
    for s in satirlar:
        y.writerow({k: s.get(k, "") for k in SUTUNLAR})
    return c.getvalue()


def sayfa_uret(satirlar=None):
    sablon = Path(__file__).resolve().parent / "adaylar-sablon.html"
    if not sablon.exists():
        print("UYARI: sayfa şablonu bulunamadı (%s); sayfa yenilenmedi." % sablon)
        return
    p = KLASOR / "adaylar.csv"
    # Kodlama ve ayirici bozuk olabilir (Excel). Sayfa da bu yuzden cokmesin:
    # satirlar yukle() ile okunup temiz csv'ye cevriliyor.
    ham = ""
    if p.exists():
        try:
            ham = _metni_oku(p)[0]
            ilk = ham.split("\n", 1)[0]
            if ilk.count(";") > ilk.count(","):
                ham = _csv_metni(yukle())
        except Exception:
            ham = _csv_metni(yukle())
    veri = ("window.ADAYLAR=" + json.dumps(ham, ensure_ascii=False) +
            ";window.ADAYLAR_TARIH=" + json.dumps(simdi_metin()) +
            ";window.ADAYLAR_NIS=" + json.dumps(nis_oku(), ensure_ascii=False) + ";")
    veri = veri.replace("</", "<\\/")
    m = sablon.read_text(encoding="utf-8")
    if "/*FOUNDEROS-VERI*/" not in m:
        print("UYARI: şablonda veri yeri yok; sayfa yenilenmedi.")
        return
    cikti = m.replace("/*FOUNDEROS-VERI*/", veri, 1)
    hedef = KLASOR / "adaylar.html"
    gecici = hedef.with_suffix(".html.tmp")
    gecici.write_text(cikti, encoding="utf-8")
    os.replace(gecici, hedef)


# ---------- satır bulma ----------

def satir_bul(satirlar, anahtar, semt=None):
    a = (anahtar or "").strip()
    if not a:
        hata("işletme adı ya da telefon gerekli")
    tel = rakam(a) if re.fullmatch(r"[+\d\s()-]{7,}", a) else ""
    if tel:
        adaylar = [s for s in satirlar if rakam(s["telefon"]).endswith(tel[-10:])]
    elif "@" in a and "." in a.split("@")[-1]:
        # e-posta adresi: gelen cevap yapistirilinca gonderenden bulunur
        k = kucult(a)
        adaylar = [s for s in satirlar if kucult(s["eposta"]) == k]
        if not adaylar:
            alan = k.split("@")[-1]
            adaylar = [s for s in satirlar if alan and (alan in kucult(s["eposta"]) or alan in kucult(s["site"]))]
    elif a.startswith("@"):
        # instagram kullanici adi
        k = kucult(a).lstrip("@")
        adaylar = [s for s in satirlar if kucult(s["instagram"]).lstrip("@") == k]
    else:
        k = kucult(a)
        adaylar = [s for s in satirlar if kucult(s["kisa_ad"]) == k or kucult(s["ad"]) == k]
        if not adaylar:
            adaylar = [s for s in satirlar if k in kucult(s["kisa_ad"]) or k in kucult(s["ad"])]
    if semt:
        adaylar = [s for s in adaylar if kucult(s["semt"]) == kucult(semt)]
    if not adaylar:
        hata("bulunamadı: %s" % a)
    if len(adaylar) > 1:
        secenek = "; ".join("%s (%s, %s)" % (s["kisa_ad"], s["semt"] or "semt yok", s["telefon"] or "telefon yok") for s in adaylar[:8])
        hata("birden fazla eşleşme, telefonla ya da --semt ile ayır: " + secenek)
    return adaylar[0]


def ozet_satir(s):
    _b, _k, _kaynak = gozlem(s)
    # Uyari isareti bulgunun yerine gecmez, yanina yazilir: aday aranmadan once
    # dogrulanacak demektir.
    _ip = set((s.get("ipuclari") or "").split())
    _uyari = [u for u in UYARI_ISARET if u in _ip]
    if _uyari:
        _b = ((_b + " ") if _b else "") + "[kapanmış olabilir, önce doğrula]"
    return " | ".join([s["kisa_ad"] or s["ad"], s["telefon"] or "telefon yok", s["sahibi"] or "sahibi ?",
                       "sızıntı " + (s["sizinti"] or "-"), s["asama"] or "yeni",
                       ("son " + s["son_temas_tarihi"] + " " + s["son_temas_kanali"]).strip() if s["son_temas_tarihi"] else "temas yok",
                       ("sıradaki " + s["siradaki_tarih"] + " " + s["siradaki_hareket"]).strip() if s["siradaki_tarih"] else "sıradaki yok",
                       (_b + (" (profilden)" if _kaynak == "profil" else "")) if _b else ""]).rstrip(" |")


# ---------- komutlar ----------

def kmt_ekle(a):
    p = Path(a.dosya)
    if not p.exists():
        hata("dosya yok: %s" % a.dosya)
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        gelen = list(csv.DictReader(f))
    if not gelen:
        hata("dosyada kayıt yok")
    listeye_ekle(gelen, a)


def listeye_ekle(gelen, a):
    satirlar = yukle()
    kaynak = getattr(a, "kaynak", None) or "haritalar"
    if kaynak not in KAYNAKLAR:
        hata("kaynak şunlardan biri olmalı: " + ", ".join(KAYNAKLAR))
    tut = {kucult(x) for x in (a.tut or [])}
    disi = [kucult(x) for x in (a.kategori_disi or [])]
    telefonlar = {rakam(s["telefon"])[-10:] for s in satirlar if s["telefon"]}
    adlar = {(kucult(s["kisa_ad"]), kucult(s["semt"])) for s in satirlar}
    eklendi = 0
    atlanan = {"tekrar": 0, "kategori dışı": 0}
    elenen = {}
    bugun_m = bugun().isoformat()
    for g in gelen:
        g = {k: (v or "").strip() for k, v in g.items() if k}
        ad = g.get("kisa_ad") or g.get("ad") or ""
        if not ad:
            continue
        if g.get("elenme") and kucult(ad) not in tut:
            elenen[g["elenme"]] = elenen.get(g["elenme"], 0) + 1
            continue
        kat = kucult(g.get("kategori"))
        if disi and any(d in kat for d in disi):
            atlanan["kategori dışı"] += 1
            continue
        tel = telefon_normalize(g.get("telefon", ""))
        anahtar = rakam(tel)[-10:] if tel else ""
        if anahtar and anahtar in telefonlar:
            atlanan["tekrar"] += 1
            continue
        if not anahtar and (kucult(ad), kucult(g.get("semt"))) in adlar:
            atlanan["tekrar"] += 1
            continue
        s = {k: "" for k in SUTUNLAR}
        for k in SERVIS:
            s[k] = g.get(k, "")
        s["kisa_ad"] = g.get("kisa_ad") or ad
        s["ad"] = g.get("ad") or ad
        s["telefon"] = tel
        s["elenme"] = ""
        s["eklenme_tarihi"] = bugun_m
        s["kaynak"] = kaynak
        s["baglayan"] = getattr(a, "baglayan", None) or g.get("baglayan", "")
        s["yuz"] = "evet" if getattr(a, "yuz", False) else ""
        s["asama"] = "yeni"
        for k in KANAL_SUTUN.values():
            s[k] = "yapılmadı"
        s["temas_sayisi"] = "0"
        for k in ("sahibi", "not", "kanca", "bulgu"):
            if g.get(k):
                s[k] = g[k]
        satirlar.append(s)
        eklendi += 1
        if anahtar:
            telefonlar.add(anahtar)
        adlar.add((kucult(s["kisa_ad"]), kucult(s["semt"])))
    kaydet(satirlar)
    print("eklendi: %d" % eklendi)
    if elenen:
        print("servisin işaretlediği için alınmayan: " + ", ".join("%s %d" % (k, v) for k, v in elenen.items()))
    print("atlanan: tekrar %d, kategori dışı %d" % (atlanan["tekrar"], atlanan["kategori dışı"]))
    print("listede toplam: %d (telefonlu %d)" % (len(satirlar), sum(1 for s in satirlar if s["telefon"])))


ANAHTAR_DESEN = re.compile(r"FOS-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}")


def anahtar_bul(verilen):
    if verilen:
        return verilen.strip()
    p = KLASOR / "is-beyni.md"
    if p.exists():
        m = ANAHTAR_DESEN.search(p.read_text(encoding="utf-8", errors="ignore"))
        if m:
            return m.group(0)
    hata("lisans anahtarı bulunamadı; --anahtar ile ver")


def servis_cagir(adres, arac, argumanlar):
    import urllib.request, urllib.error
    govde = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                        "params": {"name": arac, "arguments": argumanlar}}).encode("utf-8")
    istek = urllib.request.Request(adres, data=govde, method="POST",
                                   headers={"content-type": "application/json", "accept": "application/json",
                                            "user-agent": "founderos-aday-araci/" + SURUM})
    try:
        with urllib.request.urlopen(istek, timeout=45) as c:
            cevap = json.loads(c.read().decode("utf-8"))
    except (urllib.error.URLError, OSError, ValueError) as e:
        print("HATA: veri servisine ulaşılamadı (%s). Yedek: aday_sonuc ile sayfaları al, .founderos/gelen.csv yaz, ekle komutunu çalıştır." % e.__class__.__name__)
        sys.exit(2)
    if "error" in cevap:
        hata("servis: " + str(cevap["error"].get("message")))
    try:
        return json.loads(cevap["result"]["content"][0]["text"])
    except (KeyError, IndexError, TypeError, ValueError):
        hata("servis cevabı anlaşılmadı")


def kmt_cek(a):
    anahtar = anahtar_bul(a.anahtar)
    adres = a.adres or "https://founderos.so/mcp"
    ilk = servis_cagir(adres, "aday_sonuc", {"anahtar": anahtar, "is_id": a.is_id, "sayfa": 1,
                                             "sayfa_boyu": 10 if a.ozet else 100, "elenenler_dahil": True})
    durum = ilk.get("durum")
    if durum == "calisiyor":
        print("çalışıyor: çekim henüz bitmedi, biraz sonra yine sor")
        sys.exit(3)
    if durum != "hazir":
        hata("servis %s: %s" % (durum, ilk.get("mesaj", "")))
    o = ilk.get("ozet") or {}
    isaretli = o.get("isaretli") or {}
    print("çekim %s, %s%s, %s: toplam %s kayıt, kalan %s; telefonlu %s, e-postalı %s, instagramlı %s" % (
        a.is_id, ilk.get("kategori", ""), (", " + ilk["ilce"]) if ilk.get("ilce") else "", ilk.get("sehir", ""),
        o.get("toplam", "?"), o.get("kalan", "?"), o.get("telefonlu", "?"), o.get("epostali", "?"), o.get("instagramli", "?")))
    if isaretli:
        print("servisin işaretlediği: " + ", ".join("%s %s" % (k, v) for k, v in isaretli.items()))
    ip = o.get("ipuclari") or {}
    if ip:
        print("ipuçları: " + ", ".join("%s %s" % (k, v) for k, v in ip.items()))
    if a.ozet:
        return
    baslik = (ilk.get("baslik") or "").split(",")
    metin = [ilk.get("baslik") or ""]
    metin.append(ilk.get("satirlar") or "")
    for sayfa in range(2, int(ilk.get("sayfa_sayisi") or 1) + 1):
        c = servis_cagir(adres, "aday_sonuc", {"anahtar": anahtar, "is_id": a.is_id, "sayfa": sayfa,
                                               "sayfa_boyu": 100, "elenenler_dahil": True})
        if c.get("durum") != "hazir":
            hata("sayfa %d alınamadı: %s" % (sayfa, c.get("mesaj", "")))
        metin.append(c.get("satirlar") or "")
    ham = "\n".join(x for x in metin if x)
    gelen_dosya = calisma() / "gelen.csv"
    gelen_dosya.write_text(ham + "\n", encoding="utf-8")
    gelen = list(csv.DictReader(io.StringIO(ham)))
    if not gelen or not baslik or "kisa_ad" not in baslik:
        hata("servisten satır gelmedi")
    listeye_ekle(gelen, a)


def deger_dogrula(sutun, deger):
    if sutun not in SUTUNLAR:
        hata("böyle bir sütun yok: %s" % sutun)
    if sutun in KILITLI:
        hata("%s guncelle ile değişmez (silmek için sil komutu)" % sutun)
    if sutun == "asama" and deger and deger not in ASAMALAR:
        hata("aşama şunlardan biri olmalı: " + ", ".join(ASAMALAR))
    if sutun in KANAL_SUTUN.values() and deger:
        izin = VIDEO_DURUMLAR if sutun == "video_durumu" else DURUMLAR
        if deger not in izin:
            hata("kanal durumu şunlardan biri olmalı: " + ", ".join(izin))
    if sutun == "son_temas_kanali" and deger and deger not in KANALLAR:
        hata("kanal şunlardan biri olmalı: " + ", ".join(KANALLAR))
    if sutun == "kaynak" and deger and deger not in KAYNAKLAR:
        hata("kaynak şunlardan biri olmalı: " + ", ".join(KAYNAKLAR))
    if sutun in TARIH_SUTUN:
        return tarih_coz(deger, sutun)
    if sutun == "randevu_tarihi":
        return tarih_coz(deger, sutun)
    if sutun in SAYI_SUTUN and deger and not re.fullmatch(r"\d{1,3}", deger):
        hata("%s sayı olmalı" % sutun)
    if sutun == "uygunluk" and deger and int(deger) > 15:
        hata("uygunluk 0-15 arası")
    if sutun == "sizinti" and deger and int(deger) > 5:
        hata("sızıntı 0-5 arası")
    if sutun == "telefon":
        return telefon_normalize(deger)
    if sutun == "yuz":
        return "evet" if kucult(deger) in ("evet", "1", "x", "e") else ""
    return deger


def not_ekle(s, metin):
    metin = (metin or "").strip()
    if not metin:
        return
    parca = bugun().strftime("%d.%m") + " " + metin
    s["not"] = (s["not"] + "; " + parca) if s["not"] else parca


def kmt_guncelle(a):
    satirlar = yukle()
    s = satir_bul(satirlar, a.anahtar, a.semt)
    if not a.alanlar:
        hata("en az bir sutun=deger ver")
    for alan in a.alanlar:
        if "=" not in alan:
            hata("biçim sutun=deger olmalı: %s" % alan)
        sutun, deger = alan.split("=", 1)
        sutun = sutun.strip()
        deger = deger.strip()
        if sutun == "not":
            if deger.startswith("="):
                s["not"] = deger[1:].strip()
            else:
                not_ekle(s, deger)
            continue
        if sutun == "temas_sayisi" and deger.startswith("+"):
            deger = str(int(s["temas_sayisi"] or 0) + int(deger[1:] or 1))
        s[sutun] = deger_dogrula(sutun, deger)
    kaydet(satirlar)
    print("güncellendi: " + ozet_satir(s) + (" | DİKKAT, bu satır listeden çıkarılmış: " + s["elenme"] if s["elenme"] else ""))


def temas_uygula(satirlar, s, kanal, sonuc, durum=None, asama=None, siradaki=None, tarih=None, randevu=None, notu=None):
    if kanal not in KANALLAR:
        hata("kanal şunlardan biri olmalı: " + ", ".join(KANALLAR))
    izin = VIDEO_DURUMLAR if kanal == "video" else DURUMLAR
    if durum and durum not in izin:
        hata("durum şunlardan biri olmalı: " + ", ".join(izin))
    if asama and asama not in ASAMALAR:
        hata("aşama şunlardan biri olmalı: " + ", ".join(ASAMALAR))
    s[KANAL_SUTUN[kanal]] = durum or "yapıldı"
    s["temas_sayisi"] = str(int(s["temas_sayisi"] or 0) + 1)
    s["son_temas_tarihi"] = bugun().isoformat()
    s["son_temas_kanali"] = kanal
    if asama:
        s["asama"] = asama
    elif s["asama"] in ("", "yeni"):
        s["asama"] = "temasta"
    if durum == "cevap geldi" and s["asama"] in ("yeni", "temasta", "sonra"):
        s["asama"] = "cevap verdi"
    if randevu:
        s["randevu_tarihi"] = tarih_coz(randevu, "randevu")
        s["asama"] = "randevu"
    if siradaki is not None:
        s["siradaki_hareket"] = siradaki
    if tarih is not None:
        s["siradaki_tarih"] = tarih_coz(tarih, "sıradaki tarih")
    if s["asama"] == "kapandı":
        s["siradaki_hareket"] = ""
        s["siradaki_tarih"] = ""
    # Acik kalan hicbir adayin sirasi bos kalamaz. Bos kalirsa aday gunun
    # listesinden tamamen dusuyor ve bir daha hic gorunmuyor: ne takipte, ne
    # "hic aranmamis"ta. Cagiran komut sira vermediyse zincirden hesaplanir.
    # Randevu alindiysa sıradaki adim gorusmenin kendisidir.
    if s["asama"] == "randevu" and s["randevu_tarihi"] and not s["siradaki_tarih"]:
        s["siradaki_hareket"] = "randevu hazırlığı"
        s["siradaki_tarih"] = s["randevu_tarihi"][:10]
    eski_sira = (s["siradaki_tarih"] or "")[:10]
    if acik(s) and not tarih and s["asama"] != "randevu" \
       and (not eski_sira or eski_sira <= bugun().isoformat()):
        # Zincir adimi kanal basina degil aday basina sayiliyor, ama yalniz
        # gercekten giden bir sey adim yiyor. Video kendi zincirini yuruyor.
        zincir_sifirla_gerekirse(s, kanal)
        adim = int(s["zincir_adimi"] or 0) + 1
        s["zincir_adimi"] = str(adim)
        g = video_gunu(adim) if kanal == "video" else takip_gunu(s, adim)
        if g:
            onek = "" if kanal == "video" else "%s, " % kanal
            s["siradaki_hareket"] = onek + g[1]
            s["siradaki_tarih"] = tarih_coz("+%d" % g[0], "sıradaki tarih")
        else:
            s["asama"] = "sonra"
            s["siradaki_hareket"] = "zincir bitti, yeniden bak"
            s["siradaki_tarih"] = tarih_coz("+90", "sıradaki tarih")
    if sonuc:
        not_ekle(s, "%s: %s" % (kanal, sonuc))
    if notu:
        not_ekle(s, notu)


def kmt_temas(a):
    satirlar = yukle()
    s = satir_bul(satirlar, a.anahtar, a.semt)
    temas_uygula(satirlar, s, a.kanal, a.sonuc, a.durum, a.asama, a.siradaki, a.tarih, a.randevu, a.notu)
    kaydet(satirlar)
    print("temas işlendi: " + ozet_satir(s))


def takip_gunu(s, kacinci=None):
    """Yazili kanal zinciri: ilk mesajdan 3, 7 ve 14 gun sonra takip. Gunler goreli veriliyor
    (3, sonra 4, sonra 7), toplami 3/7/14 ediyor. Ucuncu takipten sonra zincir biter.
    Sayac temas_sayisi DEGIL zincir_adimi: acilmayan telefon zincirden adim yemiyor,
    yoksa uc kez acmayan adayin ilk e-postasi zinciri bitirmis sayiliyordu."""
    n = kacinci if kacinci is not None else int(s["zincir_adimi"] or 0) + 1
    return {1: (3, "3. gün takibi"), 2: (4, "7. gün takibi"), 3: (7, "14. gün takibi")}.get(n)


def zincir_sifirla_gerekirse(s, kanal):
    """Video kendi zincirini yuruyor ve yazili zinciri kapatiyor. Video ilk kez
    gidiyorsa sayac sifirlanir, yoksa video zinciri ortadan basliyor."""
    if kanal == "video" and s.get("son_temas_kanali") != "video":
        s["zincir_adimi"] = "0"


# Video zinciri yazili zincirden ayri: video, +2 sesli mesaj, +4 arama,
# +5 tek satir, +7 ayrilik. Gunler burada da goreli.
def video_gunu(kacinci):
    return {1: (2, "Instagram sesli mesaj takibi"),
            2: (2, "telefon, ara"),
            3: (1, "tek satır, yeni soru taşısın"),
            4: (2, "ayrılık mesajı")}.get(kacinci)


SONUC_KELIME = {"açmadı": "acmadi", "acmadi": "acmadi", "gönderdim": "gonderdim", "gonderdim": "gonderdim",
                "istemedi": "istemedi", "ilgilendi": "ilgilendi", "randevu": "randevu", "sonra": "sonra",
                "cevap": "cevap", "izlendi": "izlendi", "izledi": "izlendi",
                "acildi": "izlendi", "açıldı": "izlendi"}

# Yazili kanalda gelen cevabin hangi dala girdigi. Dal adi kaydediliyor ki
# hangi dalin gorusmeye dondugu sonradan sayilabilsin.
CEVAP_DALLARI = ["fiyat", "bilgi", "mesgul", "zaten var", "kim", "referans",
                 "ilgilenmiyor", "sonra", "olumlu", "anlasilmadi"]


def kmt_sonuclar(a):
    satirlar = yukle()
    p = Path(a.dosya)
    if not p.exists():
        hata("dosya yok: %s" % a.dosya)
    metin = p.read_text(encoding="utf-8-sig")
    islenen, bulunamayan, anlasilmayan = [], [], []
    dokum = {}
    for satir in metin.splitlines():
        try:
            satir = satir.strip()
            if not satir or satir.lower().startswith("founderos"):
                continue
            parca = [x.strip() for x in satir.split("|")]
            if len(parca) < 3:
                anlasilmayan.append(satir)
                continue
            ad, kanal, sonuc = parca[0], kucult(parca[1]), kucult(parca[2])
            kod = SONUC_KELIME.get(sonuc)
            if kanal == "eposta":
                kanal = "e-posta"
            if not kod or kanal not in KANALLAR:
                anlasilmayan.append(satir)
                continue
            ek = {}
            for x in parca[3:]:
                if ":" in x:
                    k, v = x.split(":", 1)
                    ek[kucult(k)] = v.strip()
            try:
                s = satir_bul(satirlar, ad)
            except SystemExit:
                bulunamayan.append(ad)
                continue
            notu = ek.get("not", "")
            if kod == "acmadi":
                # Telefon uc ayri gunde acilmazsa hat kapanir ve sira yaziya gecer.
                # Once sonsuza kadar "tekrar ara" yaziyordu, aday hic kapanmiyordu.
                if kanal == "telefon":
                    n_ac = int(s["acmadi_sayisi"] or 0) + 1
                    s["acmadi_sayisi"] = str(n_ac)
                    if n_ac >= 3:
                        if s["eposta"]:
                            temas_uygula(satirlar, s, kanal, "açmadı (üçüncü), telefon kapandı", "kapandı",
                                         None, "e-posta, ilk mesaj", "+1", None, notu)
                        elif s["instagram"]:
                            temas_uygula(satirlar, s, kanal, "açmadı (üçüncü), telefon kapandı", "kapandı",
                                         None, "instagram, ilk mesaj", "+1", None, notu)
                        else:
                            temas_uygula(satirlar, s, kanal, "açmadı (üçüncü), başka kanal yok", "kapandı",
                                         "sonra", "doksan gün sonra yeniden bak", "+90", None, notu)
                        islenen.append(ozet_satir(s))
                        dokum[kod] = dokum.get(kod, 0) + 1
                        continue
                temas_uygula(satirlar, s, kanal, "açmadı", "yapıldı", None, kanal + ", tekrar ara", "+1", None, notu)
            elif kod == "gonderdim":
                # Zincir adimi burada elle artiyor, cunku tarih verildigi icin
                # temas_uygula'nin zincir blogu calismiyor.
                zincir_sifirla_gerekirse(s, kanal)
                adim = int(s["zincir_adimi"] or 0) + 1
                s["zincir_adimi"] = str(adim)
                g = video_gunu(adim) if kanal == "video" else takip_gunu(s, adim)
                if g:
                    onek = "" if kanal == "video" else "%s, " % kanal
                    temas_uygula(satirlar, s, kanal, "gönderildi", "yapıldı", None, onek + g[1], "+%d" % g[0], None, notu)
                else:
                    temas_uygula(satirlar, s, kanal, "gönderildi, zincir bitti", "yapıldı", "sonra", "", "+90", None, notu)
            elif kod == "istemedi":
                temas_uygula(satirlar, s, kanal, "istemedi", "kapandı", "kapandı", "", "", None, notu)
            elif kod == "ilgilendi":
                temas_uygula(satirlar, s, kanal, "ilgilendi", "cevap geldi", "cevap verdi", kanal + ", 3. gün takibi", "+3", None, notu)
            elif kod == "randevu":
                r = ek.get("randevu", "")
                if not r:
                    anlasilmayan.append(satir + "  (randevu tarihi yok)")
                    continue
                temas_uygula(satirlar, s, kanal, "randevu alındı", "cevap geldi", "randevu", "randevu hazırlığı", r[:10], r, notu)
            elif kod == "izlendi":
                # Loom bildirimi. Temas sayilmaz, cunku yeni bir sey gondermedin;
                # sadece adayin videoyu actigi yaziliyor ve arama one aliniyor.
                if kanal != "video":
                    anlasilmayan.append(satir + "  (izlendi yalnız video kanalında)")
                    continue
                s["video_durumu"] = "izlendi"
                s["siradaki_hareket"] = "telefon, videoyu açmış, ara"
                s["siradaki_tarih"] = tarih_coz("+1", "sıradaki tarih")
                if notu:
                    s["not"] = ((s["not"] + " | ") if s["not"] else "") + notu
            elif kod == "sonra":
                t = ek.get("tarih", "+7")
                temas_uygula(satirlar, s, kanal, "sonra ara dedi", "yapıldı", "sonra", kanal + ", tekrar ara", t, None, notu)
            elif kod == "cevap":
                # Gelen cevabin kendisi kaydediliyor: yaniti FounderOS bundan yaziyor
                # ve hangi dal oldugu sayilabiliyor. Cevap gelen aday ayni gun donulur.
                metin = ek.get("metin") or ek.get("cevap") or ""
                dal = kucult(ek.get("dal", ""))
                if dal and dal not in CEVAP_DALLARI:
                    dal = ""
                s["son_cevap"] = metin[:500]
                if dal:
                    s["cevap_dali"] = dal
                temas_uygula(satirlar, s, kanal, "cevap geldi" + (" (%s)" % dal if dal else ""),
                             "cevap geldi", "cevap verdi", kanal + ", yanıt yaz", bugun().isoformat(), None, notu)
            islenen.append(ozet_satir(s))
            dokum[kod] = dokum.get(kod, 0) + 1
        except SystemExit:
            # Tek bozuk satir butun gunu cope atmasin: o satir "anlasilmayan"
            # listesine gider, kalanlar islenir ve dosya yine kaydedilir.
            anlasilmayan.append(satir + "  (işlenemedi)")
        except Exception as e:
            anlasilmayan.append(satir + ("  (işlenemedi: %s)" % e))
    kaydet(satirlar)
    print("işlenen %d, bulunamayan %d, anlaşılmayan %d" % (len(islenen), len(bulunamayan), len(anlasilmayan)))
    n = nis_oku()
    print("gün dökümü: niş %s, açılış sürümü %s, temas %d, %s" % (
        n.get("ad") or "yazılmamış", n.get("acilis_surumu") or "1", len(islenen),
        ", ".join("%s %d" % (k, dokum[k]) for k in ("acmadi", "gonderdim", "izlendi", "istemedi", "ilgilendi", "randevu", "sonra", "cevap") if dokum.get(k))))
    for x in islenen:
        print("  " + x)
    if bulunamayan:
        print("bulunamayan (elle bak): " + "; ".join(bulunamayan))
    if anlasilmayan:
        print("anlaşılmayan satırlar (elle işle):")
        for x in anlasilmayan:
            print("  " + x)


def kmt_isaret(a):
    """Toplu arastirmanin sonucunu listeye dagitir.

    Bazi arastirmalar aday basina degil, nis ve sehir basina yapiliyor:
    "bu sehirde bu niste kim eleman ariyor", "kim reklam veriyor". Tek arama
    yapilir, cikan isletme adlari bu komutla listeye isaretlenir. Aday basina
    yuz ayri arama yapmanin anlami yok; ayni sorunun cevabi hepsi icin ayni
    yerden geliyor."""
    p = Path(a.dosya)
    if not p.exists():
        hata("dosya yok: %s" % a.dosya)
    adlar = [x.strip() for x in p.read_text(encoding="utf-8-sig").splitlines() if x.strip()]
    if a.isaret not in TOPLU_ISARET:
        hata("işaret şunlardan biri olmalı: " + ", ".join(TOPLU_ISARET))
    satirlar = yukle()
    bulunan, bulunamayan = [], []
    for ad in adlar:
        k = kucult(ad)
        esler = [s for s in satirlar if kucult(s["kisa_ad"]) == k or kucult(s["ad"]) == k]
        if not esler:
            esler = [s for s in satirlar if k and (k in kucult(s["ad"]) or kucult(s["kisa_ad"]) in k)]
        if len(esler) != 1:
            bulunamayan.append(ad + ("" if not esler else " (%d eşleşme)" % len(esler)))
            continue
        s = esler[0]
        ip = (s["ipuclari"] or "").split()
        if a.isaret not in ip:
            ip.append(a.isaret)
            s["ipuclari"] = " ".join(ip)
        bulunan.append(s["kisa_ad"])
    kaydet(satirlar)
    print("işaret %s: %d adaya yazıldı, %d eşleşmedi" % (a.isaret, len(bulunan), len(bulunamayan)))
    if bulunan:
        print("  " + ", ".join(bulunan[:20]) + (" ..." if len(bulunan) > 20 else ""))
    if bulunamayan:
        print("eşleşmeyen (elle bak): " + "; ".join(bulunamayan[:10]))


def kmt_sil(a):
    satirlar = yukle()
    s = satir_bul(satirlar, a.anahtar, a.semt)
    s["elenme"] = a.sebep
    s["asama"] = "kapandı"
    s["siradaki_hareket"] = ""
    s["siradaki_tarih"] = ""
    kaydet(satirlar)
    print("listeden çıkarıldı (satır duruyor, elenme=%s): %s" % (a.sebep, s["kisa_ad"]))


# Veri servisinin her kayit icin cikardigi isaretlerden kurulan gozlem.
# Bunlar tahmin degil: Google isletme profilinde gorulen seyler. Elle yapilan
# derin denetimin yerine gecmez, ama denetimi yapilmamis adayin mesaji
# gozlemsiz gitmesin diye var. Sira guclu olandan zayifa.
# Toplu arastirmadan gelen isaretler. Aday basina degil, nis ve sehir basina
# tek arama ile bulunuyor ve listeye dagitiliyor. Sadece is_ilani elle yaziliyor;
# reklam_veriyor veri servisinden geliyor ve elle yazilmasi yasak, cunku elle
# yazilan isaretin yaninda "reklam" sutunu bos kaliyor ve kanca dogrulanmamis
# bir cumleyle gidiyor.
TOPLU_ISARET = ["is_ilani"]

IPUCU_GOZLEM = [
 ("is_ilani", "İş ilanı var: telefona bakacak kişi arıyor",
  "Şu an telefona bakacak birini arıyorsunuz, ilanınızı gördüm"),
 ("sikayet_ulasilamiyor", "Yorumlarda telefona ulaşılamadığını yazan bir müşteri var",
  "Google yorumlarınızdan birinde telefona ulaşılamadığı yazıyor"),
 ("sikayet_gelmedi", "Yorumlarda söz verilen gün gelinmediğini yazan bir müşteri var",
  "Google yorumlarınızdan birinde söz verilen gün gelinmediği yazıyor"),
 ("yorum_sikayet", "Son yorumlarda kaçan talebe işaret eden bir yorum var",
  "Google yorumlarınızdan biri yetişilemeyen bir müşteriyi anlatıyor"),
 ("profil_sahipsiz", "Google işletme profili sahiplenilmemiş görünüyor",
  "Google'daki işletme sayfanız sahiplenilmemiş görünüyor"),
 ("aksam_kapali", "Google'da hafta içi kapanış saati 18.00 ve öncesi",
  "Google'da saatleriniz akşam altıda kapanıyor görünüyor"),
 ("saat_yok", "Google profilinde çalışma saati yazmıyor",
  "Google'da çalışma saatiniz yazmıyor"),
 ("site_yok", "Google profilinde site bağlantısı yok",
  "Google'da site bağlantınız görünmüyor"),
 ("hafta_sonu_kapali", "Google'da cumartesi ve pazar kapalı yazıyor",
  "Google'da hafta sonu kapalı görünüyorsunuz"),
 ("instagram_yok", "Sitede ve profilde Instagram hesabı bulunamadı",
  "Instagram hesabınızı bulamadım"),
]


# Reklam kaynagindan gelen, tek basina anlam tasiyan isaret. Bu isletme
# Google Haritalar'da hic cikmadi, sadece reklam verdigi icin biliniyor.
IPUCU_GOZLEM.append(
 ("sadece_reklam", "Reklam veriyor ama Google Haritalar'da bulunamadı",
  "Reklamınızı gördüm ama Google'da işletme sayfanızı bulamadım"))


# Iki isaretin birlikte anlam kazandigi hal: reklama para veriyor ama
# aramaya bakan yok. Tek basina "reklam veriyorsunuz" bir sizinti degil.
IPUCU_BIRLESIK = [
 (("reklam_veriyor", "sikayet_gelmedi"),
  "Reklam veriyor ve yorumlarda söz verilen gün gelinmediği yazıyor",
  "Reklam veriyorsunuz ama yorumlarınızdan birinde söz verilen gün gelinmediği yazıyor"),
 (("reklam_veriyor", "aksam_kapali"),
  "Reklam veriyor ama Google'da akşam altıda kapanıyor",
  "Reklam veriyorsunuz ama Google'da saatleriniz akşam altıda kapanıyor"),
 (("reklam_veriyor", "sikayet_ulasilamiyor"),
  "Reklam veriyor ve yorumlarda ulaşılamadığı yazıyor",
  "Reklam veriyorsunuz ama yorumlarınızdan birinde telefona ulaşılamadığı yazıyor"),
]


# Kanca olmayan, elle bakilmasi gereken isaretler. Yorumda "bina yikilmis",
# "dukkan tasinmis" yaziyorsa aday aranmaz, once dogrulanir.
UYARI_ISARET = ["kapanmis_olabilir"]


def ipucu_gozlem(s):
    """Elle bulgu yoksa isaretlerden tek gozlem cumlesi kurar.
    Doner: (bulgu, kanca) ya da None."""
    ip = set((s.get("ipuclari") or "").split())
    for kodlar, bulgu, kanca in IPUCU_BIRLESIK:
        if all(k in ip for k in kodlar):
            return bulgu, kanca
    for kod, bulgu, kanca in IPUCU_GOZLEM:
        if kod in ip:
            return bulgu, kanca
    return None


def reklam_cumlesi(reklam):
    """'2 aktif reklam, biri 05.01.2026 tarihinden beri' -> telefonda
    soylenebilir tek cumle parcasi."""
    m = re.match(r"^(\d+) aktif reklam(?:, biri (\d{2})\.(\d{2})\.(\d{4}) tarihinden beri)?$", reklam)
    if not m:
        return "Reklam veriyorsunuz"
    adet = int(m.group(1))
    sayi = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş"}.get(adet, str(adet))
    parca = "%s reklamınız yayında" % sayi
    if m.group(4):
        parca = "%s, biri %s.%s.%s tarihinden beri" % (parca, m.group(2), m.group(3), m.group(4))
    # Turkce buyuk harf: "i" -> "I" degil "İ".
    bas = "İ" if parca[0] == "i" else parca[0].upper()
    return bas + parca[1:]


def gozlem(s):
    """Adayin mesajina girecek gozlem ve nereden geldigi.
    Doner: (bulgu, kanca, kaynak) kaynak: 'denetim' | 'profil' | ''."""
    if s.get("bulgu"):
        return s["bulgu"], s.get("kanca") or "", "denetim"
    g = ipucu_gozlem(s)
    if not g:
        return "", "", ""
    bulgu, kanca = g
    # Veri servisi sikayet cumlesini oldugu gibi getiriyorsa genel cumle yerine
    # musterinin kendi cumlesi kullanilir. Kendi cumlesi her zaman daha guclu.
    alinti = (s.get("yorum_alinti") or "").strip()
    ip = set((s.get("ipuclari") or "").split())
    if alinti and ("yorum_sikayet" in ip or "sikayet_ulasilamiyor" in ip
                   or "sikayet_gelmedi" in ip):
        kisa = alinti if len(alinti) <= 140 else alinti[:137].rstrip() + "..."
        bulgu = "Yorumda yazıyor: " + kisa
        kanca = "Google yorumlarınızdan birinde şöyle yazıyor: \"%s\"" % kisa
    # Reklam sutunu doluysa genel "reklam veriyorsunuz" yerine adet ve tarih
    # soylenir. Rakam tahmin degil, kutuphanenin kendi kaydi.
    reklam = (s.get("reklam") or "").strip()
    if reklam and "reklam_veriyor" in ip:
        kanca = kanca.replace("Reklam veriyorsunuz", reklam_cumlesi(reklam), 1)
        if "reklam" not in bulgu.lower():
            bulgu = (bulgu + " · " + reklam) if bulgu else reklam
    return bulgu, kanca, "profil"


def acik(s):
    return not s["elenme"] and s["asama"] not in ("kapandı", "müşteri")


def kmt_yuz_sec(a):
    """En cok istenen yuzu listeden secer.
    Sira: reklam veren, sonra sizinti puani, sonra yorum sayisi. Elle 'evet'
    yazilmis satirlar korunur; secim onlarin ustune yenisini ekler.
    Reklam veren once geliyor cunku parasini zaten harciyor ve talep akisi var."""
    satirlar = yukle()
    acik_satirlar = [s for s in satirlar if acik(s)]
    zaten = [s for s in acik_satirlar if s["yuz"]]
    aday = [s for s in acik_satirlar if not s["yuz"]]

    # Metindeki bes olcut, ayni sirayla. Yorum sayisi ust sinirin ustundeyse
    # aday listeden atilmaz, yuzun sonuna konur: buyuk isletmede karar tek
    # kiside olmuyor ve ilk aramalar onlarla yapilmiyor.
    ust_sinir = a.yorum_ust_siniri

    def anahtar(s):
        ip = (s.get("ipuclari") or "").split()
        yorum = int(s["yorum_sayisi"] or 0)
        return (
            1 if yorum > ust_sinir else 0,          # buyukler sona
            -(1 if "is_ilani" in ip else 0),        # 1. ilan verenler
            -(1 if "reklam_veriyor" in ip else 0),  # 2. reklam verenler
            -int(s["sizinti"] or 0),
            -yorum,                                 # 3. buyukler, sinirin altinda
            0 if (s["site"] and s["instagram"]) else 1,  # 4. ulasilabilir olanlar
        )

    aday.sort(key=anahtar)
    kalan = max(0, a.sayi - len(zaten))
    secilen = aday[:kalan]
    for s in secilen:
        s["yuz"] = "evet"
    kaydet(satirlar)
    def say(kod):
        return sum(1 for s in secilen if kod in (s.get("ipuclari") or "").split())

    buyuk = sum(1 for s in secilen if int(s["yorum_sayisi"] or 0) > ust_sinir)
    print("en çok istenen yüz: zaten işaretli %d, yeni seçilen %d (ilan veren %d, reklam veren %d), toplam %d"
          % (len(zaten), len(secilen), say("is_ilani"), say("reklam_veriyor"),
             len(zaten) + len(secilen)))
    if buyuk:
        print("bunlardan %d tanesi yorum sayısı %d üstü: listenin sonuna konuldu, ilk aramalar onlarla yapılmaz"
              % (buyuk, ust_sinir))
    if kalan and len(secilen) < kalan:
        print("liste yetmedi: %d kişilik yer boş kaldı, yeni çekim gerekiyor" % (kalan - len(secilen)))


def kmt_bugun(a):
    satirlar = yukle()
    g = bugun().isoformat()
    acik_satirlar = [s for s in satirlar if acik(s)]

    def puan(s):
        return (int(s["sizinti"] or 0), int(s["yorum_sayisi"] or 0))

    # Reklam veren isletme parasini zaten harciyor ve talep akisi var. Denetimi
    # yapilmamis adaylar arasinda once onunla konusulur.
    def reklamli(s):
        return 1 if "reklam_veriyor" in (s.get("ipuclari") or "").split() else 0

    cevap = [s for s in acik_satirlar if s["asama"] in ("cevap verdi", "randevu") and (not s["siradaki_tarih"] or s["siradaki_tarih"][:10] <= g)]
    takip = [s for s in acik_satirlar if s not in cevap and s["siradaki_tarih"] and s["siradaki_tarih"][:10] <= g]
    hazir = [s for s in acik_satirlar if s not in cevap and s not in takip and s["sizinti"] != "" and not s["son_temas_tarihi"]]
    denetsiz = [s for s in acik_satirlar if s not in cevap and s not in takip and s not in hazir and s["sizinti"] == "" and not s["son_temas_tarihi"]]
    cevap.sort(key=lambda s: s["siradaki_tarih"] or "")
    takip.sort(key=lambda s: (s["siradaki_tarih"], -puan(s)[0]))
    hazir.sort(key=lambda s: (-int(bool(s["yuz"])), -puan(s)[0], -reklamli(s), -puan(s)[1]))
    denetsiz.sort(key=lambda s: (-int(bool(s["yuz"])), -reklamli(s), -puan(s)[1]))
    n = a.sayi
    liste = (cevap + takip + hazir + denetsiz)[:n]
    gozlemsiz = sum(1 for s in liste if not gozlem(s)[0])
    print("bugün %s: cevap verenler %d, takibi gelen %d, denetimi hazır %d, denetimsiz %d; ilk %d gösteriliyor%s" %
          (g, len(cevap), len(takip), len(hazir), len(denetsiz), len(liste),
           (", %d adayda gözlem yok" % gozlemsiz) if gozlemsiz else ", hepsinde gözlem var"))
    if a.planla:
        kanal = "telefon" if (a.kanal or "telefon") == "telefon" else "yazı"
        sayac = 0
        for s in liste:
            if not s["siradaki_tarih"]:
                s["siradaki_hareket"] = "ilk temas, " + kanal
                s["siradaki_tarih"] = g
                sayac += 1
        kaydet(satirlar)
        print("planlandı: %d adayın sıradaki tarihi bugüne yazıldı, sayfa yenilendi" % sayac)
    baslik = "grup | işletme | telefon | sahibi | sızıntı | aşama | son temas | sıradaki | bulgu"
    print(baslik)
    for s in liste:
        grup = "cevap" if s in cevap else "takip" if s in takip else "hazır" if s in hazir else "denetimsiz"
        print(grup + " | " + ozet_satir(s))


def kmt_ozet(a):
    satirlar = yukle()
    g = bugun().isoformat()
    canli = [s for s in satirlar if not s["elenme"]]
    say = lambda f: sum(1 for s in canli if f(s))
    print("toplam %d (elenen %d)" % (len(canli), len(satirlar) - len(canli)))
    print("telefonlu %d, e-postalı %d, instagramlı %d" % (say(lambda s: s["telefon"]), say(lambda s: s["eposta"]), say(lambda s: s["instagram"])))
    print("en çok istenen yüz %d, denetlenmiş %d, hiç aranmamış %d" % (say(lambda s: s["yuz"]), say(lambda s: s["sizinti"] != ""), say(lambda s: not s["son_temas_tarihi"] and acik(s))))
    print("bugün sırada %d, gecikmiş %d" % (say(lambda s: acik(s) and s["siradaki_tarih"][:10] == g), say(lambda s: acik(s) and s["siradaki_tarih"] and s["siradaki_tarih"][:10] < g)))
    dag = {}
    for s in canli:
        dag[s["asama"] or "yeni"] = dag.get(s["asama"] or "yeni", 0) + 1
    print("aşama: " + ", ".join("%s %d" % (k, dag[k]) for k in ASAMALAR if k in dag))
    kaynaklar = {"denetim": 0, "profil": 0, "": 0}
    for s in canli:
        if acik(s):
            kaynaklar[gozlem(s)[2]] += 1
    print("gözlem: denetimden %d, profilden %d, gözlemsiz %d" %
          (kaynaklar["denetim"], kaynaklar["profil"], kaynaklar[""]))
    bugun_temas = say(lambda s: s["son_temas_tarihi"] == g)
    print("bugün temas edilen %d, toplam temas %d" % (bugun_temas, sum(int(s["temas_sayisi"] or 0) for s in canli)))
    n = nis_oku()
    if n.get("ad"):
        print("niş %s, açılış sürümü %s" % (n["ad"], n.get("acilis_surumu") or "1"))
    if canli:
        print("son eklenme %s, kaynaklar: %s" % (max(s["eklenme_tarihi"] for s in canli), ", ".join(sorted({s["kaynak"] for s in canli if s["kaynak"]}))))
    # Stok: liste bitmeden once haber ver. Takvimle degil stokla tetikleniyor,
    # cunku listenin ne zaman bitecegi tempoya bagli.
    dokunulmamis = say(lambda s: acik(s) and not s["son_temas_tarihi"])
    tempo = 0
    try:
        tempo = int(str(n.get("gunluk_temas") or "").strip() or 0)
    except ValueError:
        tempo = 0
    if tempo > 0:
        gun_kaldi = dokunulmamis / float(tempo)
        satir = "stok: %d dokunulmamış aday, günde %d temasla %.1f gün" % (dokunulmamis, tempo, gun_kaldi)
        if gun_kaldi < 5:
            satir += "  >>> liste bitiyor, yeni ilçe çekilmeli"
        print(satir)
    else:
        print("stok: %d dokunulmamış aday (günlük tempo sayfa.json'a yazılmamış, gün hesabı yapılamadı)" % dokunulmamis)


def cevap_verdi(s):
    """Bu aday bir sekilde cevap verdi mi. Asama ileri gittiyse ya da cevap
    kaydedildiyse evet; "sonra" da cevaptir, sessizlik degildir."""
    return bool(s["son_cevap"]) or s["asama"] in ("cevap verdi", "randevu", "görüşüldü", "müşteri", "sonra")


def kmt_ogren(a):
    """Hangi gozlem ve hangi kanal cevap getiriyor.
    Esik altindaki kova sayilmaz: az sayida temastan cikan oran yaniltir."""
    satirlar = yukle()
    esik = a.esik
    temasli = [s for s in satirlar if not s["elenme"] and s["son_temas_tarihi"]]
    if not temasli:
        print("henüz temas yok, öğrenilecek bir şey de yok")
        return

    def dok(baslik, anahtar_fn):
        kova = {}
        for s in temasli:
            k = anahtar_fn(s)
            if k is None:
                continue
            d = kova.setdefault(k, [0, 0])
            d[0] += 1
            if cevap_verdi(s):
                d[1] += 1
        if not kova:
            return
        print(baslik)
        for k in sorted(kova, key=lambda x: -kova[x][0]):
            n, c = kova[k]
            if n < esik:
                print("  %-28s %3d temas, eşik altı (%d gerekiyor), sayılmıyor" % (k, n, esik))
            else:
                print("  %-28s %3d temas, %3d cevap, %%%.0f" % (k, n, c, 100.0 * c / n))

    print("öğrenme özeti, eşik %d temas. Eşiğin altındaki satır karar için kullanılmaz." % esik)
    dok("gözlemin kaynağı:", lambda s: {"denetim": "denetimden gelen bulgu",
                                        "profil": "profilden gelen gözlem",
                                        "": "gözlemsiz"}[gozlem(s)[2]])
    dok("son temas kanalı:", lambda s: s["son_temas_kanali"] or None)
    dok("profil işareti:", lambda s: (ipucu_gozlem(s) or (None, None))[0] if gozlem(s)[2] == "profil" else None)
    dok("sızıntı puanı:", lambda s: ("sızıntı " + s["sizinti"]) if s["sizinti"] else None)

    daller = {}
    for s in temasli:
        if s["cevap_dali"]:
            d = daller.setdefault(s["cevap_dali"], [0, 0])
            d[0] += 1
            if s["asama"] in ("randevu", "görüşüldü", "müşteri"):
                d[1] += 1
    if daller:
        print("cevap dalı, randevuya dönen:")
        for k in sorted(daller, key=lambda x: -daller[x][0]):
            n, r = daller[k]
            print("  %-28s %3d cevap, %3d randevu%s" % (k, n, r, "" if n >= esik else "  (eşik altı)"))

    n = nis_oku()
    if n.get("ad"):
        print("niş %s, açılış sürümü %s. Açılış metni değişirse sürüm artar ve bu tablo o sürümden sonrasını ayrı sayar."
              % (n["ad"], n.get("acilis_surumu") or "1"))


def kmt_bul(a):
    satirlar = yukle()
    k = kucult(a.metin)
    t = rakam(a.metin)
    esle = [s for s in satirlar if k in kucult(s["kisa_ad"]) or k in kucult(s["ad"]) or k in kucult(s["sahibi"]) or k in kucult(s["semt"]) or (t and t in rakam(s["telefon"]))]
    print("%d eşleşme" % len(esle))
    for s in esle[:20]:
        print(ozet_satir(s) + (" | ELENDİ: " + s["elenme"] if s["elenme"] else "") + (" | not: " + s["not"] if s["not"] else ""))


SENARYO_ALANLAR = ["ad", "acilis_surumu", "ogrenci", "acilis_sorusu", "isleyis_sorusu", "vaat", "calisan", "gunluk_temas", "itirazlar"]
ITIRAZ_ALANLAR = ["durum", "soyle", "neden", "sonra"]


def senaryo_dogrula(n):
    """sayfa.json içeriğini süzer: bilinmeyen alan düşer, itirazlar sözlük listesine çevrilir."""
    c = {}
    for k in SENARYO_ALANLAR:
        if k not in n:
            continue
        v = n[k]
        if k == "ogrenci":
            if isinstance(v, dict):
                c[k] = {x: str(v.get(x, "")).strip() for x in ("ad", "sehir", "sistem_adi")}
        elif k == "itirazlar":
            l = []
            for x in (v if isinstance(v, list) else []):
                if isinstance(x, str) and x.strip():
                    l.append({"durum": x.strip(), "soyle": "", "neden": "", "sonra": ""})
                elif isinstance(x, dict) and str(x.get("durum", "")).strip():
                    l.append({y: str(x.get(y, "")).strip() for y in ITIRAZ_ALANLAR})
            c[k] = l
        else:
            c[k] = str(v).strip()
    # eski alan adı
    if "acilis" in n and "acilis_sorusu" not in c:
        c["acilis_sorusu"] = str(n["acilis"]).strip()
    return c


def kart_oku(metin):
    """Niş kartının "Telefonda söylenecekler" bölümünü (olduğu gibi kopyalanmış metin) senaryoya çevirir."""
    n = {}
    satirlar = metin.replace("\r\n", "\n").split("\n")
    for s in satirlar:
        t = s.strip()
        if not t:
            continue
        if t.startswith("# ") and "ad" not in n:
            n["ad"] = t[2:].strip()
            continue
        for etiket, alan in (("Açılış sürümü:", "acilis_surumu"), ("Açılış sorusu:", "acilis_sorusu"),
                             ("İşleyiş sorusu:", "isleyis_sorusu"),
                             ("Ne yaptığın:", "vaat"), ("Çalışan açarsa:", "calisan")):
            if t.startswith(etiket):
                n[alan] = t[len(etiket):].strip().strip('"').strip()
        if t.startswith('- "') and "Söyle:" in t:
            e = re.match(r'-\s*"(?P<durum>[^"]+)"\s*Söyle:\s*"(?P<soyle>[^"]*(?:"[^"]*"[^"]*)*?)"\s*(?:Ne için:\s*(?P<neden>.*?))?\s*(?:Sonra:\s*(?P<sonra>.*))?$', t)
            if not e:
                continue
            n.setdefault("itirazlar", []).append({"durum": e.group("durum").strip(), "soyle": e.group("soyle").strip(),
                                                 "neden": (e.group("neden") or "").strip(), "sonra": (e.group("sonra") or "").strip()})
    return n


def kmt_sayfa(a):
    degisti = False
    n = senaryo_dogrula(nis_oku())
    if a.dosya:
        try:
            g = json.loads(Path(a.dosya).read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            hata("senaryo dosyası okunamadı: %s" % e)
        if not isinstance(g, dict):
            hata("senaryo dosyası bir sözlük olmalı")
        n.update(senaryo_dogrula(g))
        degisti = True
    if a.kart:
        try:
            g = kart_oku(Path(a.kart).read_text(encoding="utf-8"))
        except OSError as e:
            hata("kart dosyası okunamadı: %s" % e)
        if not g.get("acilis_sorusu") and not g.get("itirazlar"):
            hata("kart dosyasında 'Açılış sorusu:' ya da '- \"...\" Söyle:' satırı yok; niş kartının Telefonda söylenecekler bölümünü olduğu gibi kopyala")
        n.update(senaryo_dogrula(g))
        degisti = True
    if a.nis:
        n["ad"] = a.nis; degisti = True
    if a.ogrenci_ad or a.sehir or a.sistem_adi:
        o = n.get("ogrenci", {"ad": "", "sehir": "", "sistem_adi": ""})
        if a.ogrenci_ad:
            o["ad"] = a.ogrenci_ad
        if a.sehir:
            o["sehir"] = a.sehir
        if a.sistem_adi:
            o["sistem_adi"] = a.sistem_adi
        n["ogrenci"] = o; degisti = True
    if a.acilis:
        n["acilis_sorusu"] = a.acilis; degisti = True
    if a.itiraz:
        n["itirazlar"] = senaryo_dogrula({"itirazlar": a.itiraz})["itirazlar"]; degisti = True
    if degisti:
        calisma().mkdir(parents=True, exist_ok=True)
        (calisma() / "sayfa.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")
    if not (KLASOR / "adaylar.csv").exists():
        kaydet([], sayfa_da=False)
    sayfa_uret()
    h = KLASOR / "adaylar.html"
    eksik = []
    o = n.get("ogrenci") or {}
    if not o.get("ad") or not o.get("sehir"):
        eksik.append("öğrencinin adı ve şehri")
    if not n.get("acilis_sorusu"):
        eksik.append("açılış sorusu")
    if not n.get("itirazlar"):
        eksik.append("nişe özel itirazlar")
    print("sayfa yenilendi: adaylar.html (%d bayt), %s" % (h.stat().st_size, simdi_metin()))
    if eksik:
        print("eksik senaryo bilgisi: " + ", ".join(eksik) + " (sayfa --dosya ile ver; Saha modu o zamana kadar genel metinle çalışır)")


def ana():
    p = argparse.ArgumentParser(description="FounderOS aday listesi aracı")
    p.add_argument("--klasor", help="öğrencinin klasörü (varsayılan: bulunulan klasör)")
    alt = p.add_subparsers(dest="komut")

    c = alt.add_parser("cek")
    c.add_argument("--is", dest="is_id", type=int, required=True)
    c.add_argument("--anahtar")
    c.add_argument("--adres")
    c.add_argument("--ozet", action="store_true")
    c.add_argument("--kaynak")
    c.add_argument("--tut", action="append")
    c.add_argument("--kategori-disi", dest="kategori_disi", action="append")

    e = alt.add_parser("ekle")
    e.add_argument("dosya")
    e.add_argument("--kaynak")
    e.add_argument("--baglayan")
    e.add_argument("--tut", action="append")
    e.add_argument("--kategori-disi", dest="kategori_disi", action="append")
    e.add_argument("--yuz", action="store_true")

    g = alt.add_parser("guncelle")
    g.add_argument("anahtar")
    g.add_argument("alanlar", nargs="*")
    g.add_argument("--semt")

    t = alt.add_parser("temas")
    t.add_argument("anahtar")
    t.add_argument("--kanal", required=True)
    t.add_argument("--sonuc", default="")
    t.add_argument("--durum")
    t.add_argument("--asama")
    t.add_argument("--siradaki")
    t.add_argument("--tarih")
    t.add_argument("--randevu")
    t.add_argument("--not", dest="notu")
    t.add_argument("--semt")

    s = alt.add_parser("ogren"); s.add_argument("--esik", type=int, default=30)
    s = alt.add_parser("isaret"); s.add_argument("dosya"); s.add_argument("--isaret", required=True)
    s = alt.add_parser("sonuclar")
    s.add_argument("dosya")

    d = alt.add_parser("sil")
    d.add_argument("anahtar")
    d.add_argument("--sebep", required=True)
    d.add_argument("--semt")

    b = alt.add_parser("bugun")
    b.add_argument("--sayi", type=int, default=100)
    b.add_argument("--planla", action="store_true")
    b.add_argument("--kanal")

    ys = alt.add_parser("yuz-sec")
    ys.add_argument("--sayi", type=int, default=100)
    ys.add_argument("--yorum-ust-siniri", dest="yorum_ust_siniri", type=int, default=300)

    alt.add_parser("ozet")
    f = alt.add_parser("bul")
    f.add_argument("metin")

    y = alt.add_parser("sayfa")
    y.add_argument("--dosya", help="senaryo JSON dosyası (ad, ogrenci, acilis_sorusu, isleyis_sorusu, vaat, calisan, itirazlar)")
    y.add_argument("--kart", help="niş kartının Telefonda söylenecekler bölümü, olduğu gibi kopyalanmış .md dosyası")
    y.add_argument("--nis")
    y.add_argument("--ogrenci-ad", dest="ogrenci_ad")
    y.add_argument("--sehir")
    y.add_argument("--sistem-adi", dest="sistem_adi")
    y.add_argument("--acilis")
    y.add_argument("--itiraz", action="append")

    alt.add_parser("surum")

    a = p.parse_args()
    global KLASOR
    if a.klasor:
        KLASOR = Path(a.klasor)
    if not a.komut:
        p.print_help()
        return
    if a.komut == "surum":
        print(SURUM)
        return
    if not KLASOR.exists():
        hata("klasör yok: %s" % KLASOR)
    calisma().mkdir(parents=True, exist_ok=True)
    {"cek": kmt_cek, "ekle": kmt_ekle, "guncelle": kmt_guncelle, "temas": kmt_temas, "sonuclar": kmt_sonuclar, "ogren": kmt_ogren, "isaret": kmt_isaret,
     "sil": kmt_sil, "bugun": kmt_bugun, "yuz-sec": kmt_yuz_sec, "ozet": kmt_ozet,
     "bul": kmt_bul, "sayfa": kmt_sayfa}[a.komut](a)


if __name__ == "__main__":
    ana()
