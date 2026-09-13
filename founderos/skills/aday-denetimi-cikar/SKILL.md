---
user-invocable: false
name: aday-denetimi-cikar
description: "Dördüncü gün hızlı denetim, sonra her sabah derin denetim ve sızıntı puanı."
---

# aday-denetimi-cikar

## 1. Adı, rolü, pazarlamadaki karşılığı

Bir işletmeye ulaşmadan önce, o işletmenin müşterisini nerede kaçırdığını dışarıdan bakarak tek sayfaya çıkaran modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Çıkardığı sayfanın adı **denetim kartı**.

Neden var: soğuk mesajın çalışıp çalışmaması tek şeye bağlı, o da mesajın o işletmeye ait olup olmadığı. "Merhaba, işletmenizin dijital varlığını inceledim" diye başlayan mesaj hiçbir şey incelememiş demektir ve işletmeci bunu ilk satırda anlıyor. Denetim kartı, mesajın ilk cümlesine koyacağın gerçek bulguyu üretir. Dört kanalın dördü de aynı karttan besleniyor: telefon, e-posta, Instagram, video.

Pazarlamadaki karşılığı: aday araştırması ve denetim.

Şunlar bu modülün işi değil: listeyi çıkarmak (aday-listesi-cikar), canlı arama ve yazma testleri (kanitini-hazirla), mesajın kendisini yazmak (adaya-mesaj-yaz), video çekmek (video-mesaj-cek), takip sisteminin kurulması (musteri-takip-sistemini-kur).

Tek kural, karıştırma: denetim kartında sadece gördüğün şey yazar. Görülemeyen satıra "bakılamadı" yazılır. Tahmin, yorum ve "muhtemelen" yasak; mesaja giren tek bulgu, ekranda gördüğün bulgudur.

## 2. Ne zaman çalışır
İki hâli var ve ikisi ayrı işler.

**Hızlı denetim.** İşletme başına iki dakika, dışarıdan bakılır, canlı test yok. Üçüncü blokta en çok istenen yüz işletmenin ilk otuzuna, dördüncü blokta kalan yetmişine yapılır; sığmayanı beşinci bloğun sabahına kalır. Sonra her ay listenin yenilenmesiyle tekrarlanır. Çıktısı beş satır ve bir puan.

### Araştırma üç katmanda yapılır, üçü de aynı yükü taşımaz

Bu modülün en büyük tuzağı şu: her adayı tek tek araştırmaya kalkmak. İşletme başına beş dakika, günde yüz temas, beş yüz dakika. Olmuyor. Ama araştırmadan gönderilen mesaj da işe yaramıyor. Çözüm, araştırmayı sorunun kaynağına göre üçe ayırmak.

**Birinci katman, kayıtla birlikte gelen.** Veri servisi her kayıt için işaretleri çıkarıyor: profil sahiplenilmemiş, akşam altıda kapanıyor, çalışma saati yazmıyor, site yok, hafta sonu kapalı, Instagram yok, yorumu az, işletme kapanmış olabilir, yorumlarda kaçan talebi anlatan bir cümle var, ve aktif reklamı var. Bunlar beş yüz kaydın hepsinde var, sıfır iş gerektiriyor ve tahmin değil: Google işletme profilinde görünen şeyler. Gözlem sırasının tabanı bu.

Yorum işaretinin iki türü ayrı duruyor, çünkü ikisi aynı şeyi söylemiyor: telefona ulaşılamadığını yazan yorum ile söz verilen gün gelinmediğini yazan yorum. Birincisi doğrudan sattığımız şeyi anlatıyor, ikincisi ona komşu. Servis işaretin yanında yorumun kendi cümlesini de getiriyor ve mesaja o cümle giriyor: "Google yorumlarınızdan birinde şöyle yazıyor: 'Telefonları açmıyor.'" Genel cümle yerine müşterisinin kendi cümlesi. "Kapanmış olabilir" işareti kanca değil, uyarı: o aday aranmadan önce doğrulanır, çünkü yorumda "bina yıkılmış" yazan işletme Google'da hâlâ açık görünüyor.

Bu katmanın ne kadar dolduğunu ölçtük, tahmin etmedik. İki gerçek çekim, kırk kayıt: telefon kırkta otuz sekiz, site kırkta otuz iki, e-posta kırkta on sekiz, Instagram kırkta on dokuz, yorum şikayeti yirmi kayıtta dört ila beş. Bundan çıkan iki sonuç plana yazıldı: yazılı kanal tek başına listenin yarısına yetmiyor, telefon ana kanal kalıyor; ve güçlü gözlem her adayda çıkmıyor, dört kayıttan birinde çıkıyor, kalanı toplu araştırma ile insan testine kalıyor.

**İkinci katman, toplu araştırma.** Bazı soruların cevabı aday başına değil, niş ve şehir başına aynı yerden geliyor. "Bu şehirde bu nişte kim eleman arıyor" sorusu için yüz ayrı arama yapmanın anlamı yok; tek arama yapılır, çıkan işletme adları listeye dağıtılır. Geriye tek soru kaldı:

- **İş ilanı.** Kartın "iş ilanı kelimeleri" satırındaki kelimelerle şehir ve niş için tek arama. Çıkan işletme adları `isaret --isaret is_ilani` ile listeye yazılır. "Resepsiyonist arıyorsunuz, ilanınızı gördüm" cümlesi profil gözlemlerinin en güçlüsüdür, çünkü işletmeci telefonu kaçırdığını kendisi ilan etmiş oluyor.

Reklam bakışı eskiden bu katmandaydı, artık değil: veri servisi reklam kütüphanesini kendisi tarıyor ve her kayda reklam sütununu dolduruyor. Tek başına sızıntı sayılmıyor; akşam kapalı ya da yorumda şikayet işaretiyle birleşince oluyor: "İki reklamınız yayında, biri 05.01.2026 tarihinden beri ama Google'da saatleriniz akşam altıda kapanıyor."

Toplu araştırma haftada bir yapılır, on dakika sürer ve liste yenilendiğinde tekrarlanır. Günlük değil: iş ilanı gün içinde değişmiyor.

**Üçüncü katman, insan gerektiren.** Geriye iki şey kalıyor ve ikisi de senin elinle yapılıyor: canlı arama testi ve yazılı test. Bunlar otomatiğe alınamaz ve alınmamalı, çünkü değerleri tam da gerçekten yapılmış olmalarından geliyor.

Bu ikisi derin denetimin içinde tek tek yapılmıyor, **toplu yapılıyor ve denetimden ayrı duruyor**. Sebebi zaman: derin denetim işletme başına beş dakika ve günde beşle sınırlı, ama tek bir test araması kırk saniye. Testi denetime bağlamak günde beş adayla sınırlıyordu; ayırınca günde altmışa çıkıyor.

Sayılar kanitini-hazirla'da yazılı ve çalışma düzenine bağlı. Tam zamanlıda akşam kırk telefon testi, sabah yirmi yazılı ve form testi. İşin yanında yirmi ve on. Kimin test edileceğini gün planı söylüyor: ertesi gün temas edilecek adaylar. Sonuçlar denetim kartının altıncı ve yedinci satırına düşüyor, denetim o satırları kendi yapmıyor, buradan okuyor.

Sonuç şu: beş yüz adayın hepsinde gözlem var, en iyi otuzunda toplu araştırmadan gelen güçlü gözlem var, günün altmış adayında (işin yanında otuzunda) gerçekten yapılmış test var. Gözlemsiz mesaj gitmiyor.

**Derin denetim.** İşletme başına beş dakika. Testler denetimden çıkınca sekiz dakika beşe indi: geriye iki elle bakış (iş ilanı, karar verenin adı) ve kartın yazılması kaldı. Sadece o gün ilk aranacak adaylar için, her sabah, sabah bloğunda. Tam zamanlıda günde beş işletme, işin yanında çalışanda üçü; sabah bloğunda yirmi beş dakika tutuyor. Çıktısı tam denetim kartı. Günün kalan temasları (e-posta, Instagram ve sıradaki aramalar) hızlı denetimle gider; derin denetim kotası günün temas sayısını sınırlamaz.

Sıra şu: hızlı denetim yüz işletmeyi puana göre sıraya dizer, derin denetim her sabah sıranın başındakileri açar.

## 3. Ne okur

İş Beyni'nden: nişin, şehrin, günlük temas dağılımın, çalışma düzenin, sistemin adı, Dönüşüm Cümlesi.

Niş kartından: kayıp birimi ve rakamı, sızıntı nerede bölümünün üç sızıntısı, duran havuz tipleri, kanal ve zaman, işletmecinin sözlüğü ve iç sesi, açılış cümlesi, yasal sınırlar.

Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv` ve İş Beyni'nin on beşinci bölümü): adayın kaydı, önceki temaslar, hangi kanalların denendiği, kanal durumu satırları.

kanitini-hazirla'dan: o adaya yapılmış canlı arama ve yazılı test sonucu varsa.

## 4. Ne sorar

Hiçbir şey sormaz. Neye bakılacağını, hangi sıraya bakılacağını ve neyin bulgu sayılacağını FounderOS söyler. İki yerde sen devreye giriyorsun ve ikisi de senin telefonunu gerektirdiği için: canlı arama ve yazılı test. Onları sen yapıyorsun, sonucu söylüyorsun, kart dolduruluyor.

## 5. Ne yapar

### Hızlı denetim, beş satır, iki dakika

Beşi de dışarıdan görünüyor, hiçbiri hesap açmayı gerektirmiyor.

**1. Google işletme profili.** İşletmenin adını Google Haritalar'da aç. Bakılan dört şey: yorum sayısı ve puanı, son yorumun tarihi, yorumlara cevap veriliyor mu, son üç yorumda ne şikayet edilmiş. Bulgu sayılan haller: yorumlara hiç cevap verilmemiş; son yorum altı aydan eski; son üç yorumun içinde "aradım açmadılar", "dönmediler", "randevu verdiler gelmediler" gibi bir cümle var; puan 4,0'ın altında.

**2. Site.** Profilde site varsa telefonundan aç. Bakılan: açılıyor mu, telefon numarası ilk ekranda görünüyor mu, WhatsApp düğmesi var mı, iletişim formu var mı. Bulgu sayılan haller: site yok; site açılmıyor ya da çok yavaş; telefon numarası aramadan bulunamıyor; form var ama nereye gittiği belli değil.

**3. Instagram.** Profilde ya da sitede hesap varsa aç. Bakılan: son gönderi tarihi, takipçi sayısı, biyografide telefon ya da WhatsApp bağlantısı var mı. Bulgu sayılan haller: hesap var ama son gönderi üç aydan eski; biyografide hiçbir iletişim yolu yok; hesap var, gönderi düzenli, ama mesaja cevap verilip verilmediği belli değil (bu satır derin denetimde ölçülüyor).

**4. Çalışma saati ve kapanış.** Google profilindeki çalışma saatleri. Bakılan: yazılı mı, akşam kaçta kapanıyor, hafta sonu açık mı. Bulgu sayılan hal: kartın "kanal ve zaman" bölümü o nişte talebin akşam ya da hafta sonu geldiğini söylüyorsa ve işletme o saatlerde kapalıysa, orada kaçan iş var demektir. Bu, o nişin en somut sızıntısı ve mesajda en kolay kabul edileni.

**5. Duran havuz izi.** Kartın duran havuz tiplerinden hangisinin bu işletmede olduğunu gösteren dışarıdan görülebilir işaret. En sık olanı yorum tarihleri: iki üç yıl öncesine giden yorumlar varsa o işletmenin eski müşteri listesi var demektir. Bulgu sayılan hal: eski yorumlar var ve son yorumlar seyrelmiş; yani müşteri gelmiş ve geri gelmemiş.

Her satır bir puan. Toplam sıfırla beş arası ve adı **sızıntı puanı**. Sızıntı puanı tek bir soruyu cevaplıyor: bu işletme müşteri kaçırıyor mu.

Sıfır puan çıkan işletme listeden çıkmaz, listenin sonuna gider. Sıfır puan "sorunu yok" demek değil, "dışarıdan görülmüyor" demek.

### Uygunluk puanı, aynı iki dakikada

Sızıntı puanı "bu işletmenin derdi var mı" diyor. Uygunluk puanı ayrı bir soruya bakıyor: **bu işletme sana para verebilir mi.** İkisi ayrı sayıdır ve karıştırılmaz; derdi olan ama ödeyemeyen işletmeye harcanan yüz arama, doksan gününü yakan şeydir.

Uygunluk puanı İş Beyni'nin on sekizinci bölümündeki ideal müşteri sayfasından üretilir. Sayfa değişince puan yeniden hesaplanır, liste yeniden çekilmez.

Üç ağırlıkta sinyal var. Sinyallerin kelimeleri nişe göre değişiyor, ağırlıkları değişmiyor:

**Güçlü sinyal, üç puan, en fazla altı.** Sahibin kendisi görünüyor: Google profilinde sahibin adı yazılı, sitede "kurucu" ya da "sahibi" bölümü var, Instagram'da sahibin yüzü var. Karar vereni bulduğun her işaret güçlü sinyaldir, çünkü tek kişilik işte en pahalı şey doğru kişiye ulaşmaktır.

**Orta sinyal, iki puan, en fazla altı.** İşletmenin büyüklüğü ideal müşteri sayfasında işaretlenen bandın içinde: çalışan sayısı, araç sayısı, şube sayısı, yorum sayısı. Para veren işaretleri: reklam veriyor, randevu sistemi var, ücretli bir sayfası var. Bunlar "bu iş para harcıyor" demektir.

**Zayıf sinyal, bir puan, en fazla üç.** Genel canlılık işaretleri: düzenli paylaşım, güncel çalışma saati, doldurulmuş profil. Tek başına hiçbir şey söylemez, eşitlik bozar.

**Eleme, puana bakılmaz.** İdeal müşteri sayfasının on birinci başlığındaki "ne satın almaz" listesindeki her madde burada elemedir. Buna ek olarak her nişte sabit dört eleme var: işletme kapanmış ya da devren ilanı var, zincirin şubesi (kararı başka şehirde veriliyor), aynı hizmeti zaten alıyor (sitede randevu ve otomatik cevap sistemi görünüyor), kartın yasal sınırları o işletmeyi kapsam dışı bırakıyor. Elenen işletme listede kalmaz, "elendi" ve sebebiyle işaretlenir.

**Sert sınırlar, eleme değil sıraya koyma.** Çok küçük olan (yorum sayısı çok düşük, tek kişi, profil neredeyse boş) listenin sonuna gider: derdi olabilir ama ödeyemez. Çok büyük olan (kendi pazarlama ekibi olacak kadar kalabalık) da sonuna gider: kararı sen ulaşamayacağın bir masada veriliyor.

Toplam sıfırla on beş arası. Üç kademeye bölünür:
- **A, on ve üstü.** Bugün aranır. En çok istenen yüz işletme buradan seçilir.
- **B, altı ile dokuz.** Sıradaki hafta.
- **C, beşin altı.** Toplu iş, mesaj ve e-posta; arama yapılmaz.

**Sıralama iki sayıyla yapılır.** Önce uygunluk kademesi, sonra kademe içinde sızıntı puanı. Yani A kademesindeki beş sızıntılı işletme listenin en başında, B kademesindeki beş sızıntılı işletme ondan sonra duruyor. Sebebi şu: ödeyebilen ve derdi olan kişiyle konuşmak, derdi olan ama ödeyemeyen kişiyle konuşmaktan her zaman iyidir.

**Puanlar CRM'e iki ayrı alan olarak yazılır.** Tek alanda toplanmaz. İlk otuz aramadan sonra hangi kademenin gerçekten randevu verdiğine bakılır; kademe eşikleri ancak o zaman değişir, kulaktan değil.

### Derin denetim, denetim kartı, beş dakika

Hızlı denetimin beş satırının üstüne beş şey daha eklenir. Beşinin üçü hazır geliyor (arama testi, yazılı test, reklam izi), ikisi burada yapılıyor (iş ilanı, kim karar veriyor). Beş dakikanın çoğu bu ikisine ve kartı yazmaya gidiyor.

**6. Canlı arama testi.** Bu satır denetim sırasında doldurulmaz, bir gün önceki akşam testinden hazır gelir. Denetim onu okur. Testi kanitini-hazirla yönetir, sınırları orada yazılı; kartın "kanal ve zaman" bölümünün söylediği yoğun saatin dışında bir arama. Yazılan: aradığın saat, açıldı mı, kaç çalışta açıldı, sesli mesaj çıktı mı, geri döndüler mi ve ne kadar sonra. Açılmadıysa bu senin en güçlü bulgun oluyor ve mesajın ilk cümlesi bu.

**7. Yazılı test.** Bu satır da hazır gelir: bir gün önceki sabah yazılı testinden. Kartın söylediği ana yazılı kanaldan, gerçek bir müşteri sorusu. Yazılan: yazdığın saat, cevap geldi mi, kaç saat sonra, cevabın içinde soru soruldu mu yoksa tek kelime mi. Bu testin sınırları kanitini-hazirla'da yazılı ve aynen geçerli: sahte isim yok, sahte işletme yok, randevu almak yok, fiyat pazarlığı yok.

**8. Reklam izi.** Bu satır da elle doldurulmaz, listenin `reklam` sütunundan gelir: aktif reklam var mı, kaç tanesi, biri ne zamandan beri yayında. Reklam veren işletme para harcıyor demektir ve gelen talebi kaçırıyorsa kaybı iki katı; bu, mesajın en sert cümlesini üretir. Sütun boşsa "bakılamadı" yazılır ve puana girmez.

**9. İş ilanı.** Kartın "iş ilanı kelimeleri" satırındaki kelimelerle iş ilanı sitelerine, işletmenin Instagram'ına ve sitesinin kariyer sayfasına bakılır. Yazılan: ilan var mı, tarihi, başlığı. "Resepsiyonist arıyoruz" ilanı veren işletme telefonu kaçırdığını kendisi söylüyor; bu bulgu varsa en güçlü bulgu sırasında canlı arama testinin hemen ardına girer ve e-posta açılışı bu ilandan kurulur.

**10. Kim karar veriyor.** Kartın "kim karar veriyor" bölümünün söylediği kişinin adı. Üç yere bakılır: sitenin hakkımızda ve iletişim sayfası, Instagram biyografisi, Google yorumlarına verilen cevapların altındaki imza. Bulunamazsa "bulunamadı" yazılır; aday yine aranır, açılış "işletme sahibi siz misiniz" olur ve ad ilk aramada öğrenilip karta yazılır. Adı bulunanlar sırada önde gelir.

### Denetim kartının kendisi

Tek sayfa, sabit yapıda, on satır artı üç sonuç satırı. FounderOS doldurur, sen okursun.

```
İşletme: [kısa ad] · Semt: [semt] · Karar veren: [ad ya da bulunamadı]
1 Google profili: [bulgu ya da temiz]
2 Site: [bulgu ya da temiz]
3 Instagram: [bulgu ya da temiz]
4 Saatler: [bulgu ya da temiz]
5 Duran havuz izi: [bulgu ya da temiz]
6 Arama testi: [saat, sonuç] ya da yapılmadı
7 Yazılı test: [saat, sonuç] ya da yapılmadı
8 Reklam: [var/yok/bakılamadı]
9 İş ilanı: [ilan var: tarih, başlık / yok / bakılmadı]
10 Sızıntı puanı: [0-5]

EN GÜÇLÜ BULGU: [tek cümle, gördüğün şey]
LİRA KARŞILIĞI: [kayıp birimi × kartın sızıntı rakamı, tek satır hesap]
SIRADAKİ KANAL: [telefon / e-posta / Instagram / video]
```

**En güçlü bulgu** nasıl seçilir, sıra sabit: canlı arama testinde açılmadıysa o. Açıldıysa ve iş ilanı varsa o ("resepsiyonist arıyorsunuz" cümlesi). O da yoksa yazılı test cevapsız kaldıysa o. İkisi de temizse reklam veriyor ama saatleri kapalı olan. O da yoksa yorumlarda çıkan şikayet cümlesi. O da yoksa duran havuz izi.

Denetim hiç yapılmadıysa **profil gözlemi** devreye girer ve mesaj yine gözlemsiz gitmez. Bu gözlem veri servisinin her kayıt için çıkardığı işaretlerden kuruluyor, yani tahmin değil, Google işletme profilinde görünen şey. Sırası şu: profil sahiplenilmemiş, akşam altıda kapanıyor, çalışma saati yazmıyor, site bağlantısı yok, hafta sonu kapalı, Instagram bulunamadı. Aday listesi sayfası bu satırı "profilden gözlem" diye ayrı etiketle gösteriyor, denetimden gelenle karıştırmıyor; öğrenci hangisinin ne olduğunu görüyor. Profil gözlemi derin denetimin yerine geçmez, sırası onun altındadır, ama beş yüz adayın hepsinde var ve denetim kotası günde beş kişiyle sınırlı.

Hiçbiri yoksa kartın açılış cümlesi kullanılır ve mesaj gözlemsiz gider; bu adayın sırası listenin sonundadır.

**Kanca sütunu** telefonda sesli söylenecek tam cümledir, bulgunun kendisi değil: bulgu "11 Eylül salı 19.05'te aradın, dört çalışta açılmadı, geri arayan olmadı" diye kaydedilir; kanca "Salı akşamı yediye doğru sizi bir kere aradım, açılmadı" olur. Kanca günün adını taşır, bir haftadan eskiyse FounderOS yeniler ya da boşaltır. Gözlem yoksa kanca boştur, sayfa "gözlem yok" gösterir ve kartın açılış sorusu kullanılır. Tek gözlemden "sürekli", "her akşam" gibi genelleme yazılmaz.

**Lira karşılığı** telefonda söylenmez; sayfanın Saha modu kartında görünmez, görüşme özet ekranında durur. Tek satır ve hesabı görünür: "Haftada üç akşam kapalısınız; kartın rakamıyla akşam gelen çağrı [sayı], çağrı başına [kayıp birimi], ayda [çarpım]." Rakamların ikisi de kartın kendisinden gelir, buradan uydurulmaz. Kartta rakam yoksa lira karşılığı satırı boş kalır ve mesaj rakamsız gider; uydurulmuş rakamla giden mesaj ilk soruda çöküyor.

**Sıradaki kanal** nasıl seçilir: aday en çok istenen yüzdeyse ve sahibinin adı biliniyorsa video, ilk temas olarak. Değilse kartın ana kanalı. Ana kanal telefonsa ve karar verenin adı bulunamamışsa yine telefon, "işletme sahibi siz misiniz" ile. Ana kanal Instagram'sa ve adayın hesabı yoksa e-posta, o da yoksa telefon. Sızıntı puanı dörtten yüksek olup üçüncü günde hâlâ cevap vermemiş adayda video, bu kez takip olarak. Bu seçimi FounderOS yapar, sen seçmezsin.

### Denetimden mesaja

Denetim kartı dört kanala dört farklı cümle veriyor ve dördü de aynı bulgudan çıkıyor. Metinlerin kendisi adaya-mesaj-yaz'da yazılı; burada sadece hangi satırın nereye gittiği yazıyor.

- **Telefon**: en güçlü bulgu, kancanın içine girer. Lira karşılığı telefonda söylenmez, görüşmeye saklanır.
- **E-posta**: en güçlü bulgu birinci cümle, lira karşılığı ikinci cümle, sistemin adı üçüncü cümle.
- **Instagram**: en güçlü bulgu soruya çevrilir, lira karşılığı hiç geçmez. Instagram'da rakam ağır duruyor ve mesaj satış gibi görünüyor.
- **Video**: ekranda gösterilen şey en güçlü bulgunun kendisi olur. Sen konuşurken o ekran açık durur.

Bir bulgu iki kanalda aynı cümleyle kullanılmaz. Aynı adaya hem e-posta hem video gidiyorsa video, e-postanın söylemediği ikinci bulguyu gösterir.

### Denetimin sınırları

Beş şey yapılmaz ve bunların hepsi öğrenciyi başını belaya sokacak şeyler.

- Hesap açmaya, şifre denemeye, kapalı bir sayfaya girmeye çalışmak yok.
- İşletmenin müşterilerine ulaşmak, yorum yazan kişilere yazmak yok.
- Sahte müşteri kimliğiyle randevu almak, keşif çağırmak, fiyat teklifi aldırmak yok. Canlı testlerin sınırı kanitini-hazirla'da yazılı ve o sınır aşılmaz.
- İşletmenin çalışanına ya da rakibine bilgi sormak yok.
- Denetimde bulduğun şeyi başkasına, özellikle başka bir adaya anlatmak yok. Kart senin çalışma notun; müşteriye bile olduğu gibi gönderilmez, içinden çıkan cümle gönderilir.

Bir de şu: denetim kartı adayın kendisine gönderilmez. Gönderilirse iki şey oluyor. Birincisi, işletmeci sayfayı okuyup "sağ ol" diyor ve görüşme hiç olmuyor. İkincisi, sayfayı elemanına verip kendisi düzeltmeye çalışıyor. Kartın işi randevu almak, bilgilendirmek değil.

## 6. Ne söyler

Sabah, derin denetim başlarken: "Bugünün beş adayı hazır, sıra sızıntı puanına göre. İlkinden başlıyoruz: [ad], puan dört. Şimdi tek şey senden: saat [saat]'te bu numarayı ara, açılıyor mu bak, sonucu söyle. Gerisini ben dolduruyorum."
Denetim bitince: "[Ad] için en güçlü bulgu şu: [bulgu]. Lira karşılığı [rakam]. Sıradaki kanal telefon. Arama kartın hazır, kanca bu bulgudan yazıldı."
Öğrenci denetimi atlamak isterse: "Yurt dışı satış verisi başlangıç rakamı olarak şunu söylüyor: denetimsiz mesaj yüzde bir cevap alıyor, denetimli mesaj yüzde yedi; kendi oranın otuz temasta belli olur. Beş dakikayı burada harcamazsan yirmi mesajı boşa harcıyorsun. Hangisi daha uzun sürüyor?"
Öğrenci yüz işletmenin hepsine derin denetim yapmak isterse: "Yüz işletmeye beş dakika sekiz saat eder ve o gün hiç arama yapmazsın. Derin denetim sadece o gün arayacaklarına. Kalanların hızlı denetimi zaten var ve sırayı o belirliyor."
Bulgu çıkmazsa: "Bu işletmede dışarıdan görünen sızıntı yok. Bu 'sorunu yok' demek değil, 'göremiyoruz' demek. Listenin sonuna gidiyor, kartın açılış cümlesiyle aranıyor. Sıradaki."
Öğrenci uydurmaya kalkarsa: "Bunu görmedin. Görmediğin bulgu mesaja girmez; ilk soruda çöker ve o adayı bir daha arayamazsın. Bakılamadı yazıyoruz, geçiyoruz."

## 7. Ne yazar

Kayıt yerine (CRM açıldıysa CRM, açılmadıysa `adaylar.csv`; denetim kartının tamamı CRM'siz günlerde klasördeki `denetim-kartlari.md` dosyasına, aday adıyla): her adayın sızıntı puanı ve uygunluk puanı, denetim tarihi, denetim kartının tamamı "denetim kartı" satırına, en güçlü bulgu tek satır olarak ayrı alana (mesaj metinleri oradan okuyor), karar verenin adı, reklam işareti, arama testi sonucu ve yazılı test sonucu kendi satırlarına. Kanal durumu satırlarına dokunulmuyor: denetim bir test, temas değil. CRM açılmadıysa her adayın denetim sonucu aday aracıyla tek komutta yazılır (aday-listesi-dosyasi, guncelle: sahibi, uygunluk, sızıntı, bulgu, kanca, lira karşılığı, denetim tarihi); sayfa kendiliğinden yenilenir.

İş Beyni'ne: kaç adayın hızlı denetimi yapıldı, kaçının derin denetimi yapıldı, puan dağılımı, hangi bulgu tipi en çok cevap alıyor (bu satır otuz temastan sonra dolmaya başlıyor).

Niş kartına: aynı bulgu tipi yirmi işletmenin on beşinde çıkıyorsa o bulgu kartın "sızıntı nerede" bölümüne sahadan gelen satır olarak eklenir, tarihiyle.

Sonraki modüllere: en güçlü bulgu ve lira karşılığı adaya-mesaj-yaz'a, video senaryosu için video-mesaj-cek'e, görüşme özet ekranı için gorusmeyi-yonet'e.

## 8. Yedek yol

- Google profili açılmıyorsa ya da işletme profilde yoksa: hızlı denetim dört satırla yapılır, puan beşte değil dörtte hesaplanır ve bu kayda yazılır.
- Site ve Instagram ikisi de yoksa: bu tek başına bulgudur ve güçlü bir bulgudur. "İnternette sizi arayan biri sadece Haritalar'daki numarayı buluyor" cümlesi kancanın kendisi olur.
- Canlı arama testi yapılamadıysa (senin telefonun yok, saat uygun değil, aynı gün ikinci kez aranmaz): kart o satır boş gider, en güçlü bulgu sıradaki satırdan seçilir. Test ertesi gün yapılır ve kart güncellenir.
- Meta reklam kütüphanesine ulaşılamazsa: "bakılamadı" yazılır, puana girmez. Bu satırın hiç dolmaması sık oluyor ve sistemi durdurmuyor.
- Karar verenin adı bulunamazsa: aday telefon sırasından çıkar, e-posta ve Instagram sırasına geçer. Sonradan ad öğrenilirse telefona döner.
- Denetim için ayrılan sabah bloğu dolarsa: o gün kaç adayın derin denetimi bittiyse ilk aramalar o kadar olur, gerisi hızlı denetimle gider. Hızlı denetimi olmayan adaya ulaşılmaz; onun yerine listenin altındaki, hızlı denetimi hazır olan aday alınır. Saha bloğu hiçbir gün denetim yüzünden kısalmaz.
- Bir aday iki kez denetlenirse: eski kart silinmez, yenisi tarihiyle altına yazılır. Aradaki fark başlı başına bir bulgudur: "üç ay önce de aramıştım, o zaman da açılmamıştı" cümlesi çok güçlü.

## 9. Sıradaki adım ve işaretler

Sıradaki: denetim biten adayın kanalı belli, adaya-mesaj-yaz o kanalın metnini üretir.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Bir aday denetimsiz aranmış: o temas sayılır ama işaret düşer; ikinci kez olursa sabah bloğu denetimle başlar.
- Yüz işletmenin hızlı denetimi dördüncü günde bitmedi: sıralama eksik yapılır, kalanlar ilk hafta içinde tamamlanır, saha ertelenmez.
- Otuz denetimde ortalama sızıntı puanı birin altında: liste yanlış seçilmiş demektir, aday-listesi-cikar'ın seçim ölçütleri yeniden çalıştırılır.
- Aynı bulgu tipi on beş işletmede çıkıyor: niş kartına sahadan gelen satır olarak yazılır.
- Elli temas oldu, en güçlü bulgusu "kartın açılış cümlesi" olan adayların cevap oranı diğerlerinin yarısından az: denetim işe yarıyor demektir, sıralama sıkılaştırılır.
- Bir denetim kartında "bakılamadı" sayısı dördü geçiyor: o aday listenin sonuna gider.

Beş kural: boş sayfa yok (on satırın hepsi ve bakılacak yerler hazır gelir) · sessiz bitiş yok (her denetim bir bulgu, bir rakam ve bir kanalla biter) · onay (canlı testleri sen yaparsın ve sonucu sen söylersin, kart senin söylediğinle dolar) · sahadan güncelleme (tekrarlanan bulgu niş kartına yazılır, cevap alan bulgu tipi sıralamayı değiştirir) · sormaz söyler (neye bakılacağını, hangi bulgunun güçlü olduğunu ve hangi kanala gideceğini FounderOS söyler).
