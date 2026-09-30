# -*- coding: utf-8 -*-
"""Haftanin iceriginin gorsellerini uretir: kaydirmali gonderi, YouTube kapagi, Reels kapaklari.

Girdi : ogrencinin klasorundeki .founderos/panel/icerik.json (panel dosyasi, window.ICERIK olur).
        Marka bilgisi dosyanin "marka" blogundan; eksik alan marka/marka-kiti.html'den tamamlanir.
Sablon: bu betigin yanindaki icerik-sablonu.html (dokunulmaz, kopyalanir).
Cikti : <hafta klasoru>/onizleme.html        haftanin panosu, tek dosya, yazi tipleri gomulu
        <hafta klasoru>/carousel/01.png ...  1080x1350, slayt basina bir dosya
        <hafta klasoru>/kapak.png            1280x720, YouTube kapagi
        <hafta klasoru>/reels-1.png ...      1080x1920, Reels kapaklari
        Hafta klasoru: hafta.klasor alani (ogrenci klasorune gore), yoksa icerik/<baslangic>-<konu>.

Calistirma (FounderOS calistirir, ogrenci terminale girmez; sessiz calisir):
  python3 icerik-uret.py <ogrenci klasoru> [--veri <json>] [--sadece-onizleme]

Nasil calisiyor: sablon her varligi #s-<n>, #kapak, #r-<n> adresinde tam olcusunde ciziyor.
Betik sablonun kopyasina veriyi ve yazi tiplerini gomer, gorunmez kipte bir tarayici acip
her adresin ekran goruntusunu alir. Once #kontrol adresinde metinlerin sigip sigmadigina bakar.
Internete cikmaz: yazi tipleri fontlar/ klasorunden, fotograf ogrencinin klasorunden gomulur.

Cikis kodlari:
  0  tamam, butun gorseller uretildi
  1  girdi hatasi (veri dosyasi yok ya da bozuk, sablon yok, slayt yok); hicbir sey yazilmadi
  2  tarayici bulunamadi; onizleme.html yazildi, gorsel uretilmedi
  3  bazi gorseller uretilemedi (liste "uretilemeyen" alaninda)
  4  gorseller uretildi ama bazi metinler en kucuk olcekte de sigmadi ("tasma"); metin kisaltilip
     betik yeniden calistirilir
Her durumda stdout'a tek satir JSON basilir; ogrenciye gosterilmez.
"""
import base64, glob, json, os, re, shutil, struct, subprocess, sys, tempfile, zlib

BURASI = os.path.dirname(os.path.abspath(__file__))
SURUM = "1.0"


def _ilk_var(*adaylar):
    for a in adaylar:
        if os.path.isdir(a):
            return a
    return adaylar[0]


# Fontlar markani-kur becerisinin yaninda duruyor; pakette iki kez tasinmasin diye oradan da okunur.
FONT_KLASORU = _ilk_var(os.path.join(BURASI, "fontlar"),
                        os.path.join(BURASI, "..", "markani-kur", "fontlar"),
                        os.path.join(BURASI, "..", "..", "ortak", "fontlar"))

ESLESME = {
 "teknik":    {"baslik": ("space-grotesk", "Space Grotesk", [500, 700]),
               "govde":  ("inter", "Inter", [400, 500, 600])},
 "karakter":  {"baslik": ("bricolage-grotesque", "Bricolage Grotesque", [600, 800]),
               "govde":  ("inter", "Inter", [400, 500, 600])},
 "editoryal": {"baslik": ("instrument-serif", "Instrument Serif", [400]),
               "govde":  ("inter", "Inter", [400, 500, 600])},
 "saglam":    {"baslik": ("archivo", "Archivo", [600, 800]),
               "govde":  ("inter", "Inter", [400, 500, 600])},
 "yumusak":   {"baslik": ("sora", "Sora", [600, 700]),
               "govde":  ("inter", "Inter", [400, 500, 600])},
 "sade":      {"baslik": ("manrope", "Manrope", [700, 800]),
               "govde":  ("manrope", "Manrope", [400, 500, 600])},
}
ARALIK = {
 "latin":     "U+0000-00FF,U+0131,U+2000-206F,U+20BA,U+2122,U+2191-2193",
 "latin-ext": "U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF",
}
PALETLER = ["gece", "murekkep", "orman", "koz", "celik", "bordo", "kum", "derin", "mor", "kiremit"]
ISARETLER = ["capraz", "hilal", "akis", "halka", "dugum", "kule", "dalga", "kivrim", "kademe",
             "mercek", "cekirdek", "yildiz"]
KILITLER = ["yatay", "dikey", "sadece-yazi"]
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}

ARANAN = [
 "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
 "/Applications/Chromium.app/Contents/MacOS/Chromium",
 "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
 "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
 "/usr/bin/chromium", "/usr/bin/chromium-browser",
 "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
 "/snap/bin/chromium",
 r"C:\Program Files\Google\Chrome\Application\chrome.exe",
 r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
 r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]
DESEN = [
 "/opt/pw-browsers/chromium*/chrome-linux/chrome",
 "/opt/pw-browsers/chromium*/chrome-mac/Chromium.app/Contents/MacOS/Chromium",
 os.path.expanduser("~/.cache/ms-playwright/chromium*/chrome-linux/chrome"),
 os.path.expanduser("~/Library/Caches/ms-playwright/chromium*/chrome-mac/Chromium.app/Contents/MacOS/Chromium"),
]


def bas(sonuc, kod):
    print(json.dumps(sonuc, ensure_ascii=False))
    return kod


def oku(yol):
    with open(yol, encoding="utf-8") as d:
        return d.read()


def yaz(yol, metin):
    with open(yol, "w", encoding="utf-8") as d:
        d.write(metin)


def tarayici():
    cevre = os.environ.get("FOS_TARAYICI")
    if cevre and os.path.exists(cevre):
        return cevre
    for y in ARANAN:
        if os.path.exists(y):
            return y
    for ad in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome", "msedge"):
        y = shutil.which(ad)
        if y:
            return y
    for d in DESEN:
        bulunan = sorted(glob.glob(d))
        if bulunan:
            return bulunan[-1]
    return None


TEMEL = ["--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--disable-background-networking", "--disable-component-update", "--disable-sync",
         "--no-first-run", "--no-default-browser-check", "--mute-audio"]


def calistir(cmd, sure=90):
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=sure, check=False)
        return True
    except Exception:
        return False


def dom_al(tr, profil, url, pencere="1280,1400", butce=4000):
    try:
        return subprocess.run([tr] + TEMEL + ["--user-data-dir=" + profil, "--virtual-time-budget=%d" % butce,
                               "--window-size=" + pencere, "--dump-dom", url],
                              capture_output=True, text=True, timeout=90, encoding="utf-8",
                              errors="replace").stdout or ""
    except Exception:
        return ""


def pay_olc(tr, profil):
    """Gorunmez kipte --window-size dis pencere olcusudur; gorunen alan kisa kalir ve ekran
    goruntusunun altinda serit birakir. Fark bir kez olculur, her cekimde telafi edilir."""
    sonda = os.path.join(profil, "sonda.html")
    yaz(sonda, "<title>x</title><script>document.title=innerWidth+'x'+innerHeight</script>")
    c = dom_al(tr, profil, dosya_url(sonda), "800,800", 1200)
    m = re.search(r"<title>(\d+)x(\d+)</title>", c)
    return max(0, 800 - int(m.group(2))) if m else 0


def dosya_url(yol):
    yol = os.path.abspath(yol).replace("\\", "/")
    if not yol.startswith("/"):
        yol = "/" + yol
    from urllib.parse import quote
    return "file://" + quote(yol, safe="/:")


# ---------- PNG: alttaki seridi kirpmak icin Pillow gerekmez ----------
def png_kirp(yol, boy):
    """PNG'nin yalniz ust `boy` satirini birakir. Filtreler yalniz ust satira baktigi icin alt
    satirlari atmak ust satirlari bozmaz; cozmeden kesilir. Once Pillow, olmazsa bu yol."""
    try:
        from PIL import Image
        im = Image.open(yol)
        if im.size[1] > boy:
            im.crop((0, 0, im.size[0], boy)).save(yol)
        return True
    except Exception:
        pass
    try:
        with open(yol, "rb") as d:
            veri = d.read()
        if veri[:8] != b"\x89PNG\r\n\x1a\n":
            return False
        i, parcalar, idat = 8, [], b""
        ihdr = None
        while i < len(veri):
            uzun = struct.unpack(">I", veri[i:i + 4])[0]
            tip = veri[i + 4:i + 8]
            govde = veri[i + 8:i + 8 + uzun]
            i += 12 + uzun
            if tip == b"IHDR":
                ihdr = govde
            elif tip == b"IDAT":
                idat += govde
            elif tip == b"IEND":
                break
            else:
                parcalar.append((tip, govde))
        en, eski_boy, derinlik, renk, _, _, gecmeli = struct.unpack(">IIBBBBB", ihdr)
        if eski_boy <= boy:
            return True
        if gecmeli or derinlik != 8 or renk not in (2, 6):
            return False
        satir = 1 + en * (3 if renk == 2 else 4)
        ham = zlib.decompress(idat)[:satir * boy]
        yeni_ihdr = struct.pack(">IIBBBBB", en, boy, derinlik, renk, 0, 0, 0)

        def parca(tip, govde):
            return struct.pack(">I", len(govde)) + tip + govde + struct.pack(">I", zlib.crc32(tip + govde) & 0xffffffff)
        cikti = b"\x89PNG\r\n\x1a\n" + parca(b"IHDR", yeni_ihdr)
        for tip, govde in parcalar:
            if tip in (b"sRGB", b"gAMA", b"pHYs", b"iCCP", b"cHRM"):
                cikti += parca(tip, govde)
        cikti += parca(b"IDAT", zlib.compress(ham, 9)) + parca(b"IEND", b"")
        with open(yol, "wb") as d:
            d.write(cikti)
        return True
    except Exception:
        return False


def png_olcu(yol):
    try:
        with open(yol, "rb") as d:
            bas_ = d.read(24)
        if bas_[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        return struct.unpack(">II", bas_[16:24])
    except Exception:
        return None


# ---------- marka ----------
def kitten_oku(kok):
    """Ogrencinin marka/marka-kiti.html dosyasindaki window.MARKA blogundan secimleri okur.
    Veri dosyasinda "marka" eksikse yedek yoldur; yazan FounderOS'tur, betik yalniz okur."""
    yol = os.path.join(kok, "marka", "marka-kiti.html")
    if not os.path.exists(yol):
        return {}
    try:
        t = oku(yol)
    except Exception:
        return {}
    m = re.search(r"window\.MARKA\s*=\s*\{", t)
    if not m:
        return {}
    blok = t[m.end():m.end() + 30000]
    blok = re.split(r"\bsecenekler\s*:", blok)[0]
    blok = re.split(r"\n\s*\}\s*;", blok)[0]
    sonuc = {}
    for alan in ("ad", "isaret", "kilit", "tipografi", "palet", "kurucu", "sehir", "site", "instagram", "yuvarlak"):
        mm = re.search(r"(?<![\w.$])[\"']?" + alan + r"[\"']?\s*:\s*([\"'])(.*?)\1", blok)
        if mm and mm.group(2).strip():
            sonuc[alan] = mm.group(2).strip()
    mr = re.search(r"(?<![\w.$])[\"']?renk[\"']?\s*:\s*\{([^}]*)\}", blok)
    if mr:
        renk = dict((a, b) for a, _, b in re.findall(r"[\"']?([a-z_]+)[\"']?\s*:\s*([\"'])(#[0-9A-Fa-f]{3,8})\2", mr.group(1)))
        if renk:
            sonuc["renk"] = renk
    ma = re.search(r"(?<![\w.$])[\"']?atmosfer[\"']?\s*:\s*\[([^\]]*)\]", blok)
    if ma:
        atm = re.findall(r"#[0-9A-Fa-f]{3,8}", ma.group(1))
        if len(atm) == 2:
            sonuc["atmosfer"] = atm
    return sonuc


def gorsel_gom(kok, yol, uyari, ad):
    if not yol:
        return None
    tam = yol if os.path.isabs(yol) else os.path.join(kok, yol)
    uz = os.path.splitext(tam)[1].lower()
    if not os.path.exists(tam):
        uyari.append("%s bulunamadı: %s" % (ad, yol))
        return None
    if uz not in MIME:
        uyari.append("%s biçimi desteklenmiyor (jpg, png, webp): %s" % (ad, yol))
        return None
    try:
        with open(tam, "rb") as d:
            veri = d.read()
    except Exception:
        uyari.append("%s okunamadı: %s" % (ad, yol))
        return None
    if len(veri) > 6 * 1024 * 1024:
        uyari.append("%s çok büyük (%d KB); yine de gömüldü" % (ad, len(veri) // 1024))
    return "data:%s;base64,%s" % (MIME[uz], base64.b64encode(veri).decode("ascii"))


def font_stili(tipografi):
    es = ESLESME.get(tipografi) or ESLESME["teknik"]
    parca, gorulen = [], set()
    for rol in ("baslik", "govde"):
        paket, aile, agirliklar = es[rol]
        for w in agirliklar:
            for alt, aralik in ARALIK.items():
                anahtar = (aile, w, alt)
                if anahtar in gorulen:
                    continue
                gorulen.add(anahtar)
                yol = os.path.join(FONT_KLASORU, "%s-%s-%d.woff2" % (paket, alt, w))
                if not os.path.exists(yol):
                    continue
                with open(yol, "rb") as d:
                    b64 = base64.b64encode(d.read()).decode("ascii")
                parca.append("@font-face{font-family:'%s';font-style:normal;font-weight:%d;font-display:block;"
                             "unicode-range:%s;src:url(data:font/woff2;base64,%s) format('woff2')}"
                             % (aile, w, aralik, b64))
    return "".join(parca)


def ascii_konu(metin, sinir=42):
    tablo = str.maketrans("çğıöşüÇĞİÖŞÜâîûÂÎÛ", "cgiosuCGIOSUaiuAIU")
    s = (metin or "").translate(tablo).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > sinir:
        s = s[:sinir].rsplit("-", 1)[0]
    return s or "icerik"


def main(argv):
    arg = list(argv)
    sadece_onizleme = "--sadece-onizleme" in arg
    if sadece_onizleme:
        arg.remove("--sadece-onizleme")
    veri_yolu = None
    if "--veri" in arg:
        i = arg.index("--veri")
        if i + 1 >= len(arg):
            return bas({"hata": "--veri için dosya yolu verilmedi"}, 1)
        veri_yolu = arg[i + 1]
        del arg[i:i + 2]
    kok = os.path.abspath(arg[0] if arg else ".")
    if not veri_yolu:
        veri_yolu = os.path.join(kok, ".founderos", "panel", "icerik.json")
    elif not os.path.isabs(veri_yolu):
        veri_yolu = os.path.join(kok, veri_yolu)

    sonuc = {"surum": SURUM, "uretilen": [], "uretilemeyen": [], "tasma": [], "uyari": []}
    if not os.path.exists(veri_yolu):
        sonuc["hata"] = "veri dosyası bulunamadı"
        sonuc["yol"] = veri_yolu
        return bas(sonuc, 1)
    try:
        veri = json.loads(oku(veri_yolu))
    except Exception as e:
        sonuc["hata"] = "veri dosyası okunamadı (geçerli JSON değil): %s" % e
        return bas(sonuc, 1)
    if not isinstance(veri, dict):
        sonuc["hata"] = "veri dosyası bir JSON nesnesi olmalı"
        return bas(sonuc, 1)

    sablon = os.path.join(BURASI, "icerik-sablonu.html")
    if not os.path.exists(sablon):
        sonuc["hata"] = "icerik-sablonu.html betiğin yanında yok"
        return bas(sonuc, 1)

    parcalar = veri.get("parcalar") or []
    car = next((p for p in parcalar if isinstance(p, dict) and p.get("tur") == "carousel"), None)
    slaytlar = (car or {}).get("slaytlar") or []
    if not slaytlar:
        sonuc["hata"] = "kaydırmalı gönderinin slaytı yok (parcalar içinde tur: carousel, slaytlar)"
        return bas(sonuc, 1)
    if not 6 <= len(slaytlar) <= 8:
        sonuc["uyari"].append("slayt sayısı %d; kural altı ile sekiz" % len(slaytlar))
    for n, s in enumerate(slaytlar, 1):
        if not isinstance(s, dict) or not str(s.get("baslik") or "").strip():
            sonuc["hata"] = "%d. slaytın başlığı yok" % n
            return bas(sonuc, 1)

    # hafta klasoru
    hafta = veri.get("hafta") or {}
    ana = veri.get("ana") or {}
    klasor = (hafta.get("klasor") or "").strip().strip("/")
    if not klasor and car and car.get("gorseller"):
        ilk = str(car["gorseller"][0]).replace("\\", "/")
        if "/carousel/" in ilk:
            klasor = ilk.split("/carousel/")[0]
    if not klasor:
        klasor = "icerik/%s-%s" % (hafta.get("baslangic") or "hafta", ascii_konu(ana.get("baslik") or hafta.get("tema")))
        sonuc["uyari"].append("hafta.klasor yok; %s kullanıldı" % klasor)
    hafta_klasoru = os.path.join(kok, klasor)
    sonuc["klasor"] = klasor

    # marka: veri dosyasi once, sonra marka kiti, sonra varsayilan
    marka = dict(veri.get("marka") or {})
    kit = kitten_oku(kok)
    kaynak = {}
    for alan, deger in kit.items():
        if not marka.get(alan):
            marka[alan] = deger
            kaynak[alan] = "kit"
    for alan, liste, vars_ in (("palet", PALETLER, "murekkep"), ("isaret", ISARETLER, "capraz"),
                               ("kilit", KILITLER, "yatay"), ("tipografi", list(ESLESME), "teknik")):
        if marka.get(alan) not in liste:
            if marka.get(alan):
                sonuc["uyari"].append("%s kütüphanede yok: %s; %s kullanıldı" % (alan, marka.get(alan), vars_))
            else:
                sonuc["uyari"].append("%s verilmedi; %s kullanıldı" % (alan, vars_))
            marka[alan] = vars_
            kaynak[alan] = "varsayilan"
    if not marka.get("ad"):
        sonuc["uyari"].append("iş adı verilmedi")
    marka["foto_veri"] = gorsel_gom(kok, marka.get("foto"), sonuc["uyari"], "fotoğraf")
    marka["logo_veri"] = gorsel_gom(kok, marka.get("logo"), sonuc["uyari"], "logo")
    for alan in ("foto_veri", "logo_veri"):
        if not marka[alan]:
            del marka[alan]
    sonuc["marka"] = {a: marka.get(a) for a in ("ad", "palet", "tipografi", "isaret", "kilit")}
    if kaynak:
        sonuc["marka"]["kaynak"] = kaynak

    icerik = dict(veri)
    icerik["marka"] = marka
    js = json.dumps(icerik, ensure_ascii=False).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = oku(sablon)
    if "/*FOUNDEROS-ICERIK*/" not in html:
        sonuc["hata"] = "şablonda /*FOUNDEROS-ICERIK*/ işareti yok"
        return bas(sonuc, 1)
    html = html.replace("/*FOUNDEROS-ICERIK*/", "window.ICERIK = " + js + ";", 1)
    stil = font_stili(marka["tipografi"])
    if stil:
        html = html.replace("<!--FOUNDEROS-FONT-->", "<!--FOUNDEROS-FONT--><style id=fos-font>" + stil + "</style>", 1)
    else:
        sonuc["uyari"].append("yazı tipi dosyaları bulunamadı; sistem yazı tipi kullanıldı")

    try:
        os.makedirs(os.path.join(hafta_klasoru, "carousel"), exist_ok=True)
        onizleme = os.path.join(hafta_klasoru, "onizleme.html")
        yaz(onizleme, html)
    except Exception as e:
        sonuc["hata"] = "hafta klasörüne yazılamadı: %s" % e
        return bas(sonuc, 1)
    sonuc["onizleme"] = os.path.relpath(onizleme, kok).replace("\\", "/")
    if sadece_onizleme:
        return bas(sonuc, 0)

    tr = tarayici()
    sonuc["tarayici"] = tr
    if not tr:
        sonuc["hata"] = "tarayici-yok"
        sonuc["uretilemeyen"] = ["hepsi"]
        return bas(sonuc, 2)

    profil = tempfile.mkdtemp(prefix="fos-icerik-")
    try:
        pay = pay_olc(tr, profil)
        sonuc["pay"] = pay
        url = dosya_url(onizleme)
        dom = dom_al(tr, profil, url + "#kontrol")
        m = re.search(r"<title>KONTROL (\{.*?\})</title>", dom, re.S)
        kontrol = {}
        if m:
            try:
                import html as _h
                kontrol = json.loads(_h.unescape(m.group(1)))
            except Exception:
                kontrol = {}
        if not kontrol:
            sonuc["uyari"].append("sığma denetimi okunamadı; görseller yine üretildi")
            kontrol = {"varliklar": ["s-%d" % (i + 1) for i in range(len(slaytlar))], "tasma": []}
        sonuc["tasma"] = kontrol.get("tasma") or []
        sonuc["olcek"] = {a: b for a, b in (kontrol.get("olcek") or {}).items() if b and b < 1}

        hedefler = []
        for vid in kontrol.get("varliklar") or []:
            if vid.startswith("s-"):
                n = int(vid[2:])
                hedefler.append((vid, os.path.join(hafta_klasoru, "carousel", "%02d.png" % n), 1080, 1350))
            elif vid == "kapak":
                hedefler.append((vid, os.path.join(hafta_klasoru, "kapak.png"), 1280, 720))
            elif vid.startswith("r-"):
                n = int(vid[2:])
                hedefler.append((vid, os.path.join(hafta_klasoru, "reels-%d.png" % n), 1080, 1920))

        for vid, hedef, en, boy in hedefler:
            if os.path.exists(hedef):
                try:
                    os.remove(hedef)
                except Exception:
                    pass
            cmd = [tr] + TEMEL + ["--user-data-dir=" + profil, "--virtual-time-budget=4000",
                                  "--force-device-scale-factor=1", "--window-size=%d,%d" % (en, boy + pay),
                                  "--screenshot=" + hedef, url + "#" + vid]
            ok = calistir(cmd)
            if ok and os.path.exists(hedef):
                olcu = png_olcu(hedef)
                if olcu and olcu[1] != boy:
                    ok = png_kirp(hedef, boy)
                    olcu = png_olcu(hedef)
                ok = ok and olcu is not None and olcu[0] == en and olcu[1] == boy and os.path.getsize(hedef) > 900
            else:
                ok = False
            if ok:
                sonuc["uretilen"].append(os.path.relpath(hedef, kok).replace("\\", "/"))
            else:
                sonuc["uretilemeyen"].append(vid)

        # slayt sayisi azaldiysa eski dosyalar kalmasin
        n = len(slaytlar)
        for eski in sorted(glob.glob(os.path.join(hafta_klasoru, "carousel", "[0-9][0-9].png"))):
            try:
                if int(os.path.basename(eski)[:2]) > n:
                    os.remove(eski)
            except Exception:
                sonuc["uyari"].append("eski slayt silinemedi: %s" % os.path.relpath(eski, kok))
    finally:
        shutil.rmtree(profil, ignore_errors=True)

    # veri dosyasindaki yollar uretilenle ayni mi
    beklenen = [p for p in sonuc["uretilen"] if "/carousel/" in p]
    if car and car.get("gorseller") and [str(x).replace("\\", "/") for x in car["gorseller"]] != beklenen:
        sonuc["uyari"].append("carousel.gorseller üretilen dosyalarla aynı değil; panel dosyasında düzelt")
    if sonuc["uretilemeyen"]:
        return bas(sonuc, 3)
    if sonuc["tasma"]:
        return bas(sonuc, 4)
    return bas(sonuc, 0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
