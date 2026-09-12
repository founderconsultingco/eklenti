---
user-invocable: false
name: aday-listesi-araci
description: "Aday listesi aracinin kurulum dosyalari: adaylar-arac.py ve adaylar-sablon.html, ham dosya olarak bu klasorde ve gomulu olarak icinde. Sadece aday listesi ilk kez cikarken (.founderos klasoru yokken) ve aracin surumu eskiyken acilir; kullanim kurallari aday-listesi-dosyasi'nda."
---

# Aday listesi aracı (kurulum dosyaları)

Bu beceri iki dosya taşır: `adaylar-arac.py` (aday listesi aracı) ve `adaylar-sablon.html` (sayfa şablonu). İkisi bu becerinin klasöründe ham dosya olarak durur; aşağıda da birebir kopyaları var. Kullanım kuralları aday-listesi-dosyasi becerisinde; burası yalnız kurulum ve güncelleme içindir.

Ne zaman açılır: aday listesi ilk kez çıkarılırken (`.founderos/` klasörü yokken) ve `python3 .founderos/adaylar-arac.py surum` çıktısı buradaki sürümden küçükken.

Kurulum:
1. Öğrencinin klasöründe `.founderos` adlı klasörü aç.
2. Beceri klasöründeki `adaylar-arac.py` ve `adaylar-sablon.html` dosyalarını oraya kopyala (beceri açıldığında klasör yolu görünür; `cp "<beceri klasörü>/adaylar-arac.py" "<öğrenci klasörü>/.founderos/"` biçiminde). Kopyalama çalışmazsa aşağıdaki iki bloğu aynı adlarla, kısaltmadan, değiştirmeden yaz.
3. Öğrencinin klasörünün içinde `python3 .founderos/adaylar-arac.py surum` çalıştır. Beklenen çıktı aşağıdaki sürüm. Gelmiyorsa dosya kesik kopyalanmıştır, yeniden yap.
4. Sayfa şablonunun `</html>` ile bittiğini kontrol et.
5. Kurulum ilk kezse ya da sürüm yükseldiyse senaryoyu yeniden yaz: aday-listesi-dosyasi'ndaki kurulum 3. adımı (`sayfa --kart .founderos/telefon.md --ogrenci-ad ... --sehir ...`). Eski `sayfa.json` bozulmaz, araç eski alanları tanır.

Öğrenci bu klasörü ve dosyaları görmez, ona anlatılmaz. Komutlar sohbete yazılmaz.

Aracın sürümü: 0.28.0

## `adaylar-arac.py` (birebir)

````python
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
  isaret DOSYA --isaret A   (toplu araştırmanın sonucu: is_ilani, reklam_veriyor; her satır bir işletme adı)
  sil ANAHTAR --sebep "..."  (satırı elenme ile işaretler, silmez)
  bugun [--sayi N] [--planla] [--kanal telefon|yazı]
  ozet
  bul METIN
  sayfa [--kart TELEFON.md | --dosya SENARYO.json] [--nis AD] [--ogrenci-ad AD --sehir S --sistem-adi AD] [--acilis "..."] [--itiraz "..."]...
                            (Saha modu kartının söyle metni: niş kartının "Telefonda söylenecekler" bölümü ve öğrencinin adı, şehri)
  surum
"""
import argparse, csv, datetime, io, json, os, re, shutil, sys, unicodedata
from pathlib import Path

SURUM = "0.28.0"
IST = datetime.timezone(datetime.timedelta(hours=3))

SERVIS = ["kisa_ad", "ad", "telefon", "eposta", "instagram", "site", "adres", "semt",
          "yorum_sayisi", "puan", "kategori", "ipuclari", "elenme", "harita"]
EKLENEN = ["eklenme_tarihi", "kaynak", "baglayan", "yuz", "sahibi", "uygunluk", "sizinti",
           "bulgu", "kanca", "lira", "denetim_tarihi", "asama", "telefon_durumu",
           "eposta_durumu", "instagram_durumu", "video_durumu", "temas_sayisi",
           "son_temas_tarihi", "son_temas_kanali", "siradaki_hareket", "siradaki_tarih",
           "randevu_tarihi", "eposta_konu", "eposta_metni", "dm_metni",
           "son_cevap", "cevap_dali", "not"]
SUTUNLAR = SERVIS + EKLENEN
ASAMALAR = ["yeni", "temasta", "cevap verdi", "randevu", "görüşüldü", "sonra", "kapandı", "müşteri"]
DURUMLAR = ["yapılmadı", "yapıldı", "cevap geldi", "kapandı"]
KANALLAR = ["telefon", "e-posta", "instagram", "video"]
KANAL_SUTUN = {"telefon": "telefon_durumu", "e-posta": "eposta_durumu",
               "instagram": "instagram_durumu", "video": "video_durumu"}
KAYNAKLAR = ["haritalar", "iş ilanı", "elle", "tanıdık", "referans"]
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

def yukle():
    p = KLASOR / "adaylar.csv"
    if not p.exists():
        return []
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        okuyucu = csv.DictReader(f)
        bilinmeyen = [b for b in (okuyucu.fieldnames or []) if b and b not in SUTUNLAR]
        if bilinmeyen:
            hata("adaylar.csv'de tanınmayan sütun var: %s. Sütunlar aday-listesi-dosyasi'nda sabittir." % ", ".join(bilinmeyen))
        # Eksik sutun hata degil: eski dosya yeni sutunlarla acilir, bos gelir
        # ve ilk kayitta dosyaya yazilir.
        satirlar = []
        for s in okuyucu:
            satirlar.append({k: (s.get(k) or "").strip() for k in SUTUNLAR})
    return satirlar


def kaydet(satirlar, sayfa_da=True):
    p = KLASOR / "adaylar.csv"
    yedek = calisma() / "yedek"
    yedek.mkdir(parents=True, exist_ok=True)
    if p.exists():
        shutil.copyfile(p, yedek / ("adaylar-" + datetime.datetime.now(IST).strftime("%Y%m%d-%H%M%S") + ".csv"))
        eskiler = sorted(yedek.glob("adaylar-*.csv"))
        for e in eskiler[:-10]:
            try:
                e.unlink()
            except OSError:
                pass
    gecici = p.with_suffix(".csv.tmp")
    with io.open(gecici, "w", encoding="utf-8", newline="") as f:
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


def sayfa_uret(satirlar=None):
    sablon = Path(__file__).resolve().parent / "adaylar-sablon.html"
    if not sablon.exists():
        print("UYARI: sayfa şablonu bulunamadı (%s); sayfa yenilenmedi." % sablon)
        return
    p = KLASOR / "adaylar.csv"
    ham = io.open(p, encoding="utf-8-sig").read() if p.exists() else ""
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
    if sutun in KANAL_SUTUN.values() and deger and deger not in DURUMLAR:
        hata("kanal durumu şunlardan biri olmalı: " + ", ".join(DURUMLAR))
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
    if durum and durum not in DURUMLAR:
        hata("durum şunlardan biri olmalı: " + ", ".join(DURUMLAR))
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
        # temas_sayisi bu fonksiyonun basinda artti; zincirde bu gonderim kacinci
        # ise onu veriyoruz, yoksa bir fazla sayip adimi atliyor.
        g = takip_gunu(s, int(s["temas_sayisi"] or 1))
        if g:
            s["siradaki_hareket"] = "%s, %s" % (kanal, g[1])
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
    """Yazılı kanal zinciri: ilk mesajdan 3, 7 ve 14 gün sonra takip. Bu gönderim kaçıncıysa sıradaki takibin
    kaç gün sonra olduğunu ve adını verir; dördüncü gönderimden sonra zincir biter.
    kacinci verilmezse sayaçtan hesaplanır (temas henüz işlenmemiş kabul edilir)."""
    n = kacinci if kacinci is not None else int(s["temas_sayisi"] or 0) + 1
    return {1: (3, "3. gün takibi"), 2: (4, "7. gün takibi"), 3: (7, "14. gün takibi")}.get(n)


SONUC_KELIME = {"açmadı": "acmadi", "acmadi": "acmadi", "gönderdim": "gonderdim", "gonderdim": "gonderdim",
                "istemedi": "istemedi", "ilgilendi": "ilgilendi", "randevu": "randevu", "sonra": "sonra",
                "cevap": "cevap"}

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
            temas_uygula(satirlar, s, kanal, "açmadı", "yapıldı", None, kanal + ", tekrar ara", "+1", None, notu)
        elif kod == "gonderdim":
            g = takip_gunu(s)
            if g:
                temas_uygula(satirlar, s, kanal, "gönderildi", "yapıldı", None, "%s, %s" % (kanal, g[1]), "+%d" % g[0], None, notu)
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
    kaydet(satirlar)
    print("işlenen %d, bulunamayan %d, anlaşılmayan %d" % (len(islenen), len(bulunamayan), len(anlasilmayan)))
    n = nis_oku()
    print("gün dökümü: niş %s, açılış sürümü %s, temas %d, %s" % (
        n.get("ad") or "yazılmamış", n.get("acilis_surumu") or "1", len(islenen),
        ", ".join("%s %d" % (k, dokum[k]) for k in ("acmadi", "gonderdim", "istemedi", "ilgilendi", "randevu", "sonra", "cevap") if dokum.get(k))))
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
# tek arama ile bulunuyor ve listeye dagitiliyor.
TOPLU_ISARET = ["is_ilani", "reklam_veriyor"]

IPUCU_GOZLEM = [
 ("is_ilani", "İş ilanı var: telefona bakacak kişi arıyor",
  "Şu an telefona bakacak birini arıyorsunuz, ilanınızı gördüm"),
 ("yorum_sikayet", "Son yorumlarda aranıp ulaşılamadığını yazan bir müşteri var",
  "Google yorumlarınızdan birinde 'aradım, açan olmadı' yazıyor"),
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


# Iki isaretin birlikte anlam kazandigi hal: reklama para veriyor ama
# aramaya bakan yok. Tek basina "reklam veriyorsunuz" bir sizinti degil.
IPUCU_BIRLESIK = [
 (("reklam_veriyor", "aksam_kapali"),
  "Reklam veriyor ama Google'da akşam altıda kapanıyor",
  "Reklam veriyorsunuz ama Google'da saatleriniz akşam altıda kapanıyor"),
 (("reklam_veriyor", "yorum_sikayet"),
  "Reklam veriyor ve yorumlarda ulaşılamadığı yazıyor",
  "Reklam veriyorsunuz ama yorumlarınızdan birinde 'aradım açan olmadı' yazıyor"),
]


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


def gozlem(s):
    """Adayin mesajina girecek gozlem ve nereden geldigi.
    Doner: (bulgu, kanca, kaynak) kaynak: 'denetim' | 'profil' | ''."""
    if s.get("bulgu"):
        return s["bulgu"], s.get("kanca") or "", "denetim"
    g = ipucu_gozlem(s)
    if g:
        return g[0], g[1], "profil"
    return "", "", ""


def acik(s):
    return not s["elenme"] and s["asama"] not in ("kapandı", "müşteri")


def kmt_bugun(a):
    satirlar = yukle()
    g = bugun().isoformat()
    acik_satirlar = [s for s in satirlar if acik(s)]

    def puan(s):
        return (int(s["sizinti"] or 0), int(s["yorum_sayisi"] or 0))

    cevap = [s for s in acik_satirlar if s["asama"] in ("cevap verdi", "randevu") and (not s["siradaki_tarih"] or s["siradaki_tarih"][:10] <= g)]
    takip = [s for s in acik_satirlar if s not in cevap and s["siradaki_tarih"] and s["siradaki_tarih"][:10] <= g]
    hazir = [s for s in acik_satirlar if s not in cevap and s not in takip and s["sizinti"] != "" and not s["son_temas_tarihi"]]
    denetsiz = [s for s in acik_satirlar if s not in cevap and s not in takip and s not in hazir and s["sizinti"] == "" and not s["son_temas_tarihi"]]
    cevap.sort(key=lambda s: s["siradaki_tarih"] or "")
    takip.sort(key=lambda s: (s["siradaki_tarih"], -puan(s)[0]))
    hazir.sort(key=lambda s: (-int(bool(s["yuz"])), -puan(s)[0], -puan(s)[1]))
    denetsiz.sort(key=lambda s: (-int(bool(s["yuz"])), -puan(s)[1]))
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
     "sil": kmt_sil, "bugun": kmt_bugun, "ozet": kmt_ozet, "bul": kmt_bul, "sayfa": kmt_sayfa}[a.komut](a)


if __name__ == "__main__":
    ana()
````

## `adaylar-sablon.html` (birebir)

````html
<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aday Listesi</title>
<style>
:root{--m:#111;--g:#6b7280;--l:#e5e7eb;--bg:#f7f7f5;--w:#fff;--a:#0f6b3a;--r:#b42318;--o:#b54708;--b:#1d4ed8}
*{box-sizing:border-box}
body{margin:0;font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--m);background:var(--bg)}
header{background:var(--w);border-bottom:1px solid var(--l);padding:14px 20px;position:sticky;top:0;z-index:5}
h1{font-size:18px;margin:0 0 2px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.sekme{display:inline-flex;border:1px solid var(--l);border-radius:8px;overflow:hidden;font-size:13px;font-weight:500}
.sekme button{border:0;background:var(--w);padding:6px 12px;font:inherit;cursor:pointer;color:var(--m)}
.sekme button.aktif{background:var(--m);color:var(--w)}
.alt{color:var(--g);font-size:13px}
.ozet{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.kutu{background:var(--bg);border:1px solid var(--l);border-radius:8px;padding:6px 10px;min-width:96px}
.kutu b{display:block;font-size:18px}
.kutu span{color:var(--g);font-size:12px}
.arac{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px}
input[type=search]{flex:1;min-width:220px;padding:8px 10px;border:1px solid var(--l);border-radius:8px;font:inherit}
.cip{border:1px solid var(--l);background:var(--w);border-radius:999px;padding:5px 11px;font:inherit;cursor:pointer;color:var(--m)}
.cip.aktif{background:var(--m);color:var(--w);border-color:var(--m)}
.cip small{color:inherit;opacity:.7;margin-left:4px}
main{padding:12px 20px 60px}
table{width:100%;border-collapse:collapse;background:var(--w);border:1px solid var(--l);border-radius:8px;overflow:hidden;font-size:13px}
th{position:sticky;top:0;background:#fafaf9;text-align:left;font-weight:600;padding:8px;border-bottom:1px solid var(--l);cursor:pointer;white-space:nowrap;user-select:none}
th.sirali::after{content:" ↓";color:var(--g)}
th.sirali.ters::after{content:" ↑"}
td{padding:7px 8px;border-bottom:1px solid var(--l);vertical-align:top}
tr.satir{cursor:pointer}
tr.satir:hover td{background:#fbfbfa}
tr.bugun td{background:#f0fdf4}
tr.gecmis td{background:#fff7ed}
tr.detay td{background:#fafaf9;padding:10px 14px 14px}
.ad{font-weight:600}
.kucuk{color:var(--g);font-size:12px}
.rozet{display:inline-block;border-radius:6px;padding:1px 6px;font-size:11px;margin:1px 2px 1px 0;background:#eef0f2;color:#374151;white-space:nowrap}
.rozet.uyari{background:#fef3c7;color:#92400e}
.rozet.iyi{background:#dcfce7;color:#166534}
.rozet.kotu{background:#fee2e2;color:#991b1b}
.rozet.mavi{background:#dbeafe;color:#1e40af}
.rozet.mor{background:#ede9fe;color:#5b21b6}
.puan{font-variant-numeric:tabular-nums}
.nokta{display:inline-block;width:9px;height:9px;border-radius:50%;background:var(--l);margin-right:2px}
.nokta.dolu{background:var(--r)}
.detay-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:8px 18px}
.detay-grid div{font-size:13px}
.detay-grid span{display:block;color:var(--g);font-size:11px;text-transform:uppercase;letter-spacing:.03em}
a{color:var(--b);text-decoration:none}
a:hover{text-decoration:underline}
.bos{padding:40px;text-align:center;color:var(--g);background:var(--w);border:1px dashed var(--l);border-radius:8px}
.gizli{display:none}
td:nth-child(3),td:nth-child(12){white-space:nowrap}
.aciklama{color:var(--g);font-size:12px;margin-top:8px}
.aciklama i{display:inline-block;width:10px;height:10px;border-radius:2px;vertical-align:-1px;margin:0 3px 0 8px}
/* saha modu */
.saha-ust{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 12px}
.saha-ust .kucuk{margin-right:auto}
.dugme{border:1px solid var(--l);background:var(--w);border-radius:8px;padding:7px 12px;font:inherit;cursor:pointer;color:var(--m)}
.dugme.ana{background:var(--a);color:var(--w);border-color:var(--a)}
.dugme.kirmizi{color:var(--r)}
.kart{background:var(--w);border:1px solid var(--l);border-radius:8px;padding:12px 14px;margin-bottom:10px;display:grid;grid-template-columns:minmax(240px,1fr) minmax(300px,1.4fr);grid-template-areas:"oku soyle" "sonuc sonuc";gap:8px 20px}
.kart .oku{grid-area:oku}.kart .soyle-alani{grid-area:soyle;border-left:1px solid var(--l);padding-left:16px}.kart .sonuc-alani{grid-area:sonuc;border-top:1px solid var(--l);padding-top:8px}
.baslik{text-transform:uppercase;letter-spacing:.05em;font-size:11px;margin-bottom:4px}
.modlar{display:flex;flex-wrap:wrap;gap:6px;margin:2px 0 8px}
.modlar button{border:1px solid var(--l);background:var(--w);border-radius:999px;padding:4px 10px;font:inherit;font-size:12px;cursor:pointer;color:var(--m)}
.modlar button.aktif{background:var(--b);color:var(--w);border-color:var(--b)}
.modlar button.itiraz-ac{margin-left:auto;border-color:var(--o);color:var(--o)}
.adimlar{margin:0;padding-left:20px}
.adimlar li{margin:0 0 7px;font-size:14px;line-height:1.5}
.adimlar li span.e{display:block;color:var(--g);font-size:11px;text-transform:uppercase;letter-spacing:.03em}
.adimlar li .kucuk{font-size:12px}
.cekmece{position:fixed;top:0;right:0;bottom:0;width:min(520px,100%);background:var(--w);border-left:1px solid var(--l);box-shadow:-8px 0 24px rgba(0,0,0,.08);padding:14px 18px 40px;overflow:auto;transform:translateX(105%);transition:transform .2s;z-index:20;font-size:13px}
.cekmece.acik{transform:none}
.cekmece-ust{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.cekmece-ust b{font-size:15px}
.cekmece details{border:1px solid var(--l);border-radius:8px;padding:6px 10px;margin:0 0 6px;background:var(--bg)}
.cekmece details.ozel{border-color:#c7d2fe;background:#eef2ff}
.cekmece summary{cursor:pointer;font-weight:600}
.cekmece .soyle{margin:6px 0 4px;font-size:14px}
.cekmece .neden{margin:3px 0;color:#374151}
.cekmece .neden span{color:var(--g);font-size:11px;text-transform:uppercase;letter-spacing:.03em;margin-right:6px}
.cekmece ul{margin:4px 0 0 18px;padding:0}
.cekmece .baslik{margin:10px 0 6px}
body.cekmece-acik main{filter:none}

.kart.gecmis{border-left:4px solid #f59e0b}
.kart.bitti{opacity:.55}
.kart.bitti:hover{opacity:1}
.kart .tel{font-size:20px;font-weight:600;letter-spacing:.02em}
.kart .tel a{color:var(--m)}
.kart .satirlar div{margin:3px 0}
.kart .satirlar span{color:var(--g);font-size:11px;text-transform:uppercase;letter-spacing:.03em;margin-right:6px}
.sonuc{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 8px}
.sonuc button{border:1px solid var(--l);background:var(--bg);border-radius:999px;padding:5px 11px;font:inherit;cursor:pointer;color:var(--m)}
.sonuc button.secili{background:var(--m);color:var(--w);border-color:var(--m)}
.sonuc button.secili.iyi{background:var(--a);border-color:var(--a)}
.sonuc button.secili.kotu{background:var(--r);border-color:var(--r)}
.kanal{display:flex;gap:6px;align-items:center;font-size:12px;color:var(--g);margin-bottom:6px}
.kanal select,.kart input[type=text],.kart input[type=date],.kart input[type=datetime-local]{font:inherit;padding:5px 8px;border:1px solid var(--l);border-radius:6px;width:100%}
.kanal select{width:auto}
.kart .ek{display:flex;gap:6px;flex-wrap:wrap}
.kart .ek input[type=text]{flex:1;min-width:200px}
textarea.cikti{width:100%;min-height:140px;font:12px/1.4 ui-monospace,Menlo,Consolas,monospace;padding:8px;border:1px solid var(--l);border-radius:8px;margin-top:8px}
.yazikutu{border:1px solid var(--l);border-radius:8px;background:#fafafa;padding:10px 12px;margin:6px 0;
 white-space:pre-wrap;font:14px/1.6 inherit}
.yazibas{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px}
.yazibas span{color:var(--g);font-size:11px;text-transform:uppercase;letter-spacing:.03em}
.yazibas button{font:inherit;font-size:12px;padding:4px 10px;border:1px solid var(--l);
 border-radius:6px;background:#fff;cursor:pointer}
.yazibas button.ok{background:#166534;color:#fff;border-color:#166534}
.yazieksik{color:var(--g);font-size:13px;font-style:italic;padding:6px 0}
.mesaj{background:#dcfce7;color:#166534;border-radius:8px;padding:8px 12px;margin:8px 0;font-size:13px}
@media (max-width:760px){.kart{grid-template-columns:1fr;grid-template-areas:"oku" "soyle" "sonuc"}.kart .soyle-alani{border-left:0;padding-left:0;border-top:1px solid var(--l);padding-top:8px}.modlar button.itiraz-ac{margin-left:0}}
@media print{header{position:static}.arac,.cip,.sekme,.saha-ust,.sonuc,.kanal,.ek,.modlar,.cekmece{display:none}tr.detay{display:none}}
</style>
</head>
<body>
<header>
  <h1>Aday Listesi <span class="sekme"><button id="sek-liste" class="aktif">Liste</button><button id="sek-saha">Saha modu <small id="saha-sayi"></small></button></span></h1>
  <div class="alt" id="alt">Yükleniyor…</div>
  <div id="liste-ust">
  <div class="ozet" id="ozet"></div>
  <div class="arac">
    <input type="search" id="ara" placeholder="İşletme, sahibi, ilçe, telefon ara…">
    <div id="cipler"></div>
  </div>
  <div class="aciklama">Satıra tıklayınca ayrıntı açılır. Sütun başlığına tıklayınca sıralanır.<i style="background:#dcfce7"></i>bugün sırada<i style="background:#ffedd5"></i>günü geçmiş<i style="background:#ede9fe"></i>İlk 100: en çok istenen yüz işletme</div>
  <div class="aciklama">Uygunluk: denetimden çıkan 0-15 arası puan, A 10 ve üstü, B 6-9, C 5 ve altı. Sızıntı: kaç sızıntı görüldüğü, 0-5. İkisi de denetim yapılmadan boş durur. En çok istenen: derin denetimden geçen işletmeler; tam zamanlı çalışanda yüz, işin yanında çalışanda kırk tane seçilir.</div>
  </div>
</header>
<main>
  <div id="icerik"></div>
  <div id="saha" class="gizli"></div>
</main>
<aside id="cekmece" class="cekmece" aria-label="Karşı taraf bunu söylerse"></aside>
<script>/*FOUNDEROS-VERI*/</script>
<script>
(function(){
// --- CSV okuma (tırnak, virgül, satır içi yeni satır) ---
function csvOku(m){var s=[],r=[],h='',t=false,i=0;m=m.replace(/^\uFEFF/,'');
for(;i<m.length;i++){var c=m[i];
 if(t){if(c==='"'){if(m[i+1]==='"'){h+='"';i++}else t=false}else h+=c}
 else if(c==='"')t=true;else if(c===','){r.push(h);h=''}
 else if(c==='\n'||c==='\r'){if(c==='\r'&&m[i+1]==='\n')i++;r.push(h);h='';if(r.length>1||r[0]!=='')s.push(r);r=[]}
 else h+=c}
if(h!==''||r.length){r.push(h);s.push(r)}
if(!s.length)return[];var b=s[0].map(function(x){return x.trim()});
return s.slice(1).map(function(x){var o={};b.forEach(function(k,j){o[k]=(x[j]||'').trim()});return o})}

// --- sözlükler ---
// Veri servisinin cikardigi isaretlerden kurulan gozlem cumlesi.
// Tahmin degil: Google isletme profilinde gorunen sey. Elle yapilan derin
// denetimin yerine gecmez; denetimi yapilmamis adayin mesaji gozlemsiz
// gitmesin diye var. Sira guclu olandan zayifa.
var IPUCU_BIRLESIK=[
 [['reklam_veriyor','aksam_kapali'],"Reklam veriyorsunuz ama Google'da saatleriniz akşam altıda kapanıyor"],
 [['reklam_veriyor','yorum_sikayet'],"Reklam veriyorsunuz ama yorumlarınızdan birinde 'aradım açan olmadı' yazıyor"]
];
var IPUCU_KANCA=[
 ['is_ilani',"Şu an telefona bakacak birini arıyorsunuz, ilanınızı gördüm"],
 ['yorum_sikayet',"Google yorumlarınızdan birinde 'aradım, açan olmadı' yazıyor"],
 ['profil_sahipsiz',"Google'daki işletme sayfanız sahiplenilmemiş görünüyor"],
 ['aksam_kapali',"Google'da saatleriniz akşam altıda kapanıyor görünüyor"],
 ['saat_yok',"Google'da çalışma saatiniz yazmıyor"],
 ['site_yok',"Google'da site bağlantınız görünmüyor"],
 ['hafta_sonu_kapali',"Google'da hafta sonu kapalı görünüyorsunuz"],
 ['instagram_yok',"Instagram hesabınızı bulamadım"]
];
function profilKancasi(r){
 for(var j=0;j<IPUCU_BIRLESIK.length;j++){
  var k=IPUCU_BIRLESIK[j][0], hepsi=true;
  for(var m=0;m<k.length;m++) if(r._ipucu.indexOf(k[m])<0) hepsi=false;
  if(hepsi) return IPUCU_BIRLESIK[j][1];
 }
 for(var i=0;i<IPUCU_KANCA.length;i++){ if(r._ipucu.indexOf(IPUCU_KANCA[i][0])>=0) return IPUCU_KANCA[i][1]; }
 return '';
}
var IPUCU={is_ilani:['İş ilanı var','uyari'],reklam_veriyor:['Reklam veriyor',''],yorum_sikayet:['Yorumda "ulaşamadım"','uyari'],profil_sahipsiz:['Profili sahipsiz','uyari'],site_yok:['Sitesi yok','uyari'],instagram_yok:['Instagram yok',''],yorum_az:['Yorumu az',''],aksam_kapali:['Akşam kapalı','uyari'],hafta_sonu_kapali:['Hafta sonu kapalı','uyari'],pazar_kapali:['Pazar kapalı',''],saat_yok:['Saati yazmıyor','']};
var ASAMA={yeni:['Yeni',''],temasta:['Temasta','mavi'],'cevap verdi':['Cevap verdi','iyi'],randevu:['Randevu','iyi'],'görüşüldü':['Görüşüldü','mor'],sonra:['Sonra',''],'kapandı':['Kapandı','kotu'],'müşteri':['Müşteri','iyi']};
var KANAL={telefon:'Telefon',eposta:'E-posta','e-posta':'E-posta',instagram:'Instagram',video:'Video'};
function rozet(m,t){return '<span class="rozet '+(t||'')+'">'+m+'</span>'}
function kac(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function tarihTr(s){if(!s)return'';var p=s.slice(0,10).split('-');if(p.length<3)return kac(s);var A=['Oca','Şub','Mar','Nis','May','Haz','Tem','Ağu','Eyl','Eki','Kas','Ara'];return parseInt(p[2],10)+' '+A[parseInt(p[1],10)-1]+' '+p[0]+(s.length>10?' '+kac(s.slice(11,16)):'')}
function isoGun(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
var BUGUN=isoGun(new Date());
function gunEkle(n){var d=new Date();d.setDate(d.getDate()+n);return isoGun(d)}
function uygunlukHarf(v){var n=parseInt(v,10);if(isNaN(n))return'';return n>=10?'A':n>=6?'B':'C'}
function sizintiNokta(v){var n=parseInt(v,10);if(isNaN(n))return'<span class="kucuk">denetlenmedi</span>';var h='';for(var i=0;i<5;i++)h+='<span class="nokta'+(i<n?' dolu':'')+'"></span>';return h+' <span class="puan">'+n+'</span>'}
function telBicim(t){var g=t.replace(/^\+90/,'0');if(g.length===11)g=g.slice(0,4)+' '+g.slice(4,7)+' '+g.slice(7,9)+' '+g.slice(9);return g}
function telLink(t){if(!t)return'<span class="kucuk">yok</span>';return'<a href="tel:'+kac(t)+'">'+kac(telBicim(t))+'</a>'}
function kapali(r){return /kapandı|müşteri/.test(r.asama||'')}

// --- veri ---
var ham=(window.ADAYLAR||'');var tarih=window.ADAYLAR_TARIH||'';var NIS=window.ADAYLAR_NIS||{};
var alt=document.getElementById('alt'),icerik=document.getElementById('icerik'),saha=document.getElementById('saha');
if(!ham){alt.textContent='Liste henüz bu sayfaya yüklenmedi.';icerik.innerHTML='<div class="bos">FounderOS\'a "listemi yenile" yaz; liste dolunca bu sayfa da dolar.</div>';return}
var satirlar=csvOku(ham).filter(function(r){return !r.elenme});
satirlar.forEach(function(r,i){r._i=i;r._ipucu=(r.ipuclari||'').split(/\s+/).filter(Boolean);r._yuz=/^(evet|1|x)$/i.test(r.yuz||'');r._sicak=/tanıdık|referans/.test((r.kaynak||'').toLocaleLowerCase('tr'));r._bugun=!!r.siradaki_tarih&&r.siradaki_tarih.slice(0,10)===BUGUN&&!kapali(r);r._gecmis=!!r.siradaki_tarih&&r.siradaki_tarih.slice(0,10)<BUGUN&&!kapali(r)});
var enCok=NIS.ad||'';if(!enCok){var kategoriler={};satirlar.forEach(function(r){if(r.kategori)kategoriler[r.kategori]=(kategoriler[r.kategori]||0)+1});enCok=Object.keys(kategoriler).sort(function(a,b){return kategoriler[b]-kategoriler[a]})[0]||''}
alt.textContent=(enCok?enCok+' · ':'')+satirlar.length+' aday'+(tarih?' · Son güncelleme: '+tarih:'')+' · Bugün: '+tarihTr(BUGUN);

// --- özet kutuları ---
var say=function(f){return satirlar.filter(f).length};
var OZET=[['Toplam',satirlar.length],['Telefonu olan',say(function(r){return r.telefon})],['E-postası olan',say(function(r){return r.eposta})],['Denetlenmiş',say(function(r){return r.sizinti!==''})],['En çok istenen',say(function(r){return r._yuz})],['Bugün sırada',say(function(r){return r._bugun})],['Gecikmiş',say(function(r){return r._gecmis})],['Cevap verdi',say(function(r){return /cevap verdi/.test(r.asama||'')})],['Randevu',say(function(r){return /randevu/.test(r.asama||'')||r.randevu_tarihi})]];
document.getElementById('ozet').innerHTML=OZET.map(function(k){return'<div class="kutu"><b>'+k[1]+'</b><span>'+k[0]+'</span></div>'}).join('');

// --- filtreler ---
var FILTRE=[['hepsi','Hepsi',function(){return true}],['bugun','Bugün sırada',function(r){return r._bugun||r._gecmis}],['yuz','En çok istenen yüz',function(r){return r._yuz}],['cevap','Cevap verenler',function(r){return /cevap verdi|randevu|görüşüldü/.test(r.asama||'')}],['yeni','Hiç aranmamış',function(r){return !r.son_temas_tarihi&&!kapali(r)}],['denetsiz','Denetlenmemiş',function(r){return r.sizinti===''}],['sonra','Sonra / kapandı',function(r){return /sonra|kapandı/.test(r.asama||'')}]];
var aktif='hepsi',arama='',siraKey='',siraTers=false;
document.getElementById('cipler').innerHTML=FILTRE.map(function(f){return'<button class="cip'+(f[0]===aktif?' aktif':'')+'" data-f="'+f[0]+'">'+f[1]+'<small>'+say(f[2])+'</small></button>'}).join('');
document.getElementById('cipler').addEventListener('click',function(e){var b=e.target.closest('.cip');if(!b)return;aktif=b.dataset.f;document.querySelectorAll('.cip').forEach(function(x){x.classList.toggle('aktif',x.dataset.f===aktif)});ciz()});
document.getElementById('ara').addEventListener('input',function(e){arama=e.target.value.toLocaleLowerCase('tr');ciz()});

// --- tablo ---
var KOLON=[['kisa_ad','İşletme'],['sahibi','Sahibi'],['telefon','Telefon'],['semt','İlçe / semt'],['yorum_sayisi','Yorum'],['sizinti','Sızıntı'],['uygunluk','Uygunluk'],['ipuclari','İpuçları'],['asama','Aşama'],['son_temas_tarihi','Son temas'],['siradaki_tarih','Sıradaki'],['eklenme_tarihi','Eklendi']];
function deger(r,k){if(k==='yorum_sayisi'||k==='sizinti'||k==='uygunluk')return parseInt(r[k],10)||-1;return (r[k]||'').toLocaleLowerCase('tr')}
function etiketler(r){return (r._yuz?' '+rozet('İlk 100','mor'):'')+(r._sicak?' '+rozet(r.kaynak==='referans'?'Referans':'Tanıdık','iyi'):'')}
function ciz(){
 var f=FILTRE.filter(function(x){return x[0]===aktif})[0][2];
 var liste=satirlar.filter(f).filter(function(r){if(!arama)return true;return [r.kisa_ad,r.ad,r.sahibi,r.semt,r.telefon,r.adres,r.not,r.bulgu].join(' ').toLocaleLowerCase('tr').indexOf(arama)>=0});
 if(siraKey){liste.sort(function(a,b){var x=deger(a,siraKey),y=deger(b,siraKey);if(x<y)return siraTers?1:-1;if(x>y)return siraTers?-1:1;return 0})}
 else{liste.sort(function(a,b){return (b._bugun|0)-(a._bugun|0)||(b._gecmis|0)-(a._gecmis|0)||(b._yuz|0)-(a._yuz|0)||(parseInt(b.sizinti,10)||0)-(parseInt(a.sizinti,10)||0)||(parseInt(b.yorum_sayisi,10)||0)-(parseInt(a.yorum_sayisi,10)||0)})}
 if(!liste.length){icerik.innerHTML='<div class="bos">Bu süzgeçte kayıt yok.</div>';return}
 var h='<table><thead><tr>'+KOLON.map(function(k){return'<th data-k="'+k[0]+'" class="'+(siraKey===k[0]?'sirali'+(siraTers?' ters':''):'')+'">'+k[1]+'</th>'}).join('')+'</tr></thead><tbody>';
 liste.forEach(function(r){
  var as=ASAMA[(r.asama||'yeni').toLocaleLowerCase('tr')]||[r.asama||'Yeni',''];
  var ip=r._ipucu.map(function(c){var x=IPUCU[c]||[c,''];return rozet(x[0],x[1])}).join('');
  var uy=uygunlukHarf(r.uygunluk);
  var sir=r.siradaki_tarih?tarihTr(r.siradaki_tarih)+(r.siradaki_hareket?'<br><span class="kucuk">'+kac(r.siradaki_hareket)+'</span>':''):'<span class="kucuk">yok</span>';
  var son=r.son_temas_tarihi?tarihTr(r.son_temas_tarihi)+(r.son_temas_kanali?'<br><span class="kucuk">'+kac(KANAL[r.son_temas_kanali.toLocaleLowerCase('tr')]||r.son_temas_kanali)+(r.temas_sayisi?' · '+kac(r.temas_sayisi)+' temas':'')+'</span>':''):'<span class="kucuk">henüz yok</span>';
  h+='<tr class="satir'+(r._bugun?' bugun':r._gecmis?' gecmis':'')+'" data-i="'+r._i+'"><td><div class="ad">'+kac(r.kisa_ad||r.ad)+etiketler(r)+'</div>'+(r.bulgu?'<div class="kucuk">'+kac(r.bulgu)+'</div>':'')+'</td>'
   +'<td>'+(r.sahibi?kac(r.sahibi):'<span class="kucuk">bulunamadı</span>')+'</td><td>'+telLink(r.telefon)+'</td><td>'+kac(r.semt)+'</td>'
   +'<td class="puan">'+kac(r.yorum_sayisi)+(r.puan?'<br><span class="kucuk">'+kac(r.puan)+' puan</span>':'')+'</td><td>'+sizintiNokta(r.sizinti)+'</td><td>'+(uy?rozet(uy+' · '+r.uygunluk,uy==='A'?'iyi':uy==='B'?'':'kotu'):'<span class="kucuk">yok</span>')+'</td>'
   +'<td>'+(ip||'<span class="kucuk">temiz</span>')+'</td><td>'+rozet(as[0],as[1])+'</td><td>'+son+'</td><td>'+sir+'</td><td class="kucuk">'+tarihTr(r.eklenme_tarihi)+'</td></tr>';
  h+='<tr class="detay gizli" data-d="'+r._i+'"><td colspan="12"><div class="detay-grid">'
   +alan('Tam ad',r.ad)+alan('E-posta',r.eposta?'<a href="mailto:'+kac(r.eposta)+'">'+kac(r.eposta)+'</a>':'')+alan('Instagram',r.instagram?'<a href="'+kac(r.instagram)+'" target="_blank">'+kac(r.instagram.replace(/^https?:\/\/(www\.)?instagram\.com\//,'@').replace(/\/$/,''))+'</a>':'')
   +alan('Site',r.site?'<a href="'+kac(r.site)+'" target="_blank">'+kac(r.site.replace(/^https?:\/\/(www\.)?/,'').replace(/\/$/,''))+'</a>':'')+alan('Adres',r.adres)+alan('Haritada',r.harita?'<a href="'+kac(r.harita)+'" target="_blank">aç</a>':'')
   +alan('Kategori',r.kategori)+alan('Kaynak',r.kaynak)+alan('Bağlayan',r.baglayan)+alan('Kanca',r.kanca)+alan('Lira karşılığı',r.lira)+alan('Denetim tarihi',tarihTr(r.denetim_tarihi))
   +alan('Telefon kanalı',r.telefon_durumu)+alan('E-posta kanalı',r.eposta_durumu)+alan('Instagram kanalı',r.instagram_durumu)+alan('Video kanalı',r.video_durumu)
   +alan('Randevu',tarihTr(r.randevu_tarihi))+alan('Sıradaki hareket',r.siradaki_hareket)+alan('Temas sayısı',r.temas_sayisi)+alan('Not',r.not)
   +'</div></td></tr>'});
 h+='</tbody></table>';icerik.innerHTML=h;
 icerik.querySelectorAll('th').forEach(function(th){th.addEventListener('click',function(){var k=th.dataset.k;if(siraKey===k)siraTers=!siraTers;else{siraKey=k;siraTers=false}ciz()})});
 icerik.querySelectorAll('tr.satir').forEach(function(tr){tr.addEventListener('click',function(e){if(e.target.closest('a'))return;var d=icerik.querySelector('tr.detay[data-d="'+tr.dataset.i+'"]');d.classList.toggle('gizli')})});
}
function alan(b,v){return v?'<div><span>'+b+'</span>'+v+'</div>':''}
ciz();

// --- saha modu: günün listesi, söyle paneli, sonuç düğmeleri, sonuçları kopyala ---
var gunluk=satirlar.filter(function(r){return r._bugun||r._gecmis}).sort(function(a,b){var ca=/cevap verdi|randevu/.test(a.asama||'')|0,cb=/cevap verdi|randevu/.test(b.asama||'')|0;return cb-ca||(b._gecmis|0)-(a._gecmis|0)||(b._yuz|0)-(a._yuz|0)||(parseInt(b.sizinti,10)||0)-(parseInt(a.sizinti,10)||0)});
var ANAHTAR='founderos-saha-'+BUGUN;
function durumOku(){try{return JSON.parse(localStorage.getItem(ANAHTAR)||'{}')}catch(e){return{}}}
function durumYaz(d){try{localStorage.setItem(ANAHTAR,JSON.stringify(d))}catch(e){}}
var durum=durumOku();
function kanalTahmin(r){var h=(r.siradaki_hareket||'').toLocaleLowerCase('tr');if(/instagram/.test(h))return'instagram';if(/e-?posta|mail/.test(h))return'e-posta';if(/video/.test(h))return'video';if(/yazı|mesaj/.test(h))return r.instagram?'instagram':r.eposta?'e-posta':'telefon';return'telefon'}
var SONUC=[['acmadi','Açmadı','kotu','telefon'],['gonderdim','Gönderdim','','yazi'],['istemedi','İstemedi','kotu',''],['ilgilendi','İlgilendi','iyi',''],['randevu','Randevu','iyi',''],['sonra','Sonra ara','','']];
document.getElementById('saha-sayi').textContent=gunluk.length?gunluk.length:'';

// --- söyle metni: modülün genel sırası + niş kartının "Telefonda söylenecekler" bölümü (sayfa.json) ---
var OGR=NIS.ogrenci||{};var OAD=OGR.ad||'[adın]',OSEHIR=OGR.sehir||'[şehir]',OSIS=OGR.sistem_adi||'';
var NIS_ACILIS=NIS.acilis_sorusu||NIS.acilis||'';
var GENEL={
 isleyis:'Yoğunken telefona yetişemediğinizde müşteri ne yapıyor, tekrar mı arıyor, mesaj mı yazıyor?',
 vaat:'Ben tam bunun için bir sistem kuruyorum: siz işteyken WhatsApp\'a, Instagram\'a ya da sitenizden yazan müşteriye dakikalar içinde cevap veriyor, bilgiyi alıp randevuya yazıyor; eski müşterilerinize de zamanı gelince hatırlatma gönderiyor. [Şehir]\'de bu ay ilk üç işletmeyle başlıyorum.',
 calisan:'Yoğunken telefona yetişemediğiniz saatlerde müşteriye cevap veren bir sistemle ilgili; kendisiyle iki dakika konuşmak istiyorum. Ne zaman dükkanda olur?',
 randevu:'Yarın on birde yirmi dakika görüşelim mi, uymazsa siz saat söyleyin.'};
var GENEL_ITIRAZ=[
 {durum:'Şu an müsait değilim.',soyle:'Tabii, ne zaman arayayım? Bugün akşamüstü mü, yarın sabah mı?',neden:'Zamanı olmadığını kabul edip somut saat almak, anlatmaya devam etmek değil.',sonra:'Saat verirse teşekkür et, kapat; "Sonra ara" düğmesine bas, tarihi yaz. Belirsizse bir kez daha sor ("Yarın on gibi uygun mu?"); yine belirsizse yarın ara, üçüncü kez arama.'},
 {durum:'Ne için arıyorsunuz?',soyle:'Yoğunken telefona yetişemediğiniz saatlerde WhatsApp\'a ve Instagram\'a yazan müşteriye cevap verip randevuya yazan bir sistem kuruyorum. Sizde böyle bir şey var mı diye soracaktım.',neden:'Tek cümlede ne olduğunu söylemek ve konuşmayı işletmenin işleyişine çevirmek.',sonra:'"Yok" derse işleyiş sorusuna geç; "var" derse "Nasıl çalışıyor, kim cevap veriyor?" diye sor, cevaba göre görüşme iste ya da kapat.'},
 {durum:'WhatsApp\'tan bilgi gönderin.',soyle:'Olur, on dakika içinde gönderiyorum: kim olduğum, ne yaptığım ve sayfamın adresi, üç satır. Okuduktan sonra yarın on dakika konuşabilir miyiz, yoksa ben mi arayayım?',neden:'İsteği reddetmemek ama sonraki teması bugün bağlamak.',sonra:'Kapatınca on dakika içinde FounderOS\'un hazırladığı üç satırlık mesajı gönder ("Gönderdim" düğmesi). Cevap gelmezse üçüncü gün tek takip, yedinci gün tek soru; sonra bırak.'},
 {durum:'Biz zaten kendimiz ilgileniyoruz.',soyle:'İyi o zaman, çoğu işletme ilgilenemiyor. Yoğunken de yetişebiliyor musunuz, yoksa akşama kalan mesajlar oluyor mu?',neden:'"Kendimiz" cevabının arkasındaki gerçeği anlamak.',sonra:'"Yetişiyoruz" derse teşekkür et, "yoğun dönemde değişirse aramamı ister misiniz" de, kapat; "Sonra ara" düğmesi. "Akşama kalıyor" derse görüşme iste.'},
 {durum:'Yapay zekâ / bot istemiyoruz.',soyle:'Anlıyorum, kötü kurulmuş olanı ben de istemem. Evet, mesajlara cevap veren bir yapay zekâ asistanı; ama fiyat vermiyor, sadece ne istendiğini ve adresi alıp size uygun bir randevu yazıyor. Fiyat ve karışık konu size düşüyor. Sizi rahatsız eden, müşteriyle robot konuşması mı, yoksa yanlış bilgi vermesi mi?',neden:'Kaygıyı gizlemeden ne yaptığını söylemek ve gerçek endişeyi ayırmak.',sonra:'"Robot konuşması" derse: "Müşteri isterse hemen size devrediyor, o kural baştan var" de, görüşmede telefonundan denemesini teklif et. "Yanlış bilgi" derse: "Fiyat ve garanti konusuna hiç girmiyor." Israr sürerse kapat: "Anladım, zorlamayayım. Fikriniz değişirse numaram sizde olsun." "İstemedi" düğmesi.'},
 {durum:'Pahalı.',soyle:'Olabilir. Şunu sorayım: rakam mı yüksek geldi, yoksa işe yarayacağından emin değilsiniz?',neden:'Fiyat itirazı ile güven itirazını ayırmak; "sonuç kesin" demeden. İlk aramada fiyat konuşulmaz; sorarsa İş Beyni\'ndeki "fiyat ne" cevabı okunur, pazarlık ve indirim yok.',sonra:'"Rakam" derse: "O zaman görüşmede bir işin sizde kaç lira ettiğini birlikte hesaplayalım, karar sizin" ve saat iste. "Emin değilim" derse: "Haklısınız, ilk müşterilerimle kanıt topluyorum; rapor günü sayıları görüyorsunuz" ve saat iste. İkisine de hayır derse kapat.'},
 {durum:'İlgilenmiyorum.',soyle:'Anladım, teşekkür ederim. Kapatmadan tek şey sorayım: şu an dolu olduğunuz için mi, yoksa konu size uzak geldiği için mi?',neden:'Bir kez, tek soruyla sebebi öğrenmek; ikinci soru yok.',sonra:'"Dolu" derse: "Anladım, yoğunluk geçince bir kez daha arayabilir miyim?" cevap ne olursa kapat, "Sonra ara". "Uzak" ya da sert hayır: "Tamam, vaktinizi aldım, iyi çalışmalar." Kapat, "İstemedi" düğmesi; bir daha aranmaz.'},
 {durum:'Sonra arayın.',soyle:'Tabii, ne zaman uygun?',neden:'Tarih almak.',sonra:'Verdiği günü "Sonra ara" ile yaz; vermezse "yarın öğleden sonra deneyeyim mi" diye sor, cevabı bekle.'},
 {durum:'Fiyat ne?',soyle:'(İş Beyni\'nin dördüncü bölümündeki "fiyat ne" cevabı: aralık, sebep, görüşmeye bağlama.)',neden:'Fiyatı söyleyip indirim yapmamak.',sonra:'Rakamı duyunca "pahalı" gelirse yukarıdaki cevap.'},
 {durum:'Zaten elemanım / ekibim var.',soyle:'Güzel, o zaman şunu sorayım: en yoğun saatte eleman sahadayken telefona ve mesajlara kim bakıyor?',neden:'Elemanın telefona bakabildiği anı sormak.',sonra:'"Bakıyor" derse teşekkür et ve kapat; "o da sahada" derse görüşme iste.'},
 {durum:'Böyle şeyler işe yaramıyor, denedik.',soyle:'Olabilir, kötü kurulmuş çoğu. Ne yaşadınız?',neden:'Yaşadığı sorunu öğrenmek, savunmak değil.',sonra:'Anlattığı sorun bizim kuralımızla çözülüyorsa tek cümleyle söyle ("fiyat vermiyor", "müşteri isterse size devrediyor") ve görüşme iste; çözülmüyorsa kapat.'},
 {durum:'Kim olduğunuzu bilmiyorum.',soyle:'Haklısınız. Ben [adın], [şehir]\'de yaşıyorum, bu işletmelere mesaj ve randevu tarafını kuruyorum; bu ay ilk üç işletmeyle başlıyorum.',neden:'Kim olduğunu tek cümlede söylemek.',sonra:'Soruya dön.'},
 {durum:'Ne kadar sürer?',soyle:'Yirmi dakika. O kadar vaktiniz olur mu?',neden:'Doğru süreyi söylemek.',sonra:'Saat al.'},
 {durum:'Instagram\'ı ajansa verdim.',soyle:'Ajans reklamı yapıyor; gelen mesaja ve telefona cevap sizde kalıyor. Ben o tarafı kuruyorum, ajansın rakibi değilim.',neden:'Ajansla çatışmamak.',sonra:'Soruya dön.'},
 {durum:'Zaten bir yapay zekâ teklifi aldık.',soyle:'Güzel, ne vaat ettiler?',neden:'Dinlemek.',sonra:'"Ne kurduğumu rapor günü sayıyla gösteriyorum. Kurulan bir şey varsa yirmi dakikada ne eksik söylerim." Görüşme iste; istemezse kapat.'},
 {durum:'Ezberden mi okuyorsun?',soyle:'Önümde not var, evet; ezber değil. İsterseniz bırakayım.',neden:'Saklamamak.',sonra:'Soruya devam.'},
 {durum:'Araba kullanıyorum / müşterideyim.',soyle:'Dikkatinizi dağıtmayayım, ne zaman uygun?',neden:'Gün almak.',sonra:'Gün al, kapat, "Sonra ara".'},
 {durum:'Hemen yazın beni.',soyle:'Açıkçası size uyar mı bilmiyorum, önce yirmi dakika tanıyalım.',neden:'Sahte evet gelmez; görüşmeye bağlamak.',sonra:'Saat al.'},
 {durum:'Çalışanlarımın yerini mi alacak?',soyle:'Hayır. Çalışanınız sahadayken cevapsız kalan mesajı karşılıyor, o kadar.',neden:'Korkuyu tek cümlede kapatmak.',sonra:'Soruya dön.'},
 {durum:'Bozulursa ne olacak?',soyle:'Haftada bir kontrol ediyorum, sorun çıkarsa aynı gün bakıyorum; hesaplar sizin adınıza açık, istediğiniz gün kapatırsınız.',neden:'Olmayan yedek ve olmayan destek hattı söylenmez.',sonra:'Soruya dön.'}];
var TON=['Ayakta ve gezinerek konuş, telefon elde değil.','Gülümseyerek konuş, sesten anlaşılır.','Karşı tarafın tonuna ayak uydur.','Kendini küçültme yok: "bir şey satmaya çalışmıyorum" yasak.','Muhtaç görünme yok: ilgilenirsen ne güzel, ilgilenmezsen sorun değil.','Dolgu kelimesi yok.','İlk hayırda tek soru, ikinci soru yok. Israr yok.','Ne kadar konuşursan konuş, cümleni soruyla bitir.','Lira rakamı telefonda söylenmez, görüşmeye kalır.','Aksan, şive, genç ses: başta söyle, saklama.'];
function ek(w,tur){if(!w||w.charAt(0)==='[')return w+"'"+tur;var v=(w.match(/[aeıioöuüAEIİOÖUÜ]/g)||[]);var son=v.length?v[v.length-1].toLocaleLowerCase('tr'):'e';var kalin=/[aıou]/.test(son);var sert=/[pçtksşhfPÇTKSŞHF]$/.test(w);var d=sert?'t':'d';var e=(tur==='den'||tur==='de')?(kalin?'a':'e'):'';var s=tur==='den'?d+e+'n':tur==='de'?d+e:tur;return w+"'"+s}
function doldur(s){return String(s||'').replace(/\[adın\]/g,OAD).replace(/\[[Şş]ehir\]'(den|dan|de|da)/g,function(x,t){return ek(OSEHIR,/n$/.test(t)?'den':'de')}).replace(/\[[Şş]ehir\]/g,OSEHIR)}
function neZaman(t){if(!t)return'daha önce';var a=new Date(t.slice(0,10)),b=new Date(BUGUN);var g=Math.round((b-a)/864e5);if(g<=0)return'bugün';if(g===1)return'dün';if(g===2)return'önceki gün';if(g<7)return['üç','dört','beş','altı'][g-3]+' gün önce';if(g<14)return'geçen hafta';return'bir süre önce'}
function nisItirazlar(){var l=NIS.itirazlar||[];return l.map(function(x){return typeof x==='string'?{durum:x,soyle:'',neden:'',sonra:''}:x}).filter(function(x){return x&&x.durum})}
function kaynakCumle(r){var k=(r.kaynak||'').toLocaleLowerCase('tr');if(k==='iş ilanı'||k==='is ilani')return'Numaranızı verdiğiniz iş ilanından aldım.';if(k==='tanıdık'||k==='referans')return r.baglayan?'Numaranızı '+r.baglayan+' verdi.':'Numaranızı ortak bir tanıdığımızdan aldım.';if(k==='haritalar'||!k)return'Numaranızı Haritalar\'daki işletme sayfanızdan aldım.';return'Numaranızı internetteki işletme sayfanızdan aldım.'}
function modTahmin(r){var n=parseInt(r.temas_sayisi,10)||0;var tel=(r.son_temas_kanali||'').toLocaleLowerCase('tr')==='telefon';return (n>0&&tel)?'ikinci':'sahibi'}
function adimlar(r,mod){var s=r.sahibi?kac(r.sahibi):'';var kim=s?s+' ile mi görüşüyorum?':'İşletme sahibi siz misiniz?';var a=[];
 if(mod==='calisan'){a.push(['Tanış','Merhaba, ben '+kac(OAD)+', '+kac(ek(OSEHIR,'den'))+' arıyorum. '+(s?s+' ile görüşebilir miyim?':'İşletme sahibiyle görüşebilir miyim?')]);
  a.push(['"Ne hakkında?" gelirse',kac(doldur(NIS.calisan||GENEL.calisan))]);
  a.push(['Kural','Konuyu saklama, "kendisi biliyor" deme. Not bıraktırma, saat al. "Bana anlatın" derse iki cümle anlat, yine saat iste; çalışana satış yok. Açanın adını nota yaz; sonraki aramada onunla başla.']);return a}
 if(mod==='acilmadi'){a.push(['Şimdi','Hemen bir kez daha ara. Yine açılmazsa bugün bırak, mesaj bırakma; "Açmadı" düğmesine bas.']);a.push(['Yarın','Başka bir saatte bir kez daha. İki günde açılmazsa e-posta, FounderOS karar tablosuna göre yazar.']);return a}
 if(mod==='ikinci'){var nz=neZaman(r.son_temas_tarihi);a.push(['Tanış ve geçmiş','Merhaba'+(s?' '+s:'')+', ben '+kac(OAD)+', '+nz+' de aramıştım'+(r.telefon_durumu==='yapıldı'?', kısa konuşmuştuk':', açılmamıştı')+'. Bir dakikanız var mı? <span class="kucuk">saat verdiyse: "'+(nz==='dün'?'Dün':'Geçen aramada')+' \'şu saatte ara\' demiştiniz, uygun mu?"</span>']);
  a.push(['Gözlem',(r.kanca?kac(r.kanca)+' Onun için arıyorum.':nz.charAt(0).toLocaleUpperCase('tr')+nz.slice(1)+' aradığımda açılmamıştı, onun için arıyorum.')+' <span class="kucuk">önceki arama gerçek gözlemdir; uydurma yok</span>']);}
 else{a.push(['Tanış ve kaynağı söyle','Merhaba, ben '+kac(OAD)+', '+kac(ek(OSEHIR,'den'))+' arıyorum. '+kac(kaynakCumle(r))+' '+kim+' <span class="kucuk">bekle</span>']);
  a.push(['Rahatlat','Sizi tanımıyorum, kısa tutacağım.']);
  var pk=r.kanca?'':profilKancasi(r);
  a.push([r.kanca?'Gözlem (doğrulanmış)':(pk?'Gözlem (profilden)':'Açılış sorusu'),
    r.kanca?kac(r.kanca)+' Onun için arıyorum.'
    :(pk?kac(pk)+' Onun için arıyorum. <span class="kucuk">Google profilinde görülen şey; denetim yapılmadı, uydurma yok</span>'
       :(NIS_ACILIS?kac(doldur(NIS_ACILIS)):'<i class="kucuk">Kartta açılış sorusu yok ve bu adayda gözlem yok; işleyiş sorusuna geç. Uydurma.</i>'))]);}
 a.push(['İşleyiş sorusu, tek soru',kac(doldur(NIS.isleyis_sorusu||GENEL.isleyis))+' <span class="kucuk">bekle, araya girme</span>']);
 a.push(['Ne yaptığın, kapsam içinde',kac(doldur(NIS.vaat||GENEL.vaat))+(OSIS?' Adı '+kac(OSIS)+'.':'')]);
 a.push(['Randevu',kac(GENEL.randevu)+' <span class="kucuk">kırk sekiz saatten uzağa alma; onay için e-posta ya da WhatsApp izni telefondayken</span>']);
 return a}
// Yazili kanal paneli: adaya ozel metin CSV'de duruyor, burada kopyalaniyor.
// Sohbete donup metin istemek yok; gonderim ogrencinin elinde kaliyor.
function yaziPanel(r,mod){
 if(mod==='eposta'){
  if(!r.eposta) return '<div class="yazieksik">Bu adayın e-posta adresi yok. Telefon ya da Instagram kullan.</div>';
  if(!r.eposta_metni) return '<div class="yazieksik">E-posta metni henüz yazılmadı. FounderOS\'a "bugünün e-postalarını yaz" de.</div>';
  return '<div class="yazibas"><span>Kime</span><button data-kop="'+kac(r.eposta)+'">Adresi kopyala</button></div>'
   +'<div class="yazikutu">'+kac(r.eposta)+'</div>'
   +(r.eposta_konu?'<div class="yazibas"><span>Konu</span><button data-kop="'+kac(r.eposta_konu)+'">Kopyala</button></div><div class="yazikutu">'+kac(r.eposta_konu)+'</div>':'')
   +'<div class="yazibas"><span>Metin</span><button class="ok" data-kop="'+kac(r.eposta_metni)+'">Metni kopyala</button></div>'
   +'<div class="yazikutu">'+kac(r.eposta_metni)+'</div>'
   +'<div class="kucuk">Kendi iş e-postandan gönder. Gönderdikten sonra aşağıdan kanalı e-posta seçip sonucu işaretle.</div>';
 }
 if(!r.instagram) return '<div class="yazieksik">Bu adayın Instagram hesabı bulunamadı. Telefon ya da e-posta kullan.</div>';
 if(!r.dm_metni) return '<div class="yazieksik">Mesaj metni henüz yazılmadı. FounderOS\'a "bugünün mesajlarını yaz" de.</div>';
 return '<div class="yazibas"><span>Hesap</span><button data-kop="'+kac(r.instagram)+'">Kopyala</button></div>'
  +'<div class="yazikutu">'+kac(r.instagram)+'</div>'
  +'<div class="yazibas"><span>Mesaj</span><button class="ok" data-kop="'+kac(r.dm_metni)+'">Mesajı kopyala</button></div>'
  +'<div class="yazikutu">'+kac(r.dm_metni)+'</div>'
  +'<div class="kucuk">Önce son gönderisine yorum yaz, sonra mesajı gönder. Gönderdikten sonra kanalı Instagram seçip sonucu işaretle.</div>';
}
function soylePanel(r,mod){
 var M=[['sahibi','Sahibi açtı'],['calisan','Çalışan açtı'],['acilmadi','Açılmadı'],['ikinci','İkinci arama']];
 if(r.eposta) M.push(['eposta','E-posta']);
 if(r.instagram) M.push(['dm','Instagram']);
 var h='<div class="modlar">'+M.map(function(m){return'<button data-mod="'+m[0]+'" class="'+(m[0]===mod?'aktif':'')+'">'+m[1]+'</button>'}).join('')+'<button class="itiraz-ac" data-itiraz>Karşı taraf bunu söylerse</button></div>';
 if(mod==='eposta'||mod==='dm') return h+yaziPanel(r,mod);
 h+='<ol class="adimlar">';
 adimlar(r,mod).forEach(function(x){h+='<li><span class="e">'+x[0]+'</span>'+x[1]+'</li>'});return h+'</ol>'}
function yedekKopya(t,bitti){
 var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';
 document.body.appendChild(a);a.select();try{document.execCommand('copy');bitti()}catch(e){}
 document.body.removeChild(a);
}
function itirazCekmece(){var ozel=nisItirazlar();var h='<div class="cekmece-ust"><b>Karşı taraf bunu söylerse</b><button class="dugme" data-kapat>Kapat</button></div>';
 function madde(x,tur){return'<details'+(tur?' class="'+tur+'"':'')+'><summary>"'+kac(x.durum)+'"</summary>'+(x.soyle?'<div class="soyle">Söyle: "'+kac(doldur(x.soyle))+'"</div>':'')+(x.neden?'<div class="neden"><span>Ne için</span>'+kac(x.neden)+'</div>':'')+(x.sonra?'<div class="neden"><span>Sonra</span>'+kac(doldur(x.sonra))+'</div>':'')+'</details>'}
 if(ozel.length)h+='<div class="kucuk baslik">'+kac(NIS.ad||'Bu niş')+' için</div>'+ozel.map(function(x){return madde(x,'ozel')}).join('');
 h+='<div class="kucuk baslik">Her nişte</div>'+GENEL_ITIRAZ.map(function(x){return madde(x)}).join('');
 h+='<details><summary>Ton kuralları</summary><ul>'+TON.map(function(t){return'<li>'+kac(t)+'</li>'}).join('')+'</ul></details>';
 h+='<div class="kucuk" style="margin-top:10px">Her cevap tek soru taşır, ikinci itiraz sorusu yok. Açık ret gelince teşekkür et, kapat; aday bir daha aranmaz.</div>';return h}
var cekmece=document.getElementById('cekmece');cekmece.innerHTML=itirazCekmece();
function cekmeceAc(a){cekmece.classList.toggle('acik',a);document.body.classList.toggle('cekmece-acik',a)}
cekmece.addEventListener('click',function(e){if(e.target.closest('[data-kapat]'))cekmeceAc(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')cekmeceAc(false)});

function sahaCiz(){
 var giren=gunluk.filter(function(r){return durum[r.kisa_ad]&&durum[r.kisa_ad].sonuc}).length;
 var h='<div class="saha-ust"><span class="kucuk">'+(gunluk.length?gunluk.length+' aday sırada · '+giren+' sonuç girildi · '+(gunluk.length-giren)+' kaldı':'')+((OAD==='[adın]'||OSEHIR==='[şehir]')?' · <span class="rozet uyari">adın ve şehrin sayfaya yazılmamış, FounderOS\'a söyle</span>':'')+'</span>'
  +'<button class="dugme" data-itiraz>Karşı taraf bunu söylerse</button><button class="dugme ana" id="kopyala">Sonuçları kopyala</button><button class="dugme kirmizi" id="temizle">Temizle</button></div><div id="kopya-alani"></div>';
 if(!gunluk.length){h+='<div class="bos">Bugün sırada kimse yok. Sabah FounderOS\'a "günaydın" yaz, günün listesi kurulunca burası dolar.</div>';saha.innerHTML=h;bagla();return}
 gunluk.forEach(function(r){
  var d=durum[r.kisa_ad]||{};var kanal=d.kanal||kanalTahmin(r);var yazi=kanal!=='telefon';var mod=d.mod||modTahmin(r);
  var dug=SONUC.filter(function(s){return !s[3]||(s[3]==='telefon'&&!yazi)||(s[3]==='yazi'&&yazi)}).map(function(s){return'<button data-s="'+s[0]+'" class="'+(d.sonuc===s[0]?'secili '+s[2]:'')+'">'+s[1]+'</button>'}).join('');
  h+='<div class="kart'+(r._gecmis?' gecmis':'')+(d.sonuc?' bitti':'')+'" data-k="'+kac(r.kisa_ad)+'"><div class="oku"><div class="kucuk baslik">Önce oku</div>'
   +'<div class="ad">'+kac(r.kisa_ad||r.ad)+etiketler(r)+(r._gecmis?' '+rozet('günü geçmiş: '+tarihTr(r.siradaki_tarih),'uyari'):'')+'</div>'
   +'<div class="tel">'+telLink(r.telefon)+'</div><div class="satirlar">'
   +(r.sahibi?'<div><span>Kim</span>'+kac(r.sahibi)+'</div>':'<div><span>Kim</span><i class="kucuk">adı bulunamadı; "işletme sahibi siz misiniz" ile başla, adı öğrenince nota yaz</i></div>')
   +(r.semt?'<div><span>İlçe</span>'+kac(r.semt)+(r.yorum_sayisi?' · '+kac(r.yorum_sayisi)+' yorum':'')+'</div>':'')
   +(r.baglayan?'<div><span>Bağlayan</span>'+kac(r.baglayan)+'</div>':'')
   +(r.bulgu?'<div><span>Doğrulanmış gözlem</span>'+kac(r.bulgu)+'</div>'
      :(profilKancasi(r)?'<div><span>Profilden gözlem</span>'+kac(profilKancasi(r))+' <i class="kucuk">denetim yapılmadı; bu satır Google profilinden geliyor</i></div>'
        :'<div><span>Doğrulanmış gözlem</span><i class="kucuk">yok; kartın açılış sorusuyla başla, "sürekli kaçırıyorsunuz" deme</i></div>'))
   +(r.kanca?'<div><span>Kanca</span>'+kac(r.kanca)+'</div>':'')
   +(r.siradaki_hareket?'<div><span>Bugün</span>'+kac(r.siradaki_hareket)+'</div>':'')
   +(r.son_temas_tarihi?'<div><span>Geçmiş</span>'+tarihTr(r.son_temas_tarihi)+(r.son_temas_kanali?', '+kac(KANAL[r.son_temas_kanali]||r.son_temas_kanali):'')+(r.temas_sayisi?' ('+kac(r.temas_sayisi)+'. temas)':'')+'</div>':'<div><span>Geçmiş</span>ilk temas</div>')
   +(r.not?'<div><span>Not</span>'+kac(r.not)+'</div>':'')+(r.instagram&&yazi?'<div><span>Instagram</span><a href="'+kac(r.instagram)+'" target="_blank">aç</a></div>':'')
   +'</div></div><div class="soyle-alani"><div class="kucuk baslik">Söyle</div>'
   +(yazi?'<div class="kucuk">Yazı kanalı: metni FounderOS hazırlar, sen gönderirsin; gönderince "Gönderdim" düğmesine bas.</div>':soylePanel(r,mod))
   +'</div><div class="sonuc-alani">'
   +'<div class="kanal">Kanal <select data-kanal>'+['telefon','instagram','e-posta','video'].map(function(k){return'<option value="'+k+'"'+(k===kanal?' selected':'')+'>'+KANAL[k]+'</option>'}).join('')+'</select></div>'
   +'<div class="sonuc">'+dug+'</div>'
   +'<div class="ek">'+(d.sonuc==='randevu'?'<input type="datetime-local" data-randevu value="'+kac(d.randevu||'')+'">':'')+(d.sonuc==='sonra'?'<input type="date" data-sonra value="'+kac(d.sonra||gunEkle(7))+'">':'')
   +'<input type="text" data-not placeholder="Kısa not (kim açtı, ne dedi, ne zaman ara)" value="'+kac(d.not||'')+'"></div>'
   +'</div></div>'});
 saha.innerHTML=h;bagla();
}
function bagla(){
 saha.querySelectorAll('.kart').forEach(function(k){var ad=k.dataset.k;
  k.querySelectorAll('.sonuc button').forEach(function(b){b.addEventListener('click',function(){var d=durum[ad]||{};d.sonuc=(d.sonuc===b.dataset.s)?'':b.dataset.s;d.kanal=k.querySelector('[data-kanal]').value;if(d.sonuc==='sonra'&&!d.sonra)d.sonra=gunEkle(7);durum[ad]=d;durumYaz(durum);sahaCiz()})});
  k.querySelectorAll('.modlar button[data-mod]').forEach(function(b){b.addEventListener('click',function(){var d=durum[ad]||{};d.mod=b.dataset.mod;durum[ad]=d;durumYaz(durum);sahaCiz()})});
  k.querySelectorAll('button[data-kop]').forEach(function(b){b.addEventListener('click',function(){
    var t=b.dataset.kop, e=b.textContent;
    function bitti(){b.textContent='Kopyalandı';setTimeout(function(){b.textContent=e},1400)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(bitti,function(){yedekKopya(t,bitti)})}
    else yedekKopya(t,bitti);
  })});
  k.querySelector('[data-kanal]').addEventListener('change',function(e){var d=durum[ad]||{};d.kanal=e.target.value;durum[ad]=d;durumYaz(durum);sahaCiz()});
  k.querySelectorAll('[data-not],[data-randevu],[data-sonra]').forEach(function(i){i.addEventListener('input',function(e){var d=durum[ad]||{};if(i.hasAttribute('data-not'))d.not=e.target.value;else if(i.hasAttribute('data-randevu'))d.randevu=e.target.value;else d.sonra=e.target.value;durum[ad]=d;durumYaz(durum)})});
 });
 saha.querySelectorAll('[data-itiraz]').forEach(function(b){b.addEventListener('click',function(){cekmeceAc(true)})});
 var kop=document.getElementById('kopyala'),tem=document.getElementById('temizle'),alan=document.getElementById('kopya-alani');
 if(kop)kop.addEventListener('click',function(){var m=sonucMetni();if(!m){alan.innerHTML='<div class="mesaj">Henüz sonuç girilmedi. Her adayın altındaki düğmelerden birine bas.</div>';return}
  var ta=document.createElement('textarea');ta.className='cikti';ta.value=m;alan.innerHTML='<div class="mesaj" id="kopya-mesaj">Kopyalandı. FounderOS\'a git, yazı kutusuna yapıştır ve gönder; listeyi o işler.</div>';alan.appendChild(ta);
  var ok=false;try{ta.select();ok=document.execCommand('copy')}catch(e){}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(m).then(function(){},function(){if(!ok)document.getElementById('kopya-mesaj').textContent='Kopyalanamadı; aşağıdaki metni seçip kendin kopyala (Cmd+A, Cmd+C), FounderOS\'a yapıştır.'})}
  else if(!ok)document.getElementById('kopya-mesaj').textContent='Aşağıdaki metni seçip kopyala, FounderOS\'a yapıştır.'});
 if(tem)tem.addEventListener('click',function(){if(tem.dataset.onay==='1'){durum={};durumYaz(durum);sahaCiz();return}tem.dataset.onay='1';tem.textContent='Evet, bugünün sonuçlarını sil';setTimeout(function(){tem.dataset.onay='';tem.textContent='Temizle'},4000)});
}
function sonucMetni(){var s=[];gunluk.forEach(function(r){var d=durum[r.kisa_ad];if(!d||!d.sonuc)return;var p=[r.kisa_ad,d.kanal||kanalTahmin(r),({acmadi:'açmadı',gonderdim:'gönderdim',istemedi:'istemedi',ilgilendi:'ilgilendi',randevu:'randevu',sonra:'sonra'})[d.sonuc]];
 if(d.sonuc==='randevu'&&d.randevu)p.push('randevu: '+d.randevu.replace('T',' '));if(d.sonuc==='sonra'&&d.sonra)p.push('tarih: '+d.sonra);if(d.not)p.push('not: '+d.not.replace(/\|/g,'/'));s.push(p.join(' | '))});
 return s.length?'FounderOS saha sonuçları '+BUGUN+'\n'+s.join('\n'):''}
// --- sekmeler ---
var sekListe=document.getElementById('sek-liste'),sekSaha=document.getElementById('sek-saha'),listeUst=document.getElementById('liste-ust');
function sekme(s){sekListe.classList.toggle('aktif',s==='liste');sekSaha.classList.toggle('aktif',s==='saha');icerik.classList.toggle('gizli',s!=='liste');listeUst.classList.toggle('gizli',s!=='liste');saha.classList.toggle('gizli',s!=='saha');if(s==='saha')sahaCiz();try{localStorage.setItem('founderos-sekme',s)}catch(e){}}
sekListe.addEventListener('click',function(){sekme('liste')});sekSaha.addEventListener('click',function(){sekme('saha')});
var ilk='liste';try{ilk=localStorage.getItem('founderos-sekme')||'liste'}catch(e){}if(ilk==='saha'&&gunluk.length)sekme('saha');
})();
</script>
</body>
</html>
````
