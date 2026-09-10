---
user-invocable: false
name: aday-listesi-cikar
description: Üçüncü gün ve her ay. Beş yüz kişilik soğuk aday listesi ve en çok istenen yüz işletme.
---

# aday-listesi-cikar

## 1. Adı, rolü, pazarlamadaki karşılığı

Üçüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Yol Haritası'nın beşinci aşamasının üçüncü adımındayız.

Bu modül üç şey çıkarıyor: beş yüz kişilik aday listesi, içinden seçilen en çok istenen yüz işletme ve her sabah kendiliğinden hazırlanan günün saha listesi. Aday, henüz müşterin olmayan ama olabilecek işletmedir.

Neden beş yüz: doksan günde bu listeye 1.320 arama yapacaksın, yani her işletmeyi ortalama iki üç kez arayacaksın. Liste beş yüzün altındaysa üçüncü haftada arayacak kimsen kalmıyor.

Neden bugün: yarın kanıtını hazırlıyorsun ve mesajlarını yazıyorsun, altıncı gün sahaya çıkıyorsun. Yarının deneme aramaları bu listeden yapılıyor.

Şunlar bu modülün işi değildir:
- Sıcak çevre listesi (tanidik-listesi-cikar, dün). O ayrı liste, ayrı mesaj.
- Adayın denetimi (aday-denetimi-cikar). Bu modül denetimi tarif etmez, çağırır.
- Mesajların metni (adaya-mesaj-yaz, yarın) ve video mesaj (video-mesaj-cek, sahaya çıktıktan sonra).
- Takip sisteminin kurulması (musteri-takip-sistemini-kur, ikinci gün). Bugün o sisteme yükleme yapıyorsun.

Pazarlamadaki karşılığı: aday listesi.

## 2. Ne zaman çalışır
- Üçüncü gün, üç saat. Instagram kaynağını da kullanıyorsan yirmi dakika daha. Liste çıkaran programın hesabı dün açıldığı için çekim yirmi dakikada biter. Tam zamanlıysan tek oturuş; işin yanında çalışıyorsan çekim ve temizlik sabah bloğunda, geri kalanı akşam bloğunda.
- Her gün: günün saha listesi sabah bloğunda kendiliğinden hazırlanır. Senin bir işin yok, açtığında sıralanmış duruyor.
- İkinci kez: her ay bir kere. Liste baştan yenilenir, yüz işletme yeniden seçilir, hızlı denetimler tazelenir.
- Üçüncü kez: liste beş yüzün altına düştüğünde ya da pazar değiştiğinde.

## 3. Ne okur

İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı tek dosya): nişin, şehrin, kanal yolun, çalışma düzenin, seçtiğin yol, varsa liste çıkaran programın anahtarı.
Niş kartından (seçtiğin sektörün bütün bilgisinin durduğu dosya): Google Haritalar'daki kategori adları, kanal ve zaman bölümü, kim karar veriyor bölümü, yasal sınırlar.
aday-denetimi-cikar'dan: hızlı denetimin beş satırı ve sızıntı puanı. Denetim orada yürür, bu modül puanı okur ve sıralamada kullanır.
CRM'den: cevap veren adaylar, takip günü bugüne düşenler, denetimi hazır olanlar. Günün saha listesi bunlardan çıkıyor.
İkinci günün sıcak listesinden: A listesindeki işletmeler.

## 4. Ne sorar

Tek bir şey sorar: listeyi hangi yolla çıkaracağın. Sebebi şu, orada senin cebinden para çıkıyor. Bunun dışında hiçbir şey sormaz; hangi kategoriyi arayacağını, kaç kayıt çekeceğini, neyi eleyeceğini ve hangi yüz işletmeyi seçeceğini FounderOS söylüyor.

Bir de silme öncesi durak var: silinecek satırları görüp onaylıyorsun.

## 4c. Tamamlandı demek için

Liste "hazır" demek için kayıt sayısı yetmez:

1. Beş yüz kayıt var ve her birinde telefon ya da e-posta dolu; ikisi de boş olan kayıt listede değil.
2. Örnekleme doğrulaması yapılmış: rastgele on kayıt açılmış, işletme gerçekten var, kategori doğru, numara çalışıyor. Onda üçten fazlası tutmuyorsa liste yeniden çekilir.
3. En çok istenen yüz işletmenin her birinde uygunluk gerekçesi var: neden bu, tek satır.
4. Liste CRM'e ya da CRM yoksa İş Beyni'nin on beşinci bölümüne yüklenmiş ve sayım tutuyor.

Dördü tamam olmadan liste "hazır" sayılmaz ve on dördüncü bölüme yazılmaz.

## 5. Ne yapar

### Hangi yolla liste çıkarılır, bu seçim senin

İki yol var ve ikisi de yürüyor.

**Birinci yol, Apify.** apify.com/compass/crawler-google-places, ekranda adı "Google Maps Scraper". Ücretsiz planı ayda 5 dolar kredi veriyor, kredi kartı istemiyor. Yirmi dakikada sekiz yüz kayıt çıkıyor; her kayıtta işletme adı, adres, telefon, web sitesi, e-posta, sosyal medya hesapları, puan ve yorum sayısı, çalışma saatleri ve kategoriler var.

**İkinci yol, Claude'un tarayıcı eklentisi.** Hesap açmıyorsun, para harcamıyorsun. Üç saatte yaklaşık yüz işletme çıkıyor, e-posta gelmiyor.

Verimli olan birincisi: üç saatlik elle tarama yerine yirmi dakika, üstüne e-posta ve sosyal medya hesabı. Sen günde otuz e-posta ve yirmi Instagram mesajı atacaksın; ikinci yolda o iki sütunu elle dolduruyorsun.

Karar senin. FounderOS başka hiçbir yerde seçenek sunmaz, kararı verir ve sebebini söyler. Burada sormasının tek sebebi şu: bu adımda para harcanıyor ve o kararı senin adına vermiyorum.

**İkinci yolu seçtiysen şöyle yürüyor:**

1. Claude'un tarayıcı eklentisini ve Google Haritalar'ı aç.
2. Arama kelimesi: kartındaki kategori adı artı semt adı ("Nilüfer klima servisi" gibi). Şehri tek seferde aratmıyorsun, Haritalar belli bir sayıdan sonrasını göstermiyor; semt semt gidiyorsun ve taradıklarını bir kenara yazıyorsun.
3. Eklenti her işletme kartından altı şeyi tabloya yazıyor: işletme adı, telefon, web sitesi, semt, yorum sayısı ve puan, varsa Instagram hesabı. E-posta bu yolda gelmiyor; siteyi açıp aramayı sadece yüz işletme için, hızlı denetim sırasında yapıyorsun.
4. Bugün üç saatte yaklaşık yüz işletme çıkarıyorsun, aynı gün CRM'e yüklüyorsun, yüz işletme seçimini bu kayıtlardan yapıyorsun. Kalanı dördüncü ve beşinci günün sabah bloklarına yayıyorsun: sahaya çıkarken elinde üç yüz kayıt oluyor, liste ilk hafta içinde beş yüze tamamlanıyor.

Hangi yolu seçtiğin İş Beyni'ne yazılıyor, ay sonundaki yenileme aynı yoldan yürüyor.

### Adım 1: ham listeyi çek (20 dakika, birinci yol)

1. Liste çıkaran programı aç, üstteki arama kutusuna "Google Maps Scraper" yaz, compass/crawler-google-places olanı seç.
2. Ayarları gir: arama kelimesi kartındaki kategori adı artı şehrin ("Bursa klima servisi"), ülke Türkiye, dil Türkçe. Sonuç sayısını 800 yap; beş yüz istiyorsun ama eleyeceksin.
3. Fiyat: 1.000 kayıt için 1,5 dolardan başlıyor, yani sekiz yüz kayıt 1,2 dolar tutuyor. Ücretsiz kredin ayda 5 dolar; bu çekim kredinin dörtte birini bile bitirmiyor. Fiyat "başlıyor" diyor, bazı ayarlarda üstüne çıkabiliyor, çıksa da beş doların yanında küçük kalıyor.
4. Ayda kaç kez: bu krediyle çekimi ayda dört kez yapabilirsin, sen ayda bir yeniliyorsun. Üç çekimlik payın artıyor; ikinci kategori, komşu ilçeler ve aşağıdaki Instagram kaynağı o paydan çıkıyor.
5. Yorum çekme seçeneğini işaretleme. Bu araç yorum metinlerini de verebiliyor ama yorum çekmek maliyeti artırıyor. Ne kadar artıracağını yazmıyorum: fiyat çekilen yorum sayısına göre işliyor, her işletmenin yorumu farklı ve bilmediğim rakamı sana söylemem. Kredin ayda 5 dolar ve yorumlu çekim onu hızla bitiriyor. Yorumlara zaten hızlı denetimde gözünle bakıyorsun.
6. Sağ altta "Start" (başlat) yazan düğmeye bas. Birkaç dakika sürer.
7. Bittiğinde Excel olarak indir. CSV seçersen Türkçe harfler bozuk geliyor.

Şehrinde 800 çıkmıyorsa sıra şu: kartındaki diğer kategori adları, komşu ilçeler, Türkiye geneli. Türkiye geneline açılırsa mesajlardan "sizin şehirde" cümlesi çıkıyor.

### Adım 2: Instagram kaynağı (20 dakika, gerekiyorsa)

İki halde çalışıyor. Birincisi: nişinin ana kanalı yazı, yani kartın kanal ve zaman bölümü o sektörün Instagram'dan yürüdüğünü söylüyor. İkincisi: Haritalar'da elemeden sonra beş yüz kayıt çıkmıyor.

Araç: apify.com/apify/instagram-scraper, ekranda adı "Instagram Scraper". Ücretsiz planda 1.000 sonuç 2,70 dolar. Haritalar çekimin 1,2 dolardı, ikisi birlikte 3,90 dolar, aylık 5 dolarlık kredinin içinde kalıyor.

Girdi olarak üç şey veriyorsun: nişin etiketleri (kartındaki sektör kelimelerinin etiket hali, bir de şehir eklenmişi), şehir artı niş arama kelimesi (Haritalar'da kullandığının aynısı) ve yer araması (şehrinin ya da semtinin Instagram'daki yer sayfası, oradan paylaşım yapan işletmeler çıkıyor).

Profil sonucunda verdiği alanlar: kullanıcı adı, ad, takipçi sayısı, takip sayısı, biyografi, biyografideki bağlantı, işletme hesabı mı, işletme kategorisi, gönderi sayısı, son gönderiler. İşletme hesabı olmayan kişisel profiller eleniyor.

**Şuraya dikkat et, atlarsan liste bozuluyor:** bu araç profil sonuçlarında telefon ve e-posta vermiyor. Üç sonucu var.

Bir: Instagram'dan çıkan aday listesi yazı yolu listesidir, telefon listesine girmiyor. Bu kayıtları arayacak numaran yok.

İki: iki liste işletme adı üzerinden birleşiyor, numara üzerinden değil, çünkü Instagram kaydında numara yok. Aynı işletme iki listede de çıkmışsa tek kayıt oluyor: Haritalar kaydı gövde, Instagram hesabı üstüne yazılıyor.

Üç: biyografideki bağlantı siteye gidiyorsa site sütunu ondan doluyor ve o siteden e-posta bulunabiliyor; bulunursa kayıt e-posta listesine de giriyor.

### Adım 3: temizlik (40 dakika)

Ham listede sana yaramayacak kayıtlar var. Altı eleme yapıyorsun.

Instagram kaynağını kullandıysan temizliğin başına tek iş ekleniyor: iki listeyi işletme adı üzerinden birleştirmek. Birleştirmeden eleme yapılmıyor, yoksa aynı işletmeyi iki kere sayıyorsun.

Her elemede aynı hareketi yapıyorsun: ilgili sütuna göre sıralıyorsun, silinecekler üst üste geliyor, bakıyorsun, topluca siliyorsun.

**Bir: numara tekrarı.** Telefon sütununa göre sırala. Aynı numara iki kere görünüyorsa biri kalıyor; aramayı genişlettiysen aynı işletme iki kere çıkıyor.

**İki: telefonu olmayan.** Telefon sütununa göre sırala, boşlar bir arada toplanıyor, sil. Tek istisnası Instagram kaynağından gelen kayıtlar: onların telefon sütunu zaten boş, yazı yolu listesinde duruyorlar ve silinmiyorlar.

**Üç: zincir ve şube.** İşletme adı sütununa göre sırala, aynı ad art arda geliyor. Beş şubesi çıkan markadan tek satır bırakıyorsun, o da genel merkez varsa. Ulusal zincirler tamamen çıkıyor: şubede karar veren kimse yok, şubedeki kişi seni dinliyor ama satın alamıyor.

**Dört: kategoriye uymayan.** Kategori sütununa göre sırala. Haritalar kategori karıştırıyor; klima servisi ararken beyaz eşya bayisi de geliyor. Kartına bakıp uymayanları siliyorsun.

**Beş: nişin yasal sınırına takılan.** Kartın yasal sınırlar bölümü hangi işletme tipinin listeye girmeyeceğini söylüyor.

**Altı: dün sıcak listeye giren işletmeler.** A listen beş on kişi, ona bakıp bu listede varsa çıkarıyorsun. Tanıdığına dün mesaj attın, iki gün sonra soğuk arama metniyle dönmüyorsun. Bu elemeyi elle yapıyorsun, CRM'in numara birleştirmesine güvenme: tanıdığının kaydında cep numarası var, buradakinde işletmenin sabit hattı, ikisi tutmuyor.

Bir şeyi yapmıyorsun: numaraları sabit hat ve cep diye ayırıp birini silmiyorsun. Sen arıyorsun ve işletmenin ilan ettiği sabit hat tam da aradığın numara.

Elemeden sonra beş yüzün altına düştüysen Adım 1'e dönüp aramayı genişletiyorsun.

### Adım 4: işletme adını kısalt (15 dakika)

Ham listede adlar "Yılmaz Isı Sistemleri San. Tic. Ltd. Şti." gibi geliyor; aramada ve mesajda bu ad kullanılırsa toplu gönderim gibi duruyor.

Tabloya bir sütun daha açıyorsun ve kısa işletme adını yazıyorsun: "Yılmaz Isı". Şu ekler kırpılıyor: Ltd. Şti., A.Ş., San., Tic., Ltd., Limited, Anonim Şirketi.

Yükleme sırasında CRM'e giden sütun bu oluyor, uzun olan değil. İki listeyi birleştirirken de bu sütun kullanılıyor, çünkü Instagram'daki ad zaten kısa halidir.

### Adım 5: en çok istenen yüz işletmeyi seç (15 dakika)

Kalan listenin içinden yüz tanesini işaretliyorsun: müşterin olmasını en çok istediğin işletmeler. Sıradaki adımda sadece onlar denetimden geçiyor.

Üç seçim ölçütü var ve sırası şu:
1. **Büyük olanlar.** Yorum sayısına göre büyükten küçüğe sırala. Yorumu çok olan işletme çok iş yapıyor, çok iş yapan çok da kaçırıyor.
2. **Ulaşılabilir olanlar.** Web sitesi ve Instagram hesabı dolu gelenler.
3. **Nişin içinde kalanlar.** Kategori tam uyanlar.

Üçünü birden taşıyan ilk yüz satırı işaretliyorsun. Emin olamadığını da işaretle, ay sonunda değiştireceksin. İşin yanında çalışıyorsan yüz değil kırk işletme seçiyorsun; onlara ayrı emek vereceksin ve günün kırk temasa yetiyor.

### Adım 6: yüz işletmenin hızlı denetimi (60 dakika)

Bu adımı bu modül tarif etmiyor. Yüz işletmenin hızlı denetimi bu adımda yapılır, nasıl yapıldığı aday-denetimi-cikar'da yazılı, çıktısı sızıntı puanıdır. İşletme başına iki dakika. Puan yüz işletmeyi sıraya diziyor ve sahaya çıktığında kimi önce arayacağını o sıra söylüyor.

Eskiden bu adımda her işletme için tek cümlelik gözlem satırı yazılıyordu; artık yazılmıyor. Yerini denetimin en güçlü bulgusu aldı. Fark şu: gözlem satırı "gördüğüm bir şey", en güçlü bulgu "kaçırdığın müşteri".

Sahibinin adını bulma işi de denetime taşındı, denetimin dokuzuncu satırı o, burada tekrar anlatılmıyor. Sonucu aynı: adı bulunan aday telefon sırasına, bulunamayan yazı sırasına giriyor.

Altmış dakikada otuz işletme bitiyor, kalan yetmişi dördüncü günün sabah bloğunda tamamlıyorsun. Bugün otuz yeterli, çünkü yarının deneme aramaları o otuz işletmeden yapılıyor. İşin yanında çalışıyorsan kırk işletme seçtin: bugün yirmisi, yarın yirmisi.

Puan ve en güçlü bulgu tabloya iki sütun olarak yazılıyor, sıradaki adımda CRM'e gidiyor.

### Adım 7: CRM'e yükle (15 dakika)

İkinci günün test yüklemesinin aynısı, bu sefer gerçek listeyle.

1. Tabloyu Excel olarak kaydet.
2. CRM'de yükleme ekranını aç, dosyayı seç, yüklemeye ad ver: kayıt sayısı ve tarih. "512 aday, 6 Eylül" gibi.
3. Eşleme ekranında sütunları işaretle: kısa işletme adı, sahibinin adı, telefon, e-posta, Instagram hesabı, web sitesi, adres, semt, yorum sayısı, kaynak, sızıntı puanı, en güçlü bulgu. Eşleşmeyeni alma. Form ve reklam işaretleri için ayrı sütun açmıyorsun, onlar denetimden geliyor.
4. Kaynak sütunu iki değer alıyor: Haritalar ya da Instagram. Hangi adayın telefonla, hangisinin yazıyla gideceğini o belirliyor ve "nereden bulundu" satırı da o sütundan doluyor.
5. Kayıtta ad alanı boş kabul edilmiyor. Sahibinin adı bulunmayan kayıtlarda o alana işletme adı yazılıyor.
6. Yükle, sonra yüklenen sayıyı dosyadakiyle karşılaştır. Numara tekrarı temizlendiği ve iki liste birleştirildiği için ikisi tutuyor olmalı; büyük fark varsa eşleme yanlış, geri al ve tekrarla.
7. Hepsinin aşaması "yeni" ve üstlerinde "soğuk" işareti var; aşama, adayın işin neresinde olduğunu gösteren etiket. En çok istenen yüz işletmeye ayrı işaret koy. Denetimi bugün yapılmayanlarda sızıntı puanı boş kalıyor, dördüncü günde doluyor.

### Listenin günlük yenilenmesi

Liste ayda bir tamamen yenileniyor ama her gün yeniden sıralanıyor. İkisi ayrı iş ve ikisi de kendiliğinden yürüyor.

**Ayda bir:** modül baştan çalışıyor. Yeni çekim, yeni temizlik, yüz işletme yeniden seçiliyor, hızlı denetimler tazeleniyor. Sen sadece silme onayını veriyorsun.

**Her gün:** sabah bloğunda "gün" yazıyorsun ve o günün saha listesi hazır geliyor. Sen sıralamıyorsun, kimi arayacağına karar vermiyorsun; sıralamayı FounderOS kuruyor, CRM'de hazır böyle bir ekran yok. Sıra sabit, dört basamak:

1. **Cevap verenler.** Mesajına dönmüş, telefonu açmış, "sonra ara" demiş herkes. En başta duruyorlar, çünkü cevap veren adayın ilgisi bir günde soğuyor.
2. **Takip günü gelenler.** Üçüncü, yedinci ve on dördüncü gün zincirinde bugüne düşenler.
3. **Denetimi hazır, sızıntı puanı yüksek adaylar.** Puanı yüksek olan önce; eşitlik yorum sayısıyla bozuluyor.
4. **Denetimsizler.** Sıranın sonu; bunlar aranmadan önce derin denetimden geçiyor, denetimsiz aday aranmıyor.

**Kaç kayıt:** çalışma düzenine göre günlük temas sayın kadar. Tam zamanlıysan yüz kayıt, işin yanında kırk. Fazlası hazırlanmıyor; ekranda gördüğün sayı o gün bitirilecek sayı.

**Liste beş yüzün altına düşerse:** uyarı o sabah düşüyor, ay sonu beklenmiyor. O hafta içinde bir sabah bloğu liste büyütmeye ayrılıyor, sıra şu: kartın diğer kategori adları, komşu ilçeler, Instagram kaynağı, Türkiye geneli. Türkiye geneline açılırsa mesajlardan "sizin şehirde" cümlesi çıkıyor. Liste üç yüzün altına inerse bu artık liste sorunu değil, niş kararı haftanın kararına gidiyor.

### Listeyle ilgili tek kural

İkinci günde konuşmuştuk, bugün liste elinde olduğu için tekrar ediyorum.

Vergi kaydı olan işletmelere ulaşırken önceden izin almana gerek yok, kanun bunu telefonla arama için de böyle sayıyor. Rahat ol, yaptığın iş normal bir iş.

Sadece şu düzeni koruyorsun: işletmenin Haritalar'da ilan ettiği numara, genel e-postası ve işletme olarak açtığı Instagram hesabı. Başka yerden bulduğun kişisel cep numarası ve kişisel hesap listeye girmiyor. İlk temasta nereden bulduğunu söylüyorsun. İstemeyen kişi aynı gün listeden çıkıyor ve bir daha aranmıyor.

Bu düzeni koruduğun sürece rahatsın.

## 6. Ne söyler

Açılışta: "Bugün üç saat. Çıktı: beş yüz kişilik liste ve içinden seçilen yüz kişi. Yarın kanıtını hazırlıyoruz, deneme aramaları bu listeden yapılacak."
Araç seçiminde: "İki yol var. Apify yirmi dakikada sekiz yüz kayıt veriyor, e-posta ve Instagram hesabı da geliyor, tutarı 1,2 dolar, kredin ayda 5 dolar. Tarayıcı eklentisi üç saatte yüz işletme veriyor, para gitmiyor ama e-posta da gelmiyor. Sana soruyorum çünkü para senin cebinden çıkıyor. Hangisi?"
Daha az kayıt çekmek isterse: "800 çekiyoruz çünkü eleyeceğiz. Doksan günde bu listeye 1.320 arama gidecek; beş yüzün altında kalırsan üçüncü haftada arayacak kimsen kalmıyor."
Yorum çekmek isterse: "İşaretleme. Bu araç yorum metnini de veriyor ama yorum çekmek maliyeti artırıyor ve ne kadar artıracağını kesin söyleyemem; fiyat çekilen yorum sayısına göre işliyor ve her işletmenin yorumu farklı. Bilmediğim rakamı söylemem. Kredin ayda 5 dolar ve yorumlu çekim onu hızla bitiriyor. Yorumlara hızlı denetimde gözünle bakıyorsun."
Instagram'dan telefon isterse: "O araç profil sonucunda telefon da e-posta da vermiyor. O adayı telefon sırasına koyarsan boş satır arıyorsun; yazıyla gidiyor. Aynı işletme Haritalar'da da varsa iki kaydı adından birleştiriyoruz."
Günlük liste hakkında: "Listeyi sen sıralamıyorsun. Sabah açtığında bugünün kayıtları sırada: önce cevap verenler, sonra takibi gelenler, sonra puanı yüksek olan denetimi hazır adaylar."
Bitince: "Liste CRM'de, yüz işletme işaretli, otuzunun denetimi bitti. Yarın kanıtını hazırlıyoruz ve mesajlarını yazıyoruz."

## 7. Ne yazar

CRM'e: bütün kayıtlar, aşamaları "yeni", "soğuk" işaretiyle, kaynağı ve nereden bulunduğu yazılı. En çok istenen yüz işletme ayrı işaretle. Denetimi bitenlerde sızıntı puanı ve en güçlü bulgu dolu; denetim kartının kendisini aday-denetimi-cikar yazıyor.
İş Beyni'ne: listenin çıkarıldığı tarih, seçilen yol (Apify mi tarayıcı eklentisi mi), ham kayıt sayısı, elenen ve kalan sayı, Instagram kaynağı kullanıldı mı, kaç kayıt adından birleştirildi, yüz işletmenin seçim tarihi, hızlı denetimi biten sayı, kullanılan kategori adı ve kapsanan semtler, harcanan kredi.
Bir sonraki modüllere: yüz işletme ve seçim sırası aday-denetimi-cikar'a, sızıntı puanı ve en güçlü bulgu adaya-mesaj-yaz ile video-mesaj-cek'e, denetimi bitmiş otuz işletme kanitini-hazirla'nın yarınki deneme aramalarına, kategori adı ve seçilen yol bir sonraki ay tekrarı için kendine.

## 8. Yedek yol

- Apify hesabı açılmazsa, çekim hata verirse ya da kredi bitmişse: tarayıcı eklentisi yoluna geçiliyor. Bu artık yedek değil, ikinci yol; günün içinde geçiliyor ve bugünün çıktısı yüz işletme oluyor.
- Tarayıcı eklentisi de çalışmazsa: elle yazma, en son çare. Bir tabloya altı sütun açıyorsun (işletme adı, telefon, web sitesi, semt, yorum sayısı, Instagram) ve Haritalar'da çıkan her işletmeyi yazıyorsun. Yavaş yol, o yüzden önce diğer ikisi deneniyor.
- Şehrinde 500 çıkmazsa: kartın diğer kategori adları, sonra komşu ilçeler, sonra Instagram kaynağı, sonra Türkiye geneli. Dördü de yetmezse niş kararı haftanın kararına gidiyor.
- Instagram aracı sonuç vermezse ya da kredi yetmezse: liste Haritalar'la yürüyor, yazı yolunun Instagram tarafı sahada elle doluyor.
- Hızlı denetim bugün otuza ulaşmazsa: yarının deneme aramaları kaç işletme denetlendiyse o kadarıyla yapılıyor. Kalan denetim dördüncü güne kayıyor, saha ertelenmiyor.
- Yükleme kabul etmezse: liste tabloda kalıyor, temaslar oradan yürüyor, yükleme ilk boş saatte tekrarlanıyor.
- Üç saat aşılırsa: hızlı denetim yarım kalabilir, otuz işletme yeter. Liste, temizlik ve yükleme bugün bitiyor.

## 9. Sıradaki adım ve işaretler

Sıradaki: dördüncü gün, kanıtını hazırlıyorsun ve mesajlarını yazıyorsun.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Üçüncü gün bitti, liste yüklenmedi: dördüncü günün ilk işi olur ve o günün akışı bir saat kayar.
- Yüz işletme seçilmedi: yarının deneme araması yapılamıyor, dördüncü günün ilk yarım saatinde seçilir.
- Hızlı denetimi biten sayı otuzun altında: yarının deneme aramaları eksik yapılır, denetim dördüncü günün sabah bloğuna eklenir.
- Aynı işletme hem sıcak hem soğuk listede görünüyor: altıncı eleme atlanmış, soğuk mesaj durdurulur.
- Bir ay geçti, liste yenilenmedi: modül ikinci kez açılır.

Beş kural: boş sayfa yok (kategori adı, ayarlar, altı eleme ve seçim ölçütleri hazır gelir) · sessiz bitiş yok (akşam liste CRM'de, yüz işletme işaretli ve otuzunun puanı yazılı) · onay (silinecek satırları görüp onaylıyorsun) · sahadan güncelleme (her ay liste ve yüz işletme yenilenir, her gün saha listesi yeniden sıralanır) · sormaz söyler (kategoriyi, sayıyı, elemeleri ve seçim ölçütlerini FounderOS söyler; tek istisna hangi araçla çalışacağın, çünkü orada cebinden para çıkıyor).
