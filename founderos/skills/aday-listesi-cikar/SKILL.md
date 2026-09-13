---
user-invocable: false
name: aday-listesi-cikar
description: "Üçüncü gün ve her ay. Beş yüz kişilik soğuk aday listesi ve en çok istenen yüz işletme."
---

# aday-listesi-cikar

## 1. Adı, rolü, pazarlamadaki karşılığı

Üçüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Yol Haritası'nın beşinci aşamasının üçüncü adımındayız.

Bu modül üç şey çıkarıyor: beş yüz kişilik aday listesi, içinden seçilen en çok istenen yüz işletme ve her sabah kendiliğinden hazırlanan günün saha listesi. Aday, henüz müşterin olmayan ama olabilecek işletmedir.

Neden beş yüz: her işletmeye ilk temas ve üç takip gidiyor, günde yüz temasla beş yüz işletme doksan günü ancak dolduruyor. Liste beş yüzün altındaysa üçüncü haftada arayacak kimsen kalmıyor.

Neden bugün: bir sonraki blokta kanıtını hazırlıyorsun ve mesajlarını yazıyorsun, iki blok sonra sahaya çıkıyorsun. O bloğun deneme aramaları bu listeden yapılıyor.

Şunlar bu modülün işi değildir:
- Sıcak çevre listesi (tanidik-listesi-cikar, dün). O ayrı liste, ayrı mesaj.
- Adayın denetimi (aday-denetimi-cikar). Bu modül denetimi tarif etmez, çağırır.
- Mesajların metni (adaya-mesaj-yaz, yarın) ve video mesaj (video-mesaj-cek, sahaya çıktıktan sonra).
- Takip sisteminin kurulması (musteri-takip-sistemini-kur, CRM açıldığı gün). Bugün liste kayıt yerine yazılıyor: CRM açıldıysa CRM'e, açılmadıysa `adaylar.csv`'ye.

Pazarlamadaki karşılığı: aday listesi.

## 2. Ne zaman çalışır
- Üçüncü gün, üç saat. Çekimi veri servisi yapar, birkaç dakika sürer. Tam zamanlıysan tek oturuş; işin yanında çalışıyorsan çekim ve temizlik sabah bloğunda, geri kalanı akşam bloğunda.
- Her gün: günün saha listesi sabah bloğunda kendiliğinden hazırlanır. Senin bir işin yok, açtığında sıralanmış duruyor.
- İkinci kez: her ay bir kere, ayın ilk iş günü. Yeni ilçe çekilir (ana kanal telefonsa üç ilçe, yazıysa bir), o listeden yeni yüz işletme seçilir, hızlı denetimleri yapılır.
- Üçüncü kez: liste beş yüzün altına düştüğünde ya da pazar değiştiğinde. O zaman yeni çekim yapılır.

**Liste bozuk geldiğinde önce yeniden puanlanır, yeniden çekilmez.** Bu kural aylık tavanla ilgili: çekim tavandan düşüyor, puanlama düşmüyor. "Listedekiler bana uygun değil" dediğinde yapılan ilk iş ideal müşteri sayfasını düzeltmek ve beş yüz kaydı o sayfaya göre yeniden puanlamak; bu birkaç dakika sürüyor ve tavandan düşmüyor. Liste ancak iki halde yeniden çekilir: kayıt sayısı beş yüzün altına düştüyse ya da şehir veya sektör değiştiyse. Aynı kategori ve şehir otuz gün boyunca aynı listeyi verir; o yüzden yeniden çekim kartın başka kategori adıyla ya da komşu ille yapılır. Bunun dışında bir daha çekim yapılmaz.

## 3. Ne okur

İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı tek dosya): nişin, şehrin, günlük temas dağılımın, çalışma düzenin, lisans anahtarın (veri servisine kimlik), veri servisinin bu ayki kullanımı, yedek yola geçildiyse tarihi.
Niş kartından (seçtiğin sektörün bütün bilgisinin durduğu dosya): Google Haritalar'daki kategori adları, kanal ve zaman bölümü, kim karar veriyor bölümü, yasal sınırlar.
aday-denetimi-cikar'dan: hızlı denetimin beş satırı ve sızıntı puanı. Denetim orada yürür, bu modül puanı okur ve sıralamada kullanır.
Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv` ve İş Beyni'nin on beşinci bölümü): cevap veren adaylar, takip günü bugüne düşenler, denetimi hazır olanlar. Günün saha listesi bunlardan çıkıyor.
İkinci günün sıcak listesinden: A listesindeki işletmeler.

## 4. Ne sorar

Sormaz. Hangi kategoriyi arayacağını, kaç kayıt çekeceğini, neyi eleyeceğini ve hangi yüz işletmeyi seçeceğini FounderOS söylüyor; listeyi nereden çekeceği de sorulmaz, veri servisinden çeker.

Bir de silme öncesi durak var: servisin işaretlediği satırları ve FounderOS'un elediklerini görüp onaylıyorsun.

## 4c. Tamamlandı demek için

Liste "hazır" demek için kayıt sayısı yetmez:

1. Beş yüz kayıt var ve her birinde telefon ya da e-posta dolu; ikisi de boş olan kayıt listede değil.
2. Örnekleme doğrulaması yapılmış: rastgele on kayıt açılmış, işletme gerçekten var, kategori doğru, numara çalışıyor. Onda üçten fazlası tutmuyorsa liste kartın başka kategori adıyla yeniden çekilir; aynı kategori otuz gün aynı listeyi verir.
3. En çok istenen yüz işletmenin her birinde uygunluk gerekçesi var: neden bu, tek satır. Yüz işletme uygunluk kademesi A olanlardan seçilir; A yüze yetmezse eksik kalan yer B kademesinden sızıntı puanı yüksek olanlarla tamamlanır ve kaç tanesinin B'den geldiği yazılır.
4. Liste kayıt yerine yazılmış (CRM açıldıysa CRM'e, açılmadıysa `adaylar.csv`'ye; sayısı sekizinci bölümde, günün adayları on beşinci bölümde) ve sayım tutuyor.

Dördü tamam olmadan liste "hazır" sayılmaz ve on dördüncü bölüme yazılmaz.

## 5. Ne yapar

### Liste nereden geliyor: veri servisi

Listeyi FounderOS'un veri servisi çekiyor. Sen hesap açmıyorsun, anahtar görmüyorsun, program ekranı açmıyorsun, Excel'de satır silmiyorsun. FounderOS servise kategoriyi ve şehri söylüyor; servis Google Haritalar'dan kayıtları çekiyor, kapalı işletmeleri, tekrarları, iletişimi olmayanları ve zincirleri işaretliyor, işletme adını kısaltıyor, telefonu tek biçime getiriyor, siteden e-posta ve Instagram hesabını çıkarıyor ve listeyi sayfa sayfa FounderOS'a veriyor. FounderOS satırları klasöründeki `adaylar.csv` dosyasına yazıyor; sen listeyi yanındaki `adaylar.html` sayfasından görüyorsun, Excel açmıyorsun. Senin yaptığın tek şey silme onayı.

Servisin aylık bir tavanı var; sekiz yüz kayıtlık çekim ve ay içindeki genişletmeler tavanın içinde. Tavan dolarsa ya da servis kapalıysa yedek yol Claude'un tarayıcı eklentisi; kurulumu araclari-kur'un üçüncü adımında yazılı. Yedek yol üç saatte yaklaşık yüz işletme veriyor ve e-posta getirmiyor; o gün sıra şu:

1. Claude'un tarayıcı eklentisini ve Google Haritalar'ı aç.
2. Arama kelimesi: kartındaki kategori adı artı semt adı ("Nilüfer klima servisi" gibi). Şehri tek seferde aratmıyorsun, Haritalar belli bir sayıdan sonrasını göstermiyor; semt semt gidiyorsun ve taradıklarını bir kenara yazıyorsun.
3. Eklenti her işletme kartından altı şeyi tabloya yazıyor: işletme adı, telefon, web sitesi, semt, yorum sayısı ve puan, varsa Instagram hesabı. E-posta bu yolda gelmiyor; siteyi açıp aramayı sadece yüz işletme için, hızlı denetim sırasında yapıyorsun.
4. Bugün üç saatte yaklaşık yüz işletme çıkarıyorsun, aynı gün kayıt yerine yazıyorsun, yüz işletme seçimini bu kayıtlardan yapıyorsun. Kalanı dördüncü ve beşinci bloğun sabah bloklarına yayıyorsun: sahaya çıkarken elinde üç yüz kayıt oluyor, liste ilk hafta içinde beş yüze tamamlanıyor. Servis açılır açılmaz kalan kayıt servisten çekilir.

### Adım 1: çekim (FounderOS yapar, birkaç dakika)

**Çekim iki kaynaktan yapılıyor, liste tek çıkıyor.** Birincisi Google Haritalar: şehirdeki bütün işletmeleri, telefonuyla, adresiyle, saatleriyle ve yorumlarıyla veriyor. İkincisi Meta reklam kütüphanesi: aynı nişte o şehirde aktif reklam veren sayfaları veriyor. İkisi aynı anda çalışıyor ve tek listede birleşiyor.

İkinci kaynağın işi yeni isim bulmak değil, sıralamayı ve açılış cümlesini düzeltmek. Reklam veren işletme üç şeyi birden kanıtlıyor: parası var, talep akışı var, ve gelen talebi kaçırıyorsa kaybı iki katı. Bu, ideal müşteri tanımının kendisi. Birleşme üç şekilde oluyor:

- Reklam veren işletme Haritalar listesinde zaten varsa satırına `reklam` sütunu doluyor ("2 reklam, 05.01.2026 tarihinden beri") ve ipuçlarına `reklam_veriyor` giriyor.
- Haritalar'da yoksa listeye yeni satır olarak giriyor, kaynağı `reklam` ve ipuçlarında `sadece_reklam` yazıyor. Telefonu genelde boş; numarasını adından aratarak buluyorsun. Bu satırlar Haritalar'ın kaçırdığı, sadece Instagram'dan yürüyen işletmelerdir ve bazı nişlerde en iyi adaylar onlardır.
- Ulusal marka ve ajans gürültüsü listeye hiç girmiyor: beğenisi iki yüz bini geçen sayfa ve altmıştan çok aktif reklamı olan sayfa eleniyor.

Reklam kaynağı ikinci ve isteğe bağlı kaynaktır. Bozulursa, kapalıysa ya da süresinde bitmezse liste yine çıkıyor, sadece reklam sütunu boş kalıyor. Liste hiçbir zaman bu kaynağı bekleyip durmuyor.

Kaç kayıt gelir, bilinmiyor, sahadan dolacak. Beklenti şu: Instagram'dan satan nişlerde (güzellik, estetik, düğün, oto kuaför, fotoğraf, pilates) çok, telefondan yürüyen nişlerde az. Sıfır çıkması sorun değil, liste zaten Haritalar'dan doluyor.

1. FounderOS kartındaki Haritalar kategori adını ve İş Beyni'ndeki şehrini alır, servise ilçe başına sekiz yüz kayıt ister; eleme sonrası elde yaklaşık beş yüz kalıyor. Ana kanalın telefonsa üç ilçe çekilir, çünkü telefonda bir adaya ortalama bir buçuk dokunuş düşüyor ve liste yazılı kanaldakinden hızlı tükeniyor.
2. Servis "çalışıyor" der. FounderOS iş kimliğini hemen İş Beyni'ne yazar ve sana tek cümle söyler: "Çekim başladı, birkaç dakika sürer." Sonucu yirmi saniyede bir sorar, en fazla on kez; on sorguda bitmediyse başka işe geçer ve daha sonra yalnız sonucu sorar, çekimi yeniden başlatmaz. Çekim sunucuda sürdüğü için ekranı kapatsan da bozulmaz.
3. Servis "hazır" deyince FounderOS özeti okur ve sana söyler: kaç kayıt geldi, kaçında telefon var, kaçında e-posta, kaçında Instagram, kaçı reklam veriyor, kaçı yalnız reklamdan bilindi, kaçı hangi sebeple işaretli. Sen "tamam" deyince listeyi klasöre kendi aracıyla indirir (aday-listesi-dosyasi); satırlar sohbete dökülmez, çift kayıt olmaz.
4. Ay başında bu çekim ilk çekimdir; genişletme ve aylık yenileme aynı yoldan yürür, hepsi aylık tavanın içinde.

Şehrinde 800 çıkmıyorsa sıra şu: kartındaki diğer kategori adları (aynı şehir), sonra komşu iller. Her il ayrı bir çekimdir ve aylık tavan ilk listeyle birlikte üç çekime yetiyor; hangi ilin ekleneceğini haftanın kararı seçer. "Türkiye geneli" ayrı bir çekim değildir, il il açılmak demektir; o zaman mesajlardan "sizin şehirde" cümlesi çıkıyor.

### Adım 2: Instagram hesapları (yazı nişlerinde)

Kartın kanal ve zaman bölümü o sektörün Instagram'dan yürüdüğünü söylüyorsa listedeki Instagram sütunu daha da önemli, ama her nişte Instagram mesajı atıyorsun. Servis o sütunu işletmenin sitesinden çıkarıyor; sitesi olmayan ya da sitesinde Instagram bağlantısı olmayan işletmede sütun boş geliyor. Boş kalanları hızlı denetimde, yalnız en çok istenen yüz işletme için, elle buluyorsun: Instagram'da işletme adını aratmak bir dakika sürüyor. Ayrı bir Instagram taraması bu sürümde yok; Instagram sütunu böyle doluyor.

Bir kural: kişisel hesap listeye girmiyor, işletme olarak açılmış hesap giriyor.

### Adım 2b: iş ilanı kaynağı (15 dakika, her nişte)

Bir işletme "resepsiyonist", "sekreter", "çağrı karşılama elemanı", "müşteri temsilcisi", "randevu asistanı" ilanı veriyorsa telefonu kaçırdığını kendi ağzıyla söylüyor demektir; bu, listedeki en sıcak niyet işaretidir. Kartın "iş ilanı kelimeleri" satırındaki kelimelerle (kartta yoksa varsayılan altı kelime: resepsiyonist, sekreter, çağrı karşılama, müşteri temsilcisi, randevu asistanı, ön büro) üç yere bakılır: iş ilanı siteleri (nişin ve şehrin adıyla arama), Instagram'da işletmenin son gönderi ve hikâyeleri ("eleman arıyoruz"), işletmenin sitesindeki "kariyer" sayfası. Bulunan işletme zaten listedeyse kaydına "ilan var: [tarih], [ilan başlığı]" yazılır; listede yoksa Haritalar'dan bulunup eklenir. Bu adımdan çıkan işletmeler en çok istenen yüze doğrudan girer ve denetim kartında dokuzuncu satırı dolu gelir. On beş dakikada beş on işletme çıkar; sıfır çıkarsa sorun değil, ay sonunda tekrar bakılır.

### Adım 3: temizlik (20 dakika, onay senin)

Ham listede sana yaramayacak kayıtlar var. Altı eleme var; ilk üçünü servis işaretleyerek getiriyor, kalan üçünü FounderOS kartına bakarak yapıyor. Karar senin: FounderOS işaretli satırların sayısını sebebiyle söyler, sen "tamam" dersin, o satırlar listeye alınmaz. Görmek istersen FounderOS işaretli satırları da getirir ve tek tek gösterir; "bunu tut" dediğin satır listeye girer.

**Bir: tekrar.** Aynı numara ya da aynı ad ve semt iki kere görünüyorsa biri kalıyor. Servis ikinciyi "tekrar" diye işaretler.

**İki: iletişimi olmayan.** Telefonu, e-postası ve Instagram hesabı üçü birden boş olan kayıt aranamaz, yazılamaz; servis "iletişim yok" diye işaretler. Kapalı işletmeler de burada, "kapalı" işaretiyle.

**Üç: zincir ve şube.** Aynı ad üç ve daha çok kez çıkıyorsa servis hepsini "zincir" diye işaretler. Beş şubesi çıkan markadan tek satır bırakıyorsun, o da genel merkez varsa. Ulusal zincirler tamamen çıkıyor: şubede karar veren kimse yok, şubedeki kişi seni dinliyor ama satın alamıyor.

**Dört: kategoriye uymayan.** Haritalar kategori karıştırıyor; klima servisi ararken beyaz eşya bayisi de geliyor. FounderOS kayıttaki kategoriyi kartınla karşılaştırır, uymayanları listeler, sen onaylarsın.

Buradaki ayrım satan ile servis verendir ve kural yazılıdır, her nişte aynı işler: **ürünü satan çıkar, ürüne servis veren kalır.** Mağaza, bayi, showroom, market satar; servis, teknik servis, tamir, bakım, montaj hizmet verir. İkisini birden yapan kalır ama kaydına "satış da yapıyor" notu düşer, çünkü onda kaçan talep hem randevu hem satış tarafında ve görüşme farklı gidiyor. Ad ve kategori bu ayrımı çoğu zaman kendisi söylüyor; söylemiyorsa FounderOS satırı sana sorar, sen karar verirsin. Aynı eleme raporunda hangi kelimeye bakıldığı yazılır, böylece yanlış eleneni görürsün.

**Beş: nişin yasal sınırına takılan.** Kartın yasal sınırlar bölümü hangi işletme tipinin listeye girmeyeceğini söylüyor; FounderOS bakar, sen onaylarsın.

**Altı: dün sıcak listeye giren işletmeler.** A listen beş on kişi, FounderOS ona bakıp bu listede varsa çıkarır. Tanıdığına bu akşam mesaj gidecek; aynı kişiye iki gün sonra soğuk arama metniyle dönmüyorsun. Bu elemede numaraya güvenilmez: tanıdığının kaydında cep numarası var, buradakinde işletmenin sabit hattı, ikisi tutmuyor; ada bakılır.

Bir şeyi yapmıyorsun: numaraları sabit hat ve cep diye ayırıp birini silmiyorsun. Sen arıyorsun ve işletmenin ilan ettiği sabit hat tam da aradığın numara.

Elemeden sonra beş yüzün altına düştüysen Adım 1'e dönüp aramayı genişletiyorsun.

### Adım 4: işletme adını kısalt (5 dakika)

Ham listede adlar "Yılmaz Isı Sistemleri San. Tic. Ltd. Şti." gibi geliyor; aramada ve mesajda bu ad kullanılırsa toplu gönderim gibi duruyor. Servis kısa adı zaten yazmış: "Yılmaz Isı Sistemleri". Kırptığı ekler: Ltd. Şti., A.Ş., Limited, Anonim Şirketi, San., Sanayi, Tic., Ticaret, Paz., Pazarlama, İnş., İnşaat, Hizmet, Hizmetleri ve aradaki "ve". Ad bu eklerden sonra hâlâ uzunsa kelime sınırında kesilir, ortadan değil; "Bursa Uzman Teknik Beyaz Eşya" adı "Bursa Uzman Teknik Beyaz" diye kesilmez, çünkü telefonda okunduğunda ne olduğu anlaşılmaz hale gelir. Tamamı büyük harf yazılmış adlar da düzeltilir: "ANADOLU DOĞALGAZ MÜHENDİSLİK" listede bağırarak duruyor ve okuması zor.

FounderOS kısa adlara göz gezdirir, yanlış kırpılmış olanı düzeltir. Kayıt yerine giden sütun bu oluyor, uzun olan değil.

### Adım 5: en çok istenen yüz işletmeyi seç (15 dakika)

Kalan listenin içinden yüz tanesini işaretliyorsun: müşterin olmasını en çok istediğin işletmeler. Sıradaki adımda sadece onlar denetimden geçiyor.

Beş seçim ölçütü var ve sırası şu:
1. **İlan verenler.** Adım 2b'deki iş ilanı kaynağından gelenler yüzün başına girer, sıra sormaz.
2. **Reklam verenler.** Reklam sütunu dolu olanlar. Reklam veren işletme üç şeyi birden kanıtlıyor: parası var, talep akışı var, ve gelen talebi kaçırıyorsa kaybı iki katı. Yüzün ikinci sırası bunlar.
3. **Büyük olanlar, ama üst sınırla.** Yorum sayısına göre büyükten küçüğe sırala. Yorumu çok olan işletme çok iş yapıyor, çok iş yapan çok da kaçırıyor. Üst sınır İş Beyni'nin ideal müşteri tanımından gelir: hedef büyüklük üç ile on kişi ve karar tek kişide olacak. Yorum sayısı listenin en üstündeki birkaç işletme çoğu zaman bu sınırın dışında kalıyor; sahibi telefona çıkmıyor, karar bir kişide değil. Bunlar listeden atılmaz, yüzün **sonuna** konur ve kaydına tek satır yazılır: "büyük, karar tek kişide olmayabilir". İlk aramalar bunlarla yapılmaz.
4. **Ulaşılabilir olanlar.** Web sitesi ve Instagram hesabı dolu gelenler.
5. **Nişin içinde kalanlar.** Kategori tam uyanlar.

Seçimi FounderOS yapıyor, sen onaylıyorsun: aday aracının `yuz-sec` komutu listeyi bu sıraya dizip yüzü işaretliyor, elle işaretlediklerine dokunmuyor. Sonra gözden geçiriyorsun.

İlanı olanlar artı kalan dördünü birden taşıyan ilk yüz satırı işaretliyorsun. Emin olamadığını da işaretle, ay sonunda değiştireceksin. İşin yanında çalışıyorsan yüz değil kırk işletme seçiyorsun; onlara ayrı emek vereceksin ve günün kırk temasa yetiyor. Sayfadaki "En çok istenen" kutusunda görünen sayı budur; kırk seçildiyse kırk yazar ve bu eksiklik değildir.

Listenin en büyüğünü yüzün sonuna koyduğunda bunu öğrenciye tek cümleyle söylersin, yoksa "en iyileri neden en sona koydun" diye sorar: "Yorumu en çok olan beş işletmeyi listenin sonuna koydum. Onlar en değerli olanlar ama en zor olanlar da; sahibi telefona çıkmıyor, karar tek kişide değil. İlk aramaların olmasınlar, ilk randevunu aldıktan sonra onlara döneriz." 

Yüz işletmenin farkı emek, mesaj sayısı değil. Kalan dört yüz hızlı denetimle ve kartın gözlemiyle gidiyor; yüz işletme derin denetimden geçiyor (on satır, karar verenin adı, lira karşılığı), mesajı o işletmede gerçekten görülmüş bulguyla açılıyor, ilk teması video mesajla gidiyor ve o ilk temas günde beş adayla yayılıyor ki her biri hazırlıklı gitsin. Denetim kartı adaya belge olarak gönderilmiyor; bulgu görüşmede ve videoda söyleniyor. Kâğıt gönderen satıcı, konuşan satıcının gerisinde kalıyor.

### Adım 6: yüz işletmenin hızlı denetimi (60 dakika)

Bu adımı bu modül tarif etmiyor. Yüz işletmenin hızlı denetimi bu adımda yapılır, nasıl yapıldığı aday-denetimi-cikar'da yazılı, çıktısı sızıntı puanıdır. İşletme başına iki dakika. Puan yüz işletmeyi sıraya diziyor ve sahaya çıktığında kimi önce arayacağını o sıra söylüyor.

Eskiden bu adımda her işletme için tek cümlelik gözlem satırı yazılıyordu; artık yazılmıyor. Yerini denetimin en güçlü bulgusu aldı. Fark şu: gözlem satırı "gördüğüm bir şey", en güçlü bulgu "kaçırdığın müşteri".

Sahibinin adını bulma işi de denetime taşındı, derin denetimin onuncu maddesi o ve sonucu kartın başlık satırına yazılıyor, burada tekrar anlatılmıyor. Sonucu aynı: adı bulunan aday telefon sırasına, bulunamayan yazı sırasına giriyor.

Altmış dakikada otuz işletme bitiyor, kalan yetmişi dördüncü günün sabah bloğunda tamamlıyorsun. Bugün otuz yeterli, çünkü yarının deneme aramaları o otuz işletmeden yapılıyor. İşin yanında çalışıyorsan kırk işletme seçtin: bugün yirmisi, yarın yirmisi.

Puan ve en güçlü bulgu tabloya iki sütun olarak yazılıyor, sıradaki adımda kayıt yerine gidiyor.

### Adım 7: listeyi kayıt yerine koy (15 dakika)

**CRM henüz açılmadıysa (başlangıç görüşmesi yapılmadıysa bu normaldir):** liste klasöre `adaylar.csv` adıyla yazılır. Sütunlar ve değerler aday-listesi-dosyasi'nda sabittir: ilk on altı sütun servisin başlığı (kısa ad, ad, telefon, e-posta, Instagram, site, adres, semt, yorum sayısı, puan, kategori, ipuçları, yorum alıntısı, reklam, elenme, harita), kalan yirmi sekizi FounderOS'un eklediği eklenme tarihi, kaynak ve bağlayan, yüz işareti, denetim sütunları (sahibinin adı, uygunluk puanı, sızıntı puanı, en güçlü bulgu, kanca, lira karşılığı, denetim tarihi) ve temas sütunları (aşama, dört kanalın durumu, temas sayısı, son temas, sıradaki hareket ve tarihi, randevu tarihi, e-posta konusu ve metni, Instagram mesajı, not). Her kayda eklenme tarihi o günün tarihiyle yazılır. Kaynak iki: Haritalar ve reklam. Satırın çoğu Haritalar'dan gelir; reklam kaynaklı satır, o işletmenin Haritalar'da hiç çıkmadığı, yalnız reklam verdiği için bilindiği anlamına gelir ve ipuçlarında "sadece_reklam" yazar. Liste yine tektir, ayrı dosya açılmaz. Başlık satırı bir kere yazılır, servisin sayfaları altına eklenir. Dosyayı ve yanındaki `adaylar.html` sayfasını FounderOS'un aday aracı yazar (aday-listesi-dosyasi); FounderOS csv'yi elle düzenlemez, her yazıştan sonra sayfa kendiliğinden yenilenir. Sayfanın iki sekmesi var: Liste ve Saha modu. Listeyi oradan görürsün, Excel açmazsın. Bu dosya havuzdur ve CRM açılana kadar CRM'in yerine geçer: denetim puanları buraya yazılır, temaslar buraya işlenir, günün listesi buradan seçilir. İş Beyni'nin sekizinci bölümüne dosyanın adı ve kayıt sayısı, on beşinci bölümüne o günün adayları yazılır; beş yüz kayıt İş Beyni'ne kopyalanmaz. CRM açıldığı gün bu dosya bir kerede yüklenir, aşağıdaki yedi adımla, ve `adaylar.csv` "CRM'e taşındı, tarih" notuyla kapanır.

**CRM açıldıysa:** aşağıdaki yedi adım, gerçek listeyle.

1. `adaylar.csv` dosyasını olduğu gibi kullan; CRM'in yükleme ekranı CSV kabul ediyor (kabul etmezse FounderOS aynı tabloyu CRM'in istediği biçimde yeniden yazar).
2. CRM'de yükleme ekranını aç, dosyayı seç, yüklemeye ad ver: kayıt sayısı ve tarih. "512 aday, 6 Eylül" gibi.
3. Eşleme ekranında sütunları işaretle: kısa ad, sahibinin adı, telefon, e-posta, Instagram, site, adres, semt, yorum sayısı, sızıntı puanı, en güçlü bulgu. Eşleşmeyeni alma; ipuçları, elenme ve harita sütunları CRM'e girmiyor. Form ve reklam işaretleri için ayrı sütun açmıyorsun, onlar denetimden geliyor.
4. "Nereden bulundu" satırına Haritalar yazılır. Hangi adaya hangi kolun önce gideceğini kaynak değil, adayın kendi satırı belirliyor: en çok istenen yüzde mi, sahibinin adı bulunmuş mu, e-postası ve Instagram'ı var mı.
5. Kayıtta ad alanı boş kabul edilmiyor. Sahibinin adı bulunmayan kayıtlarda o alana işletme adı yazılıyor.
6. Yükle, sonra yüklenen sayıyı dosyadakiyle karşılaştır. Numara tekrarı temizlendiği için ikisi tutuyor olmalı; büyük fark varsa eşleme yanlış, geri al ve tekrarla.
7. Hepsinin aşaması "yeni" ve üstlerinde "soğuk" işareti var; aşama, adayın işin neresinde olduğunu gösteren etiket. En çok istenen yüz işletmeye ayrı işaret koy. Denetimi bugün yapılmayanlarda sızıntı puanı boş kalıyor, dördüncü blokta doluyor.

### Listenin günlük yenilenmesi

Liste ayda bir tamamen yenileniyor ama her gün yeniden sıralanıyor. İkisi ayrı iş ve ikisi de kendiliğinden yürüyor.

**Ayda bir:** yüz işletme yeniden seçiliyor ve hızlı denetimler tazeleniyor. Yeni çekim yalnız liste beş yüzün altına düştüyse ya da şehir veya sektör değiştiyse yapılıyor; o zaman modül baştan çalışıyor ve sen sadece silme onayını veriyorsun.

**Her gün:** sabah bloğunda "günaydın" yazıyorsun ve o günün saha listesi hazır geliyor. Sen sıralamıyorsun, kimi arayacağına karar vermiyorsun; sıralamayı FounderOS kuruyor, CRM'de hazır böyle bir ekran yok. Liste sayfanın Saha modu sekmesinde kart kart durur: telefon, sahibi, bulgu, kanca, açılış cümlesi, itirazlar. Her aramadan sonra karttaki düğmeye basıyorsun (açmadı, istemedi, ilgilendi, randevu, sonra ara), akşam "Sonuçları kopyala" deyip FounderOS'a yapıştırıyorsun; kayıtları ve yarının sırasını o yazıyor. Sıra sabit, dört basamak:

1. **Cevap verenler.** Mesajına dönmüş, telefonu açmış, "sonra ara" demiş herkes. En başta duruyorlar, çünkü cevap veren adayın ilgisi bir günde soğuyor.
2. **Takip günü gelenler.** Üçüncü, yedinci ve on dördüncü gün zincirinde bugüne düşenler.
3. **Denetimi hazır, sızıntı puanı yüksek adaylar.** Puanı yüksek olan önce; eşitlik yorum sayısıyla bozuluyor.
4. **Hızlı denetimi olmayanlar.** Sıranın sonu; bunlara ulaşılmadan önce iki dakikalık hızlı denetim yapılıyor, hızlı denetimsiz adaya hiçbir kanaldan ulaşılmıyor. Derin denetim ayrı: her sabah sıranın başındaki üç beş aday için, ilk aramalar onlara.

**Kaç kayıt:** çalışma düzenine göre günlük temas sayın kadar. Tam zamanlıysan yüz kayıt, işin yanında kırk. Fazlası hazırlanmıyor; ekranda gördüğün sayı o gün bitirilecek sayı.

**Liste beş yüzün altına düşerse:** uyarı o sabah düşüyor, ay sonu beklenmiyor. O hafta içinde bir sabah bloğu liste büyütmeye ayrılıyor, sıra şu: kartın diğer kategori adları, komşu iller, Türkiye geneli. Türkiye geneline açılırsa mesajlardan "sizin şehirde" cümlesi çıkıyor. Liste üç yüzün altına inerse bu artık liste sorunu değil, niş kararı haftanın kararına gidiyor.

### Listeyle ilgili tek kural

İkinci günde konuşmuştuk, bugün liste elinde olduğu için tekrar ediyorum.

Vergi kaydı olan işletmelere ulaşırken önceden izin almana gerek yok, kanun bunu telefonla arama için de böyle sayıyor. Rahat ol, yaptığın iş normal bir iş.

Sadece şu düzeni koruyorsun: işletmenin Haritalar'da ilan ettiği numara, genel e-postası ve işletme olarak açtığı Instagram hesabı. Başka yerden bulduğun kişisel cep numarası ve kişisel hesap listeye girmiyor. İlk temasta nereden bulduğunu söylüyorsun. İstemeyen kişi aynı gün listeden çıkıyor ve bir daha aranmıyor.

Bu düzeni koruduğun sürece rahatsın.

## 6. Ne söyler

Açılışta: "Bugün üç saat. Çıktı: beş yüz kişilik liste ve içinden seçilen yüz kişi. Bir sonraki blokta kanıtını hazırlıyoruz, deneme aramaları bu listeden yapılacak."
Çekim başlarken: "Çekim başladı, birkaç dakika sürer. Bitince kaç kayıt geldiğini ve kaçının neden işaretlendiğini söyleyeceğim."
Çekim bitince: "[toplam] kayıt geldi. [sayı] tanesinde telefon, [sayı] tanesinde e-posta, [sayı] tanesinde Instagram var. Servis [sayı] satırı işaretledi: [sayı] tekrar, [sayı] kapalı, [sayı] iletişimsiz, [sayı] zincir. Bunları listeye almıyorum, tamam mı? Görmek istersen gösteririm."
Daha az kayıt çekmek isterse: "800 çekiyoruz çünkü eleyeceğiz. Her işletmeye ilk temas ve üç takip gidiyor; beş yüzün altında kalırsan üçüncü haftada arayacak kimsen kalmıyor."
Tavan dolduysa: "Bu ayın tavanı doldu; servis gelecek ay yeniden açılıyor. Bugün tarayıcı eklentisiyle elle devam ediyoruz, yüz işletme çıkar."
Yorumları da çekelim derse: "Hayır. Yorumlara hızlı denetimde gözünle bakıyorsun, yüz işletme için yetiyor."

**Rakam kuralı.** Bu modülde iki ayrı küme var ve karıştırılırsa öğrenci sayıya güvenmiyor. Birincisi çekimden geleni anlatır (kaç kayıt geldi, kaçı işaretlendi), ikincisi listede kalanı anlatır (kaç aday var, kaçı aranabilir). Aynı rakam iki kümeye birden takılmaz. Kural üç maddeli:
- Çekim rakamlarını `cek --ozet` çıktısından, liste rakamlarını `ozet` çıktısından alırsın. İkisini de kendi cümlenden üretmezsin, araçtan okursun. Bir rakamı hatırından yazarsan önceki mesajla çelişir.
- Her rakamın yanında hangi kümeye ait olduğu söylenir: "servisten 677 kayıt geldi, 323'ünü işaretledim" ve "listende 354 aday var, 265'i aranabilir". "265'inde telefon var" cümlesi tek başına iki kümeye de yakışıyor, o yüzden hep kümesiyle söylenir.
- Günü kapatan başlık cümlesi, gerçekten ulaşılabilir sayıyla kurulur. "354 kayıtla sahaya çıkıyorsun" yanlıştır; doğrusu "354 aday: 265'i aranabilir, 121'inin e-postası var, 98'inin Instagram'ı var". Üç sayı birden verilir, çünkü üç kol birden çalışıyor.
Günlük liste hakkında: "Listeyi sen sıralamıyorsun. Sabah açtığında bugünün kayıtları sırada: önce cevap verenler, sonra takibi gelenler, sonra puanı yüksek olan denetimi hazır adaylar."
Liste ilk kez yazılınca sayfa sohbete kart olarak açılır, sonra tek cümle: "Listen hazır, işte burada. Liste sekmesinde yeşil satır bugün sırada, turuncu satır günü geçmiş; Saha modu sekmesinde bugün arayacakların kart kart, her kartta ne söyleyeceğin yazıyor; her aramadan sonra düğmeye bas." Arkasından ikinci cümle: "Klasöründe de duruyor, adı `adaylar.html`; istediğin zaman oradan da açarsın." Klasör tarifi ancak kart açılmazsa verilir.
Listeyi görmek isteyince: sayfa yeniden kart olarak açılır, tek cümle: "Veriyi yeniledim, işte liste."
Bitince: "Liste kayıt yerinde, yüz işletme işaretli, otuzunun denetimi bitti. Bu akşam tanıdıklara ilk mesaj; bir sonraki blokta kanıt ve mesaj metinleri. Geçelim mi?"

## 7. Ne yazar

Kayıt yerine (CRM açıldıysa CRM, açılmadıysa `adaylar.csv`): bütün kayıtlar, aşamaları "yeni", "soğuk" işaretiyle, kaynağı ve nereden bulunduğu yazılı. En çok istenen yüz işletme ayrı işaretle. Denetimi bitenlerde sızıntı puanı ve en güçlü bulgu dolu; denetim kartının kendisini aday-denetimi-cikar yazıyor.
Klasöre: `adaylar.csv` ve `adaylar.html`, aday aracıyla; ilk gün gizli `.founderos/` klasörü ve araç kurulur (aday-listesi-araci), niş kartının "Telefonda söylenecekler" bölümü ve öğrencinin adı, şehri sayfaya yazılır (aday-listesi-dosyasi, kurulum 3. adım); Saha modu kartındaki Söyle metni oradan dolar.
İş Beyni'ne: listenin çıkarıldığı tarih, çekimin iş kimliği, ham kayıt sayısı, servisin işaretlediği ve onayla silinen sayılar, kalan sayı, yüz işletmenin seçim tarihi, hızlı denetimi biten sayı, kullanılan kategori adı ve kapsanan ilçeler, bu ayki kullanım ve tavan, yedek yol kullanıldıysa tarihi.
Bir sonraki modüllere: yüz işletme ve seçim sırası aday-denetimi-cikar'a, sızıntı puanı ve en güçlü bulgu adaya-mesaj-yaz ile video-mesaj-cek'e, denetimi bitmiş otuz işletme kanitini-hazirla'nın yarınki deneme aramalarına, kategori adı ve seçilen yol bir sonraki ay tekrarı için kendine.

## 8. Yedek yol

- Veri servisi kapalıysa, çekim iki denemede de hata verirse ya da aylık tavan dolduysa: tarayıcı eklentisi yoluna geçiliyor; günün içinde geçiliyor ve bugünün çıktısı yüz işletme oluyor. Servis açılınca kalan kayıt servisten çekiliyor.
- Tarayıcı eklentisi de çalışmazsa: elle yazma, en son çare. Bir tabloya altı sütun açıyorsun (işletme adı, telefon, web sitesi, semt, yorum sayısı, Instagram) ve Haritalar'da çıkan her işletmeyi yazıyorsun. Yavaş yol, o yüzden önce diğer ikisi deneniyor. Yedek yoldan gelen kayıtlar da aynı dosyaya aracın ekle komutuyla girer (aday-listesi-dosyasi).
- Şehrinde 500 çıkmazsa: kartın diğer kategori adları, sonra komşu iller, sonra Türkiye geneli. Üçü de yetmezse niş kararı haftanın kararına gidiyor.
- Hızlı denetim bugün otuza ulaşmazsa: yarının deneme aramaları kaç işletme denetlendiyse o kadarıyla yapılıyor. Kalan denetim dördüncü bloğa kayıyor, saha ertelenmiyor.
- CRM yüklemeyi kabul etmezse: liste `adaylar.csv` olarak kalıyor, temaslar oradan yürüyor, yükleme ilk boş saatte tekrarlanıyor.
- Üç saat aşılırsa: hızlı denetim yarım kalabilir, otuz işletme yeter. Liste, temizlik ve yükleme bugün bitiyor.

## 9. Sıradaki adım ve işaretler

Sıradaki: bu akşam tanıdıklara ilk mesaj (tanidiga-mesaj-yaz); bir sonraki blokta kanıt ve mesaj metinleri. Geçelim mi?

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Üçüncü gün bitti, liste yüklenmedi: dördüncü günün ilk işi olur ve o günün akışı bir saat kayar.
- Yüz işletme seçilmedi: yarının deneme araması yapılamıyor, dördüncü günün ilk yarım saatinde seçilir.
- Hızlı denetimi biten sayı otuzun altında: yarının deneme aramaları eksik yapılır, denetim dördüncü günün sabah bloğuna eklenir.
- Aynı işletme hem sıcak hem soğuk listede görünüyor: altıncı eleme atlanmış, soğuk mesaj durdurulur.
- Bir ay geçti, liste yenilenmedi: modül ikinci kez açılır.

Beş kural: boş sayfa yok (kategori adı, çekim, altı eleme ve seçim ölçütleri hazır gelir) · sessiz bitiş yok (akşam liste kayıt yerinde, yüz işletme işaretli ve otuzunun puanı yazılı) · onay (silinecek satırları görüp onaylıyorsun) · sahadan güncelleme (her ay liste ve yüz işletme yenilenir, her gün saha listesi yeniden sıralanır) · sormaz söyler (kategoriyi, sayıyı, elemeleri ve seçim ölçütlerini FounderOS söyler; listenin nereden geleceği de sorulmaz).
