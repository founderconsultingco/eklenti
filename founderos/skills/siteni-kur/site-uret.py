# -*- coding: utf-8 -*-
"""Tanitim sayfasina yazi tiplerini ve nisin acilis fotografini gomer.

Kullanim (FounderOS calistirir, ogrenci terminale girmez):
  python3 site-uret.py <site/[is-adi].html> --nis <nis-slug>
  python3 site-uret.py <site/[is-adi].html> --foto <dosya.webp|jpg|png>

Sira: sablon kopyalanir, window.SITE blogu yazilir, SONRA bu betik calisir.
Betik dosyanin yalniz iki isaretine dokunur: <!--FOUNDEROS-FONT--> ve
<!--FOUNDEROS-FOTO-->. Ikinci kez calisirsa eskisini degistirir, ustune eklemez.

Neden gomuluyor: sayfa tek dosya olarak tasinir, internet olmasa da ayni gorunur,
disaridan yazi tipi cagrilmaz (sablon kurali). Fotograf pakette nis basina bir tane
duruyor (nis-fotolari/<slug>.webp); yoksa sayfa dokulu koyu zeminle acilir, bos kalmaz.
"""
import base64, json, os, re, sys

BURASI = os.path.dirname(os.path.abspath(__file__))
def _ilk_var(*adaylar):
    for a in adaylar:
        if os.path.isdir(a):
            return a
    return adaylar[0]

# Fontlar markani-kur becerisinin yaninda duruyor; pakette iki kez tasinmasin diye oradan okunur.
FONT_KLASORU = _ilk_var(os.path.join(BURASI, "fontlar"),
                        os.path.join(BURASI, "..", "markani-kur", "fontlar"))
FOTO_KLASORU = os.path.join(BURASI, "nis-fotolari")

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
MIME = {".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".avif": "image/avif"}


def oku(yol):
    with open(yol, "r", encoding="utf-8") as d:
        return d.read()


def yaz(yol, metin):
    with open(yol, "w", encoding="utf-8") as d:
        d.write(metin)


def eslesme_bul(govde):
    """window.SITE.yazi_tipi.baslik icindeki ilk aile adindan paketi bulur."""
    m = re.search(r"yazi_tipi\s*:\s*\{[^}]*?baslik\s*:\s*[\"']\s*'?([A-Za-z ]+?)'?\s*[,\"']", govde)
    aile = (m.group(1).strip() if m else "").lower()
    for ad, es in ESLESME.items():
        if es["baslik"][1].lower() == aile:
            return ad, es
    m2 = re.search(r"yon\s*:\s*[\"']([a-z]+)[\"']", govde)
    ad = m2.group(1) if m2 and m2.group(1) in ESLESME else "saglam"
    return ad, ESLESME[ad]


def font_stili(es):
    parca = []
    aileler = []
    for rol in ("baslik", "govde"):
        paket, aile, agirliklar = es[rol]
        if aile in aileler:
            continue
        aileler.append(aile)
        for w in agirliklar:
            for alt, aralik in ARALIK.items():
                yol = os.path.join(FONT_KLASORU, "%s-%s-%d.woff2" % (paket, alt, w))
                if not os.path.exists(yol):
                    continue
                with open(yol, "rb") as d:
                    b64 = base64.b64encode(d.read()).decode("ascii")
                parca.append(
                    "@font-face{font-family:'%s';font-style:normal;font-weight:%d;"
                    "font-display:block;unicode-range:%s;"
                    "src:url(data:font/woff2;base64,%s) format('woff2')}"
                    % (aile, w, aralik, b64))
    if not parca:
        return None
    return "<style id=fos-font>" + "".join(parca) + "</style>"


def foto_stili(yol):
    if not yol or not os.path.exists(yol):
        return None
    ek = os.path.splitext(yol)[1].lower()
    mime = MIME.get(ek)
    if not mime:
        return None
    with open(yol, "rb") as d:
        b64 = base64.b64encode(d.read()).decode("ascii")
    return "<style id=fos-foto>:root{--foto:url(data:%s;base64,%s)}</style>" % (mime, b64)


def isarete_yaz(govde, isaret, stil, kimlik):
    govde = re.sub(r"<style id=%s>.*?</style>" % kimlik, "", govde, flags=re.S)
    if isaret in govde:
        return govde.replace(isaret, isaret + (stil or ""), 1)
    # eski sablon: isaret yoksa </title> sonrasina koy
    return govde.replace("</title>", "</title>" + isaret + (stil or ""), 1)


def main():
    if len(sys.argv) < 2:
        print("kullanim: site-uret.py <sayfa.html> [--nis slug] [--foto dosya]")
        return 2
    hedef = sys.argv[1]
    nis = foto = None
    argv = sys.argv[2:]
    for i, a in enumerate(argv):
        if a == "--nis" and i + 1 < len(argv):
            nis = argv[i + 1]
        if a == "--foto" and i + 1 < len(argv):
            foto = argv[i + 1]
    if not os.path.exists(hedef):
        print("HATA: sayfa yok: " + hedef)
        return 1
    govde = oku(hedef)
    if "window.SITE" not in govde:
        print("HATA: sayfada window.SITE blogu yok; once blok yazilir, sonra bu betik.")
        return 1

    ad, es = eslesme_bul(govde)
    fs = font_stili(es)
    govde = isarete_yaz(govde, "<!--FOUNDEROS-FONT-->", fs, "fos-font")
    print("yazi tipi: %s (%s / %s)%s" % (ad, es["baslik"][1], es["govde"][1], "" if fs else "  [font dosyasi bulunamadi, sistem yazi tipi kalir]"))

    if not foto and nis:
        for ek in (".webp", ".jpg", ".jpeg", ".png"):
            aday = os.path.join(FOTO_KLASORU, nis + ek)
            if os.path.exists(aday):
                foto = aday
                break
    ps = foto_stili(foto)
    govde = isarete_yaz(govde, "<!--FOUNDEROS-FOTO-->", ps, "fos-foto")
    if ps:
        print("fotograf: %s (%d KB)" % (os.path.basename(foto), os.path.getsize(foto) // 1024))
    else:
        print("fotograf: yok, dokulu koyu zemin" + ("  [%s icin dosya bulunamadi]" % nis if nis else ""))

    yaz(hedef, govde)
    print("bitti: %s (%d KB)" % (hedef, os.path.getsize(hedef) // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
