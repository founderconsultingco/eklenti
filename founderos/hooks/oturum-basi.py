#!/usr/bin/env python3
"""FounderOS SessionStart kancasi.

Cikti (stdout) modelin baglamina girer. Uc is yapar:
1. Cekirdegin kisa halini koyar (ruh ve dort temel kural).
2. Oturum sikistirmadan sonra aciliyorsa "kaldigin modulu yeniden ac" der.
3. Calisma klasorunde durum kaydi varsa kisa ozetini koyar; yoksa nereden
   okunacagini soyler (bulut oturumunda klasor bilgisayardadir).
4. Ogrencinin klasorundeki aday araci paketteki surumden eskiyse iki dosyasini
   (adaylar-arac.py, adaylar-sablon.html) paketten yeniler; csv'ye dokunmaz. Model
   eski araci kullanirsa yeni kurallar (denetimsiz aday listeye girmez, rampa
   satiri) hic calismiyor; surum karsilastirmasi modele birakilmaz.
Hata olursa sessiz kalir; oturumu asla durdurmaz.
"""
import json
import os
import re
import shutil
import sys
from pathlib import Path

KOK = Path(os.environ.get("CLAUDE_PLUGIN_ROOT") or Path(__file__).resolve().parent.parent)
ARAC_KAYNAK = KOK / "skills" / "aday-listesi-araci"
SURUM_DESENI = re.compile(r'^SURUM\s*=\s*"(\d+(?:\.\d+)*)"', re.M)


def surum_oku(p):
    try:
        with open(p, encoding="utf-8", errors="ignore") as f:
            m = SURUM_DESENI.search(f.read(40000))
        return tuple(int(x) for x in m.group(1).split(".")) if m else None
    except Exception:
        return None


def araci_guncelle(cwd):
    """Klasordeki arac paketinkinden eskiyse yenilenir. Donus: "eski yeni" ya da None."""
    yeni = surum_oku(ARAC_KAYNAK / "adaylar-arac.py")
    if not yeni:
        return None
    for kok in dict.fromkeys([cwd, os.getcwd(), os.environ.get("CLAUDE_PROJECT_DIR")]):
        if not kok:
            continue
        hedef = Path(kok) / ".founderos" / "adaylar-arac.py"
        if not hedef.is_file():
            continue
        eski = surum_oku(hedef)
        if eski is None or eski >= yeni:
            return None
        for ad in ("adaylar-arac.py", "adaylar-sablon.html"):
            kaynak = ARAC_KAYNAK / ad
            if not kaynak.is_file():
                continue
            gecici = hedef.with_name(ad + ".yeni")
            shutil.copyfile(kaynak, gecici)
            os.replace(gecici, hedef.with_name(ad))
        return "%s %s" % (".".join(map(str, eski)), ".".join(map(str, yeni)))
    return None


def oku_girdi():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def durum_ozeti(cwd):
    adaylar = []
    for kok in (cwd, os.getcwd()):
        if kok and Path(kok) / ".founderos" / "durum.json" not in adaylar:
            adaylar.append(Path(kok) / ".founderos" / "durum.json")
    proje = os.environ.get("CLAUDE_PROJECT_DIR")
    if proje:
        adaylar.append(Path(proje) / ".founderos" / "durum.json")
    for p in adaylar:
        try:
            if p.is_file():
                d = json.loads(p.read_text(encoding="utf-8"))
                break
        except Exception:
            continue
    else:
        return None
    alanlar = []
    for k, etiket in (("gun_baslangic", "başlangıç"), ("duzen", "düzen"), ("blok", "blok"),
                      ("oturus", "oturuş"), ("adim", "adım"), ("acik_modul", "açık modül"),
                      ("sonraki_adim", "sıradaki adım"), ("saha_acik", "saha açık"),
                      ("son_temas_tarihi", "son temas")):
        v = d.get(k)
        if isinstance(v, bool):
            v = "evet" if v else "hayır"
        if v not in (None, "", []):
            alanlar.append("%s: %s" % (etiket, v))
    say = d.get("sayaclar") or {}
    if isinstance(say, dict) and say:
        alanlar.append("sayaçlar: " + ", ".join("%s %s" % (k, say[k]) for k in say))
    bek = d.get("bekleyen_sorular") or []
    if bek:
        alanlar.append("bekleyen soru: %d" % len(bek))
    must = d.get("aktif_musteriler") or []
    if must:
        alanlar.append("aktif müşteri: %d" % len(must))
    return "; ".join(alanlar)


def main():
    g = oku_girdi()
    kaynak = (g.get("source") or "").lower()
    cikti = []
    try:
        cikti.append((KOK / "hooks" / "cekirdek-kisa.md").read_text(encoding="utf-8").strip())
    except Exception:
        cikti.append("[FounderOS] FounderOS işiyle gelen öğrencide ilk iş founderos:ana-yonetici becerisini aç.")
    if kaynak == "compact":
        cikti.append(
            "Bağlam az önce sıkıştırıldı. FounderOS oturumuysa: önce durum kaydını (.founderos/durum.json) "
            "ve İş Beyni'ni oku, founderos:ana-yonetici becerisini ve kaldığın modülü (durum kaydındaki "
            "acik_modul) Skill aracıyla yeniden aç, kaldığın adımdan sürdür. Öğrenciye aynı soruyu sorma.")
    try:
        guncel = araci_guncelle(g.get("cwd"))
    except Exception:
        guncel = None
    if guncel:
        eski, yeni = guncel.split()
        cikti.append(
            "Aday aracı bu oturumun başında yeni sürüme geçirildi (%s yerine %s); komutlarını ve çıktısını "
            "founderos:aday-listesi-dosyasi'ndaki haliyle kullan. Öğrenciye söylenmez." % (eski, yeni))
    ozet = durum_ozeti(g.get("cwd"))
    if ozet:
        cikti.append("Durum kaydı: " + ozet)
    else:
        cikti.append(
            "Durum kaydı bu ortamda görünmüyor. FounderOS oturumuysa öğrencinin klasöründen "
            "`.founderos/durum.json` ve `is-beyni.md` dosyasını oku (bilgisayara bağlı bir oturumdaysan "
            "o bilgisayarın dosya araçlarıyla).")
    sys.stdout.write("\n\n".join(cikti) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
