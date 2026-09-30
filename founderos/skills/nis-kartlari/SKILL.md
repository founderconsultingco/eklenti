---
user-invocable: false
name: nis-kartlari
description: "On dokuz nis kartinin listesi, kart kurallari ve kart sablonu. Nis secilirken ve hangi kart modulunun acilacagi belirsizken acilir."
---

# FounderOS Niş Kartları (taslak 2, 5 Eylül 2026)

Kartlar plugin'in skill'lerinin okuduğu bilgi dosyalarıdır. Kural: uydurma yok, her rakam kaynaklı, bilinmeyen "sahadan dolacak" diye yazılır. Şablon en sonda.

Kartın "Yasal sınırlar" bölümü model başvurusudur: öğrenciye okunmaz, uygulanır. Aynısı kartın başka bölümlerinde geçen kanun, madde, ceza ve hukuk ayrıntısı için de, Kart özeti tablosundaki "Yasal sınır" sütunu için de geçerli. Öğrenciye yalnız yapılacak iş söylenir. Teyit gereken bir nokta öğrenciye ödev olmaz, ekip notu olur.

Durum: 19 kartın 19'u şablona göre yazıldı (kart başına 5 ile 47 kaynak; oto kuaför kartı şablona sonradan tamamlandı, dil ve mesleki eğitim kursları kartı en son eklendi). Bilinen açıklar: Meta Reklam Kütüphanesi hiçbir kartta görülemedi (canlı taramayla dolacak); diş kliniğinde TDB ve Resmi Gazete tam metni robot engeline takıldı; ekip teyidi şart, öğrenciye iş olarak verilmez.

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

**Ana kanal.** telefon ya da Instagram, tek kelime. Günün yüz temasının ellisi bu kanaldan gider, kırkı diğer iki kanaldan, onu video mesajdır. Kartın kanıtına dayanır, yazanın tercihine değil: talebin ve şikayetin hangi kanalda toplandığı neyse odur.

**Kanal ve zaman.** İşletmeciye nereden ulaşılır (telefon/Instagram/e-posta açıklığı; kanıt), günün hangi saati müsait, hangi saat kesinlikle değil. Adayın kendi talep kanalı hangisi (form, IG DM, WhatsApp, telefon): demo için talep nereye bırakılır.

**Reklam kütüphanesi kelimeleri.** Meta Reklam Kütüphanesi'nde aranacak 8-15 Türkçe anahtar kelime (hizmet adları, kampanya kelimeleri, yan hizmetler).

**İş ilanı kelimeleri.** İş ilanı sitelerinde ve Instagram'da aranacak, bu nişte telefonu ve randevuyu yöneten kişinin ilan adı ("resepsiyonist", "hasta kabul", "ön büro", "müşteri temsilcisi", "randevu asistanı" gibi), şehir adıyla. Kartta bu satır yoksa varsayılan altı kelime kullanılır: resepsiyonist, sekreter, çağrı karşılama, müşteri temsilcisi, randevu asistanı, ön büro.

**Yasal sınırlar.** Reklam, tanıtım, mesaj (İYS), sağlık, KVKK açısından bu nişe özel kısıt var mı; kaynaklı. Yoksa "yok". Bu bölüm model başvurusudur: öğrenciye okunmaz, uygulanır; öğrenciye yalnız yapılacak iş söylenir. Teyit gereken nokta öğrenciye ödev olarak yazılmaz; yerine model talimatı yazılır: "Bu nişte işletmeye giden her metin kartın hazır cümleleriyle sınırlıdır; yeni bir iddia gerekiyorsa denetçi çıkarır ve ekip notu düşülür. Öğrenciye hukuk anlatılmaz."

**Yoğun şehirler.** Kaynaklı.

**Gerçek itirazlar ve karşılıkları.** 5-7 itiraz; her biri işletmecinin ağzından, karşılık sektör verisiyle. Karşılıkta kanun ya da yönetmelik adı, madde, ceza, hukukçu, İYS, KVKK geçmez; hukuki bir itirazın karşılığı kısa, sakin, ders vermeyen bir cümledir ve gerçek olmayan güvence vermez. Bölümün ilk satırı sabit: `En güçlü üç itiraz: [üç kısa ad, virgülle]`. Sistem üç itiraz videosunu bu üçünden çekiyor.

**Telefonda söylenecekler.** Öğrencinin telefonda sesli okuyacağı satırlar; aday sayfasının Bugünün listesi kartı bu bölümü olduğu gibi gösterir. Genel arama sırası (tanış, rahatlat, gözlem ya da açılış sorusu, işleyiş sorusu, ne yaptığın, randevu) ve genel itirazlar (müsait değilim, ne için arıyorsunuz, WhatsApp'tan gönderin, kendimiz ilgileniyoruz, bot istemiyoruz, pahalı, ilgilenmiyorum) adaya-mesaj-yaz modülünde durur, karta yazılmaz. Karta yalnız bu nişe özel olan girer. Bölümün yapısı sabit, satır adları değişmez:

- `Açılış sürümü: [sayı]` Bölümün ilk satırı. Yeni kartta 1. Açılış sorusu ya da Ne yaptığın satırı değiştiğinde bir artar; itiraz eklemek ya da yazım düzeltmek sürümü değiştirmez. Sahadan gelen sonuçlar bu sayıyla etiketlenir, eski ve yeni metin yan yana okunabilsin diye.
- `Açılış sorusu: "…"` Kartın açılış cümlesinin telefonda sorulan hali. Tek soru, işletmecinin bir cümleyle cevaplayabileceği, zaten yapması gerektiğini bildiği bir şeyi hatırlatan. Sınav sorusu değil ("kaç arama kaçırdığınızı biliyor musunuz" yazılmaz).
- `İşleyiş sorusu: "…"` Yoğunken telefona ya da mesaja yetişemeyince müşterinin ne yaptığını soran tek soru, nişin diliyle (sahada, koltukta, ameliyatta, keşifte).
- `Ne yaptığın: "…"` Çözümün işleyiş sorusunun sorduğu ana dokunan parçası, tek kısa cümle (Truva Atı Metodu: sistemin tamamı sayılmaz). Kalıp: "Ben tam bunun için bir sistem kuruyorum: [nişin anı] telefona ya da mesaja yetişemediğinizde müşteriye dakikalar içinde dönüyor, [nişin iki üç bilgisi]ni alıp [randevuya ya da teklife] yazıyor." Sağlıkta "tıbbi bilgi ve fiyat vermiyor", sigortada "hangi acente adına konuştuğunu söyleyerek" cümlede kalır. Telefonun o anda açıldığı bu satıra yazılmaz: öğrencinin sesli örneği İş Beyni'nde "kuruldu" yazınca FounderOS bu cümlenin başına telefon tarafını ekleyip Bugünün listesi kartına kendisi yazar. Eski müşteriye hatırlatma da bu satıra yazılmaz; açılış sorusuna gelen cevap oraya giderse adaya-mesaj-yaz'ın işlev listesinden tek cümleyle söylenir. Sonu sabit: "[Şehir]'de bu ay ilk üç [işletme türü] ile başlıyorum."
- `Çalışan açarsa: "…"` Telefonu sahibi yerine açan kişinin "ne hakkında" sorusuna nişin diliyle iki cümle ve saat isteği ("Ne zaman [yerde] olur?").
- `Karşı taraf bunu söylerse:` altında 5-7 madde, kartın "Gerçek itirazlar" bölümündeki itirazlardan, telefonda söylenecek biçimde. Her madde tek satır ve üç parça: `- "[itiraz, işletmecinin ağzından]" Söyle: "[sesli okunacak cümle]" Ne için: [tek cümle gerekçe] Sonra: [iki olası cevaba göre ne yapılır]`.

Bu bölümün kuralları: Söyle cümlesi soruyla biter ve tek soru taşır, ikinci itiraz sorusu yok. Lira rakamı telefonda söylenmez, görüşmeye kalır. Söyle, Ne için ve Sonra satırlarında kanun ya da yönetmelik adı, madde, ceza, hukukçu, İYS, KVKK geçmez; öğrenciye hukuk ödevi verilmez ("oda kuralına bak", "teyit et" yazılmaz). Kartta olmayan rakam geçmez; kartın rakamı geçiyorsa işletmecinin anlayacağı biçimde ("iki katından fazla", "günde onlarca çağrı"). Kartın kanıtı öğrencinin ağzından iddia olarak söylenmez, işletmeciye soru olarak sorulur ("bunu sen söylemezsin, ona söyletirsin"). Yer tutucu yalnız [adın], [şehir], [Şehir], [Ad]. Kendini küçültme yok, muhtaç ton yok, ısrar yok; açık ret gelince teşekkür ve kapanış; aday altı ay aranmaz, "bir daha aramayın" diyen hiç aranmaz. "Sonra" satırında FounderOS'un ne yazacağı varsa açıkça yazılır ("FounderOS 'sonra, sezon başı' yazar"). Bu bölüm yoksa Bugünün listesi kartı modülün genel metniyle çalışır, uydurmaz.

**Marka yönü.** markani-kur'un seçim ekranını besler. Tasarım kararı değil, başlangıç noktası.
İsim kökleri: [üç kök, nişin kendi dilinden]. Sistem adı kurulurken köke mekanizma (Flow, Sync, Loop, Pulse, Track, Link, Core) ve varsa sistem eki (OS, HQ) eklenir.
İsim aileleri: [müşterisi usta ve esnafsa: kısa uydurma, kısa Türkçe kelime, soyadı | müşterisi İngilizce kelimeye alışıksa: sistem adı, kısa uydurma, soyadı].
İşaretler: [üç işaret: capraz hilal akis halka dugum kule dalga kivrim kademe mercek cekirdek yildiz].
Paletler: [üç palet: gece murekkep orman koz celik bordo kum derin mor kiremit].
Tipografi: [iki eşleşme: teknik karakter editoryal saglam yumusak sade].

**Sahadan dolacak.** Bilinmeyenler listesi (gerçek dönüş süreleri, çalışan açılış cümlesi, kapatma oranı, hangi kademe satılıyor, ilk vaka çalışması). Hukuk ve izin soruları (yönetmelik metni, madde numarası, İYS, KVKK) sahadan değil ekipten gelir; listede duruyorsa "sahadan değil ekipten gelir; öğrenciye sorulmaz" diye işaretlenir.

**Kaynaklar.** Kullanılan tüm URL'ler.

## Kart özeti

Seçim için tek bakış. Karar ve rakam her zaman kartın kendisinden okunur; tablo yalnız hangi kartın açılacağını gösterir. "Düşük hazırlık" sütunu: hazırlık seviyesi düşük öğrenciye (satış tecrübesi yok ve telefon zorluyor ya da üç hazırlık ölçütünün ikisi yok) ilk müşteriye kadar önerilmeyen kartlar; öğrenci ısrar ederse bir kez rakamla karşı çıkılır, risk yazılır, devam edilir.

| Kart | Modül | Ana kanal | Müşteri yolculuğu | Masa puanı | Sezon (ilk cümle) | Kısıt (model içindir, öğrenciye okunmaz) | Düşük hazırlık |
|---|---|---|---|---|---|---|---|
| Oto kuaför, seramik kaplama, araç kaplama | `nis-oto-kuafor` | Instagram | randevu | 8/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Yok. | olur |
| Güzellik salonu ve güzellik merkezi | `nis-guzellik-salonu` | Instagram | randevu | 9/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | 12 Kasım 2025'te yürürlüğe giren Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hakkında Yönetmelik'in kapsamı Madde 2'de "sağlık meslek... | olur |
| Klima ve kombi servisi | `nis-klima-kombi` | telefon | randevu | 8/10 | Klima tarafında mayıs ile ağustos arası, kombi tarafında ekim ile ocak arası yoğun, tepe ay haziran. | Klima/kombi bakım hizmetinin pazarlamasına özel bir reklam ya da mesaj kısıtlamasına rastlanmadı. | olur |
| Temizlik şirketi | `nis-temizlik` | telefon | teklif | 9/10 | Kartta ay bazında sezon bilgisi yok. Sadece duran havuz bölümünde bahar temizliği ve bayram öncesi yoğunluk geçiyor, yani ilkbahar ve bayram öncesi... | Standart temizlik hizmeti (süpürme, silme, koltuk/halı yıkama) için sektöre özel bir sağlık ruhsatı şartına rastlanmadı; işyeri açma ve çalışma... | olur |
| Oto servis ve cam filmi | `nis-oto-servis` | telefon | randevu | 10/10 | Lastik tarafında 15 Kasım ile 15 Nisan arası yoğun; bunu kartın duran havuz bölümündeki kış lastiği takviminden çıkardım (bu tarihler ticari araçta... | Rekabet Kurumu'nun motorlu taşıtlar sektöründeki grup muafiyeti tebliği (2017/3), garantili araç sahiplerinin bağımsız serviste bakım yaptırma... | olur |
| Cam balkon, PVC pencere, panjur | `nis-cam-balkon` | telefon | teklif | 9/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | İki önemli nokta var. Birincisi, kapı ve pencere sistemleri, cam balkonlar ve elektrikli panjurlar Garanti Belgesi Yönetmeliği'nin 18. maddesi gereği... | olur |
| Mutfak-banyo tadilat ve iç mimarlık | `nis-tadilat` | telefon | teklif | 10/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Bu oturumda nişe özel bir reklam/tanıtım kısıtı bulunamadı; TMMOB İçmimarlar Odası'nın meslek etiği/reklam kuralları sayfası bu oturumda erişilip... | olur |
| Emlak ofisi | `nis-emlak` | telefon | ikisi birlikte | 7/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Bu nişte mevzuat çok belirleyici, sistemi doğrudan etkiliyor. | önerilmez |
| Düğün organizasyon ve mekan | `nis-dugun` | Instagram | ikisi birlikte | 9/10 | Nisan ile ekim arası yoğun, kasım ile mart arası sakin. Bunu kartın kanal ve zaman bölümünden çıkardım: sezon ilkbahar ile sonbahar arasına... | Düğün salonları ve organizasyon firmaları "sıhhi işyeri" sınıfında sayılıyor ve belediyeden "Umuma Açık İstirahat ve Eğlence Yeri Açma ve Çalışma... | olur |
| Randevulu kuaför ve berber | `nis-kuafor-berber` | Instagram | randevu | 8/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | İki ayrı konu var. Birincisi Pazar günü zorunlu kapanış, il valiliği kararına göre değişiyor, yukarıda anlatıldı (salonmerkezi.com). | olur |
| Haşere ilaçlama | `nis-hasere` | telefon | teklif | 8/10 | Yaz sonu yoğun, tepe ay ağustos. Bunu kartın kendi verisinden çıkardım: sivrisinek ve haşere şikayetlerinin yoğunlaştığı dönem yaz sonu olarak... | Bu iş "Halk Sağlığı Alanında Haşerelere Karşı İlaçlama Usul ve Esasları Hakkında Yönetmelik"e tabi (kaynak: saglik.gov.tr/TR,10472... | olur |
| Oto galeri | `nis-oto-galeri` | telefon | ikisi birlikte | 9/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Bu niş için gerçek ve güncel bir kısıt var: İkinci El Motorlu Kara Taşıtlarının Ticareti Hakkında Yönetmelik 27 Ağustos 2024'te yürürlüğe girdi. | olur |
| Sigorta acentesi | `nis-sigorta` | telefon | teklif | 9/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Sigorta Acenteleri Yönetmeliği Madde 19 (İlan, Reklam, Afiş ve Pano) iki bağımsız kaynaktan doğrulandı... | önerilmez |
| Elektrik ve teknik bakım | `nis-elektrik` | telefon | ikisi birlikte | 8/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Elektrik Tesisleri Kabul Yönetmeliği'nin kapsamı üretim, iletim ve dağıtım tesisleri; "Elektrik İç Tesisleri Yönetmeliği kapsamına giren elektrik... | olur |
| Fotoğraf stüdyosu | `nis-fotograf` | Instagram | ikisi birlikte | 8/10 | Mayıs ile ekim arası yoğun, kasım ile nisan arası ölü. Bunu kartın kendi verisinden çıkardım: düğün sezonu mayıs-ekim olarak veriliyor, yoğun sezonda... | Ustalık belgesi zorunluluğu Rekabetin şekli bölümünde anlatıldı (ornekbelge.com.tr); reklam ve mesajla ilgili değil ama işletme meşruiyetini... | olur |
| Diş kliniği | `nis-dis-klinigi` | telefon | randevu | 9/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Sağlık Bakanlığı 12 Kasım 2025'te, Resmi Gazete Sayı 33075 ile "Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hakkında Yönetmelik"i... | önerilmez |
| Pilates, PT ve butik stüdyo | `nis-pilates` | Instagram | randevu | 9/10 | Yaz ayları ölü, yılın kalanı yoğun. Bunu kartın kendi rakamından çıkardım: yaz aylarında müşteri sayısında yüzde 20-30 ek düşüş var ve sezonluk... | Pilates stüdyoları Gençlik ve Spor Bakanlığı'nın yetki/yeterlilik sistemine tabi. | olur |
| Estetik cerrahi ve medikal estetik | `nis-estetik` | Instagram | randevu | 9/10 | Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor. | Ana düzenleme: Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hakkında Yönetmelik, ilk hali 29 Temmuz 2023'te yürürlüğe girdi (RG 32263... | önerilmez |
| Yetişkinlere yönelik dil ve mesleki eğitim kursları | `nis-dil-kursu` | telefon | ikisi birlikte | 9/10 | İki kayıt dalgası: Eylül-Ekim (akademik yıl başı) ve Ocak-Şubat (yeni yıl); kampanyalar bu iki döneme yığılıyor (English Time 2026 yazısı). | 5580 sayılı Özel Öğretim Kurumları Kanunu ve MEB Özel Öğretim Kurumları Yönetmeliği: gerçeğe aykırı reklam yasak; öğrencinin resmi, bilgisi ve başarı... | olur |

Bir nişin rakamını, itirazını, yasal sınırını ya da kayıp birimini kendi kartından okursun. Kartta rakam yoksa "sahadan dolacak" der ve iş rakamsız yürür. Bir elemenin verisi kartta yoksa sonuç "bilinmiyor" olur, geçti sayılmaz.
