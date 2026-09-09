---
user-invocable: false
name: is-beyni
description: Is Beyni'nin on uc bolumlu semasi, yazma kurallari ve bos sablonu. Kayit ilk kez acilirken ve bir bilginin hangi bolume yazilacagi belirsizken acilir.
---

# İş Beyni (dosyanın yapısı)

İş Beyni, öğrenci hakkında bilinen her şeyin yazıldığı tek dosya. Otuz sekiz modül ondan okuyor ve ona yazıyor. Bu bölüm o dosyanın hangi bölümlerden oluştuğunu, hangi modülün nereye yazdığını ve kuralları tanımlıyor. Modüller "İş Beyni'ne şunu yaz" dediğinde yazılan yer burada tarif edilen bölümdür.

Dosya öğrencinin bilgisayarında duruyor, tek dosya, on üç bölüm. Bölümlerin sırası ve adları sabit; modüller bu adlarla arıyor.

## Kurallar

**Silme yok, üstüne yazma yok.** Bir bilgi değiştiğinde eskisi kalıyor ve yanına yeni hali tarihiyle yazılıyor. "Fiyat 40.000" satırının altına "6 Eylül: 45.000" düşüyor. Sebebi şu: doksan gün sonra neyin ne zaman değiştiğini bilmek, o gün ne olduğunu bilmekten değerli.

**Her satırın tarihi var.** Tarihsiz satır yazılmıyor.

**Kilitli satırlar işaretli.** Mesaj metni, teklifin kelimeleri, fiyatın rakamı ve niş kilitli satırlardır; yanlarında hangi eşikte açılacakları yazıyor. Eşik dolmadan bu satırlar değişmiyor.

**Boş bölüm silinmiyor.** Henüz sırası gelmemiş bölüm başlığıyla duruyor, altında "henüz yok, [kaçıncı] günde dolacak" yazıyor. Öğrenci dosyayı açtığında nerede olduğunu görüyor.

**Öğrenci dosyayı elle düzenlemiyor.** FounderOS yazıyor, öğrenci okuyor ve düzeltme istiyor.

## Bölümler

### 1. Kurucu
Kim olduğu ve nasıl çalıştığı. Lisans anahtarı (ilk mesajda sohbete yazdırılır, buraya yazılır, bir daha sorulmaz), ad, şehir, telefon, e-posta, çalışma düzeni (tam zamanlı ya da işin yanında), haftalık teslimat saati, hazırlık seviyesi, kanal yolu (telefon ya da yazı), klasörün tam yolu, başlangıç tarihi.
Birinci günün tanışma konuşmasından gelenler: ne motive ediyor, ne durduruyor, daha önce ne denedi ve neden bıraktı, düşme riski nerede.
Mali müşavirin adı ve beş sorunun cevabı.
Yazan: isini-kur (birinci gün), hizmet-akisini-ciz.

### 2. Hedef ve para
Hedef gelir, gelir planının bütün basamakları, güncellenmiş müşteri değeri, aylık masraf tablosunun dört bölümü, çıkış hesabının dört satırı ve üç aylık yaşam gideri şartı.
Aylık kâr hesapları buraya tarihiyle ekleniyor: ayın geliri kurulum ve aylık ayrımıyla, gider kalemleri tek tek, kâr marjı, banka hesabındaki değişim.
Yazan: isini-kur, araclari-kur, nisi-sec, kari-hesapla.

### 3. Niş
Seçilen niş, seçim tarihi, coğrafya (şehir mi Türkiye geneli mi), doğrulama tablosu ve tarihi, ikinci ve üçüncü aday niş, sezon durumu.
Niş kilidi: doksan gün ya da beş müşteri, hangisi önce gelirse. Kilidin başlangıç tarihi burada yazılı.
Yazan: nisi-sec, nisi-dogrula.

### 4. Teklif ve fiyat
Dönüşüm Cümlesi beş parçasıyla, sistemin adı, bir dakikalık anlatım, üç kademenin nişe özel içeriği.
Kurulum ücreti, aylık ücret, karşılaştırma fiyatı, deneme fiyatı işareti ve üç karşılık, güvence cümlesinin tam metni ve şartları, "fiyat ne" sorusunun cevabı.
En sık çıkan üç itiraz ve cevapları. Kartın kaçan müşteri rakamı ve o rakamdan çıkan kurtarma tahmini.
Kilitli satırlar: teklifin kelimeleri on görüşmede, fiyatın rakamı otuz görüşmede açılıyor. Her sürüm tarihiyle duruyor.
Yazan: teklifi-yaz, fiyati-belirle, gorusmeyi-analiz-et.

### 5. Teslimat
Müşteriye gösterilecek beş satır, saat tablosu ve tahmin oldukları notu, kapasite bölmesi ve ölçülecek satırlar, görüşmede söylenecek üç cümle, müşteriden istenecekler listesi, dört dosyanın adı ve durumu.
Yazan: hizmet-akisini-ciz.

### 6. Marka ve varlıklar
Marka kitinin yeri, renkler, yazı tipleri, logo ve en küçük boyutu, görsel yön.
Instagram kullanıcı adı ve hesap yaşı, profil fotoğrafının yeri, WhatsApp Business numarası ve karşılama mesajı, e-posta imzası metni, YouTube kanal adresi, biyografi metni ve sürümü.
Alan adı ve nereden alındığı, canlı site adresi, ön görüşme sayfasının adresi, proje klasörünün yeri, siteyi yeniden başlatma komutu, sayfanın metin sürümü ve tarihi, hangi bölümlerin gizli olduğu.
Video adresleri: ön görüşme videosu, üç itiraz videosu, deneme videosu, kanıt ekran kaydı.
Yazan: markani-kur, kisisel-markani-kur, siteni-kur, satis-videosunu-cek, satis-sayfasini-yaz, isini-kur.

### 7. Araçlar ve hesaplar
CRM bölümünün adresi, bağlanan Google hesabı, işaretlenen çalışma saatleri, arama yapacağın numara, sesli mesaj metni.
Apify hesabı, programın anahtarı, kalan kredi, harcanan kredi, on kayıtlık denemenin dosyası ve tarihi.
Claude aboneliğinin aylık tutarı.
Demo hattının numarası, demo alt hesabı, demo kaydının yeri ve tarihi.
Ödeme sağlayıcı ve link adresleri, şirket ve vergi levhası durumu, sözleşmenin sürümü ve doldurulma tarihi.
CRM kurulumu: dokuz aşamanın doğrulandığı, kayıt satırlarının tam listesi, takip zincirinin günleri, aynı numaranın birleştiğinin doğrulandığı.
Yazan: araclari-kur, musteri-takip-sistemini-kur, aday-listesi-cikar, kanitini-hazirla, onay-belgesini-hazirla, isini-kur (on birinci gün).

### 8. Listeler
Sıcak çevre: A listesindeki kişi sayısı, B listesindeki kişi sayısı, listenin çıkarıldığı tarih, hangi kaynaklardan tarandığı.
Soğuk liste: çıkarılma tarihi, ham kayıt sayısı, elenen sayı, kalan sayı, kaç işletmenin sahibinin adı bulundu, kullanılan kategori adı ve kapsanan semtler.
En çok istenen yüz işletme: seçim tarihi, kaç kişi, hangi ölçütlerle seçildi.
Yazan: tanidik-listesi-cikar, aday-listesi-cikar.

### 9. Mesajlar ve kanıt
Her kanalın mesaj metni, sürümü ve tarihi. Sıcak çevrenin iki mesajı ve mesajda geçen sayı. Kanca listesi ve hangisinin cevap aldığı. Günlük gönderim sayısı ve e-posta alıştırma tarihi.
Kanıt: deneme aramasının sonuçları, kanıt cümlesi ve güncellenme tarihi, kanıt hikâyesi, paylaşım izninin yazılı olup olmadığı.
Kilitli satır: mesaj metni üç yüz temasta açılıyor, elli temastan önce hiç dokunulmuyor.
Yazan: adaya-mesaj-yaz, tanidiga-mesaj-yaz, video-mesaj-cek, kanitini-hazirla.

### 10. Sayılar
Gün sayacı; birinci bölümdeki başlangıç tarihinden hesaplanır, ikisi tutmuyorsa tarih üstündür. Her akşamın beş sayısı, sıcak ve soğuk ayrımıyla, tarihiyle. Haftalık toplamlar. Akşamın tek cümlesi.
Sayaçlar: görüşme sayacı, prova sayacı, itiraz sayacı, fiyat itirazı sayacı, evet ile ödeme arası süre.
Eşikler ve nerede olunduğu: iki yüz temas, üç yüz temas, otuz randevu, otuz görüşme. Bu satırı her akşam rakamlari-oku yazar.
Yazan: rakamlari-oku, gorusmeyi-analiz-et, gorusme-provasi-yap, gorusmeye-getir, video-mesaj-cek, gunu-planla.

### 11. Kararlar
Haftalık karar kaydı. Her satırda: haftanın tarihi, dört halkanın sayıları, en zayıf halka ve sebebi, değişikliğin numarası, ne değiştirildi, geçen haftanın kararının sonucu.
Tek değişken kuralı burada denetleniyor: aynı hafta iki değişiklik yazılmışsa o testin verisi geçersiz sayılıyor.
Yazan: degisiklige-karar-ver.

### 12. Müşteriler
Her müşteri için ayrı bir alt başlık. Bir müşterinin bu alt başlığının adı bilgi dosyası; modüller "bilgi dosyasına yaz" dediğinde yazılan yer burasıdır, ayrı bir dosya değildir.
İçinde: adı, işletmesi, başlangıç tarihi, kademe, kurulum ve aylık ücret, kurulum döneminin günü, alınan giriş izinleri, İYS sonucu, karekodun yeri, asistanın kuralları, telefon hattının bilgileri ve sesli ajanın ayarları, haftalık kontrol sonuçları, kriz kayıtları, yirmi birinci gün raporunun üç sayısı, kapsam dışı kalan parçalar ve sebepleri, aktif mi, kim bağladı.
Ayrıca: aktif müşteri sayısı, ilk müşteri tarihi, müşteri başına haftalık saat.
Yazan: musteriyi-karsila, musteri-sistemini-kur, yazili-asistani-kur, sesli-ajani-kur, kaybolanlari-geri-getir, yorum-topla, sistemi-kontrol-et, aylik-raporu-hazirla, musteriyi-elde-tut, zor-konusmayi-yonet, onay-belgesini-hazirla, kari-hesapla.

### 13. Açık işler
Bekleyen sorular ve her birinin hangi güne ya da hangi eşiğe bağlı olduğu. Ertelenen istekler ve hangi eşikte açılacakları. Ertesi güne kalan iş.
Bu bölüm her sabah gunu-planla tarafından okunuyor; sırası gelen açık iş o günün planına giriyor.
Yazan: bütün modüller.

## Doksan Gün Planı nerede duruyor

Doksan Gün Planı İş Beyni'nin içinde değil, ayrı bir dosya olarak yanında duruyor. On altı bölümlük metin ikinci günün akşamında bir kere yazılıyor ve doksan gün boyunca modüller ona bakıyor. gorusmeyi-analiz-et sahadan gelenlerle günceller.

Niş kartı da ayrı bir dosya olarak duruyor. Kart on altı bölümlü sabit yapıda, sonunda bir de Kaynaklar bölümü var; modüller kartı bölüm adıyla okuyor: Kapsam, Gerçek fiyatlar ve kapasite (sonunda kayıp birimi), Sızıntı nerede, Sezon, Rekabetin şekli, Kim karar veriyor, İşletmecinin gerçek dertleri (sonunda sözlüğü ve iç sesi), Açılış cümlesi, Duran havuz, Asistan kuralları, Kanal ve zaman, Reklam kütüphanesi kelimeleri, Yasal sınırlar, Yoğun şehirler, Gerçek itirazlar ve karşılıkları (başında en güçlü üç itiraz), Sahadan dolacak, Kaynaklar.

Yani öğrencinin yanında üç dosya var: İş Beyni, Doksan Gün Planı, niş kartı. Modüller üçünü de bölüm adıyla okuyor. Müşteri geldiğinde dördüncü bir dosya açılmıyor: müşterinin bilgi dosyası, İş Beyni'nin on ikinci bölümündeki alt başlığın kendisidir.

---

# Boş şablon

Yeni bir öğrencinin kaydını açarken bu şablonun birebir kopyasını yazarsın. Bölüm adlarını ve sırasını değiştirmezsin.

Bu dosyayı FounderOS yazar, öğrenci okur. Elle düzenlenmez.

Kurallar: silme yok, üstüne yazma yok. Değişen bilginin yenisi tarihiyle altına yazılır. Her satırın tarihi vardır. Boş bölüm silinmez, altına "henüz yok, [kaçıncı] günde dolacak" yazılır. Kilitli satırın yanında hangi eşikte açılacağı yazar.

Bu şablon boş haliyle kopyalanır ve doldurulur. Bölüm adları ve sırası değişmez; modüller bu adlarla arar.

---

## 1. Kurucu

- Lisans anahtarı:
- Ad:
- Şehir:
- Telefon:
- E-posta:
- Çalışma düzeni (tam zamanlı / işin yanında):
- Haftalık teslimat saati:
- Hazırlık seviyesi:
- Kanal yolu (telefon / yazı):
- Klasörün tam yolu:
- Başlangıç tarihi (birinci günün tarihi):
- Ne motive ediyor:
- Ne durduruyor:
- Daha önce ne denedi, neden bıraktı:
- Düşme riski nerede:
- Mali müşavir:
- Beş sorunun cevabı:

## 2. Hedef ve para

- Hedef aylık gelir:
- Gelir planının basamakları:
- Müşteri değeri:
- Aylık masraf tablosu:
- Çıkış hesabı:
- Üç aylık yaşam gideri şartı (durum):
- Aylık kâr kayıtları (tarihli, üstüne eklenir):

## 3. Niş

- Seçilen niş:
- Seçim tarihi:
- Coğrafya:
- Doğrulama tablosu ve tarihi:
- İkinci aday niş:
- Üçüncü aday niş:
- Sezon durumu:
- Niş kilidi (doksan gün ya da beş müşteri, başlangıç tarihi):

## 4. Teklif ve fiyat

- Dönüşüm Cümlesi (beş parça):
- Sistemin adı:
- Bir dakikalık anlatım:
- Kademe 1 içeriği:
- Kademe 2 içeriği:
- Kademe 3 içeriği:
- Kurulum ücreti:
- Aylık ücret:
- Karşılaştırma fiyatı:
- Deneme fiyatı ve üç karşılık:
- Güvence cümlesinin tam metni:
- Güvencenin şartları:
- "Fiyat ne" sorusunun cevabı:
- En sık çıkan üç itiraz ve cevapları:
- Kaçan müşteri rakamı ve kurtarma tahmini:
- KİLİT: teklifin kelimeleri on görüşmede açılır. Fiyatın rakamı otuz görüşmede açılır.

## 5. Teslimat

- Müşteriye gösterilecek beş satır:
- Saat tablosu (tahmindir):
- Kapasite bölmesi ve ölçülecek satırlar:
- Görüşmede söylenecek üç cümle:
- Müşteriden istenecekler listesi:
- Dört dosyanın adı ve durumu:

## 6. Marka ve varlıklar

- Marka kitinin yeri:
- Renkler:
- Yazı tipleri:
- Logo ve en küçük boyutu:
- Görsel yön:
- Instagram kullanıcı adı ve hesap yaşı:
- Profil fotoğrafının yeri:
- WhatsApp Business numarası ve karşılama mesajı:
- E-posta imzası:
- YouTube kanal adresi:
- Biyografi metni ve sürümü:
- Alan adı ve nereden alındığı:
- Canlı site adresi:
- Ön görüşme sayfasının adresi:
- Proje klasörünün yeri:
- Sayfanın metin sürümü ve tarihi:
- Gizli duran bölümler:
- Video adresleri (ön görüşme, üç itiraz, deneme, kanıt ekran kaydı):

## 7. Araçlar ve hesaplar

- CRM bölümünün adresi:
- Bağlanan Google hesabı:
- Çalışma saatleri:
- Arama yapılacak numara:
- Sesli mesaj metni:
- Aday listesi programı, anahtar, kalan kredi, harcanan kredi:
- On kayıtlık denemenin dosyası ve tarihi:
- Yapay zeka aboneliğinin aylık tutarı:
- Demo hattı numarası, demo alt hesabı, demo kaydının yeri ve tarihi:
- Ödeme sağlayıcı ve link adresleri:
- Şirket ve vergi levhası durumu:
- Sözleşmenin sürümü ve doldurulma tarihi:
- CRM kurulumu (dokuz aşama, kayıt satırları, takip zinciri, numara birleşmesi):

## 8. Listeler

- Sıcak çevre: A listesi kişi sayısı, B listesi kişi sayısı, çıkarılma tarihi, taranan kaynaklar:
- Soğuk liste: çıkarılma tarihi, ham kayıt, elenen, kalan, sahibinin adı bulunan sayısı, kategori adı, kapsanan semtler:
- En çok istenen yüz işletme: seçim tarihi, kaç kişi, ölçütler:

## 9. Mesajlar ve kanıt

- Telefon metni, sürüm, tarih:
- E-posta metni, sürüm, tarih:
- Instagram metni, sürüm, tarih:
- Sıcak çevrenin iki mesajı ve mesajdaki sayı:
- Kanca listesi ve hangisinin cevap aldığı:
- Günlük gönderim sayısı ve e-posta alıştırma tarihi:
- Deneme aramasının sonuçları:
- Kanıt cümlesi ve güncellenme tarihi:
- Kanıt hikâyesi:
- Paylaşım izni yazılı mı:
- KİLİT: mesaj metni üç yüz temasta açılır, elli temastan önce hiç dokunulmaz.

## 10. Sayılar

- Gün sayacı:
- Akşamın beş sayısı (tarihli, sıcak ve soğuk ayrımıyla, üstüne eklenir):
- Haftalık toplamlar:
- Akşamın tek cümlesi:
- Görüşme sayacı:
- Prova sayacı:
- İtiraz sayacı:
- Fiyat itirazı sayacı:
- Evet ile ödeme arası süre:
- Eşikler ve nerede olunduğu (iki yüz temas, üç yüz temas, otuz randevu, otuz görüşme):

## 11. Kararlar

Her satırda: haftanın tarihi, dört halkanın sayıları, en zayıf halka ve sebebi, değişikliğin numarası, ne değiştirildi, geçen haftanın kararının sonucu.

Tek değişken kuralı: aynı hafta iki değişiklik yazılmışsa o testin verisi geçersizdir.

## 12. Müşteriler

- Aktif müşteri sayısı:
- İlk müşteri tarihi:
- Müşteri başına haftalık saat:

### [Müşteri adı]

- İşletmesi:
- Başlangıç tarihi:
- Kademe:
- Kurulum ücreti:
- Aylık ücret:
- Teslimat günü:
- Alınan giriş izinleri:
- İYS sonucu:
- Karekodun yeri:
- Asistanın kuralları:
- Telefon hattı bilgileri:
- Sesli ajan ayarları:
- Haftalık kontrol sonuçları:
- Kriz kayıtları:
- Yirmi birinci gün raporunun üç sayısı:
- Kapsam dışı kalan parçalar ve sebepleri:
- Aktif mi:
- Kim bağladı:

## 13. Açık işler

- Bekleyen soru, hangi güne ya da eşiğe bağlı:
- Ertelenen istek, hangi eşikte açılacak:
- Ertesi güne kalan iş:
