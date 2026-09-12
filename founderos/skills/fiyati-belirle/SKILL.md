---
user-invocable: false
name: fiyati-belirle
description: "Birinci gün fiyat bandı, üçüncü gün kesin fiyat. \"Fiyat ne diyeyim\", \"pahalı dedi\" dendiğinde itiraz bölümü."
---

# fiyati-belirle

## 1. Adı, rolü, pazarlamadaki karşılığı

Birinci ve üçüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül rakamı koyar.

Neden bu iş var: sıfırdan başlayan biri fiyatı iki yoldan biriyle belirliyor ve ikisi de yanlış. Ya kendi emeğinden hesaplıyor ("bir haftamı alıyor, şu kadar olsun"), ya da korkuyla belirliyor ("çok isterim, alamaz"). İkisi de aynı sonuca çıkıyor: düşük fiyat.

Doğru yol tek: fiyat, müşterinin kazancından geriye hesaplanır. Senin harcadığın saat maliyettir, müşterinin kazandığı para değerdir, ve insanlar değere para veriyor.

Düşük fiyatın bedeli de bilinmeli. Ucuz fiyat ucuz müşteri getiriyor: pazarlık eden, işi kıymetlendirmeyen, daha ucuzunu görünce giden müşteri. Üstelik dört müşteriyle geçineceğin bir işte ucuz fiyat, sekiz on müşteri demek. O kadarını tek başına taşıyamazsın.

Şunlar bu modülün işi değildir:
- Ne sattığını yazmak (teklifi-yaz, birinci blok; kademeleri bu sabah).
- Nasıl teslim ettiğini çizmek (hizmet-akisini-ciz, bu sabah).
- Görüşmede fiyat itirazını yönetmek (gorusmeyi-yonet). Buradan çıkan cevaplar oraya girdi olur.
- Ödeme yolu ve sözleşme (onay-belgesini-hazirla, üçüncü gün).
- Kâr hesabı ve zam kararı (kari-hesapla, her ay).

Pazarlamadaki karşılığı: fiyat matematik değil, kendini nereye koyduğun.

## 2. Ne zaman çalışır
- Birinci gün: fiyat bandı, nişin kartından alt ve üst rakam, on dakika.
- Üçüncü blok, hizmet akışından hemen sonra, bir saat: kesin fiyat. Akşam tanıdıklara ilk mesaj gidiyor, fiyat ondan önce tek rakama iner. Kesin fiyat konduğu anda süre hükmü de verilir (aşağıda) ve Doksan Gün Planı'nın yedinci bölümü güncellenir.
- Her yeni müşteri kazandığında kısa bir kontrol için.
- kari-hesapla üç ayda bir bu modülü yeniden çalıştırır.

## 3. Ne okur

İş Beyni'nden: hazırlık seviyen, gelir planın, kanal yolun, nişin, bu sabah çıkan saat tablosu (yalnız kurulum ücreti teslim maliyetini karşılıyor mu kontrolü için; fiyat saatten hesaplanmıyor).
Niş kartından: gerçek fiyatlar ve kapasite, duran havuz, yasal sınırlar.
Kilitli formül ve oranlardan: aşağıda.

Hazırlık seviyesi, satış tecrübenin, sektör bilgin ve güvenin olup olmadığıdır; üçü de yoksa ilk iki müşteride deneme fiyatı uygulanır.

## 4. Ne sorar

Sormaz. Rakamı söyler.

## 5. Ne yapar

### Formül ve oranlar (kilitli)

Fiyat iki parçadır ve ikisi de değerden hesaplanır, senin saatinden değil: **kurulum ücreti** ve **aylık ücret**. Formül ve oranlar kilitlidir; rakam işletmenin kendi sayısından çıkar.

- **Kurulum ücreti, para kazandıran sistem için:** yıllık ek gelirin yüzde onu. Yıllık ek gelir, işletmenin ayda kaybettiği paranın (kayıp birimi çarpı aylık kaçan olay) on ikiyle çarpımı. Kısa hali: kurulum, bir aylık kaybın bir buçuk katından az, bir katından fazla; öğrenciye "aşağı yukarı bir aylık kaybınız kadar" diye anlatılır. Bizim sistemin ana işi bu: kaçan talebi yakalamak, takip etmek, eski müşteriyi geri kazanmak. Varsayılan formül budur.
- **Kurulum ücreti, para kurtaran sistem için:** yıllık tasarrufun yüzde yirmisi ile yirmi beşi. Yıllık tasarruf, haftada kurtarılan personel saati çarpı saat maliyeti çarpı elli iki. Bu formül iki durumda kullanılır: kartta kayıp biriminin lira karşılığı yoksa ("sahadan dolacak"), ya da görüşmede işletmecinin kendi rakamı kaçan talep yerine telefon başında harcanan saati gösteriyorsa. İkisi de hesaplanabiliyorsa büyük olan değil, sistemin o işletmede yaptığı asıl iş hangisiyse o kullanılır; iki formül toplanmaz.
- **Aylık ücret:** kurulum ücretinin yüzde yirmisi. Karşılığı: sistemin bakımı, metin ve ayar düzeltmeleri, bozulanın onarılması, haftalık kontrol, ara raporlar ve aylık rapor. Kısa hali: "aylık, kurulumun beşte biri."
- **Deneme fiyatı:** hazırlık seviyesi düşükse ilk iki müşteride kurulum ücretinin yarısı. Aylık ücret değişmez, çünkü aylık kurulumdan hesaplanır ve tam kurulumdan hesaplanmaya devam eder.
- **Karşılaştırma fiyatı:** Kademe 2'nin üç aylık peşin paketi (kurulum artı üç aylık). Ön görüşme sayfasında durur (sitede fiyat yoktur), görüşmede söylenmez.
- **Taban:** kurulum ücreti saat tablosundaki kurulum saatlerinin maliyetini (kurulum saatleri çarpı senin saatinin değeri, yani aylık hedefin bölü ayda çalışacağın saat; bu ölçü sistemin kendi kararıdır) karşılamıyorsa o işletme sana küçük demektir; fiyat yukarı yuvarlanmaz, aday uygunluk puanında düşer ve nişte bu sık oluyorsa nisi-sec'in müşteri değeri elemesine işaret gider.

Neden saat değil değer: birinin daha iyi olduğu bir işi daha hızlı yapıyor diye daha az kazanması saçma. Saatten hesaplayan herkes kendini ucuzlatıyor; değerden hesaplayan rakamın arkasında veri taşıyor ve görüşmede "neden bu kadar" sorusuna rakamla cevap veriyor.

### Kurulum ücreti neden var

Üç işi birden yapıyor:
1. Nakit getiriyor. İlk ayın masrafını o karşılıyor.
2. Ciddi olmayanı eliyor. Kurulum ücretini peşin ödeyen kişi fiyat sormaya gelmemiş demektir.
3. Seni erken ayrılıktan koruyor. Kurulum en ağır emeğin harcandığı yer; müşteri ikinci ay ayrılsa bile o emeğin karşılığı ödenmiş oluyor.

Şunu aklında tut: kurulum ücreti teslim maliyetini karşılar ve değerin ilk dilimidir; aylık ücret kârın yaşadığı yerdir, çünkü tekrar eder.

### Fiyat nasıl hesaplanır: dört adım

**Birinci adım, işletmenin aylık kaybını hesapla.** İki rakam kartın kendisinden çıkar, ikisi de senden çıkmaz. Birincisi kayıp birimi: kartın "gerçek fiyatlar ve kapasite" bölümünün son satırında yazıyor. İkincisi aylık kaçan olay sayısı: kartın "sızıntı nerede" bölümünde birinci sızıntının rakamı. İkisini çarparsın. Kartta hangisi yoksa hesap o kalemsiz yapılır ve eksik olduğu yazılır; rakam uydurulmaz.

Kalıp, rakamlar karttan: kartın kayıp biriminin ortası alınır; kartın sızıntı bölümündeki günlük kaçan olay sayısının temkinli alt ucu, ayda yirmi iki iş günüyle çarpılır; çıkan aylık kaçan olay sayısı kayıp birimiyle çarpılır. Bu, o işletmenin bir ayda sadece o sızıntıdan kaybettiği para. Kartta günlük sayı yoksa çarpım yapılmaz, tasarruf formülüne geçilir; o da yoksa "sahadan dolacak" yazılır.

**İkinci adım, yıla çevir ve kurulumu koy.** Aylık kayıp çarpı on iki, yıllık kayıp. Kurulum ücreti bunun yüzde onu. Tasarruf formülündeysen haftalık saat çarpı saat maliyeti çarpı elli iki, kurulum bunun yüzde yirmisi ile yirmi beşi.

**Üçüncü adım, aylığı koy.** Kurulum ücretinin yüzde yirmisi. Yuvarlanır; bin lira basamağına, aşağı değil yukarı.

**Dördüncü adım, sayıya girmeyenleri söyle, rakama katma.** Sistem gece de çalışıyor, hastalanmıyor, takibi unutmuyor, gece ikide gelen mesaja cevap veriyor. Kartın ikinci ve üçüncü sızıntısı da burada (karttan okunur). Bunların lira karşılığı kartta yoksa çarpıma girmiyor; ama fiyatı savunurken söylenir, rakamın arkasındaki fazlayı bunlar taşır.

**Hesap küçük çıkarsa.** Kurulum ücreti teslim maliyetinin altında kalıyorsa fiyat yukarı yuvarlanmaz, hesap doğru kabul edilir. Sırayla üç şey yapılır. Bir: kartın ikinci ve üçüncü sızıntısının lira karşılığı sahadan biliniyorsa aylık kayba eklenir ve hesap tekrarlanır. İki: yine altındaysa bu niş için hedeflenen işletme büyüklüğü yükseltilir (çok koltuklu, çok şubeli, çok ekipli) ve ideal müşteri sayfası buna göre daraltılır; küçük işletmeler uygunluk puanında C'ye düşer. Üç: nişin çoğu işletmesi bu hesabı taşımıyorsa niş düşer ve birinci günün ikinci sırasındaki nişe geçilir. Bu sıra hiçbir zaman atlanmaz; fiyatı yukarı yuvarlayarak niş kurtarılmaz.

Bu hesabı telefonda iki cümlede söyleyebilirsin: "Ayda kaçırdığınız [aylık kayıp], yılda [yıllık]. Kurulum bunun onda biri, aylık da kurulumun beşte biri."

### Bant, kesin rakam ve görüşmedeki rakam

Üç rakam var ve karıştırılmaz:
- **Bant (birinci gün):** formül kartın alt ve üst rakamlarıyla iki kez çalıştırılır; çıkan iki kurulum ve iki aylık, bandın uçlarıdır. Öğrenciye "aralık" diye anlatılır.
- **Nişin varsayılan rakamı (üçüncü blok, kesin fiyat):** formül kartın orta rakamlarıyla çalıştırılır. Bu rakam İş Beyni'ne yazılır, ön görüşme sayfasındaki karşılaştırma fiyatı bundan hesaplanır, "fiyat ne" cevabında aralık olarak söylenir.
- **Görüşmede söylenen rakam:** soru bölümünde işletmeci kendi rakamlarını verdi (kaç arama, kaçı cevapsız, bir müşteri ne getiriyor). Formül o rakamlarla yeniden çalıştırılır ve söylenen rakam odur. İşletmecinin rakamı nişin varsayılanının yüzde otuz altında ya da üstündeyse kendi rakamı geçerlidir; aradaysa varsayılan söylenir, rakamla oynanmaz. Böylece fiyat hem her işletmeye özel hem tartışılmaz: rakamı işletmeci verdi, formül sabit.

Kilit şudur: otuz görüşme birikmeden değişmeyen şey formül, oranlar ve nişin varsayılanıdır. Görüşmede işletmecinin rakamıyla hesap kurmak fiyatı değiştirmek değildir, formülü uygulamaktır.

### Üç kademeye rakam

Üç kademeye de rakam yazılır ve üçü de aynı formülden çıkar; fark, hesaba giren sızıntılardır. Kademe 1 Temel Kapsam: yalnız birinci sızıntı (kaçan talep). Kademe 2 Tam Kapsam: birinci sızıntı artı eski müşteri geri kazanımının lira karşılığı (kartta varsa); görüşmede satılan budur. Kademe 3 Genişletilmiş Kapsam: Kademe 2 artı dış arama ve reklamın getirdiği ek gelir; en erken ikinci ay, büyüme şartından sonra. Yasal sınırı olan nişlerde Kademe 3'e "yok" yazılır.

Hesap Kademe 2 ile yapılır: bant, nişin varsayılan rakamı ve görüşmedeki rakam Kademe 2'nin rakamıdır. Kartta eski müşteri geri kazanımının lira karşılığı yoksa Kademe 2'nin rakamı Kademe 1'inkiyle aynı çıkar; iki kademe aynı rakamla yazılır, fark kapsamda kalır, rakam uydurulmaz. "Pahalı" itirazında Kademe 1'e inmek kapsamı küçültmektir; iki rakam aynıysa inilecek yer yoktur ve indirim de yapılmaz, kanıta dönülür.

Karşılaştırma fiyatı da yazılır: Kademe 2'nin üç aylık paketi. Ön görüşme sayfasında duran pahalı seçenektir (sitede fiyat yoktur), görüşmede söylenmez. Randevu alan aday onu görmüş gelir ve tek rakamı duyduğunda kafasında bir kıyas olur.

### Değer payı kuralı ve üç bölge

Fiyatın tavanı işletmecinin kazancından çıkar, senin hedefinden değil. Formülün oranları tavandır: ilk yıl işletmeci sana yıllık kaybının yaklaşık üçte birini öder (kurulum yüzde on, on iki aylık yüzde yirmi dört; toplam yüzde otuz dört), ikinci yıldan itibaren dörtte birinden azını (yüzde yirmi dört); yani verdiği her liraya karşılık ilk yıl yaklaşık üç, sonra dört lira geri alır. Bu oran gelir formülü içindir; tasarruf formülünde kurulum yıllık tasarrufun yüzde yirmisi ile yirmi beşi olduğu için oran söylenmez, yalnız kurulum ve aylık söylenir. Üç bölge var. Formülün üstünde: işletmeci sessizce "acaba yanlış mı yaptım" der, kötü bir haftada iptal eder, yorum yazmaz. Formülde: memnundur, kalır, yorum yazar. Formülün çok altında: sen kendini ucuzlatmışsındır, dört müşteriyle geçinemezsin. Değer hesabı işletmecinin brüt kazancıyla değil kârıyla yapılır; kâr payı kartın "gerçek fiyatlar ve kapasite" bölümünden, kartta yoksa görüşmede sorulur.

### Çırak tuzağı

Sıfırdan başlayan herkesin yaptığı hata: kulağa iyi geldiği için formülün üstünde bir kurulum ücreti istemek. Çırak ilk gün büyük işe konur, iş bozulur, müşteri parasını geri ister, çırak daha başlamadan biter. Formülün üstündeki kurulum ücretinde üç şey olur: ilk kurulum hatasında iade istenir ve ilk izlenim gider; rakamı haklı çıkarmak için olmayan kanıt uydurulur; para cebe girince teslimat baskısı kalkar ve sonuç düşer.

Bu yüzden ilk iki müşteride deneme fiyatı var ve güvence sözleşmede yazılı: riskin bir kısmı sende kalıyor, bu seni daha hızlı öğrenmeye zorluyor ve satışta dürüstlük olarak okunuyor. "Sadece işe yararsa ödersiniz" cümlesinin bizdeki hali "rapor gününde sayılar sıfırsa ikinci ay ücretsiz"dir. Kurulum ücreti tamamen sıfırlanmaz; sıfır olan iş ciddiye alınmıyor ve işletmeci takip etmiyor.

Randevu başına ya da gelen müşteri başına ücret modeli bizim işe uymuyor ve sebebini bil: o model reklamla dışarıdan talep üreten ajanslar içindir, talep onların. Bizim sistem işletmenin zaten gelen talebini kurtarıyor; "bu randevu sistemden mi geldi yoksa zaten gelecek miydi" tartışması her ay çıkar. O yüzden bizde kurulum artı sabit aylık ücret artı olaya bağlı güvence var.

### Süre hükmü (yalnız üçüncü blokta, kesin fiyatla)

Kesin rakam konunca gelir planı isini-kur'daki zincirle yeniden hesaplanır (hedef bölü müşteri değeri, beş görüşmede bir müşteri, randevuların yüzde yetmişi görüşme, otuz üç aramada bir randevu, arama bölü günlük arama sayısı eşittir gün). Çıkan gün doksanı geçiyorsa bugün, ilk kez, söylenir ve iki yoldan biri seçilir: hedef doksan güne indirilir ya da doksan gün sonrası için ikinci hedef yazılır. Bu cümle birinci günde kurulmaz; birinci günde yalnız tempo gösterilir. Moral bozmadan söylenir, rakamla: "Bu fiyatla hedefin doksan güne değil yüz yirmi güne sığıyor. Doksan günde dört müşteri, sonrası ikinci hedef." Karar İş Beyni'nin ikinci bölümüne tarihle yazılır.

### Deneme fiyatı

Hazırlık seviyen düşük çıktıysa ilk iki müşteride kurulum yarıya iner, aylık aynı kalır.

İndirim demiyoruz, çünkü karşılığında üç şey alıyorsun:
1. Rakamları paylaşma izni.
2. İsim ve logo izni.
3. Rapor gününde kısa bir video.

Bu üçü sözleşmeye yazılır. Karşılığı olmayan indirim indirimdir ve bir daha geri gelmez.

İndirimin kurulumda yapılması, aylıkta yapılmaması önemli. Aylık ücreti bir kere düşürürsen o müşteride hep düşük kalıyor ve gelir planın bozuluyor. Kurulum bir kerelik, o yüzden orada esneyebilirsin.

Deneme fiyatı ikinci müşteriden sonra biter. İkiden fazla müşteride uygulanmaz, çünkü artık kanıtın var.

### Fiyatı söyleme

Sıra şu:
1. Fiyattan önce tek soru sorulur: "Bu sistem sizin sorununuzu çözer mi, neden?" Cevabı o verirse rakam kolay geçer.
2. Tek rakam söylenir, tek paket. Kurulum ve aylık birlikte söylenir.
3. Susulur. Otuz saniye.
4. Otuz saniye sonra tek cümle: "Nasıl ilerleyelim?"

Susmak en zor kısmı ve en önemlisi. Rakamı söyleyip arkasından açıklama yapmaya başlarsan pahalı olduğunu sen söylemiş oluyorsun.

Bunun provası burada yapılır: rakamı üç kez sesli söylersin ve susarsın. Üç denemede rakam düşüyorsa prova sayacına "fiyat provası" yazılır.

### Fiyat itirazı

Tek bir ayırıcı soru var ve provası yapılır: "Sonucun kesin olacağını bilseniz bu rakam mantıklı gelir miydi?"

- Cevap evet ise sorun fiyat değil, inanç. Kanıta dönersin: kart rakamı, güvence, rapor günü raporu.
- Cevap hayır ise sorun gerçekten fiyat. O zaman Kademe 1 açılır. Bu kapsamı küçültmektir, indirim değil. Aylık rakam düşer çünkü verilen iş azalır.

İndirim menüsü açılmaz. Fiyat düşmez, kapsam daralır.

### Güvence

Güvence, müşteriye verdiğin sözdür: rapor gününde ([21/28]. gün) rapor, yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz. Cümlenin tam metni İş modeli bölümünde, iki sürümüyle (randevu yolu, teklif yolu); İş Beyni'nin dördüncü bölümüne nişin yolculuğuna uyan sürüm yazılır ve her belge oradan okur.

Bu bir sayı sözü değildir ve olmamalıdır. "Ayda otuz randevu" diye söz verirsen kontrol edemediğin bir şeyi taahhüt etmiş olursun. Güvencenin ölçüsü sistemin çalışıp çalışmadığıdır, müşterinin satış yapıp yapmadığı değil.

Güvencenin şartları da yazılır: müşteri giriş izinlerini kurulum görüşmesinde verir, karşılama formunu ve duran havuz onayını yedinci güne kadar verir. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir. Bir parça mevzuat yüzünden ya da müşterinin kendi adımını atmaması yüzünden kurulamıyorsa o parça güvencenin sonucuna sayılmaz.

Güvence konusunda bir rahatlatıcı bilgi: bu tip güvenceleri kullanan müşteri onda birden az çıkıyor. Güvence iade için değil, kararı kolaylaştırmak için var.

### Aday ilk mesajda "fiyat ne" diye sorarsa

Cevap üç parçalı: aralık verilir, sebep söylenir, görüşmeye bağlanır.

"Kurulum ve aylık olarak çalışıyorum, sizin büyüklüğünüzde işletmelerde toplam şu aralıkta çıkıyor. Kesin rakamı kaç kanaldan talep aldığınıza göre veriyorum. Yirmi dakikalık bir görüşmede bakalım, rakamı orada söylerim."

Rakamı yazışmada tek başına vermezsin. Bağlamsız rakam her zaman pahalı görünür.

## 6. Ne söyler

Rakamı verirken (deneme fiyatı yalnız hazırlık seviyesi düşükse, yani satış tecrübesi, sektör bilgisi ve güvenin üçü de yoksa): "Fiyatın şu: kurulum [rakam], aylık [rakam], yani kurulumun beşte biri. Hazırlık seviyen düşük, o yüzden ilk iki müşteride kurulum yarısı, aylık aynı. Karşılığında üç şey alacaksın: rakamları paylaşma izni, isim ve logo izni, rapor gününde kısa bir video."
Matematiği gösterirken: "Rakamı tartışmıyoruz, matematiği gösteriyorum. Bu sektörde kaçan bir müşteri [kart rakamı] ediyor, ayda [sayı] tanesi kaçıyor: ayda [aylık kayıp], yılda [yıllık]. Kurulum yıllığın onda biri: [kurulum]. Aylık kurulumun beşte biri: [aylık]. İlk yıl toplam ödediği, kaybettiğinin yaklaşık üçte biri; ikinci yıldan itibaren dörtte birinden azı."
Prova: "Şimdi rakamı sesli söyle ve sus. Ben saymaya başlayacağım. Otuz saniye konuşmayacaksın."
"Çok yüksek" derse: "Matematiği bir daha bakalım. Deneme fiyatın zaten var. Fiyatı sen değil, ilk otuz görüşme belirleyecek. Şimdilik bu."
Müşteri itiraz edince: "Tek soru sor: sonucun kesin olacağını bilseniz bu rakam mantıklı gelir miydi? Evet derse sorun fiyat değil, inanç; kanıta dön. Hayır derse Kademe 1'e in, indirim yapma."
Ucuz satmak isterse: "Ucuz fiyat ucuz müşteri getiriyor. Ayrıca dört müşteriyle geçineceksin. Formülün yarısına satarsan sekiz müşteri lazım, sekizini tek başına taşıyamazsın."

## 7. Ne yazar

İş Beyni'ne: hangi formülün kullanıldığı (gelir ya da tasarruf) ve hesabın iki girdisi, üç kademenin kurulum ve aylık rakamı, nişin varsayılan rakamı ve bandı, karşılaştırma fiyatı, deneme fiyatı işareti, üç karşılık, güvence cümlesi ve şartları, "fiyat ne" cevabı, kartın kaçan müşteri rakamı ve kurtarma tahmini, fiyat sürümü 1 ve tarihi.
CRM'e (açıldığı gün): kurulum ve aylık ücret satırları kayıtta hazır duruyor, aday "kazandım" aşamasına geçtiğinde doldurulur.

## 8. Yedek yol

- Bant kesinleşmemişse: modül kart verisinden formülle bir aralık önerir ve "aralık" etiketiyle kaydeder. Nişin varsayılanı üçüncü blokta konur, görüşmede işletmecinin rakamıyla hesap yeniden kurulur.
- Kartta kayıp birimi ya da sızıntı rakamı yoksa: gelir formülü yapılamaz, tasarruf formülüne geçilir (kartın personel ve telefon saati bilgisiyle); o da yoksa "kart eksik" işareti düşülür ve rakam ilk üç görüşmede işletmecinin kendi sayısıyla kurulur.
- Sen "çok yüksek" dersen: matematik bir kez daha anlatılır, deneme fiyatı hatırlatılır, indirim açılmaz.
- Fiyat itirazı son on görüşmenin yarısından fazlasında geliyorsa: sorun fiyat değil, teklifi anlatış biçimidir. teklifi-yaz'a işaret gider.
- Kapanış oranın beklenenin çok üstündeyse: fiyatın düşük demektir. kari-hesapla'ya işaret gider.
- Nişin mevzuat kısıtı varsa: Kademe 3 "yok" yazılır, güvence cümlesi o nişin sınırlarına göre yeniden kurulur.

## 9. Sıradaki adım ve işaretler

Sıradaki, birinci günde (bant): "Şimdi hesap, sonra marka. Devam edelim mi?" Üçüncü blokta (kesin fiyat): "Aynı günün ikinci yarısında paranın yolunu, sözleşmeni ve aday listeni kuruyoruz; akşam tanıdıklara ilk mesaj gidiyor. Geçelim mi?"

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Fiyatı sesli söylerken üç denemede rakam düşüyor: prova sayacına "fiyat provası" yazılır.
- Fiyat itirazı son on görüşmenin yarısından fazlasında çıktı: teklifi-yaz'a işaret gider.
- Onuncu görüşme tamamlandı: ideal-musteriyi-cikar yenileme için açılır. Sahada duyulan cümleler masabaşı satırlarının üstüne yazılır ve on sekizinci bölümün saha sürümü çıkar. Bu, teklifin kelimelerinin açıldığı eşikle aynı eşiktir; ikisi aynı oturumda yapılır.
- Kapanış oranı beklenenin üstünde: fiyat düşük, kari-hesapla'ya işaret gider.
- İlk müşteri kazanıldı: aralık etiketi kalkar, rakam kesinleşir.
- Otuz görüşme doldu: fiyat kilidi açılır, kapanış oranı ilk kez okunur, karar degisiklige-karar-ver'de verilir.
- İki müşteri deneme fiyatıyla kapandı: deneme fiyatı kapanır, üçüncüden itibaren tam fiyat.
- Üç ay doldu: kari-hesapla bu modülü yeniden çalıştırır.

Beş kural: boş sayfa yok (rakamlar, hesap ve itiraz cevabı hazır gelir) · sessiz bitiş yok (akşam ilk mesajlar gidiyor) · onay (fiyat tablosu senin "tamam"ınla kaydedilir) · sahadan güncelleme (görüşme analizleri ve aylık kâr hesabı fiyatı yeniler) · sormaz söyler (rakamı söyler, indirim menüsü açmaz).
