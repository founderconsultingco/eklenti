#!/usr/bin/env python3
"""FounderOS UserPromptSubmit kancasi.

Ogrencinin cumlesinde gunu acan selam, vazgecme, takilma ve sik niyetleri
yakalar; eslesme varsa baglama tek satirlik yon notu koyar. Eslesme yoksa
hicbir sey yazmaz. Istemi asla engellemez.
"""
import json
import re
import sys


def kucult(s):
    s = s.replace("I", "ı").replace("İ", "i")
    return s.lower()


KURALLAR = [
    ("selam", re.compile(r"^\s*(g[üu]nayd[ıi]n|ba[şs]layal[ıi]m|haz[ıi]r[ıi]m|devam( edelim)?|bug[üu]n ne yap[ıi]yoruz|kald[ıi][ğg][ıi]m yerden( devam)?|merhaba|selam)\b[\s.!?,]*$"),
     "FounderOS: kısa selam. Günü founderos:gunaydin ile aç (çekirdek bu oturumda açık değilse önce founderos:ana-yonetici). Selama selamla karşılık verip bekleme; ilk cümle düne bağlansın."),
    ("vazgecme", re.compile(r"(b[ıi]rak[ıi]yorum|b[ıi]rakaca[ğg][ıi]m|vazge[çc]|bana g[öo]re de[ğg]il|yapamayaca[ğg][ıi]m|olmayacak bu|pes ediyorum|ni[şs] de[ğg]i[şs]tir|sekt[öo]r de[ğg]i[şs]tir|i[şs] de[ğg]i[şs]tir|ara vereyim|bu i[şs] olmuyor)"),
     "FounderOS: vazgeçme işareti olabilir. Çekirdeğin 'Vazgeçme ve ara' kuralını uygula: önce plana bak (büyük mü, belirsiz mi, bilgi eksik mi, vaktine sığıyor mu), gerekiyorsa küçült; inanç değişimi en son ve rakamla. Tarihli mola işaret değildir."),
    ("takilma", re.compile(r"(anlamad[ıi]m|yapamad[ıi]m|olmad[ıi]|[çc]al[ıi][şs]m[ıi]yor|hata veriyor|bende bu ekran yok|bulam[ıi]yorum|g[öo]remiyorum|nereye bas)"),
     "FounderOS: takılma. Takılma yöntemini uygula: nerede kaldı, türü ne (bilgi, erişim, teknik, uygulama), işi küçült; aynı açıklamayı tekrarlama; iki denemede çözülmezse destek özeti."),
    ("cevap_yok", re.compile(r"(kimse cevap vermedi|cevap gelmiyor|hi[çc] d[öo]n[üu][şs] yok|kimse a[çc]m[ıi]yor|kimse d[öo]nmedi)"),
     "FounderOS: founderos:cevap-gelmiyor modülünü aç. Motivasyon konuşması yok, beş kontrol ve tek gerekçeli değişiklik."),
    ("randevu", re.compile(r"(randevu ald[ıi]m|yar[ıi]n g[öo]r[üu][şs]me|g[öo]r[üu][şs]me ayarlad[ıi]m|randevu verdi)"),
     "FounderOS: randevu. founderos:gorusmeye-getir, ardından founderos:gorusme-provasi-yap."),
    ("gorusme_bitti", re.compile(r"(g[öo]r[üu][şs]me bitti|g[öo]r[üu][şs]t[üu]k|g[öo]r[üu][şs]meyi yapt[ıi]m|[şs][öo]yle ge[çc]ti)"),
     "FounderOS: görüşme bitti. founderos:gorusmeyi-analiz-et."),
    ("evet", re.compile(r"(evet dedi|kabul etti|paray[ıi] g[öo]nderecek|[öo]deme yapacak|anla[şs]t[ıi]k)"),
     "FounderOS: evet geldi. founderos:onay-belgesini-hazirla, sonra founderos:musteriyi-karsila. Erken evet bekletilmez."),
    ("resmi", re.compile(r"(kvkk|\biys\b|yasal m[ıi]|yasal olarak|kanun|s[öo]zle[şs]me|vergi|fatura|[şs]irket (kur|a[çc])|mali m[üu][şs]avir|muhasebeci|avukat|hukuk|ceza|izin (laz[ıi]m|gerek)|ruhsat|ba[ğg]-?kur)"),
     "FounderOS: öğrenci resmi bir konu açtı. Kısa, sakin, yapılacak işle cevap ver; kanun, madde, ceza, hukukçu anlatma ve öğrencinin kullandığı resmi kelimeleri (izin sistemi, kanun, avukat, ceza, vergi levhası) tekrar etme (çekirdekte 'Korkutan dil yok'). Şirket ilk 'evet'te açılır, sözleşme hazır gelir. Bilmediğin resmi soruda destek satırını hazır ver."),
    ("aksam", re.compile(r"^\s*(ak[şs]am|g[üu]n[üu] kapatal[ıi]m|bug[üu]nl[üu]k bu kadar|kapan[ıi][şs] yapal[ıi]m)\b[\s.!?,]*$"),
     "FounderOS: akşam kapanışı. founderos:rakamlari-oku; saha açıksa önce aday aracının kapat komutu (kapanmamış günler), kapanışın tarihi onun ilk satırındaki iş günü."),
    ("crm", re.compile(r"(crm hesab[ıi]m a[çc][ıi]ld[ıi]|giri[şs] bilgilerim geldi|ba[şs]lang[ıi][çc] g[öo]r[üu][şs]mesini yapt[ıi]k)"),
     "FounderOS: CRM açıldı. Günün ilk işi founderos:araclari-kur'un 'CRM açıldığı gün' adımı, ardından founderos:musteri-takip-sistemini-kur."),
]


def main():
    try:
        g = json.load(sys.stdin)
    except Exception:
        return
    istem = g.get("prompt") or ""
    if not isinstance(istem, str) or not istem.strip():
        return
    k = kucult(istem.strip())
    if len(k) > 1200:
        return
    notlar = []
    for ad, desen, notu in KURALLAR:
        if ad in ("selam", "aksam") and len(k) > 60:
            continue
        if desen.search(k):
            notlar.append(notu)
    if notlar:
        sys.stdout.write("\n".join(notlar[:2]) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
