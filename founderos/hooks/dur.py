#!/usr/bin/env python3
"""FounderOS Stop kancasi.

Yalniz FounderOS oturumunda (bu konusmada bir founderos: becerisi acilmissa, ana
ajan FounderOS ise ya da calisma klasorunde .founderos/ veya is-beyni.md varsa)
son asistan turunu (panelin "Su an" kartina giden odak_yaz metinleri dahil) su hatalara karsi denetler:
  1. Doldurulmamis yer tutucu ([21/28], [is adi] gibi) ogrenciye gitmis mi.
  2. Uzun tire (U+2014) kullanilmis mi.
  3. "Kaydettim / Is Beyni'ne yazdim" denmis ama bu turda hicbir yazma
     araci calismamis mi.
  4. Ogrenciyi korkutan resmi dil (kanun, izin sistemi, hukukcu, ceza, sozlesme
     maddesi, vergi evraki) gitmis mi. Tirnak ya da kod blogu icindeki hazir
     metinler (musteriye ya da musavire gidecek mesaj) sayilmaz.
  5. Durum kaydi (.founderos/durum.json) bu turda yazilmis, panelin okudugu alanlar
     sunucuya son gidenden farkli ve veri baglantisi acikken (oturumda bir veri araci
     cagrilmissa) durum_yaz gitmemis mi. Panelin sayaclari, asamasi ve musterisi
     sunucudaki kopyadan okunur; gitmezse panel eski asamada kalir.
  6. "Panele gonderiyorum / gonderdim / yolladim" denmis mi (cekirdek: denmez; panel
     kendiliginden tazelenir, ogrenciye panelde ne acildigi soylenir).
  7. Ingilizce ic not sizmis mi ("Step 7: open isini-kur.", "Let me ...", "I'll ...").
     Masaustunde arac cagrilari arasindaki metin de ogrenciye gorunur.
  8. Hazirligin blok numarasi ("ucuncu blokta", "bir sonraki blokta") ogrenciye gitmis mi;
     pencere adlari (sabah blogu, arama blogu) sayilmaz.
  9. Durum kaydinda aktif musteri var ama panelin teslimat dosyasi (.founderos/panel/teslimat.json)
     o musteriyi tasimiyor mu: ogrenci musterinin gununu panelde (Bugun'deki Teslimat karti, Yol'daki
     Teslimat Motoru) goremez. musteriyi-karsila satiri para geldigi turda acar; atlanirsa burada yakalanir.
 11. Durum kaydinda musteri sayisi gorusme sayisindan buyuk mu (evet gorusmenin icinden geldi, gorusme
     sayaca yazilmadi; panelin hunisi "0 gorusme, 1 musteri" gosterir).
 10. Gunaydin turunda (founderos:gunaydin acildi) Is Beyni'ndeki panel linki turun hicbir metninde yok mu:
     yeni sohbette yan panel yalniz bu baglantiyla acilir (z2: ilk mesaj iki gun ust uste hic yazilmadi).
 13. Gunaydin turunda saha aciksa (hafta ici) bugunun saha paketi kuruldu mu (.founderos/saha-paketi.json
     tarihi bugun) ve siradaki_cekim duruyorsa durum_oku yapildi mi: musteri isi ya da bekleyen soru
     sahanin yerine gecmez (z2 gun 7: liste, saha baglantisi ve gunun sayisi hic gelmedi).
 15. Aday araci bu turda stok satirinda "liste bitiyor" dediyse durum kaydinda siradaki_cekim var mi (ya da
     oturumda aday_ara cagrildi mi): yoksa liste birkac gunde biter (z2 gun 7 kapanisi).
 14. Bu turda saha paketi kurulduysa (saha-paketi) paketteki yazili kanal adaylarinin gonderecek metni var
     mi: yoksa telefondaki kartta yalniz Gonderdim kalir (z2 gun 7: 24 yazili aday metinsiz yuklendi).
 12. Durum kaydi bu turda yazildiysa (dosya ya da durum_yaz) icindeki siradaki_cekim gece gorevinin
     okudugu adlarla mi (reklam_kelimeleri, istek_tarihi; istek_tarihi son uc gunde): degilse gece
     cekimi hic baslamaz ama ogrenciye "bu gece cekiliyor" denmistir (z2 tur 42).
  6-8'de tirnak, kod ve alinti icindeki hazir metinler sayilmaz. 6-8 yalniz kalici metne bakar:
  turun son mesaji ve panel notu (odak_yaz). Araclar arasindaki ara mesaj ogrenciye coktan gitti;
  onu duzeltmek icin durdurmak turun sonuna baglamsiz yeni bir mesaj ekletiyordu (simulasyonda
  kapanis mesajindan sonra "Birkac dakika icinde bitiyor" kaldi).
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


def ifade_disi(metin):
    """alinti_disi'na ek olarak satir ici kod ve tek tirnakli ifade ('Check for updates')
    cikarilir. Turkce ek kesmesi (Beyni'ne, Ajansim'da) tirnak sayilmaz: acan tirnagin
    onunde harf olmaz, kapayanin arkasinda harf olmaz."""
    m = alinti_disi(metin)
    m = re.sub(r"`[^`\n]*`", " ", m)
    m = re.sub(r"(?<![\w])['‘][^'’\n]{1,120}['’](?![\w])", " ", m)
    return m


# Ogrenciye "panele gonderdim" denmez (cekirdek, "Panel: odak ve tur"): panel kendiliginden
# tazelenir; soylenecek sey panelde ne acildigi ya da ne gorundugudur.
PANELE_GONDERDIM = re.compile(
    r"\bpanel(?:e|ine|inize)\s+(?:de\s+)?(?:g[öo]nder(?:iyorum|dim|dik|iyoruz|eceğim|ece[gğ]iz)"
    r"|yolla(?:d[ıi]m|d[ıi]k|yaca[ğg][ıi]m)|yoll[uı]yorum|y[üu]kl(?:edim|edik|[üu]yorum|eyece[ğg]im)"
    r"|at(?:t[ıi]m|[ıi]yorum))\b", re.I)
# Hayalet mesaj: "ozeti gonderdim", "yukarida yazdim" denip o metin bu turda ekranda yoksa. 2 Ekim z1:
# tur ortasinda baglam sikistirildi, model kapanis ozetini gonderdigini sandi; ogrencinin gordugu tek
# cumle "Birinci günün kapanış özetini gönderdim ve kayıtlar güncel. Cevabını bekliyorum." oldu.
HAYALET = re.compile(
    r"(?:[öo]zet\w*|kapan[ıi][şs]\w*|mesaj\w*|soru\w*|plan\w*|liste\w*|cevab\w*)[^.\n]{0,40}"
    r"(?:g[öo]nderdim|yollad[ıi]m|ilettim|payla[şs]t[ıi]m)|\byukar[ıi]da(?:ki)?\b", re.I)


def gorunen_diger_uzunluk(kayitlar, son_metin):
    """Bu turda ogrencinin sohbette gordugu metnin (ara metinler ve SendUserMessage) son mesaj disindaki uzunlugu."""
    toplam = 0
    for k in kayitlar:
        if k.get("type") != "assistant":
            continue
        icerik = (k.get("message") or {}).get("content")
        parcalar = [icerik] if isinstance(icerik, str) else []
        for p in icerik if isinstance(icerik, list) else []:
            if not isinstance(p, dict):
                continue
            if p.get("type") == "text":
                parcalar.append(p.get("text") or "")
            elif p.get("type") == "tool_use" and "SendUserMessage" in (p.get("name") or ""):
                parcalar.append(str((p.get("input") or {}).get("message") or ""))
        for x in parcalar:
            x = x.strip()
            if x and x != (son_metin or "").strip():
                toplam += len(x)
    return toplam


# Gunun ilk mesaji: kisa selamla (gunaydin) gelen turda panel linki ve dune bagli cumle ekrana hic gelmezse.
# 2 Ekim z1 gun 4: "günaydın"dan sonra uc dakika sessiz is yapildi, gorunen tek metin "Kesin fiyat kondu..." oldu;
# panel linki, selam, dun ve bugunun isi yoktu (sim-y2 Y4 ile ayni kalip).
SELAM = re.compile(r"^\s*(?:g[üu]nayd[ıi]n+|ba[şs]layal[ıi]m|haz[ıi]r[ıi]m)[\s.!,]*$", re.I)


def kullanici_metni(k):
    icerik = (k.get("message") or {}).get("content")
    if isinstance(icerik, str):
        return icerik
    if isinstance(icerik, list):
        return " ".join(p.get("text") or "" for p in icerik if isinstance(p, dict) and p.get("type") == "text")
    return ""


def panel_linki(kok):
    try:
        with open(os.path.join(kok, "is-beyni.md"), encoding="utf-8") as f:
            s = f.read(30000)
    except Exception:
        return None
    m = re.search(r"Panel linki[^\n]*?(https?://[^\s)]+/panel/[A-Za-z0-9_-]+)", s)
    return m.group(1) if m else None


def gorunen_metin(kayitlar):
    """Bu turda ogrencinin sohbette gordugu metin (ara metinler ve SendUserMessage)."""
    parcalar = []
    for k in kayitlar:
        if k.get("type") != "assistant":
            continue
        icerik = (k.get("message") or {}).get("content")
        if isinstance(icerik, str):
            parcalar.append(icerik)
            continue
        for p in icerik if isinstance(icerik, list) else []:
            if not isinstance(p, dict):
                continue
            if p.get("type") == "text":
                parcalar.append(p.get("text") or "")
            elif p.get("type") == "tool_use" and "SendUserMessage" in (p.get("name") or ""):
                parcalar.append(str((p.get("input") or {}).get("message") or ""))
    return "\n".join(parcalar)


# Ingilizce ic not: modelin kendine yazdigi plan cumlesi ekrana dusuyor.
INGILIZCE_NOT = re.compile(
    r"(?<![\w])(?:Step \d|Let me |Let's |I'll |I will |I need to |I'm going to |Now I |Next,? I |First,? I |"
    r"Okay,? (?:so|now|let)\b)")
# Hazirligin blok numarasi ic sozdur; pencere adlari (sabah blogu, arama blogu) degildir.
BLOK_NUMARASI = re.compile(
    r"\b(?:birinci|ikinci|üçüncü|dördüncü|beşinci|[1-5]\.|bir sonraki|sonraki|önceki)\s+blo(?:k|ğ)", re.I)


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
            # Panelin "Su an" karti (odak_yaz): not, bekleyen ve sonraki ogrencinin ekraninda durur.
            if (p.get("name") or "").endswith("odak_yaz"):
                metinler += odak_metinleri(p)
    return metinler, araclar


# Su an kartinin kopyalanacak cumlesinde (odak_yaz sonraki) ornek numara ya da yer tutucu:
# ogrenci cumleyi aynen yapistirir, sahte numara siteye girer.
SONRAKI_YER_TUTUCU = re.compile(r"\b0?5\d?[xX]{2}\b|\b[xX]{2,3}\s[xX]{2,3}\b|\[[^\]]{1,40}\]|\.\.\.|…")


def sonraki_yer_tutucu(araclar):
    for a in araclar:
        if not (a.get("name") or "").endswith("odak_yaz"):
            continue
        girdi = a.get("input") or {}
        sonraki = str(girdi.get("sonraki") or "") if isinstance(girdi, dict) else ""
        m = SONRAKI_YER_TUTUCU.search(sonraki)
        if m:
            return sonraki
    return None


# Turun son mesaji "bitince yazacagim" diye bitiyor ama arka planda calisan bir is yok: tur
# bitince hicbir sey calismaz, ogrenci bosuna bekler (simulasyonda "Bitince sonucu yazacagim").
BEKLEME_SOZU = re.compile(
    r"(bitince|birazdan|haz[ıi]r olunca|tamamlan[ıi]nca|sonu[çc] gelince)[^.\n?]{0,60}"
    r"(yazaca[ğg][ıi]m|haber verece[ğg]im|d[öo]nece[ğg]im|s[öo]yleyece[ğg]im|getirece[ğg]im|payla[şs]aca[ğg][ıi]m|g[öo]sterece[ğg]im)",
    re.I)


# Destek ekibine Claude ulasamaz; "destege bildirecegim" sozu tutulamaz (cekirdek, takilma).
DESTEGE_BILDIRIRIM = re.compile(
    r"destek(?:e| hatt[ıi]na| ekibine| ekibimize)[^.\n]{0,40}(bildirece[ğg]im|iletece[ğg]im|yazaca[ğg][ıi]m|haber verece[ğg]im|ula[şs]aca[ğg][ıi]m)", re.I)


def arka_plan_var(araclar):
    for a in araclar:
        girdi = a.get("input") or {}
        if not isinstance(girdi, dict):
            continue
        if str(girdi.get("run_in_background", "")).lower() in ("true", "1"):
            return True
    return False


def gunaydinla_bitti(araclar):
    """Bu turda odak 'bitti' ve sonraki 'Günaydın' gitti mi (gunun son kapanisi)."""
    for a in araclar:
        if not (a.get("name") or "").endswith("odak_yaz"):
            continue
        girdi = a.get("input") or {}
        if not isinstance(girdi, dict) or girdi.get("durum") != "bitti":
            continue
        sonraki = re.sub(r"[^a-zçğıöşü]", "", str(girdi.get("sonraki") or "").lower().replace("i\u0307", "i"))
        if sonraki in ("günaydın", "gunaydin"):
            return True
    return False


def ilk_blok_acik_mi(kok):
    """Klasordeki durum kaydi hala birinci blokta mi (blok 1, saha kapali)."""
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return False
    if not isinstance(d, dict) or d.get("saha_acik"):
        return False
    try:
        return int(d.get("blok") or 0) == 1
    except (TypeError, ValueError):
        return False


# Sessiz duzeltmeden sonra model genelde yine bir sey yaziyor ("Durum kaydi sunucuya gitti.",
# "Cevabini bekliyorum"). En zararsiz son: ogrencinin ekrandaki son sorusunun aynen tekrari.
SESSIZ_BITIS = ("Araçtan sonra öğrenciye kayıttan, sunucudan, panelden ya da araçtan söz etme. Turu, öğrenciye "
                "son sorduğun soruyu ya da son cümleni tek cümle olarak aynen yineleyerek bitir; başka hiçbir şey ekleme.")


# Aday araci listeyi degistirdiyse (guncelle, yuz-sec, temas, ekle, sil, isaret, cek) panele gonderilmeden
# tur bitmesin: panelin Adaylar'i ve Mesajlar'daki Truva studyosu satirlardan cizilir (panel-vitrini).
# 1 Ekim s3: ilk mesaj aday satirina yazildi, panel --yukle calismadi, ogrenciye "panelde gorunuyor" dendi.
ARAC_YAZAN = re.compile(r"adaylar-arac\.py[^\n;&|]*?\s(guncelle|yuz-sec|temas|ekle|sil|isaret|cek)\b([^\n;&|]*)")
ARAC_PANEL = re.compile(r"adaylar-arac\.py[^\n;&|]*?\spanel\b[^\n;&|]*--yukle")


PANEL_DOSYASI = re.compile(r"\.founderos/panel/[a-z-]+\.json")
PANEL_DOSYASI_YAZAN = re.compile(r"json\.dump|\.write\(|write_text|>\s*\S*\.founderos/panel/")


def panel_dosyasi_gonderilmedi(araclar):
    """Bu turda panel dosyasi (.founderos/panel/*.json) yazildi ve sonra panel --yukle ya da panel_yaz
    gitmedi mi. Simulasyon k2: konumlandirma ajans.json'a yazildi, ogrenciye 'uzun hali panelde, Fark
    kutusunda' dendi, panel bos kaldi."""
    kirli = False
    for a in araclar:
        ad = a.get("name") or ""
        girdi = a.get("input") or {}
        if not isinstance(girdi, dict):
            continue
        if ad.endswith("panel_yaz"):
            kirli = False
            continue
        if ad in ("Write", "Edit", "MultiEdit") and PANEL_DOSYASI.search(str(girdi.get("file_path") or "")):
            kirli = True
            continue
        if ad == "Bash" or ad.endswith("device_bash"):
            komut = str(girdi.get("command") or "")
            yaz = [mm.start() for mm in PANEL_DOSYASI.finditer(komut)] if PANEL_DOSYASI_YAZAN.search(komut) else []
            gonder = [mm.start() for mm in ARAC_PANEL.finditer(komut)] if "adaylar-arac.py" in komut else []
            if yaz and (not gonder or max(gonder) < max(yaz)):
                kirli = True
            elif gonder:
                kirli = False
    return kirli


def panel_gonderilmedi(araclar):
    """Bu turda aday araci listeyi degistirdi ve sonra panel --yukle (ya da panel_yaz) calismadi mi."""
    kirli = False
    for a in araclar:
        ad = a.get("name") or ""
        if ad.endswith("panel_yaz"):
            kirli = False
            continue
        if ad != "Bash" and not ad.endswith("device_bash"):
            continue
        komut = str((a.get("input") or {}).get("command") or "")
        if "adaylar-arac.py" not in komut:
            continue
        olaylar = [(m.start(), "yaz") for m in ARAC_YAZAN.finditer(komut)
                   if not (m.group(1) == "cek" and "--ozet" in m.group(2))]
        olaylar += [(m.start(), "panel") for m in ARAC_PANEL.finditer(komut)]
        for _, tur in sorted(olaylar):
            kirli = tur == "yaz"
    return kirli


PANEL_SATIRI = re.compile(r"^\s*-\s*Panel linki[^:\n]*:\s*(https?://\S+)", re.M)


def saha_plani_eksikleri(kok, araclar):
    """Saha acikken gunaydin turunda bugunun listesi kuruldu mu, gece hazirligina bakildi mi.
    z2 gun 7 (tur 43-44): ilk musterinin ertesi sabahi gunaydin gunu "tek is: kurulum saati"ne indirdi;
    liste, saha baglantisi ve gunun sayisi hic gelmedi, siradaki_cekim icin durum_oku yapilmadi.
    Donus: eksikler ("liste", "gece"); saha kapaliyken ve hafta sonu bos."""
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return []
    if not isinstance(d, dict) or not d.get("saha_acik"):
        return []
    import datetime
    simdi = datetime.datetime.now()
    gunler = {simdi.date().isoformat(), (simdi - datetime.timedelta(hours=5)).date().isoformat()}
    if simdi.date().weekday() >= 5:
        return []
    try:
        with open(os.path.join(kok, ".founderos", "saha-paketi.json"), encoding="utf-8") as f:
            p = json.load(f)
        tarih = str(p.get("tarih") or "")[:10] if isinstance(p, dict) else ""
    except Exception:
        tarih = ""
    eksik = [] if tarih in gunler else ["liste"]
    if isinstance(d.get("siradaki_cekim"), dict) and not any((a.get("name") or "").endswith("durum_oku") for a in araclar):
        eksik.append("gece")
    return eksik


def arac_ciktilari(kayitlar):
    """Kayittaki arac sonuclarinin metinleri (user kayitlarindaki tool_result)."""
    for k in kayitlar:
        if k.get("type") != "user":
            continue
        c = (k.get("message") or {}).get("content")
        if not isinstance(c, list):
            continue
        for p in c:
            if not (isinstance(p, dict) and p.get("type") == "tool_result"):
                continue
            cc = p.get("content")
            if isinstance(cc, str):
                yield cc
            elif isinstance(cc, list):
                for x in cc:
                    if isinstance(x, dict) and x.get("type") == "text":
                        yield str(x.get("text") or "")


def siradaki_cekim_var(kok):
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return True
    return isinstance(d, dict) and isinstance(d.get("siradaki_cekim"), dict)


def saha_paketi_kuruldu(araclar):
    for a in araclar:
        ad = a.get("name") or ""
        g = a.get("input") or {}
        if (ad == "Bash" or ad.endswith("device_bash")) and isinstance(g, dict) and "saha-paketi" in str(g.get("command") or ""):
            return True
    return False


def metinsiz_yazili_adaylar(kok):
    """Bugunun saha paketinde gonderecek metni olmayan yazili kanal adaylari (adlari). Listedeki satirda
    metin varsa (paket boyut yuzunden kirpti) sayilmaz. z2 gun 7: 24 yazili adayin hicbirinde metin yoktu."""
    try:
        with open(os.path.join(kok, ".founderos", "saha-paketi.json"), encoding="utf-8") as f:
            p = json.load(f)
        adaylar = p.get("adaylar") or []
    except Exception:
        return []
    satir = {}
    try:
        import csv
        with open(os.path.join(kok, "adaylar.csv"), encoding="utf-8-sig", newline="") as f:
            for s in csv.DictReader(f):
                satir[s.get("ad")] = s
    except Exception:
        pass
    bos = []
    for x in adaylar:
        if not isinstance(x, dict):
            continue
        alan = "dm_metni" if x.get("kanal") == "instagram" else "eposta_metni" if x.get("kanal") == "e-posta" else None
        if alan and not str(x.get(alan) or "").strip() and not str((satir.get(x.get("ad")) or {}).get(alan) or "").strip():
            bos.append(str(x.get("kisa_ad") or x.get("ad") or "?"))
    return bos


def gunaydin_acildi(araclar):
    return any(a.get("name") == "Skill" and str((a.get("input") or {}).get("skill", "")).endswith("gunaydin")
               for a in araclar)


def panel_linki(kok):
    try:
        with open(os.path.join(kok, "is-beyni.md"), encoding="utf-8", errors="ignore") as f:
            m = PANEL_SATIRI.search(f.read(20000))
    except Exception:
        return None
    return m.group(1).rstrip(").,;") if m else None


def son_odak_bekleyen(kayitlar):
    """Kayitlardaki son odak_yaz 'Senden' satiri birakti mi (bekleyen); biraktiysa metni."""
    son = None
    for k in kayitlar:
        if k.get("type") != "assistant":
            continue
        for p in (k.get("message") or {}).get("content") or []:
            if isinstance(p, dict) and p.get("type") == "tool_use" and str(p.get("name") or "").endswith("odak_yaz") and isinstance(p.get("input"), dict):
                son = p["input"]
    if not son:
        return None
    b = str(son.get("bekleyen") or "").strip()
    # Prova ve canli gorusme rol oyunu: kart "sirani bekliyorum" der ve her turda gecerlidir. Her cevapta
    # odak istemek oyunun replik satirini ogrenciye iki kez yazdiriyordu (z2 tur 28).
    if str(son.get("is") or "") in ("gorusme-provasi-yap", "gorusmeyi-yonet"):
        return None
    return b if b and son.get("durum") in ("bekliyor", "basladi", "calisiyor") else None


def odak_metinleri(arac):
    girdi = arac.get("input") or {}
    if not isinstance(girdi, dict):
        return []
    return [str(girdi.get(k)) for k in ("not", "bekleyen", "sonraki") if girdi.get(k)]


def gercek_kullanici_mi(k):
    # Beceri acilinca govdesi kayda isMeta'li bir kullanici mesaji olarak girer; ogrencinin
    # yazdigi degildir. Sayilirsa beceriden onceki yazimlar turdan duser (1 Ekim x4: Edit'ten
    # sonra beceri acildi, kanca "yazmadin" dedi, ogrenci "Simdi gercekten yazdim" gordu).
    if k.get("isMeta") or k.get("sourceToolUseID"):
        return False
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


# Veri baglantisinin (sunucu MCP) araclari; ad "mcp__<sunucu>__<arac>" bicimindedir.
VERI_ARACLARI = {"odak_yaz", "durum_yaz", "durum_oku", "aday_ara", "aday_sonuc", "kullanim", "olcum_yaz", "saha_yukle",
                 "saha_sonuclari", "panel_yaz", "demo_olustur", "demolar"}


def durum_kaydi_yazildi(arac):
    """Bu arac durum kaydina yazdi mi (dosya araci ya da kabukla)."""
    ad = arac.get("name") or ""
    g = arac.get("input") or {}
    if not isinstance(g, dict):
        return False
    if ad in YAZMA_ARACLARI:
        return str(g.get("file_path") or "").replace("\\", "/").endswith(".founderos/durum.json")
    if ad == "Bash" or ad.endswith("device_bash"):
        k = str(g.get("command") or "")
        # Yalniz gercek yazim: durum.json'a yonlendirme, tee, sed -i ya da Python ile
        # yazma. "2>&1; cat .founderos/durum.json" gibi okuma sayilmaz.
        return bool(
            re.search(r">>?\s*['\"]?[^\s;|&'\"]*durum\.json", k)
            or re.search(r"\btee\s+(-a\s+)?['\"]?[^\s;|&'\"]*durum\.json", k)
            or re.search(r"\bsed\s+-i[^;|&]*durum\.json", k)
            or (re.search(r"durum\.json", k) and re.search(r"write_text|json\.dump\(|open\([^)]*['\"][wa]", k))
        )
    return False


def veri_araci_mi(arac):
    ad = arac.get("name") or ""
    return ad.startswith("mcp__") and ad.rsplit("__", 1)[-1] in VERI_ARACLARI


# Panelin (ve gece gorevinin) okudugu alanlar; adim, acik_modul ve guncellendi her soruda
# degisir, sayilmaz. panel_turu ve son_kapanis yalniz klasorde ise yarar (site okumaz): onlar
# icin kanca tetiklenmez, yoksa ogrenci gereksiz ikinci bir mesaj gorur.
ONEMLI_ALANLAR = ("gun_baslangic", "duzen", "blok", "oturus", "yol_haritasi_asamasi", "ilerleme_asamasi", "sonraki_adim",
                  "saha_acik", "gunluk_hedef", "gecim_musteri", "sayaclar", "siradaki_cekim", "aktif_musteriler")


def durum_eski_mi(kok, son_gonderilen):
    """Klasordeki durum kaydinin panelin okudugu alanlari sunucuya son gidenden farkli mi."""
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            yerel = json.load(f)
    except Exception:
        return False
    if not isinstance(yerel, dict):
        return False
    son = son_gonderilen if isinstance(son_gonderilen, dict) else {}
    alanlar = ONEMLI_ALANLAR
    # Birinci blokta panel o anki isi odaktan gosterir; sonraki_adim her soruda degisir ve
    # oturusun sonunda oturus/blok ile birlikte gider. Yalniz o degistiyse kanca susar
    # (1 Ekim x4: ogrenci ayni soruyu ust uste iki kez goruyordu).
    if yerel.get("blok") == 1 and not yerel.get("saha_acik"):
        alanlar = tuple(k for k in ONEMLI_ALANLAR if k != "sonraki_adim")
    return any(yerel.get(k) != son.get(k) for k in alanlar if k in yerel or k in son)


def gorusmesiz_musteri(kok):
    """Durum kaydinda musteri sayisi gorusme sayisindan buyuk mu: evet gorusmenin icinden geldi,
    gorusme sayaca yazilmadi (z2 tur 39: randevu 1, gorusme 0, musteri 1). Donus: (musteri, gorusme) ya da None."""
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            d = json.load(f)
        say = d.get("sayaclar") or {}
        m, g = int(say.get("musteri") or 0), int(say.get("gorusme") or 0)
    except Exception:
        return None
    return (m, g) if m > g else None


# Gece gorevi (sitede lib/gece.ts) yalniz bu adlari okur; istek_tarihi yoksa ya da uc gunden eskiyse
# cekim hic baslamaz. z2 tur 42: kapanis `kelimeler` ve `tarih` yazdi, ogrenciye "bu gece cekiliyor" dendi.
SIRADAKI_YANLIS_AD = (("kelimeler", "reklam_kelimeleri"), ("anahtar_kelimeler", "reklam_kelimeleri"),
                      ("tarih", "istek_tarihi"), ("istek", "istek_tarihi"))


def siradaki_cekim_sorunlari(kok):
    """Durum kaydindaki siradaki_cekim sunucunun okudugu bicimde mi. Donus: kisa sorun listesi (bos: sorun yok)."""
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return []
    c = d.get("siradaki_cekim") if isinstance(d, dict) else None
    if not isinstance(c, dict):
        return []
    sorun = ["`%s` değil `%s`" % (yanlis, dogru) for yanlis, dogru in SIRADAKI_YANLIS_AD if yanlis in c and dogru not in c]
    for alan in ("kategori", "sehir"):
        if not str(c.get(alan) or "").strip():
            sorun.append("`%s` boş" % alan)
    t = str(c.get("istek_tarihi") or "").strip()[:10]
    try:
        import datetime
        fark = (datetime.date.today() - datetime.date.fromisoformat(t)).days
        if fark < 0 or fark > 3:
            sorun.append("`istek_tarihi` bugün değil (%s)" % t)
    except ValueError:
        if not any("istek_tarihi" in s for s in sorun):
            sorun.append("`istek_tarihi` yok")
    if "reklam_kelimeleri" in c and not isinstance(c.get("reklam_kelimeleri"), list):
        sorun.append("`reklam_kelimeleri` liste değil")
    return sorun


def teslimati_eksik_musteriler(kok):
    """Durum kaydindaki aktif musterilerden panelin teslimat dosyasinda olmayanlar.
    Klasorde musteri dosyasi yoksa (bilgisayar degisti, durum kaydi sunucudan kuruldu) bos doner:
    satiri kuracak bilgi yok, yazilan bos satir sunucudaki dolu Teslimat bolumunun ustune gider
    (simulasyon z3, uc durum d: Teslimat yalniz adla kaldi)."""
    try:
        md = [f for f in os.listdir(os.path.join(kok, "musteriler")) if f.endswith(".md")]
    except Exception:
        md = []
    if not md:
        return []
    try:
        with open(os.path.join(kok, ".founderos", "durum.json"), encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return []
    aktif = [str(x).strip() for x in (d.get("aktif_musteriler") or []) if str(x).strip()] if isinstance(d, dict) else []
    if not aktif:
        return []
    adlar = set()
    try:
        with open(os.path.join(kok, ".founderos", "panel", "teslimat.json"), encoding="utf-8") as f:
            t = json.load(f)
        for m in (t.get("musteriler") or []) if isinstance(t, dict) else []:
            if isinstance(m, dict) and str(m.get("ad") or "").strip():
                adlar.add(str(m.get("ad")).strip().casefold())
    except Exception:
        pass
    # Ad birebir tutmayabilir ("Akın Mühendislik" / "Akın Mühendislik Klima"): biri ötekini içeriyorsa aynı müşteri.
    return [a for a in aktif if not any(a.casefold() in x or x in a.casefold() for x in adlar)]


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
    veri_acik = False
    son_durum = None
    for i, k in enumerate(kayitlar):
        tip = k.get("type")
        if tip == "user" and gercek_kullanici_mi(k):
            son_kullanici = i
        if tip == "assistant":
            _, araclar = metin_parcalari((k.get("message") or {}).get("content"))
            for a in araclar:
                if a.get("name") == "Skill" and str((a.get("input") or {}).get("skill", "")).startswith("founderos:"):
                    founderos = True
                if veri_araci_mi(a):
                    veri_acik = True
                if (a.get("name") or "").endswith("durum_yaz"):
                    g2 = a.get("input") or {}
                    d2 = g2.get("durum") if isinstance(g2, dict) else None
                    if isinstance(d2, str):
                        try:
                            d2 = json.loads(d2)
                        except Exception:
                            d2 = None
                    son_durum = d2
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
    # Kalici metin: turun son mesaji ve panel notlari (6-8 yalniz buna bakar).
    son_metin = son_mesaj
    if not son_metin:
        for k in reversed(kayitlar[son_kullanici + 1:]):
            if k.get("type") != "assistant":
                continue
            icerik = (k.get("message") or {}).get("content")
            parcalar = [icerik] if isinstance(icerik, str) else [p.get("text") or "" for p in icerik or [] if isinstance(p, dict) and p.get("type") == "text"]
            parcalar = [x for x in parcalar if x.strip()]
            if parcalar:
                son_metin = parcalar[-1]
                break
    kalici = "\n".join([x for a in son_araclar if (a.get("name") or "").endswith("odak_yaz") for x in odak_metinleri(a)] + [son_metin or ""])

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
    duz = ifade_disi(kalici)
    pg = PANELE_GONDERDIM.search(duz)
    if pg:
        sorunlar.append("Öğrenciye '%s' dedin; panele gönderdiğini söylemezsin, panel kendiliğinden tazelenir. Gerekiyorsa panelde ne açıldığını ya da ne göründüğünü söyle ('Panelde Pazar Radarı açıldı; sayım orada akıyor'), gerekmiyorsa hiç söyleme. Yalnız o cümleyi düzelt." % pg.group(0))
    ing = INGILIZCE_NOT.search(duz)
    if ing:
        sorunlar.append("Öğrenciye giden metne İngilizce bir iç not düştü (%s). Kendine yazdığın plan cümlelerini ekrana yazmazsın; öğrenciye yalnız Türkçe, yapılan işi söyle." % ing.group(0).strip())
    bn = BLOK_NUMARASI.search(duz)
    if bn:
        sorunlar.append("Öğrenciye giden metinde hazırlığın blok numarası var (%s). Blok iç sözdür; o günün işiyle söyle ('kesin rakamı aday listesini çıkardığımız gün koyuyoruz'). Panel notunda da aynı kural." % bn.group(0))
    if son_kullanici >= 0 and SELAM.match(kullanici_metni(kayitlar[son_kullanici])):
        link = panel_linki(g.get("cwd") or os.getcwd())
        gorunen = gorunen_metin(kayitlar[son_kullanici + 1:]) + "\n" + (son_mesaj or "")
        if link and link not in gorunen and "Panelini aç" not in gorunen:
            sorunlar.append("Öğrenci günü selamla açtı ama günün ilk mesajı ekranda yok: ilk satır `[Panelini aç](%s)`, sonra dünü tek cümleyle bağlayan cümle ve bugünün işi (founderos:gunaydin, 'İlk satır panel', 'İlk cümle düne bağlanır'). O mesajı şimdi tek parça yaz; bu turda yaptığın işi bir iki cümleyle içine kat, öğrenciden bir şey bekliyorsan sonda tek soru." % link)
    hy = HAYALET.search(ifade_disi(son_metin or ""))
    if hy and len((son_metin or "").strip()) < 260 and gorunen_diger_uzunluk(kayitlar[son_kullanici + 1:], son_metin) < 300:
        sorunlar.append("Öğrenci bu turda sohbette yalnız şu kısa cümleyi gördü: \"%s\". Söz ettiğin mesaj ekranda yok; düşüncedeki taslak ya da bağlam sıkıştırılmadan önceki plan gönderilmiş sayılmaz. O mesajın kendisini şimdi tek parça yaz (kapanışsa kapanışın kendisi, soruysa sorunun kendisi); kısa cümleyi tekrar etme, gönderdiğini söyleme." % (son_metin or "").strip()[:160])
    bs = BEKLEME_SOZU.search(ifade_disi(son_metin or ""))
    if bs and not arka_plan_var(son_araclar):
        sorunlar.append("Turu '%s' sözüyle bitirdin ama arka planda çalışan bir iş yok; tur bitince hiçbir şey çalışmaz, öğrenci boşuna bekler. Söz verdiğin işi şimdi bu turda yap ve sonucunu kısaca söyle; öğrenciden bir şey bekliyorsan onu tek cümleyle sor." % bs.group(0)[:60])
    db = DESTEGE_BILDIRIRIM.search(ifade_disi(son_metin or ""))
    if db:
        sorunlar.append("Öğrenciye '%s' dedin; destek ekibine sen ulaşamazsın, bu söz tutulmaz. O cümleyi düzelt: gerekiyorsa beş satırlık destek özetini ver, WhatsApp'tan ya da e-postayla gönderen öğrencidir; gerekmiyorsa hiç söyleme." % db.group(0)[:60])
    syt = sonraki_yer_tutucu(son_araclar)
    if syt:
        sorunlar.append(("Şu an kartındaki kopyalanacak cümlede örnek ya da yer tutucu var (%s). Öğrenci onu aynen yapıştırır. Öğrencinin kendi bilgisini ya da serbest cevabını istiyorsan odak_yaz'ı aynı durumla, `sonraki` olmadan yeniden gönder. " % syt[:60]) + SESSIZ_BITIS)
    kok = g.get("cwd") or os.getcwd()
    # Birinci gunun son kapanisi ("Günaydın"la biten odak) durum kaydini ikinci bloga gecirir
    # (kurulum, Kontrol adimi). Gecmezse ertesi sabah panel "devam yaz" der, gunaydin birinci
    # gunu yeniden acmaya kalkar.
    if gunaydinla_bitti(son_araclar) and ilk_blok_acik_mi(kok):
        sorunlar.append("Birinci günün son kapanışını yaptın ama durum kaydı hâlâ birinci blokta. Durum kaydında `blok` 2, `oturus` 1, `adim` boş, `sonraki_adim` \"Araçlar ve sayfanın yayını.\", `yol_haritasi_asamasi` 4 yaz ve aynı içeriği durum_yaz ile gönder. " + SESSIZ_BITIS)
    elif veri_acik and any(durum_kaydi_yazildi(a) for a in son_araclar) and durum_eski_mi(kok, son_durum):
        sorunlar.append("Durum kaydını bu turda güncelledin ama sunucuya göndermedin; panel eski aşamada kaldı. Aynı içeriği şimdi veri bağlantısının durum_yaz aracıyla gönder: panelin sayaçları, aşaması ve müşterisi oradan okunur. " + SESSIZ_BITIS)
    if not panel_gonderilmedi(son_araclar) and panel_dosyasi_gonderilmedi(son_araclar):
        sorunlar.append("Panel dosyasını (.founderos/panel/) bu turda değiştirdin ama panele göndermedin; panelde gösterdiğin şey orada yok. Öğrencinin klasöründe aracın panel --yukle komutunu sessiz çalıştır. " + SESSIZ_BITIS)
    if panel_gonderilmedi(son_araclar):
        sorunlar.append("Aday listesini bu turda değiştirdin (aday aracının yazan komutu) ama panele göndermedin; panelin Adaylar bölümü ve Mesajlar'daki Truva mesaj stüdyosu eski satırları gösteriyor. Öğrencinin klasöründe aracın panel --yukle komutunu sessiz çalıştır. " + SESSIZ_BITIS)
    # Gunun ilk mesaji (gunaydin): ilk satiri panel linki. z2 tur 1 ve 7: link, dune bagli cumle ve gunun
    # isi hic yazilmadi; istem kancasinin hazir linkli notuna ragmen tur yalniz isin sonucuyla bitti.
    # Yeni sohbette yan panel yalniz bu baglantiyla acilir. Link turun hicbir metninde yoksa sona eklenir.
    link = panel_linki(kok) if gunaydin_acildi(son_araclar) else None
    if link and link not in metin:
        sorunlar.append(("Günün ilk mesajı gitmedi: panel linki ve düne bağlı cümle öğrenciye hiç yazılmadı; yeni sohbette yan panel "
                         "bu bağlantıyla açılır. Şimdi kısa bir mesaj yaz: ilk satır tam olarak [Panelini aç](%s), altında düne bağlı "
                         "tek cümle (dün ne oldu) ve bugünün tek işi, tek cümle. Az önce yazdığını tekrar anlatma; öğrenciden bir şey "
                         "istediysen mesaj o isteğin tek cümlelik aynısıyla biter. Kayıttan, panelden ya da araçtan söz etme.") % link)
    sp = saha_plani_eksikleri(kok, son_araclar) if gunaydin_acildi(son_araclar) else []
    if sp:
        parca = []
        if "gece" in sp:
            parca.append("Durum kaydında `siradaki_cekim` duruyor: önce `durum_oku`; `gece_cekimi` geldiyse listeyi `cek --is` ile al, "
                         "gelmediyse çekimi şimdi `aday_ara` ile başlat (founderos:veri-servisi, gece hazırlığı).")
        if "liste" in sp:
            parca.append("Saha açık ama bugünün listesi kurulmadı; müşteri işi, görüşme ya da öğrenciden beklenen bir cevap sahanın "
                         "yerine geçmez. Şimdi founderos:gunu-planla: aday aracıyla `bugun --planla`, ardından `saha-paketi --yukle`; "
                         "dönen saha bağlantısını ve günün sayısını (durum kaydındaki `gunluk_hedef` ve dağılımı) öğrenciye kısa bir "
                         "mesajla ver.")
        sorunlar.append(" ".join(parca) + " Öğrenciye sorduğun bir soru varsa mesaj o sorunun tek cümlelik aynısıyla biter. "
                        "Kayıttan, panelden ya da araçtan söz etme.")
    # z2 gun 7: aksam kapanisi stok 4.7 gunken siradaki_cekim yazmadi (gun 6'da yazmisti); arac stok satirini
    # basar, burada yalniz o satir bu turda ciktiysa ve ne istek ne oturumda cekim varsa durdurulur.
    if any(">>> liste bitiyor" in t for t in arac_ciktilari(kayitlar[son_kullanici + 1:])) \
            and not siradaki_cekim_var(kok) and not any((a.get("name") or "").endswith("aday_ara") for a in son_araclar):
        sorunlar.append("Aday aracı bu turda stok satırında \"liste bitiyor\" dedi ama durum kaydında `siradaki_cekim` yok; liste "
                        "birkaç günde biter. Sıradaki yeri seç (founderos:veri-servisi, gece hazırlığı: ilk çekim şehir geneliyse kartın "
                        "diğer Haritalar kategori adı, sonra çekilmemiş ilçe, sonra komşu il), `siradaki_cekim`'i tam alan adlarıyla yaz "
                        "(kategori, sehir, ilce, hedef, reklam_kelimeleri, istek_tarihi bugün) ve aynı içeriği durum_yaz ile gönder. "
                        "Listenin bu gece çekileceğini öğrenciye bu turda söylemediysen tek cümle: \"Listen beş günlük işin altına indi; "
                        "yeni ilçenin listesi bu gece çekiliyor, sabah hazır.\" Söylediysen yeni bir şey yazma, öğrenciye son sorduğun "
                        "soruyu ya da son cümleni tek cümle olarak aynen yinele. Kayıttan, panelden ya da araçtan söz etme.")
    mz = metinsiz_yazili_adaylar(kok) if saha_paketi_kuruldu(son_araclar) else []
    if mz:
        sorunlar.append(("Bugünün saha listesinde %d yazılı aday metinsiz (%s); telefondaki kartta gönderecek metin yok, yalnız "
                         "Gönderdim düğmesi var. Bu adayların metnini founderos:adaya-mesaj-yaz kuralıyla (gözlemden, adaya özel) yaz, "
                         "aday aracının guncelle komutuyla satırına işle (Instagram: `dm_metni`; e-posta: `eposta_konu` ve `eposta_metni`), "
                         "sonra `saha-paketi --yukle`'yi yeniden çalıştır. Gözlemi olmayan adaya yazılı mesaj yazılmaz, o aday bugünün "
                         "listesinden telefona bırakılır. Öğrenciye tek cümle: Instagram ve e-posta mesajları telefondaki kartlarında "
                         "hazır, kartta \"Mesajı kopyala\"ya basıp kendi hesabından gönderecek, sonra \"Gönderdim\". Öğrenciye sorduğun "
                         "bir soru varsa mesaj o sorunun tek cümlelik aynısıyla biter. Kayıttan, panelden ya da araçtan söz etme."
                         % (len(mz), ", ".join(mz[:4]) + (" ..." if len(mz) > 4 else ""))))
    gm = gorusmesiz_musteri(kok)
    if gm:
        sorunlar.append(("Durum kaydında müşteri sayısı görüşme sayısından büyük (müşteri %d, görüşme %d): evet görüşmenin içinden geldi, "
                         "görüşme sayaca yazılmadı. `sayaclar.gorusme`'yi en az müşteri sayısına çıkar (ilk görüşmeyse `ilerleme_asamasi` en az 3) "
                         "ve aynı içeriği durum_yaz ile gönder; görüşmenin notları gün kapanmadan gorusmeyi-analiz-et ile yazılır. " % gm) + SESSIZ_BITIS)
    durum_yazildi = any(durum_kaydi_yazildi(a) or (a.get("name") or "").endswith("durum_yaz") for a in son_araclar)
    sc = siradaki_cekim_sorunlari(kok) if durum_yazildi else []
    if sc:
        sorunlar.append(("Durum kaydındaki `siradaki_cekim` sunucunun okuduğu biçimde değil (%s); gece çekimi bu haliyle hiç başlamaz. "
                         "Alanları tam bu adlarla yaz: `kategori`, `sehir`, `ilce`, `hedef`, `reklam_kelimeleri` (liste), "
                         "`istek_tarihi` (bugün, YYYY-AA-GG); başka ad kullanma. Aynı içeriği durum_yaz ile gönder. " % "; ".join(sc)) + SESSIZ_BITIS)
    eksik = teslimati_eksik_musteriler(kok)
    if eksik:
        sorunlar.append(("Durum kaydında müşteri var (%s) ama panelin Teslimat dosyası (.founderos/panel/teslimat.json) onu taşımıyor; öğrenci müşterisinin gününü panelde göremez. Şimdi founderos:panel-vitrini şemasıyla müşterinin satırını yaz (ad, baslangic: paranın geçtiği gün, rapor_gunu, aylik: anlaşılan aylık ücret, evre, siradaki; öbür müşterilerin satırlarını koru) ve aracın panel --yukle komutunu sessiz çalıştır. " % ", ".join(eksik)) + SESSIZ_BITIS)
    # Su an kartinda cevaplanmis soru kalmasin: son odak_yaz 'Senden' biraktiysa ve bu turda odak
    # gitmediyse kart eski soruyu gosterir (s2 tur 8: kurulum gunu cevaplandi, Claude "Gönderdim"
    # bekledi, kart eski soruda kaldi; istem kancasinin notuna uyulmadi). Burada bir kez yakalanir.
    if not any((a.get("name") or "").endswith("odak_yaz") for a in son_araclar):
        onceki = son_odak_bekleyen(kayitlar[:son_kullanici])
        if onceki:
            sorunlar.append(("Panelin Şu an kartında \"Senden: %s\" duruyor ve bu turda odak gitmedi. Öğrenciden şimdi başka bir şey bekliyorsan odak_yaz `bekliyor` ve yeni `bekleyen` (varsa `sonraki`); aynı şeyi bekliyorsan aynı `bekleyen` ile yeniden; beklemiyorsan `calisiyor` ya da `bitti` gönder. " % onceki[:80]) + SESSIZ_BITIS)
    if sorunlar:
        # Ogrenciye yeni mesaj yazdiran bir sorun varsa (gunun ilk mesaji, hayalet mesaj) obur sorunlarin
        # "yalniz son cumleyi yinele" sonu onunla celisir: o son cikarilir, arac yine sessiz calisir.
        if any(x.startswith("Öğrenci günü selamla açtı") or x.startswith("Öğrenci bu turda sohbette yalnız") for x in sorunlar):
            sorunlar = [x.replace(SESSIZ_BITIS, "Araçtan sonra öğrenciye kayıttan, sunucudan, panelden ya da araçtan söz etme.") for x in sorunlar]
        sys.stderr.write("FounderOS denetimi: " + " ".join(sorunlar) + "\n")
        return 2
    return 0


if __name__ == "__main__":
    try:
        kod = main()
    except Exception:
        kod = 0
    sys.exit(kod)
