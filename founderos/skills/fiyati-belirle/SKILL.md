---
user-invocable: false
name: fiyati-belirle
description: Birinci gün fiyat bandı, üçüncü gün kesin fiyat. "Fiyat ne diyeyim", "pahalı dedi" dendiğinde itiraz bölümü.
---

# fiyati-belirle

## 1. Adı, rolü, pazarlamadaki karşılığı

Birinci ve üçüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül rakamı koyar.

Neden bu iş var: sıfırdan başlayan biri fiyatı iki yoldan biriyle belirliyor ve ikisi de yanlış. Ya kendi emeğinden hesaplıyor ("bir haftamı alıyor, şu kadar olsun"), ya da korkuyla belirliyor ("çok isterim, alamaz"). İkisi de aynı sonuca çıkıyor: düşük fiyat.

Doğru yol tek: fiyat, müşterinin kazancından geriye hesaplanır. Senin harcadığın saat maliyettir, müşterinin kazandığı para değerdir, ve insanlar değere para veriyor.

Düşük fiyatın bedeli de bilinmeli. Ucuz fiyat ucuz müşteri getiriyor: pazarlık eden, işi kıymetlendirmeyen, daha ucuzunu görünce giden müşteri. Üstelik dört müşteriyle geçineceğin bir işte ucuz fiyat, sekiz on müşteri demek. O kadarını tek başına taşıyamazsın.

Şunlar bu modülün işi değildir:
- Ne sattığını yazmak (teklifi-yaz, dün).
- Nasıl teslim ettiğini çizmek (hizmet-akisini-ciz, bu sabah).
- Görüşmede fiyat itirazını yönetmek (gorusmeyi-yonet). Buradan çıkan cevaplar oraya girdi olur.
- Ödeme yolu ve sözleşme (onay-belgesini-hazirla, üçüncü gün).
- Kâr hesabı ve zam kararı (kari-hesapla, her ay).

Pazarlamadaki karşılığı: fiyat matematik değil, kendini nereye koyduğun.

## 2. Ne zaman çalışır
- Birinci gün: fiyat bandı, nişin kartından alt ve üst rakam, on dakika.
- Üçüncü gün sabah, bir saat: kesin fiyat. Akşam tanıdıklara ilk mesaj gidiyor, fiyat ondan önce tek rakama iner.
- Her yeni müşteri kazandığında kısa bir kontrol için.
- kari-hesapla üç ayda bir bu modülü yeniden çalıştırır.

## 3. Ne okur

İş Beyni'nden: hazırlık seviyen, gelir planın, kanal yolun, nişin, dün çıkan saat tablosu (yalnız kurulum ücreti teslim maliyetini karşılıyor mu kontrolü için; fiyat saatten hesaplanmıyor).
Niş kartından: gerçek fiyatlar ve kapasite, duran havuz, yasal sınırlar.
Sabit fiyat kurallarından: aşağıdaki rakamlar.

Hazırlık seviyesi, satış tecrübenin, sektör bilgin ve güvenin olup olmadığıdır; üçü de yoksa ilk iki müşteride deneme fiyatı uygulanır.

## 4. Ne sorar

Sormaz. Rakamı söyler.

## 5. Ne yapar

### Sabit rakamlar

Bunlar sistemin başlangıç rakamları. Kesinleşene kadar aralık olarak durur.

- Kurulum ücreti: 40.000 TL.
- Deneme fiyatı: 20.000 TL, yani kurulum ücretinin yarısı. Aylık ücret değişmez.
- Aylık ücret, Kademe 1 için 20.000 ile 25.000 TL arası.
- Aylık ücret, Kademe 2 için nişe göre 25.000 ile 45.000 TL arası. Rakam banttan seçilmez, hesaptan çıkar; bant sadece çoğu nişin nereye düştüğünü gösterir. Görüşmede satılan budur.
- Aylık ücret, Kademe 3 için reklam bütçesi hariç 50.000 TL ve üstü.

### Kurulum ücreti neden var

Üç işi birden yapıyor:
1. Nakit getiriyor. İlk ayın masrafını o karşılıyor.
2. Ciddi olmayanı eliyor. 40.000 TL'yi peşin ödeyen kişi fiyat sormaya gelmemiş demektir.
3. Seni erken ayrılıktan koruyor. Kurulum en ağır emeğin harcandığı yer; müşteri ikinci ay ayrılsa bile o emeğin karşılığı ödenmiş oluyor.

Şunu aklında tut: kurulum ücreti teslim maliyetini karşılar, kâr aylık ücrette yaşar.

### Fiyat nasıl hesaplanır: üç adım

**Birinci adım, işletmenin kaybını hesapla.** İki rakam kartın kendisinden çıkar, ikisi de senden çıkmaz. Birincisi kayıp birimi: kartın "gerçek fiyatlar ve kapasite" bölümünün son satırında yazıyor. İkincisi aylık kaçan iş sayısı: kartın "sızıntı nerede" bölümünde birinci sızıntının rakamı. İkisini çarparsın. Kartta hangisi yoksa hesap o kalemsiz yapılır ve eksik olduğu yazılır; rakam uydurulmaz.

Örnek, klima ve kombi servisi. Kartın kayıp birimi 1.000 ile 1.500 lira, ortası 1.250. Kartın sızıntı bölümünde sezonun tepe gününde kaçırılan beş altı çağrı yazıyor; temkinli olan alt uç, yani beş. Ayda yirmi iki iş günü: 5 × 22 = 110 kaçan çağrı. Çarpım: 110 × 1.250 = 137.500 TL. Bu, o işletmenin bir ayda sadece cevaplanmayan çağrıdan kaybettiği para.

**İkinci adım, sayıya girmeyenleri ekle.** Sistem gece de çalışıyor, hastalanmıyor, takibi unutmuyor, gece ikide gelen mesaja cevap veriyor. Kartın ikinci ve üçüncü sızıntısı da burada: klimada randevu sözü verilip gidilmemesi ve geçen sezon bakım yaptıranların hiç aranmaması. Bunların lira karşılığı kartta yok, o yüzden çarpıma girmiyor. Ama fiyatı savunurken söylenir ve rakamın üst ucunu haklı çıkaran şey bunlar.

**Üçüncü adım, payını al.** Kural şu: yarattığın değerin onda biri ile beşte biri arası. 137.500 TL'lik aylık kayıpta senin payın 13.750 ile 27.500 TL arasında. Kademe 2'nin aylık rakamı bu aralığın üst ucundan seçilir ve yuvarlanır: klimada 25.000 TL.

Bu oran neden böyle: müşteri sana verdiği her 1 TL'ye en az 5 TL geri almalı. Altına inerse ilk kötü haftada iptal ediyor. Beş ile on kat arasında memnun oluyor, on katın üstünde referans getiriyor.

**Hesap bandın altına düşerse.** Çıkan rakam Kademe 2 bandının altındaysa fiyat banda çekilmez, hesap doğru kabul edilir. Sırayla üç şey yapılır. Bir: kartın ikinci ve üçüncü sızıntısının lira karşılığı sahadan biliniyorsa çarpıma eklenir ve hesap tekrarlanır. İki: yine altındaysa Kademe 2'nin rakamı hesabın verdiği rakam olur ve gelir planı o rakamla yeniden hesaplanır, yani hedefine daha çok müşteri gerekir. Üç: yeniden hesaplanan müşteri sayısı doksan güne sığmıyorsa, yani gereken arama sayısı senin günlük sayınla doksan günü aşıyorsa, niş düşer ve ikinci günün ikinci sırasındaki nişe geçilir. Bu sıra hiçbir zaman atlanmaz; fiyatı yukarı yuvarlayarak niş kurtarılmaz.

Bu hesabı telefonda tek cümlede söyleyebilirsin: "Ayda kurtardığınızın beşte birinden azını alıyorum."

### Üç kademeye rakam

Üç kademeye de rakam yazılır. Yasal sınırı olan nişlerde Kademe 3'e "yok" yazılır.

Karşılaştırma fiyatı da yazılır: Kademe 2'nin üç aylık paketi. Karşılaştırma fiyatı sitede duran pahalı seçenektir, görüşmede söylenmez. Aday onu görmüş gelir ve tek rakamı duyduğunda kafasında bir kıyas olur.

### Deneme fiyatı

Hazırlık seviyen düşük çıktıysa ilk iki müşteride kurulum yarıya iner, aylık aynı kalır.

İndirim demiyoruz, çünkü karşılığında üç şey alıyorsun:
1. Rakamları paylaşma izni.
2. İsim ve logo izni.
3. Yirmi birinci günde kısa bir video.

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

- Cevap evet ise sorun fiyat değil, inanç. Kanıta dönersin: kart rakamı, güvence, yirmi birinci gün raporu.
- Cevap hayır ise sorun gerçekten fiyat. O zaman Kademe 1 açılır. Bu kapsamı küçültmektir, indirim değil. Aylık rakam düşer çünkü verilen iş azalır.

İndirim menüsü açılmaz. Fiyat düşmez, kapsam daralır.

### Güvence

Güvence, müşteriye verdiğin sözdür: yirmi birinci günde rapor, yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz.

Bu bir sayı sözü değildir ve olmamalıdır. "Ayda otuz randevu" diye söz verirsen kontrol edemediğin bir şeyi taahhüt etmiş olursun. Güvencenin ölçüsü sistemin çalışıp çalışmadığıdır, müşterinin satış yapıp yapmadığı değil.

Güvencenin şartları da yazılır: müşteri giriş izinlerini kurulum görüşmesinde verir, karşılama formunu ve duran havuz onayını yedinci güne kadar verir. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir. Bir parça mevzuat yüzünden ya da müşterinin kendi adımını atmaması yüzünden kurulamıyorsa o parça güvencenin sonucuna sayılmaz.

Güvence konusunda bir rahatlatıcı bilgi: bu tip güvenceleri kullanan müşteri onda birden az çıkıyor. Güvence iade için değil, kararı kolaylaştırmak için var.

### Aday ilk mesajda "fiyat ne" diye sorarsa

Cevap üç parçalı: aralık verilir, sebep söylenir, görüşmeye bağlanır.

"Kurulum ve aylık olarak çalışıyorum, sizin büyüklüğünüzde işletmelerde toplam şu aralıkta çıkıyor. Kesin rakamı kaç kanaldan talep aldığınıza göre veriyorum. Yirmi dakikalık bir görüşmede bakalım, rakamı orada söylerim."

Rakamı yazışmada tek başına vermezsin. Bağlamsız rakam her zaman pahalı görünür.

## 6. Ne söyler

Rakamı verirken: "Fiyatın şu: kurulum 40.000, aylık [rakam]. Sen daha önce satış yapmadın, o yüzden ilk iki müşteride kurulum 20.000, aylık aynı. Karşılığında üç şey alacaksın: rakamları paylaşma izni, isim ve logo izni, yirmi birinci günde kısa bir video."
Matematiği gösterirken: "Rakamı tartışmıyoruz, matematiği gösteriyorum. Bu sektörde kaçan bir müşteri [kart rakamı] ediyor. Sistem ayda [sayı] tanesini geri getirirse [sonuç]. Senin payın onun beşte birinden az."
Prova: "Şimdi rakamı sesli söyle ve sus. Ben saymaya başlayacağım. Otuz saniye konuşmayacaksın."
"Çok yüksek" derse: "Matematiği bir daha bakalım. Deneme fiyatın zaten var. Fiyatı sen değil, ilk otuz görüşme belirleyecek. Şimdilik bu."
Müşteri itiraz edince: "Tek soru sor: sonucun kesin olacağını bilseniz bu rakam mantıklı gelir miydi? Evet derse sorun fiyat değil, inanç; kanıta dön. Hayır derse Kademe 1'e in, indirim yapma."
Ucuz satmak isterse: "Ucuz fiyat ucuz müşteri getiriyor. Ayrıca dört müşteriyle geçineceksin. 15.000 TL'ye satarsan sekiz müşteri lazım, sekizini tek başına taşıyamazsın."

## 7. Ne yazar

İş Beyni'ne: üç kademenin rakamı, karşılaştırma fiyatı, deneme fiyatı işareti, üç karşılık, güvence cümlesi ve şartları, "fiyat ne" cevabı, kartın kaçan müşteri rakamı ve kurtarma tahmini, fiyat sürümü 1 ve tarihi.
CRM'e: kurulum ve aylık ücret satırları kayıtta hazır duruyor, aday "kazandım" aşamasına geçtiğinde doldurulur.

## 8. Yedek yol

- Aylık aralık kesinleşmemişse: modül kart verisinden bir aralık önerir ve "aralık" etiketiyle kaydeder. Rakam ilk müşteride kesinleşir.
- Kartta kayıp birimi ya da sızıntı rakamı yoksa: hesap yapılamaz, Kademe 2 aralığının ortası yazılır ve "kart eksik" işareti düşülür. İlk üç görüşmede işletmecilere kayıp birimi sorulur, gelen cevapla hesap tekrarlanır ve fiyat düzeltilir.
- Sen "çok yüksek" dersen: matematik bir kez daha anlatılır, deneme fiyatı hatırlatılır, indirim açılmaz.
- Fiyat itirazı son on görüşmenin yarısından fazlasında geliyorsa: sorun fiyat değil, teklifi anlatış biçimidir. teklifi-yaz'a işaret gider.
- Kapanış oranın beklenenin çok üstündeyse: fiyatın düşük demektir. kari-hesapla'ya işaret gider.
- Nişin mevzuat kısıtı varsa: Kademe 3 "yok" yazılır, güvence cümlesi o nişin sınırlarına göre yeniden kurulur.

## 9. Sıradaki adım ve işaretler

Sıradaki: "Aynı günün ikinci yarısında paranın yolunu ve tanıdık listeni kuruyoruz, akşam ilk mesajlar gidiyor. Yarın görünür oluyorsun."

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Fiyatı sesli söylerken üç denemede rakam düşüyor: prova sayacına "fiyat provası" yazılır.
- Fiyat itirazı son on görüşmenin yarısından fazlasında çıktı: teklifi-yaz'a işaret gider.
- Kapanış oranı beklenenin üstünde: fiyat düşük, kari-hesapla'ya işaret gider.
- İlk müşteri kazanıldı: aralık etiketi kalkar, rakam kesinleşir.
- Otuz görüşme doldu: fiyat kilidi açılır, kapanış oranı ilk kez okunur, karar degisiklige-karar-ver'de verilir.
- İki müşteri deneme fiyatıyla kapandı: deneme fiyatı kapanır, üçüncüden itibaren tam fiyat.
- Üç ay doldu: kari-hesapla bu modülü yeniden çalıştırır.

Beş kural: boş sayfa yok (rakamlar, hesap ve itiraz cevabı hazır gelir) · sessiz bitiş yok (akşam ilk mesajlar gidiyor) · onay (fiyat tablosu senin "tamam"ınla kaydedilir) · sahadan güncelleme (görüşme analizleri ve aylık kâr hesabı fiyatı yeniler) · sormaz söyler (rakamı söyler, indirim menüsü açmaz).
