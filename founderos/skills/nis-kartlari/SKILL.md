---
user-invocable: false
name: nis-kartlari
description: "On dokuz nis kartinin listesi, kart kurallari ve kart sablonu. Nis secilirken ve hangi kart modulunun acilacagi belirsizken acilir."
---

# FounderOS Niş Kartları (taslak 2, 5 Eylül 2026)

Kartlar plugin'in skill'lerinin okuduğu bilgi dosyalarıdır. Kural: uydurma yok, her rakam kaynaklı, bilinmeyen "sahadan dolacak" diye yazılır. Şablon en sonda.

Durum: 19 kartın 19'u şablona göre yazıldı (kart başına 5 ile 47 kaynak; oto kuaför kartı şablona sonradan tamamlandı, dil ve mesleki eğitim kursları kartı en son eklendi). Bilinen açıklar: Meta Reklam Kütüphanesi hiçbir kartta görülemedi (canlı taramayla dolacak); diş kliniğinde TDB ve Resmi Gazete tam metni robot engeline takıldı, hukukçu teyidi şart.

## İçindekiler

- Oto kuaför, seramik kaplama, araç kaplama (masa puanı 8/10, 5 açık)
- Güzellik salonu ve güzellik merkezi (masa puanı 9/10, 5 açık)
- Klima ve kombi servisi (masa puanı 8/10, 15 açık)
- Temizlik şirketi (masa puanı 9/10, 19 açık)
- Oto servis ve cam filmi (masa puanı 10/10, 7 açık)
- Cam balkon, PVC pencere, panjur (masa puanı 9/10, 12 açık)
- Mutfak-banyo tadilat ve iç mimarlık (masa puanı 10/10, 10 açık)
- Emlak ofisi (masa puanı 7/10, 13 açık)
- Düğün organizasyon ve mekan (masa puanı 9/10, 16 açık)
- Randevulu kuaför ve berber (masa puanı 8/10, 17 açık)
- Haşere ilaçlama (masa puanı 8/10, 16 açık)
- Oto galeri (masa puanı 9/10, 13 açık)
- Sigorta acentesi (masa puanı 9/10, 9 açık)
- Elektrik ve teknik bakım (masa puanı 8/10, 6 açık)
- Fotoğraf stüdyosu (masa puanı 8/10, 14 açık)
- Diş kliniği (masa puanı 9/10, 14 açık)
- Pilates, PT ve butik stüdyo (masa puanı 9/10, 11 açık)
- Estetik cerrahi ve medikal estetik (masa puanı 9/10, 16 açık)
- Yetişkinlere yönelik dil ve mesleki eğitim kursları (masa puanı 9/10, 7 açık)

Masa puanı, kartın telefonda ve teklifte kullanılan on parçasının dolu olup olmadığını sayar: müşteri yolculuğu, kayıp birimi, fiyatlar, sızıntı kanıtı, sözlüğü, karar verici, en güçlü üç itiraz, telefon satırlarının dördü, en az beş telefon itirazı, yasal sınırların teyitli olması. Açık sayısı kartta kaç yerde "sahadan dolacak" ya da "bilinmiyor" yazdığıdır. İkisini `founderos-plugin/araclar/kart-puani.py` hesaplar; kart değişince `--yaz` ile bu satırlar yenilenir. nisi-sec bu iki sayıyı okur: masa puanı sekizin altındaki kart ilk müşteri çıkana kadar önerilmez. Sahada ne olduğu burada durmaz, sunucudaki kart ekranında durur.

---

# Şablon

# FounderOS Niş Kartı: Şablon ve Kurallar

Kart, FounderOS plugin'inin skill'lerinin okuduğu bilgi dosyasıdır. Öğrenci (Türkiye'de sıfırdan tek kişilik yapay zeka servis işi kuran, hiç müşterisi olmamış biri) nişini seçtiğinde bu kart açılır ve sistemin tamamı bu dille konuşur.

Sattığımız şey sabit: yerel işletmelerin KAÇIRDIĞI TALEBİ randevuya/işe çeviren sistem. Dört sızıntı: açılmayan telefon, geç dönülen DM/WhatsApp, dönülmeyen form, bir daha gelmeyen eski müşteri (veya teklif alıp kaybolan / randevu alıp gelmeyen). Reklamı biz vermiyoruz, reklamın karşılığını alıyoruz. Kademe 1: yazılı asistan + cevapsız aramaya anında mesaj + randevu ve hatırlatma. Kademe 2: + kaybolanları geri getirme + Google yorumu toplama + aylık rapor. Kademe 3: + reklam yönetimi.

## MUTLAK KURALLAR
1. Uydurma bilgi YOK. Her rakam, her fiyat, her alıntı kaynaklı (URL). Kaynağı olmayan bir şey karta girmez.
2. Bulamadığın şeyi "bilinmiyor, sahadan dolacak" diye yaz. Boş bırakmak uydurmaktan iyidir.
3. İşletmecinin KENDİ KELİMELERİ önemli. Forum, Ekşi, Şikayetvar, YouTube yorumu, haber alıntısı; tırnak içinde, kaynaklı.
4. "Telefona çıkmıyorlar" gibi varsayımları yazma; ancak yorumlarda/şikayetlerde kanıtı varsa yaz ve kanıtı göster.
5. Fiyatlar TL, güncel (2025-2026), kaynak sitesi belirtilerek. Fiyat yayınlanmıyorsa "sektör fiyat yayınlamıyor" diye yaz, bu da bulgudur.
6. Dil: sade Türkçe, kısa cümle, em dash yok, jargon yok. Öğrenci bunu telefonda söyleyecek.

## KART BÖLÜMLERİ (sıra ve başlıklar sabit)

# [Niş adı]

**Kapsam.** Hangi işletmeler dahil, hangileri değil. Google Haritalar'da nasıl geçiyorlar (kategori adları).

Bölümün son satırı sabit: `Müşteri yolculuğu: randevu | teklif | ikisi birlikte (kısa gerekçe).` Teslimat ve rapor bu satırı okur; boş bırakılmaz.

**Gerçek fiyatlar ve kapasite.** Ana hizmetlerin yayınlanmış fiyat aralıkları (kaynaklı). Günde/haftada kaç iş çıkarabildikleri (forum, röportaj, sektör yazısı). Bundan çıkan "kaçan tek bir müşteri = ne demek" hesabı, işletmecinin diliyle ("bir boş gün", "bir koltuk saati", "bir keşif").

Bölümün son satırı sabit: `Kayıp birimi: [tutar] ([işletmecinin dilindeki karşılığı]).` Rakam kartın kendi fiyat ve kapasite sayılarından çıkar; çıkmıyorsa "sahadan dolacak" yazılır, uydurulmaz.

**Sızıntı nerede.** Bu sektörde talebin gerçekten nerede kaybolduğuna dair KANIT: müşteri yorumları ("aradım açmadılar", "mesajıma üç gün sonra döndüler"), şikayet siteleri, sektör yazıları. En fazla üç sızıntı, en güçlüsü önce. Kanıt yoksa "yorumlarda iletişim şikayeti baskın değil, baskın tema şu" diye yaz; bu da kritik bulgu.

**Sezon.** Yılın hangi ayları yoğun, hangi ayları ölü; kaynağıyla. Bilgi yoksa "Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor." yazılır. Sistem nişi seçerken buraya bakıyor; yılın dört ayından fazlası ölü geçen niş ilk müşteri için eleniyor.

**Rekabetin şekli.** Türkiye'de kaç işletme (kaynak: Haritalar sayımı, meslek odası, teklif pazaryeri istatistiği, sektör raporu). Reklam veriyorlar mı (Meta Reklam Kütüphanesi'nde ne görüldü, ya da görülemedi). Zincir/franchise var mı.

**Kim karar veriyor.** Sahibi mi, müdür mü, ortak mı; telefonu kim açıyor.

**İşletmecinin gerçek dertleri.** Kendi ağzından, kaynaklı alıntılarla. Onun sözlüğü: hangi kelimeleri kullanıyor ("boş gün", "ucuzcu", "eleman", "no-show"…). Bizim "kaçan talep" kelimemizin onun dilindeki karşılığı.

Bölümün son iki satırı sabit: `Sözlüğü: [6-10 kelime ve deyim, virgülle]` ve `İç sesi: "[tek cümle, işletmecinin kendi kendine söylediği ama kimseye söylemediği cümle]"`.

**Açılış cümlesi.** Tek bir cümle, en güçlü açıdan. İtiraz üretmeyen, işletmecinin zaten yapması gerektiğini bildiği bir şeyi söyleyen cümle. Neden bu açı, bir cümle gerekçe.

**Duran havuz.** Bu sektörde geri çağrılabilecek eski müşteri tipleri, en güçlüsü önce; her biri için meşru uyandırma sebebi (bakım zamanı, sezon, garanti, kontrol, yenileme). Listenin işletmede nerede durduğu (telefon rehberi, WhatsApp, randevu defteri, fiş).

**Asistan kuralları.** Yazılı/sesli asistanın bu sektörde ne söyleyeceği, ne SÖYLEMEYECEĞİ (fiyat verir mi, hangi bilgileri toplar, hangi konuda sahibine devreder). Ton (yorumlarda övgü ve şikayet neye odaklanıyor).

**Kanal ve zaman.** İşletmeciye nereden ulaşılır (telefon/Instagram/e-posta açıklığı; kanıt), günün hangi saati müsait, hangi saat kesinlikle değil. Adayın kendi talep kanalı hangisi (form, IG DM, WhatsApp, telefon): demo için talep nereye bırakılır.

**Reklam kütüphanesi kelimeleri.** Meta Reklam Kütüphanesi'nde aranacak 8-15 Türkçe anahtar kelime (hizmet adları, kampanya kelimeleri, yan hizmetler).

**İş ilanı kelimeleri.** İş ilanı sitelerinde ve Instagram'da aranacak, bu nişte telefonu ve randevuyu yöneten kişinin ilan adı ("resepsiyonist", "hasta kabul", "ön büro", "müşteri temsilcisi", "randevu asistanı" gibi), şehir adıyla. Kartta bu satır yoksa varsayılan altı kelime kullanılır: resepsiyonist, sekreter, çağrı karşılama, müşteri temsilcisi, randevu asistanı, ön büro.

**Yasal sınırlar.** Reklam, tanıtım, mesaj (İYS), sağlık, KVKK açısından bu nişe özel kısıt var mı; kaynaklı. Yoksa "yok".

**Yoğun şehirler.** Kaynaklı.

**Gerçek itirazlar ve karşılıkları.** 5-7 itiraz; her biri işletmecinin ağzından, karşılık sektör verisiyle. Bölümün ilk satırı sabit: `En güçlü üç itiraz: [üç kısa ad, virgülle]`. Sistem üç itiraz videosunu bu üçünden çekiyor.

**Telefonda söylenecekler.** Öğrencinin telefonda sesli okuyacağı satırlar; aday sayfasının Saha modu kartı bu bölümü olduğu gibi gösterir. Genel arama sırası (tanış, rahatlat, gözlem ya da açılış sorusu, işleyiş sorusu, ne yaptığın, randevu) ve genel itirazlar (müsait değilim, ne için arıyorsunuz, WhatsApp'tan gönderin, kendimiz ilgileniyoruz, bot istemiyoruz, pahalı, ilgilenmiyorum) adaya-mesaj-yaz modülünde durur, karta yazılmaz. Karta yalnız bu nişe özel olan girer. Bölümün yapısı sabit, satır adları değişmez:

- `Açılış sürümü: [sayı]` Bölümün ilk satırı. Yeni kartta 1. Açılış sorusu ya da Ne yaptığın satırı değiştiğinde bir artar; itiraz eklemek ya da yazım düzeltmek sürümü değiştirmez. Sahadan gelen sonuçlar bu sayıyla etiketlenir, eski ve yeni metin yan yana okunabilsin diye.
- `Açılış sorusu: "…"` Kartın açılış cümlesinin telefonda sorulan hali. Tek soru, işletmecinin bir cümleyle cevaplayabileceği, zaten yapması gerektiğini bildiği bir şeyi hatırlatan. Sınav sorusu değil ("kaç arama kaçırdığınızı biliyor musunuz" yazılmaz).
- `İşleyiş sorusu: "…"` Yoğunken telefona ya da mesaja yetişemeyince müşterinin ne yaptığını soran tek soru, nişin diliyle (sahada, koltukta, ameliyatta, keşifte).
- `Ne yaptığın: "…"` Sistemin bu nişte ne yaptığı, tek cümle, kapsam içi: yazan müşteriye dakikalar içinde cevap, bilgiyi alıp randevuya ya da teklife yazma, eski müşteriye zamanı gelince hatırlatma. Teslim edilmeyen parça (cevapsız aramayı geri arama, telefonu açan sesli asistan) yazılmaz. Sonu sabit: "[Şehir]'de bu ay ilk üç [işletme türü] ile başlıyorum."
- `Çalışan açarsa: "…"` Telefonu sahibi yerine açan kişinin "ne hakkında" sorusuna nişin diliyle iki cümle ve saat isteği ("Ne zaman [yerde] olur?").
- `Karşı taraf bunu söylerse:` altında 5-7 madde, kartın "Gerçek itirazlar" bölümündeki itirazlardan, telefonda söylenecek biçimde. Her madde tek satır ve üç parça: `- "[itiraz, işletmecinin ağzından]" Söyle: "[sesli okunacak cümle]" Ne için: [tek cümle gerekçe] Sonra: [iki olası cevaba göre ne yapılır]`.

Bu bölümün kuralları: Söyle cümlesi soruyla biter ve tek soru taşır, ikinci itiraz sorusu yok. Lira rakamı telefonda söylenmez, görüşmeye kalır. Kartta olmayan rakam geçmez; kartın rakamı geçiyorsa işletmecinin anlayacağı biçimde ("iki katından fazla", "günde onlarca çağrı"). Kartın kanıtı öğrencinin ağzından iddia olarak söylenmez, işletmeciye soru olarak sorulur ("bunu sen söylemezsin, ona söyletirsin"). Yer tutucu yalnız [adın], [şehir], [Şehir], [Ad]. Kendini küçültme yok, muhtaç ton yok, ısrar yok; açık ret gelince teşekkür ve kapanış, aday bir daha aranmaz. "Sonra" satırında FounderOS'un ne yazacağı varsa açıkça yazılır ("FounderOS 'sonra, sezon başı' yazar"). Bu bölüm yoksa Saha modu kartı modülün genel metniyle çalışır, uydurmaz.

**Sahadan dolacak.** Bilinmeyenler listesi (gerçek dönüş süreleri, çalışan açılış cümlesi, kapatma oranı, hangi kademe satılıyor, ilk vaka çalışması).

**Kaynaklar.** Kullanılan tüm URL'ler.

## Kart modüllerinin adları

- Oto kuaför, seramik kaplama, araç kaplama: `nis-oto-kuafor`
- Güzellik salonu ve güzellik merkezi: `nis-guzellik-salonu`
- Klima ve kombi servisi: `nis-klima-kombi`
- Temizlik şirketi: `nis-temizlik`
- Oto servis ve cam filmi: `nis-oto-servis`
- Cam balkon, PVC pencere, panjur: `nis-cam-balkon`
- Mutfak-banyo tadilat ve iç mimarlık: `nis-tadilat`
- Emlak ofisi: `nis-emlak`
- Düğün organizasyon ve mekan: `nis-dugun`
- Randevulu kuaför ve berber: `nis-kuafor-berber`
- Haşere ilaçlama: `nis-hasere`
- Oto galeri: `nis-oto-galeri`
- Sigorta acentesi: `nis-sigorta`
- Elektrik ve teknik bakım: `nis-elektrik`
- Fotoğraf stüdyosu: `nis-fotograf`
- Diş kliniği: `nis-dis-klinigi`
- Pilates, PT ve butik stüdyo: `nis-pilates`
- Estetik cerrahi ve medikal estetik: `nis-estetik`
- Yetişkinlere yönelik dil ve mesleki eğitim kursları: `nis-dil-kursu`

Bir nişin rakamını, itirazını, yasal sınırını ya da kayıp birimini kendi kartından okursun. Kartta rakam yoksa "sahadan dolacak" der ve iş rakamsız yürür.
