---
user-invocable: false
name: video-mesaj-cek
description: "Kurulum beşinci gün, sonra yazı yolunda her gün. En çok istenen yüz işletmeye kişisel video mesaj."
---

# video-mesaj-cek

## 1. Adı, rolü, pazarlamadaki karşılığı

Yazı yolundaki öğrencinin modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır; bu modül, en çok istenen yüz işletmeden seçilmiş adaya, o adayın denetim kartından çıkan bulguyu ekranda göstererek bir dakikalık video mesaj çektirir ve gönderdirir. Yazmak değil çekmek olduğu için ayrı modül.

Şöyle düşün: yazı okunmaz, geçilir. Yüz ve ses geçilmez. Ekranda kendi işletmesinin sayfası açıkken hiç geçilmez. Video emek gösterir, şüpheyi düşürür, işletmeciye "bu bana çekilmiş" dedirtir. Yerel işletmeci büyük şirketlerden yanmıştır, karşısında insan ister. "Ben de bu şehirdeyim" demek seni bir e-posta adresinden yakındaki gerçek bir insana çevirir.

**Bu modül denetim yapmaz, denetimi okur.** Videonun omurgası aday-denetimi-cikar'ın çıkardığı denetim kartıdır. Ekranda gösterilen şey EN GÜÇLÜ BULGU'nun kendisidir; senaryo o bulgunun etrafına kurulur. Kart yoksa video da yok. **Denetimsiz adaya video çekilmez**, istisnası da yoktur: sabah listesinde denetimi olmayan bir aday görünürse o satır atlanır, yerine listenin altındaki denetimi hazır aday gelir.

Videoya kimin gireceğini de bu modül seçmez. Seçimi adaya-mesaj-yaz'daki karar tablosu yapar: sızıntı puanı dörtten yüksek, aday en çok istenen yüz işletmeden, yazı yolu, ilk yazılı temasın üçüncü günü ve hâlâ cevap yok. Bu satır uyduğu gün o aday video listesine düşer, burası da çeker.

Pazarlamada bunun adı: en çok istediğin yüz işletmeye, her ay, tek tek kendi elinle uğraşmak. Doğru yüz kişi, yanlış yüz bin takipçiden değerlidir.

Şunlar bu modülün işi değildir: denetimin kendisi (aday-denetimi-cikar), hangi adaya hangi gün hangi kanalın geleceği kararı (adaya-mesaj-yaz), ön görüşme videosu ve üç itiraz videosu (satis-videosunu-cek, ön görüşme sayfasında durur), kendi sisteminin demo ekran kaydı (kanitini-hazirla), rapor günü müşteri videosu, yazılı mesajlar (adaya-mesaj-yaz). Telefon yolunda video yok; orada en çok istenen yüz işletme aranır.

## 2. Ne zaman çalışır
- Beşinci gün, sabah bloğu, kırk dakika. Yirmi beş dakika kurulum: ekran kaydı programı ve YouTube bir kez ayarlanır. On beş dakika deneme: listenin en altındaki bir adayın denetim kartıyla bir deneme videosu çekersin. Kimseye gitmez. Bir kez izlersin, beş maddelik listeye bakarsın, ikinci kez izlemezsin. Kanal dördüncü blokta kisisel-markani-kur ile açılmıştı, video oraya yükleniyor.
- Altıncı günden itibaren, yazı yolunda, her gün. En çok istenen yüz işletmeye ilk yazılı temas günde beş adayla yayılır; bu beş, günün kırk e-postası ve otuz Instagram mesajının içindedir. Video, o ilk temasın üçüncü günü, cevap gelmediyse, iki kanaldan aynı gün gider. Yani her gün beş yeni ilk temas, beş video.
- Videonun yeri saha bloğunun son yarım saatidir; denetim kartları o sabah zaten okunmuştur, video çekilirken kart açık durur.
- İlk hafta ilk temas da video da günde üç, bir saat; ikinci haftadan itibaren ikisi de beş, doksan dakika. İşin yanında çalışıyorsan ilk temas da video da günde iki, saha bloğunun sonunda, kırk dakika; en çok istenen listen kırk işletme.
- İşin yanında çalışanda hedef iki dönemde yarıya iner: ilk müşterinin bütün teslim süresi, yani sıfırıncı günden rapor gününe, ve şirket kuruluş günü. O günlerde iki değil bir video çekilir, süre yirmi dakikaya iner. Sebebi rakamda: [21/28] günlük teslim elli saat alıyor ve o saatler akşamdan çıkıyor. Sıfır video günü yine olmaz.
- Yüz işletme yaklaşık dört haftada biter; ilk hafta üçle başladığın için birkaç gün fazlasıyla. Ay sonunda aday-listesi-cikar yeni yüz işletme seçer, aday-denetimi-cikar onların hızlı denetimini yapar.
- Cevap gelirse o adaya video durur; konuşma adaya-mesaj-yaz'ın üç adımlı cevap konuşmasıyla sürer. Üç adım: önce dinlediğini belli edersin, sonra göremediği şeyi söylersin, sonra saat teklif edersin.

## 3. Ne okur

**Denetim kartından (aday-denetimi-cikar), üç satır. Videonun gövdesi budur.**
- EN GÜÇLÜ BULGU: tek cümle, o adayda gerçekten görülmüş şey. Ekranda gösterilecek olan bu.
- LİRA KARŞILIĞI: kayıp birimi çarpı kartın rakamı, tek satır hesap.
- SIRADAKİ KANAL: bu adayda "video" yazıyorsa video çekilir.

Kartın altıncı ve yedinci satırı da okunur: canlı arama testi ve yazılı test. Yaşanmış kanca oradan çıkıyor, "dün akşam yedide aradım, açan olmadı" cümlesinin kaynağı o satır.

Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv`): en çok istenen yüz işletme işareti, dört kanalın durum satırları, sıradaki hareket satırı, ilk temas tarihi ve kanalı, cevap durumu, sahibinin adı, Instagram hesabı, e-posta adresi.

İş Beyni'nden: Dönüşüm Cümlesi, sistemin adı, şehir, Instagram hesabının yaşı, kanıt cümlesi, YouTube kanalı hazır mı.

Niş kartından: kayıp birimi, işletmecinin sözlüğü, yasal sınırlar (sağlıkta fiyat, "en iyi", öncesi-sonrası, hasta yorumu; güzellik ve kuaförde tıbbi işlem; sigortada acente unvanı).

## 4. Ne sorar

Sormaz. Günün adaylarını karar tablosu seçer, senaryoyu FounderOS yazar, hangi ekranın açılacağını FounderOS söyler. Çekimden hemen önce cevap durumuna yeniden bakılır; cevap gelen listeden düşer.

Sabahki tek satırlık kişisel gözlem kalktı. Yerini denetim kartının en güçlü bulgusu aldı. Fark şu: gözlem "gördüğüm bir şey", en güçlü bulgu "kaçırdığın müşteri". İkincisi ekranda gösterilebiliyor, birincisi gösterilemiyordu.

Senden aldığı üç şey: her video için "gitti" ve hangi kanaldan gittiği, e-posta metni için "tamam", ekran kaydı programında bir şey görünmüyorsa ekran görüntüsü.

## 5. Ne yapar

### Denetimi tüket, kendin denetim yapma

Çekilir: en çok istenen yüz işletmeden, denetim kartı hazır, sızıntı puanı dörtten yüksek, ilk yazılı temasın üçüncü gününde hâlâ cevap vermemiş, sahibinin adı bilinen aday.

Çekilmez: denetimi olmayan aday, cevap vermiş aday, tanıdık, sahibinin adı olmayan işletme, Instagram hesabı yeni ve e-posta adresi de olmayan aday. Cevapsız ilk temas "bizi biliyor" saymaz; "bizi biliyor" olan, tanıdıktan yönlendirilen, daha önce konuşulmuş ya da siteni ziyaret etmiş adaydır. Bir adaya bir video.

Aynı adaya daha önce e-posta gittiyse video, e-postanın söylemediği ikinci bulguyu gösterir. Bir bulgu iki kanalda aynı cümleyle kullanılmaz.

Denetim kartının kendisi ekranda gösterilmez ve adaya gönderilmez. Ekranda kartın işaret ettiği gerçek sayfa açılır, kart değil. Kartı gönderirsen işletmeci "sağ ol" der, sayfayı elemanına verir, görüşme hiç olmaz.

### Hangi bulgu ekranda nerede durur

Kartın en güçlü bulgusu hangi satırdan geldiyse ekranda o sayfa açık durur. Sıra kartın kendi sırasıdır.

- **Arama testi (kartın altıncı satırı).** Ekranda adayın Google işletme profili ve numarası durur. Aramanın kendisi ekranda gösterilmez, sen sözle söylersin: "Dün akşam yedide bu numarayı aradım, açan olmadı."
- **Yazılı test (yedinci satır).** Senin gönderdiğin mesajın ekranı açılır: gönderdiğin saat ve altındaki boşluk görünür. Cevapsız boşluğu göstermek bütün cümlelerden güçlü.
- **Reklam izi (sekizinci satır).** Reklam kütüphanesinde işletmenin aktif reklamı ekranda durur. "Reklama para veriyorsunuz, gelen aramayı ise kimse açmıyor" cümlesinin arkasında bu ekran olur.
- **Google profili (birinci satır).** Şikayet cümlesinin geçtiği yorum ekranda açılır. Yorumu yazan kişinin adı imleçle ya da elle kapatılır, ekranda kalmaz.
- **Site (ikinci satır).** Site telefon görünümünde açılır, telefon numarasının bulunamadığı yer gösterilir.
- **Instagram (üçüncü satır).** Profil açılır, son gönderinin tarihi ya da biyografide iletişim yolunun olmadığı yer gösterilir.
- **Saatler (dördüncü satır).** Çalışma saatleri kutusu açılır, kapalı olan akşam ya da hafta sonu gösterilir.
- **Duran havuz izi (beşinci satır).** Yorum tarihleri ekranda yukarıdan aşağı kaydırılır; eski yorumlar ile seyrelmiş yeni yorumlar aynı ekranda görünür.

Ekranda görünmeyecekler: denetim kartı, kendi e-postan ve bildirimler, başka adayların sekmeleri, CRM ekranı, kendi sisteminin demosu. Çekimden önce diğer sekmeleri ve bildirimleri kapatırsın; bu tek adım videonun yarısını kurtarıyor.

### Senaryo: altı parça, altmış saniye

FounderOS senaryoyu altı parça yazar, her parçanın yanında kaç saniye olduğu ve o saniyede ekranda ne açık olduğu yazar. Sen okumazsın, söylersin. Kayıt boyunca ekran açık, yüzün köşede küçük bir baloncukta.

**1. parça, sıfırdan sekizinci saniyeye. Ekran: bulgunun durduğu sayfa açık.**
Adıyla başlarsın ve ne yaptığını değil ne gördüğünü söylersin. "Ahmet Bey, merhaba. Şu an ekranda sizin Haritalar sayfanız açık." Klişe övgü yok, "içeriğinizi takip ediyorum" yok.

**2. parça, sekizinci saniyeden yirmi beşinci saniyeye. Ekran: bulgunun tam üstünde, imleç orada. Videonun omurgası burası.**
EN GÜÇLÜ BULGU'yu gösterirsin, okumazsın. Yaşanmış kanca varsa burada geçer: "Dün akşam yedide aradım, açan olmadı." Ekranda ne varsa ağzından çıkan cümle onu anlatır; ikisi tutmuyorsa video yeniden çekilir. Bu parça kısalırsa video çöker, uzarsa aday kapatır.

**3. parça, yirmi beşinci saniyeden otuz beşinci saniyeye. Ekran: aynı, hâlâ bulgunun üstünde.**
LİRA KARŞILIĞI tek cümlede ve tek yerde geçer, ekran açıkken. Hesap görünür olur: kayıp birimi çarpı kartın rakamı. Kartta rakam yoksa bu parça hiç yoktur, video on saniye kısalır ve rakamsız gider. Uydurulmuş rakam ilk soruda çöker. Aynı bulgunun hesabı e-postada zaten söylendiyse burada tekrarlanmaz; video ikinci bulguyu ve varsa onun karşılığını söyler.

**4. parça, otuz beşinci saniyeden kırk beşinci saniyeye. Ekran aynı kalır, sen kamera baloncuğuna dönersin.**
Kime yardım ettiğin ve ne yaptığın, iki cümle. Şehirle birlikte: "[Şehir]de klima servisleriyle çalışıyorum, telefon çaldığında araç altında olanlarla." Sonra Dönüşüm Cümlesi'nin konuşma hali ve sistemin adı. "Yapay zeka", "bot" ve araç adı geçmez.

**5. parça, kırk beşinci saniyeden elli beşinci saniyeye. Ekran aynı.**
İki şey olabilir, ikisi de varsa söylenir: kanıt cümlesi ve neden şimdi görüşmek gerektiği. Toplu kanıt cümlesi varsa "ben saydım" diye söylenir. Neden şimdi sorusunun cevabı gerçek ve fiyatsız olur: "İlk müşterilerimle kanıt topluyorum, bu ay [şehir]de birkaç işletmeyle çalışacağım." Fiyat ve deneme fiyatı görüşmede söylenir, videoda değil. Sonuç yoksa sonuçtan söz edilmez.

**6. parça, elli beşinci saniyeden altmışıncı saniyeye. Ekran kapanmaz, sen kameraya bakarsın.**
Tek somut saat teklifi ve adıyla kapanış. Tek saat, iki seçenek değil: "Yarın on birde on beş dakika konuşalım, uymazsa siz saat söyleyin. Görüşürüz Ahmet Bey." İki tarih vermek videoda karar geciktiriyor; telefonda iki seçenek verilir, videoda bir.

**Süre: hedef altmış saniye, en fazla doksan.** Sebebi üç tane ve üçü de senin lehine. Birincisi, işletmeci videoyu iş arasında açıyor; kendi adını ve kendi ekranını ilk saniyelerde görmezse kapatıyor. İkincisi, uzun video sohbette ve e-postada ağır kalıyor, açılmıyor. Üçüncüsü, sen günde beş tane çekeceksin; üç dakikalık video çeken öğrenci ikinci günü bırakıyor.

**Senaryoda hiç geçmeyecek kalıplar:** "içeriğinizi takip ediyorum", "umarım iyisinizdir", "hızlı bir soru", "sayfanıza baktım", "sizin gibi işletmelere". "Şu kadar müşteri getiririm" gibi sayı sözü yok. Adı ve şirketi olmayan kanıt hikâyesi yok. "Ayda on beş müşteri, olmazsa para iade" gibi teklif artı söz kalıbı yok. Görmediğin hiçbir şey videoya girmez.

### Teklif anlatım kalıbı, videonun ortası

Senaryonun teklif parçası şu kalıpla söylenir; kelimeler senin, sıra sabit:

"Size ulaşmamın sebebi şu: [birinci dert], [ikinci dert] ve [üçüncü dert] yaşayan [niş] işletmeleriyle çalışıyorum. Biz [sonuç bir], [sonuç iki] ve [sonuç üç] yapıyoruz ve hepsini [21/28] günde kuruyoruz. Karışık duruyor ama aslında basit ve çalışıyor. [Kanıt cümlesi, varsa.] Şu an ilk örnek çalışmalarımı çıkarmak için takvimimi buna ayırdım. Yarın on birde yirmi dakika konuşalım, uymazsa siz saat söyleyin. Uygun değilse hiç sorun değil, yoğun olduğunuzu biliyorum."

Üç dert kartın "işletmecinin gerçek dertleri" bölümünden ve denetim kartından; üç sonuç teklifin sonuç basamağından. Fiyat, deneme fiyatı ve kademe videoda söylenmez, görüşmeye kalır. Kanıt cümlesi yalnızca gerçek kanıt varsa söylenir; yoksa o cümle yoktur, "onlarca işletmede yaptık" denmez. Son cümle çıkış kapısıdır ve atlanmaz.

### Kayıt: ekran kaydı, tek çekim, montaj yok

Kayıt bilgisayarın kendi ekran kaydıyla yapılır: ekran açık, sesin kayıtta, yüzün yok. Program indirilmiyor, hesap açılmıyor, ücretsiz. Yüzün olmadığı için ses her şey: mikrofon açık, sessiz oda. Tek çekim, montaj yok.

Mac'te: "Shift", "Command" ve "5" tuşlarına birlikte bas; ekranın altında bir çubuk çıkar. Çubukta ekranı çerçeveleyen ikinci simge "Record Entire Screen" (bütün ekranı kaydet); yanındaki "Options" (seçenekler) listesinde "Microphone" (mikrofon) altında bilgisayarın mikrofonunu seç. "Record" (kaydet) düğmesine bas, konuş; bitince üst çubuktaki kare "Stop" (durdur) düğmesine bas. Video masaüstüne düşer.

Windows'ta: "Windows" tuşu ile "Shift" ve "S" tuşlarına birlikte bas, üstte küçük çubuk çıkar; çubuktaki kamera simgesi "Record" (kaydet) yazar, ona bas, kaydedilecek alanı seç, mikrofon simgesinin açık olduğuna bak, "Start" (başla) de. Bitince "Stop" (durdur). Video "Videos" (Videolar) klasörüne düşer. Bu çubuk yoksa Windows'un eski sürümündedir; "Windows" tuşu ile "G" oyun çubuğunu açar, oradaki "Record" (kaydet) düğmesi aynı işi görür.

Ekran senin gördüğünle uyuşmuyorsa ekranın görüntüsünü al, buraya at, hangi düğme olduğunu söylerim.

Işık yüzüne gelsin, karanlık köşe olmasın; arka plan temiz olsun. Sessiz yer; kulaklığın mikrofonu yeter. Gülümse, sesini canlı tut; robot gibi konuşmak, videoyu yapay zekaya çektirmekle aynı şeye çıkıyor.

**Yasak:** yapay zekaya konuşturmak, ses kopyası, adı ve ekranı kendiliğinden değiştirip yüzlerce video üreten program, yapay yüz. Video sen olacaksın.

Kendi sisteminin demo ekran kaydı bu videoya eklenmez. Aday "nasıl çalışıyor" diye sorsa da demo mesajla gönderilmez; üç adımlı cevap konuşmasıyla randevuya çevrilir. Demo görüşmeye gelme sebebidir.

Sağlık ve güzellik nişlerinde videoda söylenmeyecekler ve ekranda gösterilmeyecekler: fiyat, "en iyi", öncesi-sonrası, hasta adı, hasta yorumu. Yorumdan gösterilen alıntı yalnızca "aradım açmadılar" tipi olur.

### Acemi için: kamera korkusu ve kaç çekim

İlk videon kötü olacak. Herkesinki öyle. Sebebi de sende değil: insan kendi sesini kayıttan duyunca yabancı buluyor, bu herkeste böyle ve üç dört videoda geçiyor.

İki şey bu işi kolaylaştırıyor ve ikisi de bu modülün yeni hali sayesinde var. Birincisi, kameraya bakmıyorsun, ekrana bakıyorsun; anlatacak somut bir şey var, imleci oraya götürüyorsun, gözün gidecek yer belli. İkincisi, senaryo altı parça ve ekranın kenarında açık duruyor; ezberlemiyorsun, sırayı takip ediyorsun.

Çekim sayısı üç, dördüncü yok:
- Birinci çekim ısınmadır, gitmeyecek, bunu baştan bil.
- İkinci çekim genelde gidendir.
- Üçüncü çekim sadece ikincide bir yerde takıldıysan.

"Yeter" kararını FounderOS verir, sen vermezsin. Ölçü beş madde: adı ilk sekiz saniyede geçti mi, bulgu ekranda göründü mü, tek somut saat teklifi var mı, doksan saniyenin altında mı, sesin canlı mı. Beşi de tuttuysa yeter, gönderilir. Bir kez izlenir, ikinci kez izlenmez; ikinci izleme çekimi düzeltmiyor, sadece cesaretini kırıyor.

Takılma sebebi kelimeleri unutmaksa senaryoyu ekranın kenarında açık tutarsın. Kelime kelime okuma; okuyan ses duyuluyor ve robotlaştırıyor.

### Gönderim: iki kanal, aynı gün, senin elinden

**Instagram** (hesabın bir yıldan eski ve yüz takipçiden çoksa): videoyu galeriden sohbete yüklersin, sohbette oynar, link yok. Üstüne tek satır: "Ahmet Bey, size özel kısa bir video çektim, bir dakika." Gönderdikten sonra sohbette oynadığını gör, sonra "gitti" de; oynamıyorsa videoyu altmış saniyeye kısalt.

**E-posta** (adres varsa): video YouTube'a "liste dışı" yüklenir; liste dışı videoyu linki olan herkes izler, hesap gerekmez, aramada çıkmaz.

Kurulum bir kez, beşinci gün:
1. İkinci günün iş e-postasıyla açılmış Google hesabına gir (yoksa o e-postayla aç).
2. O hesapla YouTube'a gir; kanal dördüncü blokta kisisel-markani-kur ile açılmıştı, videolar oraya yüklenir.

Her gün, her video için:
1. YouTube uygulamasını aç, alttaki artı işaretine bas, "video yükle" de.
2. Videoyu galeriden ya da bilgisayardan seç, başlığa "[Ad] Bey için" yaz.
3. Görünürlük sorusu gelince "liste dışı" seç, yükle.
4. Yüklenen videoda "paylaş" deyip linki kopyala.

E-postaya ek değil link konur; kapak görseli yok, düz metin ve link. Sebebi: yeni e-posta adresinde görsel ve süslü içerik istenmeyen posta kutusuna düşürür; adres alışınca da görsel yok, basit kalır. Metin üç beş cümle, sonunda adın ve şehrin. Konu: "Ahmet Bey, size bir video çektim." Gövde: "Salı yazmıştım. Anlatmak yerine göstereyim dedim, ekranınızı açıp bir dakikalık video çektim: [link]. Uymazsa sorun değil. Ahmet Kaya, Bursa." Metni FounderOS hazırlar, linki sen yapıştırırsın, "tamam" dersin, CRM'den gider.

WhatsApp'tan video yok.

### Videodan sonra ne oluyor

Video gittiği anda kanal durumu satırı değişir ve tek bir sıradaki hareket kalır. Bir adayın aynı anda iki hareketi olmaz.

```
Video:     yapıldı · [gittiği tarih] · iki kanaldan gitti, cevap yok · [iki gün sonrası]
SIRADAKİ HAREKET: Instagram sesli mesaj takibi · [iki gün sonrası]
```

Aynı video hem e-postadan hem Instagram'dan gittiyse bu tek harekettir, iki temas değil. Video giden adayın üçüncü, yedinci ve on dördüncü gün takip zinciri kapanır; yerini video zinciri alır.

Sırası şu ve adaya-mesaj-yaz'ın karar tablosuyla aynıdır:
- **İki gün sonra, cevap yok:** Instagram'dan sesli mesaj takibi. "Geçen gün bir video göndermiştim, görmüş müydünüz? Görmediyseniz sorun değil." Adayın Instagram'ı yoksa bu takip e-postadan tek satır gider.
- **Yedi gün sonra, cevap yok:** e-postadan tek ayrılık mesajı, sonra aday "sonra" aşamasına geçer ve altı ay sonra yeniden taranır. Adayın e-postası yoksa ayrılık mesajı Instagram'dan gider.
- **Cevap gelirse:** beş dakika içinde aynı kanaldan üç adımlı cevap konuşması. Diğer kanalların sıradaki hareketi durur. Kayıt yerinde cevabın videodan sonra geldiği işaretlenir.

Şaka ve hareketli görsel takibi yok. İkinci video yok; bir adaya bir video.

### Ölçüm

İzlenme sayacı yok, tek işaret cevap. Yirmi videoda bir bakılır: video sonrası cevap oranı ve hangi bulgu tipiyle çekilen videonun cevap aldığı. Elli videodan önce senaryonun iskeleti değişmez, altı parça yerinde kalır. Yurt dışı oranları sana hedef diye söylenmez.

### Günün akışı, pencerelere göre

**Tam zamanlı, yazı yolu.** Sabah bloğu: günün denetim kartları okunur, video listesi hazır gelir. Saha bloğu: kırk e-posta, otuz Instagram, on arama; bloğun son yarım saati video bloğudur, ilk hafta üç video bir saat, sonra beş video doksan dakika (senaryo, üç çekim, YouTube yükleme, iki kanala gönderim). Akşam bloğu: kanal durumu ekranı, kaç video gitti, kaç cevap geldi.

**İşin yanında.** Sabah bloğu, yani işe gitmeden önceki bir saat ya da öğle arası: beş adayın denetim kartı okunur. Saha bloğunun sonu: iki video, kırk dakika. Akşam bloğu: kanal durumu ekranı, on beş dakika. İlk müşterinin teslim süresinde ve şirket kuruluş gününde bir video, yirmi dakika.

## 6. Ne söyler

Beşinci gün: "Yarın sahaya çıkıyorsun. Bugün kurulum ve bir deneme videosu, kimseye gitmeyecek. Listenin en altındaki adayın kartını açtım, bulgusu Haritalar'daki yorum. Ekranı aç, konuş. Sonra bir kez izle, beş şeye bak: adı ilk sekiz saniyede geçiyor mu, bulgu ekranda görünüyor mu, tek saat teklifi var mı, doksan saniyenin altında mı, sesin canlı mı. Sonra bir daha izleme. İlk videon ortalama olacak, herkesinki öyle."
Saha bloğunun sonunda: "Bugün beş video: Ahmet, Mehmet, Ayşe, Kemal, Selin. Beşinin de kartı hazır. Ahmet Bey'in bulgusu şu: salı formu doldurdun, dönüş gelmedi. Ekranda o formun sayfası duracak. Senaryo altı parça, karşında. Okuma, söyle. Üç çekim, en iyisi gider."
Denetimsiz aday çıkarsa: "Bu adayın denetimi yok, video çekmiyoruz. Yerine listenin altından denetimi hazır olanı aldım. Devam."
Kartta rakam yoksa: "Bu kartta lira karşılığı boş. Üçüncü parçayı çıkardım, video elli saniye. Rakam uydurmuyoruz, ilk soruda çöker."
Video gitmeyince: "Beş videodan üçü gitti. Kalan ikisi yarın ilk iş."
Cevap gelince: "Ahmet Bey videoya cevap yazdı: 'nasıl çalışıyor bu?' Anlatma, gösterme; saat teklif et: 'Yarın on birde on beş dakika, kendi telefonunuzda görürsünüz.' Beş dakikan var."
İki gün geçince: "Ahmet Bey'in videosu iki gün önce gitti, cevap yok. Sıradaki hareket Instagram sesli mesaj, bugün. Yedinci günde ayrılık mesajı gidecek, sonra listeden düşecek."

## 7. Ne yazar

Kayıt yerinde (CRM ya da `adaylar.csv`) adayın kaydına: video kanal durumu satırı "yapıldı", gittiği tarih, hangi kanallardan gittiği, YouTube linki, sonucu ve sıradaki tarih. Tek sıradaki hareket satırı: iki gün sonrası Instagram sesli mesaj, yedi gün sonrası ayrılık. Temas sayacına bir temas. Bu adayın üçüncü, yedinci ve on dördüncü gün takibi kapatılır. Cevap gelirse "video sonrası" işareti.

Denetim kartına dokunulmaz; kart aday-denetimi-cikar'ın çıktısıdır, buradan değiştirilmez.

İş Beyni'ne: video sayısı (bugün, toplam), yirmi videoda video sonrası cevap oranı, hangi bulgu tipiyle çekilen video cevap aldı.

Niş kartına: otuz videodan sonra hangi bulgu tipi cevap aldı, "sahadan dolacak" bölümüne tarihiyle.

Doksan Gün Planı'nın onuncu bölümüne (mesajlar): nişe uyarlanmış altı parçalık video senaryosu kalıbı ve hangi bulgunun hangi ekranda gösterildiği.

## 8. Yedek yol

- Denetimi hazır aday sayısı o günün video sayısını karşılamıyorsa: kaç denetim varsa o kadar video çekilir. Denetimsiz adaya hiçbir koşulda video çekilmez.
- Kartta lira karşılığı boşsa: üçüncü parça çıkar, video kısalır, rakamsız gider.
- Bilgisayarın yoksa ya da ekran kaydı programı hiç kurulamıyorsa: telefonun ön kamerasıyla yüz videosu çekilir, bulgu ekranda gösterilemez, sözle söylenir. Ayakta, telefon sabit, eller serbest; oturup okumak robotlaştırır. Takılıyorsan telefonun uygulama mağazasında (App Store ya da Google Play) telesuflör (metni kameranın yanında kaydırarak gösteren uygulama) diye aratıp birini kurarsın; onu kullanan telefonu sabit koyar, kullanmayan telefonu elinde tutup yürüyerek de çekebilir. Bu ikinci tercihtir, ekran kaydı üçüncü haftada tekrar denenir.
- Instagram hesabın yeni ve adayın e-posta adresi yoksa: video yok, aday telefonla aranır.
- YouTube'a yükleme olmuyorsa: video yalnızca Instagram'dan gider; e-postaya "Instagram'dan bir video gönderdim" diye tek satır.
- Kameraya çıkamıyorsan: aynı altı parçayı Instagram'da sohbet içi ses kaydı olarak gönderirsin, bulguyu ekran görüntüsüyle birlikte atarsın; e-postada yok. Kamera üçüncü haftada tekrar denenir.
- Aday videoyu izlemeden "ne istiyorsunuz" yazarsa: üç adımlı cevap konuşması.
- Sağlık nişinde kartın bulgusu ekranda gösterilemiyorsa (hasta yorumu, öncesi sonrası): video çekilmez, yazılı takip sürer.
- Ekran kaydı programının ekranı tarif ettiğimden farklıysa: ekran görüntüsü at, FounderOS söyler. Adım atlanmaz.
- Günde beş çekilemiyorsa iki; sıfır gün olmaz.

## 9. Sıradaki adım ve işaretler

Sıradaki: cevap gelen aday adaya-mesaj-yaz'ın üç adımlı cevap konuşmasına, randevu alınınca gorusmeye-getir'e. Cevap gelmeyen aday iki gün sonra Instagram takibine, yedi gün sonra ayrılık mesajına, sonra "sonra" aşamasına. Ay sonunda yeni yüz işletme ve yeni denetimler.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Denetimsiz bir adaya video çekilmiş: o temas sayılır ama işaret düşer; ikinci kez olursa video bloğu kartların okunmasıyla başlar.
- Yirmi videoda sıfır cevap: önce kanal kontrol edilir (Instagram kısıtlı mı, e-posta gitti mi), sonra ekranda bulgunun gerçekten göründüğü kontrol edilir; senaryo değişmez.
- Elli videoda video sonrası cevap oranı yazılı mesajın altında: degisiklige-karar-ver'e not.
- Bir adayda aynı anda iki sıradaki hareket görünüyor: o gece düzeltilir.
- Video satırı üç gün "yapıldı"da kalmış, sıradaki tarihi geçmiş: o aday sıranın başına alınır.
- Üç gün üst üste sıfır video: video bloğu saha bloğunun başına alınır.
- Aynı bulgu tipiyle çekilen videolar diğerlerinin iki katı cevap alıyor: o bulgu tipi video sırasında öne çekilir, niş kartına yazılır.
- Kanıt hikâyesi çıktı: beşinci parça kanıt hikâyesi olur.

Beş kural: boş sayfa yok (günün adayları, denetim kartları ve altı parçalık senaryolar hazır gelir) · sessiz bitiş yok (akşam kaç video gitti, kaç cevap geldi, sıradaki hareket ne) · onay (video ve metin senin elinden; tek istisna "tamam" dediğin video e-postası CRM'den gider) · sahadan güncelleme (cevap alan bulgu tipi karta yazılır ve video sırasını değiştirir) · sormaz söyler (adayı karar tablosu, bulguyu denetim kartı, senaryoyu ve "yeter" kararını FounderOS söyler).
