# -*- coding: utf-8 -*-
"""Marka kitinin gercek dosyalarini uretir.

Girdi : marka/marka-kiti.html  (ortak/marka-sablonu.html'in doldurulmus kopyasi)
Cikti : marka/logo/, marka/site-gorselleri/, marka/sosyal/, marka/kurumsal/

Calistirma (FounderOS calistirir, ogrenci terminale girmez):
  python3 marka-uret.py <marka klasoru>

Nasil calisiyor: sablonun kendisi her varligi #v-<ad> adresinde tam olcusunde
ciziyor. Bu betik bir tarayiciyi gorunmez kipte acip her adresi o olcude
ekran goruntusu aliyor, PDF olanlari yazdiriyor. Tarayici bulunamazsa
uretebildigini uretiyor, uretemedigini raporluyor; sessizce gecmiyor.
"""
import glob, json, os, shutil, subprocess, sys, tempfile

# (ad, klasor, bicim, olcek)  bicim: png | png-saydam | pdf
VARLIKLAR = [
 ("logo-yatay-acik",     "logo",            "png",        2),
 ("logo-yatay-koyu",     "logo",            "png",        2),
 ("logo-dikey",          "logo",            "png",        2),
 ("sembol",              "logo",            "png-saydam", 2),
 ("sosyal-profil",       "logo",            "png",        1),
 ("whatsapp-profil",     "sosyal",          "png",        1),
 ("favicon",             "logo",            "png",        1),
 ("eposta-logo",         "logo",            "png",        2),
 ("ana-gorsel",          "site-gorselleri", "png",        2),
 ("baglanti-onizlemesi", "site-gorselleri", "png",        1),
 ("instagram-1",         "sosyal",          "png",        1),
 ("instagram-2",         "sosyal",          "png",        1),
 ("instagram-3",         "sosyal",          "png",        1),
 ("hikaye",              "sosyal",          "png",        1),
 ("kapak-banner",        "sosyal",          "png",        1),
 ("marka-karti",         "kurumsal",        "pdf",        1),
 ("kartvizit-on",        "kurumsal",        "pdf",        1),
 ("kartvizit-arka",      "kurumsal",        "pdf",        1),
 ("antetli",             "kurumsal",        "pdf",        1),
 ("onay-belgesi-kapak",  "kurumsal",        "pdf",        1),
 ("eposta-imzasi",       "kurumsal",        "png",        2),
]

ARANAN = [
 # macOS
 "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
 "/Applications/Chromium.app/Contents/MacOS/Chromium",
 "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
 "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
 # Linux paket kurulumlari
 "/usr/bin/chromium", "/usr/bin/chromium-browser",
 "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
 "/snap/bin/chromium",
]

DESEN = [
 # Claude'un calisma ortaminda hazir duran tarayici
 "/opt/pw-browsers/chromium*/chrome-linux/chrome",
 "/opt/pw-browsers/chromium*/chrome-mac/Chromium.app/Contents/MacOS/Chromium",
 os.path.expanduser("~/.cache/ms-playwright/chromium*/chrome-linux/chrome"),
 os.path.expanduser("~/Library/Caches/ms-playwright/chromium*/chrome-mac/Chromium.app/Contents/MacOS/Chromium"),
]

def tarayici():
    cevre = os.environ.get("FOS_TARAYICI")
    if cevre and os.path.exists(cevre):
        return cevre
    for y in ARANAN:
        if os.path.exists(y):
            return y
    for ad in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome"):
        y = shutil.which(ad)
        if y:
            return y
    for d in DESEN:
        bulunan = sorted(glob.glob(d))
        if bulunan:
            return bulunan[-1]
    return None

def pay_olc(tr, profil):
    """Gorunmez kipte --window-size dis pencere olcusudur; gorunen alan arac
    cubugu kadar kisa kalir ve ekran goruntusunun altinda beyaz serit birakir.
    Bu farki bir kez olcup her cekimde telafi ediyoruz."""
    sonda = os.path.join(profil, "sonda.html")
    io_yaz(sonda, "<title>x</title><script>document.title=innerWidth+'x'+innerHeight</script>")
    try:
        c = subprocess.run([tr, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--user-data-dir=" + profil, "--virtual-time-budget=1200",
                            "--window-size=800,800", "--dump-dom", "file://" + sonda],
                           capture_output=True, text=True, timeout=45).stdout
        import re as _re
        m = _re.search(r"<title>(\d+)x(\d+)</title>", c)
        if m:
            return max(0, 800 - int(m.group(2)))
    except Exception:
        pass
    return 0

def io_yaz(yol, metin):
    with open(yol, "w", encoding="utf-8") as d:
        d.write(metin)

def kirp(yol, en, boy):
    """Alttaki beyaz seridi atar. Once Pillow, sonra macOS sips."""
    try:
        from PIL import Image
        im = Image.open(yol)
        if im.size == (en, boy):
            return True
        im.crop((0, 0, en, boy)).save(yol)
        return True
    except Exception:
        pass
    if shutil.which("sips"):
        calistir(["sips", "-c", str(boy), str(en), "--cropOffset", "0", "0", yol], 30)
        return True
    return False

def calistir(cmd, sure=90):
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       timeout=sure, check=False)
        return True
    except Exception:
        return False

def main():
    kok = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "marka")
    kaynak = os.path.join(kok, "marka-kiti.html")
    if not os.path.exists(kaynak):
        print(json.dumps({"hata": "marka-kiti.html bulunamadi", "yol": kaynak},
                         ensure_ascii=False)); return 1

    tr = tarayici()
    sonuc = {"uretilen": [], "uretilemeyen": [], "tarayici": tr}
    if not tr:
        sonuc["hata"] = "tarayici-yok"
        sonuc["uretilemeyen"] = [a for a, _, _, _ in VARLIKLAR]
        print(json.dumps(sonuc, ensure_ascii=False)); return 2

    profil = tempfile.mkdtemp(prefix="fos-marka-")
    pay = pay_olc(tr, profil)
    sonuc["pay"] = pay

    VARSAYILAN = {
     "logo-yatay-acik": (1200, 300), "logo-yatay-koyu": (1200, 300),
     "logo-dikey": (900, 900), "sembol": (512, 512), "sosyal-profil": (1000, 1000),
     "whatsapp-profil": (1000, 1000), "favicon": (512, 512), "eposta-logo": (480, 120),
     "ana-gorsel": (1600, 900), "baglanti-onizlemesi": (1200, 630),
     "instagram-1": (1080, 1350), "instagram-2": (1080, 1350), "instagram-3": (1080, 1350),
     "hikaye": (1080, 1920), "kapak-banner": (1640, 856), "kartvizit-on": (1004, 650),
     "kartvizit-arka": (1004, 650), "antetli": (794, 1123), "marka-karti": (794, 1123),
     "onay-belgesi-kapak": (794, 1123), "eposta-imzasi": (560, 240),
    }

    for ad, klasor, bicim, olcek in VARLIKLAR:
        hedef_klasor = os.path.join(kok, klasor)
        os.makedirs(hedef_klasor, exist_ok=True)
        en, boy = VARSAYILAN[ad]
        url = "file://" + kaynak + "#v-" + ad
        if bicim == "pdf":
            hedef = os.path.join(hedef_klasor, ad + ".pdf")
            ok = calistir([tr, "--headless=new", "--disable-gpu", "--no-sandbox",
                           "--user-data-dir=" + profil, "--no-pdf-header-footer",
                           "--virtual-time-budget=2500",
                           "--print-to-pdf=" + hedef, url])
        else:
            hedef = os.path.join(hedef_klasor, ad + ".png")
            cmd = [tr, "--headless=new", "--disable-gpu", "--no-sandbox",
                   "--user-data-dir=" + profil, "--hide-scrollbars",
                   "--virtual-time-budget=2500",
                   "--force-device-scale-factor=" + str(olcek),
                   "--window-size=%d,%d" % (en, boy + pay),
                   "--screenshot=" + hedef]
            if bicim == "png-saydam":
                cmd.insert(1, "--default-background-color=00000000")
            ok = calistir(cmd + [url])
            if ok and pay and os.path.exists(hedef):
                ok = kirp(hedef, en * olcek, boy * olcek)
        if ok and os.path.exists(hedef) and os.path.getsize(hedef) > 900:
            sonuc["uretilen"].append(os.path.relpath(hedef, kok))
        else:
            sonuc["uretilemeyen"].append(ad)

    # favicon-32: buyuk favicondan kucultulur
    buyuk = os.path.join(kok, "logo", "favicon.png")
    kucuk = os.path.join(kok, "logo", "favicon-32.png")
    if os.path.exists(buyuk):
        if shutil.which("sips"):
            calistir(["sips", "-z", "32", "32", buyuk, "--out", kucuk], 30)
        if not os.path.exists(kucuk):
            try:
                from PIL import Image
                Image.open(buyuk).resize((32, 32), Image.LANCZOS).save(kucuk)
            except Exception:
                pass
        if os.path.exists(kucuk):
            sonuc["uretilen"].append("logo/favicon-32.png")
        else:
            sonuc["uretilemeyen"].append("favicon-32")

    shutil.rmtree(profil, ignore_errors=True)
    print(json.dumps(sonuc, ensure_ascii=False))
    return 0 if not sonuc["uretilemeyen"] else 3

if __name__ == "__main__":
    sys.exit(main())
