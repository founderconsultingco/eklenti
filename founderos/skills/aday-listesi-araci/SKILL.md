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

Öğrenci bu klasörü ve dosyaları görmez, ona anlatılmaz. Komutlar sohbete yazılmaz.

Aracın sürümü: 0.23.0

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
  sil ANAHTAR --sebep "..."  (satırı elenme ile işaretler, silmez)
  bugun [--sayi N] [--planla] [--kanal telefon|yazı]
  ozet
  bul METIN
  sayfa [--nis AD] [--acilis "..."] [--itiraz "..."]...
  surum
"""
import argparse, csv, datetime, io, json, os, re, shutil, sys, unicodedata
from pathlib import Path

SURUM = "0.23.0"
IST = datetime.timezone(datetime.timedelta(hours=3))

SERVIS = ["kisa_ad", "ad", "telefon", "eposta", "instagram", "site", "adres", "semt",
          "yorum_sayisi", "puan", "kategori", "ipuclari", "elenme", "harita"]
EKLENEN = ["eklenme_tarihi", "kaynak", "baglayan", "yuz", "sahibi", "uygunluk", "sizinti",
           "bulgu", "kanca", "lira", "denetim_tarihi", "asama", "telefon_durumu",
           "eposta_durumu", "instagram_durumu", "video_durumu", "temas_sayisi",
           "son_temas_tarihi", "son_temas_kanali", "siradaki_hareket", "siradaki_tarih",
           "randevu_tarihi", "not"]
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
    return " | ".join([s["kisa_ad"] or s["ad"], s["telefon"] or "telefon yok", s["sahibi"] or "sahibi ?",
                       "sızıntı " + (s["sizinti"] or "-"), s["asama"] or "yeni",
                       ("son " + s["son_temas_tarihi"] + " " + s["son_temas_kanali"]).strip() if s["son_temas_tarihi"] else "temas yok",
                       ("sıradaki " + s["siradaki_tarih"] + " " + s["siradaki_hareket"]).strip() if s["siradaki_tarih"] else "sıradaki yok",
                       s["bulgu"] or ""]).rstrip(" |")


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


def takip_gunu(s):
    """Yazılı kanal zinciri: ilk mesajdan 3, 7 ve 14 gün sonra takip. Bu gönderim kaçıncıysa sıradaki takibin
    kaç gün sonra olduğunu ve adını verir; dördüncü gönderimden sonra zincir biter."""
    n = int(s["temas_sayisi"] or 0) + 1
    return {1: (3, "3. gün takibi"), 2: (4, "7. gün takibi"), 3: (7, "14. gün takibi")}.get(n)


SONUC_KELIME = {"açmadı": "acmadi", "acmadi": "acmadi", "gönderdim": "gonderdim", "gonderdim": "gonderdim",
                "istemedi": "istemedi", "ilgilendi": "ilgilendi", "randevu": "randevu", "sonra": "sonra"}


def kmt_sonuclar(a):
    satirlar = yukle()
    p = Path(a.dosya)
    if not p.exists():
        hata("dosya yok: %s" % a.dosya)
    metin = p.read_text(encoding="utf-8-sig")
    islenen, bulunamayan, anlasilmayan = [], [], []
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
        islenen.append(ozet_satir(s))
    kaydet(satirlar)
    print("işlenen %d, bulunamayan %d, anlaşılmayan %d" % (len(islenen), len(bulunamayan), len(anlasilmayan)))
    for x in islenen:
        print("  " + x)
    if bulunamayan:
        print("bulunamayan (elle bak): " + "; ".join(bulunamayan))
    if anlasilmayan:
        print("anlaşılmayan satırlar (elle işle):")
        for x in anlasilmayan:
            print("  " + x)


def kmt_sil(a):
    satirlar = yukle()
    s = satir_bul(satirlar, a.anahtar, a.semt)
    s["elenme"] = a.sebep
    s["asama"] = "kapandı"
    s["siradaki_hareket"] = ""
    s["siradaki_tarih"] = ""
    kaydet(satirlar)
    print("listeden çıkarıldı (satır duruyor, elenme=%s): %s" % (a.sebep, s["kisa_ad"]))


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
    print("bugün %s: cevap verenler %d, takibi gelen %d, denetimi hazır %d, denetimsiz %d; ilk %d gösteriliyor" %
          (g, len(cevap), len(takip), len(hazir), len(denetsiz), len(liste)))
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
    bugun_temas = say(lambda s: s["son_temas_tarihi"] == g)
    print("bugün temas edilen %d, toplam temas %d" % (bugun_temas, sum(int(s["temas_sayisi"] or 0) for s in canli)))
    if canli:
        print("son eklenme %s, kaynaklar: %s" % (max(s["eklenme_tarihi"] for s in canli), ", ".join(sorted({s["kaynak"] for s in canli if s["kaynak"]}))))


def kmt_bul(a):
    satirlar = yukle()
    k = kucult(a.metin)
    t = rakam(a.metin)
    esle = [s for s in satirlar if k in kucult(s["kisa_ad"]) or k in kucult(s["ad"]) or k in kucult(s["sahibi"]) or k in kucult(s["semt"]) or (t and t in rakam(s["telefon"]))]
    print("%d eşleşme" % len(esle))
    for s in esle[:20]:
        print(ozet_satir(s) + (" | ELENDİ: " + s["elenme"] if s["elenme"] else "") + (" | not: " + s["not"] if s["not"] else ""))


def kmt_sayfa(a):
    if a.nis or a.acilis or a.itiraz:
        n = nis_oku()
        if a.nis:
            n["ad"] = a.nis
        if a.acilis:
            n["acilis"] = a.acilis
        if a.itiraz:
            n["itirazlar"] = a.itiraz
        calisma().mkdir(parents=True, exist_ok=True)
        (calisma() / "sayfa.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")
    if not (KLASOR / "adaylar.csv").exists():
        kaydet([], sayfa_da=False)
    sayfa_uret()
    h = KLASOR / "adaylar.html"
    print("sayfa yenilendi: adaylar.html (%d bayt), %s" % (h.stat().st_size, simdi_metin()))


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
    y.add_argument("--nis")
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
    {"cek": kmt_cek, "ekle": kmt_ekle, "guncelle": kmt_guncelle, "temas": kmt_temas, "sonuclar": kmt_sonuclar,
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
.nis{background:var(--w);border:1px solid var(--l);border-radius:8px;padding:10px 14px;margin-bottom:12px;font-size:13px}
.nis b{display:block;margin-bottom:4px}
.nis ol{margin:4px 0 0 18px;padding:0}
.kart{background:var(--w);border:1px solid var(--l);border-radius:8px;padding:12px 14px;margin-bottom:10px;display:grid;grid-template-columns:minmax(260px,1.2fr) minmax(260px,1fr);gap:8px 20px}
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
.mesaj{background:#dcfce7;color:#166534;border-radius:8px;padding:8px 12px;margin:8px 0;font-size:13px}
@media (max-width:700px){.kart{grid-template-columns:1fr}}
@media print{header{position:static}.arac,.cip,.sekme,.saha-ust,.sonuc,.kanal,.ek{display:none}tr.detay{display:none}}
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
  </div>
</header>
<main>
  <div id="icerik"></div>
  <div id="saha" class="gizli"></div>
</main>
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
var IPUCU={profil_sahipsiz:['Profili sahipsiz','uyari'],site_yok:['Sitesi yok','uyari'],instagram_yok:['Instagram yok',''],yorum_az:['Yorumu az',''],aksam_kapali:['Akşam kapalı','uyari'],hafta_sonu_kapali:['Hafta sonu kapalı','uyari'],pazar_kapali:['Pazar kapalı',''],saat_yok:['Saati yazmıyor','']};
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
var OZET=[['Toplam',satirlar.length],['Telefonu olan',say(function(r){return r.telefon})],['E-postası olan',say(function(r){return r.eposta})],['Denetlenmiş',say(function(r){return r.sizinti!==''})],['En çok istenen yüz',say(function(r){return r._yuz})],['Bugün sırada',say(function(r){return r._bugun})],['Gecikmiş',say(function(r){return r._gecmis})],['Cevap verdi',say(function(r){return /cevap verdi/.test(r.asama||'')})],['Randevu',say(function(r){return /randevu/.test(r.asama||'')||r.randevu_tarihi})]];
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

// --- saha modu: günün listesi, sonuç düğmeleri, sonuçları kopyala ---
var gunluk=satirlar.filter(function(r){return r._bugun||r._gecmis}).sort(function(a,b){var ca=/cevap verdi|randevu/.test(a.asama||'')|0,cb=/cevap verdi|randevu/.test(b.asama||'')|0;return cb-ca||(b._gecmis|0)-(a._gecmis|0)||(b._yuz|0)-(a._yuz|0)||(parseInt(b.sizinti,10)||0)-(parseInt(a.sizinti,10)||0)});
var ANAHTAR='founderos-saha-'+BUGUN;
function durumOku(){try{return JSON.parse(localStorage.getItem(ANAHTAR)||'{}')}catch(e){return{}}}
function durumYaz(d){try{localStorage.setItem(ANAHTAR,JSON.stringify(d))}catch(e){}}
var durum=durumOku();
function kanalTahmin(r){var h=(r.siradaki_hareket||'').toLocaleLowerCase('tr');if(/instagram/.test(h))return'instagram';if(/e-?posta|mail/.test(h))return'e-posta';if(/video/.test(h))return'video';if(/yazı|mesaj/.test(h))return r.instagram?'instagram':r.eposta?'e-posta':'telefon';return'telefon'}
var SONUC=[['acmadi','Açmadı','kotu','telefon'],['gonderdim','Gönderdim','','yazi'],['istemedi','İstemedi','kotu',''],['ilgilendi','İlgilendi','iyi',''],['randevu','Randevu','iyi',''],['sonra','Sonra ara','','']];
document.getElementById('saha-sayi').textContent=gunluk.length?gunluk.length:'';
function sahaCiz(){
 var giren=gunluk.filter(function(r){return durum[r.kisa_ad]&&durum[r.kisa_ad].sonuc}).length;
 var h='<div class="saha-ust"><span class="kucuk">'+(gunluk.length?gunluk.length+' aday sırada · '+giren+' sonuç girildi · '+(gunluk.length-giren)+' kaldı':'')+'</span>'
  +'<button class="dugme ana" id="kopyala">Sonuçları kopyala</button><button class="dugme kirmizi" id="temizle">Temizle</button></div><div id="kopya-alani"></div>';
 if(NIS.acilis||(NIS.itirazlar&&NIS.itirazlar.length)){h+='<div class="nis">'+(NIS.acilis?'<b>Açılış cümlesi</b><div>'+kac(NIS.acilis)+'</div>':'')+(NIS.itirazlar&&NIS.itirazlar.length?'<b style="margin-top:8px">İtiraz gelirse</b><ol>'+NIS.itirazlar.map(function(x){return'<li>'+kac(x)+'</li>'}).join('')+'</ol>':'')+'</div>'}
 if(!gunluk.length){h+='<div class="bos">Bugün sırada kimse yok. Sabah FounderOS\'a "günaydın" yaz, günün listesi kurulunca burası dolar.</div>';saha.innerHTML=h;bagla();return}
 gunluk.forEach(function(r){
  var d=durum[r.kisa_ad]||{};var kanal=d.kanal||kanalTahmin(r);var yazi=kanal!=='telefon';
  var dug=SONUC.filter(function(s){return !s[3]||(s[3]==='telefon'&&!yazi)||(s[3]==='yazi'&&yazi)}).map(function(s){return'<button data-s="'+s[0]+'" class="'+(d.sonuc===s[0]?'secili '+s[2]:'')+'">'+s[1]+'</button>'}).join('');
  h+='<div class="kart'+(r._gecmis?' gecmis':'')+(d.sonuc?' bitti':'')+'" data-k="'+kac(r.kisa_ad)+'"><div>'
   +'<div class="ad">'+kac(r.kisa_ad||r.ad)+etiketler(r)+(r._gecmis?' '+rozet('günü geçmiş: '+tarihTr(r.siradaki_tarih),'uyari'):'')+'</div>'
   +'<div class="tel">'+telLink(r.telefon)+'</div><div class="satirlar">'
   +(r.sahibi?'<div><span>Sahibi</span>'+kac(r.sahibi)+'</div>':'<div><span>Sahibi</span><i class="kucuk">bulunamadı, telefonu açana sor</i></div>')
   +(r.semt?'<div><span>İlçe</span>'+kac(r.semt)+(r.yorum_sayisi?' · '+kac(r.yorum_sayisi)+' yorum':'')+'</div>':'')
   +(r.bulgu?'<div><span>Bulgu</span>'+kac(r.bulgu)+'</div>':'')+(r.kanca?'<div><span>Kanca</span>'+kac(r.kanca)+'</div>':'')+(r.lira?'<div><span>Lira karşılığı</span>'+kac(r.lira)+'</div>':'')
   +(r.siradaki_hareket?'<div><span>Bugün</span>'+kac(r.siradaki_hareket)+'</div>':'')
   +(r.son_temas_tarihi?'<div><span>Son temas</span>'+tarihTr(r.son_temas_tarihi)+(r.son_temas_kanali?', '+kac(KANAL[r.son_temas_kanali]||r.son_temas_kanali):'')+(r.temas_sayisi?' ('+kac(r.temas_sayisi)+'. temas)':'')+'</div>':'')
   +(r.not?'<div><span>Not</span>'+kac(r.not)+'</div>':'')+(r.instagram&&yazi?'<div><span>Instagram</span><a href="'+kac(r.instagram)+'" target="_blank">aç</a></div>':'')
   +'</div></div><div>'
   +'<div class="kanal">Kanal <select data-kanal>'+['telefon','instagram','e-posta','video'].map(function(k){return'<option value="'+k+'"'+(k===kanal?' selected':'')+'>'+KANAL[k]+'</option>'}).join('')+'</select></div>'
   +'<div class="sonuc">'+dug+'</div>'
   +'<div class="ek">'+(d.sonuc==='randevu'?'<input type="datetime-local" data-randevu value="'+kac(d.randevu||'')+'">':'')+(d.sonuc==='sonra'?'<input type="date" data-sonra value="'+kac(d.sonra||gunEkle(7))+'">':'')
   +'<input type="text" data-not placeholder="Kısa not (kim açtı, ne dedi)" value="'+kac(d.not||'')+'"></div>'
   +'</div></div>'});
 saha.innerHTML=h;bagla();
}
function bagla(){
 saha.querySelectorAll('.kart').forEach(function(k){var ad=k.dataset.k;
  k.querySelectorAll('.sonuc button').forEach(function(b){b.addEventListener('click',function(){var d=durum[ad]||{};d.sonuc=(d.sonuc===b.dataset.s)?'':b.dataset.s;d.kanal=k.querySelector('[data-kanal]').value;if(d.sonuc==='sonra'&&!d.sonra)d.sonra=gunEkle(7);durum[ad]=d;durumYaz(durum);sahaCiz()})});
  k.querySelector('[data-kanal]').addEventListener('change',function(e){var d=durum[ad]||{};d.kanal=e.target.value;durum[ad]=d;durumYaz(durum);sahaCiz()});
  k.querySelectorAll('[data-not],[data-randevu],[data-sonra]').forEach(function(i){i.addEventListener('input',function(e){var d=durum[ad]||{};if(i.hasAttribute('data-not'))d.not=e.target.value;else if(i.hasAttribute('data-randevu'))d.randevu=e.target.value;else d.sonra=e.target.value;durum[ad]=d;durumYaz(durum)})});
 });
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
