---
user-invocable: false
name: aday-denetimi-cikar
description: Sekizinci ve dokuzuncu gün hızlı denetim, sonra her sabah derin denetim ve sızıntı puanı.
---

# aday-denetimi-cikar

## 1. Adı, rolü, pazarlamadaki karşılığı

Bir işletmeye ulaşmadan önce, o işletmenin müşterisini nerede kaçırdığını dışarıdan bakarak tek sayfaya çıkaran modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Çıkardığı sayfanın adı **denetim kartı**.

Neden var: soğuk mesajın çalışıp çalışmaması tek şeye bağlı, o da mesajın o işletmeye ait olup olmadığı. "Merhaba, işletmenizin dijital varlığını inceledim" diye başlayan mesaj hiçbir şey incelememiş demektir ve işletmeci bunu ilk satırda anlıyor. Denetim kartı, mesajın ilk cümlesine koyacağın gerçek bulguyu üretir. Dört kanalın dördü de aynı karttan besleniyor: telefon, e-posta, Instagram, video.

Pazarlamadaki karşılığı: aday araştırması ve denetim.

Şunlar bu modülün işi değil: listeyi çıkarmak (aday-listesi-cikar), canlı arama ve yazma testleri (kanitini-hazirla), mesajın kendisini yazmak (adaya-mesaj-yaz), video çekmek (video-mesaj-cek), takip sisteminin kurulması (musteri-takip-sistemini-kur).

Tek kural, karıştırma: denetim kartında sadece gördüğün şey yazar. Görülemeyen satıra "bakılamadı" yazılır. Tahmin, yorum ve "muhtemelen" yasak; mesaja giren tek bulgu, ekranda gördüğün bulgudur.

## 2. Ne zaman çalışır

İki hâli var ve ikisi ayrı işler.

**Hızlı denetim.** İşletme başına iki dakika, dışarıdan bakılır, canlı test yok. Sekizinci ve dokuzuncu günde, en çok istenen yüz işletmenin hepsine yapılır. Sonra her ay listenin yenilenmesiyle tekrarlanır. Çıktısı beş satır ve bir puan.

**Derin denetim.** İşletme başına sekiz dakika, canlı testler dahil. Sadece o gün temas edilecek adaylar için, her sabah, sabah bloğunda. Tam zamanlıda günde beş işletme, işin yanında çalışanda üçü. Çıktısı tam denetim kartı.

Sıra şu: hızlı denetim yüz işletmeyi puana göre sıraya dizer, derin denetim her sabah sıranın başındakileri açar.

## 3. Ne okur

İş Beyni'nden: nişin, şehrin, kanal yolun, çalışma düzenin, sistemin adı, Dönüşüm Cümlesi.

Niş kartından: kayıp birimi ve rakamı, sızıntı nerede bölümünün üç sızıntısı, duran havuz tipleri, kanal ve zaman, işletmecinin sözlüğü ve iç sesi, açılış cümlesi, yasal sınırlar.

CRM'den: adayın kaydı, önceki temaslar, hangi kanalların denendiği, kanal durumu satırları.

kanitini-hazirla'dan: o adaya yapılmış canlı arama ve yazılı test sonucu varsa.

## 4. Ne sorar

Hiçbir şey sormaz. Neye bakılacağını, hangi sıraya bakılacağını ve neyin bulgu sayılacağını FounderOS söyler. İki yerde sen devreye giriyorsun ve ikisi de senin telefonunu gerektirdiği için: canlı arama ve yazılı test. Onları sen yapıyorsun, sonucu söylüyorsun, kart dolduruluyor.

## 5. Ne yapar

### Hızlı denetim, beş satır, iki dakika

Beşi de dışarıdan görünüyor, hiçbiri hesap açmayı gerektirmiyor.

**1. Google işletme profili.** İşletmenin adını Google Haritalar'da aç. Bakılan dört şey: yorum sayısı ve puanı, son yorumun tarihi, yorumlara cevap veriliyor mu, son üç yorumda ne şikayet edilmiş. Bulgu sayılan haller: yorumlara hiç cevap verilmemiş; son yorum altı aydan eski; son üç yorumun içinde "aradım açmadılar", "dönmediler", "randevu verdiler gelmediler" gibi bir cümle var; puan 4,0'ın altında.

**2. Site.** Profilde site varsa telefonundan aç. Bakılan: açılıyor mu, telefon numarası ilk ekranda görünüyor mu, WhatsApp düğmesi var mı, iletişim formu var mı. Bulgu sayılan haller: site yok; site açılmıyor ya da çok yavaş; telefon numarası aramadan bulunamıyor; form var ama nereye gittiği belli değil.

**3. Instagram.** Profilde ya da sitede hesap varsa aç. Bakılan: son gönderi tarihi, takipçi sayısı, biyografide telefon ya da WhatsApp bağlantısı var mı. Bulgu sayılan haller: hesap var ama son gönderi üç aydan eski; biyografide hiçbir iletişim yolu yok; hesap var, gönderi düzenli, ama mesaja cevap verilip verilmediği belli değil (bu satır derin denetimde ölçülüyor).

**4. Çalışma saati ve kapanış.** Google profilindeki çalışma saatleri. Bakılan: yazılı mı, akşam kaçta kapanıyor, hafta sonu açık mı. Bulgu sayılan hal: kartın "kanal ve zaman" bölümü o nişte talebin akşam ya da hafta sonu geldiğini söylüyorsa ve işletme o saatlerde kapalıysa, orada kaçan iş var demektir. Bu, o nişin en somut sızıntısı ve mesajda en kolay kabul edileni.

**5. Duran havuz izi.** Kartın duran havuz tiplerinden hangisinin bu işletmede olduğunu gösteren dışarıdan görülebilir işaret. En sık olanı yorum tarihleri: iki üç yıl öncesine giden yorumlar varsa o işletmenin eski müşteri listesi var demektir. Bulgu sayılan hal: eski yorumlar var ve son yorumlar seyrelmiş; yani müşteri gelmiş ve geri gelmemiş.

Her satır bir puan. Toplam sıfırla beş arası ve adı **sızıntı puanı**. Puan CRM'e yazılır ve yüz işletme buna göre sıralanır. Aynı puandakiler yorum sayısına göre sıralanır, çünkü çok yorum çok iş demek.

Sıfır puan çıkan işletme listeden çıkmaz, listenin sonuna gider. Sıfır puan "sorunu yok" demek değil, "dışarıdan görülmüyor" demek.

### Derin denetim, denetim kartı, sekiz dakika

Hızlı denetimin beş satırının üstüne dört şey daha eklenir.

**6. Canlı arama testi.** kanitini-hazirla'nın kuralıyla, o modülün metnindeki sınırlar aynen geçerli. Kartın "kanal ve zaman" bölümünün söylediği yoğun saatin dışında bir arama. Yazılan: aradığın saat, açıldı mı, kaç çalışta açıldı, sesli mesaj çıktı mı, geri döndüler mi ve ne kadar sonra. Açılmadıysa bu senin en güçlü bulgun oluyor ve mesajın ilk cümlesi bu.

**7. Yazılı test.** Kartın söylediği ana yazılı kanaldan, gerçek bir müşteri sorusu. Yazılan: yazdığın saat, cevap geldi mi, kaç saat sonra, cevabın içinde soru soruldu mu yoksa tek kelime mi. Bu testin sınırları kanitini-hazirla'da yazılı ve aynen geçerli: sahte isim yok, sahte işletme yok, randevu almak yok, fiyat pazarlığı yok.

**8. Reklam izi.** Meta reklam kütüphanesinde işletmenin adı aratılır. Yazılan: aktif reklam var mı, kaç tanesi, ne zamandır yayında, hangi kelimeler geçiyor. Reklam veren işletme para harcıyor demektir ve gelen talebi kaçırıyorsa kaybı iki katı; bu, mesajın en sert cümlesini üretir. Kütüphaneye ulaşılamazsa "bakılamadı" yazılır.

**9. Kim karar veriyor.** Kartın "kim karar veriyor" bölümünün söylediği kişinin adı. Üç yere bakılır: sitenin hakkımızda ve iletişim sayfası, Instagram biyografisi, Google yorumlarına verilen cevapların altındaki imza. Bulunamazsa "bulunamadı" yazılır ve o aday telefon sırasına girmez, yazı sırasına düşer.

### Denetim kartının kendisi

Tek sayfa, sabit yapıda, dokuz satır artı üç sonuç satırı. FounderOS doldurur, sen okursun.

```
İşletme: [kısa ad] · Semt: [semt] · Karar veren: [ad ya da bulunamadı]
1 Google profili: [bulgu ya da temiz]
2 Site: [bulgu ya da temiz]
3 Instagram: [bulgu ya da temiz]
4 Saatler: [bulgu ya da temiz]
5 Duran havuz izi: [bulgu ya da temiz]
6 Arama testi: [saat, sonuç] ya da yapılmadı
7 Yazılı test: [saat, sonuç] ya da yapılmadı
8 Reklam: [var/yok/bakılamadı]
9 Sızıntı puanı: [0-5]

EN GÜÇLÜ BULGU: [tek cümle, gördüğün şey]
LİRA KARŞILIĞI: [kayıp birimi × kartın sızıntı rakamı, tek satır hesap]
SIRADAKİ KANAL: [telefon / e-posta / Instagram / video]
```

**En güçlü bulgu** nasıl seçilir, sıra sabit: canlı arama testinde açılmadıysa o. Açıldıysa ve yazılı test cevapsız kaldıysa o. İkisi de temizse reklam veriyor ama saatleri kapalı olan. O da yoksa yorumlarda çıkan şikayet cümlesi. O da yoksa duran havuz izi. Hiçbiri yoksa kartın açılış cümlesi kullanılır ve mesaj gözlemsiz gider; bu adayın sırası listenin sonundadır.

**Lira karşılığı** tek satır ve hesabı görünür: "Haftada üç akşam kapalısınız; kartın rakamıyla akşam gelen çağrı [sayı], çağrı başına [kayıp birimi], ayda [çarpım]." Rakamların ikisi de kartın kendisinden gelir, buradan uydurulmaz. Kartta rakam yoksa lira karşılığı satırı boş kalır ve mesaj rakamsız gider; uydurulmuş rakamla giden mesaj ilk soruda çöküyor.

**Sıradaki kanal** nasıl seçilir: karar verenin adı bulunduysa ve kartın kanal yolu telefonsa telefon. Ad bulunamadıysa e-posta. Nişin ana kanalı yazıysa ve Instagram hesabı canlıysa Instagram. Sızıntı puanı dörtten yüksekse ve aday en çok istenen yüzdeyse video. Bu seçimi FounderOS yapar, sen seçmezsin.

### Denetimden mesaja

Denetim kartı dört kanala dört farklı cümle veriyor ve dördü de aynı bulgudan çıkıyor. Metinlerin kendisi adaya-mesaj-yaz'da yazılı; burada sadece hangi satırın nereye gittiği yazıyor.

- **Telefon**: en güçlü bulgu, kancanın içine girer. Lira karşılığı telefonda söylenmez, görüşmeye saklanır.
- **E-posta**: en güçlü bulgu birinci cümle, lira karşılığı ikinci cümle, sistemin adı üçüncü cümle.
- **Instagram**: en güçlü bulgu soruya çevrilir, lira karşılığı hiç geçmez. Instagram'da rakam ağır duruyor ve mesaj satış gibi görünüyor.
- **Video**: ekranda gösterilen şey en güçlü bulgunun kendisi olur. Sen konuşurken o ekran açık durur.

Bir bulgu iki kanalda aynı cümleyle kullanılmaz. Aynı adaya hem e-posta hem video gidiyorsa video, e-postanın söylemediği ikinci bulguyu gösterir.

### Denetimin sınırları

Beş şey yapılmaz ve bunların hepsi öğrenciyi başını belaya sokacak şeyler.

- Hesap açmaya, şifre denemeye, kapalı bir sayfaya girmeye çalışmak yok.
- İşletmenin müşterilerine ulaşmak, yorum yazan kişilere yazmak yok.
- Sahte müşteri kimliğiyle randevu almak, keşif çağırmak, fiyat teklifi aldırmak yok. Canlı testlerin sınırı kanitini-hazirla'da yazılı ve o sınır aşılmaz.
- İşletmenin çalışanına ya da rakibine bilgi sormak yok.
- Denetimde bulduğun şeyi başkasına, özellikle başka bir adaya anlatmak yok. Kart senin çalışma notun; müşteriye bile olduğu gibi gönderilmez, içinden çıkan cümle gönderilir.

Bir de şu: denetim kartı adayın kendisine gönderilmez. Gönderilirse iki şey oluyor. Birincisi, işletmeci sayfayı okuyup "sağ ol" diyor ve görüşme hiç olmuyor. İkincisi, sayfayı elemanına verip kendisi düzeltmeye çalışıyor. Kartın işi randevu almak, bilgilendirmek değil.

## 6. Ne söyler

Sabah, derin denetim başlarken: "Bugünün beş adayı hazır, sıra sızıntı puanına göre. İlkinden başlıyoruz: [ad], puan dört. Şimdi tek şey senden: saat [saat]'te bu numarayı ara, açılıyor mu bak, sonucu söyle. Gerisini ben dolduruyorum."
Denetim bitince: "[Ad] için en güçlü bulgu şu: [bulgu]. Lira karşılığı [rakam]. Sıradaki kanal telefon. Arama kartın hazır, kanca bu bulgudan yazıldı."
Öğrenci denetimi atlamak isterse: "Denetimsiz mesaj yüzde bir cevap alıyor, denetimli mesaj yüzde yedi. Beş dakikayı burada harcamazsan yirmi mesajı boşa harcıyorsun. Hangisi daha uzun sürüyor?"
Öğrenci yüz işletmenin hepsine derin denetim yapmak isterse: "Yüz işletmeye sekiz dakika on üç saat eder ve o gün hiç arama yapmazsın. Derin denetim sadece o gün arayacaklarına. Kalanların hızlı denetimi zaten var ve sırayı o belirliyor."
Bulgu çıkmazsa: "Bu işletmede dışarıdan görünen sızıntı yok. Bu 'sorunu yok' demek değil, 'göremiyoruz' demek. Listenin sonuna gidiyor, kartın açılış cümlesiyle aranıyor. Sıradaki."
Öğrenci uydurmaya kalkarsa: "Bunu görmedin. Görmediğin bulgu mesaja girmez; ilk soruda çöker ve o adayı bir daha arayamazsın. Bakılamadı yazıyoruz, geçiyoruz."

## 7. Ne yazar

CRM'e: her adayın sızıntı puanı, denetim tarihi, denetim kartının tamamı "denetim kartı" satırına, en güçlü bulgu tek satır olarak ayrı alana (mesaj metinleri oradan okuyor), karar verenin adı, reklam işareti, arama testi sonucu ve yazılı test sonucu kendi satırlarına. Kanal durumu satırlarına dokunulmuyor: denetim bir test, temas değil.

İş Beyni'ne: kaç adayın hızlı denetimi yapıldı, kaçının derin denetimi yapıldı, puan dağılımı, hangi bulgu tipi en çok cevap alıyor (bu satır otuz temastan sonra dolmaya başlıyor).

Niş kartına: aynı bulgu tipi yirmi işletmenin on beşinde çıkıyorsa o bulgu kartın "sızıntı nerede" bölümüne sahadan gelen satır olarak eklenir, tarihiyle.

Sonraki modüllere: en güçlü bulgu ve lira karşılığı adaya-mesaj-yaz'a, video senaryosu için video-mesaj-cek'e, görüşme özet ekranı için gorusmeyi-yonet'e.

## 8. Yedek yol

- Google profili açılmıyorsa ya da işletme profilde yoksa: hızlı denetim dört satırla yapılır, puan beşte değil dörtte hesaplanır ve bu kayda yazılır.
- Site ve Instagram ikisi de yoksa: bu tek başına bulgudur ve güçlü bir bulgudur. "İnternette sizi arayan biri sadece Haritalar'daki numarayı buluyor" cümlesi kancanın kendisi olur.
- Canlı arama testi yapılamadıysa (senin telefonun yok, saat uygun değil, aynı gün ikinci kez aranmaz): kart o satır boş gider, en güçlü bulgu sıradaki satırdan seçilir. Test ertesi gün yapılır ve kart güncellenir.
- Meta reklam kütüphanesine ulaşılamazsa: "bakılamadı" yazılır, puana girmez. Bu satırın hiç dolmaması sık oluyor ve sistemi durdurmuyor.
- Karar verenin adı bulunamazsa: aday telefon sırasından çıkar, e-posta ve Instagram sırasına geçer. Sonradan ad öğrenilirse telefona döner.
- Denetim için ayrılan sabah bloğu dolarsa: o gün kaç aday denetlendiyse o kadarıyla sahaya çıkılır. Denetimsiz aday aranmaz; onun yerine listenin altındaki, denetimi hazır olan aday aranır. Saha bloğu hiçbir gün denetim yüzünden kısalmaz.
- Bir aday iki kez denetlenirse: eski kart silinmez, yenisi tarihiyle altına yazılır. Aradaki fark başlı başına bir bulgudur: "üç ay önce de aramıştım, o zaman da açılmamıştı" cümlesi çok güçlü.

## 9. Sıradaki adım ve işaretler

Sıradaki: denetim biten adayın kanalı belli, adaya-mesaj-yaz o kanalın metnini üretir.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Bir aday denetimsiz aranmış: o temas sayılır ama işaret düşer; ikinci kez olursa sabah bloğu denetimle başlar.
- Yüz işletmenin hızlı denetimi dokuzuncu günde bitmedi: sıralama eksik yapılır, kalanlar ilk hafta içinde tamamlanır, saha ertelenmez.
- Otuz denetimde ortalama sızıntı puanı birin altında: liste yanlış seçilmiş demektir, aday-listesi-cikar'ın seçim ölçütleri yeniden çalıştırılır.
- Aynı bulgu tipi on beş işletmede çıkıyor: niş kartına sahadan gelen satır olarak yazılır.
- Elli temas oldu, en güçlü bulgusu "kartın açılış cümlesi" olan adayların cevap oranı diğerlerinin yarısından az: denetim işe yarıyor demektir, sıralama sıkılaştırılır.
- Bir denetim kartında "bakılamadı" sayısı dördü geçiyor: o aday listenin sonuna gider.

Beş kural: boş sayfa yok (dokuz satırın hepsi ve bakılacak yerler hazır gelir) · sessiz bitiş yok (her denetim bir bulgu, bir rakam ve bir kanalla biter) · onay (canlı testleri sen yaparsın ve sonucu sen söylersin, kart senin söylediğinle dolar) · sahadan güncelleme (tekrarlanan bulgu niş kartına yazılır, cevap alan bulgu tipi sıralamayı değiştirir) · sormaz söyler (neye bakılacağını, hangi bulgunun güçlü olduğunu ve hangi kanala gideceğini FounderOS söyler).
