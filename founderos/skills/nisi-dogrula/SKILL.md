---
user-invocable: false
name: nisi-dogrula
description: "nisi-sec'in yardımcısı, ikinci gün. Seçilen pazarın canlı verisini sayar: işletme sayısı, reklam veren oranı, sezon, rakip. Karar bozulursa o gün değiştirilir."
---

# nisi-dogrula (arka plan yardımcısı)

## 1. Adı, rolü, pazarlamadaki karşılığı

İkinci bloğun arka plan yardımcısı. Arka plan yardımcısı, FounderOS'un ağır işleri verdiği yardımcıdır; sen onu görmezsin, sonucu FounderOS anlatır.

İşi tek cümleyle: nisi-sec'in seçtiği üç nişin gerçekten satış yapılabilir bir pazar olup olmadığını canlı sayılarla kontrol etmek.

Neden bu iş var: niş kartlarındaki rakamlar yazıldıkları tarihte doğruydu, ama senin şehrinde bugün ne olduğunu söylemiyorlar. Kart Türkiye'de kaç klima servisi olduğunu yazar; senin ilinde 340 mı yoksa 60 mı olduğunu yazmaz. O sayı yanlışsa doksan günün tamamı yanlış kurulur.

Pazarlamadaki karşılığı: bu kontrolün ekranı, FounderOS'un tanıtım sayfasında gerçek ekran görüntüsüyle kanıt olarak gösterilir.

Şunlar bu yardımcının işi değildir:
- Niş seçmek. O nisi-sec'in işi; bu yardımcı sadece sayı üretir.
- Aday listesi çıkarmak. O üçüncü blokta, aday-listesi-cikar modülünde. Aynı tarama kullanılır ama amaç farklıdır: burada sayıyoruz, orada listeliyoruz.

## 2. Ne zaman çalışır

- İkinci blokta, sayım çekimleri hazır olunca FounderOS çağırır; üç niş için birden. Yarım saat sürer.
- Bir daha çalışmaz. Niş değiştirme konuşulursa yeniden çağrılır.

## 3. Ne okur

nisi-sec'ten: üç nişin adı, şehir, tarih.
Niş kartlarından: "reklam kütüphanesi kelimeleri" ve "rekabetin şekli" bölümleri.
İş Beyni'nden: şehir, üç nişin adı, ikinci blokta başlatılan üç sayım çekiminin iş kimlikleri.
Veri servisinden: her sayım çekiminin özeti: kaç kayıt geldi, kaçında telefon var, kaçında Instagram var, kaçında site yok, kaçının profili sahipsiz, kaçı akşam kapalı.

## 4. Ne sorar

Sormaz, sana hiç konuşmaz. Veri servisi kapalıysa ya da sayım çekimi başlatılmadıysa FounderOS'a "sayım yok" der ve elle sayım yoluna geçilir.

## 5. Ne yapar

### Sayım

Her niş için sırayla:

1. Sayımı veri servisi yapar. Üç niş için çekim ikinci bloğun sabahında, araclari-kur'un üçüncü adımında başlatılmıştır: kartın Haritalar kategori adı, senin şehrin, beş yüz kayıta kadar. Sonucu FounderOS alır (servise yalnız FounderOS sorar; yardımcının servise erişimi yok), özeti bu yardımcıya verir; servis hâlâ "çalışıyor" diyorsa FounderOS yirmi saniye bekleyip tekrar sorar, en fazla on kez.
2. Özetten üç sayı okunur: kaç kayıt geldi, kaçında telefon var, kaçının sitesi yok. Sayım çekimi siteden e-posta ve Instagram çıkarmadığı için Instagram bu sayımda ölçülmez. Profili sahipsiz ve akşam kapalı sayıları servis verebiliyorsa okunur, veremiyorsa "ölçülemedi". Sahibinin adı ve son yorumun tarihi de ölçülmez; o hücrelere "ölçülemedi" yazılır ve karar diğer ölçülere kalır.
3. Reklam tarafı: Meta Reklam Kütüphanesi'ne (Facebook ve Instagram'da kimin reklam verdiğini gösteren açık sayfa) hangi yoldan bakılacağı henüz karara bağlanmadı; karar gelene kadar o sütuna "görülemedi" yazılır.
4. Türkiye geneli sayıyı kartın rekabet bölümünden alır; canlı sayılan yalnız şehirdir.

Örnekleme yok: servis beş yüz kayıta kadar listenin tamamını sayıyor, oranlar bütünden çıkıyor.

Reklam sütunu "görülemedi" kaldığında o niş yorum sayısına göre puanlanır. Sayı uydurulmaz.

### Beş soru

Her nişe aynı beş soru sorulur ve cevaplar tabloya yazılır:

1. Bu şehirde en az 500 işletme var mı? Sayım çekimi beş yüze ulaştıysa cevap evet; altında kaldıysa gelen sayı yazılır. Üçüncü blokta 500 kişilik aday listesi çıkacak ve doksan günde ona 1.320 arama yapılacak. Bu sayının altında liste dolmuyor.
2. Türkiye'de en az 2.000 işletme var mı? Şehirde 500 çıkmazsa niş Türkiye geneline açılıyor, o zaman bu sayı devreye giriyor. Ülke çapında büyük bir pazar aranmıyor; dört müşteri için 2.000 yeter. Gerekçe tabloya yazılır.
3. Reklam veren oranı en az yüzde on mu? Reklam veren işletme, pazarlamaya para ayırmayı zaten kabul etmiş işletmedir. Bakılamadıysa "görülemedi" yazılır ve bu soru elemez.
4. Telefonu dolu olanlar en az yüzde yetmiş mi? Ulaşamadığın işletmeye satamazsın. Instagram bu sayımda ölçülmüyor, oran yalnız telefonla kurulur.
5. Bu ay bu nişin sezonu mu, ve para hesabı tutuyor mu? Para hesabı nisi-sec'te yazılı: kurulum ücreti yıllık kaybın onda biri, aylık kurulumun beşte biri; kurulum teslim maliyetini karşılamalı (ikinci blokta kaba ölçü: elli saat çarpı öğrencinin saatinin değeri; saat tablosu üçüncü blokta).

### Altıncı sütun: rakip

Bu sütun eleme yapmaz, bilgi verir. Sorusu şu: bu şehirde bu nişe WhatsApp botu, yapay zeka asistanı ya da kendiliğinden giden mesaj sistemi satan biri var mı.

Nasıl bakılır: Google'da ve Instagram'da "şehir adı, niş adı, whatsapp botu" ve "şehir adı, niş adı, yapay zeka asistan" aranır. On dakika sürer. Böyle biri varsa adı ve ne vaat ettiği yazılır.

Bu bilgi teklifi-yaz ve adaya-mesaj-yaz modüllerine gider. Rakip varsa niş düşmez, sadece açılış cümlesi değişir.

### Sonuç

nisi-sec'e üç satır ve altı sütunluk bir tablo döner. Her hücrede rakam ve o rakamın nereden geldiği yazar. Tablonun altında tek satır: birinci aday şu, sebebi şu.

**Bulunamayan hücreye "ölçülemedi" yazılır ve boş bırakılmaz.** Altı sütunun hepsi her nişte dolmuyor; reklam veren oranı ve rakip sayısı en sık boş kalanlar. Boş bırakılan hücre öğrenciye "bakılmadı mı, sıfır mı" diye okunuyor. nisi-sec kararı anlatırken ölçülemeyen sütunu da söyler: "Reklam veren oranını ölçemedim, o yüzden bu karar diğer dört ölçüye dayanıyor." Eksik ölçü kararı durdurmuyor, ama saklanmıyor.

**Rakamın kaynağı hem tabloda hem sohbette adlandırılır.** "Bursa'da 409 servis" yetmiyor; nereden sayıldığı söyleniyor. Kaynağı söylenmeyen rakam, öğrencinin müşteriye tekrarlayamayacağı rakamdır ve o rakam ilk görüşmede onu zor durumda bırakıyor.

FounderOS bunu sana kendi cümlesiyle anlatır ve tabloyu gösterir.

### Veri konusunda bir not

Bu tarama herkese açık yerlerden işletme bilgisi topluyor: harita kaydı, işletme telefonu, işletme hesabı. Şahıs işletmelerinde bu bilgilerin kişisel veri sayılıp sayılmadığı net değil. Çekimi FounderOS'un veri servisi yapıyor; aynı şehir ve kategori bir kere çekilip bir süre saklanıyor ki ikinci kişi için yeniden çekilmesin. Kişisel cep numarası ve kişisel hesap toplanmıyor. Kesin cevabı avukata soracağız; soru listesine bu da eklendi.

## 6. Ne söyler

Öğrenciye hiç konuşmaz. Bütün çıktısı tablodur.

## 7. Ne yazar

Yardımcı dosya yazmaz; tabloyu FounderOS'a döner ve şunları FounderOS yazar. İş Beyni'ne: doğrulama tablosu ve tarihi, hangi sayıların canlı sayıldığı, hangilerinin karttan geldiği.
Niş kartına (`nis-karti.md`): bu tarihte bu şehirde sayılan işletme sayısı, kartın "sahadan dolacak" bölümüne.
CRM'e: hiçbir şey. Aday listesi üçüncü blokta çıkar.

## 8. Yedek yol

- Veri servisi kapalıysa ya da sayım çekimi başlatılmadıysa: FounderOS öğrenciyle birlikte tarayıcı eklentisinden bir semtte sayar, on beş dakika sürer; "500 var mı" sorusuna "ölçülemedi" yazılır, kalan sorular sayılan kadarıyla cevaplanır, tablonun altına "elle yapıldı" notu düşülür.
- Reklam sayfasına bakılamazsa: "görülemedi" yazılır, o soru elemez. Sayı uydurulmaz.
- Şehir sayımı 500'ün altında çıkarsa: aynı nişin Türkiye geneli sayısı karttan yazılır ve tabloya iki satır birden girer; Türkiye geneli canlı sayılmaz.
- Bir nişin kategori adı Haritalar'da tutmuyorsa: kartın diğer kategori adları denenir. Hiçbiri tutmazsa "sayılamadı" yazılır ve o niş elenmez, karar diğer sorulara kalır.

## 9. Sıradaki adım ve işaretler

İş bitince nisi-sec'e döner.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Üç nişten hiçbiri beş sorudan üçünü geçemiyor: "aday havuzu zayıf" denir ve nisi-sec üç yeni niş çıkarır.
- Üç nişin de şehir sayısı 500'ün altında: coğrafya Türkiye geneline açılır.
- Rakip sütunu dolu: teklifi-yaz ve adaya-mesaj-yaz'a not gider.
- Kartın Türkiye geneli sayısı ile canlı sayım arasında büyük fark var: kart eskimiş demektir, işaretlenir ve güncellenir.

Beş kural: boş sayfa yok (kartın kelimeleri ve beş soru hazır gelir) · sessiz bitiş yok (tablo ve tek satırlık sonuç) · onay (kayıt yapmaz, onay gerekmez) · sahadan güncelleme (canlı sayım kartın sahadan dolacak bölümüne yazılır) · sormaz söyler (öğrenciye hiç konuşmaz, sonucu FounderOS anlatır).
