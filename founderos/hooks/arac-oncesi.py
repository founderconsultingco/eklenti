#!/usr/bin/env python3
"""FounderOS PreToolUse kancasi.

adaylar.csv'nin aday araci disinda elle degistirilmesini engeller. Aday
listesi 47 sutunlu, tekrar eleme ve tarih hesaplari aracin icinde; elle
yazilan tek satir listeyi bozuyor. Engellenen islemde cikis kodu 2 ve sebep
stderr'e gider; Claude araci kullanarak yeniden dener.

panel_yaz'in dogrudan cagrisini da denetler. 0.75 sunucusu gelen bolumu bastan yaziyordu,
gonderilmeyen alan panelden siliniyordu (0.76'da sunucu alanlari birlestirir). 2 Ekim z1: model ajans bolumunu her adimda
yalniz yeni alanla gonderdi (once pazar, sonra ideal musteri, sonra fiyat); son
gonderimde pazar, ideal musteri, fark ve teklif silindi, panel "Sirada pazar secimi"
dedi. Dogrudan cagri ancak gonderilen her alan klasordeki .founderos/panel/<bolum>.json ile ayniysa gecer
(dosya tek kayittir; panel ondan beslenir).

saha_yukle'nin dogrudan cagrisi da ayni yoldan: sunucu ayni gunun listesini gelenle
degistirir. 2 Ekim z1 gun 11: arac listeyi yukleyip baglantiyi bastiktan sonra model
saha_yukle'yi bos aday listesiyle cagirdi (sunucu bos diye reddetti; kisa bir liste
telefondaki on satirlik listenin yerine gecerdi). Dogrudan cagri ancak
.founderos/saha-paketi.json'un tamamiysa gecer.

Ogrencinin klasoru bu ortamda gorunmuyorsa (bulut oturumu, klasor bilgisayarda)
iki denetim de atlanir: dosyayla karsilastirilamayan cagri engellenmez.
"""
import json
import os
import re
import sys

YAZMA = re.compile(r"(>|\bsed\s+-i|\btee\b|\btruncate\b|\brm\b|\bmv\b|\bcp\b|\bperl\s+-p?i)")
# Her gonderimde degisen alanlar karsilastirilmaz.
DEGISKEN = ("surum", "guncellendi")


def _sade(d):
    return {k: v for k, v in d.items() if k not in DEGISKEN} if isinstance(d, dict) else d


def _musteri_adi(x):
    """Sunucunun musteri eslemesiyle ayni: kucuk harf, aksansiz, harf ve rakam disi bosluk."""
    if not isinstance(x, dict) or not isinstance(x.get("ad"), str):
        return ""
    import unicodedata
    t = x["ad"].replace("I", "ı").replace("İ", "i").lower()
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn").replace("ı", "i")
    return " ".join("".join(c if c.isalnum() and c.isascii() else " " for c in t).split())


def _musteriler_tutarli(gelen, yerel):
    """Teslimat musterileri sunucuda adla birlesir: gelen her satir dosyadaki ayni adli musterinin parcasi olmali;
    "sil": true gelen ad dosyada olmamali."""
    if not isinstance(gelen, list) or not isinstance(yerel, list):
        return False
    dosya = {_musteri_adi(m): m for m in yerel if _musteri_adi(m)}
    for m in gelen:
        a = _musteri_adi(m)
        if not a:
            return False
        if m.get("sil") is True:
            if a in dosya:
                return False
            continue
        y = dosya.get(a)
        if not isinstance(y, dict) or any(k not in y or y[k] != v for k, v in m.items() if k != "ad"):
            return False
    return True


def ogrenci_koku(cwd):
    """Ogrencinin klasoru: .founderos'u olan ilk aday kok. Gorunmuyorsa None."""
    for kok in dict.fromkeys([cwd, os.environ.get("CLAUDE_PROJECT_DIR"), os.getcwd()]):
        if kok and os.path.isdir(os.path.join(kok, ".founderos")):
            return kok
    return None


def saha_yukle_denetle(girdi, kok):
    """Dogrudan saha_yukle cagrisi aracin paket dosyasinin tamami mi. Sorun yoksa None, varsa sebep."""
    if not kok:
        return None
    paket = girdi.get("paket")
    if isinstance(paket, str):
        try:
            paket = json.loads(paket)
        except Exception:
            return None
    if not isinstance(paket, dict):
        return None
    yol = os.path.join(kok, ".founderos", "saha-paketi.json")
    if not os.path.isfile(yol):
        return ("FounderOS: günün saha listesini aday aracı kurar ve yükler: `python3 .founderos/adaylar-arac.py "
                "saha-paketi --yukle`. saha_yukle'yi yalnız araç 'saha ekranı yüklenmedi' derse, "
                "`.founderos/saha-paketi.json` dosyasının tamamıyla çağırırsın. Öğrenciye bundan söz etme.")
    try:
        with open(yol, encoding="utf-8") as f:
            yerel = json.load(f)
    except Exception:
        return None
    if not isinstance(yerel, dict) or paket == yerel:
        return None
    yerel_say = len(yerel.get("adaylar") or []) if isinstance(yerel.get("adaylar"), list) else 0
    gelen = paket.get("adaylar")
    gelen_say = len(gelen) if isinstance(gelen, list) else 0
    return ("FounderOS: gönderdiğin saha paketi `.founderos/saha-paketi.json` ile aynı değil (dosyada %d aday, "
            "gönderdiğinde %d). Sunucu aynı günün listesini gelenle değiştirir; eksik liste telefondaki listeyi kısaltır. "
            "Araç 'saha ekranı:' satırını bastıysa liste zaten yüklü, yeniden gönderme; basmadıysa dosyanın tamamını "
            "olduğu gibi gönder. Listeyi değiştireceksen önce `bugun --planla`, sonra `saha-paketi --yukle`. "
            "Öğrenciye bundan söz etme." % (yerel_say, gelen_say))


def panel_yaz_denetle(girdi, kok):
    """Dogrudan panel_yaz cagrisi bolumun tamamini mi gonderiyor. Sorun yoksa None, varsa sebep."""
    if not kok:
        return None
    bolumler = girdi.get("bolumler")
    if isinstance(bolumler, str):
        try:
            bolumler = json.loads(bolumler)
        except Exception:
            return None
    if not isinstance(bolumler, dict) or not bolumler:
        return None
    tam = girdi.get("tam")
    tamlar = set(bolumler) if tam is True else {x for x in tam if isinstance(x, str)} if isinstance(tam, list) else set()
    for bolum, veri in bolumler.items():
        if veri is None:
            continue
        if bolum == "adaylar":
            return ("FounderOS: adaylar bölümünü aday aracı listeden hesaplar, elle gönderilmez. "
                    "`python3 .founderos/adaylar-arac.py panel --yukle` çalıştır.")
        yol = os.path.join(kok, ".founderos", "panel", bolum + ".json")
        yukle = ("Önce `.founderos/panel/%s.json` dosyasını tamamıyla yaz (founderos:panel-vitrini şeması; o bölüme "
                 "bugüne kadar giden her şey dahil, İş Beyni'nden), sonra `python3 .founderos/adaylar-arac.py panel --yukle` "
                 "çalıştır (araç yoksa founderos:aday-listesi-araci ile kur) ya da panel_yaz'a dosyanın tamamını gönder. "
                 "Öğrenciye bundan söz etme." % bolum)
        if not os.path.isfile(yol):
            return ("FounderOS: panelin her bölümünün tek kaydı klasördeki dosyasıdır; dosya yokken doğrudan gönderim panelle klasörü ayırır. " + yukle)
        try:
            with open(yol, encoding="utf-8") as f:
                yerel = json.load(f)
        except Exception:
            continue
        if not isinstance(yerel, dict):
            continue
        if not isinstance(veri, dict):
            return ("FounderOS: %s bölümü nesne olarak gider, metin olarak değil. `python3 .founderos/adaylar-arac.py panel --yukle` "
                    "çalıştır ya da dosyanın tamamını nesne olarak gönder. Öğrenciye bundan söz etme." % bolum)
        if bolum in tamlar:
            # tam: sunucu bolumu oldugu gibi yazar; yalniz dosyanin tamami gidebilir.
            if _sade(veri) != _sade(yerel):
                return ("FounderOS: tam ile giden %s bölümü panelde olduğu gibi yazılır; yalnız `.founderos/panel/%s.json` "
                        "dosyasının tamamı gider. `python3 .founderos/adaylar-arac.py panel --yukle` çalıştır. Öğrenciye bundan söz etme."
                        % (bolum, bolum))
            continue
        # Sunucu gelen alanlari eskisinin ustune yazar, gelmeyeni korur: dosyanin bir kismini gondermek
        # paneli silmez. Gonderilen her alan dosyadakiyle ayni olmali; yoksa dosya ile panel ayrisir ve
        # sonraki "panel --yukle" eski degeri geri yazar. null dosyada olmayan alani panelden siler (dosyayla
        # tutarli); teslimat musterileri adla eslenir.
        gelen = _sade(veri)
        dosya = _sade(yerel)
        fazla = sorted(k for k, v in gelen.items() if k not in dosya and v is not None)
        farkli = sorted(k for k, v in gelen.items() if k in dosya and v != dosya[k]
                        and not (bolum == "teslimat" and k == "musteriler" and _musteriler_tutarli(v, dosya[k])))
        if fazla or farkli:
            return ("FounderOS: gönderdiğin %s bölümü klasördeki `.founderos/panel/%s.json` ile aynı değil (%s). Önce dosyayı "
                    "güncelle, sonra `python3 .founderos/adaylar-arac.py panel --yukle` çalıştır ya da dosyanın tamamını gönder. "
                    "Öğrenciye bundan söz etme."
                    % (bolum, bolum, "; ".join(x for x in (
                        ("dosyada olmayan alanlar: %s" % ", ".join(fazla)) if fazla else "",
                        ("dosyadakinden farklı alanlar: %s" % ", ".join(farkli)) if farkli else "") if x)))
    return None


def main():
    try:
        g = json.load(sys.stdin)
    except Exception:
        return 0
    ad = g.get("tool_name") or ""
    girdi = g.get("tool_input") or {}
    if ad.endswith("panel_yaz") or ad.endswith("saha_yukle"):
        denetle = panel_yaz_denetle if ad.endswith("panel_yaz") else saha_yukle_denetle
        sebep = denetle(girdi, ogrenci_koku(g.get("cwd")))
        if sebep:
            sys.stderr.write(sebep + "\n")
            return 2
        return 0
    if ad in ("Write", "Edit", "MultiEdit"):
        yol = str(girdi.get("file_path") or "")
        if os.path.basename(yol) == "adaylar.csv":
            sys.stderr.write("FounderOS: adaylar.csv elle düzenlenmez. Aday aracının komutunu kullan (.founderos/adaylar-arac.py ekle, guncelle, temas, sonuclar, sil).\n")
            return 2
        return 0
    if ad == "Bash" or ad.endswith("device_bash"):
        komut = str(girdi.get("command") or "")
        if "adaylar.csv" in komut and "adaylar-arac.py" not in komut and YAZMA.search(komut):
            sys.stderr.write("FounderOS: adaylar.csv'yi kabukla değiştirme. Aday aracının komutunu kullan (.founderos/adaylar-arac.py ...).\n")
            return 2
    return 0


if __name__ == "__main__":
    try:
        kod = main()
    except Exception:
        kod = 0
    sys.exit(kod)
