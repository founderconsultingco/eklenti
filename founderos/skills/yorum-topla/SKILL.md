---
user-invocable: false
name: yorum-topla
description: "Müşteride yorum isteme ve yorum yanıtlama."
---

# yorum-topla

## 1. Adı, rolü, pazarlamadaki karşılığı

İşi biten kişiden Google yorumu isteyen ve gelen yorumları yöneten modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Görüşmede sattığın tam sistemin, yani Kademe 2'nin parçalarından biridir. Kademe 2, Kademe 1'in üstüne üç iş ekler: eski müşterileri geri arama, Google yorumu toplama, aylık rapor. Bu modül ikincisini yapar.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil.

Dil ayrımı: "müşteri" senin paranı ödeyen işletmedir. Yorum yazacak kişiye "işletmenin müşterisi" diyoruz.

Neden bu iş var: memnun müşteri kendiliğinden hiçbir şey yazmıyor, memnun olmayan şikâyet sitesine yazıyor. Düğün kartındaki cümle bunu tam anlatıyor: memnun çift referans getirmiyor ama memnun olmayan şikâyet sitesine yazıyor. Yani işletmenin internetteki yüzü, sadece kızgın insanların yazdıklarından oluşuyor.

İkinci sebep: insanlar satın almadan önce yoruma bakıyor. Oto galeri kartında bir alıcı, yorumlar yüzünden o galeriden araç almaktan vazgeçtiğini anlatıyor.

Üçüncü sebep: müşteri sana parayı yeni ödedi. İlk hafta görünür bir kazanım çıkarmak pişmanlığı düşürür, yorum bunun en hızlı yolu.

Şunlar bu modülün işi değildir:
- Google yönetici izni almak (musteriyi-karsila).
- Yorum linkini sisteme yazmak, yorum bildirimini açmak (musteri-sistemini-kur).
- Eski müşteri listesine mesaj göndermek (kaybolanlari-geri-getir). Bu iki iş karıştırılmaz.
- Aylık rapor (aylik-raporu-hazirla).
- Senin kendi referansın ve kanıt hikâyen. O ayrı bir iş.

Pazarlamadaki karşılığı: işletmenin bir daha kaybetmediği itibar. Google'ın mesajlaşma kanalı kapandı; Google'dan elimizde kalan iki şey yorum linki ve yorum bildirimi.

## 2. Ne zaman çalışır

- Kurulum görüşmesinin yapıldığı gün: yorum isteği şablonu diğer şablonlarla birlikte onaya gider. Bunu musteri-sistemini-kur yürütür.
- İkinci günden dördüncü güne: yorum linki ve QR kodu alınır, metinler müşteriye onaya gider, QR kodun basılıp nereye asılacağı kararlaştırılır. Link ve metin işi akşam bloğunda yapılır; QR kodun yeri müşteriyle konuşulacağı için kurulum bloğuna girer, çoğunlukla haftalık görüşmenin içinde.
- Altıncı gün canlıya alma sonrası: işi biten her kişi için istek çalıştırılır. Hangi yolun açık olduğu aşağıdaki kurallara göre belirlenir.
- On üçüncü günden sonra: WhatsApp yolu açılabilir. Daha önce açılmaz, çünkü sekizinci günden on ikinci güne kadar hattın günlük yerinin çoğu eski müşteri listesinin ilk mesajlarına ayrılmıştır. O günlerde hatta yalnız randevu hatırlatmaları ve cevapsız aramaya dönüşler için yer kalır.
- Yirmi birinci gün: rapora yorum satırı girer.
- Sonrası: haftalık kontrolde yeni yorumlar okunur, cevapsız yorum bırakılmaz (sistemi-kontrol-et).

Eski müşteri listesine yorum isteği gönderilmez. O listeye giden mesaj ayrı bir iştir ve ikisi birbirine karışmaz.

## 3. Ne okur

Bilgi dosyasından (İş Beyni'nin müşteriler bölümü; her müşteri için tuttuğun geniş dosya): Google işletme profilinin doğrulanmış olup olmadığı, yorum linki ve QR kodu, müşterinin çalışma saatleri, izin durumu.
Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): işin bittiği an için Sahadan dolacak bölümü, yasal sınırlar, yorumlarda en çok neyin konuşulduğu, işletmecinin kendi kullandığı cümleler.
CRM'den (adayların ve müşterilerin kaydedildiği takip programı): kapanmış randevular, gelen yorum bildirimleri.
İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı dosya): yirmi bir günün takvimi, sistemin adı.

## 4. Ne sorar

Sormaz. İstek anını karttan, kimden isteneceğini CRM'den çıkarır.

Senden aldığı üç şey: müşterinin metne yazılı onayı; QR kodun basılıp asıldığı haberi; kötü yorum geldiğinde müşterinin cevap onayı.

## 5. Ne yapar

### Google'ın iki yasağı, işin şeklini belirliyor

Google kendi sayfasında iki şeyi açıkça yasaklıyor.

Birincisi teşvik: yorum yazması, yorumunu değiştirmesi ya da kötü yorumunu silmesi karşılığında ödeme, indirim, hediye ya da ücretsiz hizmet teklif etmek. Google'ın kendi ifadesi "kesinlikle yasak".

İkincisi yorum ayıklama, yani yorumları eleyip yalnız iyilerini toplamaya çalışmak. Google'ın yapılmaması gerekenler listesinde "müşterilerden özellikle olumlu yorum yazmalarını istemek" ve "olumsuz yorumları engellemek ya da yasaklamak" sayılıyor.

İzin verilen şey şu: gerçek bir deneyimi yansıtan yorumun yazılmasını istemek, karşılığında bir şey teklif etmeden ve puanı ya da içeriği etkilemeye çalışmadan.

Buradan çıkan üç kural:
1. Piyasadaki "önce memnun musunuz diye sor, memnunsa link gönder" yolu bizde yok. İstek herkese aynı gider.
2. İndirim, hediye ya da çekiliş karşılığı yorum istenmez.
3. Metinde "beş yıldız", "olumlu", "güzel yorum", "puan verin" gibi kelimeler geçmez.

Kızgın olan işletmenin müşterisini listeden çıkarmıyoruz. Şikâyeti olan da isteği alır. Kötü yorum gelirse ona cevap yazarız; bu işin bir parçası, kaçınılacak bir kaza değil.

Haşere kartında sektörün kendi siteleri sadece olumlu yorum gösteriyor ve gerçek bir şikâyet yolu bırakmıyor. Piyasa böyle yapıyor; biz yapmıyoruz.

### Google yorumu müşterinin sitesine taşınmaz

Google'da hizmeti almamış kişi de yorum yazabildiği için o yorumlar kanıt sayılmıyor, bu yüzden siteye taşınmıyor.

Bu alanda bir de yönetmelik maddesi var. Genel çerçevesi şu:
1. Yorumu yalnız o hizmeti satın alan yapabilir.
2. Yorumlar olumlu olumsuz ayrımı yapılmadan, tarafsız bir sıraya göre, en az bir yıl yayında kalır.
3. Sahte yorum yazdırmak için anlaşma yapılamaz.
Maddenin bugünkü hâlini müşterinin hukukçusu teyit eder.

Kural: Google yorumları müşterinin sitesine taşınmaz, sitede yorum kutucuğu kurulmaz. Yorum Google'da kalır. Aynı yolu kendi sitende de izle. Bu, kendi işin için verdiğimiz bir tedbir kararıdır, hukuk görüşü değildir.

### Üç yol ve sırası

Yorum isteği üç yoldan gidebilir. Sıra şu: QR her müşteride kurulur ve hep orada durur. İzin varsa üstüne e-posta eklenir. On üçüncü günden sonra ve şablon onaylıysa WhatsApp eklenir. Aynı kişiye aynı iş için tek mesaj gider; e-posta ile WhatsApp birlikte gönderilmez.

Birinci yol, QR kod ve link. Google'ın kendi "yorum iste" özelliği bunu veriyor. Adımlar:
1. İşletme profiline girilir.
2. Yorumlar bölümünde paylaş simgesine basılır.
3. Link kopyalanır ya da QR kod indirilir.
QR kod üretimi yalnız bilgisayar tarayıcısında var, telefonda yok. Kodu sen indirirsin. Nereye asılacağını ikinci ile dördüncü gün arasında, kurulum bloğunda müşteriyle birlikte kararlaştırırsın. Bastırmayı ve asmayı müşteri yapar, masrafı ona aittir. Astığında sana yazar, sen bilgi dosyasına geçersin. Mekâna asılanın yanında fişe, teslim belgesine, faturaya ve araç anahtarlığına da konur.

İkinci yol, e-posta. Kısa metin ve link.

Üçüncü yol, WhatsApp mesajı. Onaylı şablonla gider. Onaylı şablon, WhatsApp'ın sahibi Meta'nın önceden onayladığı hazır mesaj metnidir.

E-posta ve WhatsApp izin ister. İzni işletme kendi adına alır; senin adına alınmış izinle bu mesajlar gönderilmez. İznin biçimini ve kaydını müşteri kendi hukukçusuna sorar. İzin yoksa iki yol da kapalıdır, yalnız QR kalır.

Asılan bir QR kod mesaj değildir, o yüzden izin kuralının dışında sayıyoruz. Bunu müşterinin hukukçusuna teyit ettirirsin.

Birinci ayda çoğu müşteride yalnız QR çalışır. Bunu müşteriye baştan söylersin. Mesaj yolunun açılması için işletmenin yeni müşterilerinden izin toplamaya başlaması gerekir.

### İstek anı nişten çıkar

İsteğin zamanı "iş bitti" anıdır. Bu an nişe göre değişiyor ve karttan çıkıyor:

- Temizlik: aynı gün, ekip evden çıktıktan sonra.
- Kuaför ve berber: koltuktan kalkınca. Kırk beş altmış dakikalık randevunun sonu. QR için en uygun niş.
- Oto kuaför, oto servis, oto galeri: araç teslimi.
- Cam balkon ve PVC: montaj bitince.
- Klima ve kombi: servis ziyareti bitince.
- Elektrik ve teknik bakım: arıza giderilince ya da cihaz teslim edilince. Bakım işinde rapor ve fotoğrafla birlikte.
- Tadilat: teslim.
- Emlak: tapu ya da sözleşme.
- Düğün: düğün gününden sonra.
- Sigorta: poliçe düzenlenince.
- Fotoğraf: çekim günü değil, albüm ya da video teslim edilince. Bu nişte şikâyetler teslimat gecikmesinden çıkıyor. Çekimden hemen sonra yorum istemek yanlış olur.
- Haşere: ilk uygulamadan sonra değil, kontrol turu kapandıktan sonra. Kartta iki üç uygulama yazıyor; böcek hâlâ varsa on beş yirmi gün arayla yeni ziyaret yapılıyor.
- Pilates: seans ya da paket sonunda.
- Güzellik: klasik hizmette seans ya da paket sonunda. Tıbbi işlemde aşağıdaki ayrı yol geçerli.
- Diş ve estetik: aşağıdaki ayrı yol geçerli.

İşin bittiği an sahada doğrulanınca karta yazılır.

Gecikme: QR yolunda gecikme yok, kod zaten orada duruyor. Mesaj yolunda iş bittikten iki saat sonra, müşterinin çalışma saatleri içinde. Gece biten işte ertesi gün, müşterinin çalışma saati başlayınca. Bunlar müşterinin sisteminin saatleridir; senin pencerelerinle ilgisi yok, sistem sen uyurken de gönderir.

Kimden istenir: CRM'de randevusu kapanmış her kayıttan. Randevusuz gelen kişi sistemde görünmez, ona mesaj gitmez. Onun tek yolu mekâna asılı QR koddur. Bu boşluğu müşteriye baştan söylersin.

Bir kural daha: yorum isteği giden kayda, randevudan bir saat sonra giden sonuç sorusu gitmez. Sonuç sorusu, randevunun nasıl geçtiğini soran kısa mesajdır. İkisi aynı kişiye aynı gün gitmez; yoksa önce memnuniyet sorup sonra link göndermiş oluruz, o da Google'ın yasakladığı yol olur. Sonuç sorusu yalnız yorum isteği gitmeyen kayıtlarda çalışır: randevusu iptal olan, gelmeyen ve yorum yolu kapalı olan kayıtlar.

### Sağlık nişlerinin ayrı yolu

Sağlık tanıtım yönetmeliği şunları söylüyor:
1. Örtülü ya da açık reklam yasak.
2. Hastanın ya da yakınının teşekkür ve memnuniyet sözleri üzerinden reklam gibi paylaşım yapılamaz.
3. Görsel paylaşımlarda yorum, beğeni ve paylaşım kapatılmak zorunda.
4. Kişinin bilgisi ve rızası olmadan onunla iletişim kurulamaz.
5. Özendirme, çekiliş ve hediye yasak.

Yönetmelikte Google, işletme profili ya da yorum isteme diye bir şey geçmiyor.

Bu yüzden diş, estetik ve güzellik salonunun tıbbi işlemlerinde kural şu: yorum toplama, kliniğin kendi hukukçusunun yazılı onayı olmadan hiç kurulmaz, QR dahil. Hukukçuya sorulacak tek soru yazılı gider: "Hastalarımızdan, karşılığında hiçbir şey vermeden, asılı bir QR kod üzerinden Google yorumu istememizde sakınca var mı?" Cevap yazılı gelmeden bu parça kurulmaz.

Onay gelirse yalnız QR kurulur, mesaj yolu açılmaz. Kliniğin kendi paylaşımlarında hasta yorumu kullanılmaz.

Onay gelmezse bu parça ilk turda kapsam dışıdır ve müşteriye yazılı bildirilir.

Güzellik salonu ve kuaför bu yönetmeliğin kapsamında değil. Ama bu işletmelerin sağlık kuruluşu gibi görünmesine izin verilmiyor; öncesi sonrası fotoğrafı ve hasta yorumu paylaşımı yasak sayılıyor. Kural: bu iki nişte klasik hizmetlerde yorum istenir. Tıbbi işlem yapılan hizmetlerde yukarıdaki klinik kuralı geçerlidir: hukukçunun yazılı onayı gelmeden hiç kurulmaz, onay gelirse yalnız QR kurulur. Hiçbir yorum işletmenin kendi paylaşımına taşınmaz.

### Metin

Tek adım, tek istek, tek link. İki adımlı memnuniyet sorusu yok.

Mesaj kalıbı: "Merhaba [ad], ben [iş adı]. [Bugün yaptığımız iş: kombinizin bakımını yaptık]. Nasıl bulduğunuzu Google'a yazarsanız çok memnun olurum, bir dakika sürüyor: [link]"

Kurallar: yaklaşık yüz altmış harf, tek istek, tek link. Yasak kelimeler: beş yıldız, olumlu, güzel yorum, puan verin, indirim, hediye. Mesaj işletmenin adına gider. Altında tek satır bulunur: "[İş adı] · [MERSİS ya da vergi numarası] · Mesaj istemiyorsanız 'çıkar' yazın." MERSİS numarası, işletmenin ticaret sicilindeki kayıt numarasıdır; müşteri kendi belgelerinden bulup verir. Kanun her ticari mesajda çıkma yolu arıyor.

E-posta metni aynı, biraz uzun olabilir. Link tek başına bir satırda durur.

QR kodun altına şu tek cümleyi sen koyarsın, baskıya birlikte gider: "Memnun kaldıysanız da kalmadıysanız da yazabilirsiniz." Bu cümle ayıklama yapmadığımızı gösterir.

Hatırlatma yalnız WhatsApp ve e-posta yollarında var: tek, üç gün sonra, aynı yoldan. İkincisi yok. Yorum isteği takip zinciri değildir. Fazla mesaj hem sinir bozar hem hattın kalite notunu düşürür. Kalite notu, WhatsApp'ın her hatta verdiği yeşil, sarı, kırmızı notudur; düşerse günlük gönderim sınırı iner. QR'da hatırlatma yoktur.

Yorum yazıldıysa ya da kişi cevap verdiyse hatırlatma gitmez.

Şablonun kutusu: Meta her şablonu ya "hizmet" ya "pazarlama" kutusuna koyar. Yorum isteği pazarlama kutusuna girer, çünkü hizmetin kullanımına ya da bakımına dair bir bildirim değil. Pazarlama kutusuna giren mesaj, kişi başına düşen pazarlama sınırına sayılır. Bu yüzden eski müşteri listesine mesaj gitmiş bir kişiye aynı gün yorum isteği gönderilmez. Şablon reddedilirse WhatsApp yolu kapanır, QR ve e-posta kalır.

### Gelen yorumu yönetme

Her yoruma cevap yazılır, iyisine de kötüsüne de.

İyi yorumun cevabı, müşterinin önceden onayladığı iki üç şablondan seçilir ve sen "tamam" deyince yayınlanır. Kötü yorumun cevabını sen yazarsın, müşteri yazılı onaylar. Yayınlamayı sen yaparsın; Google profiline yönetici olarak eklendiğin için cevap müşterinin işletme hesabından çıkar.

Cevap metni yorumun geldiği gün hazırlanır ve müşteriye onaya gider. Onay geldikten sonraki yirmi dört saat içinde yayınlanır.

Google'ın cevap için verdiği açık kural: cevapta kampanya ya da indirim teklif edilmez.

Kötü yorumda üç adım:
1. Aynı gün kısa bir cevap yaz. Kendini savunma: olayı kabul et, kişiyi işletmenin kendi telefonuna çağır, orada tartışma açma.
2. Müşteriye haber ver, işin kendisini o düzeltsin.
3. Silme talebi yalnız Google'ın kurallarını çiğneyen yorumlar için. Google'ın kendi cümlesi açık: bir yorumu sadece katılmadığın ya da beğenmediğin için bildirme. Değerlendirmenin kaç gün süreceğine söz verilmez. Reddedilirse itiraz yolu bir kez kullanılır.

Müşteri "bunu sildir" derse bu kural anlatılır. Olmayan bir yetki vaat edilmez.

Nişe göre cevap kuralları:
1. Sigortada cevapta acente unvanı geçer, sigorta şirketiymiş gibi konuşulmaz.
2. Haşerede cevapta "kesin çözüm" ve "garanti" kelimeleri geçmez.
3. Diş ve estetikte cevap kişiye özel yazılmaz, tedaviden söz edilmez; kısa ve tek tip bir cümle kullanılır. Sebebi şu: kliniğin bir yoruma isimle cevap yazması, o kişinin hasta olduğunu herkese doğrular. Sağlık bilgisi özel korunan bir bilgidir.

Yorum isteğine gelen cevabı yazılı asistan karşılamaz. Bu mesajlar randevu konuşması değildir: asistan teşekkür eder ve konuşmayı kapatır, kızgın cevap gelirse aynı gün insana devreder. Bu kural asistanın kurallar bölümüne yazılır.

### Ölçüm

Tutulan sayılar: gönderilen mesaj ve e-posta isteği, basılıp dağıtılan QR sayısı, toplam yorum sayısı, ortalama puan, cevaplanan yorum, cevapsız yorum, kötü yorum ve çözülüp çözülmediği.

Dürüst olalım: QR'dan gelen yorum sayılamaz. Google'ın verdiği kod düz bir link, tarama sayacı yok. Yani "kaç istekten kaç yorum çıktı" hesabı yalnız WhatsApp ve e-posta yollarında yapılabilir. Ölçtüğümüz asıl şey toplam yorum sayısının ve puanın nasıl değiştiği. Raporda da böyle yazılır, uydurma oran yazılmaz.

Beklenen oran verilmez. Müşteriye "şu kadar yorum getiririm" denmez. Kaç istekten kaç yorum çıktığına dair güvenilir bir rakam yok; kendi rakamın ilk müşterilerinden çıkacak.

### Sahadan güncelleme

Niş kartının Sahadan dolacak bölümüne yazılır: bu nişte işin bittiği gerçek an, en çok yorum getiren yol, yorumlarda en çok neyin konuşulduğu. Kartlar bunu birkaç nişte zaten söylüyor: oto kuaförde nezaket, klima ve kombide verilen sözün tutulması, kuaförde personel tavrı, fotoğrafta sessizlik.

## 6. Ne söyler

Kurulumda: "Yorum işi üç yoldan yürüyor: QR, e-posta, WhatsApp. Birinci ay büyük ihtimalle sadece QR çalışacak, çünkü mesaj için müşterilerinden izin toplaman gerekiyor. QR'ı bugün basıyoruz. Yorum yazmak bir dakika sürüyor; ilk hafta içinde ilk yorumun gelsin. Parayı yeni ödedin, ilk görünen kazanç bu olacak."
Ayıklama isteyince: "Sadece memnun olana link gönderemeyiz. Google bunu yasaklı davranışlar arasında sayıyor. Herkese aynı mesaj gidiyor, yüzde yüzüne. Kötü yorum gelirse aynı gün cevabını yazarız."
Müşteri "indirim verelim yorum yazsınlar" derse: "Hayır. Google'ın kendi sayfasında hediye ya da indirim karşılığı yorum için 'kesinlikle yasak' yazıyor. Bunu yapmıyoruz."
Kötü yorum gelince: "Yorum geldi, kötü. Bugün cevabını yazıyorum, sen onaylayacaksın; onaydan sonra yirmi dört saat içinde yayında olur. Silinmesini isteme, olmuyor; Google beğenmediğin için bildirilen yorumu kaldırmıyor. Cevapsız kötü yorum en pahalı yorumdur."
Sağlık nişinde: "Klinikte yorum işine hukukçun yazılı onay vermeden başlamıyoruz. Kanun bu tarafta net değil, riski sana aldırmam. Onay gelirse sadece QR asıyoruz, mesaj göndermiyoruz."

## 7. Ne yazar

Bilgi dosyasına: Google profilinin doğrulanma durumu, yorum linki ve QR kodun yeri, kaç QR basıldı ve nereye asıldı, metnin onay tarihi, bu nişte istek anının ne olduğu, gönderilen istek sayısı ve tarihleri, gelen yorumlar, cevap tarihleri, kötü yorumlar ve ne yapıldığı.
CRM'e: her kayıt için istek gitti mi, hangi yoldan, ne zaman.
Niş kartının Sahadan dolacak bölümüne: işin bittiği gerçek an, işe yarayan yol, yorumlarda en çok neyin konuşulduğu.

## 8. Yedek yol

- Google profili doğrulanmamışsa: doğrulama bitene kadar hiçbir yol çalışmaz, QR da yok. Doğrulama altıncı güne kadar bitmezse bu parça ilk turda kapsam dışına alınır, müşteriye yazılı bildirilir ve güvencenin sonucuna sayılmaz.
- İzin yoksa: mesaj ve e-posta yolu kapalı, yalnız QR yürür.
- Şablon onayı gelmediyse ya da reddedildiyse: WhatsApp yolu kapalı, QR ve e-posta yürür.
- Müşteri QR asmıyorsa: fişe ve teslim belgesine bastırması istenir. O da olmazsa yorum toplama fiilen çalışmaz. Müşteriye yazılı bildirilir; müşterinin kendi adımını atmadığı bu hal güvencenin sonucuna sayılmaz.
- Sağlık nişinde hukukçu onayı gelmezse: parça hiç kurulmaz, kapsam dışıdır ve güvencenin sonucuna sayılmaz.
- Müşteri sahte yorum yazdırmak isterse: yapılmaz, sebebi yazılı bildirilir.
- Puan düşerse: istek durmaz. Son gelen kötü yorumları okur, ortak şikâyeti tek cümleyle yazar ve haftalık kontrolde müşteriye sorarsın: bu şikâyet gerçekten yaşanıyor mu.

## 9. Sıradaki adım ve işaretler

Sıradaki: haftalık kontrol (sistemi-kontrol-et), yirmi birinci gün raporu (aylik-raporu-hazirla).

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Cevap metni yazıldı ama müşterinin onayı iki gün gelmedi: müşteriye hatırlatılır.
- Ortalama puan yarım puan düştü: haftalık kontrolün ilk maddesi olur, istek durmaz.
- Otuz mesaj isteği gitti, hiç yorum yok: istek anına ve metne bakılır, kart gözden geçirilir. İlk müşterilerin sayıları çıkana kadar bu eşik geçicidir.
- Müşteri yorumları sitesine koymak istiyor: yukarıdaki kural anlatılır, konulmaz.
- Şablon reddedildi: WhatsApp yolu kapatılır, diğer iki yol sürer.

Beş kural: boş sayfa yok (link, QR, metin ve cevap şablonları hazır gelir) · sessiz bitiş yok (gelen her yoruma cevap yazılır) · onay (metni ve kötü yorum cevaplarını müşteri onaylar) · sahadan güncelleme (işin bittiği gerçek an ve işe yarayan yol karta yazılır) · sormaz söyler (istek anını ve yolu FounderOS verir).
