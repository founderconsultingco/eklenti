---
user-invocable: false
name: satis-videosunu-cek
description: "Beşinci günün ikinci yarısı, provalarla aynı gün. Ön görüşme videosu, üç itiraz videosu ve site videosu."
---

# satis-videosunu-cek

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "satis-videosunu-cek"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Beşinci günün ikinci yarısının modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Yol Haritası'nın dördüncü aşaması, satışa hazırlan: satış videoları.

Bu modül ön görüşme videosunu çektirir. Randevu alan adaya, görüşmeden önce izlettiğin video. Üstüne üç kısa itiraz videosu gelir.

Neden bu video: randevu alan adayların bir kısmı gelmiyor. Gelmeyenlerin çoğu kiminle konuşacağını bilmediği için gelmiyor. Görüşmeden önce seni izlemiş olan aday görüşmeye hem daha çok geliyor hem hazır geliyor.

Bu sayfa kurulu değilse hem gelme oranın hem kapanış oranın düşüyor, çünkü aday görüşmeye ne beklediğini bilmeden geliyor.

### Siteye iki video girmiyor, bir video giriyor

Bunu açıkça yazıyorum, çünkü "satış videosu" denince akla o geliyor.

Sitenin video bölümü yarın sahaya çıktığında dolu olmak zorunda. Mesajındaki linke tıklayan işletmeci boş bir sayfa değil, seni görecek. O yüzden site videosu bugün çekiliyor.

Ayrı bir gün gerekmiyor: site videosu aynı oturuşta, aynı kıyafetle, aynı yerde, ön görüşme videosunun hemen arkasından çekilir. Ama onun kısaltması değil. Ön görüşme videosu randevu almış adama konuşuyor ("bu videoyu benimle görüşme ayarlayan herkes için çektim") ve ondan bir şeyler istiyor; site videosu seni hiç tanımayana gidiyor ve ondan tek bir şey istiyor, görüşme planlamak. Aynı malzeme tanımayana göre yeniden sıralanır, beş parça, iki dakika:
1. Kanıtla aç, on beş saniye: "Geçen hafta Bursa'da otuz klima servisini akşam yedide aradım, yirmi ikisine ulaşamadım. O saatte arayan müşteri ne yapıyor? Sıradaki numarayı arıyor." Kanıt cümlen yoksa kartın kaynaklı rakamıyla açılır; kanıt cümlesi çıkınca bu parça yeniden çekilir.
2. Tek sahne, yirmi saniye, hizmet akışındaki "bir günü anlat"tan: "Saat yedi kırk, usta kombinin başında, telefon cepte çalıyor. Bugün o arama kayboluyor. Sistemle aramayı resepsiyonist açıyor, ne istediğini soruyor, randevuyu yazıyor."
3. Kim, on saniye: "Ben [ad]. [Şehir]'deki [niş] işletmelerine bu kaçan aramayı yakalayan sistemi kuruyorum."
4. Ne yapıyorum, otuz saniye: sistemin adı ve üç akış, tek cümlelik adımlar, araç adı yok.
5. Görüşme ve çağrı, otuz saniye: "Yirmi dakikalık görüşmede sizde kaç aramanın kaçtığını birlikte sayıyoruz. Size uygun değilse bunu da söylerim. Aşağıdan saat seçin."
Kesme yok, müzik yok. Demo kaydı videoya gömülmez, demoya dair tek cümle yeter.

Siteye konan uzun satış videosu ayrı bir iştir ve bugün çekilmez. Onun işi ikna etmek değil, reklamdan gelen kalabalığı elemek. İki şartı var ve ikisi de bugün yok: elenecek kadar çok yabancının sayfaya gelmesi için her gün reklam parası harcaman gerekiyor, ve videonun içine koyacağın kanıt ilk müşteriden sonra çıkıyor. Kanıtsız çekilen uzun video kimseyi elemiyor, sadece bir günü yiyor. Onu satis-sayfasini-yaz kurar.

Şunlar bu modülün işi değildir:
- Landing page (siteni-kur, birinci blok; ikinci blokta yayında).
- Ön görüşme sayfasının kurulması ve randevu akışı (gorusmeye-getir, CRM açıldığı gün). Bu modül videoyu üretir, o sayfaya koyar.
- Video mesaj (video-mesaj-cek). O bir dakika ve adaya özel.
- Siteye konan uzun satış videosu ve satış sayfası (satis-sayfasini-yaz, ilk müşteriden sonra). Sitenin kısa tanıtım videosu bu modülün işi.

Sistemdeki videolar, karıştırma:
- **Ön görüşme videosu:** bu modül. Üç ile beş dakika, herkese aynı, randevu alana gider.
- **İtiraz videoları:** bu modül. Üç tane, her biri bir iki dakika, aynı sayfada durur.
- **Video mesaj:** bir dakika, adaya özel, Loom ile; ilk yazılı temastan sonra üçüncü gün cevap gelmediyse ikinci dokunuş olarak, önce en çok istenen yüz işletmeye (video-mesaj-cek).
- **İzinden sonraki demo videosu:** bir iki dakika, cevap verip çalışan örneği görmek isteyen adaya: onun sayfası, konuşulan ihtiyaç, demoda test randevusu, görüşme daveti (video-mesaj-cek).
- **Deneme videosu:** beşinci gün, kimseye gitmez.
- **Site videosu:** bu modül, aynı oturuş. Ön görüşme videosunun malzemesi seni hiç tanımayana göre yeniden sıralanır, beş parça, iki dakika; sitenin video bölümüne girer.
- **Uzun satış videosu:** ilk müşteriden sonra, satış sayfasıyla birlikte.
- **Rapor günü videosu:** müşterinin çektiği kısa video.

Pazarlamadaki karşılığı: görüşmeden önce seni izlemiş aday, görüşmeye yabancı gelmiyor.

## 2. Ne zaman çalışır
- Beşinci günün ikinci yarısında, bir buçuk saat. Beş video aynı oturuşta: ön görüşme videosu, site videosu, üç itiraz videosu. Her video tek parça çekilir ve telefondan doğrudan yüklenir. Provaların yapıldığı gün; kayda konuşmakla prova aynı kası çalıştırıyor, ikisi arka arkaya daha iyi gidiyor.
- İlk kanıt hikâyesi çıkınca ikinci kez: kanıt parçası gerçek müşteriyle değişir.
- Elli görüşme dolmadan metin değişmez.

## 3. Ne okur

İş Beyni'nden: adın, şehir, iş adı, Dönüşüm Cümlesi, sistemin adı, üç kademenin içeriği, görüşme süresi.
Niş kartından: sızıntı kanıtı, işletmecinin sözlüğü ve dertleri, üç itiraz.
İş Beyni'nin on sekizinci bölümünden (ideal müşteri sayfası): tek cümlelik tanım ve üç dert. Videonun ilk on saniyesi birinci başlıktaki kişiye hitap eder.
kanitini-hazirla'dan: deneme aramasının sonucu ve kanıt cümlesi. Henüz yoksa niş kartındaki rakam.
Marka kitinden: video kapağı şablonu.

## 4. Ne sorar

Sormaz. Metni FounderOS yazar.

Tek şey ister: çekimden önce metni bir kez sesli okuman. Ağzına oturmayan cümleyi söylersin, değiştirir.

## 5. Ne yapar

### Ön görüşme videosunun yedi parçası

Sıra sabit. Toplam üç ile beş dakika.

**1. Kim olduğun ve videonun sebebi.** Otuz saniye. "Ben Ahmet. Bu videoyu, benimle görüşme ayarlayan herkes için çektim, ki yarın konuşurken ikimiz de hazır olalım."

**2. Görüşmede ne olacağı.** Bu parça beklentiyi kuruyor ve gelme oranını en çok yükselten yer burası. "Yirmi dakika. Bu bir satış konuşması değil; size uyup uymadığımıza bakacağız. Uymuyorsa bunu size ben söyleyeceğim."

**3. Senden istediklerim.** Sessiz bir yerde ol, araba kullanırken bağlanma, yanında kâğıt kalem olsun. Sebebi de söylenir: "İşinizle ilgili sorular soracağım, sistemi de kendi telefonunuzda deneyeceksiniz."

**4. Neden gelmeni istiyorum.** Bu parça dürüst ve işe yarıyor: "Her görüşmeden önce o işletmeyi inceliyorum. Sizin sayfanıza, yorumlarınıza, telefonunuza baktım. Bu bir saatimi alıyor, o yüzden gelemeyecekseniz haber verin, kırılmam. Ama söz verdiyseniz bekliyorum." Bu cümle uydurma değil; sistem gerçekten her görüşmeden önce görüşme özet ekranını hazırlıyor ve sen deneme aramasını yapıyorsun.

**5. Ne yaptığın, kısaca.** Sistemin adı ve üç adım, tek cümlelik adımlar. Teknik kelime yok. Bu parça kısa kalır; asıl anlatım görüşmede.

**6. Kanıt.** İlk müşteriden önce kanıt dört şeydir: niş kartındaki rakam, senin kendi deneme araman, sesli örneğin kaydı (varsa) ve tarayıcı demosunun kırk ile altmış saniyelik ekran kaydı (ikinci blokta çekilir; üstüne tek cümle: bu bir örnek, gerçek sistem işletmenin kendi kurallarıyla kurulur). "Geçen hafta şehrimizdeki otuz klima servisini akşam yedide aradım, yirmi ikisi açmadı." Bu cümle gerçek olacak; sayı uydurulmuyor. İlk kanıt hikâyesi çıkınca bu parça onunla değişir ve video yeniden çekilir.

**7. Onaylama ve kapanış.** "Aşağıdaki EVET düğmesine basın, takvim davetini kabul edin. Görüşmeden önce iki hatırlatma göndereceğim. Yarın görüşürüz."

### Üç itiraz videosu

Ön görüşme videosunun altına üç kısa video daha konur. Her biri bir ile iki dakika, tek çekim, tek konu.

Konular niş kartının üç itirazından gelir. Çoğu nişte bunlar çıkıyor:
- "Bu nasıl çalışıyor, gerçekten iş getiriyor mu?"
- "Ne kadar tutuyor?"
- "Daha önce böyle şeylere para verdim, olmadı. Bunun farkı ne?"

Fiyat videosunda rakam verilmez. Verilen şey şu: neye göre fiyatlandığın ve rakamı görüşmede matematiğiyle söyleyeceğin.

Bu üç videonun işi şu: aday bu soruları görüşmede sormuyor, çünkü cevabını biliyor. Böylece hem gelme oranı hem kapanış oranı yükseliyor.

### Süre

Ön görüşme videosu üç ile beş dakika. Bu videoyu üç dakikadan yirmi dakikaya kadar çekenler var, ama yirmi dakikayı dolduran kişinin elinde yıllarca birikmiş kanıt var. Senin beşinci gününde beş dakikadan fazlası doldurma olur ve doldurma izlenmiyor.

İtiraz videoları bir ile iki dakika.

### Çekim

Telefonla, tek çekim. İki yol var, ikisi de işliyor ve seçim senin: yüz yolu (ön kamera, sen konuşursun) ya da ses yolu (sesini kaydedersin, üstüne sitenin, demonun ve deneme aramanın ekran görüntüleri gelir). Kameraya çıkmak istemiyorsan ses yolu kalıcıdır; yüzle yeniden çekmek şart değil.

Kurallar:
- Işık pencereden gelsin, pencere karşında olsun.
- Sade arka plan. Dağınık oda yok.
- Telefon göz hizasında, bir yere yaslı.
- Sessiz oda. Ses görüntüden önemli.
- Kesme yok, müzik yok, animasyon yok.

Üç çekim yaparsın, en iyisini seçersin. Dördüncüyü çekmezsin; dördüncüden sonra ezbere kayılıyor.

Metni ezberleme, yedi parçayı bil ve kendi kelimelerinle anlat.

### Yükleme ve yerleştirme

Videolar YouTube'a liste dışı yüklenir. Liste dışı video aramada çıkmaz, linki olan izler. Kanal dördüncü blokta kisisel-markani-kur ile açılmıştı. Yükleme telefondan, çektiğin anda; bilgisayara taşımak yok. Her video bir çekimdir: kesme, birleştirme, kurgu yok; üç denemenin en iyisi olduğu gibi yüklenir. Telefonundaki YouTube uygulamasında alttaki artı düğmesi, "Upload a video" (video yükle), videoyu seç; başlık kutusuna videonun adını yaz, görünürlükte "Unlisted" (liste dışı) seç, "Upload" (yükle). Yükleme bitince videonun yanındaki üç noktadan "Share" (paylaş), "Copy link" (bağlantıyı kopyala); bağlantıyı bana yapıştır. Uygulamanın dili Türkçeyse aynı düğmelerin Türkçesi ekranda yazıyor; ekran tarif ettiğimden farklıysa görüntüsünü at, hangi düğme olduğunu söylerim.

Ön görüşme sayfasına şu sırayla konur: ön görüşme videosu en üstte, altında EVET düğmesi, altında üç itiraz videosu.

EVET düğmesi videodan sonra değil, videonun hemen altında durur. Videoyu sonuna kadar izlemeyen de onaylayabilmeli.

### Videoyu izletmek

Video sayfaya konunca iş bitmiyor. Randevu alan adayların bir kısmı sayfayı açıp videoyu izlemiyor.

Bu yüzden hatırlatma mesajlarının işi videoyu izletmek. Randevudan sonra giden ilk mesaj ve ilk e-posta "görüşmeden önce şu üç dakikalık videoyu izleyin" der. Bu akış CRM açıldığı gün gorusmeye-getir'de kuruluyor; o güne kadar videoyu randevu alan adaya WhatsApp'tan sen gönderiyorsun.

### İlk videon ortalama olacak

İzleyince beğenmeyeceksin, herkes beğenmiyor. Kural: üç çekim, en iyisini seç, yükle, bir daha izleme.

Video elli görüşme dolmadan değişmiyor. O zamana kadar aynı cümleleri elli kez canlı söylemiş olacaksın ve ikinci video kendiliğinden iyi olacak.

### Ses yolu

Sesini kaydedersin, üstüne sitenin, demonun ve deneme aramanın ekran görüntülerini koyarsın; telefonun ekran kaydıyla tek parça çekersin. Kurallar aynı: sessiz oda, tek çekim, montaj yok. Bu yol işliyor ve kalıcıdır. İleride yüzünle çekmek istersen elli görüşmeden sonraki ikinci videoda çekersin; o noktada aynı cümleleri elli kez canlı söylemiş olacaksın. İstemezsen ses yolunda kalırsın.

## 6. Ne söyler

Açılışta: "Bir buçuk saat. Beş video: üç dakikalık ön görüşme videosu, iki dakikalık site videosu, üç tane bir dakikalık itiraz videosu. Telefonla, her biri tek parça, montaj yok; çektiğin anda telefondan yüklüyorsun. Yüzünle ya da sesinle, sen seçiyorsun. Ön görüşme videosunu görüşmeye gelen herkes izleyecek."
Site videosunu sorarsa: "Siteye giren kısa videoyu bugün, aynı oturuşta çekiyoruz: ön görüşme videosunun malzemesi, seni hiç tanımayana göre beş parçada, iki dakika. Yarın sahaya çıkıyorsun ve mesajındaki linke tıklayan adam seni tanısın istiyoruz. Siteye konan uzun satış videosu ayrı bir iş, onu ilk müşteriden sonra çekiyoruz; çünkü onun işi kalabalığı elemek ve bugün ne kanıtın var ne reklamın."
Metni verirken: "Yedi parça. Ezberleme, bil. Şimdi bir kez sesli oku; ağzına oturmayan cümleyi söyle, değiştireyim."
Dördüncü parçada: "Bu cümleyi rahat söyle, çünkü doğru. Her görüşmeden önce o işletmeyi gerçekten inceliyorsun. Bunu söyleyene insanlar geliyor."
Kanıt parçasında: "Buraya kendi deneme aramanın sonucunu koyuyoruz, gerçek sayıyla. Uydurma rakam koymuyoruz; ilk soruda çöker."
Beğenmezse: "İlk videon ortalama olacak, herkesinki öyle. Üç çekim yaptın, en iyisini seç. Dördüncüyü çekme."
İtiraz videolarını atlamak isterse: "Üç dakikalık iş. Bu üç video adayın görüşmede soracağı üç soruyu önceden cevaplıyor. Cevabı bilerek gelen aday hem daha çok geliyor hem daha kolay kapanıyor."
Kameraya çıkmak istemiyorsa: "Sorun değil. Ses yolu da işliyor: senin sesin, üstünde ekran görüntüleri. Yüzünü göstermek zorunda değilsin."

## 7. Ne yazar

İş Beyni'ne: ön görüşme videosunun adresi, üç itiraz videosunun adresleri, metnin sürümü ve tarihi, kaç çekimde alındığı, hangi yolla çekildiği (yüz ya da ses).

CRM'e: ön görüşme videosunun adresi özel değerler ekranındaki "ön görüşme videosu linki" satırına yapıştırılır. Randevu alındığı anda giden e-posta o satırı okuyor; satır boşsa mesaj linksiz gidiyor ve adayın videoyu izlemesi için elinde bir şey kalmıyor.
Bir sonraki modüllere: video adresleri gorusmeye-getir'in ön görüşme sayfasına ve hatırlatma metinlerine.
Niş kartına: elli görüşmeden sonra hangi itirazın videoya rağmen sorulduğu.

## 8. Yedek yol

- Bugün çekilemezse: ertesi sabah çekilir. Ön görüşme sayfası videosuz açılır, yerine üç cümlelik yazı konur ve gün durmaz.
- Ses kötü çıkarsa: kulaklık mikrofonuyla tekrar. Kötü ses videoyu bitirir.
- Kameraya çıkmak istemiyorsan: ses yolu, yukarıdaki kuralla; kalıcıdır.
- Üç itiraz videosuna vakit kalmazsa: ön görüşme videosu bugün, itiraz videoları ertesi sabah. Sıra bu, tersi değil.
- Telefondan yükleme olmuyorsa: video bilgisayara alınır ve youtube.com'dan yüklenir: sağ üstte "Create" (oluştur), "Upload videos" (video yükle), görünürlükte "Unlisted" (liste dışı).
- YouTube'a yüklenemezse: video geçici olarak sayfaya doğrudan konur.
- Üç çekimde de olmadıysa: en iyisi yüklenir. Dördüncü çekim yok.
- Sağlık nişindeysen: metinde tedavi sözü, hasta görseli ve "kesin sonuç" gibi iddialar geçmez. Metni FounderOS kartın yasal sınırlar bölümüne bakarak yazar; öğrenciye kural anlatılmaz.

## 9. Sıradaki adım ve işaretler

Sıradaki: bu videolar ön görüşme sayfasına CRM açıldığı gün giriyor; o güne kadar WhatsApp'tan gidiyor. Aynı blokta video mesaj kurulumu, öğleden sonra sahaya çıkış kontrol listesi.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Beşinci gün bitti, video yok: altıncı sabahın ilk işi olur.
- Dördüncü çekim isteği: reddedilir, en iyisi yüklenir.
- Ses yolu kullanıldı: yüzle yeniden çekim şart değil; öğrenci isterse elli görüşmeden sonraki ikinci videoda yüzle çeker.
- Otuz randevu doldu ve gelme oranı yüzde ellinin altında: videonun izlenip izlenmediğine bakılır, hatırlatma metinleri gözden geçirilir.
- Elli görüşme doldu: metin gözden geçirilir, karar degisiklige-karar-ver'de verilir.
- İlk kanıt hikâyesi çıktı: altıncı parça değişir, video yeniden çekilir. satis-sayfasini-yaz'ın üç şartı da sağlanıyorsa o modül açılır.
- Aynı itiraz görüşmelerin yarısında videoya rağmen soruluyor: o itiraz videosu yeniden çekilir.

Beş kural: boş sayfa yok (yedi parçalı metin ve üç itiraz konusu hazır gelir) · sessiz bitiş yok (akşam videolar yayında) · onay (metin senin sesli okumandan sonra kesinleşir) · sahadan güncelleme (elli görüşmede metin, kanıt çıkınca video yenilenir) · sormaz söyler (metni, sırayı ve çekim kurallarını FounderOS verir).
