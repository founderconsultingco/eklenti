---
user-invocable: false
name: nisi-dogrula
description: nisi-sec'in yardımcısı, ikinci gün. Seçilen pazarın canlı verisini sayar: işletme sayısı, reklam veren oranı, sezon, rakip. Karar bozulursa o gün değiştirilir.
---

# nisi-dogrula (arka plan yardımcısı)

## 1. Adı, rolü, pazarlamadaki karşılığı

Üçüncü günün arka plan yardımcısı. Arka plan yardımcısı, FounderOS'un ağır işleri verdiği yardımcıdır; sen onu görmezsin, sonucu FounderOS anlatır.

İşi tek cümleyle: nisi-sec'in seçtiği üç nişin gerçekten satış yapılabilir bir pazar olup olmadığını canlı sayılarla kontrol etmek.

Neden bu iş var: niş kartlarındaki rakamlar yazıldıkları tarihte doğruydu, ama senin şehrinde bugün ne olduğunu söylemiyorlar. Kart Türkiye'de kaç klima servisi olduğunu yazar; senin ilinde 340 mı yoksa 60 mı olduğunu yazmaz. O sayı yanlışsa doksan günün tamamı yanlış kurulur.

Pazarlamadaki karşılığı: bu kontrolün ekranı, FounderOS'un tanıtım sayfasında gerçek ekran görüntüsüyle kanıt olarak gösterilir.

Şunlar bu yardımcının işi değildir:
- Niş seçmek. O nisi-sec'in işi; bu yardımcı sadece sayı üretir.
- Aday listesi çıkarmak. O sekizinci gün, aday-listesi-cikar modülünde. Aynı tarama kullanılır ama amaç farklıdır: burada sayıyoruz, orada listeliyoruz.

## 2. Ne zaman çalışır

- nisi-sec çağırınca, üç niş için birden. Yarım saat sürer.
- Bir daha çalışmaz. Niş değiştirme konuşulursa yeniden çağrılır.

## 3. Ne okur

nisi-sec'ten: üç nişin adı, şehir, tarih.
Niş kartlarından: "reklam kütüphanesi kelimeleri" ve "rekabetin şekli" bölümleri.
İş Beyni'nden: aday listesi çıkaran programın anahtarı. Anahtar, o programı çalıştırmak için gereken şifredir.

## 4. Ne sorar

Sormaz, sana hiç konuşmaz. Anahtar yoksa FounderOS'a "anahtar yok" der ve elle sayım yoluna geçilir.

## 5. Ne yapar

### Sayım

Her niş için sırayla:

1. Google Haritalar'dan o şehirdeki işletme listesini çeker. Aramada kartın kategori adlarını kullanır.
2. Listeden rastgele otuz işletme seçer. Her biri için beş şeye bakar: telefon var mı, Instagram var mı, sahibinin adı görünüyor mu, kaç yorumu var, son yorumu ne zaman.
3. Reklam tarafına bakar: kartın kelimeleriyle Meta Reklam Kütüphanesi'ni şehir bazlı tarar. Meta Reklam Kütüphanesi, Facebook ve Instagram'da kimin reklam verdiğini gösteren açık sayfadır.
4. Türkiye geneli sayıyı kartın rekabet bölümünden alır. Şehir sayısını canlı sayar.

Neden otuz işletme: hepsini kontrol etmek saatler sürer ve otuzda çıkan oran yüzde kaçlık bir hata payıyla bütünü temsil eder. Otuzun altında güvenilmez, üstünde zaman kaybı.

Reklam sayfasına hangi yoldan bakılacağı henüz karara bağlanmadı. Karar gelene kadar o sütuna "görülemedi" yazılır ve o niş yorum sayısına göre puanlanır. Sayı uydurulmaz.

### Beş soru

Her nişe aynı beş soru sorulur ve cevaplar tabloya yazılır:

1. Bu şehirde en az 500 işletme var mı? Üçüncü günde 500 kişilik aday listesi çıkacak ve doksan günde ona 1.320 arama yapılacak. Bu sayının altında liste dolmuyor.
2. Türkiye'de en az 2.000 işletme var mı? Şehirde 500 çıkmazsa niş Türkiye geneline açılıyor, o zaman bu sayı devreye giriyor. Ülke çapında büyük bir pazar aranmıyor; dört müşteri için 2.000 yeter. Gerekçe tabloya yazılır.
3. Reklam veren oranı en az yüzde on mu? Reklam veren işletme, pazarlamaya para ayırmayı zaten kabul etmiş işletmedir. Bakılamadıysa "görülemedi" yazılır ve bu soru elemez.
4. Telefonu ya da Instagram'ı açık olanlar en az yüzde yetmiş mi? Ulaşamadığın işletmeye satamazsın.
5. Bu ay bu nişin sezonu mu, ve para hesabı tutuyor mu? Para hesabı nisi-sec'te yazılı: aylık ücretin beş katı, o işletmenin ayda kurtarabileceği para olmalı.

### Altıncı sütun: rakip

Bu sütun eleme yapmaz, bilgi verir. Sorusu şu: bu şehirde bu nişe WhatsApp botu, yapay zeka asistanı ya da kendiliğinden giden mesaj sistemi satan biri var mı.

Nasıl bakılır: Google'da ve Instagram'da "şehir adı, niş adı, whatsapp botu" ve "şehir adı, niş adı, yapay zeka asistan" aranır. On dakika sürer. Böyle biri varsa adı ve ne vaat ettiği yazılır.

Bu bilgi teklifi-yaz ve adaya-mesaj-yaz modüllerine gider. Rakip varsa niş düşmez, sadece açılış cümlesi değişir.

### Sonuç

nisi-sec'e üç satır ve altı sütunluk bir tablo döner. Her hücrede rakam ve o rakamın nereden geldiği yazar. Tablonun altında tek satır: birinci aday şu, sebebi şu.

FounderOS bunu sana kendi cümlesiyle anlatır ve tabloyu gösterir.

### Veri konusunda bir not

Bu tarama herkese açık yerlerden işletme bilgisi topluyor: harita kaydı, işletme telefonu, işletme hesabı. Şahıs işletmelerinde bu bilgilerin kişisel veri sayılıp sayılmadığı net değil. Tarama sonucu yalnız senin bilgisayarında durur, kimseyle paylaşılmaz, satılmaz. Kesin cevabı avukatına soracağız; soru listesine bu da eklendi.

## 6. Ne söyler

Öğrenciye hiç konuşmaz. Bütün çıktısı tablodur.

## 7. Ne yazar

İş Beyni'ne: doğrulama tablosu ve tarihi, hangi sayıların canlı sayıldığı, hangilerinin karttan geldiği.
Niş kartına: bu tarihte bu şehirde sayılan işletme sayısı, kartın "sahadan dolacak" bölümüne.
CRM'e: hiçbir şey. Aday listesi sekizinci gün çıkar.

## 8. Yedek yol

- Aday listesi çıkaran program yoksa ya da kullanım hakkı bittiyse: Google Haritalar'da otuz işletmelik liste elle sayılır. On beş dakika sürer, aynı tablo çıkar, altına "elle yapıldı" notu düşülür.
- Reklam sayfasına bakılamazsa: "görülemedi" yazılır, o soru elemez. Sayı uydurulmaz.
- Şehir sayımı 500'ün altında çıkarsa: aynı niş için Türkiye geneli sayılır ve tabloya iki satır birden yazılır.
- Bir nişin kategori adı Haritalar'da tutmuyorsa: kartın diğer kategori adları denenir. Hiçbiri tutmazsa "sayılamadı" yazılır ve o niş elenmez, karar diğer sorulara kalır.
- Programın çalıştırma maliyeti maliyet tablosuna yazılır.

## 9. Sıradaki adım ve işaretler

İş bitince nisi-sec'e döner.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Üç nişten hiçbiri beş sorudan üçünü geçemiyor: "aday havuzu zayıf" denir ve nisi-sec üç yeni niş çıkarır.
- Üç nişin de şehir sayısı 500'ün altında: coğrafya Türkiye geneline açılır.
- Rakip sütunu dolu: teklifi-yaz ve adaya-mesaj-yaz'a not gider.
- Kartın Türkiye geneli sayısı ile canlı sayım arasında büyük fark var: kart eskimiş demektir, işaretlenir ve güncellenir.

Beş kural: boş sayfa yok (kartın kelimeleri ve beş soru hazır gelir) · sessiz bitiş yok (tablo ve tek satırlık sonuç) · onay (kayıt yapmaz, onay gerekmez) · sahadan güncelleme (canlı sayım kartın sahadan dolacak bölümüne yazılır) · sormaz söyler (öğrenciye hiç konuşmaz, sonucu FounderOS anlatır).
