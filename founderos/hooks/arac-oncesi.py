#!/usr/bin/env python3
"""FounderOS PreToolUse kancasi.

adaylar.csv'nin aday araci disinda elle degistirilmesini engeller. Aday
listesi 46 sutunlu, tekrar eleme ve tarih hesaplari aracin icinde; elle
yazilan tek satir listeyi bozuyor. Engellenen islemde cikis kodu 2 ve sebep
stderr'e gider; Claude araci kullanarak yeniden dener.
"""
import json
import os
import re
import sys

YAZMA = re.compile(r"(>|\bsed\s+-i|\btee\b|\btruncate\b|\brm\b|\bmv\b|\bcp\b|\bperl\s+-p?i)")


def main():
    try:
        g = json.load(sys.stdin)
    except Exception:
        return 0
    ad = g.get("tool_name") or ""
    girdi = g.get("tool_input") or {}
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
