---
user-invocable: false
name: kaybolanlari-geri-getir
description: "Müşterinin duran havuzu: eski müşteri listesinin uyandırılması, randevu ya da teklif çıkarma. Artı hizmet sonrası üç devam zinciri: tekrar randevu, ek hizmet, referans."
---

# kaybolanlari-geri-getir

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "kaybolanlari-geri-getir"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Müşterinin elindeki eski müşteri listesine mesaj gönderip randevu ya da teklif çıkaran modül; iş modelindeki adıyla Eski Müşteri ve Başvuruyu Yeniden Kazanma (Database Reactivation). Aynı modül, hizmet bittikten sonraki üç devam zincirinin de sahibidir: tekrar randevu, ek hizmet, referans. Teslimatın yedinci gününden on yedinci gününe kadar çalışır. Hazırlığı daha erken başlar: mesaj metinlerini müşteri kurulum görüşmesinde onaylar, Meta'nın onayına ikinci gün, hat CRM'e bağlandığı gün gider. Modül, FounderOS'un belli bir işi yapan parçasıdır.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil.

Dil ayrımı: "müşteri" senin paranı ödeyen işletmedir. Listedeki kişilere "işletmenin eski müşterisi" diyoruz.

Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir. İlk somut sonucu neden buradan bekliyoruz: müşteri o kişilere ulaşmak için parayı zaten ödedi. Liste elinde duruyor ve kimse dokunmuyor. Yeni müşteri bulmaktan hem ucuz hem hızlı.

Bir de şu var: müşteri sana parayı yeni ödedi. İlk hafta boş geçerse pişmanlık başlar. Bu modül o boşluğu doldurur.

Şunlar bu modülün işi değildir:
- Listeyi istemek, hatırlatmak ve sahibinden onay almak. Bunu musteriyi-karsila yapar (üçüncü, altıncı ve yedinci gün).
- Altyapıyı kurmak, listeyi yüklemek, şablon onaylarını almak (musteri-sistemini-kur).
- Gelen cevabı karşılayan yazılı asistanın kuralları (yazili-asistani-kur). Yazılı asistan, müşterinin WhatsApp ve Instagram hesabına gelen mesaja cevap veren, en fazla üç soru sorup randevuyu yazan asistandır.
- Yorum toplamak (yorum-topla).
- Aylık rapor (aylik-raporu-hazirla).

Pazarlamadaki karşılığı: dört sızıntının dördüncüsü. Dört sızıntı, işletmenin müşteri kaybettiği dört yerdir: açılmayan telefon, geç dönülen mesaj, dönülmeyen form, geri aranmayan eski müşteri. Bu modül dördüncüsünü kapatır. Görüşmede sattığın tam sistemin, yani Kademe 2'nin içindedir.

## 2. Ne zaman çalışır

- Kurulum görüşmesinin yapıldığı gün: bu modülün üç mesaj metni de hazır kurulum paketinden çıkar ve müşteri onaylar. İkinci gün, hat CRM'e bağlanınca diğer şablonlarla birlikte Meta'nın onayına gider. Bu işi musteri-sistemini-kur yürütür.
- Yedinci gün: sahibin onayı elinde olur. Aynı gün listeyi FounderOS ikiye ayırır ve temizler, sen sonucu onaylarsın.
- Sekizinci gün: ilk elli kişi. Bu parti aynı zamanda bir testtir.
- Dokuzuncu günden on ikinci güne: günde en çok doksan yeni kişi.
- On birinci günden on dördüncü güne: cevap verenleri tek tek elden geçirme. Akşam bloğunda yapılır.
- On ikinci günden sonra yeni kişiye ilk mesaj gitmez. Kalan liste ikinci aya kalır.
- On beşinci günden on sekizinci güne: eksikler turu. Bu dört gün bu modülün sahipliğindedir. Kurulamayan parçalar kapatılır, kapatılamayanlar kapsam dışı sayılır ve müşteriye yazılı bildirilir, açık kalan işler tek listede toplanır ve rapora hazır edilir. Son takip mesajları bu turla üst üste biner.
- On yedinci günde son takip mesajı da bitmiş olur.
- On dokuzuncu günden rapor gününe: rapor.
- Sonrası: bu kampanya en sık altı ayda bir tekrarlanır, daha sık değil. Talebi yoğun nişte üç ayda bir olabilir. Hiçbir nişte, o nişin kendi doğal tekrar aralığından sık yapılmaz. Doğal aralık yılda birse kampanya da yılda bir olur.

## 3. Ne okur

Müşterinin bilgi dosyasından (`musteriler/<musteri-adi>.md`; her müşteri için tuttuğun geniş dosya): duran havuz listesi, sahibin yazılı onayı, karşılama formundaki mesaj izni sorusunun cevabı ve müşterinin yazılı verdiği izinli numara listesi, müşterinin çalışma saatleri, devri alacak kişinin adı. Mesaj izni kaydı, işletmenin toplu mesaj izinlerini tuttuğu resmi kayıttır; öğrenciye kendiliğinden anlatılmaz.
Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): Duran havuz bölümündeki kimlerin geri çağrılacağı ve uyandırma sebebi; tekrar aralığı orada yazılı değilse Sahadan dolacak bölümüne bakılır. Ayrıca yasal sınırlar, işletmecinin kendi kullandığı cümleler, sezon.
CRM'den (adayların ve müşterilerin kaydedildiği takip programı): yüklenen kayıtlar, gönderim ve cevap sayıları, numaranın kalite notu.
İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı dosya): [21/28] günün takvimi, sistemin adı.

## 4. Ne sorar

Sormaz. Kimin listeye gireceğini müşterinin izin cevabından, mesajın sebebini karttan çıkarır.

Senden aldığı üç şey: müşterinin metne yazılı onayı; ilk elli kişilik partinin sonucu; kızgın cevap geldiyse haberi. Son ikisini CRM'de göreceksin. Dokuzuncu günün sabah bloğunda birinci partinin sayıları önüne gelir; kızgın işaretlenen her konuşma da ayrı bildirim olarak düşer.

## 5. Ne yapar

### Önce izin, sonra mesaj

Kural: listeye yalnız mesaj izni kayıtlı numaralar girer. Sağlık nişlerinde ayrıca kişinin bilgi kullanım onayı gerekir.

Bu kural FounderOS'un kendi işidir. Öğrenciye kural anlatılmaz; öğrenci yalnız sonucu duyar: "Eski listeden izni olan 212 kişiye mesaj gidecek." ya da "Bu parça bu müşteride şimdilik açılmıyor; ücreti ona göre ayarladım." Sayı örnektir, gerçeği ayrımdan gelir. Ücret cümlesi yalnız kurulamayan parça indirimi varsa söylenir.

Hangi numaraların izinli olduğunu müşteri kendi kaydından çıkarır ve yazılı verir. Öğrenci de FounderOS da sorgu yapmaz.

### İzin cevabı nereden gelir

İzin cevabı karşılama formundaki sorudan gelir; FounderOS cevabı formdan okur. Formda cevap yoksa öğrenciye müşteriye gidecek tek cümle hazır verilir, öğrenci onu olduğu gibi gönderir ve açıklamaz: "Eski müşterilerinize toplu mesaj gönderme izni kaydınız (İYS) var mı? Bilmiyorsanız muhasebeciniz bilir." Kayıt varsa ve izinli numaralar listede işaretli gelmediyse ikinci hazır cümle gider: "Listede mesaj izni kayıtlı numaraları işaretleyip gönderebilir misiniz?" Öğrenci ne olduğunu sorarsa tek cümle yeter: "İşletmenin toplu mesaj izinlerini tuttuğu kayıt; cevabı müşteri biliyor, biz sonucu kullanıyoruz." Kaydı yoksa kayıt açtırmak müşterinin kendi işidir; öğrenci bunu müşteri adına yapmaz, ücretini ödemez, müşteriye konuyu anlatmaz. Yedinci güne kadar yazılı cevap gelmezse duran havuz ilk turda kapsam dışıdır, güvencenin sonucuna sayılmaz ve müşteriye o gün yazılı bildirilir; öğrenci yalnız sonucu duyar. Kayıt sonradan çıkarsa parça ikinci turda kurulur.

Listeyi FounderOS ikiye ayırır:
1. İzinli olanlar: mesaj buraya gider.
2. İzni olmayanlar: sistem bunlara hiçbir mesaj göndermez, hiçbir arama listesi çıkarmaz. CRM'de işaretli kalırlar. Kendi kayıtlarıyla ne yapacağına müşteri karar verir, bu senin işin değil.

Sağlık bilgisi taşıyan nişlerde (diş, estetik, güzellik salonunun tıbbi işlemleri, pilates) bir kontrol daha var: mesaj izni tek başına yetmez, kişinin ayrıca bilgi kullanım onayı gerekir. Bu, kişinin "bu bilgimi şu iş için kullanabilirsiniz" diye ayrıca verdiği onaydır. Müşteri bunu yazılı teyit etmezse o kayıt listeye girmez. Teyit müşteriye giden hazır cümleyle alınır, öğrenci açıklamaz: "Bu listede, bilgilerinin bu tür hatırlatmalar için kullanılmasına onay vermiş kişileri işaretleyebilir misiniz?"

Üç sınır daha var; üçü de FounderOS'un kendi kuralıdır ve öğrenciye anlatılmaz. Birincisi: izin işletmenin kendi adına kayıtlı olmalı; öğrencinin adına alınmış izin sayılmaz. İkincisi: izni olmayan eski müşteriye "bakım bildirimi" diye istisna yolundan yazılmaz. Üçüncüsü: randevu, ödeme ya da teslimat bildiriminin içine hiçbir hizmetin tanıtımı konmaz.

Bakım hatırlatması ile pazarlama arasındaki sınırın tam olarak nerede olduğu belli değil. Bu yüzden biz istisnaya güvenmiyoruz, izne bakıyoruz.

### Sebep karttan çıkar, kampanya değil

Bu mesaj indirim duyurusu değildir. Sebebi kartın duran havuz bölümündedir ve kişinin kendi geçmiş işine bağlanır. Kartlardan çıkan en güçlü sebepler:

- Sigorta: poliçenin bitiş tarihi yaklaşıyor. Tarih zaten kayıtlarda, yılda bir.
- Diş: altı ayda bir kontrol; tedavisi yarıda kalanlar.
- Klima ve kombi: sezon öncesi bakım, yılda bir.
- Oto servis: periyodik bakım, on ile on beş bin kilometre arasında bir ya da yılda bir.
- Oto kuaför: üç ile altı ay arasında bir tazeleme, yılda bir kontrol; kaplama iki ile üç yılda bir yenileniyor.
- Cam balkon ve PVC: garanti dönemi içinde kontrol.
- Güzellik salonu: ödediği paketin kalan seansı; lazerde bakım seansının zamanı.
- Haşere: seans süreci ve sezon.
- Pilates: paketi bitip yenilemeyenler; yaz dönüşü.
- Estetik: işlemi yarıda kalanlar.
- Fotoğraf: hamile, yenidoğan, bir yaş zinciri; doğum günü.
- Emlak: kira yenileme zamanı, yılda bir.
- Elektrik ve teknik bakım: sözleşmeli bakım müşterisi.
- Temizlik: mevsimlik iş; halı ve koltuk yenileme.
- Oto galeri, düğün, tadilat, kuaför: en güçlü sebep fiyat sorup kaybolanlar.

Kartta yazan dil uyarıları aynen uygulanır, tek kelimesi değişmez:
- Oto serviste kış lastiği kuralı araç tipine göre değişiyor. Mesajda "zorunlu" kelimesi hiç geçmez. "Hava soğudu, güvenlik için değiştirme zamanı" denir. Zorunluluk sorusu gelirse müşteriye bırakılır.
- Haşerede "kesin çözüm" ve "garanti" kelimeleri geçmez.
- Sigortada asistan hangi acente adına konuştuğunu yazar, sigorta şirketiymiş gibi görünmez.
- Güzellik ve kuaförde tıbbi işlem tanıtımı, öncesi sonrası fotoğrafı ve "hasta" kelimesi yok.
- Diş ve estetikte indirim, kampanya, hediye ve çekiliş yazılmaz. Fiyat da yazılmaz. Hatırlatma kişinin kendi tedavisine bağlanır. Metni klinik yazılı onaylar; kliniğin "onaylıyorum"u yeter.
- Elektrikte sebep sözleşmeli bakımdır. Mesaj bir zorunluluk varmış gibi yazılmaz; "düzenli kontrol zamanı geldi" gibi bir kural ima eden cümle kullanılmaz.

### Sağlık nişlerinin ayrı yolu

Diş ve estetikte mesajla belirli bir hekime ya da kliniğe yönlendiren tanıtım yapılmaz. Kliniğin kendi hastasına giden tek tek hatırlatmanın bu sınıra girip girmediği net değil; o yüzden en güvenli yol seçilir.

Bu yüzden bu iki nişte ilk turda yalnız iki tip yazılır: işlemi ya da tedavisi yarıda kalanlar, ve kliniğin kendisinin verdiği kontrol tarihi gelmiş olanlar. Kliniğin verdiği bir tarih yoksa o kişiye yazılmaz.

Mesaj kişinin kendi tedavisine bağlanır. Hizmet anlatılmaz, fiyat yazılmaz, kampanya olmaz. Metni klinik yazılı onaylar; kliniğin "onaylıyorum"u yeter, kliniğin kendi danışmanına sorması kliniğin işidir. Onay gelmezse bu parça ilk turda kapsam dışıdır ve müşteriye yazılı bildirilir; öğrenci yalnız sonucu duyar.

### Üç mesaj, fazlası yok

Mesajlar müşterinin kendi WhatsApp hattından gider.

Üçü de onaylı şablondur. Onaylı şablon, WhatsApp'ın sahibi Meta'nın önceden onayladığı hazır mesaj metnidir. Üçünde de buna gerek var, çünkü üçünde de karşı taraf son yirmi dört saatte yazmamış oluyor.

Meta her şablonu bir kutuya koyar: ya "hizmet" ya "pazarlama". Bu seçim şablon onaya gönderilirken yapılır ve mesajın hangi sınırlara tabi olacağını belirler. Seçim nişe göre değişir: bakım ve kontrol hatırlatmasında hizmet kutusu denenir, reddedilirse gönderim durur ve metin sadeleşir; kampanya dili taşıyan nişlerde pazarlama kutusu seçilir. Bunu tek tip yapmıyoruz. Sebebi iki tane. Birincisi: sağlıkta mesaj bir hatırlatmadır, pazarlama kutusuna konmaz. İkincisi: kişi başına düşen pazarlama sınırı yalnız pazarlama mesajlarını sayıyor.

Zamanlama:
1. Gün sıfır: sebep ve tek soru.
2. İki gün sonra: hatırlatma.
3. Beş gün sonra: kolay çıkış.

Kalıplar. Köşeli parantezler kartın ve bilgi dosyasının doldurduğu yerlerdir.

Birinci mesaj: "Merhaba [ad], ben [iş adı]. [Sebep: geçen yıl bu dönemde kombinizin bakımını yapmıştık]. [Tek soru: bu yılın bakımını ayarlayalım mı?]"

İkinci mesaj: "Merhaba [ad], [iş adı]. Mesajımı görmemiş olabilirsiniz. [Aynı tek soru]"

Üçüncü mesaj: "Merhaba [ad], [iş adı]. Bu konuda son yazışım. İlgilenirseniz tek kelime yeterli; istemezseniz rahatsız etmeyeyim."

Her mesajın altında tek satır bulunur: "[İş adı] · [MERSİS ya da vergi numarası] · Mesaj istemiyorsanız 'çıkar' yazın." Numara, kurulumda müşteriden alınan satırdan gelir; MERSİS numarası yoksa vergi numarası yazılır. Bu satır her mesajda durur ve hiç çıkarılmaz: işletmeyi tanıtır, kişiye çıkma yolunu gösterir.

Mesaj kısa olur, yaklaşık yüz altmış harf, tek soru. Uzun mesaj okunmuyor.

Metni sadeleştirmek şu demek: sebep cümlesi kalır, soru kalır, çıkma satırı kalır. Onun dışındaki her cümle silinir; hizmet anlatımı, rakam ve "fırsat", "son gün" gibi kelimeler çıkar.

Cevap gelirse zincir durur. Asistan devralır, kuralları yazili-asistani-kur'dan gelir.

### Hacim: günde iki yüz elli mesajı geçmiyoruz

WhatsApp'ın kuralı şu: Meta'nın işletme doğrulamasından geçmemiş bir hat, yirmi dört saat içinde en çok iki yüz elli ayrı numaraya kendisi mesaj başlatabilir. Müşterinin hattı eski olsa da bu sınır geçerli. Bu sayı yeni ve takip mesajlarının toplamıdır, sadece yenilerin değil.

Bir üst basamak iki bindir. Oraya çıkmanın iki yolu var: ya Meta işletmeyi doğrular, ya da otuz gün boyunca şikâyet almadan iki bin mesaj gönderilir. Biz ilk ayda bu basamağa çıkmıyoruz.

Plan buna göre kuruldu:
- Sekizinci gün: elli kişi.
- Dokuzuncu, onuncu, on birinci ve on ikinci gün: her gün en çok doksan yeni kişi.
- Bu günlerde eski partilerin takipleri de gidiyor. En yoğun gün yüz seksen mesaj.
- Kalan yetmiş mesaj boş bırakılıyor. Sebebi şu: aynı hattan randevu hatırlatmaları, yorum istekleri ve cevapsız aramaya dönüşler de gidiyor. Onlar da bu iki yüz elliye sayılıyor.
- Birinci ayın tavanı dört yüz on kişidir. Liste daha uzunsa kalanı ikinci aya kalır. Sıra en yeni işten en eskiye.

Mesajlar hepsi birden gitmez, azar azar gider. Gönderimi CRM yapar: saatte en çok elli mesaj, yalnız müşterinin çalışma saatleri içinde. Sen sabah bloğunda "tamam" dersin, gün içinde eline bakmazsın.

Şunu bilerek kuruyoruz: CRM'de "bugün bu hattan kaç mesaj gitti" diye bakılacak tek bir sayaç yok, iki yüz elliye gelince kendiliğinden duran bir durdurucu da yok. Sayaç bu planın kendisi. Bir günde kaç kişiye gideceğini belirleyen tek şey o gün partiye kaç kişi koyduğun; elindeki gerçek kol bu, başka kol yok. Randevu hatırlatmaları, yorum istekleri ve cevapsız aramaya dönüşler aynı hattan gidiyor ve hiçbir yerde bu partiyle toplanmıyor; boş bırakılan yetmiş mesaj tam olarak onların payı. O yüzden partiyi büyütme, boşluğu doldurma, "bugün az gitti yarın fazla atayım" deme. Günün sayısını FounderOS tutar ve sabah bloğunda önüne koyar.

Kişi başına düşen bir sınır daha var: WhatsApp bir kişinin ne kadar pazarlama mesajı alacağını kendi kısıtlıyor, sayısını açıklamıyor. Sınıra takılan mesaj gitmiyor, en az yirmi dört saat beklemek gerekiyor. Bir istisnası var: kişi cevap verirse yirmi dört saatlik bir pencere açılıyor ve o pencerede yazılanlar bu sınıra sayılmıyor.

### Numaranın kalite notu ve üç durak kuralı

WhatsApp her hatta bir kalite notu veriyor: yeşil, sarı, kırmızı. Notu belirleyen şey son yedi günde kaç kişinin engellediği ve şikâyet ettiği.

Not düşerse ne oluyor: hat önce işaretleniyor, yedi gün içinde düzelmezse günlük sınırı bir kademe iniyor. Sınır dolduğunda yeni sohbet açılamıyor, yalnız gelen mesaja cevap verilebiliyor. Şablon da duraklatılabiliyor: önce üç saat, ikinci kez altı saat, üçüncüde o şablon kapanıyor. Uyarılar sürerse hat günlerce, en sonunda süresiz olarak mesaj başlatamaz hale gelebiliyor. Bunlar FounderOS'un bilgisidir, öğrenciye tehdit olarak anlatılmaz; öğrenci yalnız o günün sayısını ve işini duyar ("Not sarı, bugün yarım parti gidiyor.").

Üç durak kuralı:
1. İlk elli kişi gittikten sonra yirmi dört saat beklenir.
2. Kırmızı not, şablon duraklatma ya da uyarı varsa gönderim durur, metin sadeleşir, not yeşile dönene kadar yeni parti gitmez.
3. Sarı notta günlük parti yarıya iner.
Yeşilse tam hız devam.

Kalite yüzünden duraksarsak gönderim günleri uzar. Yeni takvimi FounderOS hesaplar ve sana verir, sen hesap yapmazsın. On birinci günden on dördüncü güne kadar olan elden geçirme işi yerinde kalır. Gönderilemeyen kişiler ikinci aya kalır. Müşteriye aynı gün yazılı bildirilir.

### Liste temizliği

Sırayla şunlar listeden çıkar:
1. Adı ya da telefonu olmayan satır.
2. Aynı numaranın ikinci kaydı.
3. Sabit hat numaraları.
4. Müşterinin onay listesinde olmayan isim.
5. Müşterinin "bununla aramız bozuk" diye işaretlediği kişi.

Sıra en yeni işten en eskiye. Kartın doğal tekrar aralığının iki katından eski kayıt birinci aya girmez, ikinci aya kalır. Örnek: altı ayda bir kontrol olan bir nişte, son işi bir yıldan eski olan kayıt bekler.

Liste müşterinindir. Senin tarafında kural sabit: iş bitince listeyi silersin; FounderOS silme gününü takvime koyar ve o gün hatırlatır. Listeyi ne kadar saklayacağına müşteri karar verir. Saklama süresiyle ilgili bir soru gelirse cevaplamazsın; FounderOS "Bunu ekip netleştiriyor." der ve destek adresine (destek@founderos.so) gidecek tek satırı müşterinin adıyla hazır verir, sen gönderirsin. İş durmaz.

### Cevap yönetimi

Gelen cevabı asistan karşılar. Beş hal var:
1. İlgileniyor: asistan en fazla üç soru sorar ve randevuyu yazar.
2. İlgilenmiyor: zincir durur, kayıt kapanır.
3. Kızgın: asistanın öfke devri işler, iş insana geçer.
4. "Bir daha yazmayın" diyor: devir yok, zincir durur. O numara çıkma talebi olarak işaretlenir ve müşteriye bildirilir; çıkma talebi en geç üç iş günü içinde işlenir, FounderOS bu süreyi takipte tutar.
   Burada bir tuzak var, bilerek yazıyorum. CRM'in "şu kelime gelirse listeden çıkar" diye çalışan hazır bir özelliği var ama İngilizce kelimelerle ve SMS için kurulmuş; Türkçe "çıkar" yazana kendiliğinden bir şey yapmıyor. Yani çıkma talebini hazır özellik değil, kurulumda açılan bir akış yakalar: gelen mesajda şu kelimelerden biri geçerse akış kaydı mesaj almaya kapatır, işaret koyar, sana ve müşteriye bildirim düşürür. Kelimeler: çıkar, ÇIK, DUR, İPTAL, istemiyorum, rahatsız etmeyin, yazmayın, aramayın, mesaj atmayın, listeden çıkarın. Büyük harf, küçük harf ve Türkçe karaktersiz yazım (cik, iptal, rahatsiz etmeyin) ayrı ayrı yazılır; akış harf farkını kendisi tanımayabilir. Akış hazır pakette yoksa kurulumda FounderOS adım adım gösterir, sen kurarsın. Akışın kaçırdığını asistan yakalar. İkisinin de kaçırdığını bulmak için iki günde bir, sabah bloğunda, konuşmalar ekranında bu kelimeleri ararsın; üç iş günü sınırı haftalık kontrolü beklemez. İkinci tuzak daha pahalı: kayda "çıkma talebi" diye işaret koymak o kişiye mesaj gitmesini DURDURMUYOR. İşaret sadece bir not; başka bir akış aynı kişiye pekâlâ yazar. Durduran tek şey kaydı mesaj almaya kapatmak, yani CRM'in kendi kapatma anahtarını açmak. O yüzden sıra hep aynı: aynı gün kaydı mesaj almaya kapat, sonra işareti koy, sonra müşteriye bildir. İlkini atlarsan çıkma talebi işlenmemiş olur.
5. Yanlış numara ya da hiç cevap yok: zincir kendi akışında biter.

Cevaba geç dönme diye bir sorun burada yok. Cevabı asistan karşılıyor, saat kaç olursa olsun.

### Elden geçirme ve randevuya çevirme

Cevapları asistan ilk günden itibaren anında karşılar, kimse beklemez. On birinci günden on dördüncü güne kadar olan iş ayrı: o günlerde cevap vermiş herkesin listesini tek tek elden geçirirsin. Ortada kalan kimse bırakılmaz, ya randevu olur ya net hayır.

Randevu hatırlatmaları altyapıdan gelir, sayısı artırılmaz. Fazla hatırlatma insanları sinirlendiriyor ve gelme oranını düşürüyor.

Bir de şu: fotoğraf nişinin kartında yedi şikâyetin yedisi de ilk temasta değil, iş satıldıktan sonraki sessizlikten çıkmış. Randevu alan kişiye randevu gününe kadar en az bir kere yazılır. Sessiz kalmak bu listede en pahalı hatadır.

Randevuya gelmeyen kişi, randevudan bir saat sonra giden sonuç sorusuyla yakalanır. Cevabı asistan karşılar.

### Üç devam zinciri: tekrar randevu, ek hizmet, referans

Duran havuz geçmişe yazar; bu üç zincir hizmeti bitmiş müşteriye yazar. Üçü de Kademe 2'nin parçasıdır, üçü de iş modelinde adıyla var, üçü de aynı izin kuralına tabidir: hizmet ilişkisi olan kişiye, mesaj izni kayıtlıysa, tek zincir.

**Tekrar Randevu Alma (Rebooking).** Tetik: hizmetin doğal tekrar aralığı doldu. Aralık karşılama formunun yeni sorusundan gelir: klima bakımı yılda bir, diş kontrolü altı ayda bir, kuaför altı haftada bir, araç kaplama koruma yenilemesi. Mesaj bir hatırlatmadır, kampanya değil: "Geçen bakımın üstünden bir yıl geçti, sezon başlamadan bir gün ayıralım mı." Bir mesaj, bir hatırlatma; cevap gelmezse kapanır, gelirse asistan devralır. Aralığı olmayan hizmette (düğün, tadilat) bu zincir açılmaz.

**Ek Hizmet Satışı (Upsell).** Tetik: hizmet bitti ve işletmenin önceden belirlediği bir ek hizmet bu kişiye uyuyor. Ek hizmet listesi karşılama formunda işletmeden alınır; asistan kendi kafasından ek hizmet önermez. Tek mesaj, hizmet bittikten yedi gün sonra, işletmenin onayladığı cümleyle. Cevap gelirse asistan devralır, gelmezse kapanır; ikinci mesaj yok. Sağlık nişlerinde bu zincir yasal sınırlar bölümüne göre daralır ya da kapanır.

**Referans İsteme (Referral Requests).** Tetik: yorum isteğine olumlu cevap geldi ya da hizmet sonrası memnuniyet mesajı geldi. Yalnızca memnun olduğunu yazana gider; herkese gitmez. Tek mesaj: "Çevrenizde aynı ihtiyacı olan biri varsa bu numarayı verebilirsiniz, ilk görüşme benden." Karşılık teklif edilmez, iyilik olarak istenmez, ikinci mesaj yok. Gelen referans normal aday hattına girer ve kaynağı "referans" yazılır. Sağlık nişlerinde "ilk görüşme benden" cümlesi çıkar, çünkü ücretsiz hizmet sözü kampanya gibi okunur; mesaj "Çevrenizde aynı ihtiyacı olan biri varsa bu numarayı verebilirsiniz." diye biter. Metni klinik yazılı onaylar; onay yoksa bu zincir kurulmaz.

Üç zincirin de metni hazır kurulum paketinde gelir, müşteri kurulum görüşmesinde onaylar. Üçü de raporun "eski müşteri listesinde ulaşılan kişi" satırına değil, ayrı bir satıra yazılır: hizmet sonrası temas ve ondan çıkan randevu ya da teklif.

### Ölçüm

Tutulan sayılar: gönderilen, teslim edilen, okunan, cevap veren, ilgilenen, randevu alan, randevuya gelen, çıkma talebi, engelleme ve şikâyet işareti.

Oran ne zaman hesaplanır: iki yüz kişiye gitmeden metin hakkında teşhis konmaz, üç yüz kişiye gitmeden karar verilmez. Liste bundan kısaysa oran yazılmaz, sayı yazılır. Elli kişilik bir listede yüzde konuşmak yanıltır.

Beklenen oran verilmez. Müşteriye "şu kadar randevu çıkarırım" denmez. Bu listeye ait güvenilir bir Türkiye rakamı yok; başka işlerin yüzdesini buraya taşımak yanıltır. Kendi rakamın ilk müşterilerinden çıkacak.

Rapor gününün raporundaki sayıların çoğu buradan çıkacak.

### Emin olunmayan yerde

Kural net değilse FounderOS en güvenli yolu seçer: o kayda ya da o cümleye mesaj gitmez. Öğrenciden ya da müşteriden cevaplanamayan resmi bir soru gelirse öğrenciye "Bunu ekip netleştiriyor; destek adresine şu satırı gönder." denir ve destek adresine (destek@founderos.so) gidecek tek satır hazır verilir. İş durmaz.

## 6. Ne söyler

Yedinci gün, ayrım bitince (sayı örnektir, gerçeği ayrımdan gelir): "Liste geldi, ayırdım. Eski listeden izni olan 212 kişiye mesaj gidecek. Birinci ay dört yüz on kişiye kadar gidebiliyoruz, fazlası ikinci aya kalıyor. Sonucu onaylarsan yarın ilk elli kişiyle başlıyoruz."
Sekizinci gün: "Bugün elli kişi. Hepsini birden göndermiyoruz, ilk elli tepkiyi ölçmek için. Yarın sabah bloğunda engellenme ve şikâyet var mı bakacağız; temizse tam hız, günde doksan."
Kırmızıya düşerse: "Numaranın notu kırmızı, gönderimi durdurdum. Metni sadeleştiriyorum; not yeşile dönünce elli kişilik yeni bir partiyle devam ediyoruz. Birkaç gün kayar, kalan liste sırasını korur."
Formda izin cevabı boşsa: "Müşteriye şu tek cümleyi olduğu gibi gönder; cevap gelince listeyi ben ayırıyorum." Hemen altına, ayrı satırda ve çift tırnak içinde müşteriye gidecek cümle: "Eski müşterilerinize toplu mesaj gönderme izni kaydınız (İYS) var mı? Bilmiyorsanız muhasebeciniz bilir."
Müşteri "rahatsız olurlar" derse: "Bu kampanya değil, hatırlatma. Kişinin kendi geçmiş işine bağlı. İzni olan numaraya gidiyor ve her mesajda çıkış satırı var. Elli kişiyle başlıyoruz; ilk ellide kötü giderse orada durduruyoruz."
On ikinci gün: "Yeni mesaj işi bitti sayılır, dört yüz on kişiye yazdık. Bundan sonrası tek tek elden geçirme: cevap veren herkes ya randevu alacak ya net hayır diyecek. Ortada kalan bırakmıyoruz."

## 7. Ne yazar

Bilgi dosyasına: izinli ve izinsiz sayıları, izin cevabının tarihi, müşterinin metin onayının tarihi, gönderim günleri ve sayıları, kalite notu kayıtları, çıkma talepleri ve müşteriye bildirildiği tarih, randevu sayısı, ikinci aya kalan kayıt sayısı.
CRM'e: her kaydın izinli mi izinsiz mi olduğu, gönderim durumu, cevabın hangi hale girdiği, randevu, çıkma işareti.
Bir uyarı, bu satırın en pahalı yeri: "izinsiz" ya da "çıktı" diye alana yazmak o kişiye mesaj gitmesini DURDURMUYOR. Alan sadece bir not; başka bir akış aynı kişiye pekâlâ yazar. Durduran tek şey kaydı CRM'in kendi kapatma anahtarıyla mesaj almaya kapatmak. O yüzden izinsiz çıkan her kayıt, listeye yüklendiği gün mesaj almaya kapatılır; alan işareti bunun üstüne, sebebi görünsün diye konur. Sıra hep bu: önce kapat, sonra işaretle.
Niş kartının Sahadan dolacak bölümüne: bu nişte işe yarayan geri çağırma sebebi, en çok cevap alan ilk cümle, çıkma oranı, sahadan doğrulanan tekrar aralığı.

## 8. Yedek yol

- İzin cevabı gelmediyse: gönderim başlamaz, liste bekler, müşteriye yazılı bildirilir. [21/28] gün müşterinin verdiği günden başlar.
- Müşterinin izin kaydı yoksa ya da müşteri bilmiyorsa: hazır soru olduğu gibi müşteriye gider, öğrenci konuyu açıklamaz. Yedinci güne kadar yazılı cevap gelmezse bu parça ilk turda kapsam dışıdır ve güvencenin sonucuna sayılmaz; öğrenci yalnız sonucu duyar.
- Listede hiç izinli numara çıkmadıysa: bu parça ilk turda kapsam dışıdır, müşteriye yazılı bildirilir ve güvencenin sonucuna sayılmaz. Güvence, müşteriye verdiğin sözdür: rapor gününde rapor; raporda sistemin yazdığı randevu sıfırsa ikinci ay ücreti alınmaz. Bu ihtimali kurulum görüşmesinin ikinci maddesinde, güvencenin şartını söylerken zaten söyledin; söylemediysen bugün söylenir.
- İzinli liste elliden azsa: tek parti, tek gönderim, konuşmaları elle okursun. Oran hesaplanmaz, rapora sayı yazılır.
- Şablon onayı gelmediyse: gönderim bekler. Başka kanaldan yazılmaz; bu listede e-posta yedeği de kullanılmaz, çünkü e-posta için ayrı izin gerekir.
- Numaranın notu kırmızıya düşerse: gönderim durur, metin sadeleşir, not yeşile dönünce elli kişilik yeni parti denenir.
- Sağlık nişinde klinik metni onaylamazsa: bu parça ilk turda kapsam dışı, müşteriye yazılı bildirilir.
- Liste kirliyse (yarıdan fazlası eksik satır): temizlenen kısımla başlanır, müşteriden ikinci bir döküm istenir.
- Müşteri listeyi hiç vermezse: [21/28] gün onun listeyi verdiği günden başlar. Yedinci güne kadar da gelmezse bu parça ilk turda kapsam dışıdır, müşteriye yazılı bildirilir ve güvencenin sonucuna sayılmaz.

## 9. Sıradaki adım ve işaretler

Sıradaki: on beşinci günden on sekizinci güne eksikler turu (bu modülde), on dokuzuncu günden itibaren rapor (aylik-raporu-hazirla). Bu modülün son takip mesajları on yedinci güne kadar gitmeye devam eder, ikisi üst üste biner. Yorum toplama ayrı yürür (yorum-topla).

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- İlk elli kişide beşten çok çıkma talebi: metin sert ya da sebep zayıf, metin değişir.
- Kalite notu sarı: günlük parti yarıya iner.
- Kalite notu kırmızı ya da şablon duraklatıldı: gönderim durur.
- İki yüz kişiye gitti, cevap yok: metin değişir. Üç yüze gitti, hâlâ yok: sebep yanlış seçilmiş, kart gözden geçirilir.
- Cevap geliyor ama randevu çıkmıyor: asistanın görev bölümü düzeltilir.
- Müşteri şikâyet aldı: gönderim durur, aynı gün metin ve liste birlikte okunur.

Beş kural: boş sayfa yok (ayrım, üç mesajın metni ve gönderim planı hazır gelir) · sessiz bitiş yok (her gönderim gününün sayısı müşteriye ve bilgi dosyasına yazılır) · onay (metni müşteri yazılı onaylar, gönderim senin "tamam"ınla başlar) · sahadan güncelleme (işe yarayan sebep ve ilk cümle karta yazılır) · sormaz söyler (kimin listeye gireceğini, sebebi ve takvimi FounderOS verir).
