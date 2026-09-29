#!/usr/bin/env python3
"""FounderOS Stop kancasi.

Yalniz FounderOS oturumunda (bu konusmada bir founderos: becerisi acilmissa, ana
ajan FounderOS ise ya da calisma klasorunde .founderos/ veya is-beyni.md varsa)
son asistan turunu dort hataya karsi denetler:
  1. Doldurulmamis yer tutucu ([21/28], [is adi] gibi) ogrenciye gitmis mi.
  2. Uzun tire (U+2014) kullanilmis mi.
  3. "Kaydettim / Is Beyni'ne yazdim" denmis ama bu turda hicbir yazma
     araci calismamis mi.
  4. Ogrenciyi korkutan resmi dil (kanun, izin sistemi, hukukcu, ceza, sozlesme
     maddesi, vergi evraki) gitmis mi. Tirnak ya da kod blogu icindeki hazir
     metinler (musteriye ya da musavire gidecek mesaj) sayilmaz.
Hata varsa cikis kodu 2 ve sebebi stderr'e yazar: Claude durmaz, duzeltir.
stop_hook_active doluysa (ikinci tur) hicbir sey yapmaz; dongu olmaz.
"""
import json
import os
import re
import sys

YER_TUTUCU = re.compile(
    r"\[(?:\d{1,3}\s*/\s*\d{1,3}|i[şs] ad[ıi]|tarih|[şs]ehir|ad[ıi]n?|ni[şs]|say[ıi]|g[üu]n|m[üu][şs]teri ad[ıi]|"
    r"sistem ad[ıi]|kart rakam[ıi]|ana kanal|oran|i[şs]letme ad[ıi]|saat|kanal)\]",
    re.I)
KAYIT_IDDIASI = re.compile(
    r"((i[şs] beyni|is-beyni|dosya|klas[öo]r|g[üu]nl[üu][ğg]|durum kayd|durum\.json|kay[ıi]t)[^.\n]{0,40}"
    r"(yazd[ıi]m|yaz[ıi]ld[ıi]|i[şs]ledim|ekledim|g[üu]ncelledim|kaydettim)|\bkaydettim\b)",
    re.I)
YAZMA_ARACLARI = {"Write", "Edit", "MultiEdit", "NotebookEdit"}

# Ogrenciye hic gitmeyen resmi dil (cekirdekteki "Korkutan dil yok").
KORKUTAN = re.compile(
    r"\bİYS\b|\bIYS\b|\bKVKK\b|[Hh]ukukçu|[Aa]vukat|[Mm]evzuat|[Yy]önetmeli[kğ]|\b[Kk]anun|Resm[iî] Gazete|"
    r"\b[Cc]eza(sı|ları|lar|ya|yı|dan|da|sını)?\b|\b[Dd]ava(sı|ya|yı|lar)?\b|\b[Mm]adde(si)?\s+\d|"
    r"Bağ-?[Kk]ur|[Vv]ergi levha|[Uu]sulsüzlük|[Tt]icari (elektronik )?ileti|[Aa]çık rıza|[Vv]eri sorumlusu|"
    r"[Yy]asal (risk|sorumluluk|yükümlülük)")
# Musterinin vergi levhasi (0850 hatti icin kurulumda istenir) ogrencinin
# normal isidir; ayni cumlede musteri ya da isletme geciyorsa sayilmaz.
MUSTERI_BELGESI = re.compile(r"[Vv]ergi levha")
MUSTERI_BAGLAMI = re.compile(r"[Mm]üşteri|[İi]şletme|[Kk]linik")


def korkutan_bul(metin):
    for m in KORKUTAN.finditer(metin):
        if MUSTERI_BELGESI.fullmatch(m.group(0)):
            bas = max(metin.rfind(ch, 0, m.start()) for ch in ".!?\n") + 1
            sonlar = [i for i in (metin.find(ch, m.end()) for ch in ".!?\n") if i != -1]
            cumle = metin[bas:min(sonlar) if sonlar else len(metin)]
            if MUSTERI_BAGLAMI.search(cumle):
                continue
        return m
    return None


def alinti_disi(metin):
    """Hazir metinler (kod blogu, > ile baslayan satir, tirnak ici) cikarilir;
    musteriye ya da musavire gidecek mesajda resmi terim olabilir."""
    m = re.sub(r"```.*?```", " ", metin, flags=re.S)
    m = "\n".join(x for x in m.split("\n") if not x.lstrip().startswith(">"))
    m = re.sub(r"“[^”]{0,4000}”", " ", m)
    m = re.sub(r"\"[^\"]{0,4000}\"", " ", m)
    return m


def metin_parcalari(icerik):
    if isinstance(icerik, str):
        return [icerik], []
    metinler, araclar = [], []
    for p in icerik or []:
        if not isinstance(p, dict):
            continue
        if p.get("type") == "text":
            metinler.append(p.get("text") or "")
        elif p.get("type") == "tool_use":
            araclar.append(p)
            # Kullaniciya dogrudan giden mesaj araci da ogrencinin gordugu metindir.
            if "SendUserMessage" in (p.get("name") or ""):
                metinler.append(str((p.get("input") or {}).get("message") or ""))
    return metinler, araclar


def gercek_kullanici_mi(k):
    icerik = (k.get("message") or {}).get("content")
    if isinstance(icerik, str):
        return bool(icerik.strip())
    if isinstance(icerik, list):
        tipler = {p.get("type") for p in icerik if isinstance(p, dict)}
        return "tool_result" not in tipler and bool(tipler)
    return False


def yazma_mi(arac):
    ad = arac.get("name") or ""
    if ad in YAZMA_ARACLARI:
        return True
    if ad == "Bash" or ad.endswith("device_bash"):
        return True
    if "commit_files" in ad or "memory_write" in ad or "memory_str_replace" in ad or "memory_append" in ad:
        return True
    if ad.startswith("mcp__") and any(x in ad for x in ("durum_yaz", "olcum_yaz", "saha_yukle", "write", "update", "create")):
        return True
    return False


def main():
    try:
        g = json.load(sys.stdin)
    except Exception:
        return 0
    if g.get("stop_hook_active"):
        return 0
    # Son asistan mesaji kayda Stop kancasindan SONRA yaziliyor; metin once
    # girdideki last_assistant_message'tan alinir, kayit araclar ve beceri icin okunur.
    son_mesaj = g.get("last_assistant_message")
    son_mesaj = son_mesaj.strip() if isinstance(son_mesaj, str) else ""
    yol = g.get("transcript_path")
    if not yol and not son_mesaj:
        return 0
    kayitlar = []
    if yol:
        try:
            with open(yol, encoding="utf-8") as f:
                for satir in f:
                    satir = satir.strip()
                    if not satir:
                        continue
                    try:
                        kayitlar.append(json.loads(satir))
                    except Exception:
                        continue
        except Exception:
            kayitlar = []

    founderos = str(g.get("agent_type") or "").startswith("founderos")
    son_kullanici = -1
    for i, k in enumerate(kayitlar):
        tip = k.get("type")
        if tip == "user" and gercek_kullanici_mi(k):
            son_kullanici = i
        if tip == "assistant":
            _, araclar = metin_parcalari((k.get("message") or {}).get("content"))
            for a in araclar:
                if a.get("name") == "Skill" and str((a.get("input") or {}).get("skill", "")).startswith("founderos:"):
                    founderos = True
    if not founderos:
        # Beceri acilmadan dogrudan cevap verilen turlar da denetlenir:
        # ogrencinin FounderOS klasorunde calisiyorsak oturum FounderOS'tur.
        for kok in (g.get("cwd"), os.getcwd()):
            try:
                if kok and (os.path.isdir(os.path.join(kok, ".founderos")) or os.path.isfile(os.path.join(kok, "is-beyni.md"))):
                    founderos = True
                    break
            except Exception:
                continue
    if not founderos:
        return 0

    son_metinler, son_araclar = [], []
    for k in kayitlar[son_kullanici + 1:]:
        if k.get("type") != "assistant":
            continue
        m, a = metin_parcalari((k.get("message") or {}).get("content"))
        son_metinler += m
        son_araclar += a
    metin = "\n".join(son_metinler)
    if son_mesaj and son_mesaj not in metin:
        metin = (metin + "\n" + son_mesaj).strip()
    if not metin.strip():
        return 0

    sorunlar = []
    yt = YER_TUTUCU.search(metin)
    if yt:
        sorunlar.append("Öğrenciye giden metinde doldurulmamış yer tutucu var (%s). Gerçek değerle doldur ya da cümleden çıkar." % yt.group(0))
    if "\u2014" in metin:
        sorunlar.append("Metinde uzun tire var. Cümleyi böl ya da virgül kullan.")
    kt = korkutan_bul(alinti_disi(metin))
    if kt:
        sorunlar.append("Öğrenciye giden metinde korkutan resmi dil var (%s). Kuralı sessizce uygula: aynı şeyi yapılacak iş ya da sonuç olarak, bu kelime olmadan söyle; gerekmiyorsa hiç söyleme. Müşteriye ya da müşavire gidecek hazır bir metnin parçasıysa o metni tırnak içinde ver ve öğrenciye açıklama." % kt.group(0))
    if KAYIT_IDDIASI.search(metin) and not any(yazma_mi(a) for a in son_araclar):
        sorunlar.append("Bu turda kaydettiğini ya da dosyaya yazdığını söyledin ama hiçbir yazma işlemi yapılmadı. Şimdi gerçekten yaz; yazmayacaksan 'not aldım' de.")
    if sorunlar:
        sys.stderr.write("FounderOS denetimi: " + " ".join(sorunlar) + "\n")
        return 2
    return 0


if __name__ == "__main__":
    try:
        kod = main()
    except Exception:
        kod = 0
    sys.exit(kod)
