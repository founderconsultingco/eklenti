---
user-invocable: false
name: musteriyi-karsila
description: "İlk ödeme geldiğinde, müşterinin birinci günü. Karşılama, erişimler, müşterinin dosyası, on dört sorulu karşılama formu (müşteri yolculuğu ve tekrar aralığı dahil), rapor gününe kadarki takvim (tam zamanlıda yirmi bir, işin yanında yirmi sekiz gün)."
---

# musteriyi-karsila

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "musteriyi-karsila"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Teslimatın ilk modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül para hesaba geçtiği anda başlar. Kurulum haftası yoğundur; haftalık görüşme ve iş kanıtı ise rapor gününe, rapor gününe kadar bu modülden yürür. Üç işi var: karşılama, kurulum görüşmesi, ilk haftanın görünürlüğü.

Neden var: para ile ilk iş arasındaki sessizlik en pahalı sessizliktir. Pişmanlık çoğunlukla ilk iki günde gelir. Müşteri çoğu zaman kötü sonuç için değil, unutulduğu için gider.

Şöyle düşün: müşteri senin işini değerlendiremez, işten anlamıyor. Değerlendirdiği şey iletişimin. İki hafta sessiz kalırsan aynı işi yapmış olsan bile ilişkiyi bozarsın.

Pazarlamada tek cümle: teknolojiye dokunmadan önce karşılama yapılır.

Şunlar bu modülün işi değildir: sözleşme ve ödeme linki (onay-belgesini-hazirla), sistemin kurulması (musteri-sistemini-kur), yazılı asistanın ayarları (yazili-asistani-kur), eski müşterilere mesaj (kaybolanlari-geri-getir), aylık rapor (aylik-raporu-hazirla), bir şey ters gidince (zor-konusmayi-yonet).

## 2. Ne zaman çalışır

- Sıfırıncı gün, para hesaba geçtiği an. Altı iş:
  1. Onay belgesi hazır gelir; en geç bir saat içinde sen gönderirsin. Para gece ya da hafta sonu geçtiyse ertesi günün sabah bloğunda ilk iş.
  2. Karşılama formunu doldurmadıysa hatırlatırsın.
  3. Kurulum görüşmesinin saatini teyit edersin.
  4. İzin adımlarını gösteren kısa ekran videosunu gönderirsin.
  5. Bu müşteri bir tanıdığının bağlaması üzerinden geldiyse o kişiye tek satır yazarsın: "Bağladığın işletmeyle anlaştık, teşekkürler." Bir daha kimseyi bağlaması bu satıra bakıyor.
  6. Müşterinin CRM bölümünü istersin: destek@founderos.so adresine müşterinin adını ve sektörünü yazarsın. Satırı FounderOS aynı mesajda hazır verir, öğrenci yalnız gönderir: işletmenin adı ve sektörü, CRM bölümü isteği, kurulum görüşmesinin günü ve 0850 numara başvurusunun nasıl yapılacağı sorusu (başvuru kurulum görüşmesi günü başlıyor; yolu görüşmeden önce elde olur). İş Beyni'nin yedinci bölümünde öğrencinin kendi CRM bölümü henüz yoksa ("CRM açılmadı") satıra "Kendi CRM hesabım da henüz açılmadı." eklenir; birinci dalga ikisi açılmadan kurulamaz. İsteğin tarihi müşterinin bilgi dosyasına yazılır. Ekip bölümü açtığı gün CRM bağlantısı iki bölüme yenilenir (aşağıda, "Müşteri bölümü açıldığı gün").
- Birinci gün, en geç ikinci gün: kurulum görüşmesi. Bir saat, görüntülü, ekran paylaşımlı. Kurulum bloğunda yapılır, yani müşterinin uygun olduğu saatte.
- İkinci günden itibaren: kurulum musteri-sistemini-kur'a geçer; bu modül ilk haftanın görünürlüğünü yürütür.
- Üçüncü gün: duran havuz listesi istenir. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir.
- Yedinci gün: karşılama formu ve duran havuz onayı elinde olur. Gelmezse [21/28] gün, onun verdiği günden başlar.
- İlk ay: haftada bir görüşme.

## 3. Ne okur

CRM'den (adayların ve müşterilerin kaydedildiği takip programı): karşılama formuna gelen cevaplar, kapanan adayın kaydı, işletme adı, karar vericinin adı, telefon, e-posta, ödeme saati ve tutarı, sözleşme durumu, kurulum görüşmesi tarihi, kayıp rakamı ve birimi, görüşmede söylediği itiraz.

İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı dosya): sistemin adı, Kademe 2'nin (görüşmede satılan tam sistem) bu nişteki içeriği, güvence ve şartı, kurulum ve aylık rakam, teslimatın bu nişe uyarlanmış [21/28] günlük takvimi.

Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa) iki şey okur. Birincisi işin bilgisi:
- telefonu kim açıyor,
- karar verici kim,
- listenin işletmede nerede durduğu (çoğu kartta bu satır boştur, sahadan dolar).
İkincisi bu nişin sınırları. Bunlar FounderOS'un başvurusudur; öğrenciye kural anlatılmaz, öğrenci yalnız sonucu duyar (hangi parça kuruluyor, hangisi şimdilik açılmıyor):
- emlakta izin kaydı olmayan numaraya kampanya mesajı gitmez;
- sigortada özel bilgiler için kişinin ayrıca verdiği izin gerekir; yenileme hatırlatmasının satış mesajı sayılıp sayılmadığı belirsiz;
- sağlıkta mesaj tanıtım değil hizmet devamlılığı olmalı, ama sınırı sahadan doğrulanacak;
- diş ve estetikte tanıtım yasağı var;
- haşerede muhatap mesul müdürdür.

## 4. Ne sorar

Sormaz. Görüşmenin gündemi, izin listesi ve mesajlar hazır gelir. Senden aldığı üç şey: görüşmeyi yaptığın, hangi izinlerin alındığı, listenin geldiği.

## 5. Ne yapar

### Sıfırıncı gün: karşılama

Para hesaba geçer geçmez, arada ölü zaman bırakmadan yukarıdaki altı iş yapılır.

Karşılama formu on dört sorudur. Ayrımı karıştırma: müşterinin yedinci güne kadar vermesi gereken şey karşılama formudur, güvencenin şartı odur. Bilgi dosyası ise senin tuttuğun geniş dosyadır; formu, görüşme notlarını ve izinleri içerir. Her müşterinin ayrı dosyası olur ve klasörde müşteriler klasöründe durur (`musteriler/<musteri-adi>.md`); para geldiği gün FounderOS açar.

Sorular:
1. Ad, soyad, işletme adı, telefon, e-posta; işletmenizin vergi numarası (varsa MERSİS numarası).
2. Talep ve randevu bildirimleri başka bir numaraya ya da e-postaya gidecekse onu yazın.
3. Çalışma saatleri ve randevu almak istediği saatler.
4. Hizmet bölgesi: hangi semtler, kaç kilometre.
5. Ortalama iş bedeli ve almak istediği iş tipi.
6. Telefonu kim açıyor, siz yokken kim bakıyor.
7. Gelen talepleri kim arayacak: adı ve telefonu.
8. Eski müşteri listesi nerede duruyor: telefon rehberi, WhatsApp, randevu defteri, muhasebe programı, Excel. Eski müşterilerinize toplu mesaj gönderme izni kaydınız (İYS) var mı? Bilmiyorsanız muhasebeciniz bilir.
9. Google işletme profili, Instagram ve Facebook sayfası kimin hesabında; bir ajansta mı.
10. Neden benimle çalışmaya karar verdiniz.
11. Karar vermeden önce en büyük tereddüdünüz neydi.
12. Logo, iş fotoğrafları, varsa tanıtım metinleri.
13. Satışınız nasıl kapanıyor: randevuyla mı, fiyat teklifiyle mi, ikisiyle mi? Teklifle kapanıyorsa teklifi kim hazırlıyor, kaç günde çıkıyor, hangi belgeyle gidiyor?
14. Hizmetin tekrar aralığı var mı (bakım, kontrol, yenileme; kaç ayda bir) ve müşteriye sunmak istediğiniz ek hizmetler neler?

Onuncu ve on birinci soru bilgi toplamaz. Müşteriye kendi kararını kendi eliyle yazdırır; pişmanlığı düşüren en ucuz şey budur. Bir de rapor gününün kanıt hikâyesine malzeme olur.

Sekizinci sorunun ikinci cümlesini öğrenci açıklamaz; müşteri sorarsa: "Muhasebeciniz bilir; kaydınız varsa listeyi ona göre ayırıyoruz." FounderOS cevaba göre eski liste parçasını kurar. Cevap "yok" ise ya da listede izinli numara çıkmazsa parça şimdilik açılmaz, kurulamayan parça kuralı işler ve öğrenci yalnız şunu duyar: "Bu parça bu müşteride şimdilik açılmıyor; ücreti ona göre ayarladım." Cevap hiç gelmezse bu müşterinin kendi adımıdır, yedinci güne kadar hatırlatılır. Birinci sorudaki numara mesajların altındaki tanıtıcı satıra girer; öğrenciye ayrıca anlatılmaz.

### Müşteri bölümü açıldığı gün: bağlantıyı yenile

Ekip müşterinin bölümünü açtığını yazdığı gün, aynı oturumda FounderOS CRM bağlantısını yeniler. Ekranda giriş penceresi açılır; kendi kullanıcı adın ve şifrenle girersin. Hangi bölümlere erişileceği sorulunca iki bölümü de işaretlersin: kendi bölümün ve müşterinin bölümü. İkinci müşteride kendi bölümün ve bütün müşteri bölümlerin birlikte işaretlenir.

Neden atlanmaz: bağlantı yalnız işaretlenen bölümü görür. Müşterinin bölümü işaretlenmezse rapor ve haftalık kontrol bağlantıdan okunamaz; sayıları ekrandan tek tek sen sayarsın ve rapor gecikir.

Pencere açılmadan FounderOS tek cümle söyler: "Müşterinin bölümü açıldı, CRM bağlantısını yeniliyorum. Giriş penceresi açılacak; girdikten sonra hangi bölümlere erişeceğim sorulacak, orada hem kendi bölümünü hem [müşteri adı] bölümünü işaretle ve onayla."

### Birinci gün: kurulum görüşmesi

Bir saat, görüntülü, ekran paylaşımlı, ödemeden en geç iki gün sonra. Kurulum bloğunda yapılır: saatini müşteri seçer. Katılacaklar: karar verici ve gelen talepleri arayacak kişi. Sağlık nişlerinde hekim ve sekreter birlikte katılır.

İşin yanında çalışıyorsan kurulum bloğu senin için akşam ya da hafta sonu demektir. Bunu müşteriye gizlemezsin, tam tersine bu görüşmede en baştan söylersin. Cümle şu: "Görüşmelerimizi akşam ya da cumartesi yapacağız, gündüz ulaşamayabilirim. Mesajına aynı gün dönerim." Sonradan söylenen bu cümle mazeret gibi durur, baştan söylenen cümle düzen gibi durur.

Ön koşullar: alt hesap açılmış olur (müşteri için CRM'de açılan ayrı bölüm; sıfırıncı gün destek@founderos.so adresine müşterinin adını ve sektörünü yazarsın, FounderOS ekibi aynı gün açar; müşteri bölümünün aylık bedelini ekip açılış gününde sana yazılı söyler, kâr hesabına o gün girer), CRM bağlantısı iki bölüme yenilenmiş olur, karşılama formu dolmuş olur, sözleşme imzalanmış olur.

Form eksikse görüşme bir buçuk saat sürer. Sığmazsa izinler dışındaki maddeler ikinci görüşmeye kalır; izinler her hâlükârda bugün alınır.

Görüşme kaydedilir. Kayıt iznini görüşmedeki herkesten tek tek alırsın ve kaydın başında tekrar edersin: "Görüşmeyi kaydediyorum, notlarımı çıkarmak için; uygun mu?" Herkesin cevabını CRM'e yazarsın.

Gündem dokuz madde, bu sırayla:
1. Neden buradayız: kayıp rakamını geri okursun, [21/28] günün takvimini ekranda gösterirsin.
2. Güvence ve şartını sesli söylersin: rapor gününde rapor; giriş izinleri bu görüşmede, karşılama formu ve duran havuz onayı yedinci güne kadar. Geç verirse [21/28] gün onun verdiği günden başlar. Kurulamayan parçayı da burada söylersin; hazır cümle şu: "Eski müşteri listenizden yalnız mesaj izni kayıtlı numaralara yazıyoruz; izinli numara çıkmazsa o parça şimdilik açılmaz. Kurulamayan bir parça rapordaki sayıma girmez. Sebep bizim elimizde değilse parça kurulana kadar her ay aylık ücret yüzde yirmi iner; sizin tarafınızdaki bir adım eksik kaldığı için kurulamazsa ücret inmez." Açıklama eklemezsin; cümle bu kadar. Sonuç cümlesini de burada sesli okursun: İş Beyni'nin dördüncü bölümündeki, nişin yolculuğuna uyan güvence cümlesi (kaynağı İş modeli; ikinci sayı randevu yolunda yazılan randevu, teklif yolunda takip edilen teklif, ikisinde ikisi); kuramadığımız bir parça olursa o satır boş kalır ve sayılmaz; sistemin yazdığı randevu sıfırsa ikinci ay ücreti alınmaz. O ay bittiğinde üç yoldan biri seçilir: kapsamı daraltıp devam, normal ücretle devam, ya da sözleşmedeki yazılı bildirimle ayrılma. Bu cümle sözleşmede ve onay belgesinde hazır durur. Görüşme sığmazsa bu madde ikinci görüşmeye kalmaz, izinlerle birlikte birinci görüşmede kalır.
3. Giriş izinleri: formda cevap geldiyse teyit edilir, gelmediyse sorulur. Videoda anlattığın adımlar teyit edilir, eksik kalan ekran paylaşımıyla birlikte yapılır.
4. Duran havuz listesi: formda cevap geldiyse teyit, gelmediyse sorulur. Nasıl çıkaracağı ve üçüncü güne yetişeceği konuşulur. Bir de randevu uzunluğunu sorarsın: bir randevu kaç dakika sürüyor. Kartlarda yazmıyor, sistem takvimi ona göre kuruluyor.
5. Asistanın malzemesi: hizmet listesi (ne satıyor, hangi işleri yapıyor) ve işletmenin müşterilerinin en çok sorduğu on soru ile cevapları. Kartlarda yazmıyor, asistanın cevap listesi bunlardan kuruluyor.
6. İletişim düzeni: tek kanal, haftalık görüşme günü ve hangi pencerede yapılacağı.
7. Eksik iki cevap ve iki kalem, tek nefeste: birinci sorudaki vergi numarası ya da sekizinci sorudaki izin kaydı formda boşsa formdaki cümleyle aynen sorulur; sen açıklamazsın, cevabı yazarsın. Sonra WhatsApp'ın işletmeden mesaj başına aldığı ücretin müşterinin kendi hesabından çıktığı ve ilk ayda gönderim tavanının dört yüz on kişi olduğu; şablon onayının Meta'dan birkaç gün sürebildiği ve onay gelmeden eski müşteriye mesajın gitmeyeceği.
8. Telefon tarafı: işletmenin telefon altyapısına bakılır; uygunsa 0850 numara başvurusu müşteri adına burada başlatılır (yolu sıfırıncı günün e-postasıyla ekipten istenmişti; cevabı henüz gelmediyse görüşmede "bugün başlatıyorum" denmez, "başvuru bağlantısını bu hafta size iletiyorum" denir ve ekibin cevabı gelince aynı gün iletilir) ve hat bilgilerinin destek adresine nasıl gideceği söylenir; uygun değilse sesli karşılama kurulamayan parça olarak yazılır ve söylenir: o akış yazılı çalışır, kurulmadığı her ay ücret yüzde yirmi iner. İki sınırı da burada söylersin: ajan aramayı işletmeye canlı bağlamaz, "sizi birazdan arayacak" deyip kaydı acil işaretiyle düşürür; telefonla dış arama şimdilik açılmıyor, o iki iş yazılı yürür ve açılmadığı her ay ücret yüzde yirmi iner.
9. Beklenti: ne zaman ne olacak; ve kapsam sesli: onay belgesindeki "ne aldınız" ve "neyi yapmıyorum" başlıkları bir kez okunur, kurulum döneminde yeni parça eklenmeyeceği, isteklerin sonra listesine yazılıp rapor gününden sonra konuşulacağı söylenir.

Metin onayının sırası şudur: bu görüşmede hazır paketten çıkan şablonlar onaylanır (eski müşteri mesajları, yorum isteği, hatırlatmalar). Meta'nın onayına ikinci gün, müşterinin WhatsApp hattı CRM'e bağlandığı gün gider; onay gelene kadar akışlardaki mesajlar e-postayla çalışır. Yazılı asistanın kendi metinleri ikinci günde gönderilir, onayı üçüncü günden önce gelir.

Tek sert kural: izinleri almadan bu görüşmeden çıkma. Çıkarsan iki hafta peşinde koşarsın.

### Giriş izinleri: şifre yok, en az yetki

Kural: hesaplar müşterinin adına kalır. Şifre alınmaz, davetle giriş izni alınır. Giriş izni, müşterinin kendi hesabından seni davet ederek verdiği yetkidir. Gerekçeyi müşteriye söylersin: hesabın sahibi sensin; ben ayrılırsam hesapların, numaran, takvimin ve müşteri listen sende kalır.

Dört izin, müşterinin kendi elinden:

1. Google işletme profili. Adımlar:
   1. Müşteri işletme profilini açar.
   2. "Diğer" ve ayarlar.
   3. "Kişiler ve erişim" bölümü (ekranda aynen böyle yazar).
   4. "Ekle" der.
   5. Senin e-posta adresini yazar.
   6. Yetki olarak "yönetici" seçer.
   7. "Davet et" der.
   Sahiplik istenmez, yönetici yeter. Şart: profilin doğrulanmış olması. Doğrulanmamışsa doğrulama başlatılır, günler sürebilir; yorum toplama o kadar gecikir ve bunu müşteriye söylersin.

2. Facebook sayfası. CRM'e bağlanabilmesi için hem sayfada hem de bağlı iş portfolyosunda yönetici seviyesi gerekiyor; yarım yetki bağlantıyı açmıyor. İş portfolyosu, Facebook'un işletme sayfalarını ve reklam hesaplarını topladığı bölümdür. Şifre yine paylaşılmaz: müşteri kendi iş portfolyosundan seni davet eder. Müşteride iş portfolyosu yoksa (çoğu küçük işletmede yok) ya kısa bir ekran videosuyla kurdurursun ya ikinci bir görüşme yaparsın.

3. Instagram. Hesap işletme ya da içerik üretici hesabı olmalı; kişisel hesapsa müşteri ayarlardan çevirir. Facebook sayfası yoluyla bağlanacaksa hesabın o sayfaya bağlı olması gerekir.
4. WhatsApp ve Meta hesabı. Müşterinin WhatsApp Business hattı ikinci günde CRM'e bağlanacak; bunun için Meta hesabına ihtiyaç var. Bu görüşmede sadece kararı ve iznini alırsın, bağlantıyı musteri-sistemini-kur yapar. Müşteri normal WhatsApp kullanıyorsa WhatsApp Business uygulamasına geçeceğini şimdiden söylersin; numarası değişmez.

Telefon: mevcut numarasına dokunulmaz; telefon altyapısı uygunsa müşteri adına yeni 0850 numara alınır. Cevapsız aramanın yeni numaraya nasıl bağlanacağı musteri-sistemini-kur'un işi; burada sadece kararı ve iznini alırsın.

Alt hesapta müşteriye kısıtlı kullanıcı açılır, yönetici değil.

Bir izin alınamazsa: o kanal ilk turda kapsam dışı kalır, sebebi bilgi dosyasına yazılır, takvim kaymaz, kalanla devam edersin. İzin sonradan gelirse o kanal ikinci turda açılır.

### Duran havuz listesi

Nerede durduğu nişe göre değişir. Baskın üç yer: sahibin telefon rehberi, WhatsApp geçmişi, Instagram mesajları. Kayıtlı istisnalar: oto serviste fatura kaydı, sigortada Excel ya da ajanda, kuaförde randevu yazılımı.

Biçim: CSV dosyası. CSV, bir tablonun düz metne çevrilmiş hâlidir; Excel "farklı kaydet" derken bu biçimi verir. Tek sayfa olacak, başlıklar dolu olacak, dosya otuz megabayttan küçük olacak. Her satırda ad, telefon ya da e-postadan en az biri bulunacak. Telefonlardan boşluk ve tire temizlenir.

Liste üçüncü gün istenir, sahibin onayı yedinci güne kadar alınır: hangi isimler aranacak, hangileri elenecek. Hatırlatmayı altıncı gün yaparsın. Sekizinci günde ilk elli kişiye mesaj gideceği için listenin temizlenmesi, yüklenmesi ve onayı tek güne sığmaz.

Liste müşterinindir. Sadece onun yazılı talimatıyla kullanılır; iş biterse silinir.

İzin: eski listeye mesaj yalnız izni kayıtlı numaralara gider. Kaydın olup olmadığı karşılama formunun sekizinci sorusundan gelir; hangi numaraların izinli olduğunu müşteri kendi kaydından çıkarır ve yazılı verir, sorguyu öğrenci yapmaz. İzni olmayan numaraya mesaj gitmez; o kişiler için yalnız gelen aramaya dönüş kalır. Gönderilecek metinleri müşteri yazılı onaylar ve her mesajın altında çıkma satırı durur. Öğrenciye kural anlatılmaz, öğrenci yalnız sonucu duyar: "Bu mesaj yalnız izni olan kişilere gidiyor; listeyi ben ayırıyorum."

Kendi müşterilerini bilgilendirmek işletmenin işidir; bu konu öğrenciye açılmaz.

### İletişim düzeni

Tek kanal seçilir; müşteri hangisini kullanıyorsa o. Türkiye'de varsayılan WhatsApp. Yasak: aynı anda e-postadan, Instagram'dan ve mesajdan yazmak. Her şeyi e-postadan yürütmek de olmaz, e-postada kaybolur.

Cevap süresi sözü sıfırıncı günde onay belgesinde yazılıdır: aynı gün cevap, saatler içinde teyit. Hemen çözemeyeceğin bir şeyde bile "aldım, bakıyorum" yazarsın. Görüşmede sadece kanalı seçersin, süreyi yeniden konuşmazsın.

Görüşmenin penceresi de burada kesinleşir. Müşteriyle yaptığın her görüşme kurulum bloğundadır: kurulum görüşmesi, haftalık görüşme, rapor görüşmesi, sıfırlama ve kurtarma görüşmesi. Kurulum bloğunun saati müşterinin uygun olduğu saattir. İşin yanında çalışıyorsan bu akşam ya da hafta sonu demektir ve bunu kurulum görüşmesinde en baştan söylersin. Müşteri gündüzden başka saat kabul etmiyorsa iki yol var: ya görüşmeyi cumartesiye alırsınız, ya da takvim kayar ve kaydığını aynı gün yazılı söylersin.

Cevap yazmak görüşme değildir. Mesaja aynı gün dönersin, pencere beklemezsin. Bir şey bozulduysa haber vermek de pencere beklemez.

Gecikme olursa erken haber verirsin: şu çıktı, şununla çözüyorum, çarşamba yazacağım.

Ritim: ilk ay haftada bir görüşme, sonra iki haftada bir. Haftada iki üç iş kanıtı. O ayın en çok randevu gelen günü olursa aynı gün mesaj atarsın.

Müşteri tarafında tek muhatap belirlenir; adı ve telefonu bilgi dosyasına yazılır.

### Beklenti: ne zaman ne olacak

[21/28] günün takvimini ekranda gösterir ve üç şey söylersin:
- Sıralama: ilk günler kurulum, altıncı gün canlı, yedinci günden sonra eski müşteriler.
- Sessiz günler normaldir: canlıya kadar sonuç değil, ilerleme mesajı gelir.
- En iyi ve en kötü hâli birlikte söylersin. Yavaş giderse ne yapacağını da şimdiden söylersin.

Sayı sözü vermezsin. "İlk haftada şu kadar randevu" denmez. Kural şu: ne teslim edeceksen onu söyle, sonra söylediğini teslim et.

İşin iki taraflı olduğunu da söylersin: randevuya çıkmak ve işi kapatmak müşterinin işi.

"Bitti" tanımı yazılıdır: altıncı günde canlı, takvimin son gününde rapor. Tam zamanlıysan o gün takvimin rapor gününüdür; işin yanında çalışıyorsan takvim yirmi sekiz güne yazıldığı için o gün yirmi sekizinci günüdür. Belgelerde bu gün "rapor günü" ya da "[21/28]. gün" diye geçer. Hangisi olduğunu ekranda gösterir ve tarihini söylersin. Güvenceyi tetikleyen şey raporun kendisi değil, raporun sayılarıdır: sistemin yazdığı randevu sıfırsa ikinci ay ücreti alınmaz.

Rapor günü tek tarih olur ve bir kere söylenir. Sonra kaydırılmaz. Kayması gereken tek hal, müşterinin kendi adımını geç atmasıdır; o zaman da sebebini aynı gün yazılı söylersin.

### İlk haftanın görünürlüğü

İlk yedi gün, erken sonuçlardan daha önemli. Görünmeyen işi görünür yaparsın.

Uygulama: ikinci günden altıncı güne her gün tek satır ve tek görüntü, ekran fotoğrafı ya da kısa kayıt. Sabah bloğunda yapılır, on saniyelik iş. En yaygın hata bunu düzensiz yapmak.

İlk müşterinin bütün teslim süresinde, yani sıfırıncı günden rapor gününe kadar günlük temas hedefin düşer: tam zamanlıysan yüz yerine altmış, işin yanında çalışıyorsan kırk yerine yirmi. Sadece kurulum haftası değil, [21/28] günün tamamı. Garanti şartı bu günlerin hepsini hariç tutar.

Altıncı gün canlıya alma mesajı gider. Yedinci gün duran havuz onayı elinde olur.

Haftalık ilerleme mesajı iki dakikada yazılır: neyi bitirdik, şimdi ne var, sıradaki ne. Akşam bloğunda yazılır.

### İşin yanında çalışıyorsan: teslimin takvimi

[21/28] günlük teslimin bir kısmını FounderOS ekibi yapar: müşteri bölümünün açılması, telefon hattının bağlanması, sesli ajanın servise kurulması ve CRM'e bağlanması, çağrının kayda düşmesi. Kalanı senin payın. İlk müşteride yaklaşık kırk beş saat tutar:
- karşılama, kurulum görüşmesi ve hazırlığı: dört saat,
- birinci dalganın kurulumu (FounderOS ekran ekran gösterir, sen tıklarsın): sekiz saat,
- beşinci günün testi: beş saat,
- yazılı asistanın ve sesli ajanın metinleri, onaylar, on arama ve ikinci dalganın testi: altı saat,
- canlıdan sonraki ilk hafta konuşmaları okumak: dört saat,
- eski müşteri listesi, gönderim ve cevap verenleri elden geçirmek: yedi saat,
- yorum isteği: bir saat,
- haftalık görüşmeler, günlük tek satır ve ara raporlar: beş saat,
- haftalık kontrol, rapor hazırlığı ve rapor görüşmesi: beş saat.
Bu saatler tahmindir. İlk müşteride gerçek süreler ölçüm satırlarına yazılır, ikinci müşteride onlarla hesaplanır. Tam zamanlıysan bu saatler gündüzden çıkar ve takvim değişmez. İşin yanında çalışıyorsan akşamdan ve hafta sonundan çıkar. O yüzden bu bölüm var.

Hangi iş hangi pencereye giriyor:
- Kurulum görüşmesi ve bütün müşteri görüşmeleri: kurulum bloğu. Sende akşam ya da cumartesi.
- Sistem kurulumu, ikinci günden dördüncü güne: akşam bloğu ve saha bloğundan boşalan saat, günde yaklaşık bir buçuk saat. İlk müşteride birinci dalga bu üç akşama sığmayabilir; kalanı ilk hafta sonuna kayar.
- Beşinci günün testi: akşam bloğuna sığmaz, hafta sonuna kayar. On dört senaryo ve otuz iki tur tek oturumda bitmez.
- Altıncı gün canlıya alma: akşam bloğu. Ama müşterinin "açalım" cevabını beklediğin için kurulum bloğuna bağlı kalır.
- Eski müşteri gönderimi, sekizinci günden on ikinci güne: sabah bloğunda "tamam" dersin. Gönderimi sistem müşterinin çalışma saatleri içinde yapar, sen gün içinde eline bakmazsın.
- Cevap verenleri elden geçirme, on birinci günden on dördüncü güne: akşam bloğu.
- Haftalık kontrol: akşam bloğu ya da hafta sonu.
- Her günün tek satır tek görüntüsü: sabah bloğu, on saniye.
- Eksikler turu ve rapor hazırlığı, on beşinci günden yirminci güne: akşam bloğu, ağır kısmı hafta sonu.

Hafta sonuna kayan üç iş bunlar: beşinci günün testi, haftalık kontrol, rapor hazırlığı. Bunları hafta içi akşamına sıkıştırmaya çalışırsan yarım yaparsın.

Kaç güne uzuyor: hesap açık ve önceki sürümde iyimserdi, düzelttim. Hafta içi beş gün, her gün yaklaşık bir buçuk saat: akşam bloğundan yirmi dakika (bloğun kırk dakikası kayıt, sayım ve provaya gidiyor, o iş devredilemiyor), artı temas kırktan yirmiye indiği için saha bloğunda boşalan yaklaşık bir saat on beş dakika. Cumartesi iki saat; cumartesinin üç saatlik saha bloğunun tamamı teslimata verilmiyor, çünkü o gün de temas var. **Pazar sabahı iki saat**; pazar olmadan hafta on saat kalıyor ve teslim otuz beş güne çıkıyor, o yüzden bu iki saat müşteriye verilen yirmi sekiz günlük sözün parçası ve ilk müşteriden önce söyleniyor. Haftada on iki saat eder. Kırk beş saat bölü on iki, dört haftaya yakın. Yani teslim [21/28] günde değil, yirmi sekiz günde biter. En sıkışık hafta ilki: karşılama, birinci dalga ve beşinci günün testi birlikte on yedi saat, haftanın penceresi on iki saat. Sığmazsa canlıya alma birkaç gün kayar. Bu yüzden ilk müşteriden önce FounderOS takvimi seninle bu hesapla yazar, sen de kurulum görüşmesinde müşteriye baştan söylersin.

Bunun karşılığı şu: teslim takvimini [21/28] güne değil yirmi sekiz güne yazarsın, rapor günü o takvimin son günüdür ve güvence o günden ölçülür. Müşteriye söylenme anı bellidir: kurulum görüşmesinin birinci maddesinde, takvimi ekranda gösterirken. Gecikince değil, baştan. "[21/28] gün" deyip sonra kaydırmak, baştan yirmi sekiz demekten çok daha pahalıya patlar.

Hafta sonunu hiç kullanamıyorsan takvim daha da uzar. O zaman ilk müşteriye başlamadan önce FounderOS'a yazarsın, takvimi birlikte yeniden yazarız.

### İşin yanında çalışıyorsan: kilitler ne zaman açılır

Sistemde dört kilit var ve dördü de gün sayısıyla değil, sayıyla açılır:
- Mesaj metni: üç yüz temasta karar verilir, iki yüz temasta sadece bakılır.
- Teklifin kelimeleri: on görüşme birikecek.
- Fiyatın rakamı: otuz görüşme birikecek.
- Niş: doksan gün ya da beş müşteri. Tek istisnası üç yüz olgun temasta hiç görüşme çıkmamış olması (üç yüzüncü temasın üstünden yedi gün geçmiş olacak, çünkü üç yüzün içinde yazılı temas da var).

Şimdi senin hesabın. İşin yanında çalışan günde kırk temas yapıyor. Teslim sürecinde bu yirmiye iniyor. Yani teslim yürürken kilitlerin sayacı yarı hızda işliyor.

Mesaj metni kilidi: kırk temasla üç yüze sekiz saha gününde varırsın. Yirmi temasla on beş saha günü sürer. Teslimin ortasında yakalandıysan aradaki fark kadar uzar.

Teklifin kelimeleri ve fiyatın rakamı: bunlar temasa değil görüşmeye bağlı. Temas yarıya inince görüşme de yaklaşık yarıya iner, o yüzden on görüşme ve otuz görüşme eşikleri kabaca iki kat sürede dolar. Kaç temasta bir görüşme çıktığını kimse önceden bilemez; senin rakamın sahadan çıkacak.

Niş kilidi tek istisnadır, o gün sayısına da bağlı: doksan gün geçince ya da beş müşteri olunca açılır, temas hızından etkilenmez. Ama onun içindeki üç yüz temas istisnası yine sayıya bağlıdır ve o da uzar.

Net söyleyeyim: işin yanında çalışanda kilit gün sayısıyla değil temas sayısıyla açılır. Süre uzar ve bu normaldir. "Yirminci günde olmam gereken yerde değilim" diye kendini dövme; sayaç senin yaptığın temasa bakıyor, takvime değil. Kilidi erken açtırmak diye bir şey yok.

## 6. Ne söyler

Para gelince: "Para geldi. Şimdi sessizlik olmayacak. Onay belgesi hazır, sen gönder. Kurulum görüşmesi yarın, kurulum bloğunda; saatini müşteri seçti. Bugün üç işin var: formu doldurmadıysa hatırlat, izin videosunu gönder, ekibe müşterinin bölümünü iste; e-postanın satırı aşağıda hazır." Satır, sıfırıncı günün altıncı işindeki gibi aynı mesajda verilir; ertesi güne kalmaz.
İşin yanında çalışıyorsan, kurulum görüşmesinden önce: "Takvimi [21/28] güne değil yirmi sekiz güne yazdım. Sebebi basit: bu işte senin payın kırk beş saat civarı, senin elinde akşamlar ve hafta sonu var. Bunu bugün söyleyeceksin, üçüncü hafta gecikince değil. Baştan söylenen tarih düzendir, sonradan söylenen tarih mazerettir."
Kilit sayacı sorulunca: "Teslim yürürken günde kırk değil yirmi temas yapıyorsun, sayaç yarı hızda işliyor. Üç yüz temas gün sayısıyla değil, senin yaptığın temasla doluyor. Süre uzar, bu normaldir. Sen sayıyı büyüt, kilidi ben açarım."
Görüşmeden önce: "Bir saat, dokuz madde. En önemlisi üçüncüsü: izinler. İzinleri alamadan bu görüşmeden çıkma, sonra iki hafta peşinde koşarsın."
Görüşmede izin isterken: "Şifrenizi istemiyorum. Kendi hesabınızdan beni yönetici olarak davet edeceksiniz. Hesaplar sizin adınıza; ben ayrılırsam hesaplarınız, numaranız, takviminiz ve müşteri listeniz sizde kalır, ben yalnız çıkarım."

Bu cümleyi bundan fazla büyütme. "Her şey sizde kalır" deme, çünkü doğru değil: akışlar, şablonlar ve asistanın cevapları senin çalışma hesabında kurulu, onların devri yok. Müşteri sorarsa dürüst cevap şudur: "Hesaplarınız ve verileriniz sizin. Sistemin kurulduğu çalışma alanı benim; ayrılırsak listeyi dışa aktarıp size veririm, sistem benimle gider." Ayrılık anında ne olacağını sonra ayrıca konuşacağız.
Beklenti cümlesi: "İlk günler sessiz gelebilir, kurulum yapıyorum. Altıncı gün canlıya alıyoruz. Her gün ne yaptığımı göstereceğim."
İkinci gün: "Bugün müşterine tek satır ve tek görüntü gönder. On saniye sürer. Müşteri kaybetmemenin en ucuz yolu bu."

## 7. Ne yazar

Bilgi dosyasına: karşılama formunun cevapları, görüşme kaydından çıkan notlar, alınan ve alınamayan izinler, tek muhatap, iletişim kanalı ve haftalık görüşme günü, listenin nerede durduğu ve ne zaman geleceği, beklenti cümleleri, nişin sınırı yüzünden açılmayan parça ve sonucu (tek sakin satır, kaynaksız; bu dosyayı öğrenci de okur), müşteri bölümünün aylık bedeli, CRM bağlantısının iki bölüme yenilendiği tarih.
CRM'e: kurulum görüşmesi yapıldı ve tarihi, kayıt izni var mı, izin durumu, liste durumu, [21/28] günün başlangıç tarihi ve şart geç yerine getirildiyse kayan tarih, kayan aylık tahsilat günü, haftalık görüşme günü.
Niş kartının Sahadan dolacak bölümüne: listenin bu nişte gerçekte nerede durduğu, telefonu kimin açtığı, Google ve Instagram hesabının kimde olduğu. Kartta boş duran satırlar ilk müşteriden sonra dolar.
Panel dosyasına (`.founderos/panel/teslimat.json`, şeması `founderos:panel-vitrini`'de): müşterinin satırı, para hesaba geçtiği gün, karşılama mesajıyla aynı turda açılır (ertesi güne kalmaz): `ad` (işletmenin adı), `baslangic`, `rapor_gunu` (şart geç geldiyse kayan tarih), `aylik` (onay belgesindeki aylık ücret, sayı; panelin Her ay gelen kartı bundan toplar), `evre` (`karsilama`, kurulum görüşmesinden sonra `kurulum`), `bilgiler` (toplanacak on bir bilgiden gelen), `siradaki`; sonra aracın `panel --yukle` komutu sessiz çalışır. Öğrenci müşterinin gününü Bugün'deki Teslimat kartında görür.

## 8. Yedek yol

- Karşılama formu görüşmeye kadar dolmadıysa: görüşmenin ilk on beş dakikasında birlikte doldurulur, görüşme bir buçuk saate çıkar. Yedinci güne kadar hiç gelmezse [21/28] gün o günden başlar.
- Müşteri görüşmeye gelmezse: beş dakika sonra ararsın, aynı gün ikinci saat verirsin. İki denemede olmazsa [21/28] gün başlamaz, sebebi bilgi dosyasına yazılır.
- Bir izin alınamıyorsa (hesap ajansta, sahibi bilmiyor): o kanal ilk turda kapsam dışı, sebebi yazılır, kalanla devam edersin, takvim kaymaz.
- Liste telefon rehberinde, WhatsApp'ta ya da Instagram mesajlarındaysa: telefon rehberinden kişiler dışa aktarılır (kişiler uygulaması, seç, paylaş, dosya olarak). WhatsApp ve Instagram'da elle döküm alınır: üç sütun, ad, telefon, son iş tarihi. Elli kişiden çoksa önce en yeni elli kişi çıkarılır, kalanı ikinci haftaya.
- Liste kâğıt defterde, ajandada ya da fişlerde duruyorsa: iş bilgisayara geçirmektir ve bu işi müşteri yapar, sen yapmazsın. O defterde kimin telefonu var, kimin yok, hangi kayıt eski, bunu sadece o bilir. Yolu tek cümleyle verirsin: en yeni işten geriye doğru gider, üç sütun yazar (ad, telefon, son iş tarihi) ve tabloyu tek dosya olarak sana gönderir. Bilgisayar kullanmıyorsa telefonuna not uygulamasından da yazabilir, sen tabloya sen çevirirsin. Sayfayı fotoğraflayıp göndermek işe yaramaz, numaralar yanlış okunur.
  Kaç gün sürer: sen gün veremezsin, defterin kalınlığına bağlı. Kural şu: üçüncü günde istenir, yedinci güne kadar gelirse takvim kaymaz. Gelmezse [21/28] gün listenin geldiği günden başlar ve bunu müşteriye o gün yazılı söylersin. Defter kalınsa müşteriye şunu dersin: "Hepsini bekleyip durmayalım. En yeni elli kişiyi bugün çıkar, gerisini sonra ekleriz."
- Müşterinin eski müşteri listesi hiç yoksa: kimseyi zorlamazsın, uydurma liste kurmazsın. Duran havuz bölümü ilk turda kapsam dışıdır, güvencenin sonucuna sayılmaz ve raporda o satır boş kalır. Bunu aynı gün yazılı söylersin, sebebiyle birlikte. Bu, kurulum görüşmesinde güvencenin şartını söylerken zaten anlattığın halin aynısıdır. Karşılığında iki şey yaparsın: kalan parçaları tam kurarsın, ve müşterinin bundan sonra gelen her işini sisteme kaydettirirsin ki ikinci turda listesi olsun.
- Müşteri "şifremi vereyim" derse: alınmaz, davet yolu tekrar gösterilir.
- Kayıt izni verilmezse: notları görüşme biter bitmez beş dakikada yazarsın.
- Karar verici görüşmede yoksa: görüşme yapılmaz, ertelenir. Kurulum onun onayı olmadan başlamaz.

## 9. Sıradaki adım ve işaretler

Sıradaki: ikinci günden itibaren musteri-sistemini-kur. Yedinci günde kaybolanlari-geri-getir için liste hazır olur.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- İki gün geçti, kurulum görüşmesi yapılmadı: sabah planının ilk işi olur.
- Müşterinin bölümü açıldı, bağlantı iki bölüme yenilenmedi: aynı oturumda yenilenir; o gün olmadıysa ertesi sabahın ilk işi olur.
- İzinlerden biri eksik ve üç gün geçti: o kanal kapsam dışı, müşteriye yazılı bildirilir.
- Yedinci gün geldi, liste yok: [21/28] gün kayar, müşteriye tek cümleyle bildirilir.
- Müşteride hiç eski müşteri listesi yok: duran havuz bölümü ilk turda kapsam dışına alınır, aynı gün yazılı bildirilir, güvencenin sonucuna sayılmaz.
- İşin yanında çalışıyorsun ve ilk müşteri kapandı: teslim takvimi yirmi sekiz güne yazılır, günlük temas hedefi [21/28] gün boyunca kırktan yirmiye iner, kilit sayaçları yarı hızda işler.
- İki gün üst üste görünür iş yok: sabah planına eklenir.
- Müşteri iki mesaja cevap vermedi: haftalık görüşmede konuşulur, zor-konusmayi-yonet'e not gider.
- İlk müşterinin kurulum görüşmesi bitti: niş kartının boş satırları güncellenir.

Beş kural: boş sayfa yok (form, gündem, izin listesi ve mesajlar hazır gelir) · sessiz bitiş yok (her gün ne yapıldığı müşteriye ve bilgi dosyasına yazılır) · onay (bütün mesajlar senin elinden gider) · sahadan güncelleme (listenin yeri, hesapların kimde olduğu ve yasal sınır karta yazılır) · sormaz söyler (gündemi ve sırayı FounderOS verir).
