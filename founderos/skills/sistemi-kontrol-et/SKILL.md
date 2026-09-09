---
user-invocable: false
name: sistemi-kontrol-et
description: Her hafta, her müşteri için. Sistem sessizce bozuldu mu.
---

# sistemi-kontrol-et

## 1. Adı, rolü, pazarlamadaki karşılığı

Canlıya alınmış müşteri sistemlerinin haftalık bakımını yapan modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Canlıya alma, sistemin gerçekten çalışmaya başlaması demek; altıncı günde yapılır. Bu modül yedinci günden itibaren devreye girer ve müşteri devam ettiği sürece her hafta çalışır.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil.

Neden bu iş var: kurulan sistem sessizce bozulur. Sessizce bozulan şeyler şunlar:
- Şablon duraklatılır. Şablon, WhatsApp'ın sahibi Meta'nın önceden onayladığı hazır mesaj metnidir.
- Numaranın kalite notu düşer. Hat, müşterinin WhatsApp mesajlarının gittiği telefon numarasıdır; WhatsApp o numaraya bir kalite notu verir, not düşerse gönderim daralır.
- Facebook bağlantısının süresi dolar.
- Takvim kopar.
- Akış hata verir. Akış, bir olay olunca kendiliğinden çalışan adım zinciridir; mesajı o gönderir.

Hiçbiri sana haber vermez. Sen fark etmezsen müşteri fark eder, o zaman sonucu düzeltsen bile güven gider.

Tek kural: bozukluğu müşteriden önce sen bulacaksın.

Bozukluk çıkması normaldir, her hafta bir şey çıkar. Kötü olan bozukluk değil, senin geç görmen. Aşağıdaki sıra bunun için var.

Üç tehlikeli ayrıntı var:
1. Akış hatası bildirimi kapalı gelir. Kurulumda açılır, ama açılsa bile WhatsApp gönderimini ve takvim adımlarını kapsamıyor. Yani açacaksın, yine de elle bakacaksın.
2. Takvim koptuğunda bildirim yalnız takvimin sahibine gider. Alt hesap ya da ajans yöneticisine gitmiyor, yani sana gelmiyor. Bu kapatılamaz bir boşluktur. Tek çare her hafta takvime kendin bakmak ve müşteriye "bu e-posta gelirse bana ilet" kuralını yazılı vermek.
3. Bağlantı süresi uyarısı da kapalı olabilir. Kapalıysa Facebook bağlantısı haber vermeden ölür.

Şunlar bu modülün işi değildir:
- Sistemi kurmak ve beşinci gün test etmek (musteri-sistemini-kur).
- Asistanın ilk hafta izlenmesi. Altıncı günden on ikinci güne o iş yazili-asistani-kur'da, günde tek düzeltme. On üçüncü günden sonra buraya geçer. Sesli ajanın ilk haftası da aynı: canlıya alındığı günden yedi gün sesli-ajani-kur izler, sonra buraya geçer.
- Eski müşteri gönderimi sürerken hattın kalite notuna göre karar vermek (kaybolanlari-geri-getir).
- Raporu yazmak (aylik-raporu-hazirla). Sekizinci ve on dördüncü günün akşamında giden üç satırlık ara rapor da orada; burası ona sayı üretmez, o sayılar CRM'den okunur.
- Müşteri ilişkisini yönetmek (musteriyi-elde-tut).
- Kötü haberi vermek (zor-konusmayi-yonet).
- Senin kendi işinin haftalık kontrolü ve kaç müşteri taşıyabileceğin. O ayrı iştir (degisiklige-karar-ver ve rakamlari-oku).

Pazarlamadaki karşılığı: müşterinin ödediği şey sadece kurulum değil, sistemin çalışmaya devam etmesi.

## 2. Ne zaman çalışır

- Her hafta aynı gün. Gün ilk ayda haftalık görüşmeden bir gün öncesidir; böylece görüşmeye elin dolu girersin. Görüşmeler seyrekleşince o gün sabit kalır, kontrol yine her hafta aynı gün yapılır. Gün kurulumda bilgi dosyasına yazılır.
- Kontrolün penceresi akşam bloğudur. Dokuz madde bir oturumda bitmiyorsa hafta sonuna alınır, parça parça yapılmaz. Müşteriyle yapılan haftalık görüşme ise ayrı bir iştir ve kurulum bloğundadır; işin yanında çalışıyorsan akşam ya da hafta sonu.
- Yedinci günden itibaren her müşteri için.
- On üçüncü günden sonra asistanın izlenmesi de bu kontrolün içine girer.
- Ayda bir, kontrolün içine iki madde daha eklenir: bağlantı bildirimlerinin açık olması ve müşterinin kendi ayarlarında ne değiştirdiği.
- Bağlanma tarihinden elli gün sonrası: Facebook ve Instagram bağlantısını yenileme işi takvime düşer.
- Bir şey bozulduğu anda: bekleme, aynı gün düzelt. Bu, asistanın davranış ayarı için geçerli değil; o ayrı, aşağıda yazıyor.

## 3. Ne okur

Bütün ekran yolları CRM'de, o müşterinin alt hesabının içindedir. CRM, adayların ve müşterilerin kaydedildiği takip programıdır. Önce CRM'e girersin, üstten o müşterinin alt hesabını seçersin, sonra aşağıdaki yolları izlersin. İki madde CRM'de değil, onların yeri ayrıca yazıyor.

CRM'den: akışların hata listesi, randevular, gelen mesajlar, asistanın konuşmaları, bağlantı kutularının durumu, değişiklik kaydı (kimin neyi ne zaman değiştirdiğini gösteren liste).
Meta'nın WhatsApp yönetim ekranından: hattın kalite notu ve hattın günlük mesaj sınırı. Bu ekran CRM'in içinde değil; Meta'nın işletme hesapları için açtığı ayrı bir sayfadır. Müşterinin kurulumunda kullandığın Meta hesabıyla girersin. Bu panelin her müşteride açılacağı garanti değil; açılmadığı bilgi dosyasında yazıyorsa bu iki satırın yerine yedek ölçü okunur, beşinci maddede yazılı.
Bilgi dosyasından (İş Beyni'nin müşteriler bölümü; her müşteri için tuttuğun geniş dosya): kurulan parçalar, kapsam dışı kalanlar, ayarların başlangıç değerleri, geçen haftaki kontrolün notları ve sayıları.
Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): "Sezon" bölümü, yoğun saatler için "Kanal ve zaman" bölümü.

## 4. Ne sorar

Sormaz. Kontrol listesini, sırasını ve ekran yollarını FounderOS verir. Senden aldığı iki şey: her maddenin sonucu ve bozuk bir şey bulduysan ne yaptığın.

## 5. Ne yapar

### Haftalık kontrol: dokuz madde, bu sırayla

Sıra rastgele değil. Önce en sessiz bozulanlar, en sona göze çarpanlar.

Bir istisna: geçen haftadan kalan bir bozukluk varsa ya da FounderOS sana "şununla başla" dediyse o iş dokuz maddenin önüne geçer. Sıranın geri kalanı aynı kalır.

**1. Geçen haftadan kalanlar.** Geçen kontrolde bulunan bozukluk düzeldi mi. Düzelmediyse bu haftanın ilk işi budur. Şu üç durumda FounderOS zaten sana "önce bununla başla" der: müşterinin Google puanı yarım puan düştüyse, müşteri iki haftadır rapora cevap vermiyorsa, ya da aynı parça iki kontrolde de bozuk çıktıysa.

**2. Takvim.** Alt hesapta ayarlar, takvimler, takvimin yanındaki "sorun giderme" düğmesi. Kontrol ettikleri:
- personelin müsait görünmemesi
- iki takvimin birbirine yazamaması
- yetki sorunları
- çakışma ve aynı saate iki randevu
- kapalı görünen saatler
Kapalı bir saatin üstüne gelince sebebi yazar. Dört sebep var: uygun personel yok, müşterinin Google takvimindeki bir etkinlikle çakışıyor, iki randevu arasındaki tampon süre engelliyor, ya da takvimi dolu gösterme ayarı gizliyor.
Bir hatırlatma: müşterinin Google takviminde "meşgul" işaretli olmayan etkinlik saati kapatmaz. Aynı saate ikinci randevu çoğunlukla bundan çıkar.
Takvim kopmuşsa yolu farklıdır: ayarlar, kendi profilim, takvim ayarları. Bağlantıyı silip yeniden kurar, sonra denersin. Mevcut randevular kaybolmaz.

**3. Akış hataları.** Alt hesapta akışlar bölümü, "gözden geçirilmesi gerekenler" sekmesi. Hatalı akış varsa akışı aç. Solda açılan hata listesinde iki başlık vardır: bağlantı sorunları, ve doldurulması zorunlu olup boş kalan satırlar. Sen düzeltirsin ve "hata görüldü" diye işaretlersin.
Hatanın ne olduğunu anlamadıysan ekranı bana anlat, hangi düğmeye basacağını adım adım söylerim. Kendi kafana göre akışın içini değiştirme.

**4. Şablon durumları.** Alt hesapta WhatsApp, şablonlar bölümü. Her şablonun bir durumu var:
- incelemede: Meta bakıyor, yirmi dört saate kadar sürebilir
- reddedildi: metni düzeltip yeniden gönderirsin ya da itiraz edersin
- itiraz incelemede
- onaylı, kalite bekleniyor: gönderilebilir, henüz geri bildirim toplanmamış
- onaylı, yüksek kalite: en iyi durum
- onaylı, orta kalite: yakında duraklatılabilir, metni düzeltirsin
- onaylı, düşük kalite: hâlâ gider ama risk altında, metni düzeltirsin
- duraklatıldı: ilk seferde üç saat, ikinci seferde altı saat gönderilemez. Metni düzeltip yeniden gönderirsin.
- kapatıldı: üçüncü seferde olur, o şablon bir daha gitmez. Yeni metinle yeni şablon açarsın.

**5. Hattın kalite notu.** Bu madde on üçüncü günden sonra başlar. Sekizinci ile on ikinci gün arasında hattın notuna eski müşteri gönderimi sırasında bakılıyor, sen burada tekrar bakmazsın.
Yer: Meta'nın WhatsApp yönetim ekranı, telefon numaraları sekmesi, kalite notu sütunu. Not üç renk: yeşil, sarı, kırmızı. Son yedi güne bakar.
Panele hiç giremiyorsan (kurulumda bunu test etmiştin ve bilgi dosyasında yazıyor) bu madde atlanmaz, yerine yedek ölçü bakılır: CRM'in konuşmalar ekranında o haftanın giden şablon mesajlarında teslim edilmeyen var mı, ve hafta içinde engelleme ya da şikâyet bildirimi geldi mi. Teslim edilmeyen sayısı bir öncekine göre belirgin arttıysa sarı kabul eder, aşağıdaki sarı kuralını uygularsın.
Sarıysa o hafta toplu gönderim yarıya iner. Kırmızıysa yeni toplu gönderim durur. Randevu onayları ve hatırlatmaları durmaz, onlar gitmeye devam eder.
Not düştükten sonra yedi günün var: o süre içinde düzelmezse hattın günlük sınırı bir kademe iner.
Hattın günlük mesaj sınırı da aynı panelde, hesap araçları, mesajlaşma sınırları bölümünde. Bu sınır hattın bir günde kaç yeni kişiye kendisi mesaj başlatabileceğidir; e-postanın günlük gönderim sınırıyla karıştırma.

**6. Bağlantılar.** Alt hesapta ayarlar, bağlantılar. Her bağlantının ekranda bir kutusu var, kutunun içinde üç durumdan biri yazar: bağlı, dikkat gerekiyor, kopmuş. Burada bakılacaklar: Facebook, Instagram, Google işletme profili. Kopmuş olan varsa hata göstergesine tıklar, açılan pencereden yeniden bağlarsın.
WhatsApp bu kutuların içinde değil, kendi ekranındadır. WhatsApp koparsa yeniden bağlama müşterinin telefonuyla kare kod okutmayı gerektirir; aynı gün müşteriden randevu alırsın, tek başına halledemezsin.

**7. Asistanın konuşmaları.** Bir haftanın bütün konuşmasını okumak mümkün değil, o yüzden örnekleme yaparsın: insana devredilen konuşmaların hepsi, artı rastgele on konuşma. İnsana devir, asistanın konuşmayı bırakıp işi insana bırakmasıdır.
Aradığın üç şey: uydurma cevap, fiyat verme, randevu yazmadan kapatma.
Karşılıkları:
- İki konuşmada uydurma çıktıysa cevap listesi eksiktir, doldurulur. Cevap listesi, asistanın bakıp cevap verdiği hazır bilgilerdir.
- Aynı soru üç konuşmada takıldıysa cevap listesine eklenir.
- İnsana devir oranı yarıdan fazlaysa asistanın soru sırasının ilk sorusu değiştirilir. Sağlık nişleri bunun dışındadır.
Sen konuşmaları okur, bana tek satır yazarsın; düzeltmeyi ben yaparım, haftada tek düzeltme. Düzeltme asistanın kurallarında ve cevap listesinde olur, kurulum ayarlarına dokunulmaz.
Tek istisna: müşteri asistanın bir cevabından şikâyet ettiyse o aynı gün düzeltilir, haftada tek düzeltme kuralının dışındadır.

**8. Yorumlar.** Yeni yorum var mı, cevapsız yorum var mı, puan ne oldu.
- Cevap metni yazıldı ama müşterinin onayı iki gün gelmediyse hatırlatırsın. Onay geldikten sonra yirmi dört saat içinde yayınlanır.
- Ortalama puan yarım puan düştüyse bu, gelecek haftanın ilk maddesidir. Yorum isteği durmaz. Son gelen kötü yorumları okur, ortak şikâyeti tek cümleyle yazar ve haftalık görüşmede müşteriye sorarsın: bu şikâyet gerçekten yaşanıyor mu.
- Otuz yorum isteği gitti ve hiç yorum gelmediyse istek anına ve metne bakılır.
- "Bir daha yazmayın" diyen varsa üç iş günü içinde işlenir. Kanun bunu istiyor. Bu kuyruğun boşaldığını her hafta doğrularsın.

**9. Sayılar.** Geçen haftanın rakamları alınır ve bir öncekiyle karşılaştırılır:
- randevu sayısı
- gelme oranı, yani randevu alanların kaçının gerçekten geldiği. Ölçüt yüzde yetmiş; altındaysa sorun randevuda değil hatırlatmadadır.
- asistanın insana devir sayısı
- cevapsız aramaya dönüş sayısı
- gelen mesaj sayısı
Bir de şunu doğrularsın: talep geldiğinde bildirim zinciri çalışmış mı. Otuz dakikada dönülmeyen talebe ikinci bildirim, iki saatte dönülmeyene müşterinin kendisine bildirim gidiyor. Bu zincirin çalıştığını görmezsen sistemin en kritik parçası ölmüş demektir.

### Dokuz maddeden sonra tek soru

Dokuz madde bittiğinde ekranda gördüklerini bir kenara bırakır, o hafta müşteriyle olan yazışmalarını ve konuşmalarını hatırlar ve bana tek soruya cevap yazarsın: bu hafta bu müşterinin tonu değişti mi.

Cevap "hayır" ise tek kelime yazarsın, iş biter. Cevap "evet" ise ne değiştiğini tek cümleyle yazarsın. Aradığın dört şey var: küçük şikâyetlerle sürekli mesaj atmaya başladı mı, kendi satış sorunları için seni suçluyor mu, ayrılmak için dosya hazırlıyormuş gibi konuşuyor mu, aldığı şeyi anlamadığını gösteren sorular soruyor mu.

Bu soru tekniğin dışındadır ve ekranlarda görünmez. Sistemin dokuz maddesi yeşil olabilir, müşteri yine de gitmeye hazırlanıyor olabilir. Ayrılma haftalar önce tondan belli olur ve bunu sadece sen duyarsın. Cevabın "evet" olduğunda ne yapılacağını musteriyi-elde-tut söyler; sen burada sadece bildirisin, kendi başına görüşme ayarlamazsın.

### Ayda bir eklenen iki madde

**Bildirimler açık mı.** Üç bildirimin açık olduğunu doğrularsın: akış hatası bildirimi, sosyal hesap bildirimleri (pazarlama, sosyal planlayıcı, dişli simgesi, bildirimler; açılacak türler hesap süresi doldu, süre dolmadan uyarı, gönderi başarısız), ve takvim bildirimleri (kendi profilim, bildirimler, takvim).

**Değişiklik kaydı.** Alt hesapta ayarlar, değişiklik kayıtları. Kim neyi ne zaman değiştirmiş görürsün, altmış gün geriye gider. Aradığın şey şu: müşteri kendi bildirimlerini kapattı mı, bir ayarı değiştirdi mi, birini hesaptan çıkardı mı. Sistem çalışmıyor gibi görünen şeylerin çoğu buradan çıkar. Kayıt altmış günde siliniyor, o yüzden bir kontrol atlanırsa değişiklik kaydına önce bakarsın.

Facebook ve Instagram bağlantısının bir süresi var ve dolunca ölüyor. Kesin bir gün sayısı yazmıyor ama uyarı bildirimi altmış günlük bir döngüye göre ellinci gün civarında geliyor. Bir de şu: şifre değişikliği, yetkinin kaldırılması ya da oturumun kapatılması bağlantıyı süre dolmadan da koparır. Bu yüzden bağlanma tarihinden elli gün sonrası takvime iş olarak düşer ve bağlantıyı orada yenilersin.

Google işletme profilinin bağlantısı için bir süre yazmıyor. Yine de aynı bağlantılar ekranından, ayda bir onun da bağlı göründüğüne bakarsın.

### Bozuk bir şey bulunca

Arıza arama sırası dörttür ve bu sırayla gidilir:
1. Olağandışı bir durum var mı. Bayram, tatil, müşterinin dükkânı kapalı, personeli izinde. Varsa sistemde arama, sebep bu.
2. Girdiye bak. Mesaj geliyor mu, arama düşüyor mu, form dolduruluyor mu. Girdi yoksa çıktı da yok.
3. Sürece bak. Bir şey değişmiş mi. Çoğu arıza birinin bir ayarı değiştirmesinden çıkar.
4. Dışarıya bak. Bağlantı kopmuş mu, günlük gönderim sınırına takılmış mı, WhatsApp ya da Google tarafında bir şey değişmiş mi.

Düzeltme sırası beş adımdır:
1. Sahiplen. Bahane yok. Teknik olarak senin hatan olmasa bile.
2. Hızlı düzelt. Bu her şeyi bırakmak anlamına geliyorsa bırak.
3. Sade anlat. Müşterinin anlayacağı dille ne olduğunu söyle.
4. Tekrarını önle. Aynı şey bir daha olmasın diye ne yaptığını göster.
5. Telafi et. Küçük bir jest, faturadan uzun süre hafızada kalır.

Müşteriye söyleme kuralı: bozukluğu sen bulduysan ve aynı gün düzelttiysen yine de söylersin. "Şu oldu, şunu yaptım, şu an çalışıyor" cümlesi güven kazandırır.

Arıza sırasında gelen mesajları sen tek tek okur ve cevaplarsın. Telefonla dönülmesi gereken varsa müşteriye o listeyi verirsin.

### Müşteri sistemi kendi bozarsa

Olur. Yapabilecekleri:
- bildirimi kapatır
- uygulamayı siler
- telefonu değiştirir
- birini hesaptan çıkarır
- takvimi başka bir hesaba bağlar

Yapacağın: değişiklik kaydından ne olduğunu bulur, düzeltir, müşteriye tek cümleyle sen yazarsın. Suçlama yok.

Aynı şey ikinci kez olursa sebebini sorarsın. Müşteri bilerek kapattıysa sebebi vardır ve o sebep sistemin ayarında düzeltilir.

### Kapsam ve ücret

Haftalık kontrol aylık ücretin içindedir, ayrıca ücretlendirilmez.

Kapsam dışı olan: müşterinin sonradan istediği yeni parça, yeni kanal, yeni akış, başka bir yazılıma bağlanma. Bunları müşteriyle ayrıca konuşursun. En erken ikinci ayda, büyüme şartı sağlanınca açılır. Büyüme şartı iki maddedir: görüşmede satılan tam sistem, yani Kademe 2, ilk müşteride sorunsuz teslim edilmiş olacak ve yirmi birinci gün raporu çıkmış olacak.

Ayda birkaç küçük istek normaldir, onları yaparsın. Yeni parça, yeni kanal, yeni akış ya da başka bir yazılıma bağlanma isteği küçük istek değildir; o kapsam dışıdır ve müşteriye yazılı sen söylersin.

Kaç müşteri taşıyabileceğin bu modülün işi değil. Dört aktif müşteriye ulaştığında bakım yükü konuşulur, kararı degisiklige-karar-ver verir.

## 6. Ne söyler

Kontrol gününde: "Bugün bakım günü, akşam bloğu, dokuz madde. Sıraya uy; en tehlikeli olanlar en sessiz bozulanlar, onlar ilk beş maddede. Her hafta bir şey çıkar, bu normal."
Bozukluk bulununca: "Şunu buldum. Şimdi düzeltiyorum, sonra müşteriye tek cümle yazacaksın. Sen söylemezsen o bulur; o bulursa on dakikada düzelttiğin şey ikinci ay ödemesini tartışmaya açar."
Kırmızı not çıkarsa: "Hattın notu kırmızı. Bu hafta yeni toplu gönderim yok, randevu hatırlatmaları gitmeye devam ediyor. Üstüne mesaj atarsak önce uyarı, sonra günlerce engel gelir, en sonu süresiz kilit. Yedi günün var; bu sürede düzelmezse günlük sınır bir kademe iner."
Müşteri bir şeyi kapatmışsa: "Bildirimler kapanmış. Suçlama yok, açtım; kapalıyken gelen üç talebi de arattım. Üçü de bugün aranmasa kaybolurdu. Sebebini sor, ikinci kez olursa ayarı değiştireceğiz."
Anlamadığın bir hata görürsen: "Ekranı bana anlat, adım adım söylerim. Akışın içini kendi kafana göre değiştirme; bir hafta boyunca hiçbir mesaj gitmeyebilir."

## 7. Ne yazar

Bilgi dosyasına: her haftalık kontrolün tarihi, o kontrolün kaç dakika sürdüğü (haftalık bakım süresi; kapasite kararı bu satıra bakar), dokuz maddenin sonucu, dokuzuncu maddedeki beş sayının o haftaki değerleri, bulunan bozukluk ve ne yapıldığı, müşteriye ne yazıldığı, düzelmeyen ve haftaya kalan işler, bağlantı yenileme tarihleri.
CRM'e: kontrol yapıldı ve tarihi, açık kalan arıza.
Niş kartının Sahadan dolacak bölümüne: bu nişte en sık bozulan parça, sezonda değişen ayar.

## 8. Yedek yol

- Bağlantı kopmuşsa: aynı gün müşteriye sen yazarsın ve yeniden bağlamayı denersin. Üç gün içinde bağlanamazsa o kanal kapsam dışına alınır; kapsam dışı kalan parça güvencenin sonucuna sayılmaz.
- Şablon duraklatıldıysa: üç ya da altı saat bekler, metni düzeltip yeniden gönderirsin. Kapatıldıysa yeni metinle yeni şablon açarsın.
- Hattın notu kırmızıysa: yeni toplu gönderim durur, yeşile dönene kadar beklenir, müşteriye sebebini sen yazarsın.
- Takvim kopmuşsa: ayarlar, kendi profilim, takvim ayarları. Bağlantıyı silip yeniden kurar, sonra denersin.
- Arıza senin çözebileceğin bir şey değilse: müşteriye aynı gün sen haber verirsin, ne zaman döneceğini söylersin, söylediğin günde dönersin.
- Aynı parça iki kontrolde de bozuk çıktıysa: kurulum yanlış demektir, iş musteri-sistemini-kur'a döner ve o parça baştan kurulup yeniden test edilir.
- Kontrol günü kaçtıysa: ertesi gün yaparsın, atlamazsın. Atlanan haftada önce değişiklik kaydına bakarsın, çünkü o kayıt altmış günde siliniyor.
- Müşteri haftalık özeti istemiyorsa: özeti göndermezsin. Ama bulduğun bozukluğu ve ne yaptığını yine tek cümleyle yazarsın, o kural değişmez.

## 9. Sıradaki adım ve işaretler

Sıradaki: haftalık görüşme (ilk ay musteriyi-karsila, sonra musteriyi-elde-tut), aylık rapor (aylik-raporu-hazirla), kötü haber varsa zor-konusmayi-yonet.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Kontrol iki hafta üst üste yapılmadı: sabah planının ilk işi olur.
- Aynı parça iki kontrolde de bozuk çıktı: parça baştan kurulur.
- Bağlantı kopmuş ve üç gün geçti: o kanal kapsam dışına alınır, müşteriye yazılı bildirilir.
- Gelme oranı yüzde yetmişin altına düştü: hatırlatma akışına bakılır.
- İnsana devir oranı yarıdan fazla (sağlık nişleri hariç): asistanın soru sırasının ilk sorusu değiştirilir.
- Ortalama puan yarım puan düştü: gelecek kontrolün ilk maddesi olur.
- Müşteri iki haftadır rapora cevap vermiyor: gelecek kontrolün ilk maddesi olur.
- Dört aktif müşteriye ulaşıldı: bakım yükü degisiklige-karar-ver'de konuşulur.

Beş kural: boş sayfa yok (dokuz maddelik liste ve ekran yolları hazır gelir) · sessiz bitiş yok (bulunan her bozukluk müşteriye tek cümleyle bildirilir) · onay (müşteriye giden cümle senin elinden çıkar, yorum cevabı müşterinin onayıyla yayınlanır) · sahadan güncelleme (bu nişte en sık bozulan parça karta yazılır) · sormaz söyler (listeyi, sırayı ve ekran yollarını FounderOS verir).
