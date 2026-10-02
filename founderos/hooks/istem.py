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


SELAM_NOTU = ("FounderOS: kısa selam. Günü founderos:gunaydin ile aç (çekirdek bu oturumda açık değilse önce founderos:ana-yonetici). "
              "Selama selamla karşılık verip bekleme; ilk cümle düne bağlansın.")
# "Devam" gunun ortasinda da geliyor: oturus arasi moladan donunce ve panelin Su an
# kartindan kopyalanan "Devam" (bir modul bitince sonraki cumle). Sohbette daha once
# asistan konusmussa gun yeniden acilmaz; sohbetin ilk mesajiysa selam gibi.
DEVAM_NOTU = ("FounderOS: devam. Bu sohbette süren bir iş var: kaldığın adımdan sürdür (bu sohbet ve durum kaydındaki adim); "
              "günü yeniden açma, lisansa yeniden bakma, selam verme. Panelin Şu an kartından kopyalanan 'Devam' da budur.")

KURALLAR = [
    ("selam", re.compile(r"^\s*(g[üu]nayd[ıi]n|ba[şs]layal[ıi]m|haz[ıi]r[ıi]m|bug[üu]n ne yap[ıi]yoruz|merhaba|selam)\b[\s.!?,]*$"),
     SELAM_NOTU),
    ("devam", re.compile(r"^\s*(devam( edelim| et| ediyoruz)?|kald[ıi][ğg][ıi]m yerden( devam( edelim)?)?)\b[\s.!?,]*$"),
     DEVAM_NOTU),
    ("vazgecme", re.compile(r"(b[ıi]rak[ıi]yorum|b[ıi]rakaca[ğg][ıi]m|vazge[çc]|bana g[öo]re de[ğg]il|yapamayaca[ğg][ıi]m|olmayacak bu|pes ediyorum|ni[şs] de[ğg]i[şs]tir|sekt[öo]r de[ğg]i[şs]tir|i[şs] de[ğg]i[şs]tir|ara vereyim|bu i[şs] olmuyor)"),
     "FounderOS: vazgeçme işareti olabilir. Çekirdeğin 'Vazgeçme ve ara' kuralını uygula: önce plana bak (büyük mü, belirsiz mi, bilgi eksik mi, vaktine sığıyor mu), gerekiyorsa küçült; inanç değişimi en son ve rakamla. Tarihli mola işaret değildir."),
    # Ogrencinin kendi guvencesi ve destegi (musterinin garantisi degil). Simulasyon k2: "garanti
    # var mi, param iade olur mu, destek nasil" sorusuna "bilmiyorum, satin alma kosullarinda yaziyor"
    # cevabi geldi; cekirdekteki bolum uzun sohbette akilda kalmamisti. Notta kararlar aynen durur.
    ("guvence", re.compile(r"(para(m|m[ıi]z)?[ıi]? iade|iade (var|olur|ediliyor|alabil)|ilk m[üu][şs]teri g[üu]vence|g[üu]vence(niz|n[ıi]z)? (nedir|ne\b|nas[ıi]l)|garanti(niz)? var m[ıi]|garanti(si)? (nedir|ne\b)|destek nas[ıi]l|destek var m[ıi]|deste[ğg]e nas[ıi]l)"),
     "FounderOS: öğrenci FounderOS'un kendisine verdiği güvenceyi ya da desteği soruyor (müşteriye verdiği güvence değil). Çekirdeğin 'İlk Müşteri Güvencesi' ve 'Takılma ve destek' bölümleriyle, bilmiyorum demeden, kısa ve sakin cevap ver: 90 günlük İlk Müşteri Güvencesi; şart üç eylem (verilen müşteri mesajlarını her gün göndermek: tam zamanlı 100, işin yanında 40 temas, takipler dahil; randevu alan işletmelerle görüşmeye girmek; canlı görüşme geri bildirimini uygulamak); karşılığı ilk ücretli müşteriye kadar destek, grup görüşmeleri ve CRM ücretsiz devam; para iadesi yok; 'garanti yok' ya da 'garanti değildir' gibi uyarı cümlesi kurma, yerine aynen 'Gelir değil, ilk müşteri güvencesi.' Destek: 'Destek kanalı 7/24 açık; ekip en geç 12 saat içinde döner.' Yolu WhatsApp hattı ve destek@founderos.so. Süreler: FounderOS, beceriler, şablonlar ve topluluk 12 ay; canlı grup görüşmeleri, destek kanalı ve CRM ilk 120 gün."),
    ("destek", re.compile(r"(destek [öo]zeti|deste[ğg]e yaz(al[ıi]m|aca[ğg][ıi]m)?|destekle g[öo]r[üu][şs]mek)"),
     "FounderOS: destek özeti. Takılma yöntemini baştan yürütme; çekirdekteki beş satırı (iş, denenen, takılan yer, ilgili kayıt, beklenen yardım) hemen yaz. Lisans anahtarı, şifre ve kişisel bilgi girmez. Altına iki yolu koy: WhatsApp hattı ve destek@founderos.so; öğrenci yapıştırıp gönderir."),
    # "Istanbul'da implant hizmeti veren 100 dis klinigi bul" (satis videosundaki cumle) de
    # buraya gelir: sehir eki -da/-de, arada hizmet ve sayi, sonda bul/listele.
    ("aday_bul", re.compile(r"(\w+['’]?(?:deki|daki|teki|taki)\s+[\w ]{2,40}?\s*(?:bul|listele|tara|[çc][ıi]kar)\b|\w+['’](?:da|de|ta|te)\s+[^.?!\n]{2,80}?\b(?:bul|listele|tara)\b|\b\d{2,4}\s+[\w ]{2,40}?\b(?:bul|listele)\b|(?:klini[kğg]\w*|i[şs]letme\w*|ofis\w*|servis\w*|salon\w*|merkez\w*)\s+(?:bul|listele)\b|m[üu][şs]teri adaylar[ıi]n[ıi] bul|\baday(?:lar[ıi])? bul\b)"),
     "FounderOS: aday listesi, açık istek. Günün sırası bekletmez: pazar seçiliyse founderos:aday-listesi-cikar şimdi (veri servisi, aday_ara; aday aracı yoksa önce kur); planda liste sonraki bir günse tek cümle söyle, işi yap. Pazar yoksa önce pazarı seç (founderos:nisi-sec). İstenen niş öğrencinin pazarı değilse niş kilidini tek cümleyle söyle, kendi pazarının listesini öner. Çekim başlayınca: panelde Adaylar'daki Müşteri Bulma Motoru'nda liste canlı akar. Yüz seçilince ilk on tek tablo (İşletme, Telefon, Site, Instagram, Neden bu işletme; kanal istendiyse İlk temas). Taramada olmayan bilgi (yönetici adı) boş kalır ve tek cümleyle söylenir; kaynak her satırın Google Haritalar kaydı."),
    # Satis videosundaki uzun istek "Klinik: X. Instagram: Y. ... klinige ozel demo hazirla" da buraya gelir.
    ("demo_olustur", re.compile(r"(demo olu[şs]tur|i[çc]in demo (olu[şs]tur|haz[ıi]rla|yap)|(?:adaya|klini[ğg]e|i[şs]letmeye|ofise|salona) [öo]zel demo|[öo]zel (bir )?demo (haz[ıi]rla|olu[şs]tur|yap)|demo ba[ğg]lant[ıi]s[ıi] (ver|olu[şs]tur|haz[ıi]rla))"),
     "FounderOS: adaya özel demo, açık istek. Günün sırası bekletmez: veri servisinin demo_olustur aracını şimdi, işletmenin adı ve varsa Instagram'ıyla çağır (önce eksik bilgi sorma, bağlantı önce gelir); bağlantıyı ve dürüstlük cümlesini ver. Demo Instagram sayfasını okumaz: 'sayfadaki bilgileri aldım' deme; kliniğin adıyla açıldığını, saatler taramada yoksa örnek olduğunu söyle. Demo telefonla başlayan akışı gösterir; öğrenci reklam formu ya da eski müşteri listesinin aynı kayda toplandığını da istediyse onu panelde Ajansım'daki hizmet akışı şeması gösterir, demoda varmış gibi anlatma (istemediyse bu konu açılmaz). 'Eksik bilgileri sor' dense de saat ve semt sorma: demo onları alamaz, işletme aday listesine girince kendiliğinden gelir; mesaj soruyla değil, demoyu nasıl deneyeceğiyle biter (Mesajla dene, Sesli dene, İşletmenin ekranı). İlk mesajda bağlantı gitmez, aday izin verince gider. Öğrenci kendisi bakacaksa cevaptaki onizleme adresini ver (alan yoksa adresin sonuna ?onizleme=1); adaya yalnız çıplak adres gider. Araç hata verirse panelde Adaylar'daki Tek Tıkla Demo."),
    ("demo_acti", re.compile(r"(demo(yu|mu|yi)? a[çc]t[ıi] m[ıi]|demo(yu|mu)? a[çc]m[ıi][şs] m[ıi]|demoya bakt[ıi] m[ıi]|\bdemolar[ıi]m\b)"),
     "FounderOS: demonun durumu. demolar aracıyla bak: açtıysa takip demoya bağlanır (randevu kısmını denedi mi), açmadıysa izinden sonraki demo videosu (founderos:video-mesaj-cek). Öğrenci demoya kendisi bakacaksa satırdaki onizleme adresini verirsin; çıplak adresi açarsa adayın açtığı sayılır."),
    ("kurulum_studyo", re.compile(r"^\s*(kurulum bilgileri|test sonu[çc]lar[ıi]|canl[ıi]ya al)\b"),
     "FounderOS: panelin Kurulum stüdyosundan. founderos:musteri-sistemini-kur: kurulum bilgilerini müşterinin bilgi dosyasına yaz, eksikleri tek listede iste; test sonuçlarında kalan her madde için düzeltmeyi adım adım ver; canlıya almadan teslim kontrolünün beş şartına bak. Fiyat kuralı sabit; sesli tarafın kurulum adımı yazılmaz."),
    ("hata_incele", re.compile(r"^\s*hata incele"),
     "FounderOS: asistanın yanlış cevabı. founderos:sistemi-kontrol-et'in hata incelemesi: nedeni ayır (bilgi, kural, akış), düzeltmeyi Türkçe adım adım yaz, aynı soruyla yeniden test ettir. Sesli taraftaysa adım yazma, destek satırını ver."),
    ("pano", re.compile(r"(\bile temas kurdum|\bcevap verdi\s*:|\bile g[öo]r[üu][şs]t[üu]m\b|\bile g[öo]r[üu][şs]me ayarlad[ıi]m|m[üu][şs]teri oldu)"),
     "FounderOS: aday panosundan aşama bildirimi. Aday aracıyla adayın aşamasını ve son temasını yaz. Cevap verdiyse cevabını satırına yaz, sıradaki cümleyi founderos:adaya-mesaj-yaz ile hazırla; görüşme ayarladıysa aşama randevu ve randevu tarihi (temas --randevu), sayaçtaki randevu ve durum_yaz (founderos:gorusmeye-getir); görüştüyse founderos:gorusmeyi-analiz-et; müşteri olduysa founderos:onay-belgesini-hazirla, sonra founderos:musteriyi-karsila."),
    ("takilma", re.compile(r"(anlamad[ıi]m|yapamad[ıi]m|tak[ıi]ld[ıi]m|olmad[ıi]|[çc]al[ıi][şs]m[ıi]yor|hata veriyor|bende bu ekran yok|bulam[ıi]yorum|g[öo]remiyorum|nereye bas)"),
     "FounderOS: takılma. Takılma yöntemini uygula: nerede kaldı, türü ne (bilgi, erişim, teknik, uygulama), işi küçült; aynı açıklamayı tekrarlama; iki denemede çözülmezse destek özeti."),
    ("cevap_yok", re.compile(r"(kimse cevap vermedi|cevap gelmiyor|hi[çc] d[öo]n[üu][şs] yok|kimse a[çc]m[ıi]yor|kimse d[öo]nmedi)"),
     "FounderOS: founderos:cevap-gelmiyor modülünü aç. Motivasyon konuşması yok, beş kontrol ve tek gerekçeli değişiklik."),
    ("randevu", re.compile(r"(randevu ald[ıi]m|yar[ıi]n g[öo]r[üu][şs]me|g[öo]r[üu][şs]me ayarlad[ıi]m|randevu verdi|g[öo]r[üu][şs]mem var(?!d)|g[öo]r[üu][şs]meye haz[ıi]rlan)"),
     "FounderOS: randevu. founderos:gorusmeye-getir (açılışta odak_yaz basladi), ardından founderos:gorusme-provasi-yap. Randevu hangi kanaldan gelirse gelsin aday listesine (temas --randevu) ve sayaca yazılır; saha ekranında Randevu'ya basılmadıysa sayaç şimdi artar ve durum_yaz gider."),
    ("gorusme_bitti", re.compile(r"(g[öo]r[üu][şs]me bitti|g[öo]r[üu][şs]t[üu]k|g[öo]r[üu][şs]meyi yapt[ıi]m|[şs][öo]yle ge[çc]ti)"),
     "FounderOS: görüşme bitti. founderos:gorusmeyi-analiz-et."),
    ("evet", re.compile(r"(evet dedi|kabul etti|paray[ıi] g[öo]nderecek|[öo]deme yapacak|anla[şs]t[ıi]k)"),
     "FounderOS: evet geldi. founderos:onay-belgesini-hazirla, sonra founderos:musteriyi-karsila. Erken evet bekletilmez."),
    ("resmi", re.compile(r"(kvkk|\biys\b|yasal m[ıi]|yasal olarak|kanun|s[öo]zle[şs]me|vergi|fatura|[şs]irket (kur|a[çc])|mali m[üu][şs]avir|muhasebeci|avukat|hukuk|ceza|izin (laz[ıi]m|gerek)|ruhsat|ba[ğg]-?kur)"),
     "FounderOS: öğrenci resmi bir konu açtı. Kısa, sakin, yapılacak işle cevap ver; kanun, madde, ceza, hukukçu anlatma ve öğrencinin kullandığı resmi kelimeleri (izin sistemi, kanun, avukat, ceza, vergi levhası) tekrar etme (çekirdekte 'Korkutan dil yok'). Şirket ilk 'evet'te açılır, sözleşme hazır gelir; teslimindeki tek not 'İmzadan önce kendi avukatına okut.' cümlesidir. Bilmediğin resmi soruda destek satırını hazır ver."),
    ("aksam", re.compile(r"^\s*(ak[şs]am|g[üu]n[üu] kapatal[ıi]m|bug[üu]nl[üu]k bu kadar|kapan[ıi][şs] yapal[ıi]m)\b[\s.!?,]*$"),
     "FounderOS: akşam kapanışı. founderos:rakamlari-oku; saha açıksa önce aday aracının kapat komutu (kapanmamış günler), kapanışın tarihi onun ilk satırındaki iş günü."),
    # "video metni" tek basina icerik degil: "Karaca Klima icin video metni" adaya giden
    # video mesajdir (video-mesaj-cek). Yalniz haftanin uzun videosu icerige gider.
    ("icerik", re.compile(r"(i[çc]erik haz[ıi]rla|(bu )?haftan[ıi]n i[çc]eri[ğg]i|(youtube|uzun) video(su)?(nun)? metni|ne payla[şs]ay[ıi]m|\breels\b|kayd[ıi]rmal[ıi] g[öo]nderi|carousel|linked[iı]n g[öo]nderi|videoyu ([çc]ektim|y[üu]kledim)|^\s*payla[şs]t[ıi]m\b)"),
     "FounderOS: haftanın içeriği. founderos:icerik-motoru. Müşteri bulma başlamadıysa içerik başlamadı; tek cümle ve güne dön."),
    ("panel", re.compile(r"(paneli g[üu]ncelle|panelim bo[şs]|panelde g[öo]r[üu]nm[üu]yor|panelde (teklifim|markam|adaylar[ıi]m|mesajlar[ıi]m|pazar[ıi]m|fiyat[ıi]m) yok)"),
     "FounderOS: panel. founderos:panel-vitrini: eksik dosyayı kayıttan yaz, aday aracının panel --yukle komutunu sessiz çalıştır, sonra odak_yaz bitti (is: doldurduğun bölümün modülü, panel-vitrini değil); tek cümle söyle."),
    ("tur", re.compile(r"(\btur(u|unu)? (g[öo]ster|a[çc]|tekrarla|ba[şs]lat)|panel turu|panel(i)? nas[ıi]l kullan|panel nas[ıi]l [çc]al[ıi][şs][ıi]r|panel(de)? neler? var|paneli tan[ıi]t)"),
     "FounderOS: panel turu. odak_yaz'ı tur: true ile gönder (is: durum kaydındaki açık modül, yoksa gunaydin). Panel yanda açık değilse önce İş Beyni'ndeki panel linkiyle [Panelini aç](link). Çekirdekteki iki tur cümlesi: Şu an kartı, kopyalanıp buraya yapıştırılan cümle, sekmeler. Durum kaydına panel_turu yaz."),
    # Satis videosundaki istekler (ogrenci videodaki cumleyi aynen yazar). Gun sirasi bekletmez (cekirdek,
    # "Acikca istenen is sira beklemez").
    ("nis_karsilastir", re.compile(r"kar[şs][ıi]la[şs]t[ıi]r\w*[^.?!\n]{0,200}?(ni[şs]|sekt[öo]r|klini[kğ]|ofis|merkez|salon|servis)|(ni[şs]|sekt[öo]r|klini[kğ]\w*|ofis\w*|merkez\w*)[^.?!\n]{0,160}?kar[şs][ıi]la[şs]t[ıi]r"),
     "FounderOS: nişleri karşılaştırma, açık istek. Tabloyu bu turda ver: öğrencinin ölçütleri, rakamlar karttan (founderos:nis-kartlari ve nişlerin kartları), kesin olmayan 'tahmin' işaretli; her sektör için tek problem ve üç soru; sonunda tek öneri. Şehir belliyse karşılaştırılan nişlerin canlı sayımı bu turda başlar (aday_ara sayim: true, kartın reklam kelimeleriyle; founderos:veri-servisi), iş kimlikleri İş Beyni'ne ve panelin pazar alanına (pazar.sehir, pazar.adaylar: nişler ve is_id), panel --yukle, odak_yaz (is: nisi-sec); Pazar Radarı bu nişleri canlı sayar. Pazar onaylanınca sayım yeniden başlatılmaz, yedekler karşılaştırılan nişlerdir. Pazar zaten seçilmişse kilit tek cümle, tablo yine verilir."),
    ("pazar_onay", re.compile(r"^(?=.{0,140}$).*((bu )?pazarla ba[şs]l[ıi]yoruz|\w+(?:la|le|yla|yle)\s+(ba[şs]l[ıi]yoruz|ba[şs]layal[ıi]m|devam (ediyorum|edelim|ediyoruz|edece[ğg]im)))"),
     "FounderOS: pazar onayı olabilir. Onay pazara geldiyse founderos:nisi-sec'in onay adımı ve kurulumun 10a sırası. Canlı sayım: seçilen niş ve bu sohbette karşılaştırılan nişler (karşılaştırma yoksa kartın iki yedeği); sayım karşılaştırmada başladıysa iş kimlikleri İş Beyni'nde, yeniden başlatılmaz, pazar satırlarındaki karar alanı güncellenir."),
    ("teklif_iste", re.compile(r"(teklif[ıi]?\s+(haz[ıi]rla|yaz|olu[şs]tur|[çc][ıi]kar)|hizmet teklifi|teklifimi (yaz|haz[ıi]rla)|iki c[üu]mlelik teklif)"),
     "FounderOS: teklif, açık istek. Pazar seçiliyse founderos:teklifi-yaz bu turda; günün sırası (ideal müşteri, konumlandırma) teklifi bekletmez, onlar tekliften sonra tamamlanır. Öğrencinin verdiği sistem adı, akışlar ve süre aynen kullanılır; istenen biçim önce (iki cümle teklif, sonra dahil işler listesi); hasta, müşteri ya da gelir sayısı garantisi yok; eksik bilgi sorusu en sonda, tek soru. Panele: donusum, sistem_adi, mekanizma, teklif, deger_bolgesi, ajanlar (founderos:panel-vitrini), panel --yukle, odak_yaz (is: teklifi-yaz). Pazar yoksa önce pazar. Birinci gün sürüyorsa iş bitince atlanan adıma dönülür (ideal müşteri, konumlandırma, teslimat kontrolü); durum kaydının adim ve sonraki_adim alanı ile mesajın son cümlesi onu söyler, marka ve sayfaya atlanmaz."),
    ("fiyat_rakam", re.compile(r"(fiyat\w*[^.?!\n]{0,60}?(\d{2,3}[.\s]?000|\d{2,3} ?bin|k[ıi]rk bin|elli bin|altm[ıi][şs] bin|on (iki|be[şs]) bin)|(kurulum|ayl[ıi]k)[^.?!\n]{0,30}?(\d{2,3}[.\s]?000|\d{2,3} ?bin|k[ıi]rk bin|on (iki|be[şs]) bin))"),
     "FounderOS: fiyat, öğrenci rakamı kendisi verdi. Günün sırası bekletmez: teklif yazılıysa founderos:fiyati-belirle bu turda; rakam bandın içindeyse (kurulum 40.000-60.000, aylık 10.000-15.000) fiyat olarak yazılır (40.000 + 12.500 Kademe 2'nin rakamı), dışındaysa farkı tek cümle, karar onun. İstenen hesap rakamla: [sayı] × kurulum, [sayı] × aylık, ikisinin toplamı; giderler öncesi olduğu söylenir; sayı sözü yok. Mesaj istenen hesapla sınırlı: fayda kontrolü sorulmadıysa tek cümle (ayda kaç müşteri kurtarması aylığı çıkarıyor), ayrıntısı Teklif stüdyosunda. Birinci gün sürüyorsa iş bitince atlanan adıma dönülür (ideal müşteri, konumlandırma, teslimat kontrolü, vizyonun hesabı); marka ve sayfaya atlanmaz. İş Beyni'ne fiyat, panele fiyat ve teklif.hesap (founderos:panel-vitrini), panel --yukle, odak_yaz (is: fiyati-belirle); panelde Teklif stüdyosu ve Kâr hesabı."),
    ("ilk_mesaj", re.compile(r"(ilk mesaj\w*\s+(haz[ıi]rla|yaz|olu[şs]tur)|truva at[ıi])"),
     "FounderOS: bir işletmeye ilk mesaj, açık istek. Günün sırası bekletmez: founderos:adaya-mesaj-yaz bu turda, sohbette son konuşulan işletmeyle (ad yoksa ve sohbette işletme geçmediyse listenin ilk satırı; hangisi olduğunu ilk cümlede söyle). İşletmenin satırı aday listesinde ve hızlı denetimi yoksa önce yalnız o işletmenin hızlı denetimi (satırın ipuçları, yorum alıntısı, reklam sütunu, saatler). Gözlem yalnız kayıtta görülen şeydir; yapılmamış arama anlatılmaz, kayıp uydurulmaz, ilk mesajda bağlantı yok, tek soru. Bulgu, kanca ve metin adayın satırına aday aracıyla yazılır (guncelle ... yuz=evet bulgu=... kanca=... dm_metni=... ya da eposta_metni=...), sonra panel --yukle; Mesajlar'daki Truva mesaj stüdyosu ve Adaylar'daki kartı oradan dolar. odak_yaz (is: adaya-mesaj-yaz)."),
    ("pazar_arastir", re.compile(r"(pazar ara[şs]t[ıi]rmas[ıi]|ni[şs] ara[şs]t[ıi]rmas[ıi]|ni[şs] raporu|kaynakl[ıi] ara[şs]t[ıi]r|hangi sekt[öo]re satar[ıi]m)"),
     "FounderOS: kaynaklı pazar araştırması. founderos:nis-arastirmasi; nişi seçmez, kilidi açmaz. Başta odak_yaz (is: nis-arastirmasi, basladi); panelde Pazar Radarı açılır. Pazar seçilmediyse ve şehir belliyse ilk üçün sayım çekimi başlar başlamaz is_id'leriyle pazar.adaylar'a yaz, panel --yukle, odak_yaz calisiyor."),
    ("pazar_sec", re.compile(r"(ni[şs]imi se[çc]|pazar[ıi]m[ıi] se[çc]|ni[şs] se[çc]elim|pazar se[çc]elim|hangi (ni[şs]e|pazara|sekt[öo]re) (gireyim|girsem|ba[şs]layay[ıi]m|ba[şs]lasam))(?!.*kaynak)"),
     "FounderOS: pazar kararı. founderos:nisi-sec; pazar seçilmiş ve kilitliyse kilidi tek cümleyle söyle, Pazar Radarı'ndaki sayımı göster. Başta odak_yaz (is: nisi-sec, basladi); panelde Ajansım'ın Pazar Radarı açılır. Onaydan sonra sayım çekimlerinin is_id'lerini hemen pazar.adaylar'a yaz (karar dahil), panel --yukle, sonra odak_yaz."),
    ("sayim", re.compile(r"(say[ıi]m(lar)?[ıi]? (ne oldu|bitti mi|haz[ıi]r m[ıi]|nerede)|canl[ıi] say[ıi]m|pazar radar[ıi])"),
     "FounderOS: canlı sayım. İş kimlikleri İş Beyni'nin yedinci bölümünde; aday_sonuc ile sor, aday_ara'yı yeniden çağırma. Hazırsa ölçüleri, puanı ve kararı pazar.adaylar'a yaz (founderos:panel-vitrini), panel --yukle, odak_yaz (is: nisi-dogrula, bitti)."),
    ("fiyat_hesap", re.compile(r"(fiyat[ıi]m[ıi] (hesapla|belirle|koy|kesinle[şs]tir|[çc][ıi]kar)|fiyat[ıi]m ne olmal[ıi]|fiyat band[ıi]m[ıi] (hesapla|[çc][ıi]kar))"),
     "FounderOS: fiyat hesabı. founderos:fiyati-belirle (birinci günse bant, aday listesinin çıktığı gün kesin fiyat; sırası gelmediyse tek cümle). teklif.hesap'ı gerçek kayıttan yaz (bilinmeyen alan yazılmaz), panel --yukle, odak_yaz (is: fiyati-belirle); panelde Teklif stüdyosu açılır."),
    ("kar_hesap", re.compile(r"(k[âa]r[ıi]m[ıi] hesapla|k[âa]r hesab[ıi]|cebime ne kal[ıi]yor|ne kadar k[âa]r (ediyorum|ederim|kal[ıi]yor))"),
     "FounderOS: kâr hesabı. founderos:kari-hesapla (müşteri yoksa yalnız gider tarafı). teklif.hesap'ın arac_maliyeti ve sabit_maliyet alanlarını gerçek rakamla güncelle, panel --yukle, odak_yaz (is: kari-hesapla); panelde Teklif stüdyosu açılır."),
    ("deste", re.compile(r"(^\s*[şs]u i[şs]letmeye mesaj yaz|i[çc]in mesaj yaz\s*$|i[çc]in ba[şs]ka bir a[çc][ıi]l[ıi][şs] yaz|video senaryosu yaz|^\s*prova yapal[ıi]m|teklifimi g[öo]ster|markam[ıi] g[öo]ster|^\s*sitemi a[çc]|yeni aday listesi [çc]ek|adaylar[ıi] denetle|m[üu][şs]terimi kar[şs][ıi]layal[ıi]m|bu haftay[ıi] de[ğg]erlendirelim|demomu haz[ıi]rla|grup g[öo]r[üu][şs]mesine haz[ıi]rlan)"),
     "FounderOS: panelin beceri destesinden gelen cümle. Çekirdeğin tek kapı listesindeki eşlemeyle modülü aç; sırası gelmemişse tek cümleyle ne zaman açılacağını söyle."),
    ("crm", re.compile(r"(crm hesab[ıi]m a[çc][ıi]ld[ıi]|giri[şs] bilgilerim geldi|ba[şs]lang[ıi][çc] g[öo]r[üu][şs]mesini yapt[ıi]k)"),
     "FounderOS: CRM açıldı. Günün ilk işi founderos:araclari-kur'un 'CRM açıldığı gün' adımı, ardından founderos:musteri-takip-sistemini-kur."),
]


# Video isteklerinin desenleri genis; yanlis eslesmeyi bu ek sartlar eler.
NIS_KELIMESI = re.compile(r"klini[kğ]|merkez|ofis|salon|servis|st[üu]dyo|acente|galeri|firma")
FIYAT_EYLEM = re.compile(r"\b(koy|yaz|belirle|ayarla|olsun|yap)\w*\b")
FIYAT_ITIRAZ = re.compile(r"pahal[ıi]|dedi\b|itiraz|indirim|sordu")


def ek_sart(ad, k):
    if ad == "nis_karsilastir":
        return bool(re.search(r"ni[şs]|sekt[öo]r|pazar", k)) or len(NIS_KELIMESI.findall(k)) >= 2
    if ad == "fiyat_rakam":
        return bool(FIYAT_EYLEM.search(k)) and not FIYAT_ITIRAZ.search(k)
    if ad == "ilk_mesaj":
        return "ilk mesaj" in k or bool(re.search(r"mesaj|haz[ıi]rla|yaz\b", k))
    return True


def sohbet_suruyor(yol):
    """Bu sohbette asistan daha once konustu mu. Kayit okunamazsa False (ilk mesaj sayilir).
    Ilk asistan satirinda durur; butun kaydi okumaz."""
    if not isinstance(yol, str) or not yol:
        return False
    try:
        with open(yol, encoding="utf-8", errors="ignore") as f:
            for satir in f:
                if '"assistant"' not in satir:
                    continue
                try:
                    if json.loads(satir).get("type") == "assistant":
                        return True
                except Exception:
                    continue
    except Exception:
        return False
    return False


def son_senden(yol):
    """Kayittaki son odak_yaz girdisi panelin Su an kartinda 'Senden' satiri birakti mi (bekleyen).
    Biraktiysa ogrencinin yeni mesaji cogu zaman onun cevabidir; o tur odak guncellenmezse kart
    cevaplanmis soruda kalir (simulasyon k2: tanisma sorularinda kart eski soruyu gosterdi)."""
    if not isinstance(yol, str) or not yol:
        return None
    son = None
    try:
        with open(yol, encoding="utf-8", errors="ignore") as f:
            for satir in f:
                if "odak_yaz" not in satir or '"assistant"' not in satir:
                    continue
                try:
                    k = json.loads(satir)
                except Exception:
                    continue
                if k.get("type") != "assistant":
                    continue
                for p in (k.get("message") or {}).get("content") or []:
                    if isinstance(p, dict) and p.get("type") == "tool_use" and str(p.get("name") or "").endswith("odak_yaz"):
                        if isinstance(p.get("input"), dict):
                            son = p["input"]
    except Exception:
        return None
    if not son:
        return None
    b = str(son.get("bekleyen") or "").strip()
    if b and son.get("durum") in ("bekliyor", "basladi", "calisiyor"):
        return b[:120]
    return None


def hatali_kayit_araclari(yol):
    """odak_yaz, durum_yaz ve panel_yaz'in kayittaki son cagrisi hata dondurduyse adlari. Baglanti
    koptugunda (sunucu yeniden basladi, ECONNREFUSED) panel eski iste kalir; cekirdek bir sonraki
    turda yeniden gondermeyi istiyor ama simulasyonda (k2) gonderilmedi."""
    if not isinstance(yol, str) or not yol:
        return []
    son = {}
    try:
        with open(yol, encoding="utf-8", errors="ignore") as f:
            for satir in f:
                if "_yaz" not in satir and '"is_error"' not in satir and "panel --yukle" not in satir:
                    continue
                try:
                    k = json.loads(satir)
                except Exception:
                    continue
                icerik = (k.get("message") or {}).get("content")
                for p in icerik if isinstance(icerik, list) else []:
                    if not isinstance(p, dict):
                        continue
                    if p.get("type") == "tool_use":
                        ad = str(p.get("name") or "")
                        for arac in ("odak_yaz", "durum_yaz", "panel_yaz"):
                            if ad.endswith(arac):
                                son[arac] = [p.get("id"), False]
                        # Aday aracinin panel --yukle komutu da paneli gonderir.
                        if ad == "Bash" and "panel --yukle" in str((p.get("input") or {}).get("command") or ""):
                            son["panel_yaz"] = [p.get("id"), False]
                    elif p.get("type") == "tool_result" and p.get("is_error"):
                        for arac, v in son.items():
                            if v[0] and v[0] == p.get("tool_use_id"):
                                v[1] = True
    except Exception:
        return []
    return [arac for arac in ("odak_yaz", "durum_yaz", "panel_yaz") if son.get(arac, [None, False])[1]]


HATA_NOTU = ("FounderOS: son %s çağrısı hata döndürdü (bağlantı koptu); panel eski hâlinde duruyor. Bu turda "
             "işin şimdiki hâliyle yeniden gönder (panel_yaz için aracın panel --yukle komutu); öğrenciye bundan söz edilmez.")


SENDEN_NOTU = ("FounderOS: panelin Şu an kartında \"Senden: %s\" duruyor. Bu mesaj onun cevabıysa kart eski "
               "soruda kalmaz: bu turda yeni soru soracaksan soruyu yazmadan önce odak_yaz `bekliyor` ve yeni "
               "`bekleyen`, soru yoksa `calisiyor` (bekleyensiz) gider; öğrenciye bundan söz edilmez.")


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
    eslesen = set()
    for ad, desen, notu in KURALLAR:
        if ad in ("selam", "devam", "aksam") and len(k) > 60:
            continue
        if ad == "devam" and desen.search(k):
            notlar.append(DEVAM_NOTU if sohbet_suruyor(g.get("transcript_path")) else SELAM_NOTU)
            eslesen.add(ad)
            continue
        # Destek ozeti istendiyse takilma yontemi bastan yurutulmez (cekirdek).
        if ad == "takilma" and ("destek" in eslesen or "hata_incele" in eslesen or "kurulum_studyo" in eslesen):
            continue
        # Kaynakli arastirma istendiyse pazar karari ayrica acilmaz (nis-arastirmasi nisi secmez).
        if ad == "pazar_sec" and "pazar_arastir" in eslesen:
            continue
        if desen.search(k) and ek_sart(ad, k):
            notlar.append(notu)
            eslesen.add(ad)
    notlar = notlar[:2]
    hatali = hatali_kayit_araclari(g.get("transcript_path"))
    senden = None if "odak_yaz" in hatali else son_senden(g.get("transcript_path"))
    if hatali:
        notlar.append(HATA_NOTU % ", ".join(hatali))
    if senden:
        notlar.append(SENDEN_NOTU % senden)
    if notlar:
        sys.stdout.write("\n".join(notlar) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
