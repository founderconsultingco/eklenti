---
user-invocable: false
name: gunu-planla
description: "Her sabah, saha açıldıktan sonra. Dünü tek cümleyle okur, o günün tek işini, sayılarını ve sırasını verir; günün listesini telefondaki saha ekranına yükler."
---

# gunu-planla

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "gunu-planla"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Her sabah çalışan modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül o gün ne yapacağını söyler.

Neden bu iş var: sıfırdan başlayan biri sabah masaya oturunca ne yapacağını bilmiyor. Bilmediği için önce e-postalara bakıyor, sonra araçları kurcalıyor, sonra bir şeyler okuyor, öğlen oluyor ve henüz kimseyi aramamış oluyor. Gün dolu geçiyor ama iş ilerlemiyor.

İkinci sebep: kolay işle zor iş aynı listede duruyorsa insan kolayı seçiyor. Aramak zor, liste düzenlemek kolay. Plan bu seçimi senin elinden alıyor.

Kural tek: gün satışla başlar. Teslimat, kurulum, araç, öğrenme, hepsi satıştan sonra gelir. Müşteri kazanmayan bir işte teslim edilecek bir şey de olmuyor.

Şunlar bu modülün işi değildir:
- Sayıları okumak (rakamlari-oku, her akşam).
- Haftanın kararını vermek (degisiklige-karar-ver, haftada bir).
- Adayı denetlemek (aday-denetimi-cikar). Plan denetimin sırasını söyler, denetimi kendisi yapmaz.
- Modüllerin kendi içeriğini üretmek. Bu modül sadece sırayı ve o günün tek işini söyler.

Pazarlamadaki karşılığı: sabah ne yapacağını bilen kişi öğlene kadar iş yapmış oluyor, bilmeyen kişi öğlene kadar hazırlanıyor.

## 2. Ne zaman çalışır
- Her gün, sabah bloğunun başında, çalışmaya başlamadan önce. Beş dakika sürer.
- Sabah bloğunun saati çalışma düzenine göre değişir. Plan sana saat vermez, pencere adı verir.
- Saha açıldıktan sonra her gün. Hazırlık kapanmadan bu modül çalışmaz; hazırlığın sırasını ana yönetici beş bloktan kurar.
- Bir gün açılmazsa ertesi sabah iki gün birden gösterir. İki gün üst üste açılmazsa bu bir vazgeçme işaretidir ve planın yerine tek konu gelir.

## 3. Ne okur

İş Beyni'nden: gün sayacı, çalışma düzeni ve günlük temas sayın, günlük temas dağılımı, haftanın kararı, ertelenen işler, kurucu bölümündeki zorlanma riskin.
Durum kaydından (`.founderos/durum.json`): gün, blok, sayaçlar, saha açık mı, sıradaki adım.
Kayıttan (soğuk havuz ve günün sırası `adaylar.csv`'de, CRM açıldıktan sonra da; randevular ve cevap verenler CRM açıldıysa CRM'de, açılmadıysa `adaylar.csv` ve İş Beyni'nin on beşinci bölümünde): bugünün randevuları, cevap bekleyen adaylar, takip günü gelenler, gelmedi işaretli randevular. Dünkü sayılar ve günün sıralanmış saha listesi CRM'de hazır durmuyor; FounderOS kayıtlardan çıkarıp sıraya koyuyor.
Denetim tarafından: hangi adayların denetim kartı hazır, sızıntı puanları, her birinin sıradaki kanalı, bugün derin denetimi yapılacak adayların sırası.
Teslimat tarafından: aktif müşterilerin hangi günde olduğu ve o günün işi.
Takvimden: hangi gün, hangi pencerenin ne kadarı dolu.

## 4. Ne sorar

Sormaz. Planı verir. Senden tek şey ister: her aramadan sonra sonuç düğmesine basman. Akşam sayıları kayıt söyler, sen yazmazsın; sohbete yalnız cevap veren, randevu isteyen ya da yeni bir itiraz söyleyen aday için gelirsin.

Tek istisna var. Plan verilirken bir randevu ya da müşteri işi çakışıyorsa hangisinin öne alınacağını sorar, çünkü takvimini o bilmiyor.

## 5. Ne yapar

### Planın şekli

Plan her gün aynı şekilde gelir ve üç parçadan oluşur:

1. Bugünün tek işi. Bir cümle. Bu, o günün en pahalı işi.
2. Günün sayısı. Kaç temas, hangi kanaldan kaçı.
3. Akşam ne söyleyeceksin. Tek satır: ilerleyen iş ve yarının ilk işi; sayıları kayıt söyler.

Üçten fazla madde konmaz. Beş maddelik plan yapılmıyor, çünkü beş maddelik planın beşincisi hiçbir zaman yapılmıyor.

### Pencereler

Plan hiçbir zaman "sabah dokuzda" demez. Pencere adı söyler ve o pencerenin saatini senin çalışma düzenin belirler. Aynı plan tam zamanlı çalışanla işin yanında çalışanda iki ayrı saate düşer. Dört pencere var ve hiçbiri diğeriyle kesişmez; hangi işin hangi pencereye düştüğünü ana yöneticinin blok listesi ve günlük döngüsü söyler, sayıları aşağıda.

**Sabah bloğu.** Tam zamanlıda 09.00-10.30. İşin yanında çalışıyorsan işe gitmeden önceki bir saat.
**Saha bloğu**, yani aramanın ve mesajın yapıldığı saatler. Tam zamanlıda 10.30-12.30 ve 14.00-17.00. İşin yanında iki parça: arama pencereleri öğle arası (yaklaşık 12.30-13.30) ve cumartesi sabahı (10.00-13.00); akşam 18.00-20.30 yazılı kanalın (e-posta, Instagram) ve hazırlığın saatidir. Kartın kanal ve zaman bölümü akşam telefonun açık olduğunu söylüyorsa akşam da arama yapılır.
**Akşam bloğu**, yani kaydın, sayıların, analizin ve provanın saati. Tam zamanlıda 17.00-18.00. İşin yanında 21.00-22.00.
**Kurulum bloğu**, yani müşteriyle yapılan görüşmeler. İkisinde de müşterinin uygun olduğu saat; işin yanında akşam ya da hafta sonu.
**İçerik penceresi**, yani haftanın içeriğinin çekildiği ve paylaşıldığı kısa zaman. Yalnız pazartesi (elli dakika), çarşamba (on beş) ve cuma (on), günün temasları bittikten sonra. Tam zamanlıda akşam bloğunun arkasına eklenir; işin yanında akşamın yazı saatinin içinde, yazılı temaslardan sonra. Temas bitmeden açılmaz (icerik-motoru).

Plan "sabah" diyorsa sabah bloğunu kastediyor. Nişin kanal ve zaman bölümü saha bloğunun içinde bir daraltma yapıyorsa, yani o işletmelerin telefonunun açık olduğu saatler daha darsa, o daraltma üstündür. İki pencere hiç kesişmiyorsa o gün yazılı kanala geçilir ve plan sebebini söyler.

### Sıra

Gün şu sırayla geçer ve bu sıra değişmez:

**Sabah bloğu: önce denetim, sonra liste.** Plan beş dakikada verilir, hemen ardından o günün derin denetimleri yapılır. Tam zamanlıda beş aday, işin yanında üç; bunlar günün ilk aramaları. Kalan temaslar hızlı denetimle gider, hızlı denetimi olmayan aday listeye girmez. Denetim bitmeden aranacak liste kilitlenmez. Denetimler bitince bugünün saha listesi açılır ve telefondaki saha ekranına yüklenir: üstte dün cevap verenler, sonra takip günü bugüne düşenler, sonra denetimi hazır ve sızıntı puanı yüksek adaylar. Denetimsiz aday listede yoktur: hızlı denetimi olmayan adaya hiçbir kanaldan ulaşılmaz. Sabah denetimi planın parçasıdır ve ertelenmez; aday aracı "denetim bekliyor" derse o adayların hızlı denetimi (işletme başına yirmi saniye) bu sabah yapılır ve liste yeniden kurulur. Denetimi yapılamayan aday o gün listeye girmez; "denetimi yarın yaparız" deyip denetimsiz adayla aranmaz. Sen sıralamıyorsun, sıra hazır geliyor. Dünkü cevaplara dönüş ve e-posta takiplerinin onayı da bu blokta biter.

**Önce satış.** Saha bloğunun ilk yarım saati temasa ayrılır. Aramalar nişin söylediği yoğun saatte yapılır, çoğu nişte bu sabahın ve öğlenin içine düşüyor. Bu blok bitmeden başka bir şey açılmaz.

**Sonra cevaplar.** Gün içinde gelen cevaplara dönülür, randevular yazılır. Bu iş saha bloğunun içindedir, sonrasına bırakılmaz; cevap veren adayın ilgisi bir günde soğuyor.

**Sonra görüşmeler.** Randevu varsa görüşme ve öncesindeki on dakikalık prova. Randevunun saati saha bloğunun dışına düştüyse adayın verdiği saat üstündür ve plan o günü ona göre kurar.

**En son teslimat.** Aktif müşterinin işi. Teslimat akşam bloğundan ve kurulum bloğundan çıkar, saha bloğundan çıkmaz.

Öğrenme, araç kurcalama ve düzenleme günün sonunda kalan zamanda yapılır. Kalmazsa yapılmaz.
Haftanın içeriği bu listede değil: kendi penceresi var ve günün temasları bitmeden açılmaz. Plan onu günün tek işi yapmaz.

Akşam bloğunun içi de sabittir: kayıt kontrolü, günün sayılarının okunması, görüşme yapıldıysa analizi, ertesi günün provası ve ertesi günün listesinin onayı. Akşam bloğu kapanmadan gün kapanmıyor.

### Teslimat ve çalışma düzeni

**Teslimat süresince günlük temas hedefi düşer, ikisinde de.** Tam zamanlıda yüzden altmışa (otuz ana kanal, yirmi dört diğer iki kanal, altı video), işin yanında kırktan yirmiye (on, sekiz, iki); oran aynı kalır. Eskiden tam zamanlıda "hedef düşmez, teslim akşam bloğuna sığar" yazıyordu ve bu yanlıştı: teslimatta senin payın yaklaşık kırk beş saat, akşam bloğu yirmi bir günde otuz bir saat ve o otuz bir saat zaten kayıt, sayım, analiz ve provayla dolu. Aradaki fark sessizce saha bloğundan kapanıyordu; öğrenci sebebini bilmeden sayı tutturamıyordu. Şimdi açık: günde iki buçuk saat teslimata gidiyor ve o saat saha bloğunun içinden çıkıyor. Teslim bitip rapor günü geldiğinde hedef kendiliğinden geri yükseliyor.

İşin yanında çalışıyorsan hedef sadece kurulum haftasında değil, ilk müşterinin **bütün teslim süresinde** yarıya iniyor: sıfırıncı günden rapor gününe kadar, her gün. Kırk temas o dönemde yirmi oluyor. Bir gün daha aynı şekilde yarılanıyor, o da şirket kuruluş günü.

Sebebi rakamda: [21/28] günlük teslimde senin payın yaklaşık kırk beş saat (hattı, sesli ajanı ve müşteri bölümünün açılışını ekip yapar) ve o saatler senin akşam bloğundan çıkıyor. Senin akşam bloğun günde bir saat; teslim süresi boyunca bu saatler kırk beş saati karşılamıyor. Aradaki fark başka bir yerden değil, saha bloğundan alınıyor. Bunu plan baştan yazıyor ki sen hem sayıyı tutturamayıp hem de kendini suçlu hissetme. İlk Müşteri Güvencesi'nin şartı da bu günleri hariç tutuyor.

Teslim bitip rapor günü raporu çıktığı gün hedef kırka döner. Plan bunu kendisi yapar, sen hatırlatmazsın.

### İlk otuz dakika

Kural iki düzende de aynı: saha bloğunun ilk otuz dakikasında o günün ilk temasları gitmiş olacak. Değişen tek şey rakam.

**Tam zamanlı: otuz dakika, yirmi temas.** Bu yirmi, günlük yüzün içindedir, üstüne değil.

**İşin yanında: otuz dakika, on temas.** Bu on, günlük kırkın içindedir. Senin arama pencerenin çoğu öğle arası, bir saat; öğle arasının ilk yarım saatinde on arama gitmiş olacak. Telefonu ilk yarım saatte eline almadıysan gün yazışmaya kayıyor ve yazışmaya kayan gün hedefin altında kapanıyor. Akşam penceresinde de aynı kural yazılı kanal için geçer: oturduğun ilk yarım saatte ilk mesajlar gitmiş olacak. İlk müşterinin teslim süresindeysen günlük sayın yirmi, ilk otuz dakikada beş.

Sebebi şu: günün ilk işi arama olursa gün arama günü oluyor. İlk işi e-posta okumak olursa gün okuma günü oluyor. İlk otuz dakika günün geri kalanının rengini belirliyor.

Denetim bu otuz dakikanın içinde değil, öncesinde. Denetim sabah bloğunda bitiyor, otuz dakika saha bloğuyla başlıyor.

### Arama rampası

Sahanın ilk iki günü aramada rampa var: ilk gün on arama, ikinci gün yirmi, üçüncü günden itibaren planındaki arama sayısı (ana kanal telefonsa tam zamanlıda elli, işin yanında yirmi; ana kanal yazılıysa, örneğin Instagram, kartın "Ana kanal" satırındaki arama payı: işin yanında sekiz, tam zamanlıda yirmi). Rampa en çok sayıdır: planın arama sayısı rampadan küçükse rampa günü de o sayı aranır; Instagram ana kanallı öğrenciye "yarın yirmi arama" denmez. Eksik kalan pay yazılı kanala geçer, e-postanın ve Instagram'ın kendi günlük sınırını aşmadan; sığmayan pay o gün yapılmaz ve kötü gün sayılmaz. Sahanın birinci günü ilk soğuk temas sonucunun kayda geçtiği gündür: açılış akşamının ilk on teması saha ekranından kayda geçtiyse o akşam birinci gün, ertesi sabah ikinci gündür. Panel de aynı günü sayar. Kaçıncı gün olduğunu aday aracının "saha günü" satırı söyler (`kapat`, `bugun` ve `ozet` basar); plan rampayı o satırdan söyler, sen tarihten hesaplamazsın. Açılış akşamı (sahanın birinci günü) yalnız ilk on temastır: günün sayısı on, panelin günün halkası ve saha ekranının sayacı da on gösterir; liste tek adımda kurulur (`bugun --planla --sayi 10 --kanal telefon`, sonra `saha-paketi --yukle`), yazılı pay o akşam yoktur. İkinci günden itibaren rampa yalnız aramayı küçültür, günün sayısını küçültmez: işin yanında yine kırk, tam zamanlıda yüz; panelin günün halkası ve saha ekranının sayacı da bu toplamı gösterir. O yüzden ikinci günden itibaren liste her gün iki adımda kurulur, rampa günü de rampadan sonra da: önce `bugun --planla --sayi <bugünün arama sayısı> --kanal telefon` (rampa günü rampanın sayısı; sonra planın arama sayısı: ana kanal telefonsa işin yanında yirmi, tam zamanlıda elli, teslim süresinde on ve otuz; ana kanal yazılıysa işin yanında sekiz, tam zamanlıda yirmi, teslim süresinde dört ve on), hemen ardından `bugun --planla --sayi <günün sayısı> --kanal yazı` (aramaya alınanlar yeniden planlanmaz, kalan pay yazılı kanaldan gider; telefonu olmayan zaten yazılı gider). Tek komutla günün sayısı telefona yazılırsa saha ekranına bütün liste arama diye gider; panel ise günü arama, mesaj ve video diye böler. Öğrenciye "bugün on arama" ya da "bugün yirmi arama" tek başına söylenmez; aynı cümlede kalan payın yazılı mesajla gittiği ve günün toplamı söylenir, yoksa akşam panel günü "eksik" gösterirken sohbet "tamamladın" der.

### Günün sayısı

Tek kural, her sabah aynı: ana kanaldan elli, diğer iki kanaldan kırk, on video mesaj; işin yanında yirmi, on altı, dört. Ana kanal telefonsa bu elli arama ve kırk yazılı mesaj (yarısı Instagram, yarısı e-posta) demek; ana kanal Instagram'sa elli Instagram, kırk arama ve e-posta. Video ilk hafta beş (işin yanında iki). Instagram tavanı ya da e-posta sınırı o günün payını taşımıyorsa artan pay önce öbür yazılı kanala, o da doluysa aramaya geçer; toplam değişmez. Plan sayıyı kanal kanal verir ve hangi payın nereye geçtiğini tek cümleyle söyler.

### Toplu iş günleri

Bazı işler her gün değil, tek seferde yapılır:

- Aday listesi ve yüz işletmenin hızlı denetimi: ayda bir, listenin yenilendiği gün.
- Mesaj kalıplarının o haftaki güncellenmesi: tek oturuşta, haftalık. Adaya özel yazılı metin haftalık değildir: o günün yazılı adaylarının metni her sabah, saha paketinden önce yazılır (aşağıda, günün listesi).
- Video mesaj çekimi: günde on (ilk hafta beş), arka arkaya, tek oturuşta, saha bloğunun son bir buçuk saatinde; varsa izinden sonraki demo videosu ilk sırada. İşin yanında akşam penceresinde, günde dört (ilk hafta iki).
- Haftanın içeriği: pazartesi sabahı, saha bağlantısı verildikten sonra FounderOS hazırlar; çekim pazartesi akşamı, paylaşım çarşamba ve cuma, içerik penceresinde (icerik-motoru).

Bunları güne yaymak zaman kaybı. Bir işe her gün baştan başlamak, o işi her gün yeniden öğrenmek demek.

Derin denetim bu listede yok. O toplu yapılmıyor, her sabah o günün adayları için yapılıyor; beş dakikalık iş yüz adaya toplu yapılırsa o gün hiç arama yapılmıyor.

### Kötü gün

Sayıyı tutturamadığın gün olacak. Kural şu: telafi yok.

Ertesi gün iki katı yapılmaz. İki katı denenirse iki gün birden kaybediliyor, çünkü ikinci gün de bitmiyor ve moral de gidiyor.

Yapılacak tek şey: ertesi sabah normal sayıya dönmek. Kaç gün tutturduğun sayılır, kaç gün kaçırdığın değil.

Üst üste üç gün tutturulamadıysa o artık kötü gün değil, bir işarettir ve haftanın kararına girer.

### Vazgeçme işaretleri

Şunlardan biri görülürse o günün planı iptal olur ve yerine tek konu gelir:
- Kayıtta iki gün sıfır kayıt (saha ekranında ya da aday listesinde sonuç varsa sıfır sayılmaz).
- Sabah planı iki gün açılmamış.
- Senden "niş değiştirsem", "bana göre değil" gibi bir cümle gelmiş.

"Ara vereyim" tek başına işaret değildir. Tarihi ve sebebi olan ara planlı moladır: FounderOS kaç gün olduğunu sorar, takipleri o güne kaydırır, dönüşte küçültülmüş tek işle başlar (ana yöneticinin "ara verince" kuralı). Tarihsiz, sebepsiz ve ikinci kez gelen "ara vereyim" işarettir.

İşaret gelince önce plana bakılır, kişiye değil: iki gün açılmamış ya da tutmamış planın ilk şüphelisi plandır. İş büyük, belirsiz ya da vaktine sığmıyorsa plan küçülür, sebebi günlüğe yazılır ve inanç konuşmasına girilmez.

O gün plan yerine şu olur: durumun rakamla gösterilir, o güne küçültülmüş tek bir iş verilir, ve sana bugüne kadar ne yaptığın hatırlatılır. Rakamla, övgüyle değil.

Küçültülmüş iş gerçekten küçüktür: yirmi temas, ya da tek arama. Amaç o günü sıfırla kapatmamak.

### Günün kapanış notu, dört sayı

Akşam tek satır yetmiyor, çünkü "kaç temas" sorusunun cevabı kolayca şişiyor. Kapanış notu tarihin altında dört satırdır ve her satırın ne sayıldığı yazılı. İlk iki satırı kayıt doldurur (saha ekranının sonuçları), son ikisini sen söylersin:

- Tarih.
- İlk kez ulaşmaya çalıştığım farklı işletme: kaç ayrı işletmeye ilk kez gidildi.
- İnsan yanıtı aldığım farklı işletme: kaç ayrı işletmeden gerçek bir insan cevap verdi.
- Bugün ilerleyen iş: örnek gönderildi, görüşme yapıldı, teklif gitti gibi gerçekten olan şey.
- Yarın ilk yapacağım iş ve saati.

Sayma kuralları, hepsi tek yönde çalışıyor: kendini kandırmayı zorlaştırmak için.

Aynı işletmeye iki kanaldan gitmek iki işletme değildir, bir işletmedir. Beğeni, takip ve profil ziyareti temas değildir. Otomatik cevap insan yanıtı değildir. Video izlenmesi cevap değildir. Video hazırlamakla göndermek, görüşme planlamakla görüşmeyi yapmak, teklifin beğenilmesiyle paranın gelmesi ayrı sonuçlardır ve ayrı satırlara yazılır.

İlk günlerde yalnız satışa bakılmaz. Doğru kişiye ulaşmak, söz verilen şeyi zamanında göndermek ve takibi unutmamak da ilerlemedir ve kapanış notunda görünür.

### Haftada bir, tek yeri düzelt

Haftanın sonunda son konuşmalara bakılır ve tek bir yer düzeltilir. Sırası şu: yetkiliye ulaşılamıyorsa arama saati ve doğru kişiyi sorma cümlesi; ne satıldığı anlaşılmıyorsa açılış cümlesi; örnek gönderilince konuşma duruyorsa gönderilen şeyin gerçekten konuşulan derdi gösterip göstermediği; görüşmeden sonra ilerlemiyorsa adayın kendi söylediği sebep.

Bir seferde bir şey değişir. Aynı hafta hem niş, hem mesaj, hem kanal değişirse hangisinin işe yaradığı bir daha anlaşılmıyor. Tek retle yöntem değiştirilmez; kilitlerin eşiği degisiklige-karar-ver'de yazılı. Hatalı adres ve çalışmayan bağlantı bu kuralın dışındadır, beklemeden düzeltilir.

### Süreklilik

Bu işte yoğunluk değil, süreklilik kazanıyor. İki hafta günde iki yüz temas yapıp üçüncü hafta duran kişi, on iki hafta boyunca günde seksen yapan kişinin çok gerisinde kalıyor.

Gün sayacı bunun için var. Her sabah planın başında duruyor: kaçıncı gündesin ve şu ana kadar kaç temas yaptın.

## 6. Ne söyler

Normal bir sabah (tam zamanlı): "Gün [sayı]. Bugünün tek işi şu. Önce beş adayın derin denetimi, sonra liste açılıyor. Günün sayısı: elli [ana kanal], kırk diğer iki kanal, on video mesaj. Arama bloğunun ilk otuz dakikasında ilk yirmi temas gitmiş olacak. Listen telefonunda, bağlantı burada; her aramadan sonra sonuç düğmesine bas. Akşam sayıları kayıt söyleyecek."
Normal bir sabah (işin yanında): "Gün [sayı]. Sabah bloğun bir saat: üç adayın denetimi ve dünkü cevaplar. Aramalar öğle arasında, ilk yarım saatte on arama; akşam yazılı mesajlar ve videolar. Günün sayısı kırk: yirmi [ana kanal], on altı diğer iki kanal, dört video. Listen telefonunda, her aramadan sonra sonuç düğmesi."
Saha günü 2 (dün akşam ilk on temas gitti): "Gün [sayı], müşteri bulmanın ikinci günü; dün akşam ilk on temas gitti. Aramada bugün yirmi, yarından itibaren tam sayı. Günün sayısı yine [kırk ya da yüz]: kalan [yirmi ya da seksen] yazılı mesaj ve video, listen ona göre hazır."
Saha günü 1 (açılış akşamında temas gitmediyse): "Gün [sayı], müşteri bulmanın ilk günü. Aramada bugün on, fazlası yok; yarın yirmi, öbür gün tam sayı. Günün sayısı yine [kırk ya da yüz]: kalan [otuz ya da doksan] yazılı mesaj ve video, listen ona göre hazır. İlk yirmi aramanın her birinden sonra kartın not kutusuna otuz saniyelik not."
Denetimden önce: "Plan hazır, beş dakika sürdü. Şimdi bugünün adaylarının denetimi. Denetim bitmeden liste kilitlenmiyor; ilk aramalar bu adaylara, gerisi hızlı denetimle."
Öğrenci araç kurcalamaya başlarsa: "Bugün arama bloğunun temas kısmı bitmedi. O bitmeden başka bir şey açılmıyor. Kurcaladığın şey akşam da orada duruyor, aramadığın işletme akşam orada durmuyor."
Görüşme günü: "Bugün iki görüşmen var. Her birinden on dakika önce prova yapacağız, tek konu. Görüşmeler arasındaki boşluk arama bloğu, boş bırakmıyoruz."
Kötü günden sonra: "Dün sayı tutmadı. Bugün iki katını yapmıyoruz, normal sayıya dönüyoruz. İki katını denersen ikisini birden kaybedersin."
Üç gün üst üste tutmadıysa: "Üç gündür sayı tutmuyor. Bu artık kötü gün değil. Bu hafta neyin değişmesi gerektiğini konuşacağız, ama önce bugünün sayısını tuttur."
Vazgeçme işareti gelirse: "Bugün planı bir kenara bırakıyoruz. Şu an [gün] gündesin ve [sayı] temas yaptın. On dört gün önce sıfırdı. Bugün tek işin var: yirmi temas. Başka hiçbir şey yok."
Teslim süresinde, işin yanında çalışana: "Müşterinin teslim süresindesin, bugün [gün]. Hedefin kırk değil yirmi: on [ana kanal], sekiz diğer iki kanal, iki video. Bu rapor gününe kadar böyle sürecek, sadece kurulum haftası değil. Teslimde senin payın kırk beş saat civarı, o saatler senin akşamından çıkıyor. Bu bir taviz değil, planın içinde yazılı."
Teslim süresinde, tam zamanlı çalışana: "Müşterinin teslim süresindesin. Hedefin yüz değil altmış: otuz [ana kanal], yirmi dört diğer iki kanal, altı video. Bu rapor gününe kadar böyle sürecek. Teslim günde iki buçuk saat alıyor, o saat saha bloğundan çıkıyor; sayı bu yüzden iniyor."
Pazartesi, içerik başladıktan sonra, saha bağlantısını verdikten sonra: "Aramaya başla. Ben bu arada haftanın içeriğini hazırlıyorum, panelinde olacak. Çekim akşam, temasların bitince; elli dakika."
Çarşamba ve cuma, akşam: "Temasların bitti. Bugün paylaşım günü; kesit hazır, on beş dakika."

## 7. Ne yazar

Günlüğe (`gunluk/` altında o günün dosyası, sadece eklenir): o günün planı, planın açıldığı, o gün kaç adayın derin denetiminin yapıldığı, ertesi güne kalan iş.
Durum kaydına (`.founderos/durum.json`; veri bağlantısı açıksa `durum_yaz` ile sunucuya da): açık modül, sıradaki adım, güncellenme saati.
İş Beyni'ne: açık işler bölümünde ertesi güne kalan iş ve "Sonraki adım" satırı; tek değerli alanlar yerinde güncellenir.
CRM'e: hiçbir şey. Kayıtları modüllerin kendisi yazar, plan sadece sırayı verir.
Günün listesi her sabah aday aracıyla kurulur, CRM açık olsa da (aday-listesi-dosyasi): önce iki adımda `bugun --planla` (günün sayısı tam zamanlıda yüz, işin yanında kırk, teslim süresinde yarısı; önce arama sayısı telefonla, sonra günün sayısına kalan pay yazılı, yukarıda "Arama rampası"); bugün sıraya alınan adayların sıradaki tarihi bugüne yazılır, sayfanın Bugünün listesi dolar. Sonra o günün yazılı adaylarının (Instagram, e-posta) metni adaya-mesaj-yaz kuralıyla tek seferde yazılır ve aday aracının `guncelle` komutuyla satırlarına işlenir (`dm_metni`; e-postada `eposta_konu` ve `eposta_metni`); gözlemi olmayan adaya yazılı mesaj yazılmaz, telefona bırakılır. Metinsiz yazılı aday telefonda yalnız "Gönderdim" düğmesi olan boş bir kart olur; `saha-paketi` çıktısı "metni olmayan yazılı aday" derse önce o metinler yazılır. Sonra `saha-paketi --yukle` günün listesini, her adayın ilk cümlesini ve arama senaryosunu servise kendisi yükler ve bağlantıyı basar (araç servise ulaşamazsa FounderOS `.founderos/saha-paketi.json`'u veri bağlantısındaki `saha_yukle` aracıyla yükler); bağlantı öğrenciye verilir: "Bugünün listen telefonunda, şu bağlantıdan aç. Aramayı oradan yap, her aramadan sonra sonuç düğmesine bas." Bağlantı yoksa yedek yol bugünkü sayfa: "Bugünün listesi sayfada, Bugünün listesi sekmesinde; her kartta ne söyleyeceğin yazıyor, her aramadan sonra düğmeye bas, akşam Sonuçları kopyala." Sekiz yüz satır sohbete okunmaz, aracın çıktısı yeter.

## 8. Yedek yol

- Takvim boşsa ya da bağlanmadıysa: plan yine verilir, saatler yerine pencere sırası verilir.
- Randevu ile müşteri işi çakışıyorsa: randevu öne alınır, müşteri işi aynı gün içinde kaydırılır. Randevu ertelenmez.
- Sabah bloğu denetime yetmezse: o gün kaç aday denetlendiyse o kadarıyla sahaya çıkılır. Saha bloğu hiçbir gün denetim yüzünden kısalmaz. Hızlı denetimi olmayan aday o gün listeye girmez; denetim yarına ertelenip denetimsiz adayla aranmaz.
- Saha bloğu ile nişin söylediği saatler hiç kesişmiyorsa: o gün yazılı kanala geçilir ve plan sebebini söyler.
- Gün yarıda kalırsa: kalan iş ertesi güne yazılır ama ertesi günün sayısına eklenmez.
- Hasta olduğun ya da gidemediğin gün: plan verilmez, gün sayacı durmaz. Ertesi gün normal sayıdan devam edilir.
- Aktif müşteri sayısı arttıkça satış bloğu küçülüyorsa: bu kapasite işaretidir, haftanın kararına gider.

## 9. Sıradaki adım ve işaretler

Sıradaki: sabah bloğunda aday-denetimi-cikar, akşam bloğunda rakamlari-oku.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Sabah planı iki gün üst üste açılmadı: vazgeçme işareti, plan yerine tek konu gelir.
- Kayıtta iki gün sıfır kayıt (saha ekranında sonuç varsa sıfır sayılmaz): aynı şekilde.
- Üç gün üst üste günlük sayı tutmadı: haftanın kararına gider.
- Saha bloğunun ilk otuz dakikasında temas yok, beş gün üst üste: sıra bozulmuş demektir, plan sabah bloğunu tek madde haline getirir.
- Sabah bloğu iki gün üst üste denetimsiz kapandı: plan ertesi sabah denetimle başlar, başka madde açılmaz.
- Satış bloğu iki hafta üst üste teslimat yüzünden kısaldı: kapasite kararı açılır.
- Teslim süresi bittiği halde hedef yarıda kaldı: plan hedefi kendisi kırka döndürür ve söyler.
- Prova atlandı: plana uyarı olarak düşer.
- Pazartesi temas sayısı iki hafta üst üste tutmadı: çekim temasın önüne geçmiş demektir; plan çekimi temaslar bitmeden açmaz.

Beş kural: boş sayfa yok (plan üç maddeyle hazır gelir) · sessiz bitiş yok (gün akşam tek satırla kapanır) · onay (plan sana gösterilir, sen uygularsın) · sahadan güncelleme (hangi saatte ne çalıştığı karta yazılır) · sormaz söyler (sırayı ve günün tek işini FounderOS verir).
