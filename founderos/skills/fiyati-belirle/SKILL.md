---
user-invocable: false
name: fiyati-belirle
description: "Birinci gün fiyat bandı, üçüncü gün kesin fiyat. \"Fiyat ne diyeyim\", \"pahalı dedi\" dendiğinde itiraz bölümü. \"Fiyatımı hesapla\" dendiğinde de; hesap panelin Teklif stüdyosunda."
---

# fiyati-belirle

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "fiyati-belirle"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Birinci ve üçüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül rakamı koyar.

Neden bu iş var: sıfırdan başlayan biri fiyatı iki yoldan biriyle belirliyor ve ikisi de yanlış. Ya kendi emeğinden hesaplıyor ("bir haftamı alıyor, şu kadar olsun"), ya da korkuyla belirliyor ("çok isterim, alamaz"). İkisi de aynı sonuca çıkıyor: düşük fiyat.

Doğru yol tek: fiyat, müşterinin kazancına bakılarak konur; kazandırdığın birkaç müşteri onun ödediği parayı çıkarmalı. Senin harcadığın saat maliyettir, müşterinin kazandığı para değerdir, ve insanlar değere para veriyor.

Düşük fiyatın bedeli de bilinmeli. Ucuz fiyat ucuz müşteri getiriyor: pazarlık eden, işi kıymetlendirmeyen, daha ucuzunu görünce giden müşteri. Üstelik dört müşteriyle geçineceğin bir işte ucuz fiyat, sekiz on müşteri demek. O kadarını tek başına taşıyamazsın.

Şunlar bu modülün işi değildir:
- Ne sattığını yazmak (teklifi-yaz, birinci blok; kademeleri bu sabah).
- Nasıl teslim ettiğini çizmek (hizmet-akisini-ciz, bu sabah).
- Görüşmede fiyat itirazını yönetmek (gorusmeyi-yonet). Buradan çıkan cevaplar oraya girdi olur.
- Ödeme yolu ve sözleşme (onay-belgesini-hazirla, üçüncü gün).
- Kâr hesabı ve zam kararı (kari-hesapla, her ay).

Pazarlamadaki karşılığı: fiyat matematik değil, kendini nereye koyduğun.

## 2. Ne zaman çalışır
- Birinci gün: fiyat bandı ve nişin kartıyla fayda kontrolü, on dakika.
- Öğrenci rakamı kendisi verirse ("fiyatı kırk bin lira kurulum, aylık on iki bin beş yüz lira olarak koy"): teklif yazılıysa o turda, birinci gün de olsa. Rakam bandın içindeyse fiyat olarak yazılır; 40.000 ve 12.500 Kademe 2'nin rakamıdır, kesin fiyat günü beklenmez, o gün yalnız kademeler ve süre hükmü tamamlanır. Bandın dışındaysa farkı tek cümleyle söylersin, karar onun. İstediği hesap rakamla gösterilir: "Beş klinik: 5 × 40.000 = 200.000 TL kurulum, bir kerelik. 5 × 12.500 = 62.500 TL aylık hizmet. Beş kurulum ve birer aylık hizmet: 262.500 TL. Bunlar giderler öncesi ciro." Kâr ya da müşteri sayısı sözü verilmez. Mesaj istenen hesapla sınırlıdır; fayda kontrolü sorulmadıysa sohbete tek cümle gider ("Ayda bir hasta kurtarması aylığı çıkarıyor."), ayrıntısı Teklif stüdyosundadır. İş Beyni'ne fiyat yazılır; panele `fiyat` ve `teklif.hesap` gider, Teklif stüdyosu ve Kâr hesabı açılır. Birinci gün sürüyorsa iş bitince kurulumun atlanan adımına dönülür (ideal müşteri, konumlandırma, teslimat kontrolü, vizyonun hesabı); marka ve sayfaya atlanmaz.
- Üçüncü blok, hizmet akışından hemen sonra, bir saat: kesin fiyat. Akşam tanıdıklara ilk mesaj gidiyor, fiyat ondan önce tek rakama iner. Kesin fiyat konduğu anda süre hükmü de verilir (aşağıda) ve Doksan Gün Planı'nın yedinci bölümü güncellenir.
- Her yeni müşteri kazandığında kısa bir kontrol için.
- kari-hesapla üç ayda bir bu modülü yeniden çalıştırır.

## 3. Ne okur

İş Beyni'nden: hazırlık seviyen, gelir planın, günlük temas dağılımın, nişin, aylık hedefin (dört müşteri kontrolü için; fiyat saatten hesaplanmıyor).
Niş kartından: kayıp birimi satırındaki müşteri değeri, kaçan talep satırı, gerçek fiyatlar ve kapasite, duran havuz, yasal sınırlar.
Kilitli bant, kademe rakamları ve fayda kontrolünden: aşağıda.

Hazırlık seviyesi üç ölçüte bakar: satış tecrüben, sektör bilgin ve tanımadığın birini telefonla arama rahatlığın. Düşük demek: satış tecrüben yok ve telefon seni zorluyor, ya da üçünün ikisi yok. Düşükse ilk iki müşteride deneme fiyatı uygulanır.

## 4. Ne sorar

Sormaz. Rakamı söyler.

## 5. Ne yapar

### Bant, kademeler ve fayda kontrolü (kilitli)

Fiyat iki parçadır: **kurulum ücreti** ve **aylık ücret**. İkisi de senin saatinden değil, kurduğun kapsamdan ve işletmeye sağladığı faydadan belirlenir. Rakamlar her nişte aynı banttadır ve kilitlidir; işletmenin kendi sayısı fiyatı değiştirmez, fayda kontrolünü ve kayıp cümlesini kurar.

- **Bant:** kurulum 40.000 ile 60.000 TL, aylık 10.000 ile 15.000 TL. Satış videosundaki örnek paket bu bandın içindedir: kurulum 40.000, aylık 12.500.
- **Kademe 1 Temel Kapsam:** kurulum 40.000, aylık 10.000.
- **Kademe 2 Tam Kapsam, görüşmede satılan:** kurulum 40.000, aylık 12.500.
- **Kademe 3 Genişletilmiş Kapsam:** kurulum 60.000, aylık 15.000; en erken ikinci ay, büyüme şartından sonra.
- **Fayda kontrolü:** aylık ücret işletmenin aylık kaybının dörtte birini geçmez. Aylık kayıp = ayda kaçan talep × bunların yüzde kaçı müşteri olurdu × bir müşterinin değeri (ilk iş ve yıl içindeki tekrar). Sistem o işletmede yalnız personel saati kurtarıyorsa aynı kontrol tasarrufla yapılır: aylık ücret, aylık tasarrufun (haftada kurtarılan personel saati × saat maliyeti × 52 ÷ 12) yarısını geçmez. İkisi toplanmaz; sistemin o işletmede yaptığı asıl iş hangisiyse o kullanılır, varsayılan kayıptır.
- **Kaç müşteri ücreti çıkarır:** aylık ücret bölü müşteri değeri, yukarı yuvarlanır; kurulum için de aynı hesap. Görüşmede ve teklifte bu cümle kurulur: "Ayda [sayı] müşteri kurtarması aylığı çıkarıyor."
- **Ödeme:** kurulumun yarısı başlangıçta, sözleşmeyle; kalan yarısı teslimde, rapor gününde ([21/28]. gün). Aylık ücretin ilk tahsilatı [31/38]. gün.
- **Deneme fiyatı:** hazırlık seviyesi düşükse ilk iki müşteride kurulum ücretinin yarısı. Aylık ücret değişmez.
- **Karşılaştırma fiyatı:** Kademe 2'nin üç aylık peşin paketi (kurulum artı üç aylık). Ön görüşme sayfasında durur (sitede fiyat yoktur), görüşmede söylenmez.
- **Küçük işletme:** fayda kontrolü Kademe 2'de tutmuyorsa Kademe 1'e bakılır; Kademe 1'de de tutmuyorsa o işletme sana küçük demektir. Fiyat düşürülmez, aday uygunluk puanında düşer ve nişte bu sık oluyorsa nisi-sec'in müşteri değeri elemesine işaret gider.
- **İlk müşteri tavanı:** ilk iki müşteride kurulum en fazla 60.000 TL, aylık en fazla 15.000 TL; bant zaten bu tavanın içinde. Hazırlık seviyesi düşükse deneme fiyatı bunun üstüne işler.

Neden saat değil değer: birinin daha iyi olduğu bir işi daha hızlı yapıyor diye daha az kazanması saçma. Saatten hesaplayan herkes kendini ucuzlatıyor; değerden hesaplayan rakamın arkasında veri taşıyor ve görüşmede "neden bu kadar" sorusuna rakamla cevap veriyor.

### Kurulum ücreti neden var

Üç işi birden yapıyor:
1. Nakit getiriyor. İlk ayın masrafını o karşılıyor.
2. Ciddi olmayanı eliyor. Kurulumun ilk yarısını peşin ödeyen kişi fiyat sormaya gelmemiş demektir.
3. Seni erken ayrılıktan koruyor. Kurulum en ağır emeğin harcandığı yer; müşteri ikinci ay ayrılsa bile o emeğin karşılığı ödenmiş oluyor.

Şunu aklında tut: kurulum ücreti değerin ilk dilimidir ve bir kere alınır; aylık ücret kârın yaşadığı yerdir, çünkü tekrar eder.

### Fiyat nasıl kurulur: dört adım

**Birinci adım, işletmenin aylık kaybını hesapla.** Üç rakam kartın kendisinden çıkar, hiçbiri senden çıkmaz: kartın "Kaçan talep" satırı (ayda kaç talebe dönülemiyor ve bunların yüzde kaçı müşteri olurdu) ve kayıp birimi satırındaki müşteri değeri (bir müşterinin ilk işi ve yıl içindeki tekrarı; aralığın ortası). Çarparsın: ayda kaçan talep × müşteri olma oranı = ayda kaçan müşteri; × müşteri değeri = aylık kayıp. Kartta hangisi yoksa hesap o kalemsiz yapılmaz, eksik olduğu yazılır; rakam uydurulmaz.

**Kaçan şey bir çağrı değil, bir müşteridir.** Kayıp çağrı ya da seans başına iş tutarıyla sayılmaz: yıl içinde birkaç iş bırakan bir müşteri tek bir iş gibi görünür ve kayıp olduğundan kat kat küçük çıkar. Eskiden böyle sayıyorduk ve rakam işletmecinin gerçeğine uymuyordu. Sayı aylıktır, günlük değil, ve yirmi iki iş günüyle çarpılmaz.

**Hesap büyük çıkarsa tavan var.** Müşteri değeri yıl içindeki tekrarı da taşıdığı için büyük sayılarla çarpınca işletmenin bütün cirosunu aşan rakamlar çıkabiliyor ve görüşmede söylenen her rakam ters tepiyor. Kural: **aylık kayıp, kartın kapasite bölümünden çıkan aylık cironun yüzde otuzunu geçemez.** Geçiyorsa hesap o tavana oturur ve karta "tavana oturdu" notu düşülür. Sebebi basit: hiçbir işletme cirosunun yarısını kaçan telefondan kaybetmiyor, kaybetse kapanırdı.

**İkinci adım, fiyatı koy.** Kademe 2'nin rakamı: kurulum 40.000, aylık 12.500. Bant ve kademeler yukarıda; kilitli.

**Üçüncü adım, fayda kontrolünü yap.** Aylık ücret aylık kaybın dörtte birini geçmiyor mu? Kaç kurtarılan müşteri aylığı çıkarıyor (aylık ücret bölü müşteri değeri, yukarı yuvarlanır), kaçı kurulumu? Tutmuyorsa Kademe 1'e bakılır; o da tutmuyorsa işletme küçüktür (aşağıda, hesap küçük çıkarsa).

**Dördüncü adım, sayıya girmeyenleri söyle, rakama katma.** Sistem gece de çalışıyor, hastalanmıyor, takibi unutmuyor, gece ikide gelen mesaja cevap veriyor. Kartın ikinci ve üçüncü sızıntısı da burada (karttan okunur). Bunların lira karşılığı kartta yoksa çarpıma girmiyor; ama fiyatı savunurken söylenir, rakamın arkasındaki fazlayı bunlar taşır.

**Hesap küçük çıkarsa.** Nişin varsayılan rakamlarıyla (kartın kaçan talebi, oranı ve müşteri değeri) fayda kontrolü Kademe 1'de de tutmuyorsa fiyat aşağı çekilmez, hesap doğru kabul edilir. Sırayla üç şey yapılır. Bir: kartın ikinci ve üçüncü sızıntısının lira karşılığı sahadan biliniyorsa aylık kayba eklenir ve kontrol tekrarlanır. İki: yine tutmuyorsa bu niş için hedeflenen işletme büyüklüğü yükseltilir (çok koltuklu, çok şubeli, çok ekipli) ve ideal müşteri sayfası buna göre daraltılır; küçük işletmeler uygunluk puanında C'ye düşer. Üç: nişin çoğu işletmesi bu kontrolü taşımıyorsa niş düşer ve birinci günün ikinci sırasındaki nişe geçilir. Bu sıra hiçbir zaman atlanmaz; fiyatı aşağı çekerek niş kurtarılmaz.

Bu hesabı telefonda iki cümlede söyleyebilirsin: "Ayda [sayı] müşteri kaçıyor, tanesi [müşteri değeri]; ayda [aylık kayıp]. Kurulum 40.000, aylık 12.500; ayda [sayı] müşteri kurtarması aylığı çıkarıyor."

### Bant, kesin rakam ve görüşmedeki rakam

Üç rakam var ve karıştırılmaz:
- **Bant (birinci gün):** kurulum 40.000 ile 60.000 TL arası, aylık 10.000 ile 15.000 TL. Her nişte aynıdır; nişin kartı bandı değiştirmez, fayda kontrolünü sınar. Öğrenciye "aralık" diye anlatılır. Bant İş Beyni'ne onay beklemeden yazılır; birinci günün onay noktası teklifin gövdesidir, bant değil.
- **Nişin varsayılan rakamı (üçüncü blok, kesin fiyat):** Kademe 2'nin rakamı, kurulum 40.000 ve aylık 12.500; yanında kartın rakamlarıyla nişin varsayılan aylık kaybı ve fayda kontrolü. Bu rakam İş Beyni'ne yazılır, ön görüşme sayfasındaki karşılaştırma fiyatı bundan hesaplanır, "fiyat ne" cevabında aralık olarak söylenir.
- **Görüşmede söylenen rakam:** fiyat yine Kademe 2'nin rakamıdır. Soru bölümünde işletmeci kendi rakamlarını verir (ayda kaç talep, kaçına dönemiyor, dönebildiklerinin kaçı müşteri oluyor, bir müşteri yıl içinde ne bırakıyor); kayıp o rakamlarla yeniden kurulur ve fayda kontrolü o rakamlarla yapılır. İşletmecinin rakamı nişin varsayılanının yüzde otuz altında ya da üstündeyse kendi rakamı geçerlidir; aradaysa varsayılan söylenir, rakamla oynanmaz. Kontrol işletmecinin rakamıyla tutmuyorsa Kademe 1 söylenir (kapsam küçülür, indirim değil); Kademe 1'de de tutmuyorsa fiyat söylenmez, görüşme dürüstçe kapanır: "Şu an bu sistem size pahalı gelir; talebiniz büyüyünce konuşalım."

Kilit şudur: otuz görüşme birikmeden değişmeyen şey bant, kademe rakamları ve fayda kontrolünün oranıdır. Görüşmede işletmecinin rakamıyla kayıp kurmak fiyatı değiştirmek değildir, kontrolü uygulamaktır.

### Üç kademeye rakam

Üç kademeye de rakam yazılır: Kademe 1 Temel Kapsam kurulum 40.000 ve aylık 10.000; Kademe 2 Tam Kapsam kurulum 40.000 ve aylık 12.500, görüşmede satılan budur; Kademe 3 Genişletilmiş Kapsam kurulum 60.000 ve aylık 15.000, reklamın ve ek hizmetlerin getirdiği ek işle, en erken ikinci ay, büyüme şartından sonra. Yasal sınırı olan nişlerde Kademe 3'e "yok" yazılır.

Kademe 1 ile 2 arasındaki fark aylıktadır: eski müşteriyi geri kazanma, yorum ve referans ve aylık rapor ayda 2.500 TL ediyor; kurulum aynıdır. "Pahalı" itirazında Kademe 1'e inmek kapsamı küçültmektir, indirim değil; Kademe 1'den aşağı inilmez, kanıta dönülür.

Karşılaştırma fiyatı da yazılır: Kademe 2'nin üç aylık paketi. Ön görüşme sayfasında duran pahalı seçenektir (sitede fiyat yoktur), görüşmede söylenmez. Randevu alan aday onu görmüş gelir ve tek rakamı duyduğunda kafasında bir kıyas olur.

### Değer payı kuralı ve üç bölge

Fiyatın tavanı işletmecinin kazancından çıkar, senin hedefinden değil. Fayda kontrolü tavandır: aylık ücret aylık kaybın dörtte birini geçmez; böylece işletmeci ilk yıl sana (kurulum artı on iki aylık) yıllık kaybının en fazla üçte birini öder, verdiği her liraya karşılık en az üç lira geri alır. Bu oran kayıp hesabı içindir; tasarruf hesabında aylık ücret aylık tasarrufun yarısını geçmez ve oran söylenmez, yalnız kurulum ve aylık söylenir. Üç bölge var. Kontrolün dışında: işletmeci sessizce "acaba yanlış mı yaptım" der, kötü bir haftada iptal eder, yorum yazmaz. Kontrolün içinde: memnundur, kalır, yorum yazar. Bandın altında: sen kendini ucuzlatmışsındır, dört müşteriyle geçinemezsin. Müşteri değeri işletmenin cirosudur, elinde kalan değil: kayıp işletmecinin cirosuyla söylenir, çünkü işletmeci kaybı cirosuyla sayıyor; "elinize şu kalır" denmez.

### Çırak tuzağı

Sıfırdan başlayan herkesin yaptığı hata: kulağa iyi geldiği için bandın üstünde bir kurulum ücreti istemek. Çırak ilk gün büyük işe konur, iş bozulur, müşteri parasını geri ister, çırak daha başlamadan biter. Bandın üstündeki kurulum ücretinde üç şey olur: ilk kurulum hatasında iade istenir ve ilk izlenim gider; rakamı haklı çıkarmak için olmayan kanıt uydurulur; para cebe girince teslimat baskısı kalkar ve sonuç düşer.

Bu yüzden ilk iki müşteride deneme fiyatı var ve güvence sözleşmede yazılı. Riskin ne kadarının sende kaldığını olduğu gibi söylüyorum, çünkü bunu abartmak satışta bir kere işe yarıyor ve rapor gününde patlıyor: risk altındaki tutar bir aylık ücret (Kademe 2'de 12.500 TL), artı kurulamayan her parça için o ayın yüzde yirmisi. Kurulum ücreti tamamen sıfırlanmaz; sıfır olan iş ciddiye alınmıyor ve işletmeci takip etmiyor. "Sadece işe yararsa ödersiniz" cümlesinin bizdeki hali "sistemin yazdığı randevu sıfırsa ikinci ay ücretsiz"dir. Bunu müşteriye "riskin çoğu bende" diye anlatmazsın, olduğu gibi anlatırsın; sözleşmeyi okuyan işletmeci farkı zaten görüyor.

Randevu başına ya da gelen müşteri başına ücret modeli bizim işe uymuyor ve sebebini bil: o model reklamla dışarıdan talep üreten ajanslar içindir, talep onların. Bizim sistem işletmenin zaten gelen talebini kurtarıyor; "bu randevu sistemden mi geldi yoksa zaten gelecek miydi" tartışması her ay çıkar. O yüzden bizde kurulum artı sabit aylık ücret artı olaya bağlı güvence var.

### Süre hükmü (yalnız üçüncü blokta, kesin fiyatla)

Kesin rakam konunca gelir planı isini-kur'daki zincirle yeniden hesaplanır (hedef bölü aylık ücret, beş görüşmede bir müşteri, randevuların yüzde yetmişi görüşme, otuz üç aramada bir randevu, arama bölü günlük arama sayısı eşittir gün). Gider satırı da yeni aylık ücretle yeniden hesaplanır ve durum kaydındaki `gecim_musteri` güncellenir (yukarı yuvarlanmış tam sayı, 1 ile 60 arası). Çıkan gün doksanı geçiyorsa bugün, ilk kez, söylenir ve iki yoldan biri seçilir: hedef doksan güne indirilir ya da doksan gün sonrası için ikinci hedef yazılır. Bu cümle birinci günde kurulmaz; birinci günde yalnız tempo gösterilir. Moral bozmadan söylenir, rakamla: "Bu fiyatla hedefin doksan güne değil yüz yirmi güne sığıyor. Doksan günde dört müşteri, sonrası ikinci hedef." Karar İş Beyni'nin ikinci bölümüne tarihle yazılır.

### Deneme fiyatı

Hazırlık seviyen düşük çıktıysa ilk iki müşteride kurulum yarıya iner (40.000 yerine 20.000; o da yarısı başlangıçta, yarısı teslimde), aylık aynı kalır.

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

Güvence, müşteriye verdiğin sözdür: rapor gününde ([21/28]. gün) rapor, sistemin yazdığı randevu sıfırsa ikinci ay ücreti alınmaz. Cümlenin tam metni İş modeli bölümünde, iki sürümüyle (randevu yolu, teklif yolu); İş Beyni'nin dördüncü bölümüne nişin yolculuğuna uyan sürüm yazılır ve her belge oradan okur.

Bu bir sayı sözü değildir ve olmamalıdır. "Ayda otuz randevu" diye söz verirsen kontrol edemediğin bir şeyi taahhüt etmiş olursun. Güvencenin ölçüsü sistemin çalışıp çalışmadığıdır, müşterinin satış yapıp yapmadığı değil.

Güvencenin şartları da yazılır: müşteri giriş izinlerini kurulum görüşmesinde verir, karşılama formunu ve duran havuz onayını yedinci güne kadar verir. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir. Bir parça dışarıdan bir engel (izin, hat, sağlayıcı, sektör kuralı) ya da müşterinin kendi adımını atmaması yüzünden kurulamıyorsa o parça güvencenin sonucuna sayılmaz.

Güvence nerede söylenir, nerede söylenmez. Sözleşmede yazılıdır ve onay belgesinde durur; görüşmede "garanti veriyor musunuz" sorusuna cevap olarak söylenir. Teklifin başlığında, sitenin açılışında, telefon açılışında ve ilk mesajlarda geçmez. Sebebi şu: iade sözü kimseyi ikna etmiyor, hatta "demek ki çalışmama ihtimali var" diye okunuyor. İkna eden şey kanıt: deneme aramalarının rakamı ve adayın kendi telefonundan arayabileceği çalışan demo. Güvence kararı kolaylaştırmak için var, kararı kurmak için değil.

### Aday ilk mesajda "fiyat ne" diye sorarsa

Cevap üç parçalı: aralık verilir, sebep söylenir, görüşmeye bağlanır.

"Kurulum ve aylık olarak çalışıyorum: kurulum 40.000 ile 60.000, aylık 10.000 ile 15.000 arası. Hangisinin size uyduğunu kaç kanaldan talep aldığınız ve sistemin ne kadarını kurduğumuz belirliyor. Yirmi dakikalık bir görüşmede bakalım, rakamı orada söylerim."

Rakamı yazışmada tek başına vermezsin. Bağlamsız rakam her zaman pahalı görünür.

## 6. Ne söyler

Rakamı verirken (deneme fiyatı yalnız hazırlık seviyesi düşükse, yani satış tecrüben yok ve telefon seni zorluyorsa ya da üç ölçütün ikisi yoksa): "Fiyatın şu: kurulum [rakam], aylık [rakam]; kurulumun yarısı başlangıçta, yarısı teslimde. Hazırlık seviyen düşük, o yüzden ilk iki müşteride kurulum yarısı, aylık aynı. Karşılığında üç şey alacaksın: rakamları paylaşma izni, isim ve logo izni, rapor gününde kısa bir video."
Matematiği gösterirken: "Rakamı tartışmıyoruz, matematiği gösteriyorum. Bu sektörde bir müşteri yıl içinde [müşteri değeri] bırakıyor; kartın tahminiyle ayda [kaçan talep] talebe dönülemiyor, [kaçan müşteri] tanesi müşteri olurdu: ayda [aylık kayıp]. Aylık ücret [aylık], kaybın dörtte birinin altında; ayda [sayı] müşteri kurtarması aylığı çıkarıyor, kurulumu [sayı] müşteri karşılıyor."
Prova: "Şimdi rakamı sesli söyle ve sus. Ben saymaya başlayacağım. Otuz saniye konuşmayacaksın."
"Çok yüksek" derse: "Matematiği bir daha bakalım. Deneme fiyatın zaten var. Fiyatı sen değil, ilk otuz görüşme belirleyecek. Şimdilik bu."
Müşteri itiraz edince: "Tek soru sor: sonucun kesin olacağını bilseniz bu rakam mantıklı gelir miydi? Evet derse sorun fiyat değil, inanç; kanıta dön. Hayır derse Kademe 1'e in, indirim yapma."
Bant ya da kesin fiyat panele gidince, panel linki yazılıysa tek cümle: "Panelde Teklif stüdyosu açıldı; kayıp hesabın ve fiyatın burada, işletmecinin kendi sayıları ilk görüşmelerde dolacak." (İlk görüşmelerin ortancası yazılıysa cümlenin son parçası söylenmez.)
Ucuz satmak isterse: "Ucuz fiyat ucuz müşteri getiriyor. Ayrıca dört müşteriyle geçineceksin. Yarı fiyata satarsan sekiz müşteri lazım, sekizini tek başına taşıyamazsın."

## 7. Ne yazar

İş Beyni'ne: fayda kontrolünün hangi hesapla yapıldığı (kayıp ya da tasarruf) ve girdileri (ayda kaçan talep, müşteri olma oranı, müşteri değeri), üç kademenin kurulum ve aylık rakamı, ödeme düzeni (kurulumun yarısı başlangıçta, yarısı teslimde), nişin varsayılan rakamı ve bandı, karşılaştırma fiyatı, deneme fiyatı işareti, üç karşılık, güvence cümlesi ve şartları, "fiyat ne" cevabı, kartın kaçan müşteri rakamı ve kurtarma tahmini, fiyat sürümü 1 ve tarihi.
CRM'e (açıldığı gün): kurulum ve aylık ücret satırları kayıtta hazır duruyor, aday "kazandım" aşamasına geçtiğinde doldurulur.

Panel dosyasına (`.founderos/panel/ajans.json`, şeması `founderos:panel-vitrini`'de): `fiyat` (bant; kesinleşince kurulum ve aylık), `teklif.kademeler`'in `kurulum` ve `aylik` rakamları, fiyat itirazı ve cevabı `teklif.itirazlar`'a ve `teklif.hesap` (Teklif stüdyosunun sayıları, İş Beyni'ndeki gerçek kayıttan: `musteri_degeri` kartın müşteri değerinin ortası, en az üç görüşmeden sonra işletmecilerin verdiği sayıların ortancası; `kacan_aylik` ve `musteri_orani` kartın kaçan talep satırından, en az üç görüşmeden sonra altı veri sorusunun ortancasından; `sabit_maliyet` masraf tablosunun aylık toplamı; `arac_maliyeti` müşteri bölümünün bedeli belli olunca; `not` sayıların nereden geldiği; bilinmeyen alan yazılmaz); sonra aracın `panel --yukle` komutu sessiz çalışır.
Panele odak (`odak_yaz`; panelde Teklif stüdyosu açılır): başta `basladi` (birinci gün adım 1/2 "Fiyat bandı", üçüncü blokta adım 2/2 "Kesin fiyat"), prova ya da onay beklerken `bekliyor`, panel yazılınca `bitti` (not: fiyatın ve hesabın Teklif stüdyosunda; birinci günde "kesin rakam aday listesinin çıktığı gün" eklenebilir, blok numarası yazılmaz; sonraki: "Devam").

## 8. Yedek yol

- Kesin fiyat konmadıysa: bant (kurulum 40.000 ile 60.000, aylık 10.000 ile 15.000) "aralık" etiketiyle kaydedilir. Nişin varsayılanı üçüncü blokta konur, görüşmede kayıp işletmecinin rakamıyla yeniden kurulur.
- Kartta müşteri değeri ya da kaçan talep satırı yoksa: kayıp hesabı yapılamaz, fayda kontrolü tasarrufla yapılır (kartın personel ve telefon saati bilgisiyle); o da yoksa "kart eksik" işareti düşülür, fiyat bantla kalır ve kontrol ilk üç görüşmede işletmecinin kendi sayısıyla yapılır.
- Sen "çok yüksek" dersen: matematik bir kez daha anlatılır, deneme fiyatı hatırlatılır, indirim açılmaz.
- Fiyat itirazı son on görüşmenin yarısından fazlasında geliyorsa: sorun fiyat değil, teklifi anlatış biçimidir. teklifi-yaz'a işaret gider.
- Kapanış oranın beklenenin çok üstündeyse: fiyatın düşük demektir. kari-hesapla'ya işaret gider.
- Nişin kartında yasal sınır varsa: Kademe 3 "yok" yazılır, güvence cümlesi o nişin sınırlarına göre yeniden kurulur; öğrenciye sebep anlatılmaz.

## 9. Sıradaki adım ve işaretler

Sıradaki, birinci günde (bant): "Şimdi hesap; marka ve sayfa sıradaki oturuşta." ve hesaba geçilir; doksan günlük plan arka planda yazılmaya başlar. Üçüncü blokta (kesin fiyat): "Aynı günün ikinci yarısında paranın yolunu ve aday listeni kuruyoruz; akşam tanıdıklara ilk mesaj gidiyor." ve aynı mesajda sıradaki işe geçilir; "geçelim mi?" diye sorulmaz.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Fiyatı sesli söylerken üç denemede rakam düşüyor: prova sayacına "fiyat provası" yazılır.
- Fiyat itirazı son on görüşmenin yarısından fazlasında çıktı: teklifi-yaz'a işaret gider.
- Onuncu görüşme tamamlandı: ideal-musteriyi-cikar yenileme için açılır. Sahada duyulan cümleler masabaşı satırlarının üstüne yazılır ve on sekizinci bölümün saha sürümü çıkar. Bu, teklifin kelimelerinin açıldığı eşikle aynı eşiktir; ikisi aynı oturumda yapılır.
- Kapanış oranı beklenenin üstünde: fiyat düşük, kari-hesapla'ya işaret gider.
- İlk müşteri kazanıldı: aralık etiketi kalkar, rakam kesinleşir.
- Otuz görüşme doldu: fiyat kilidi açılır, kapanış oranı ilk kez okunur, karar degisiklige-karar-ver'de verilir.
- İki müşteri deneme fiyatıyla kapandı: deneme fiyatı kapanır, üçüncüden itibaren tam fiyat.
- Üç ay doldu: kari-hesapla bu modülü yeniden çalıştırır.

Beş kural: boş sayfa yok (rakamlar, hesap ve itiraz cevabı hazır gelir) · sessiz bitiş yok (akşam ilk mesajlar gidiyor) · onay (bant ve fiyat İş Beyni'ne onay beklemeden yazılır; CRM'e ücret satırları senin "tamam"ınla girer) · sahadan güncelleme (görüşme analizleri ve aylık kâr hesabı fiyatı yeniler) · sormaz söyler (rakamı söyler, indirim menüsü açmaz).
