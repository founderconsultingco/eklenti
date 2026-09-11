---
user-invocable: false
name: musteri-sistemini-kur
description: "Müşterinin ikinci gününden itibaren. AI Müşteri Dönüşüm Sistemi'nin kurulması: yedi altyapı parçası, üç ajan, on üç işlev; hangi parçaların açılacağını nişin müşteri yolculuğu (randevu ya da teklif) belirler."
---

# musteri-sistemini-kur

## 1. Adı, rolü, pazarlamadaki karşılığı

Teslimatın ikinci modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül müşterinin sistemini kurar.

Bir şeyi baştan netleştiriyorum, çünkü satışın tamamı buna dayanıyor. Sen tek tek otomasyon satmıyorsun, komple sistem satıyorsun. Müşteriye "cevapsız aramaya mesaj atan bir şey" ya da "randevu alan bir bot" kurmuyorsun. İşletmenin gelen talebi karşılayan, randevuya çeviren, takip eden ve eskiyi geri kazanan bütün tarafını kuruyorsun. Dışarıda kalan tek taraf aday bulma, yani reklam ve liste çıkarma. Bu ayrım fiyatı da belirliyor: parçaların tek tek karşılığı yoktur, sistemin karşılığı vardır. Müşteri "şu parçayı çıkaralım, ucuzlasın" derse cevabın hazır: parçalar birbirini besliyor, biri çıkınca fiyat değil sonuç düşüyor.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil.

Bir de dil ayrımı: "müşteri" senin paranı ödeyen işletmedir. Onun kendi müşterisine bu bölümde "arayan kişi" ya da "işletmenin müşterisi" diyoruz.

### Kurulan sistem: üç ajan, on üç işlev, yedi altyapı parçası

Kurduğun şeyin listesi "İş modeli" bölümünde duruyor ve buradaki liste onun kurulum sırasına dizilmiş halidir; 17. ve 22. satırlar işlev değil, altyapının (ödeme ve rapor) bu listedeki yeridir, sayım yine üç ajan, on üç işlev, yedi altyapı. Her satır ayrı bir ürün değil; bir kısmı asistanın yürüttüğü iş, bir kısmı asistanla birlikte çalışan otomasyon. Müşteriye anlatırken parça saymazsın, yolculuğu anlatırsın: "Biri yazdığında, aradığında, geldiğinde ya da gelmediğinde ne oluyor."

**Hangi parçalar açılır, yolculuk söyler.** Randevu nişinde takvim, hatırlatma ve gelmeyeni geri kazanma açılır; teklif takibi kapalı kalabilir. Teklif nişinde teklif takibi, görüşme sonrası takip ve kapora yolu açılır; takvim ancak keşif randevusu varsa. İkisi birlikte olan nişte ikisi de açılır. Açılmayan parça sessizce düşmez; kurulum görüşmesinde söylenir ve teslim paketinde "bu işletmede kapalı, sebebi şu" diye yazar.

**Altyapı, önce (birinci dalga, ilk gün):**
1. Müşteri ve Satış Süreci Takibi (CRM & Pipeline). Bütün kanallar tek ekrana düşer, her kişinin tek kaydı olur, aşamalar yolculuğa göre adlandırılır.
2. İletişim Kanalı Bağlantıları (Channel Integrations). WhatsApp, Instagram, site sohbeti, formlar, karekod; telefon ikinci dalgada.
3. İşletme Bilgi Bankası (Knowledge Base). Hizmetler, onaylı fiyatlar, saatler, sık sorular. Asistan burada olmayan şeyi uydurmaz, "çalışana aktarıyorum" der.
4. Takvim ve Yönlendirme (Calendars & Routing). Çakışmasız takvim, hangi işin hangi çalışana gideceği.
5. Konuşmayı Çalışana Devretme (Human Handover). Müşteri insan isteyince ya da asistanın yetkisi aşılınca; devralınca asistan susar.
6. Otomasyon ve Takip Kontrolleri (Workflow Controls). Randevu alınınca davet takibi durur, satış olunca satış takibi durur, aynı kişiye iki zincir aynı anda yazmaz.
7. Sonuç Takibi ve Raporlama (Reporting). Başvuru, randevu, katılım, teklif, doğrulanmış satış. Randevu satış sayılmaz, teklif kabulü ödeme sayılmaz.

**Gelen taraf (birinci dalga, yazılı; ikinci dalga, sesli):**
8. AI Mesajlaşma ve Randevu Asistanı (AI Chat & Appointment Setter). Yazana anında cevap verir, ihtiyacı öğrenir, ölçüte uygunluğuna bakar, randevuya ya da çalışana yönlendirir. Adayı Değerlendirme ve Yönlendirme (Lead Qualification & Routing) bu asistanın içindedir. Metni ve kuralları: yazili-asistani-kur.
9. Yeni Başvuruya Hızlı Dönüş (Speed-to-Lead). Form, karekod ya da mesaj gelince ilk iletişim altmış saniye içinde çıkar; ölçülür, kaçarsa bildirim yükselir. Formdan gelen başvuruya giden ilk mesajın şablonu hazır pakette gelir ve müşteri onaylar: "Merhaba [ad], [işletme adı]'na formunuz ulaştı. [Hizmet] için size en uygun saati bulalım: bugün mü, yarın mı?" Metin işletmecinin sözlüğüyle nişe uyarlanır, fiyat geçmez.
10. Cevapsız Arama Sonrası Mesaj (Missed-Call Text Back). Açılmayan aramanın ardından aynı dakika WhatsApp'tan yazılı dönüş.
11. AI Telefon Karşılama Asistanı (AI Voice Receptionist). İkinci dalga. İşletme açmadığında hattı karşılar, bilgi verir, randevu yazar, gerekince çalışana aktarır.

**Randevu ve satış (yolculuğa göre):**
12. Randevu Hatırlatmaları (Appointment Reminders). Onay mesajı, bir gün ve bir saat kala hatırlatma.
13. Randevuya Gelmeyeni Geri Kazanma (No-Show Recovery). Gelmeyenle aynı gün yeniden iletişim, yeni randevu hedefi.
14. AI Otomatik Takip (AI Auto Follow-Up). Konuşmayı yarıda bırakanı, cevap vermeyeni, "sonra" diyeni takip eden zincir. Bu ve 13, 15, 16 numaralı zincirlerin metni: yazili-asistani-kur, "Dört takip zinciri".
15. Fiyat Teklifinden Satışa Takip (Quote-to-Close). Teklif nişinde: işletmenin onayladığı teklif gönderilir, cevap ve kabul takip edilir, kapora ya da ödeme linki düşer.
16. Görüşme Sonrası Satış Takibi (Post-Call Follow-Up). Görüşüp almayanı, görüşmenin sonucuna göre takip.
17. Ödeme ve fatura (altyapı: Müşteri ve Satış Süreci Takibi'nin ödeme parçası). Kapora ya da tamamı için ödeme linki, ödendi bilgisinin kayda düşmesi.

**Geri kazanma ve itibar (Kademe 2):**
18. Eski Müşteri ve Başvuruyu Yeniden Kazanma (Database Reactivation). Duran havuzun mesajla geri çağrılması; izin ve altyapı uygunsa dış aramayla.
19. AI Dış Arama (AI Outbound Calling). Şarta bağlı, ilk müşteride vaat edilmez; sebebi aşağıda.
20. Müşteri Yorumu İsteme ve Referans İsteme (Review Requests, Referral Requests). İşi bitenden yorum, memnun olandan tavsiye.
21. Tekrar Randevu Alma ve Ek Hizmet Satışı (Rebooking, Upsell). Bakım ve kontrol zamanı gelince ulaşma; işletmenin önceden belirlediği ek hizmeti sunma. Bu ikisinin ve referans isteğinin metni: kaybolanlari-geri-getir, "Üç devam zinciri".

**Görünürlük:**
22. Sonuç ekranı ve aylık rapor (altyapı: Sonuç Takibi ve Raporlama). Müşterinin kendi girip rakamı gördüğü ekran, artı rapor günü ve aylık rapor.

Nişe göre parçalar düşer ve bu normaldir. Sağlık nişinde yorum yanıtlamanın dili daralır, teklif nişinde takvim kapalı kalabilir, randevu nişinde teklif takibi hiç açılmaz. Düşen parça niş kartında yazılıdır ve kurulum görüşmesinde söylenir.

Şunlar bu modülün işi değildir: asistanın senaryosu, soruları ve kuralları (yazili-asistani-kur), sesli ajanın konuşma metni ve kuralları (sesli-ajani-kur), eski müşteri mesajlarının metni ve gönderimi (kaybolanlari-geri-getir), yorum kampanyasının yürütülmesi (yorum-topla), aylık raporun yazılması (aylik-raporu-hazirla), karşılama ve izinler (musteriyi-karsila). Şöyle düşün: bu modül boruyu döşer, suyu başka modül akıtır.

Pazarlamadaki karşılığı hazır kurulum paketidir: adını yazınca çalışan set. Teknik karşılığı özel değerler ekranıdır. Oradaki satırlar bütün mesajları, sayfaları ve bildirimleri doldurur.

## 2. Ne zaman çalışır

Kurulum iki dalgada yapılır. Sebebi tek: yazılı taraf senin elinde, sesli taraf dışarıdan gelen bir hatta ve bir numaraya bağlı. İkisini aynı güne yığarsan sesli tarafın gecikmesi bütün teslimi durdurur.

- Kurulum görüşmesi biter bitmez, aynı gün: WhatsApp şablon onayları, telefon hattı başvurusu ve numara talebi başlatılır. İzinler o görüşmede alındığı için daha önce başlatılamaz. Gecikme de buradan çıkar.
- İkinci, üçüncü ve dördüncü gün: birinci dalga. Yazılı tarafın tamamı, takvim, formlar, ödeme, yorum, pano.
- Beşinci gün: birinci dalganın üç sorulu testi.
- Altıncı gün: birinci dalga canlıya alınır, teslim paketi gider.
- Yedinci günden on dördüncü güne: ikinci dalga. Hat gelince sesli ajan, cevapsız aramaya dönüş ve varsa giden arama kurulur, test edilir, canlıya alınır.
- Her canlıya almadan sonraki yirmi dört saat izlenir.
- On beşinci günden on sekizinci güne: kalan eksikler. İkinci dalga bu pencereye kayabilir, rapor gününün raporu kaymaz.
- Sonrasında sistem çalışır, haftalık kontrolü sistemi-kontrol-et devralır.

Tasarım kararı, açıkça söylüyorum: bu iki dalgalı sıra bir kaynaktan gelmiyor, sistemin kendi kararı. Sebebi ölçülebilir: yazılı taraf dışarıdan tek onay bekliyor (Meta'nın şablon onayı), sesli taraf üç şey bekliyor (numara başvurusu, hattın bağlanması, ses testi). Birinci dalga altıncı günde canlıya alındığı için müşteri sistemin çalıştığını sesli taraf gelmeden görüyor.

İkinci dalga senin akşam bloğuna, duran havuzun gönderim günleriyle aynı haftaya düşüyor. O hafta yüklüdür. Kural şu: akşam bloğu dolduysa sesli dalga on beşinci güne kayar, duran havuz kaymaz. Sebebi güvence: rapordaki üç sayının biri duran havuza bağlı.

Hangi işin hangi pencereye sığdığı ve işin yanında çalışanda takvimin ne kadar uzadığı musteriyi-karsila'da yazılı.

## 3. Ne okur

Bilgi dosyasından (İş Beyni'nin müşteriler bölümü; musteriyi-karsila'nın tuttuğu dosya): çalışma saatleri ve randevu saatleri, randevu uzunluğu, hizmet bölgesi, ortalama iş bedeli, talepleri arayacak kişi, bildirimlerin gideceği e-posta ve telefon, alınan izinler, müşterinin mevcut numarası, vergi ya da MERSİS numarası, ödeme almak istediği yol.
Niş kartından: asistanın toplayacağı bilgiler, işi insana devretme kuralları, asistanın söylemeyecekleri, "Sezon" bölümü, yoğun saatler için "Kanal ve zaman" bölümü, teklif verilen bir iş mi yoksa fiyatı sabit mi, yasal sınırlar.
yazili-asistani-kur'dan: asistanın ayar listesi (cevap gecikmesi, mesaj uzunluğu sınırı, asistanın kullanmayacağı kelimeler, sinirlenme algılanınca insana devir, mesai dışı davranışı).
sesli-ajani-kur'dan: sesli ajanın karşılama cümlesi, soru sırası, insana devir eşiği, konuşma sonunda dolduracağı alanlar.
İş Beyni'nden: Kademe 2'nin bu nişteki içeriği, [21/28] günün takvimi, güvence şartı ve şart geç geldiyse [21/28] günün kayan başlangıç tarihi.

## 4. Ne sorar

Sormaz. Ayarların değerleri karttan ve bilgi dosyasından gelir. Senden aldığı beş şey: her kurulum adımının bittiği ("tamam"), test sonuçları, iki dalganın canlıya alma onayı, müşterinin yönlendirme için yazılı onayı, telefon aboneliğinin açıldığı bilgisi.

Müşteriden istenen tek yeni belge var ve kurulum görüşmesinde istenir: vergi levhası. Telefon hattı müşterinin kendi adına açılıyor, sağlayıcı onu istiyor.

## 4c. Tamamlandı demek için

"Sistem teslim edildi" demek için kurulmuş olması yetmez:

1. Her parça test edilmiş: cevapsız aramaya mesaj gitti mi, asistan cevap verdi mi, randevu düştü mü, hatırlatma gitti mi; her testin tarihi ve sonucu yazılı.
2. Müşterinin gerekli onayları alınmış: metinler, çalışma saatleri, liste izni; yazılı.
3. Müşteri kendi telefonundan en az bir kere sistemi görmüş ve "çalışıyor" demiş; cümlesi kaydedilmiş.
4. Teslim kontrolü yapılmış: kapsam dışı kalan parçalar ve sebepleri müşteriye yazılı verilmiş.
5. Bakım işleri takvime girmiş: haftalık kontrol, aylık rapor.

Beşi tamam olmadan dördüncü aşama kapanmaz. Beşinci aşama, "müşterin kullanıyor", rapor günü raporunda üç sayının sıfır olmamasıyla kapanır.

## 5. Ne yapar

### Sıra

Birinci dalganın sırası sabittir: şablon onayları ve hat başvurusu, hazır paketin yüklü geldiğinin kontrolü, müşterinin kendi girişi, kanallar, formlar, takvim, ödeme, akışlar, özel değerler, bildirimler, sonuç ekranı, test.

Müşterinin girişi neden bu kadar başta: takvim ona bağlanıyor, asistanın insana devri ona bağlanıyor, müşterinin kendi bildirimleri ona bağlanıyor. Giriş bir gün gecikirse üç iş birden bekliyor.

İkinci dalganın sırası da sabittir: numara gelir, hat bilgileri desteğe gider, "hat bağlandı" gelir, sesli asistanın metni ve cevap listesi Voice AI ekranına yüklenir, çağrı olayı akışa bağlanır, on arama testi, yönlendirme müşterinin telefonundan açılır.

Akış, bir olay olunca kendiliğinden çalışan adım zinciridir; mesajı o gönderir.

Özel değerler birinci dalganın sonuna kalır, çünkü içinde takvim linki, ödeme linki ve onay sayfası adresi var; onlar da takvim ve ödeme kurulmadan belli olmaz. Sesli hattın numarası ikinci dalgada dolar.

Tek kural: paketin dışına çıkma. Senin işin ekleme yapmak değil, çalıştırmak. Değişecek yerler bellidir: mesaj metinleri, mesajı başlatan durumlar, hangi kanala bağlandığı. Paketin kendi yapısına dokunulmaz.

### Alt hesaptaki kayıt satırları

Bunları sen açmıyorsun. Müşterinin alt hesabı hazır paketten geliyor ve satırlar içinde kurulu; senin işin doğru satıra doğru şeyin yazıldığını görmek. Altı grup var:

Talep: talep kanalı (WhatsApp, Instagram, sohbet kutusu, Facebook, sesli ajan, cevapsız arama, form, telefon), talep tarihi, talep saati, dönüş süresi, kayıt kaynağı (sistem ya da dışarıdan), hizmet tipi, eski müşteri mi, arama sonucu.
Randevu: randevu tarihi, randevu sonucu (bekliyor, geldi, gelmedi, iptal), gelmeme sebebi.
Teklif ve ödeme: teklif tutarı, teklif tarihi, teklif durumu, ödeme durumu.
İzin: izin durumu, izin kaynağı, çıkma talebi tarihi.
Duran havuz: parti no, gönderim durumu, gönderim tarihi, son iş tarihi, havuz cevabı.
Yorum: yorum isteği durumu, yorum isteği tarihi.

Üç şey bilerek bu listede yok, çünkü CRM'in kendi kaydında zaten duruyor ve ikinci kez tutulursa ikisi birbirini tutmaz: randevunun onaylı mı olduğu (randevunun kendi durumu), notlar (kaydın kendi not bölümü), ve mesajların kendisi (konuşmalar ekranı). Sesli görüşmenin dökümü ve özeti de bu listede yok; onlar konuşmalar ekranına çağrı kaydı olarak düşüyor.

"Kayıt kaynağı" satırının ayrı bir işi var, atlanmasın: raporun randevu sayısına yalnız kaynağı "sistem" olan kayıtlar giriyor. Müşterinin kendi getirdiği iş ya da kapıdan giren müşteri elle açılırsa "dışarıdan" işaretlenir, yoksa rapor gerçekte olmayan bir sonucu sana yazar.

### Telefon tarafı: hat, numara, sesli ajan

Bu parça en çok soru çıkaran parça, o yüzden zinciri olduğu gibi yazıyorum. Dört halka var ve sırası değişmez.

Birinci halka, numara. Müşteri adına Türkiye'den 0850 ile başlayan bir numara alınır. Numara müşterinin kendi aboneliğinde durur, faturası ona gider, işi biterse numara onda kalır. Müşterinin mevcut numarasına dokunulmaz; ilan ettiği numara aynı kalır.

İkinci halka, hat. Bu numara sağlayıcının ses hizmeti üzerinden dışarıya açılır. Sağlayıcının panelinde bir bölüm var, hattın adresi, kullanıcı adı ve şifresi orada yazılı. O üç bilgiyi sen sohbete yazmazsın, ekranda göstermezsin, hiçbir yere kopyalamazsın: müşteri sağlayıcının panelinden o bilgileri müşteri bölümünün adıyla destek@founderos.so adresine kendisi gönderir (ya da sen onun yanında gönderirsin), FounderOS ekibi hattı müşteri bölümündeki sesli asistana aynı gün bağlar ve sana "hat bağlandı" yazar. Senin işin başvuruyu başlatmak, bilgilerin gittiğini teyit etmek ve testi yapmak.

Üçüncü halka, ajan. Sesli ajan CRM'in kendi telefon karşılama asistanıdır (ekranda Voice AI), müşteri bölümünün içinde durur; ayrı bir servis hesabı açılmaz, bağlantı anahtarı yok. Türkçe konuşur, karşılama cümlesini söyler, niş kartındaki soruları sorar ve takvimde boş saat görüp randevu yazar; metni sesli-ajani-kur'dan gelir ve Voice AI ekranına yazılır. Hat bağlanınca ajan kişiyi tanır, randevu yazar, erteler, iptal eder, kayda not düşer.

Dördüncü halka, yönlendirme. Müşterinin kendi telefonu, cevap verilmeyen aramayı bu 0850 numaraya yönlendirir. Bunu operatör kurar, müşteri kendi telefonundan yapar, adımları ekran paylaşımıyla birlikte yaparsınız. Yönlendirme üç durumda ayrı ayrı açılır: cevap verilmedi, meşgul, ulaşılamıyor. Üçü de açılmazsa aramaların bir kısmı kaybolur.

Sonuç şu: işletme telefonu açarsa hiçbir şey değişmez, konuşmayı insan yapar. Açmazsa arama otuz saniye içinde ajana düşer ve ajan konuşur. Arayan kişi tek numara biliyor, o da işletmenin kendi numarası.

Cevapsız aramaya dönüş bu zincirin üstüne oturur. Ajan konuşmayı bitirince ne olduğunu CRM'e yazar. Randevu yazıldıysa iş biter. Randevusuz bittiyse ya da arayan ajan açmadan kapattıysa akış çalışır ve müşterinin kendi WhatsApp hattından onaylı şablon gider. Yani arama 0850'ye düşer, yazılı dönüş müşterinin kendi numarasından gider; ikisi CRM'de aynı kayda bağlanır.

Dikkat: 0850 numaranın kendi yönlendirmesi kapalı kalır. İkisini birden açarsan arama kendi üstüne döner.

Google işletme profilindeki numara değiştirilmez. CRM'in Google profiline kendi numarasını koyan bir özelliği var; onu açarsan müşterinin asıl numarası geri plana düşer. Müşteriye "numaranıza dokunmuyorum" dedin, o yüzden açmıyoruz.

Giden arama ayrı bir mesele ve şarta bağlı. CRM'in sesli asistanı giden aramayı destekliyor, ama telefon sağlayıcısı giden aramayı bu hat üzerinden resmi belgede anlatmıyor. Sadece gelen arama belgeli. Bu yüzden giden arama ajanı ilk müşteride kurulmaz; sağlayıcıya sorulur, çalıştığı doğrulanırsa sonraki müşterilerde varsayılan olur. Doğrulanana kadar duran havuz yazılı gider, sesli gitmez. Bunu müşteriye ihtimal diye anlatma; sistemde şu an yazılı geri kazanma var, o kadar.

Telefon tarafının parası. Müşterinin cebinden çıkan: aylık hat paketi, numaranın yıllık kullanım ücreti ve giden arama yapılırsa dakika ücreti; rakamlar sağlayıcının o günkü tarifesinden, abonelik açılırken müşteriyle birlikte okunur ve bilgi dosyasına yazılır, buraya sabit rakam yazılmaz. 0850'ye gelen arama arayana ücretsizdir. Senin cebinden çıkan: sesli asistanın konuşma dakikası. CRM dakika başına ücretlendiriyor; rakamı müşteri bölümünün ücret ekranından okur, kâr hesabına "sesli dakika" satırı olarak yazarsın; ilk müşteride ölçülür, sahadan dolacak.

Tasarım kararı: hat müşterinin adına, ajan müşterinin CRM bölümünde. Sebebi iki taraflı. Numara müşterinin işine ait, ilişki biterse onda kalmalı. Ajan müşterinin bölümünde, çünkü müşterinin kayıtları, takvimi ve akışları orada; sen bütün müşteri bölümlerini kendi hesabından görüyor ve yönetiyorsun. Konuşma dakikasının parası senin aylık ücretinden çıkıyor; fiyat verirken bunu hesaba katarsın.

### SMS neden hiç yok

Sistemde SMS yok. Yedek olarak da yok. Üç sebebi var ve üçü de kalıcı: CRM'in numara verdiği ülkeler listesinde Türkiye görünmüyor, Türkiye'ye giden uluslararası kısa mesajlar link taşıyamıyor, ve gönderici kaydı zorunlu. Randevu hatırlatması bile link taşıdığı için bu yasak bizim işimizi doğrudan vuruyordu. Bütün yazılı iletişim WhatsApp'tan gidiyor. CRM'in hazır cevapsız arama özelliği de SMS attığı için kullanılmıyor; onun yerine yukarıdaki akış kuruluyor.

### Kanallar

Bağlanacaklar: WhatsApp (ana kanal), Instagram, sitedeki sohbet kutusu, Facebook sayfası mesajları. Dördü de aynı asistana bağlanır ve dördü de aynı ekrana düşer.

WhatsApp hangi numaraya bağlanır: müşterinin kendi WhatsApp Business hattına. Bağlantı yolu, ekranda "Coexistence" yazan seçenektir; o seçilince hat hem müşterinin telefonunda hem CRM'de aynı anda çalışır, numarası değişmez ve numara müşterinin kendi Meta işletme hesabında kalır. Sebebi basit: işletmenin müşterileri zaten o numaraya yazıyor. Bir alt hesaba tek WhatsApp numarası bağlandığı için ikinci bir numara bağlanmaz. Müşteri normal WhatsApp kullanıyorsa WhatsApp Business uygulamasına geçer; numarası aynı kalır.

Bu bağlantının satışta söylenmesi gereken bir bedeli var: kurulum bittikten sonra o numaradan WhatsApp araması yapılamıyor, grup sohbetleri ve toplu gönderim listeleri de kapanıyor. Müşteri o numarayla WhatsApp'tan arama yapıyorsa bunu kurulum görüşmesinde duyacak, kurulum gününde değil.

Google, Facebook ve Instagram izinleri karşılamada alınmıştır. WhatsApp bağlantısı ve bunun için gereken Meta hesabı izni bu bölümde, müşteriyle birlikte yapılır.

WhatsApp'ta iki kural var:
- İşletmenin müşterisi son yirmi dört saat içinde yazmadıysa ona ancak Meta'nın onayladığı hazır şablonla yazılabilir. Yani cevapsız aramaya dönüş, randevu hatırlatması, teklif takibi ve yorum isteği şablon olmak zorunda.
- Meta onayı olmayan hesapta günde iki yüz elli konuşma sınırı vardır. Bu müşteriye söylenir.

Google mesajlaşması kapandı, o kanal yok. Google'dan kalan iki iş: yorum linki ve yorum bildirimi.

Yazılı asistanın Türkçesi konusunda bir açık var: CRM'in asistanı dil ayarı sunmuyor, desteklediği diller de yayımlanmamış. Altyapısı dil modeli olduğu için Türkçe talimatla çalışması bekleniyor, ama beklenti kanıt değil. Bu yüzden birinci dalganın testinde asistanla Türkçe konuşulur ve çıkan cevaplar okunur. Bozuk cümle kuruyorsa iş yazili-asistani-kur'a döner.

### Formlar ve ön eleme

İki form kurulur ve ikisi de hazır pakette gelir. Birincisi sitedeki talep formu: ad, telefon, hizmet tipi, kısa açıklama. İkincisi karekodun açtığı form; karekod işletmenin duvarında ya da aracında durur.

Formun tek işi bilgi toplamak değil, ön elemek. Niş kartındaki eleme sorusu forma konur: hizmet bölgesi dışındaysa ya da iş tipi listede yoksa kayıt açılır ama randevu adımına gitmez, doğrudan insana düşer. Sebebi şu: elenmeyen talep randevu takvimini doldurur ve gelme oranını düşürür.

Form dolunca kayıt açılır, talep kanalı "form" yazılır ve asistan yazılı olarak devam eder. Yarım kalan form da kayıt açar; test senaryosunda bu var.

### Müşterinin kendi girişi

Hazır paket her şeyi getiriyor ama bir şeyi getirmiyor: müşterinin kendi kullanıcısını. Getiremez de, çünkü kullanıcı bir e-posta adresine bağlı ve o adres her müşteride başka.

Bu yüzden kurulumun ilk işlerinden biri müşteriye kendi girişini açmak. Alt hesap ayarlarında ekip bölümü var, oradan kullanıcı eklenir: ad, soyad, e-posta, cep telefonu. Sistem müşterinin adresine bir davet gönderiyor, şifresini o kendi belirliyor. Sen şifreyi görmüyorsun ve istemiyorsun; bu kural burada da değişmiyor.

Üç şey bu girişe bağlı ve o yüzden bunu erteleyemezsin:
1. Takvim. Randevu bir kişiye yazılıyor, kişi yoksa takvim kurulamıyor.
2. İnsana devir. Konuşma bir kişiye atanıyor, kişi yoksa devir kurulamıyor.
3. Müşterinin kendi panosu ve bildirimleri. Kendi hesabı olmayan müşteri sistemi göremez, göremediği sistemi de yok sayar.

Hangi adres kullanılır: işletmenin kendi e-postası. Karşılama formunda yazan adres. Müşteri "ben e-posta kullanmıyorum" derse yine de bir adres gerekiyor; kurulum görüşmesinde birlikte açarsınız, adres onun adına kalır.

İkinci bir kullanıcı gerekiyor mu: hayır. Talepleri arayacak kişi işletmecinin kendisinden başkasıysa ona da giriş açılır, ama bu isteğe bağlıdır ve ilk turda yapılmaz. Tek kullanıcıyla sistem çalışıyor.

Tasarım kararı: müşterinin girişi kurulumun birinci günü açılır, ikinci güne bırakılmaz. Sebebi: takvim ve devir bu girişe bağlı, ikisi de ikinci günün işi. Giriş bir gün geç açılırsa iki iş birden kayıyor.

### Takvim

Takvim hazır pakette gelmiyor, kurulumda sen açıyorsun. Sebebi yukarıda: takvim bir kişiye bağlanıyor ve o kişi her müşteride farklı. Açılışı kısa bir iş; asıl iş ayarlar.

Ayarlanacaklar: randevu uzunluğu, randevu aralığı, tampon süre (arka arkaya randevuyu engeller), randevunun en erken kaç saat sonrasına verilebileceği, aynı saate ve aynı güne düşecek randevu tavanı.

Çift randevu engeli tek ayar değildir: çakışma takvimi, tampon, en erken süre ve saat başına randevu tavanı birlikte çalışır. Müşterinin Google takvimi bağlanır ve iki yönlü çalışır: sistemde açılan randevu Google'a, Google'da açılan sisteme düşer. Bir uyarı: Google'da "meşgul" işaretli olmayan etkinlik randevu saatini kapatmaz. Test senaryosunda bu var.

Takvim iki yerden yazılır: yazılı asistandan ve sesli ajandan. İkisi de aynı takvime yazdığı için çakışma ayarları ikisini birden koruyor. Sesli ajan bağlandıktan sonra takvim ayarlarına dokunulmaz.

### Ödeme ve fatura

Ödeme linki CRM'den üretilir ve müşterinin kendi tahsilat hesabına bağlanır. İki kullanım var: randevuya kapora, ya da iş bitince tamamı. Hangisinin kurulacağı niş kartında yazılı; kapora almayan işte bu parça sadece iş sonu ödemesi olarak kurulur.

Link gidince kayıtta ödeme durumu değişir, ödeme gelince kendiliğinden "ödendi" olur. Fatura CRM'den kesilmiyor; faturayı müşterinin kendi düzeni kesiyor. Sistemin işi ödemenin geldiğini kayda yazmak ve müşteriye haber vermek.

Bir şeyi karıştırma: burada üretilen link müşterinin alt hesabında, müşterinin tahsilat hesabına bağlı. Senin kendi tahsilatın ayrı; onu kendi hesabından üretiyorsun.

### Akışlar

Bir şeyi kurulumdan önce bil, yoksa ilk müşteride şaşırırsın. Hazır pakette mesaj adımları e-posta olarak geliyor, WhatsApp olarak değil. Sebebi CRM'in kendi kuralı: WhatsApp adımı kurulurken onaylı bir şablon seçmek zorunlu ve şablon ancak hattı bağlı olan hesapta görünüyor. Paketin hazırlandığı hesapta hat yok, o yüzden orada WhatsApp adımı hiç kaydedilemiyor.

Sonuç senin için tek bir işe dönüşüyor ve atlanmaz: hat bağlanıp şablonlar onaylandıktan sonra, her mesaj adımının yanına WhatsApp adımını sen eklersin ve e-posta adımını kapatırsın. Hangi adımların bu işi beklediği adının sonundaki "(WhatsApp'a çevrilecek)" ibaresinden belli. Şablon onayı gelmemiş bir mesaj için e-posta adımı açık kalır; o mesaj o hafta e-postadan gider, kayıp olmaz.

Randevu akışı: yeni randevu, CRM'de aşama, işletmeye iç bildirim, randevu alan kişiye onay mesajı, hatırlatma yirmi dört saat ve bir saat kala, randevudan bir saat sonra sonuç sorusu. "İş bitti" tarihi tek tanımdır ve iki parçadan dolar: randevu durumu "geldi" olur (bunu işletme, randevudan sonra kendisine giden iç bildirime "geldi" ya da "gelmedi" diye cevaplayarak işaretler; arayana giden mesaj değildir) ve işletme aynı iç bildirimde "bitti" der; nişin karttaki "iş bitti" anı (koltuktan kalkınca, araç teslimi, albüm teslimi gibi) bu "bitti" işaretinin ne zaman verileceğini söyler. Yorum isteği, tekrar randevu ve ek hizmet zincirlerinin üçü de bu tarihten sayar, başka bir tetik kullanmaz. Teklif yolunda aynı alan "ödeme alındı ve iş teslim edildi" işaretiyle dolar. Arayana giden sonuç sorusu ("nasıl geçti?") ayrı bir mesajdır ve yorum isteği giden kişiye aynı gün gitmez (yorum-topla). Gelme oranı ve raporun gelen randevu satırı işletmenin "geldi" işaretinden çıkar.

Gelme oranı, randevu alanların kaçının gerçekten geldiğidir. Ölçüt yüzde yetmiştir. Altındaysa sorun randevuda değil, hatırlatma akışındadır.

Saatler: iç bildirim ve onay mesajı 09.00-21.00 arası, hatırlatmalar kendi saatinde. Bunlar müşterinin sisteminin saatleridir, senin çalışma pencerelerinle ilgisi yoktur.

Çağrı akışı: sesli ajan konuşmayı bitirince olay CRM'e düşer, kişi telefondan eşleştirilir, yoksa açılır, çağrı kayda yazılır. Randevu yazılmamışsa yazılı dönüş gider. Aynı kişiye aynı gün ikinci dönüş gitmez, gece gelen arama ertesi gün 09.00'da cevaplanır. Tekrar koruması ve gece penceresi hazır özellikte yok; ikisini de akışa biz koyuyoruz.

Altmış saniye akışı: her yeni talepte dönüş süresi ölçülür. Yazılı kanallarda asistan zaten anında cevap veriyor, ölçüm asıl formda ve telefonda anlam kazanıyor. Altmış saniye aşılırsa kayda işaret düşer ve haftalık kontrolde sayılır. Bu bir mesaj göndermiyor, ölçüyor; ölçülmeyen şey düzelmiyor.

Teklif takibi akışı: teklif durumu "verildi" olunca zincir başlar. Teklif belgesi kayda önce yüklenir: işletmenin onayladığı PDF ya da fotoğraf kişinin kaydına "teklif" alanına eklenir, akış o dosyayı gönderir; dosya yoksa akış başlamaz ve işletmeye "teklif belgesi eksik" bildirimi gider. Üç dokunuş var ve günleri yazili-asistani-kur'daki zincirle aynıdır: aynı gün teklif gönderildi mesajı ve "sorunuz var mı", iki gün sonra soru, beş gün sonra son mesaj. Cevap gelirse zincir durur, kabul ya da ret işaretlenir. Cevap gelmezse kayıt duran havuza düşer, çünkü orada zaten sırası var.

Bildirim yükseltme akışı: talebe otuz dakika içinde dönülmezse ikinci bildirim gider, iki saat içinde dönülmezse müşterinin kendisine gider. Sayaç yalnız müşterinin çalışma saatleri içinde işler; saat dışında gelen talep ertesi iş günü 09.00'da birinci bildirimden başlar.

Yorum akışı: iş bitince yorum isteği, cevap yoksa üç gün sonra tek hatırlatma. Gelen yoruma yanıt ise ayrı çalışır: CRM'in yorum yanıtlama özelliği açılır, önce öneri getiren modda kurulur, yani yanıtı sistem yazar müşteri onaylar. İki hafta sorunsuz gittikten sonra düşük yıldızlılar hariç tam otomatiğe alınır. Düşük yıldızlı yorum hiçbir zaman otomatik yanıtlanmaz, müşteriye düşer. Yanıtların Türkçesi ilk haftada okunarak kontrol edilir; desteklenen diller yayımlanmamış.

Duran havuz akışının boruları kurulur; metinleri ve gönderimi kaybolanlari-geri-getir'in işi.

### Pano

Müşteri kendi alt hesabına girince karşısına bir ekran çıkar ve dört şeyi görür: bu ay gelen talep, yazılan randevu, gelen randevu, bekleyen iş. Panonun kurulmasının sebebi rakam değil, güven: müşteri sistemin çalıştığını görmezse ayın sonunu beklemeden çalışmadığını düşünür.

Pano hazır pakette gelir. Senin işin müşterinin kullanıcısını doğru ekrana açmak ve ilk girişini onunla birlikte yapmak. Aylık raporun ekranı da burada açılır; içeriğini ve gönderimini aylik-raporu-hazirla yürütür.

### Bildirimler: müşteri görmezse sistem yok sayılır

Üç adım: müşteri alt hesaba kullanıcı olarak eklenir (kısıtlı yetki, kurulum görüşmesinde açılmıştı), kendi profilinden bildirimleri açar, telefonuna uygulamayı kurar. Bu üçü yapılmazsa sistem çalışır ama müşteri hiçbir şey görmez.

Bildirim kanalları: uygulama, e-posta, WhatsApp. Talepleri arayacak kişi de eklenir; adı karşılama formunun yedinci sorusunda.

### Beşinci gün: üç sorulu test

Üç soru:
1. Teknik çalışıyor mu. Sistemi zorlayan uç örnekleri kasten denersin: yarım kalan form, saat dışı mesaj, bağlantı hatası. Hataları müşteriden önce sen bulacaksın.
2. Kullanması iyi mi. Kuranın gözünden değil, kullananın gözünden denenir.
3. Randevuya çeviriyor mu. En çok atlanan soru budur. Somut tuzak şu: asistan her soruya öyle güzel cevap verir ki kimse randevu almaz. O zaman sistem satışı engelliyordur.

Geçme ölçütü tek cümle: "Müşteriye, söz verdiğim sonucu bu sistemin nasıl getirdiğini anlatabiliyor muyum?" Cevap hayırsa hazır değildir.

Yöntem: uçtan uca çalıştır, kötü örnekleri dene. Çalışmıyorsa teslim edilmez. Özel değerler ekranındaki satırlar dolmadan test etme.

Testleri kendi adın ve kendi telefonunla açtığın tek bir kayıt üzerinden yaparsın. Müşteriye giden bildirimleri kapalı tutarsın; yalnız "müşteriye bildirimin ulaşması" senaryosunun son üç turunda açarsın.

Birinci dalganın on dört senaryosu, toplam otuz iki tur. Her senaryo bir tur; kritik dördü (randevu alma, hatırlatma, teklif takibi, müşteriye bildirim) beş tur:
- WhatsApp'tan yeni müşteri,
- Instagram'dan yeni müşteri,
- sohbet kutusundan yeni müşteri,
- Facebook mesajından yeni müşteri,
- form dolduran müşteri,
- yarım kalan form,
- bölge dışından gelen talep (eleme çalışıyor mu),
- randevu alma,
- aynı saate ikinci randevu denemesi,
- Google'da "meşgul" işaretli olmayan etkinlik,
- randevu iptali,
- hatırlatmaların gelmesi,
- teklif verildi, cevap gelmedi,
- müşteriye bildirimin ulaşması.
Artı iki dil kontrolü: asistanın bilmediği soru ve insana devir, fiyat sorusu (asistan fiyat vermez).

İkinci dalganın altı senaryosu, toplam on dört tur. Kritik ikisi (ajanın randevu yazması, cevapsız aramaya dönüş) beş tur:
- işletme açmıyor, arama ajana düşüyor,
- ajan randevu yazıyor,
- arayan ajan açmadan kapatıyor,
- konuşma randevusuz bitiyor, yazılı dönüş gidiyor,
- mesai dışı arama,
- ajanın anlamadığı istek ve insana devir.

Sağlık nişlerinde ek kontrol: hatırlatma dili hastanın kendi tedavisine bağlanır; kampanya dili ve hasta yorumu kullanılmaz. Sesli ajanın konuşmasında da aynı sınır geçerli.

### Canlıya alma ve teslim

Her dalganın kendi canlıya alması var, sırası aynı: önce giden mesajlar ve bildirimler, sonra gelen kanallar, en son yönlendirme. Ters sırada açarsan ilk randevular onay mesajı ve hatırlatma almadan kalır.

Yönlendirmeyi müşteri "açalım" yazınca açarsın. İkinci dalganın canlıya alma gününün sabah bloğunda tek cümleyle sorarsın. Akşama kadar yazılı cevap gelmezse kalan parçaları canlıya alırsın, yönlendirmeyi cevap gelince açarsın.

Canlıya alma anahtarı bellidir ve kapatma yolu aynı yerdedir; geri alma iki dakikalık iştir.

Yayına aldıktan sonra ayarla oynanmaz.

Teslim paketi altıncı günde müşteriye gider: kişiye özel olmayan, ekiple paylaşılabilir kısa video (ne yapar, nasıl değiştirilir, bozulursa ne yapılır) ve yazılı rehber, üstüne teslim mesajı. Video ve rehber hazır pakette gelir; sen sadece müşterinin adını yazarsın. Sesli taraf canlıya alınınca ikinci kısa video gider.

Her canlıya almadan sonraki yirmi dört saat izlenir. Bir şey bozulursa sıra şu: sahiplen, saatler içinde haber ver, aynı gün düzelt, kaçan talepleri elle ara, izlemeyi sıkılaştır.

### Kapsam dışı bırakılan her parça

Bir parça kurulamadıysa (izin yok, onay gelmedi, hat açılmadı) o parça kapsam dışına alınır ve aynı gün müşteriye yazılı bildirilir: ne çalışmıyor, sebebi ne, ne zaman bakılacak. Sessizce atlanmaz.

Kural şu: kurulamayan parça kapsam dışıdır ve güvencenin sonucuna sayılmaz. Raporda o satır boş kalır, sıfır yazılmaz. Bunun sebebi kaçamak değil dürüstlük: kurulmamış bir parçanın sonucu ölçülemez.

Söylenme anı ikiye ayrılır ve ikisi de kaçırılmaz.

Birincisi, ihtimalin söylendiği an: kurulum görüşmesi. Güvencenin şartını anlatırken bu ihtimal sesli söylenir ve onay belgesinin "neyi yapmıyorum" başlığında yazılı durur. Yani müşteri bunu ilk kez kötü haberle duymaz.

İkincisi, gerçekten olduğu an: o parçanın kurulamadığını anladığın gün, beklemeden. Ertesi güne bırakmazsın, canlıya alma gününü beklemezsin, rapora saklamazsın. Cümle şudur ve bundan uzun yazılmaz:

"Bugün [şu parça] kurulamadı. Sebebi [şu]. Bu parça ilk turda kapsam dışında kalıyor, rapor gününün raporunda o satır boş görünecek ve güvencenin hesabına girmeyecek. Kalan parçalar takvimde, tarih kaymıyor. [Şu] tamamlanırsa ikinci turda kurarım."

Köşeli parantezleri sen doldurursun. Üç şey yazmazsın: bahane, suçlama, ve "belki olur" diye açık kalan bir söz. Sebep müşterinin kendi adımıysa (izin vermedi, liste gelmedi) bunu suçlar gibi değil, tabloyu okur gibi yazarsın.

Kapsam dışı kalan her parça bilgi dosyasına sebebiyle geçer. Rapor gününün raporunda sayfanın en üstündeki kutuya bir kez yazılır.

### Ekran yolları

Hazır paketin yüklü geldiğini kontrol: alt hesap ayarlarında akışlar, şablonlar ve aday hattı görünüyor mu; görünmüyorsa destek@founderos.so'ya yazılır, sen yüklemezsin.
Özel değerler: ayarlar, özel değerler. On dört satır ve biçimleri: iş adı ("Yılmaz Klima"), sahibin adı ("Ahmet Yılmaz"), ofis telefonu ("+905321234567"), bildirim e-postası, bildirim cep telefonu ("+905321234567"), site adresi ("https://..."), çalışma saatleri ("09.00-18.00"), hizmet bölgesi ("Nilüfer, Osmangazi"), vergi ya da MERSİS numarası ("1234567890"), takvim linki ("https://..."), onay sayfası adresi ("https://..."), yorum linki ("https://..."), ödeme linki ("https://..."), sesli hat numarası ("+908501234567"). İlk dokuzu kurulumun ikinci gününde dolar; takvim linki ve onay sayfası takvim kurulunca, yorum linki Google profili açılınca, ödeme linki tahsilat bağlanınca, sesli hat numarası ikinci dalgada. Vergi ya da MERSİS numarası isteğe bağlı değil: her toplu mesajın altındaki tanıtım satırı onu kullanıyor, boşsa o satır eksik gider. Yanlış yazılan tek satır bütün akışları bozar.
Müşterinin girişini açma: alt hesap ayarları, ekip, kullanıcı ekle. Ad, soyad, e-posta, cep telefonu yazılır, kaydedilir. Davet müşterinin adresine gider, şifresini o belirler.
Takvimi açma: takvimler bölümü, yeni takvim, tek kişilik randevu türü. Ad ("Randevu"), takvimin bağlanacağı kişi (müşterinin kendi kullanıcısı), randevu uzunluğu. Kaydettikten sonra ayarlara girip tampon süre, en erken saat ve saat başına tavan yazılır.
Yazılı asistanı açma: yapay zeka bölümü, yazılı asistan, asistanı aç, hal seçilir (kapalı, öneri, otomatik). Hazır paket kapalı geliyor; canlıya alırken otomatik yapılır. Aynı ekranda hangi kanallarda çalışacağı seçilir.
Asistanın kişi kartına yazması: aynı ekranda işlemler bölümü, kişi bilgisi işlemi. Hazır pakette iki satır bağlı geliyor (istenen iş ve ilçe); sen dokunmuyorsun.
Asistanın insana devri: aynı ekranda işlemler bölümü, insana devret. Burada konuşmanın atanacağı kişi seçiliyor; o kişi müşterinin kendi kullanıcısıdır ve bu yüzden giriş açılmadan bu adım kurulamaz.
Yorum linki: müşterinin Google işletme profili, "yorum iste", çıkan linki kopyala.
Yorum yanıtlama: itibar bölümü, yapay zeka yanıtları, önce öneri modu, yıldız sayısına göre ayrı yanıt, düşük yıldızlılar elle.
Çakışma takvimi: takvim ayarlarında bağlı takvim seçilir, müşterinin Google takvimi işaretlenir.
Ödeme: ödemeler bölümü, tahsilat hesabı bağlanır, ürün olarak hizmet açılır, link üretilir.
Sohbet kutusu: siteler bölümü, sohbet kutusu, kodu kopyala, müşterinin sitesine yapıştır. Site müşterinin elinde değilse kutunun kodu sitesini yapan kişiye gider.
Sesli hat: hat bilgileri sağlayıcının panelinde; müşteri o bilgileri müşteri bölümünün adıyla destek@founderos.so adresine gönderir, FounderOS ekibi hattı müşteri bölümündeki sesli asistana bağlar ve sana "hat bağlandı" yazar. Sen bilgileri görmez, yazmaz, kopyalamazsın.
Ajanın CRM bağlantısı: alt hesap ayarları, bağlantı anahtarı açılır (kişiler, fırsatlar, alanlar, takvim yetkileriyle), anahtar ve alt hesap kimliği ajan servisine girilir.
Çağrı olayının CRM'e düşmesi: akışta gelen bağlantı tetikleyicisi kurulur, ajan servisinden gelen olay oraya bağlanır, akış önce kişiyi telefondan bulur ya da açar, sonra çağrıyı kayda yazar.
İç bildirim: akışa iç bildirim adımı eklenir, alıcı olarak müşteri ve talepleri arayacak kişi, kanal uygulama ve e-posta.
Müşterinin bildirimleri: müşteri alt hesaba girer, ayarlar, kendi profili, bildirimler; yeni mesaj, yeni randevu ve yorum bildirimlerini açar. Sonra telefonuna CRM uygulamasını kurar ve aynı hesapla girer.

Senin bildirimlerin: üç tanesi kapalı gelir ve kurulumda sen açarsın, yoksa sistem sessizce bozulur ve haberin olmaz.
1. Akış hatası bildirimi: akışlar listesi, akış ayarları, bildirim anahtarı. Alıcı listesine kendini eklersin. Günde bir toplu e-posta gelir. Uyarı: bu bildirim WhatsApp gönderimini ve takvim adımlarını kapsamıyor, o yüzden haftalık kontrolde akış hatalarına elle de bakılır.
2. Sosyal hesap bildirimleri: pazarlama, sosyal planlayıcı, dişli simgesi, bildirimler. Açılacak üç tür: hesap süresi doldu, süre dolmadan uyarı, gönderi başarısız. Facebook ve Instagram bağlantısının süresi doluyor; ön uyarı ellinci gün civarında geliyor.
3. Takvim bildirimleri: kendi profilim, bildirimler, takvim. E-posta ve uygulama anahtarları açık olacak. Ama bir boşluk var: takvim kopunca bildirim yalnız takvimin sahibine gidiyor, alt hesap ya da ajans yöneticisine gitmiyor. Bu kapatılamıyor. Bu yüzden takvimi hangi hesaba bağladığını bilgi dosyasına yazarsın ve müşteriye şunu yazılı söylersin: "Takvim bağlantısı koptu diye bir e-posta gelirse bana ilet."

Dört şey daha kurulumda yapılır ve haftalık bakımın ön şartıdır:
- Meta'nın WhatsApp yönetim ekranına girebildiğini test edersin, kurulum günü, ertelemeden. Hattın kalite notu ve günlük mesaj sınırı CRM'de değil, orada. Numara müşterinin kendi Meta işletme hesabında durduğu için panel normalde açılır. Açılmıyorsa bunu arıza sayma: bilgi dosyasına "kalite paneli yok" diye yazarsın, müşteriye tek cümleyle söylersin, ve haftalık kontrolün o iki maddesi yerine yedek ölçüye geçersin: CRM'deki konuşmalar ekranında giden şablon mesajların teslim edilmeyen sayısı ve hafta içinde gelen engelleme ya da şikâyet bildirimi. Bu ikisi kalite notunun aynısı değildir, ama aynı yöne bakar: hat sıkıntıya girdiğinde ikisi de kıpırdar.
- Şablonları yalnız CRM içinden açarsın. Kurulumdan sonra Meta'nın kendi ekranından şablon açılmaz.
- Ayarların başlangıç değerlerini bilgi dosyasına yazarsın: on dört özel değer satırı, randevu uzunluğu, aralık, tampon süre, en erken saat, saat başına randevu tavanı, asistan ayarları, sesli ajanın ayarları. Karşılaştırma tabanı olmadan "bir ayar değişmiş mi" sorusu cevaplanamaz.
- Haftalık kontrol gününü belirler ve bilgi dosyasına yazarsın: ilk ayda haftalık görüşmeden bir gün öncesi.

Bir de WhatsApp bağlantısının bir tuzağı var: bağlantı kurulduktan sonra yirmi dört saatlik bir eşleşme süresi işliyor. O süre kaçarsa numara sistemden çıkarılıp bağlantı baştan kurulmak zorunda kalıyor. Bu yüzden WhatsApp bağlandığı gün test edilir, ertesi güne bırakılmaz.
WhatsApp şablonu: metin hazır pakette gelir, müşteri yazılı onaylar, CRM'den Meta onayına gönderilir. Onayın kaç gün süreceği belli değildir; o yüzden kurulum görüşmesinin yapıldığı gün gönderilir. Reddedilirse metin sadeleştirilip aynı gün yeniden gönderilir.
Mesaj adımını WhatsApp'a çevirme: akışı aç, "(WhatsApp'a çevrilecek)" yazan adımın altına WhatsApp adımı ekle, onaylı şablonu seç, sonra e-posta adımını kapat. Şablon listesi boş görünüyorsa şablon henüz onaylanmamıştır; adımı kurmadan önce onayı bekle.
Canlıya alma: alt hesapta akışların listesi, her akışın yanındaki anahtar açılır. Kapatmak için aynı anahtar kapatılır.
Yönlendirme: müşterinin telefonundan operatör ayarıyla kurulur. Üç durum ayrı ayrı açılır: cevapsız, meşgul, ulaşılamıyor. Kodları operatör veriyor, müşteriyle birlikte operatörün uygulamasından yaparsınız.

### Yapma listesi

Fazla kurma, paketin dışına çıkma. Yeni araç ekleme; elle yapılan her devir bir kırılma noktasıdır. Müşterinin çalışan sistemine dokunma. Kod yazma. Yayına girdikten sonra ayarla oynama. Google profilindeki numarayı değiştirme. Müşterinin ilan ettiği numarayı değiştirme. Sesli ajanı yazılı asistanın yerine koyma; ikisi yan yana çalışır. Giden aramayı doğrulanmadan kurma. Test etmeden teslim etme.

## 6. Ne söyler

İkinci gün: "Bugün birinci dalga: kanallar, formlar, takvim, ödeme, akışlar, özel değerler, bildirimler, sonuç ekranı. Sesli taraf ikinci dalgada, çünkü hat dışarıdan geliyor. Şablon onaylarını ve hat başvurusunu dün başlattık. Paketin dışına çıkma; senin işin ekleme yapmak değil, çalıştırmak."
Beşinci gün: "Bugün üç soru var. Çalışıyor mu, kullanması iyi mi, randevuya çeviriyor mu. Üçüncüsü en çok atlanan soru: asistan her şeyi güzel anlatıp randevu almıyorsa sistem satışı engelliyor demektir."
Test bitince: "Tek soru: müşteriye, söz verdiğin sonucu bu sistemin nasıl getirdiğini anlatabiliyor musun? Hayırsa canlıya almıyoruz."
Altıncı gün: "Birinci dalgayı canlıya alıyoruz. Bugünden sonra ayarla oynamak yok. Yirmi dört saat izliyoruz; bozulursa saatler içinde haber verir, aynı gün düzeltirsin."
Hat gelince: "Hat bağlandı. Sıra sabit: asistanın metni, çağrı olayı, on arama testi, en son yönlendirme. Yönlendirmeyi müşteri 'açalım' yazınca açıyorsun."
Bir parça kurulamayınca: "Bugün o parçayı kuramadık, sebebi belli. Aynı gün müşteriye yazacaksın: kurulamadı, sebebi bu, raporda satırı boş kalacak, güvencenin hesabına girmeyecek, tarih kaymıyor. Bunu ihtimal olarak kurulum görüşmesinde zaten söylemiştin; bugün olan şeyi söylüyorsun, yeni bir kötü haber vermiyorsun."
Müşteri parça çıkarmak isterse: "Sen tek tek parça satmıyorsun, sistem satıyorsun. Bir parçayı çıkarınca fiyat düşmüyor, sonuç düşüyor. Bütçe konuşacaksak kademeyi konuşuruz, parçayı değil."

## 7. Ne yazar

Bilgi dosyasına: kurulan parçalar ve tarihleri, 0850 numara, başvuru tarihi ve "hat bağlandı" tarihi (kullanıcı adı, şifre, adres asla), aylık telefon maliyeti ve teyit tarihi, yönlendirmenin hangi durumlar için açıldığı, onaylanan şablonlar, takvim ayarları, ödeme yolu, iki dalganın test sonuçları (hangi senaryo kaç turda temiz çıktı), kapsam dışı kalan parçalar ve sebepleri, canlıya alma saatleri, teslim paketinin yeri.
CRM'e: teslimat aşaması (kurulum, test, canlı), randevu ve mesaj sayıları.
Niş kartının Sahadan dolacak bölümüne: bu nişte randevu süresi, yoğun saatler, asistanın en sık takıldığı soru, sesli ajanın en sık takıldığı istek, hatırlatma saatlerinin gelme oranı, teklif takibinin kaçıncı dokunuşta cevap getirdiği.
Her kurulum gününün tek satırı ve tek görüntüsü musteriyi-karsila'ya teslim edilir; müşteriye onu o modül gönderir.

## 8. Yedek yol

- Şablon onayı gecikirse: kurulum devam eder, canlıya alma o parça olmadan yapılır, parça onay gelince açılır. [21/28] gün durmaz.
- Hat ya da numara gecikirse: birinci dalga zaten canlıda, ikinci dalga on beşinci güne kayar. Müşteriye kayma gününde yazılı bildirilir.
- Hat hiç açılamazsa (abonelik reddi, belge eksiği): sesli ajan ve cevapsız aramaya dönüş kapsam dışı kalır, müşteriye yazılı bildirilir. Gelen kanallar sistemi yine taşır.
- Yönlendirme kurulamıyorsa: sesli ajan yalnız 0850 numarayı doğrudan arayanları karşılar, bu numara da ilanda kullanılmaz; pratikte parça kapsam dışıdır ve öyle bildirilir.
- Giden arama doğrulanamazsa: duran havuz yazılı gider, o kadar. Bu bir arıza değil, kapsamın kendisi.
- WhatsApp bağlanamıyorsa: gelen kanal Instagram, sohbet kutusu ve Facebook'la sınırlı kalır, hatırlatmalar e-postadan gider. Cevapsız aramaya yazılı dönüş de kapsam dışı kalır, çünkü o mesaj WhatsApp şablonuyla gidiyor. Hepsi müşteriye yazılı bildirilir.
- Asistan Türkçe konuşmakta zorlanıyorsa: iş yazili-asistani-kur'a döner, metin sadeleştirilir. Düzelmezse yazılı asistan insana devir moduna alınır, yani karşılar ve hemen aktarır; parça kapsam dışına alınmaz ama sınırı müşteriye söylenir.
- Ödeme tahsilatı bağlanamıyorsa: ödeme linki parçası kapsam dışı kalır, müşteri kendi yolundan tahsil eder, kayda elle işlenir.
- Üçüncü soru geçilemiyorsa (asistan randevuya çevirmiyor): canlıya alınmaz, iş yazili-asistani-kur'a döner, asistanın görev bölümü düzeltilir.
- Müşterinin takvimi bağlanamıyorsa: sistemin kendi takvimi kullanılır, müşteri ona bakar.
- Canlıda bir şey bozulursa: anahtarı kapat, müşteriye saatler içinde haber ver, aynı gün düzelt, kaçan talepleri elle ara.

## 9. Sıradaki adım ve işaretler

Sıradaki: yedinci gün duran havuz onayı, sekizinci gün kaybolanlari-geri-getir, aynı hafta ikinci dalga. Haftalık kontrolü sistemi-kontrol-et devralır.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Dördüncü gün bitti, birinci dalga bitmedi: şablon dışındaki eksik parça kapsam dışına alınır, test ve canlıya alma günü kaymaz.
- Testte aynı senaryo iki kez düştü: o dalganın canlıya alması durur.
- Canlıya alındı, ilk yirmi dört saatte hiç mesaj gelmedi: yönlendirme ve kanal bağlantısı kontrol edilir.
- On dördüncü gün bitti, hat gelmedi: ikinci dalga on beşinci güne yazılır, müşteriye aynı gün bildirilir.
- Sesli ajan açtı ama randevu yazmıyor: iş sesli-ajani-kur'a döner, ajanın takvim bağlantısı ve görev bölümü kontrol edilir.
- Hatırlatma akışı kurulu ama gelme oranı yüzde yetmişin altında: akış düzeltilir.
- Altmış saniye işareti bir haftada üç kez düştü: eleme sorusu ve bildirim yükseltmesi kontrol edilir.
- Müşteri bildirimleri görmüyor: kullanıcı, profil bildirimi ve uygulama üçlüsü kontrol edilir.

Beş kural: boş sayfa yok (paket, ayar değerleri, şablon metinleri, teslim videosu ve test senaryoları hazır gelir) · sessiz bitiş yok (her kurulum gününün tek satırı ve tek görüntüsü musteriyi-karsila'ya teslim edilir) · onay (canlıya almayı sen "tamam" dediğinde yaparız, yönlendirmeyi müşteri "açalım" dediğinde açarız) · sahadan güncelleme (randevu süresi, yoğun saat, sık takılan soru karta yazılır) · sormaz söyler (sırayı ve ayarları FounderOS verir).
