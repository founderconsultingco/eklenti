---
user-invocable: false
name: aylik-raporu-hazirla
description: "Ayda bir, artı sekizinci ve on dördüncü günün ara raporu. Müşteriye giden rapor ve kanıt hikâyesi."
---

# aylik-raporu-hazirla

## 1. Adı, rolü, pazarlamadaki karşılığı

Müşteriye gösterilen raporu üreten modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Üç hali var: sekizinci ve on dördüncü günün ara raporu, rapor günü raporu (güvencenin karşılığı olan rapor budur), ve sonraki aylık raporlar. Müşteriye sayı gösteren her şey buradan çıkar.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil. Müşteri şartını geç yerine getirdiyse [21/28] gün onun verdiği günden başlar; buradaki bütün günler onunla birlikte kayar.

Neden bu iş var: müşteri çoğunlukla kötü sonuç yüzünden değil, hiçbir şey görmediği için ayrılır. Kendini değersiz hisseder, işin yapılıp yapılmadığını bilmez. Müşterinin kafasında sessizlik, işin yapılmadığı anlamına gelir.

Buradan çıkan kural: görünmeyen işi görünür kıl. İyi sonuç üretip sessiz kalırsan müşteriyi kaybedersin; orta sonuç üretip iyi haber verirsen yıllarca kalır.

Şunlar bu modülün işi değildir:
- Ölçüm altyapısını kurmak (musteri-sistemini-kur).
- Haftalık kazanım kanıtı ve haftalık görüşme (musteriyi-karsila). Bunlar rapor değildir. Kurulum haftasında her gün tek satır tek görüntü, sonrasında haftada iki üç iş kanıtı musteriyi-karsila'dan yürür. Bu, rapor gününe kadar böyle gider. Rapor günü teslim biter: yirmi ikinci günden itibaren haftalık kanıtı ve haftalık görüşmeyi musteriyi-elde-tut devralır. Ritim aynı gün değişmez; ilk ay boyunca haftalık sürer, otuzuncu günden sonra seyreler.
- Eski müşteri gönderim sayılarını üretmek (kaybolanlari-geri-getir).
- Yorum sayısını üretmek (yorum-topla).
- Haftalık kontrol (sistemi-kontrol-et).
- İkinci ay ve sonrasını yönetmek (musteriyi-elde-tut).
- Kötü haberi vermek (zor-konusmayi-yonet).

Pazarlamadaki karşılığı: müşterinin ödediği şeyin görünür hali.

## 2. Ne zaman çalışır

- Kurulum görüşmesinde: sonuç cümlesini sesli okursun. Bu cümle sözleşmede ve onay belgesinde hazır durur, doldurulacak bir yeri yoktur.
- Sekizinci günün akşam bloğu: ara rapor. Üç satır, üç sayı.
- On dördüncü günün akşam bloğu: ikinci ara rapor. Aynı üç satır.
- On dokuzuncu gün: rapor hazırlanmaya başlar, eksik sayılar toplanır.
- Yirminci gün: müşteriye tek soruyu sen sorarsın. Aşağıda yazıyor.
- Rapor günü: rapor görüşmesi ve tek sayfa. Bu birinci ayın raporudur. Görüşme kurulum bloğundadır, saatini müşteri seçer; işin yanında çalışıyorsan akşam ya da hafta sonu.
- Sonraki raporlar: her aylık tahsilat gününden üç gün önce. İlk aylık rapor ikinci ayın tahsilatından üç gün önce çıkar; rapor günüyle ikinci aylık rapor arasında başka rapor gitmez. Tahsilat günü kayarsa rapor da onunla kayar.
- Görüşme sıklığı: ilk ay haftalık, sonra iki haftada bir, müşterinin doksanıncı gününden sonra ayda bir.

## 3. Ne okur

CRM'den (adayların ve müşterilerin kaydedildiği takip programı):
- randevu sayısı ve mesaj sayısı
- teslimat aşaması
- asistanın insana devir sayısı. İnsana devir, asistanın konuşmayı bırakıp işi insana bırakmasıdır.
- randevuya dönen konuşma oranı
- her randevunun geldi mi gelmedi mi işareti
- duran havuzun kayıt başına gönderim ve cevap durumu. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir.
- yorum isteği gitti mi

Bilgi dosyasından (İş Beyni'nin müşteriler bölümü; her müşteri için tuttuğun geniş dosya):
- ortalama iş bedeli
- kayıp rakamı ve birimi. Kayıp birimi, işletmecinin bir kaçan müşteriyi kendi diliyle ölçtüğü şeydir: bir boş gün, bir koltuk saati.
- [21/28] günün başlangıç tarihi
- kapsam dışı kalan parçalar ve sebepleri
- duran havuz ve yorum sayıları
- beklenti cümleleri

Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): kayıp birimi, ortalama iş bedeli aralığı, kapasite, sezon.
Hazır rapor kalıbından: tek sayfanın iskeleti ve görüşmenin sırası.

## 4. Ne sorar

Müşteriye tek soru sorar, rapordan bir gün önce: randevu yolunda "Bu randevulardan kaçı işe döndü?", teklif yolunda "Bu tekliflerden kaçı ödemeye döndü?"

Sebebi şu: sistem para görmüyor. Kim ne kadar ödedi, hangi iş kapandı, bunlar sistemin dışında. Bu sayı müşterinin ağzından gelmezse rapora yazılmaz.

Aynı soru sonraki aylarda da rapor gününden bir gün önce sorulur.

Senden aldığı iki şey: müşterinin verdiği bu sayı ve rapor görüşmesinin yapıldığı bilgisi.

## 5. Ne yapar

### Sonuç cümlesi: rakamsız, ölçülebilir, senin elinde

Güvence, müşteriye verdiğin sözdür: rapor gününde rapor, sonuç yoksa ikinci ay ücret yok. Peki "sonuç yok" ne demek? Bu tanımlanmazsa rapor günü tartışmaya döner.

Sonuç cümlesi sözleşmede ve onay belgesinde hazır durur, her müşteride aynıdır:

Cümle İş modeli bölümündeki "Güvence cümlesi"dir, iki sürümü ve "ikisi birlikte" hali oradadır; teklif yolunda ikinci sayı "sistemin takip ettiği teklif sayısı"dır. Randevu satış sayılmaz, teklif kabulü ödeme sayılmaz; rapor gerçekleşen olayı yazar. Bir parça kurulamadıysa o satır boş kalır ve sayılmaz. Yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz.

Bu cümle üç işi birden yapıyor:
1. Rakam sözü vermiyor. "Şu kadar randevu" demiyor, sıfır olmamasını istiyor. Satışta sayı sözü verilmez, bu kurala uyuyor.
2. Ölçülebilir. Üç sayı da CRM'de duruyor, tartışma açılmıyor.
3. Senin elinde. Randevuya çıkmak ve işi kapatmak müşterinin işidir; sen onun sorumluluğunu almıyorsun.

Boş kalan satır ne demek: bir parça mevzuat yüzünden ya da müşterinin kendi adımını atmaması yüzünden hiç kurulamadıysa o satır sayılmaz. Bilinen haller: cevapsız arama yönlendirmesi kurulamaması, izinlerin çıkmaması, listenin gelmemesi, listede İYS izinli numara çıkmaması, Google işletme profilinin doğrulanmamış olması, sağlık nişinde hukukçu onayının gelmemesi, kare kodun bastırılıp asılmaması.

Kartta kayıp biriminin lira karşılığı yazmayan iki niş var: emlak ofisi ve oto galeri ("sahadan dolacak"). Orada birimi kurulum görüşmesinde müşteriye sorar ve karta yazarsın.

### Ara rapor: sekizinci ve on dördüncü günün akşamı

Rapor günü raporu tek rapor değildir. Sekizinci günün ve on dördüncü günün akşam bloğunda müşteriye üç satırlık bir durum mesajı gider.

Neden gerekiyor, tek cümle: para verip iki hafta ses duymayan müşteri sistemin çalışmadığını düşünür ve rapor gününü beklemez.

Üç satırda üç sayı var, hepsi CRM'den okunur: bugüne kadar kaç kişiye ulaşıldı, kaç cevap geldi, kaç randevu yazıldı.

Sekizinci günün metni:

"[Ad], sekizinci gün özeti.
Ulaşılan kişi: [x]. Gelen cevap: [y]. Yazılan randevu: [z].
Sıradaki iş [şu]. Bir sorun görürsen yaz, bugün dönerim."

On dördüncü günün metni:

"[Ad], on dördüncü gün özeti.
Ulaşılan kişi: [x]. Gelen cevap: [y]. Yazılan randevu: [z].
Rapor günü [tarih]; o gün üç sayıyı birlikte geçeceğiz."

Üç sayıyı sen doldurmuyorsun, CRM'den geliyor. Adı, tarihi ve sıradaki işi sen yazarsın, sonra okur ve gönderirsin.

Kurallar:
- Sayı sıfırsa sıfır yazılır. Gizlenmez, yuvarlanmaz, "yakında gelir" diye süslenmez.
- Oran yazılmaz. Bu sayılar bu kadar erken oranla konuşulacak kadar birikmemiştir.
- Yorum yazılmaz, söz verilmez. Üç satır, o kadar.
- Bir parça kapsam dışı kaldıysa o satır boş kalır ve yanına tek kelime yazılır: kurulmadı.
- Mesaj senin elinden gider, kendiliğinden gitmez.
- Müşterinin şartı geç geldiği için takvim kaydıysa ara raporlar da onunla kayar; sekizinci ve on dördüncü gün, takvimin kendi sekizinci ve on dördüncü günüdür.
- Takvim yirmi sekiz güne yazıldıysa (işin yanında çalışanda böyle olur) rapor gününün akşamında üçüncü bir ara rapor gider, metni aynıdır. Sebebi aynı: müşteri iki haftadan uzun süre sayı görmeden kalmaz.

Bu mesaj haftalık iş kanıtının yerine geçmez. İş kanıtı tek satır ve tek görüntüdür, "sistem çalışıyor" der. Ara rapor sayı gösterir, "şu ana kadar şu oldu" der. İkisi ayrı iştir ve ikisi de gider.

### Rapor günü raporu: görüşme, sonra tek sayfa

Kendiliğinden gitmez. Rapor gününün raporu görüşmede anlatılır, tek sayfa arkasından gider. Bu görüşme o haftanın görüşmesinin yerine geçer; saatini on dokuzuncu gün müşteriye yazıp teyit alırsın. Görüşme kurulum bloğunda yapılır.

Görüşmenin sırası:
1. Kötü haber. Kötü olan neyse ilk sen söylersin.
2. Sayılar.
3. Hedefi yeniden koy.
4. Kazanımı kutla.
5. Sıradaki adımı göster.
6. Tek soru, görüşmenin son cümlesi: "İşinizde çözebileceğim bir sonraki en büyük baş ağrısı ne?" Cevabı tartışmazsın, satmazsın, yazarsın: müşterinin bilgi dosyasına "sıradaki baş ağrısı" satırına, tarihle. Bu satır ikinci ayın teklifidir; büyüme şartı sağlanınca musteriyi-elde-tut buradan başlar. Cevap "yok, şimdilik iyiyiz" ise onu da yazarsın ve bir ay sonra aynı soruyu bir daha sorarsın.

Birinci maddeyi atlama. Müşteri sorunu senden önce bulursa, sonucu düzeltsen bile güveni kaybedersin.

Süre: üç sayıdan en az biri sıfır değilse, yani sonuç cümlesi tuttuysa, yirmi dakika. Tutmadıysa ya da ay kötüyse kırk dakika ayır. O görüşme zor bir görüşmedir.

Tek sayfanın satırları. Kapsam dışı kalan parça varsa sebebini sayfanın en üstündeki kutuya bir kez sen yazarsın, aşağıdaki satırlarda tekrar etmezsin.

1. Ne kurduk: canlıya alınan parçalar ve tarihleri.
2. Sistem ne yaptı: karşılanan mesaj sayısı, yazılan randevu sayısı, gelen randevu sayısı. Cevapsız aramaya dönüş kurulduysa onun sayısı da burada.
3. Eski müşteriler: kaç kişiye gidildi, kaç cevap geldi, kaç randevu çıktı.
4. Yorum: kaç istek gitti, kaç yeni yorum geldi, puan ne oldu. Bu ikisi ayrı okunur, aralarında oran yazılmaz. Kare koddan gelen yorumu sistem sayamaz.
5. Sonuç cümlesi: yazılan satırlar sıfır mı değil mi, tek cümle.
6. Para satırı: müşterinin kendi söylediği sayı.
7. Ücret satırı: ilk ay kurulum ve aylık ücretin toplamı, sonraki aylarda yalnız aylık ücret. Para satırı boşsa bu satır da yazılmaz.

Yasak: sistemin yapabildiklerini anlatmak. Rapor sadece yaptıklarını gösterir. Her özelliği sayarsan müşterinin gözü kayar ve ödediği sonucu göremez.

### Hangi randevu sayılır

Yalnız CRM'de kaydı açılmış ve kaynağı sistem olarak işaretlenmiş randevular sayılır. Müşterinin kendi getirdiği iş, kapıdan giren müşteri, sistemin dışından gelen telefon sayılmaz.

Bu sınır rapora tek cümleyle yazılır. Yoksa müşteri bütün işi sistemin ürettiğini sanır, sonra bir gün fark eder ve güven gider.

### Para satırı

Cümle şu: "Sistem [21/28] günde [x] randevu yazdı. Sen bunlardan [y] tanesinin işe döndüğünü söyledin. Senin verdiğin ortalama iş bedeliyle bu [z] TL."

Kurallar:
- Ortalama iş bedeli müşterinin kendi verdiği rakamdır. Kartın aralığı yalnız kontrol içindir.
- Müşteri sayı vermezse para satırı yazılmaz. Uydurulmaz, tahmin edilmez.
- Ciro yazılır, kâr yazılmaz. Kârın ne kadar kaldığını bilmiyorsun.
- Para satırı doluysa yanına ilk ay için kurulum ve aylık ücretin toplamı yazılır, sonraki aylarda yalnız aylık ücret. Karşılaştırmayı müşteri kendisi yapar, sen yapmazsın.
- Para satırı boşsa ücret satırı da yazılmaz. Boş ciro ile görünen ücret raporu senin aleyhine çevirir. Onun yerine kayıp birimi cümlesi yazılır: "Üç randevu, üç dolan koltuk saati demek."

### Sonuç kötüyse

Kural tek: mazeret yok, sahiplen. Müşteri piyasayı, sezonu ya da talebi dinlemek istemiyor. Teknik olarak senin hatan olmasa bile senin işin gibi konuşursun.

Sorunu ilk sen söyle. Öfkelenmişse sen ondan daha öfkeli ol. O zaman sana kızamaz, çünkü sen zaten onun adına kızgınsın.

Kötü ay raporsuz geçmez. En kötü şey rapor göndermemektir. İlk hafta detaylı, sonra seyrelen, en sonunda susan bir düzen her şeyi bozar.

Sonuç cümlesi tutmadıysa üç yol var:
1. Kapsam dışı bir parça yüzünden tutmadıysa: güvenceye sayılmaz, sebebi raporun üstündeki kutuda yazılıdır. Tahsilat kart kaydından kendiliğinden çekilir, sen bir şey yapmazsın.
2. Sistem çalıştı ama yazılan satırların hepsi sıfırsa: ikinci ay ücreti alınmaz, sistem çalışmaya devam eder. Bu bir ücretsiz aydır, açık uçlu değildir. Ayın sonunda üç yol var: kapsamı daraltıp devam, normal ücretle devam, ya da sözleşmedeki yazılı bildirimle ayrılma. Bildirimin kaç gün önce yapılacağı senin sözleşmende yazar; o rakamı müşteriye oradan okursun, kendin uydurmazsın. Süresiz bedava çalışmak yok.
3. Müşteri parasını geri isterse: hiçbir teslimat yapılmadıysa kurulum ücretini iade edersin, tartışma açmazsın. Teslimat başladıysa güvence maddesi işler.

Sayı düşük diye erken karar verilmez. Talep dalgalar halinde gelir; beş gün sıfır, sonra bir günde dört tane olabilir.

### Aylık rapor

Rapor kendiliğinden hazırlanır ama kendiliğinden gitmez. Sistem taslağı çıkarır, sen bakarsın, sen gönderirsin. Müşteriye giden her mesaj senin elinden çıkar, bu rapor da öyle.

Nasıl çıkar: CRM'de hazır bir aylık rapor taslağı yok. CRM'in raporlar bölümü sabit panolardan ibaret ve senin açtığın satırlara göre kişi saymıyor; oradan hazır rapor beklersen boş ekrana bakarsın. Taslağı FounderOS çıkarır: müşterinin alt hesabındaki kayıtları okur, her satırın sayısını kendi sayar ve önüne dolmuş bir metin koyar. Sen bilgi dosyasından gelen satırları tamamlar, baştan sona okur ve müşteriye kendi elinle gönderirsin.

Yanına iki cümlelik not değil, altmış saniyelik bir sesli mesaj koyarsın. Tek başına giden bir dosya soğuk durur. Müşteri rakamı değil, biriyle konuştuğunu hissetmeyi arıyor.

Aylık raporun satırları rapor günündeki ile aynıdır, üstüne geçen ayla karşılaştırma eklenir. Karşılaştırma en az iki ay birikmeden yazılmaz.

Sezon uyarısı: düşüşü sezona bağlamak yalnız sezon rakamı karta yazılmış nişlerde geçerlidir. Klima ve kombi, düğün, fotoğraf, pilates, haşere, oto servisin lastik dönemi. Kalan nişlerde sezon mazerettir, yapılmaz.

### Sıradaki adım ve yenileme

Görüşmenin beşinci maddesi budur. Kurallar:
- Yenileme ayrı bir olay değildir. İyi haber verdiysen, kazanımı kutladıysan ve sayıları birlikte geçtiysen yenileme sıradan bir kontrol görüşmesidir.
- Her ay "yenileyelim mi" diye sorulmaz. Sorduğun her sefer müşteriyi seni yeniden yargılamaya zorlarsın; tahsilat arka planda sessiz akar.
- Üst pakete geçiş ilk raporda konuşulmaz; ilk raporda yalnız "sıradaki en büyük baş ağrısı ne" sorusu sorulur ve cevap yazılır. Geçiş en erken ikinci ay, ve ancak büyüme şartı sağlandıysa. Büyüme şartı iki maddedir: görüşmede satılan tam sistem, yani Kademe 2, sorunsuz teslim edilmiş olacak ve rapor günü raporu çıkmış olacak.
- Sistemin yapabildiği fazladan şeyleri raporda anlatma; onları üst pakete geçiş görüşmesine sakla.

### Rapordan kanıt hikâyesi

Rapor günü raporu senin ilk kanıt hikâyenin ham maddesidir. Kanıt hikâyesi, bir müşteride ne yaptığını gerçek rakamla anlatan kısa yazıdır.

Kurallar: ham, canlı ve yeni kanıt cilalıdan iyidir. Anlatmak yerine göstermek iyidir. Küçük kilometre taşı yeter; hayat değiştiren sonuç bekleme.

İstenecek an: kazanım tazeyken. Müşteri ilk randevusunu, ilk işini ya da ilk kârlı ayını gördüğü gün.

İzin: müşterinin adı, işletme adı, logosu ya da ekran görüntüsü kullanılacaksa yazılı izin alınır. Deneme fiyatıyla çalıştıysan bu izin sözleşmende zaten var; değilse izni ayrıca yazılı istersin. İzni sen istersin: rapor görüşmesinin sonunda tek cümleyle sorar, aynı gün yazılı olarak WhatsApp'tan alırsın. İzin yazısını bilgi dosyasına tarihiyle geçirirsin. İzin sonradan geri alınırsa yayındaki isim, logo ve video kaldırılır. İzin yoksa yalnız niş ve şehir yazılır.

Bir kilit daha: diş, estetik ve güzellik salonunun tıbbi işlemlerinde kanıt hikâyesi isim, logo ya da rakamla yayınlanmadan önce müşterinin hukukçusundan yazılı görüş alınır. Bu nişlerde tanıtım kuralları sert ve ceza müşteriye kesiliyor. Görüş gelmezse yalnız niş ve şehir yazılır.

Uydurulmuş rakam yok. Kanıt hikâyesinde gerçek rakam şart.

### Raporda kişisel veri

Rapor sayı gösterir, kişi göstermez. İşletmenin müşterilerinin adı, telefonu ve mesaj içeriği rapora girmez. Bu bilgileri kendi tarafına da kopyalamazsın.

Sağlık nişlerinde ek kural: rapor tedavi, işlem ya da hasta durumu bilgisi taşımaz. Yalnız randevu ve mesaj sayısı yazar.

Müşterinin hukukçusu farklı derse ona uyulur.

### Ölçümün sınırları

Az sayıda oran yanıltır. Duran havuzun kuralı burada da geçerli: iki yüz kişiye gitmeden teşhis konmaz, üç yüz kişiye gitmeden karar verilmez, altında oran değil sayı yazılır.

Gelme oranı ölçütü yüzde yetmiştir. Altındaysa sorun randevuda değil, hatırlatmadadır.

## 6. Ne söyler

Kurulum görüşmesinde: "Rapor gününde ne göreceğini şimdi söylüyorum. Raporda üç sayı olacak: gelen talep, yazılan randevu, ulaşılan eski müşteri. Kuramadığımız bir parça olursa o satır boş kalır ve sayılmaz. Yazılan satırların hepsi sıfırsa ikinci ay parayı almam. O ay bittiğinde birlikte karar veririz: ya kapsamı daraltıp devam ederiz, ya normal ücretle devam ederiz, ya da sözleşmedeki yazılı bildirimle ayrılırız. Sana şu kadar randevu getiririm demiyorum, öyle diyen yalan söylüyor."
Sekizinci gün akşamı: "Bugün üç satır gidiyor. Ulaşılan, cevap veren, randevu. Sayılar düşükse de gidiyor; müşteri kötü sayıyı kaldırır, sessizliği kaldıramaz. Parayı verip iki hafta ses duymayan adam sistemin çalışmadığını düşünür."
Yirminci gün: "Yarın rapor. Bugün senden tek bir sayı istiyorum: bu randevulardan kaçı işe döndü. Bu sayıyı ben bilemem, sistem parayı görmüyor. Söylersen rapora yazarım, söylemezsen para satırı boş kalır."
Öğrenciye, rapordan önce: "Kötü haberi ilk sen söyleyeceksin. Yirmi dakikalık görüşmenin ilk iki dakikası bu. Müşteri sorunu senden önce bulursa sonucu düzeltsen bile güveni kaybedersin."
Rapor kötüyse müşteriye: "Baştan söylüyorum, bu ay istediğimiz yerde değiliz. Sebebini biliyorum ve benim işim. Önce sayıları geçelim, sonra ne yapacağımı anlatacağım."
Rapordan sonra öğrenciye: "Rapor gitti, yanına altmış saniyelik sesli mesaj at. Tek başına giden bir dosya soğuk durur. Müşteri rakamı değil, biriyle konuştuğunu hissetmeyi arıyor."

## 7. Ne yazar

Bilgi dosyasına: ara raporların gönderildiği tarihler ve o günkü üç sayı, rapor tarihleri, raporun satırlarının değerleri, müşterinin verdiği işe dönme sayısı, sonuç cümlesinin tuttu mu tutmadı mı, kapsam dışı kutusunun içeriği, büyüme şartı sağlandı mı ve hangi tarihte sağlandı, kanıt hikâyesi izni ve tarihi.
CRM'e: rapor gönderildi mi ve tarihi, sonuç cümlesi tuttu mu, ikinci ay ücreti alındı mı.
Niş kartının Sahadan dolacak bölümüne: bu nişte [21/28] günde çıkan gerçek randevu sayısı, işe dönme sayısı, kayıp biriminin sahada nasıl söylendiği.

## 8. Yedek yol

- Müşteri işe dönme sayısını vermezse: aynı günün akşam bloğunda bir kez daha sorarsın. Sonraki aylarda da aynı. Yine vermezse para satırı ve ücret satırı boş kalır, yerine kayıp birimi cümlesi yazılır.
- Kapsam dışı parça varsa: raporun üstündeki kutuda sebebiyle yazılır, sonuç cümlesi kalan satırlardan ölçülür, güvenceye sayılmaz.
- Yazılan satırların hepsi sıfırsa: ikinci ay ücreti alınmaz, sistem çalışır, ayın sonunda kapsamı daraltma, normal ücretle devam ya da ayrılma yollarından biri seçilir.
- Müşteri hiçbir teslimat yapılmadan ayrılmak isterse: kurulum ücreti iade edilir, tartışma açılmaz.
- Rapor kendiliğinden hazırlanamıyorsa: tek sayfayı elle hazırlarsın. Rapor gitmemesi seçenek değil.
- Ara raporun üç sayısı sistemden gelmiyorsa: sayıları elle sayar, yine gönderirsin. Üç satırlık mesajın atlanması seçenek değil.
- Ara raporun üç sayısı da sıfırsa: yine gidersin, üstüne tek cümle eklersin: neyin beklendiği ve ne zaman. Sıfırı saklamak, sıfırı yazmaktan pahalıdır.
- Müşteri raporu okumuyorsa: rapor kısalır, görüşmede ekrandan gösterilir.
- Kartta kayıp birimi yoksa: kurulum görüşmesinde müşteriye sorar ve karta yazarsın.

## 9. Sıradaki adım ve işaretler

Sıradaki: ikinci ay planı (musteriyi-elde-tut), haftalık kontrol (sistemi-kontrol-et), kötü haber varsa zor-konusmayi-yonet.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Sekizinci ya da on dördüncü gün geldi, ara rapor gitmedi: akşam bloğunun ilk işi olur.
- On dokuzuncu gün geldi, raporun sayıları eksik: sabah planının ilk işi olur.
- Yirminci gün geldi, müşterinin sayısı yok: aynı gün ikinci kez sorulur.
- Normal ücretle devam edildi ve ikinci rapor da bütün satırları sıfır gösterdi: iş zor-konusmayi-yonet'e geçer.
- Müşteri iki haftadır rapora cevap vermiyor: ayrılık böyle başlar, haftalık kontrolün ilk maddesi olur.
- Kademe 2 sorunsuz teslim edildi ve rapor günü raporu çıktı: büyüme şartı açılır, kanıt hikâyesi istenir. Kanıt hikâyesi çıkınca siten, e-posta imzan, yedinci gün takibin ve Instagram profilin yeni kanıtla güncellenir.

Beş kural: boş sayfa yok (raporun satırları, görüşmenin sırası ve sonuç cümlesi hazır gelir) · sessiz bitiş yok (kötü ay da raporlanır) · onay (rapor senin elinden gider, kendiliğinden gitmez) · sahadan güncelleme (gerçek randevu sayısı ve kayıp birimi karta yazılır) · sormaz söyler (raporun sırasını FounderOS verir; müşteriye tek soru sorulur).
