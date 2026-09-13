---
user-invocable: false
name: gunu-planla
description: "Her sabah, saha açıldıktan sonra. Dünü tek cümleyle okur, o günün tek işini, sayılarını ve sırasını verir."
---

# gunu-planla

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
Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv` ve İş Beyni'nin on beşinci bölümü): bugünün randevuları, cevap bekleyen adaylar, takip günü gelenler, gelmedi işaretli randevular. Dünkü sayılar ve günün sıralanmış saha listesi CRM'de hazır durmuyor; FounderOS kayıtlardan çıkarıp sıraya koyuyor.
Denetim tarafından: hangi adayların denetim kartı hazır, sızıntı puanları, her birinin sıradaki kanalı, bugün derin denetimi yapılacak adayların sırası.
Teslimat tarafından: aktif müşterilerin hangi günde olduğu ve o günün işi.
Takvimden: hangi gün, hangi pencerenin ne kadarı dolu.

## 4. Ne sorar

Sormaz. Planı verir. Senden tek şey ister: gün bitince akşam sayılarını yazman.

Tek istisna var. Plan verilirken bir randevu ya da müşteri işi çakışıyorsa hangisinin öne alınacağını sorar, çünkü takvimini o bilmiyor.

## 5. Ne yapar

### Planın şekli

Plan her gün aynı şekilde gelir ve üç parçadan oluşur:

1. Bugünün tek işi. Bir cümle. Bu, o günün en pahalı işi.
2. Günün sayısı. Kaç temas, hangi kanaldan kaçı.
3. Akşam ne yazacaksın. Tek satır.

Üçten fazla madde konmaz. Beş maddelik plan yapılmıyor, çünkü beş maddelik planın beşincisi hiçbir zaman yapılmıyor.

### Pencereler

Plan hiçbir zaman "sabah dokuzda" demez. Pencere adı söyler ve o pencerenin saatini senin çalışma düzenin belirler. Aynı plan tam zamanlı çalışanla işin yanında çalışanda iki ayrı saate düşer. Dört pencere var.

**Sabah bloğu.** Tam zamanlıda 09.00-12.00. İşin yanında çalışıyorsan işe gitmeden önceki bir saat ya da öğle arası.
**Saha bloğu**, yani aramanın ve mesajın yapıldığı saatler. Tam zamanlıda 10.00-12.00 ve 14.00-17.00. İşin yanında 18.00-20.30 ve cumartesi 10.00-13.00.
**Akşam bloğu**, yani kaydın, sayıların, analizin ve provanın saati. Tam zamanlıda 17.00-18.30. İşin yanında 21.00-22.00.
**Kurulum bloğu**, yani müşteriyle yapılan görüşmeler. İkisinde de müşterinin uygun olduğu saat; işin yanında akşam ya da hafta sonu.

Plan "sabah" diyorsa sabah bloğunu kastediyor. Nişin kanal ve zaman bölümü saha bloğunun içinde bir daraltma yapıyorsa, yani o işletmelerin telefonunun açık olduğu saatler daha darsa, o daraltma üstündür. İki pencere hiç kesişmiyorsa o gün yazılı kanala geçilir ve plan sebebini söyler.

### Sıra

Gün şu sırayla geçer ve bu sıra değişmez:

**Sabah bloğu: önce denetim, sonra liste.** Plan beş dakikada verilir, hemen ardından o günün derin denetimleri yapılır. Tam zamanlıda beş aday, işin yanında üç; bunlar günün ilk aramaları. Kalan temaslar hızlı denetimle gider, hızlı denetimi olmayan aday listeye girmez. Denetim bitmeden aranacak liste kilitlenmez. Denetimler bitince bugünün saha listesi açılır: üstte dün cevap verenler, sonra takip günü bugüne düşenler, sonra denetimi hazır ve sızıntı puanı yüksek adaylar, en sonda denetimsizler. Sen sıralamıyorsun, sıra hazır geliyor. Dünkü cevaplara dönüş ve e-posta takiplerinin onayı da bu blokta biter.

**Önce satış.** Saha bloğunun ilk yarım saati temasa ayrılır. Aramalar nişin söylediği yoğun saatte yapılır, çoğu nişte bu sabahın ve öğlenin içine düşüyor. Bu blok bitmeden başka bir şey açılmaz.

**Sonra cevaplar.** Gün içinde gelen cevaplara dönülür, randevular yazılır. Bu iş saha bloğunun içindedir, sonrasına bırakılmaz; cevap veren adayın ilgisi bir günde soğuyor.

**Sonra görüşmeler.** Randevu varsa görüşme ve öncesindeki on dakikalık prova. Randevunun saati saha bloğunun dışına düştüyse adayın verdiği saat üstündür ve plan o günü ona göre kurar.

**En son teslimat.** Aktif müşterinin işi. Teslimat akşam bloğundan ve kurulum bloğundan çıkar, saha bloğundan çıkmaz.

Öğrenme, araç kurcalama ve düzenleme günün sonunda kalan zamanda yapılır. Kalmazsa yapılmaz.

Akşam bloğunun içi de sabittir: kayıt kontrolü, günün sayılarının okunması, görüşme yapıldıysa analizi, ertesi günün provası ve ertesi günün listesinin onayı. Akşam bloğu kapanmadan gün kapanmıyor.

### Teslimat ve çalışma düzeni

Tam zamanlı çalışıyorsan ilk müşterinin teslimi günlük temas hedefini düşürmez. Teslim işi akşam bloğuna ve kurulum bloğuna sığıyor, saha bloğuna taşınmıyor.

İşin yanında çalışıyorsan hedef sadece kurulum haftasında değil, ilk müşterinin **bütün teslim süresinde** yarıya iniyor: sıfırıncı günden rapor gününe kadar, her gün. Kırk temas o dönemde yirmi oluyor. Bir gün daha aynı şekilde yarılanıyor, o da şirket kuruluş günü.

Sebebi rakamda: [21/28] günlük teslim bir kişinin yaklaşık elli saatini alıyor ve o saatler senin akşam bloğundan çıkıyor. Senin akşam bloğun günde bir saat; teslim süresi boyunca bu saatler elli saati karşılamıyor. Aradaki fark başka bir yerden değil, saha bloğundan alınıyor. Bunu plan baştan yazıyor ki sen hem sayıyı tutturamayıp hem de kendini suçlu hissetme. Garanti şartı da bu günleri hariç tutuyor.

Teslim bitip rapor günü raporu çıktığı gün hedef kırka döner. Plan bunu kendisi yapar, sen hatırlatmazsın.

### İlk otuz dakika

Kural iki düzende de aynı: saha bloğunun ilk otuz dakikasında o günün ilk temasları gitmiş olacak. Değişen tek şey rakam.

**Tam zamanlı: otuz dakika, yirmi temas.** Bu yirmi, günlük yüzün içindedir, üstüne değil.

**İşin yanında: otuz dakika, on temas.** Bu on, günlük kırkın içindedir. Senin saha bloğun akşam açılıyor ve iki buçuk saat; işten çıkıp oturduğun ilk yarım saatte gün ya başlıyor ya bitiyor. Telefonu ilk yarım saatte eline almadıysan o akşam yazışmaya kayıyor ve yazışmaya kayan akşam hedefin altında kapanıyor. İlk müşterinin teslim süresindeysen günlük sayın yirmi, ilk otuz dakikada beş.

Sebebi şu: günün ilk işi arama olursa gün arama günü oluyor. İlk işi e-posta okumak olursa gün okuma günü oluyor. İlk otuz dakika günün geri kalanının rengini belirliyor.

Denetim bu otuz dakikanın içinde değil, öncesinde. Denetim sabah bloğunda bitiyor, otuz dakika saha bloğuyla başlıyor.

### Toplu iş günleri

Bazı işler her gün değil, tek seferde yapılır:

- Aday listesi ve yüz işletmenin hızlı denetimi: ayda bir, listenin yenilendiği gün.
- Mesaj metinlerinin o haftaki kişiselleştirmesi: tek oturuşta, haftalık.
- Video mesaj çekimi: günde beş, arka arkaya, tek oturuşta, saha bloğunun son yarım saatinde.

Bunları güne yaymak zaman kaybı. Bir işe her gün baştan başlamak, o işi her gün yeniden öğrenmek demek.

Derin denetim bu listede yok. O toplu yapılmıyor, her sabah o günün adayları için yapılıyor; sekiz dakikalık iş yüz adaya toplu yapılırsa o gün hiç arama yapılmıyor.

### Kötü gün

Sayıyı tutturamadığın gün olacak. Kural şu: telafi yok.

Ertesi gün iki katı yapılmaz. İki katı denenirse iki gün birden kaybediliyor, çünkü ikinci gün de bitmiyor ve moral de gidiyor.

Yapılacak tek şey: ertesi sabah normal sayıya dönmek. Kaç gün tutturduğun sayılır, kaç gün kaçırdığın değil.

Üst üste üç gün tutturulamadıysa o artık kötü gün değil, bir işarettir ve haftanın kararına girer.

### Vazgeçme işaretleri

Şunlardan biri görülürse o günün planı iptal olur ve yerine tek konu gelir:
- CRM'de ya da Bugünün listesi'nde iki gün sıfır kayıt.
- Sabah planı iki gün açılmamış.
- Senden "niş değiştirsem", "bana göre değil", "ara vereyim" gibi bir cümle gelmiş.

O gün plan yerine şu olur: durumun rakamla gösterilir, o güne küçültülmüş tek bir iş verilir, ve sana bugüne kadar ne yaptığın hatırlatılır. Rakamla, övgüyle değil.

Küçültülmüş iş gerçekten küçüktür: yirmi temas, ya da tek arama. Amaç o günü sıfırla kapatmamak.

### Süreklilik

Bu işte yoğunluk değil, süreklilik kazanıyor. İki hafta günde iki yüz temas yapıp üçüncü hafta duran kişi, on iki hafta boyunca günde seksen yapan kişinin çok gerisinde kalıyor.

Gün sayacı bunun için var. Her sabah planın başında duruyor: kaçıncı gündesin ve şu ana kadar kaç temas yaptın.

## 6. Ne söyler

Normal bir sabah (tam zamanlı): "Gün [sayı]. Bugünün tek işi şu. Önce beş adayın derin denetimi, sonra liste açılıyor. Günün sayısı: otuz beş arama, otuz Instagram, yirmi e-posta, beş video mesaj. Saha bloğunun ilk otuz dakikasında ilk yirmi temas gitmiş olacak. Akşam bana tek satır yazacaksın: kaç temas, kaç cevap, kaç randevu."
Normal bir sabah (işin yanında): "Gün [sayı]. Sabah bloğun bir saat: üç adayın denetimi ve dünkü cevaplar. Saha bloğun akşam. Günün sayısı kırk. İlk otuz dakikada on temas. Akşam tek satır."
Denetimden önce: "Plan hazır, beş dakika sürdü. Şimdi bugünün adaylarının denetimi. Denetim bitmeden liste kilitlenmiyor; ilk aramalar bu adaylara, gerisi hızlı denetimle."
Öğrenci araç kurcalamaya başlarsa: "Bugün saha bloğunun temas kısmı bitmedi. O bitmeden başka bir şey açılmıyor. Kurcaladığın şey akşam da orada duruyor, aramadığın işletme akşam orada durmuyor."
Görüşme günü: "Bugün iki görüşmen var. Her birinden on dakika önce prova yapacağız, tek konu. Görüşmeler arasındaki boşluk arama bloğu, boş bırakmıyoruz."
Kötü günden sonra: "Dün sayı tutmadı. Bugün iki katını yapmıyoruz, normal sayıya dönüyoruz. İki katını denersen ikisini birden kaybedersin."
Üç gün üst üste tutmadıysa: "Üç gündür sayı tutmuyor. Bu artık kötü gün değil. Bu hafta neyin değişmesi gerektiğini konuşacağız, ama önce bugünün sayısını tuttur."
Vazgeçme işareti gelirse: "Bugün planı bir kenara bırakıyoruz. Şu an [gün] gündesin ve [sayı] temas yaptın. On dört gün önce sıfırdı. Bugün tek işin var: yirmi temas. Başka hiçbir şey yok."
Teslim süresinde, işin yanında çalışana: "Müşterinin teslim süresindesin, bugün [gün]. Hedefin kırk değil yirmi ve bu rapor gününe kadar böyle sürecek, sadece kurulum haftası değil. Teslim elli saat alıyor, o saatler senin akşamından çıkıyor. Bu bir taviz değil, planın içinde yazılı."
Teslim süresinde, tam zamanlı çalışana: "Müşterinin teslimi akşam bloğunda ve kurulum bloğunda. Temas hedefin düşmüyor. Teslim işi saha bloğuna taşınmıyor."

## 7. Ne yazar

İş Beyni'ne: gün sayacı, o günün planı, planın açılıp açılmadığı, tamamlanan blok, o gün kaç adayın derin denetiminin yapıldığı, ertesi güne kalan iş.
CRM'e: hiçbir şey. Kayıtları modüllerin kendisi yazar, plan sadece sırayı verir.
CRM açılmadıysa günün listesi aday aracıyla kurulur (aday-listesi-dosyasi, `bugun --planla`; tam zamanlıda yüz, işin yanında kırk): bugün sıraya alınan adayların sıradaki tarihi bugüne yazılır, sayfanın Saha modu dolar. Öğrenciye: "Bugünün listesi sayfada, Saha modu sekmesinde; her kartta ne söyleyeceğin yazıyor, her aramadan sonra düğmeye bas, akşam Sonuçları kopyala." Sekiz yüz satır sohbete okunmaz, aracın çıktısı yeter.

## 8. Yedek yol

- Takvim boşsa ya da bağlanmadıysa: plan yine verilir, saatler yerine pencere sırası verilir.
- Randevu ile müşteri işi çakışıyorsa: randevu öne alınır, müşteri işi aynı gün içinde kaydırılır. Randevu ertelenmez.
- Sabah bloğu denetime yetmezse: o gün kaç aday denetlendiyse o kadarıyla sahaya çıkılır. Saha bloğu hiçbir gün denetim yüzünden kısalmaz.
- Saha bloğu ile nişin söylediği saatler hiç kesişmiyorsa: o gün yazılı kanala geçilir ve plan sebebini söyler.
- Gün yarıda kalırsa: kalan iş ertesi güne yazılır ama ertesi günün sayısına eklenmez.
- Hasta olduğun ya da gidemediğin gün: plan verilmez, gün sayacı durmaz. Ertesi gün normal sayıdan devam edilir.
- Aktif müşteri sayısı arttıkça satış bloğu küçülüyorsa: bu kapasite işaretidir, haftanın kararına gider.

## 9. Sıradaki adım ve işaretler

Sıradaki: sabah bloğunda aday-denetimi-cikar, akşam bloğunda rakamlari-oku.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Sabah planı iki gün üst üste açılmadı: vazgeçme işareti, plan yerine tek konu gelir.
- CRM'de ya da Bugünün listesi'nde iki gün sıfır kayıt: aynı şekilde.
- Üç gün üst üste günlük sayı tutmadı: haftanın kararına gider.
- Saha bloğunun ilk otuz dakikasında temas yok, beş gün üst üste: sıra bozulmuş demektir, plan sabah bloğunu tek madde haline getirir.
- Sabah bloğu iki gün üst üste denetimsiz kapandı: plan ertesi sabah denetimle başlar, başka madde açılmaz.
- Satış bloğu iki hafta üst üste teslimat yüzünden kısaldı: kapasite kararı açılır.
- Teslim süresi bittiği halde hedef yarıda kaldı: plan hedefi kendisi kırka döndürür ve söyler.
- Prova atlandı: plana uyarı olarak düşer.

Beş kural: boş sayfa yok (plan üç maddeyle hazır gelir) · sessiz bitiş yok (gün akşam tek satırla kapanır) · onay (plan sana gösterilir, sen uygularsın) · sahadan güncelleme (hangi saatte ne çalıştığı karta yazılır) · sormaz söyler (sırayı ve günün tek işini FounderOS verir).
