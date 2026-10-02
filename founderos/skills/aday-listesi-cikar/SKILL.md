---
user-invocable: false
name: aday-listesi-cikar
description: "Üçüncü gün ve her ay. Beş yüz kişilik soğuk aday listesi ve en çok istenen yüz işletme."
---

# aday-listesi-cikar

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "aday-listesi-cikar"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Üçüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Yol Haritası'nın beşinci aşaması, müşteri bul: aday listesi.

Bu modül üç şey çıkarıyor: beş yüz kişilik aday listesi, içinden seçilen en çok istenen yüz işletme ve her sabah kendiliğinden hazırlanan günün saha listesi. Aday, henüz müşterin olmayan ama olabilecek işletmedir.

**Neden beş yüz: bir aylık liste, doksan günlük değil.** Matematiği açık yazıyorum, çünkü bu sayı yanlış anlaşılınca üçüncü haftada arayacak kimse kalmıyor. Yazılı yolda bir adaya dört dokunuş gidiyor (ilk mesaj artı üç takip): 500 × 4 = 2.000 temas, günde yüz temasla yirmi iş günü. Telefon yolunda bir adaya ortalama bir buçuk dokunuş düşüyor, çünkü açmayan adayın satırı üçüncü denemede kapanıyor: 500 × 1,5 = 750 arama, günde elli aramayla on beş iş günü.

Yani beş yüz bir ayın listesidir ve **liste her ay yenilenir**. Doksan gün için gereken toplam: yazılı yolda yaklaşık bin beş yüz, telefon yolunda yaklaşık dört bin iki yüz aday. Bu sayı bir kerede çekilmiyor, ayın ilk iş gününde bir ilçe daha açılarak dolduruluyor; telefon yolunda ayda üç ilçe, yazılı yolda bir.

Liste beş yüzün altına düşerse ay dolmadan biter. Stok uyarısı bunun için var: dokunulmamış aday sayısı günlük temposuna bölünüp beş günün altına inince yeni ilçe kendiliğinden çekilir; çekim gece yapılır, sabah liste hazırdır (rakamlari-oku).

Neden bugün: bir sonraki blokta kanıtını hazırlıyorsun ve mesajlarını yazıyorsun, iki blok sonra sahaya çıkıyorsun. O bloğun deneme aramaları bu listeden yapılıyor.

Şunlar bu modülün işi değildir:
- Sıcak çevre listesi (tanidik-listesi-cikar, dün). O ayrı liste, ayrı mesaj.
- Adayın denetimi (aday-denetimi-cikar). Bu modül denetimi tarif etmez, çağırır.
- Mesajların metni (adaya-mesaj-yaz, yarın) ve video mesaj (video-mesaj-cek, sahaya çıktıktan sonra).
- Takip sisteminin kurulması (musteri-takip-sistemini-kur, CRM açıldığı gün). Bugün liste `adaylar.csv`'ye yazılıyor; CRM açık olsa da soğuk liste oraya yüklenmez, CRM'e yalnız cevap veren, randevu alan ve müşteri olan aday geçer.

Pazarlamadaki karşılığı: aday listesi.

## 2. Ne zaman çalışır
- Üçüncü gün, bir saat. Çekimi veri servisi yapar, birkaç dakika sürer. Tam zamanlıysan tek oturuş; işin yanında çalışıyorsan çekim ve temizlik sabah bloğunda, geri kalanı akşam bloğunda.
- Her gün: günün saha listesi sabah bloğunda kendiliğinden hazırlanır. Senin bir işin yok, açtığında sıralanmış duruyor.
- İkinci kez: her ay bir kere, ayın ilk iş günü. Yeni ilçe çekilir (ana kanal telefonsa üç ilçe, yazıysa bir), o listeden yeni yüz işletme seçilir, hızlı denetimleri yapılır.
- Üçüncü kez: liste beş yüzün altına düştüğünde ya da pazar değiştiğinde. O zaman yeni çekim yapılır.
- Öğrenci listeyi daha önce açıkça isterse ("İstanbul'da implant hizmeti veren yüz diş kliniği bul", "İstanbul'daki diş kliniklerini bul"): pazar seçiliyse o gün, o turda çalışır; üçüncü gün beklenmez, "liste üçüncü gün çıkıyor" denmez. Planın neresinde olduğunu tek cümleyle söylersin ("Planda liste üçüncü gün çıkıyordu; istedin, şimdi çekiyorum."). Aday aracı klasörde yoksa önce kurulur (aday-listesi-araci). Öğrencinin cümlesindeki hizmet (implant gibi) kategori değil, sıralama ölçüsüdür: çekim kartın kategori adıyla yapılır, hizmet reklam kelimelerinin başına konur ve yüz seçiminde reklam verenler öne alınır. İstediği ama taramada olmayan bilgi (yönetici ya da sahibinin adı) uydurulmaz, boş kalır ve tek cümleyle söylenir; kaynak her satırın Google Haritalar kaydıdır, panelde işletmenin çekmecesinin altında açılır. Kanal da istediyse tablonun altıncı sütunu "İlk temas"tır: kanal ve kısa gerekçe, satırın ipuçlarından ve kartın kanal bölümünden (telefonu öne çıkarıyorsa arama, yalnız Instagram'dan yürüyorsa mesaj). Erken çıkan liste üçüncü gün yeniden çekilmez; o gün yalnız eksik kalan (silme onayı, yüz seçimi) tamamlanır.

**Liste bozuk geldiğinde önce yeniden puanlanır, yeniden çekilmez.** Bu kural aylık tavanla ilgili: çekim tavandan düşüyor, puanlama düşmüyor. "Listedekiler bana uygun değil" dediğinde yapılan ilk iş ideal müşteri sayfasını düzeltmek ve beş yüz kaydı o sayfaya göre yeniden puanlamak; bu birkaç dakika sürüyor ve tavandan düşmüyor. Liste ancak iki halde yeniden çekilir: kayıt sayısı beş yüzün altına düştüyse ya da şehir veya sektör değiştiyse. Aynı kategori ve şehir otuz gün boyunca aynı listeyi verir; o yüzden yeniden çekim kartın başka kategori adıyla ya da komşu ille yapılır. Bunun dışında bir daha çekim yapılmaz.

## 3. Ne okur

İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı tek dosya): nişin, şehrin, günlük temas dağılımın, çalışma düzenin, lisans anahtarın (veri servisine kimlik), veri servisinin bu ayki kullanımı, yedek yola geçildiyse tarihi.
Niş kartından (seçtiğin sektörün bütün bilgisinin durduğu dosya): Google Haritalar'daki kategori adları, reklam kütüphanesi kelimeleri satırı, kanal ve zaman bölümü, kim karar veriyor bölümü, yasal sınırlar.
aday-denetimi-cikar'dan: hızlı denetimin beş satırı ve sızıntı puanı. Denetim orada yürür, bu modül puanı okur ve sıralamada kullanır.
Aday listesinden (`adaylar.csv`, CRM açıldıktan sonra da): cevap veren adaylar, takip günü bugüne düşenler, denetimi hazır olanlar. Günün saha listesi bunlardan çıkıyor.
İkinci günün sıcak listesinden: A listesindeki işletmeler.

## 4. Ne sorar

Sormaz. Hangi kategoriyi arayacağını, kaç kayıt çekeceğini, neyi eleyeceğini ve hangi yüz işletmeyi seçeceğini FounderOS söylüyor; listeyi nereden çekeceği de sorulmaz, veri servisinden çeker.

Bir de silme öncesi durak var: servisin işaretlediği satırları ve FounderOS'un elediklerini görüp onaylıyorsun.

## 4c. Tamamlandı demek için

Liste "hazır" demek için kayıt sayısı yetmez:

1. Beş yüz kayıt var ve her birinde telefon ya da e-posta dolu; ikisi de boş olan kayıt listede değil.
2. Örnekleme doğrulaması yapılmış: rastgele on kayıt açılmış, işletme gerçekten var, kategori doğru, numara çalışıyor. Onda üçten fazlası tutmuyorsa liste kartın başka kategori adıyla yeniden çekilir; aynı kategori otuz gün aynı listeyi verir.
3. En çok istenen yüz işletmenin her birinde uygunluk gerekçesi var: neden bu, tek satır. Yüz işletme uygunluk kademesi A olanlardan seçilir; A yüze yetmezse eksik kalan yer B kademesinden sızıntı puanı yüksek olanlarla tamamlanır ve kaç tanesinin B'den geldiği yazılır.
4. Liste `adaylar.csv`'ye yazılmış (sayısı İş Beyni'nin sekizinci bölümünde) ve sayım tutuyor.

Dördü tamam olmadan liste "hazır" sayılmaz; durum kaydına ve günlüğe "liste hazır" yazılmaz.

## 5. Ne yapar

### Liste nereden geliyor: veri servisi

Listeyi FounderOS'un veri servisi çekiyor. Sen hesap açmıyorsun, anahtar görmüyorsun, program ekranı açmıyorsun, Excel'de satır silmiyorsun. FounderOS servise kategoriyi ve şehri söylüyor; servis Google Haritalar'dan kayıtları çekiyor, kapalı işletmeleri, tekrarları, iletişimi olmayanları ve zincirleri işaretliyor, işletme adını kısaltıyor, telefonu tek biçime getiriyor, siteden e-posta ve Instagram hesabını çıkarıyor ve listeyi sayfa sayfa FounderOS'a veriyor. FounderOS satırları klasöründeki `adaylar.csv` dosyasına yazıyor; sen listeyi yanındaki `adaylar.html` sayfasından görüyorsun, Excel açmıyorsun. Senin yaptığın tek şey silme onayı.

Servisin aylık bir tavanı var; sekiz yüz kayıtlık çekim ve ay içindeki genişletmeler tavanın içinde. Tavan dolarsa ya da servis kapalıysa yedek yol devreye giriyor ve sekizinci bölümde yazılı. **Servis çalışırken yedek yoldan, tarayıcıdan ve eklentiden söz edilmez**; öğrenci o gün Google Haritalar açmıyor, liste kendiliğinden geliyor. Yedek yola geçmenin dört şartı ortak kurallarda yazılı: servis gerçekten çağrılacak, iki kez denenecek, kalan hakka bakılacak, sebep öğrenciye söylenecek. Kalan hak varken elle liste çıkarılmaz.

### Adım 1: çekim (FounderOS yapar, birkaç dakika)

**Çekim iki kaynaktan yapılıyor, liste tek çıkıyor.** Birincisi Google Haritalar: şehirdeki bütün işletmeleri, telefonuyla, adresiyle, saatleriyle ve yorumlarıyla veriyor. İkincisi Meta reklam kütüphanesi: aynı nişte o şehirde aktif reklam veren sayfaları veriyor. İkisi aynı anda çalışıyor ve tek listede birleşiyor.

İkinci kaynağın işi yeni isim bulmak değil, sıralamayı ve açılış cümlesini düzeltmek. Reklam veren işletme üç şeyi birden kanıtlıyor: parası var, talep akışı var, ve gelen talebi kaçırıyorsa kaybı iki katı. Bu, ideal müşteri tanımının kendisi. Birleşme üç şekilde oluyor:

- Reklam veren işletme Haritalar listesinde zaten varsa satırına `reklam` sütunu doluyor ("2 aktif reklam, biri 05.01.2026 tarihinden beri") ve ipuçlarına `reklam_veriyor` giriyor.
- Haritalar'da yoksa listeye yeni satır olarak giriyor, kaynağı `reklam` ve ipuçlarında `sadece_reklam` yazıyor. Telefonu genelde boş; numarasını adından aratarak buluyorsun. Bu satırlar Haritalar'ın kaçırdığı, sadece Instagram'dan yürüyen işletmelerdir ve bazı nişlerde en iyi adaylar onlardır.
- Ulusal marka ve ajans gürültüsü listeye hiç girmiyor: beğenisi iki yüz bini geçen sayfa ve altmıştan çok aktif reklamı olan sayfa eleniyor.

Reklam kaynağı ikinci ve isteğe bağlı kaynaktır. Bozulursa, kapalıysa ya da süresinde bitmezse liste yine çıkıyor, sadece reklam sütunu boş kalıyor. Liste hiçbir zaman bu kaynağı bekleyip durmuyor.

On iki arama, çekim başına en çok dört yüz **reklam veren**. Buradaki birim önemli: reklam sayısı değil işletme sayısı. Servis her sayfadan tek kayıt alıyor ve o sayfanın kaç aktif reklamı olduğunu ayrıca soruyor; yoksa tek klinik yüz reklamıyla listeyi de maliyeti de şişiriyordu. Bu haliyle bir çekim birkaç kuruş tutuyor. Tavan ve kelime sayıları ayarlanabilir, ayar deploy gerektirmiyor.

Kaç kayıt gelir, bilinmiyor, sahadan dolacak. Beklenti şu: Instagram'dan satan nişlerde (güzellik, estetik, düğün, oto kuaför, fotoğraf, pilates) çok, telefondan yürüyen nişlerde az. Sıfır çıkması sorun değil, liste zaten Haritalar'dan doluyor.

1. FounderOS kartındaki Haritalar kategori adını, İş Beyni'ndeki şehri ve coğrafyadaki ilçeyi alır; her ilçe ayrı bir `aday_ara` çağrısıdır (`ilce` alanı dolu) ve servise ilçe başına sekiz yüz kayıt ister; eleme sonrası elde yaklaşık beş yüz kalıyor. Ana kanal telefonsa coğrafyanın ilk üç ilçesi bugün çekilir (üç çağrı), yazıysa ilki. Coğrafyada ilçe yazmıyorsa kartın yoğun ilçeleri alınır. Şehir geneli tek çekim (ilçesiz) yapılmaz: sekiz yüzde kesilir ve sonraki ayların yeni ilçe yenilemesi aynı işletmeleri yeniden getirir; tam zamanlıda günde yüz temasla şehir geneli bir liste birkaç günde biter.

**Reklam araması kategori adıyla yapılmaz, kartın kelimeleriyle yapılır.** Bu ayrım kritik: hiçbir diş kliniği "diş kliniği" diye reklam vermiyor, "implant fiyatları" ve "gülüş tasarımı" diye veriyor. Kategori adıyla aranırsa o şehirdeki reklam verenlerin neredeyse hepsi kaçar. Kartın **reklam kütüphanesi kelimeleri** satırı tam bunun için yazıldı ve on dokuz kartın hepsinde dolu.

FounderOS o satırı okur, temiz bir liste çıkarır ve servise verir. Kural üç satır:
- Açıklama cümleleri alınmaz. Kartta "şehir adıyla", "erişilemedi", "doğrulanmadı" gibi notlar var; onlar kelime değil.
- Birbirini içeren kelimelerden biri alınır. "Gülüş tasarımı" varken "dijital gülüş tasarımı" ayrı bir arama hak etmiyor, aynı reklamları getiriyor.
- İlk sekizi alınır, kartta yazdığı sırayla. Sıra kartta güçlüden zayıfa yazılı: nişin kendi adı, sonra en çok reklam edilen hizmetler.

**Arama iki koldan yapılır, biri dar biri geniş.** Sebebi kütüphanenin kendi mantığı: kütüphane reklamın hedeflediği şehri göstermiyor, reklamın **metninde** ve **sayfanın adında** arıyor. Yani "implant fiyatları Bursa" araması ancak şehrini yazan reklamı buluyor, ki yerel işletmelerin çoğu yazmıyor.

- **Dar kol:** ilk sekiz kelime, her biri şehirle. "implant fiyatları Bursa", "gülüş tasarımı Bursa". Kesin sonuç verir, az getirir.
- **Geniş kol:** ilk dört kelime, şehirsiz. "implant fiyatları", "gülüş tasarımı". Şehrini hiç yazmayan yerel reklamcıyı da getirir, yanında bütün ülkenin gürültüsünü de getirir.

Gürültüyü arama elemiyor, birleştirme eliyor. Kural tek: **Haritalar listesiyle eşleşmeyen ve adında, adresinde ya da sitesinde şehir veya ilçe geçmeyen reklamcı listeye hiç girmiyor.** Yani geniş kolun getirdiği yüzlerce ulusal reklam listeyi şişirmiyor; işi, şehirdeki gerçek işletmeyi bulup satırına işaret koymak.

Üç sonuç çıkıyor. İstanbul'daki bir zincir klinik geniş kolda çıkıyor ama listeye girmiyor, çünkü ne Haritalar listesinde var ne adında Bursa geçiyor. Bursa'daki bir klinik Haritalar listesinde varsa sitesinden ya da adından eşleşiyor ve satırına reklam sütunu doluyor. "Nilüfer Ağız ve Diş Sağlığı" gibi adında semtini yazan, Haritalar'da hiç çıkmayan bir işletme ise yeni satır olarak listeye giriyor.

Şehir her reklam aramasının içine giriyor, ilçe girmiyor: reklam metni ilçe adı geçirmiyor (bu kural reklam kelimeleri içindir; Haritalar çekimi yukarıdaki gibi ilçe ilçe yapılır). İlçe yalnız eleme aşamasında, adında semt yazan işletmeyi kurtarmak için kullanılıyor. Ana kanalın telefonsa üç ilçe çekilir, çünkü telefonda bir adaya ortalama bir buçuk dokunuş düşüyor ve liste yazılı kanaldakinden hızlı tükeniyor.
2. Servis "çalışıyor" der. FounderOS iş kimliğini hemen İş Beyni'ne yazar ve sana tek cümle söyler: "Çekim başladı, birkaç dakika sürer." Sonucu yirmi saniyede bir sorar, en fazla on kez; on sorguda bitmediyse başka işe geçer ve daha sonra yalnız sonucu sorar, çekimi yeniden başlatmaz. Çekim sunucuda sürdüğü için ekranı kapatsan da bozulmaz.
3. Servis "hazır" deyince FounderOS özeti okur ve sana söyler: kaç kayıt geldi, kaçında telefon var, kaçında e-posta, kaçında Instagram, kaçı reklam veriyor, kaçı yalnız reklamdan bilindi, kaçı hangi sebeple işaretli. Sen "tamam" deyince listeyi klasöre kendi aracıyla indirir (aday-listesi-dosyasi); satırlar sohbete dökülmez, çift kayıt olmaz.
4. Ay başında bu çekim ilk çekimdir; genişletme ve aylık yenileme aynı yoldan yürür, hepsi aylık tavanın içinde.

Şehrinde 800 çıkmıyorsa sıra şu: kartındaki diğer kategori adları (aynı şehir), sonra komşu iller. Her il ayrı bir çekimdir ve aylık tavan ilk listeyle birlikte üç çekime yetiyor; hangi ilin ekleneceğini haftanın kararı seçer. "Türkiye geneli" ayrı bir çekim değildir, il il açılmak demektir; o zaman mesajlardan "sizin şehirde" cümlesi çıkıyor.

### Adım 2: Instagram hesapları (yazı nişlerinde)

Kartın kanal ve zaman bölümü o sektörün Instagram'dan yürüdüğünü söylüyorsa listedeki Instagram sütunu daha da önemli, ama her nişte Instagram mesajı atıyorsun. Servis o sütunu işletmenin sitesinden çıkarıyor; sitesi olmayan ya da sitesinde Instagram bağlantısı olmayan işletmede sütun boş geliyor. Boş kalanları hızlı denetimde aramıyorsun, o oturuşu uzatır; en çok istenen yüz işletmede derin denetimin sabahında buluyorsun: Instagram'da işletme adını aratmak bir dakika sürüyor. Ayrı bir Instagram taraması bu sürümde yok; Instagram sütunu böyle doluyor.

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

**Beş: bu nişte çalışmadığımız işletme tipi.** Kart hangi işletme tipinin listeye girmeyeceğini söylüyor; FounderOS bakar, sen onaylarsın. Kaynağı kartın yasal sınırlar bölümü; öğrenciye sebep anlatılmaz, eleme raporunda "bu tip işletmeyle çalışmıyoruz" yazar.

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
2. **Reklam verenler.** Reklam sütunu dolu olanlar ("2 aktif reklam, biri 05.01.2026 tarihinden beri"). Reklam veren işletme üç şeyi birden kanıtlıyor: parası var, talep akışı var, ve gelen talebi kaçırıyorsa kaybı iki katı. Yüzün ikinci sırası bunlar.
3. **Büyük olanlar, ama üst sınırla.** Yorum sayısına göre büyükten küçüğe sırala. Yorumu çok olan işletme çok iş yapıyor, çok iş yapan çok da kaçırıyor. Üst sınır İş Beyni'nin ideal müşteri tanımından gelir: hedef büyüklük üç ile on kişi ve karar tek kişide olacak. Yorum sayısı listenin en üstündeki birkaç işletme çoğu zaman bu sınırın dışında kalıyor; sahibi telefona çıkmıyor, karar bir kişide değil. Bunlar listeden atılmaz, yüzün **sonuna** konur ve kaydına tek satır yazılır: "büyük, karar tek kişide olmayabilir". İlk aramalar bunlarla yapılmaz.
4. **Ulaşılabilir olanlar.** Web sitesi ve Instagram hesabı dolu gelenler.
5. **Nişin içinde kalanlar.** Kategori tam uyanlar.

Seçimi FounderOS yapıyor, sen onaylıyorsun: aday aracının `yuz-sec` komutu listeyi bu sıraya dizip yüzü işaretliyor, elle işaretlediklerine dokunmuyor. Sonra gözden geçiriyorsun.

İlanı olanlar artı kalan dördünü birden taşıyan ilk yüz satırı işaretliyorsun. Emin olamadığını da işaretle, ay sonunda değiştireceksin. İşin yanında çalışıyorsan yüz değil kırk işletme seçiyorsun; onlara ayrı emek vereceksin ve günün kırk temasa yetiyor. Sayfadaki "En çok istenen" kutusunda görünen sayı budur; kırk seçildiyse kırk yazar ve bu eksiklik değildir.

Listenin en büyüğünü yüzün sonuna koyduğunda bunu öğrenciye tek cümleyle söylersin, yoksa "en iyileri neden en sona koydun" diye sorar: "Yorumu en çok olan beş işletmeyi listenin sonuna koydum. Onlar en değerli olanlar ama en zor olanlar da; sahibi telefona çıkmıyor, karar tek kişide değil. İlk aramaların olmasınlar, ilk randevunu aldıktan sonra onlara döneriz." 

Yüz işletmenin farkı emek, mesaj sayısı değil. Kalan dört yüz hızlı denetimle ve kartın gözlemiyle gidiyor; yüz işletme derin denetimden geçiyor (on satır, karar verenin adı, lira karşılığı), mesajı o işletmede gerçekten görülmüş bulguyla açılıyor, ilk yazılı temasına üç gün cevap gelmezse ikinci dokunuşu video mesaj oluyor. İlk yazılı temaslar ve videolar derin denetim hızıyla, günde beş adayla yayılıyor ki her biri hazırlıklı gitsin; günün on videosunun kalanı listenin geri kalanından gelir (video-mesaj-cek). Denetim kartı adaya belge olarak gönderilmiyor; bulgu görüşmede ve videoda söyleniyor. Kâğıt gönderen satıcı, konuşan satıcının gerisinde kalıyor.

### Adım 6: en çok istenenlerin hızlı denetimi (dördüncü blokta, yarım saat; tam zamanlıda yüz, işin yanında kırk işletme)

Bu adım bugün yapılmaz ve bu modül onu tarif etmez. Yüz işletmenin hızlı denetimi dördüncü bloğun sabahında, tek oturuşta yapılır; nasıl yapıldığı aday-denetimi-cikar'da yazılı, çıktısı sızıntı puanıdır. İşletme başına yaklaşık yirmi saniye; beş satırın dördü veri servisinden hazır geliyor, senin işin okuyup onaylamak. Puan yüz işletmeyi sıraya diziyor ve sahaya çıktığında kimi önce arayacağını o sıra söylüyor.

Eskiden bu adımda her işletme için tek cümlelik gözlem satırı yazılıyordu; artık yazılmıyor. Yerini denetimin en güçlü bulgusu aldı. Fark şu: gözlem satırı "gördüğüm bir şey"di, en güçlü bulgu müşterinin kaçtığı yeri gösteren, gerçekten görülmüş şey; mesajların açılışı (Truva Atı Metodu) ondan kurulur.

Sahibinin adını bulma işi de denetime taşındı, derin denetimin onuncu maddesi o ve sonucu kartın başlık satırına yazılıyor, burada tekrar anlatılmıyor. Sonucu şu: adı bulunan aday telefon sırasında önde gelir; adı bulunamayan da aranır, açılış adı sormadan yapılır (adaya-mesaj-yaz'daki yardım isteyen açılış) ve ad ilk aramada öğrenilir.

Yüz işletme yarım saatte bitiyor, o yüzden bölünmüyor. Dördüncü günün deneme aramaları o sabah denetlenen işletmelerden yapılıyor. İşin yanında çalışıyorsan kırk işletme seçtin; kırkı da aynı oturuşta biter.

Puan ve en güçlü bulgu kayıttaki iki sütuna yazılıyor; bugün boş gidiyorlar, denetim sabahı doluyorlar.

### Adım 7: listeyi klasöre yaz ve sayfayı aç (beş dakika)

**Liste klasöre yazılır; CRM açılmış olsa da yeri burasıdır:** `adaylar.csv` adıyla. Sütunlar ve değerler aday-listesi-dosyasi'nda sabittir: ilk on altı sütun servisin başlığı (kısa ad, ad, telefon, e-posta, Instagram, site, adres, semt, yorum sayısı, puan, kategori, ipuçları, yorum alıntısı, reklam, elenme, harita), kalan otuz biri FounderOS'un eklediği eklenme tarihi, kaynak ve bağlayan, yüz işareti, denetim sütunları (sahibinin adı, uygunluk puanı, sızıntı puanı, en güçlü bulgu, kanca, lira karşılığı, denetim tarihi) ve temas sütunları (aşama, dört kanalın durumu, temas sayısı, son temas, sıradaki hareket ve tarihi, randevu tarihi, e-posta konusu ve metni, Instagram mesajı, not). Her kayda eklenme tarihi o günün tarihiyle yazılır. Kaynak iki: Haritalar ve reklam. Satırın çoğu Haritalar'dan gelir; reklam kaynaklı satır, o işletmenin Haritalar'da hiç çıkmadığı, yalnız reklam verdiği için bilindiği anlamına gelir ve ipuçlarında "sadece_reklam" yazar. Liste yine tektir, ayrı dosya açılmaz. Başlık satırı bir kere yazılır, servisin sayfaları altına eklenir. Dosyayı ve yanındaki `adaylar.html` sayfasını FounderOS'un aday aracı yazar (aday-listesi-dosyasi); FounderOS csv'yi elle düzenlemez, her yazıştan sonra sayfa kendiliğinden yenilenir. Sayfanın iki sekmesi var: Liste ve Bugünün listesi. Listeyi oradan görürsün, Excel açmazsın. Bu dosya havuzdur ve CRM açıldıktan sonra da havuz olarak kalır: denetim puanları buraya yazılır, temaslar buraya işlenir, günün listesi ve telefondaki saha ekranı buradan kurulur. İş Beyni'nin sekizinci bölümüne dosyanın adı ve kayıt sayısı yazılır; günün listesi sayfadadır, beş yüz kayıt İş Beyni'ne kopyalanmaz. CRM açıldığında bu dosya yüklenmez ve kapanmaz: CRM'e yalnız cevap veren, randevu alan ve müşteri olan aday geçer, onu da FounderOS tek tek, senin "tamam"ınla yazar.

**CRM açıldıysa:** liste yine CRM'e yüklenmez. Yükleme ekranı yalnız sıcak kayıtların (cevap veren, randevu alan) ilk aktarımında kullanılır ve o iş musteri-takip-sistemini-kur'da yazılı.

### Listenin günlük yenilenmesi

Liste ayda bir tamamen yenileniyor ama her gün yeniden sıralanıyor. İkisi ayrı iş ve ikisi de kendiliğinden yürüyor.

**Ayda bir:** yüz işletme yeniden seçiliyor ve hızlı denetimler tazeleniyor. Yeni çekim yalnız liste beş yüzün altına düştüyse ya da şehir veya sektör değiştiyse yapılıyor; o zaman modül baştan çalışıyor ve sen sadece silme onayını veriyorsun.

**Her gün:** sabah bloğunda "günaydın" yazıyorsun ve o günün saha listesi hazır geliyor. Sen sıralamıyorsun, kimi arayacağına karar vermiyorsun; sıralamayı FounderOS kuruyor, CRM'de hazır böyle bir ekran yok. Liste telefondaki saha ekranında kart kart durur (bağlantı yoksa sayfanın Bugünün listesi sekmesinde): telefon, sahibi, bulgu, kanca, açılış cümlesi, itirazlar. Her aramadan sonra karttaki sonuç düğmesine basıyorsun (açmadı, istemedi, ilgilendi, randevu, sonra); sohbete yalnız cevap veren, randevu isteyen ya da yeni bir itiraz söyleyen aday için geliyorsun. Akşam sonuçları FounderOS kendisi alıyor; bağlantı yoksa "Sonuçları kopyala" deyip yapıştırıyorsun. Kayıtları ve yarının sırasını o yazıyor. Sıra sabit, dört basamak:

1. **Cevap verenler.** Mesajına dönmüş, telefonu açmış, "sonra ara" demiş herkes. En başta duruyorlar, çünkü cevap veren adayın ilgisi bir günde soğuyor.
2. **Takip günü gelenler.** Üçüncü, yedinci ve on dördüncü gün zincirinde bugüne düşenler.
3. **Denetimi hazır, sızıntı puanı yüksek adaylar.** Puanı yüksek olan önce; eşitlik yorum sayısıyla bozuluyor.
4. **Hızlı denetimi olmayanlar.** Sıranın sonu; bunlara ulaşılmadan önce yirmi saniyelik hızlı denetim yapılıyor, hızlı denetimsiz adaya hiçbir kanaldan ulaşılmıyor. Derin denetim ayrı: her sabah sıranın başındaki üç beş aday için, ilk aramalar onlara.

**Kaç kayıt:** çalışma düzenine göre günlük temas sayın kadar. Tam zamanlıysan yüz kayıt, işin yanında kırk. Fazlası hazırlanmıyor; ekranda gördüğün sayı o gün bitirilecek sayı.

**Liste beş yüzün altına düşerse:** uyarı o sabah düşüyor, ay sonu beklenmiyor. O hafta içinde bir sabah bloğu liste büyütmeye ayrılıyor, sıra şu: kartın diğer kategori adları, komşu iller, Türkiye geneli. Türkiye geneline açılırsa mesajlardan "sizin şehirde" cümlesi çıkıyor. Liste üç yüzün altına inerse bu artık liste sorunu değil, niş kararı haftanın kararına gidiyor.

### Listeyle ilgili tek kural

İkinci günde konuşmuştuk, bugün liste elinde olduğu için tekrar ediyorum.

İşletmeleri arıyor, onlara yazıyorsun; yaptığın iş normal bir iş.

Sadece şu düzeni koruyorsun: işletmenin Haritalar'da ilan ettiği numara, genel e-postası ve işletme olarak açtığı Instagram hesabı. Başka yerden bulduğun kişisel cep numarası ve kişisel hesap listeye girmiyor. İlk temasta nereden bulduğunu söylüyorsun. İstemeyen kişi aynı gün listeden çıkıyor ve bir daha aranmıyor.

Bu kadar. Öğrenci sebebini sorarsa kaynak ve kural anlatılmaz: "Bu işte böyle yürüyor, en güvenli yol bu."

## 6. Ne söyler

Açılışta: "Bugün bir saat. Çıktı: beş yüz kişilik liste ve içinden seçilen yüz kişi. Denetim ve prova günü sabah bu yüzü denetliyoruz, deneme aramaları da bu listeden yapılacak." İşin yanında "yüz" yerine "kırk" denir; sayı düzenden.
Çekim başlarken (aynı anda odak, `odak_yaz` `calisiyor`: panel Adaylar'daki Müşteri Bulma Motoru'nu açar): "Çekim başladı, birkaç dakika sürer. Panelde Müşteri Bulma Motoru açıldı; kayıtlar gelirken haritada ve tabloda canlı akar. Bitince kaç kayıt geldiğini ve kaçının neden işaretlendiğini söyleyeceğim." Panel linki yazılı değilse ikinci cümle söylenmez. Liste içeri alınıp yüz seçilince aracın `panel --yukle` komutu sessiz çalışır ve odak `bitti` gider (not: listenin kaç adayla kurulduğu; sonraki: "Devam").
Çekim bitince: "[toplam] kayıt geldi. [sayı] tanesinde telefon, [sayı] tanesinde e-posta, [sayı] tanesinde Instagram var. Servis [sayı] satırı işaretledi: [sayı] tekrar, [sayı] kapalı, [sayı] iletişimsiz, [sayı] zincir. Bunları listeye almıyorum, tamam mı? Görmek istersen gösteririm."
Daha az kayıt çekmek isterse: "800 çekiyoruz çünkü eleyeceğiz. Her işletmeye ilk temas ve üç takip gidiyor; beş yüzün altında kalırsan üçüncü haftada arayacak kimsen kalmıyor."
Tavan dolduysa: "Bu ayın tavanı doldu; servis gelecek ay yeniden açılıyor. Bugün tarayıcı eklentisiyle elle devam ediyoruz, yüz işletme çıkar."
Yorumları da çekelim derse: "Hayır. Yorumlara hızlı denetimde gözünle bakıyorsun, yüz işletme için yetiyor."

**Rakam kuralı.** Bu modülde iki ayrı küme var ve karıştırılırsa öğrenci sayıya güvenmiyor. Birincisi çekimden geleni anlatır (kaç kayıt geldi, kaçı işaretlendi), ikincisi listede kalanı anlatır (kaç aday var, kaçı aranabilir). Aynı rakam iki kümeye birden takılmaz. Kural üç maddeli:
- Çekim rakamlarını `cek --ozet` çıktısından, liste rakamlarını `ozet` çıktısından alırsın. İkisini de kendi cümlenden üretmezsin, araçtan okursun. Bir rakamı hatırından yazarsan önceki mesajla çelişir.
- Her rakamın yanında hangi kümeye ait olduğu söylenir: "servisten 677 kayıt geldi, 323'ünü işaretledim" ve "listende 354 aday var, 265'i aranabilir". "265'inde telefon var" cümlesi tek başına iki kümeye de yakışıyor, o yüzden hep kümesiyle söylenir.
- Günü kapatan başlık cümlesi, gerçekten ulaşılabilir sayıyla kurulur. "354 kayıtla aramalara başlıyorsun" yanlıştır; doğrusu "354 aday: 265'i aranabilir, 121'inin e-postası var, 98'inin Instagram'ı var". Üç sayı birden verilir, çünkü üç kol birden çalışıyor.
Günlük liste hakkında: "Listeyi sen sıralamıyorsun. Sabah açtığında bugünün kayıtları sırada: önce cevap verenler, sonra takibi gelenler, sonra puanı yüksek olan denetimi hazır adaylar."
Liste ilk kez yazılınca sayfa sohbete kart olarak açılır, sonra tek cümle: "Listen hazır, işte burada. Liste sekmesinde yeşil satır bugün sırada, turuncu satır günü geçmiş; Bugünün listesi sekmesinde bugün arayacakların kart kart, her kartta ne söyleyeceğin yazıyor; her aramadan sonra düğmeye bas." Arkasından ikinci cümle: "Klasöründe de duruyor, adı adaylar.html; istediğin zaman oradan da açarsın." Klasör tarifi ancak kart açılmazsa verilir.
Listeyi görmek isteyince: sayfa yeniden kart olarak açılır, tek cümle: "Veriyi yeniledim, işte liste."
Yüz işletme seçilince sohbette tek tablo: yüzün ilk onu, beş sütun: İşletme, Telefon, Site, Instagram, Neden bu işletme. İlk on, aday aracının `yuz-sec` çıktısının sonundaki "listenin başı" sırasıdır; panelde Adaylar'daki En çok istenen listesi de aynı sırayla açılır. Sırayı kendin kurma, csv'nin sırasından alma. Neden sütunu satırın ipuçlarından ve uygunluk gerekçesinden tek satır ("akşam 18.00'de kapanıyor, reklam veriyor", "yorumda 'telefona çıkmadılar' yazıyor"). Telefon, site ve Instagram işletmenin herkese açık kaydıdır; kişisel numara yazılmaz. Tablonun altında tek cümle: "Yüzün tamamı panelinde Adaylar'da; bir işletmeye dokununca bulgusu, mesajı ve demo düğmesi açılıyor." Satırların geri kalanı sohbete dökülmez.
Bitince: "Liste kayıt yerinde, yüz işletme işaretli. Bu akşam tanıdıklara ilk mesaj; denetim ve prova günü sabah bu işletmelerin denetimi, sonra kanıt ve mesaj metinleri." İşin yanında "kırk işletme".

## 7. Ne yazar

`adaylar.csv`'ye, aday aracıyla (CRM açık olsa da): bütün kayıtlar, aşamaları "yeni", "soğuk" işaretiyle, kaynağı ve nereden bulunduğu yazılı. En çok istenen yüz işletme ayrı işaretle. Sızıntı puanı ve en güçlü bulgu dördüncü bloğun hızlı denetiminde doluyor; denetim kartının kendisini aday-denetimi-cikar yazıyor.
Klasöre: `adaylar.csv` ve `adaylar.html`, aday aracıyla; ilk gün gizli `.founderos/` klasörü ve araç kurulur (aday-listesi-araci), niş kartının "Telefonda söylenecekler" bölümü ve öğrencinin adı, şehri sayfaya yazılır (aday-listesi-dosyasi, kurulum 3. adım); Bugünün listesi kartındaki Söyle metni oradan dolar.
İş Beyni'ne: listenin çıkarıldığı tarih, çekimin iş kimliği, ham kayıt sayısı, servisin işaretlediği ve onayla silinen sayılar, kalan sayı, yüz işletmenin seçim tarihi, hızlı denetimi biten sayı, kullanılan kategori adı ve kapsanan ilçeler, bu ayki kullanım ve tavan, yedek yol kullanıldıysa tarihi.
Bir sonraki modüllere: yüz işletme ve seçim sırası aday-denetimi-cikar'a, sızıntı puanı ve en güçlü bulgu adaya-mesaj-yaz ile video-mesaj-cek'e, denetlenen yüz işletme kanitini-hazirla'nın dördüncü gündeki deneme aramalarına, kategori adı ve seçilen yol bir sonraki ay tekrarı için kendine.

## 8. Yedek yol

- Veri servisi kapalıysa, çekim iki denemede de hata verirse ya da aylık tavan dolduysa: tarayıcı eklentisi yoluna geçiliyor; günün içinde geçiliyor ve bugünün çıktısı yüz işletme oluyor. Servis açılınca kalan kayıt servisten çekiliyor. O günün sırası şu:

  1. Claude'un tarayıcı eklentisini ve Google Haritalar'ı aç. Eklenti kurulu değilse kurulumu araclari-kur'un sekizinci bölümünde.
  2. Arama kelimesi: kartındaki kategori adı artı semt adı ("Nilüfer klima servisi" gibi). Şehri tek seferde aratmıyorsun, Haritalar belli bir sayıdan sonrasını göstermiyor; semt semt gidiyorsun ve taradıklarını bir kenara yazıyorsun.
  3. Eklenti her işletme kartından altı şeyi tabloya yazıyor: işletme adı, telefon, web sitesi, semt, yorum sayısı ve puan, varsa Instagram hesabı. E-posta bu yolda gelmiyor; siteyi açıp aramayı sadece yüz işletme için, hızlı denetim sırasında yapıyorsun.
  4. Bugün üç saatte yaklaşık yüz işletme çıkarıyorsun, aynı gün kayıt yerine yazıyorsun, yüz işletme seçimini bu kayıtlardan yapıyorsun. Kalanı dördüncü ve beşinci bloğun sabah bloklarına yayıyorsun: sahaya çıkarken elinde üç yüz kayıt oluyor, liste ilk hafta içinde beş yüze tamamlanıyor. Servis açılır açılmaz kalan kayıt servisten çekilir.
- Tarayıcı eklentisi de çalışmazsa: elle yazma, en son çare. Bir tabloya altı sütun açıyorsun (işletme adı, telefon, web sitesi, semt, yorum sayısı, Instagram) ve Haritalar'da çıkan her işletmeyi yazıyorsun. Yavaş yol, o yüzden önce diğer ikisi deneniyor. Yedek yoldan gelen kayıtlar da aynı dosyaya aracın ekle komutuyla girer (aday-listesi-dosyasi).
- Şehrinde 500 çıkmazsa: kartın diğer kategori adları, sonra komşu iller, sonra Türkiye geneli. Üçü de yetmezse niş kararı haftanın kararına gidiyor.
- Hızlı denetim dördüncü bloğun sabahında yarıda kalırsa: deneme aramaları denetlenen kadarıyla yapılıyor, kalanı ertesi sabah bitiyor; saha ertelenmiyor.
- Aday aracı yazamazsa: yedek yol aday-listesi-dosyasi'nın "Araç çalışmazsa" bölümünde; liste CRM'e yüklenerek kurtarılmaz.
- Bir saat aşılırsa: liste, temizlik, yüz işletmenin seçimi ve klasöre yazım yine bugün bitiyor; denetim zaten ertesi sabahın işi.

## 9. Sıradaki adım ve işaretler

Sıradaki: bu akşam tanıdıklara ilk mesaj (tanidiga-mesaj-yaz); bir sonraki blokta kanıt ve mesaj metinleri.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Üçüncü gün bitti, liste klasöre yazılmadı: dördüncü günün ilk işi olur ve o günün akışı bir saat kayar.
- Yüz işletme seçilmedi: dördüncü günün ilk on beş dakikasında seçilir, hızlı denetim ondan sonra başlar.
- Aynı işletme hem sıcak hem soğuk listede görünüyor: altıncı eleme atlanmış, soğuk mesaj durdurulur.
- Bir ay geçti, liste yenilenmedi: modül ikinci kez açılır.

Beş kural: boş sayfa yok (kategori adı, çekim, altı eleme ve seçim ölçütleri hazır gelir) · sessiz bitiş yok (akşam liste kayıt yerinde ve yüz işletme işaretli) · onay (silinecek satırları görüp onaylıyorsun) · sahadan güncelleme (her ay liste ve yüz işletme yenilenir, her gün saha listesi yeniden sıralanır) · sormaz söyler (kategoriyi, sayıyı, elemeleri ve seçim ölçütlerini FounderOS söyler; listenin nereden geleceği de sorulmaz).
