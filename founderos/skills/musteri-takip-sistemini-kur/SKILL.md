---
user-invocable: false
name: musteri-takip-sistemini-kur
description: CRM hesabı açıldığı gün (başlangıç görüşmesinden sonra), bağlantıdan hemen sonra. Öğrencinin kendi CRM bölümü: fırsat hattı, aşamalar, şablonlar, takip zinciri.
---

# musteri-takip-sistemini-kur

## 1. Adı, rolü, pazarlamadaki karşılığı

CRM hesabın açıldığı günün modülü, bağlantıdan hemen sonra. Modül, FounderOS'un belli bir işi yapan parçasıdır. Yol Haritası'nın altıncı aşamasının altyapısını kuruyoruz: takip sistemi.

Bu modül senin kendi adaylarını izlediğin düzeni tamamlıyor. CRM, adayların ve her temasın kaydedildiği takip programıdır. Aday, henüz müşterin olmayan ama olabilecek işletmedir. Temas, bir adaya bir kanaldan bir kez ulaşmandır.

Müşterinin sistemiyle karıştırma. O, müşteri kazandığında CRM'de ayrı bir bölümde kuruluyor.

Neden bu iş var: altıncı günden itibaren günde yüz temas yapacaksın. Telefon yolunda kırk beş arama, yirmi beş e-posta, on beş Instagram mesajı, on beş takip. İşin yanında çalışıyorsan günde kırk temas. Bunu kafanda tutmak mümkün değil. Tutmaya çalışan kişi iki hafta sonra kimi aradığını, kimin ne dediğini ve kime dönmesi gerektiğini bilmiyor. İkincisi: her akşam beş sayı okuyacaksın ve o sayılar ancak kayıt varsa çıkıyor. Yazılmayan temas olmamış sayılıyor.

Üçüncüsü bugünün asıl işi: aynı adaya dört ayrı kanaldan ulaşacaksın. Telefon, e-posta, Instagram, video. Kimin hangi kanalda nerede kaldığını bilmezsen ya aynı kişiye üst üste yazarsın ya da cevap vereni unutursun. İkisi de adayı kaybettiriyor.

Neden bugün: aday listesini üçüncü günde çıkaracaksın, sahaya altıncı günde çıkacaksın. Sistem listeden önce hazır olacak ki liste geldiğinde tek seferde içine girsin.

Bugün sıfırdan kurmuyorsun. Dokuz aşama, elli beş kayıt satırı ve dört akış hesabın açıldığı gün hazır geldi. Bugünkü işin doğrulamak ve tanımak.

Şunlar bu modülün işi değildir:
- Randevu takvimi, hatırlatma akışı ve ön görüşme sayfasının doldurulması (gorusmeye-getir, aynı gün).
- Aday listesinin çıkarılması (aday-listesi-cikar, üçüncü gün).
- Adayın denetlenmesi ve denetim kartının doldurulması (aday-denetimi-cikar). Bu modül o kartın CRM'deki yerini gösteriyor, kartı doldurmuyor.
- Mesaj metinleri ve hangi durumda hangi kanalın açılacağı (adaya-mesaj-yaz, dördüncü gün).

Pazarlamadaki karşılığı: aday takibi.

## 2. Ne zaman çalışır
- CRM hesabın açıldığı gün, bağlantıdan hemen sonra, üç saat. Hesap başlangıç görüşmesinde açıldığı için bu gün sabit değil; görüşmenin ertesi günüdür. O güne kadar takip işini İş Beyni'nin "Bugünün listesi" bölümü yapar: takip günü gelenler her sabah oradan okunur ve mesajları sen gönderirsin.
- İkinci kez: üçüncü günde liste geldiğinde. O gün yalnız yükleme bölümü açılır.
- Üçüncü kez: üç yüzüncü temasta ya da bir satır işe yaramadığında.

Üç saat tam zamanlıda sabah bloğunu tam dolduruyor. İşin yanında çalışıyorsan sabah bloğun bir saat, o yüzden modül bölünüyor. Bölünmenin nasıl olduğu beşinci bölümün sonunda yazılı.

## 3. Ne okur

İş Beyni'nden: çalışma düzenin, kanal yolun, gelir planındaki günlük temas hedefin, CRM bölümünün adresi.
Niş kartından: kanal ve zaman. Niş kartı, seçtiğin sektörün bütün bilgisinin durduğu dosyadır.
Kanal düzeninden: dört kanalın adı ve dört durum değeri. Aynı tanım adaya-mesaj-yaz'da da geçerli; iki yerde tek tanım var, ikisi birbirinden farklı olamaz.
Denetim düzeninden: aday-denetimi-cikar'ın ürettiği alanların listesi, yani sızıntı puanı, en güçlü bulgu, lira karşılığı ve karar verenin adı.
İkinci günden: on kayıtlık deneme dosyası. Bugünkü test yüklemesi onunla yapılıyor.

## 4. Ne sorar

Hiçbir şey sormaz.

## 5. Ne yapar

Bugün hiçbir satır kurmuyorsun. Hepsi hesabında hazır duruyor; senin işin doğrulamak, tanımak ve bir kez deneyerek çalıştığını görmek. Kurmadığın bir sistemi kullanamazsın, o yüzden bugün ekranı öğreniyorsun.

Bir şeyi baştan söyleyeyim: CRM'in ekranı İngilizce ve öyle kalacak. Türkçe seçeneği yok. Sana hiçbir zaman "İngilizce ekranı oku" demeyeceğim; hangi düğmeye basacağını, ekranda hangi yazının durduğunu ve nerede durduğunu birlikte vereceğim. Tarif ettiğim yazıyı bulamazsan ekranın görüntüsünü buraya at, hangisi olduğunu söylerim. Tarayıcının çeviri özelliğini açma, çeviri düğme adlarını değiştiriyor.

### Birinci iş, hazır geleni doğrula (20 dakika)

1. Sol menüde "Opportunities" (fırsatlar) yazan bölümü aç. "Adaylar" adında bir hat göreceksin ve içinde dokuz sütun olacak: yeni, yazdım, cevap verdi, görüşme ayarlandı, görüşme yaptım, teklif verdim, kazandım, kaybettim, sonra.
2. Sırasının bu olduğunu gör. Bu dokuzu değiştirmiyorsun; akşam okuduğun sayılar ve haftalık kararların hepsi bunlardan çıkıyor.
3. Sol menünün altındaki "Settings" (ayarlar) içinde "Custom Fields" (kayıt satırları) bölümünü aç. Ekranda on klasör duruyor, şaşırma. Beşi bizim ve Türkçe adlı: aday bilgileri, denetim, kanal durumu, görüşme, kapanış. Kalan beşi programın kendi klasörleri, İngilizce adlarıyla duruyorlar; onlara dokunmuyorsun ve hiçbir modül onları okumuyor.
4. Aynı ayarlar bölümünde "Automation" (akışlar) kısmını aç. Dört akış duruyor ve dördü de açık: yeni aday hazırlama, takip zinciri, randevu hatırlatma ve randevu onayını yakalama.
5. Bir eksik görürsen buraya yaz, düzeltirim. Sen elle eklemiyorsun; eklersen ad birebir tutmuyor ve sayım bozuluyor.

Aşamalar hakkında bilmen gereken iki şey:

**"Sonra" ne demek.** Şimdi olmayan ama altı ay sonra yeniden aranacak aday. Hem sen elle koyabiliyorsun hem de takip zinciri bittiğinde kendiliğinden düşüyor.

**Randevuya gelmemek bir aşama değil.** Aday gelmediğinde aşaması "görüşme ayarlandı"da kalıyor. Gelmediğini randevunun kendi kaydına yazıyorsun. Sebebi şu: o kişi hâlâ randevu almış bir aday, sadece o gün gelmemiş. İki denemede de gelmezse "sonra" aşamasına geçiyor.

### İkinci iş, kanal durumu düzenini öğren (25 dakika)

Bugünün en önemli işi bu. Dört kanaldan ulaşacaksın: telefon, e-posta, Instagram, video. Her kanalın kendi durumu, tarihi ve sonucu var; hepsi "kanal durumu" klasöründe duruyor.

Bir kaydı aç ve o klasöre bak. Şöyle görünüyor:

```
Aday: [kısa ad] · Sızıntı puanı: [0-5] · Aşama: [aşama]
Telefon:   [durum] · [tarih] · [sonuç]
E-posta:   [durum] · [tarih] · [sonuç]
Instagram: [durum] · [tarih] · [sonuç]
Video:     [durum] · [tarih] · [sonuç]
SIRADAKİ HAREKET: [tek kanal] · [tarih]
Kapanma sebebi: [boş ya da üç sebepten biri]
```

Dört durumun her birinin dört değeri var ve bu tanım her yerde aynı:

- **yapılmadı**: o kanaldan hiç temas edilmedi.
- **yapıldı**: temas gitti, cevap yok.
- **cevap geldi**: aday o kanaldan döndü.
- **kapandı**: o kanal bitti. Sebebi kapanma sebebi satırına yazılıyor: adres ya da numara yok, deneme hakkı doldu, aday istemedi.

Sıradaki hareket ve sıradaki tarih kanal başına değil, adayın tamamı için tek satır. Sebebini dördüncü işte anlatıyorum.

Bilmen gereken üç şey var:

**Bu satırları sahada sen doldurmuyorsun.** Telefonu kapatınca tek kelime söylüyorsun: "açmadı" ya da "randevu yarın on birde". Kanalı, tarihi, sonucu ve yeni durumu ben yazıyorum.

**Kanal durumu geçmişi tutmuyor, bugünü tutuyor.** O kanalın şu anki hâlini gösteriyor. Adayın ne dediği ayrı: her temastan sonra kayda tek satırlık bir not düşüyorum. Akşamki sayılar nottan değil, kanalın tarih satırından çıkıyor: o gün tarihi bugüne yazılan her kayıt bir temas demek. Bu yüzden tarih satırı boş kalmıyor.

**Denetimin testleri kanal durumunu değiştirmiyor.** Denetim sırasında yapılan deneme araması "arama testi sonucu" satırına, yazılı test "yazılı test sonucu" satırına yazılıyor. İkisi de denetim klasöründe ve ikisi de kanal durumuna dokunmuyor. Sebebi basit: o bir test, temas değil. Temas, adaya kendini tanıttığın andır. Kanal durumuna yazsak hiç konuşmadığın aday konuşulmuş görünür ve takip zinciri boşuna çalışır.

Hangi durumda hangi kanalın açılacağını dördüncü günde yazılan karar tablosu söylüyor. Bugün senin işin düzeni anlamak, kuralı ezberlemek değil.

### Üçüncü iş, kayıt satırlarını tanı (30 dakika)

Bizim beş klasörümüzde toplam elli beş satır duruyor. Hepsini ezberlemiyorsun; hangi klasörde ne olduğunu biliyorsun, yeter.

**Aday bilgileri:** kısa işletme adı · karar veren · semt · yorum sayısı · Instagram hesabı · nereden bulundu · en çok istenen yüz · gözlem satırı · kim bağladı · kayıt türü. İşletmenin adı, telefonu, e-postası, adresi ve web sitesi CRM'in kendi satırlarında; onlar için ayrı bir yer açılmıyor.

**Denetim:** sızıntı puanı (sıfırla beş arası) · denetim tarihi · en güçlü bulgu (tek satır, mesajın ilk cümlesi buradan okunuyor, uzun yazılmaz) · lira karşılığı · denetim kartının tamamı · reklam veriyor mu · sitesinde form var mı · yaşanmış kanca · arama testi sonucu · yazılı test sonucu.

**Kanal durumu:** ikinci işte anlattığım on yedi satır (dört kanalın durumu, tarihi ve sonucu, artı sıradaki hareket, sıradaki tarih, cevap tarihi, kapanma sebebi, olumlu cevap işareti).

**Görüşme:** ne kadar bildiği · sıcak mı soğuk mu · itiraz (kelimesi kelimesine) · kayıp rakamı ve birimi · sözlü rıza · erteleme sayısı · gelmeme sebebi.

**Kapanış:** kurulum ücreti · aylık ücret · sözleşme durumu · onay belgesi gönderildi mi · aylık tahsilat günü · kayıp sebebi · kurulum görüşmesi tarihi · ödeme saati · teslimat başlangıç tarihi · teslimat aşaması · tahsilat durumu.

Dört satır hakkında ayrıca bilgin olsun:

**"Kayıt türü" ne işe yarıyor.** İki değeri var: aday ve bağlantı. Aday, senin nişinde işletmesi olan kişi. Bağlantı, sana birini bağlayabilecek kişi; ikinci günün akşamında çıkardığın B listesi buraya giriyor. Günün listesi sadece "aday" işaretlileri getiriyor, yani bağlantılar akşamki sayıları bozmuyor.

**"Sıcak mı soğuk mu" ne zaman doluyor.** Görüşmede değil, kayıt açıldığında. Tanıdıkların ve onların bağladığı kişiler "sıcak", listeden çıkan işletmeler "soğuk".

Bu ayrım sadece etiket değil, zincirin çalışıp çalışmayacağını belirliyor. Üç adımlı takip zinciri YALNIZ SOĞUK kayıtlarda çalışıyor. Sıcak kayıtta zincir hiç açılmıyor: takibi sen yazıyorsun ve tanidiga-mesaj-yaz'ın kuralı geçerli, yani iki gün sonra tek takip, sonrası yok. Sebebi basit, sıcak çevrede ısrar ilişkiyi yıpratıyor ve o ilişki soğuk listeden değerli.

**"En güçlü bulgu" tek satır olacak.** Mesajın ilk cümlesi doğrudan oradan okunuyor. Oraya paragraf yazarsan mesaj bozuluyor. Kartın uzun hâli "denetim kartı" satırında duruyor, oradan kimse cümle almıyor.

**"Ne dedi" diye bir satır yok, çünkü notlara yazılıyor.** Onuncu işte anlatıyorum.

Denetim satırlarını sen doldurmuyorsun, denetim modülü dolduruyor. "Nereden bulundu" satırı düzen için duruyor: ilk temasta numarayı nereden bulduğunu söylüyorsun ve bunun kaydı sende kalıyor.

### Dördüncü iş, sıradaki hareket kuralı (10 dakika)

Kuralı tek cümle: **bir adayın aynı anda tek bir sıradaki hareketi ve tek bir tarihi olur.**

Neden tek:

1. İki kanal aynı gün açılırsa aday iki ayrı yerden aynı gün mesaj alıyor ve bu satış gibi değil, kovalama gibi görünüyor.
2. Bir kanaldan cevap gelince diğerlerinin işi bitiyor. Aday artık cevap konuşmasında; ona hâlâ takip mesajı gidiyorsa sistemin dinlemediği anlaşılıyor.
3. Günün listesi tek harekete göre kuruluyor. Bir adayın iki hareketi olursa o aday listede iki kere çıkıyor ve günün sayısı şişiyor.

Satır zaten tek değer alıyor, iki kanal birden seçilemiyor. Seçenekleri şunlar: ara, e-posta, Instagram, video, bekle, yok. "Bekle" adayın kendi verdiği ileri tarih için, "yok" ise iş bittiğinde konuyor.

Bir kayıt aç, sıradaki hareketi "ara" yap ve tarihine yarını yaz. Sonra geri al. Nasıl çalıştığını gördün, yeter.

### Beşinci iş, takip zincirini doğrula (15 dakika)

Cevap vermeyene tek seferde vazgeçmiyorsun. Zincir üç adımlı: üçüncü gün, yedinci gün, on dördüncü gün. Zincir hesabında kurulu ve açık; sen kurmuyorsun.

Ne yapıyor: bir kanalın durumu "yapıldı" olduğu anda başlıyor. Üçüncü, yedinci ve on dördüncü günde adayın sıradaki tarihini o güne çekiyor, yani aday o sabah kendiliğinden günün listesine düşüyor. Yirmi birinci günde sıradaki hareketi "yok" yapıyor ve adayı "sonra" aşamasına taşıyor. Kaydı silinmiyor, altı ay sonra yeniden açılıyor.

Mesajı zincir göndermiyor, sen gönderiyorsun. Zincir sadece o günü sana hatırlatıyor. Tek istisna e-posta takipleri: onların metnini sen onaylıyorsun, gönderimi CRM yapıyor.

Sebebi şu: satışların çoğu ilk temasta olmuyor, beşinci ile yedinci temas arasında oluyor. İki temasta bırakan kişi işin çoğunu görmeden bırakıyor.

Zincirin istisnası yok, herkeste aynı çalışıyor. Bu bilerek böyle: dallanan akış bozulduğunda sessizce bozuluyor, tek yollu akış bozulduğunda hemen görülüyor. Yazı yolundaki yüz işletmede video sırası ayrı yürüyor; zincir o adayları sadece listende gösteriyor, ne yapacağını video sırası söylüyor.

Doğrulaması şöyle: bir test kaydında telefon durumunu "yapıldı" yap. Akışın kayıt listesinde o adayın adı birkaç saniye içinde görünecek. Görmüyorsan buraya yaz.

### Altıncı iş, randevu durumu (10 dakika)

Randevunun durumu ayrı bir satırda değil, randevunun kendi kaydında duruyor. Beş değeri var: onaysız, onaylı, geldi, gelmedi, iptal. Ekran İngilizce, orada sırayla "New", "Confirmed", "Showed", "No Show", "Cancelled" yazıyor.

Randevu alındığı anda "onaysız" duruyor. Aday ön görüşme sayfasındaki EVET düğmesine bastığında "onaylı" oluyor. Geldi ve gelmedi işaretini sen koyuyorsun, kendiliğinden düşmüyor.

Randevu durumu ile aşama ayrı şeyler. Aday gelmese de aşaması "görüşme ayarlandı"da kalıyor.

Takvimi bugün gorusmeye-getir'de açtın, ayarları da o gün yapıldı.

### Yedinci iş, günün listesi ve akşam sayıları (15 dakika)

Bu ikisini CRM'de aramıyorsun, çünkü CRM'de böyle bir ekran yok. İkisi de benden geliyor.

Sabah "gün" yazıyorsun. O gün temas edeceğin adayları sırayla veriyorum: önce cevap verenler, sonra takip günü bugüne düşenler, sonra denetimi hazır ve sızıntı puanı yüksek adaylar, en sonda denetimsizler. Aynı puandakileri yorum sayısı ayırıyor, çok yorum çok iş demek. Kaç kayıt geleceğini çalışma düzenin belirliyor; ekranda gördüğün sayı o gün bitirilecek sayı.

Akşam "akşam" yazıyorsun. Beş sayıyı veriyorum: kaç temas (kanal ayrımıyla), kaç cevap, kaç olumlu cevap, kaç randevu, kaç görüşme ve kapanış. Sayıları CRM kayıtlarından ben çıkarıyorum.

Sen kimi arayacağına karar vermiyorsun, sıralama yapmıyorsun, sayı toplamıyorsun. Kimi önce arayacağını düşünmek günde yirmi dakika yiyor ve o yirmi dakika beş arama demek.

Oranlara bugün bakmıyorsun. Her oranın kendi eşiği var: iki yüz temasta cevap oranına ilk teşhis için bakılıyor, üç yüz temasta karar veriliyor, gelme oranı otuz randevu birikmeden okunmuyor, kapanış oranı otuz görüşme birikmeden okunmuyor. Tek istisna haftalık zayıf halka bakışı; o ilk haftadan itibaren çalışıyor ve sayıya bakıyor, orana değil.

### Sekizinci iş, test yüklemesi (30 dakika)

İkinci günde on kayıtlık bir deneme yapmıştın. O Excel dosyasını şimdi kullanıyorsun.

1. Dosyayı aç, sütun başlıklarına bak: işletme adı, adres, telefon, web sitesi, puan, yorum sayısı, kategori, çalışma saatleri.
2. CRM'de kişiler bölümünü aç, sağ üstteki "Import" (yükleme) düğmesine bas, dosyayı seç.
3. Eşleme ekranı geliyor. Dosyanın hangi sütunu CRM'in hangi satırına gidecek, tek tek işaretliyorsun: işletme adı, telefon, web sitesi, adres, yorum sayısı, semt.
4. Kayıt türü satırına "aday" yaz. Yükleme ekranı bütün kayıtlara aynı değeri verebiliyor, tek tek yazmıyorsun.
5. Yükle. 10 kayıt düşüyor.
6. Bir kaydı aç ve üç şeye bak: dört kanal durumunun dördü de "yapılmadı" mı, sıradaki hareket satırı boş mu, kayıt türü "aday" mı. Dört kanalı "yeni aday hazırlama" akışı dolduruyor, birkaç saniye sürebiliyor; hemen bakma, sayfayı bir kez yenile.
7. Bir kaydı aday hattına ekle, aşaması "yeni" gelsin. Sonra elle "yazdım" yap ve ekranın o kaydı taşıdığını gör.
8. Aynı dosyayı ikinci kez yükle. CRM aynı kişiyi gördüğünde yeni kayıt açmıyor, mevcut kaydı güncelliyor. 10 kayıt 10 kalmalı. 20 olduysa eşlemeyi yanlış yapmışsın, geri al ve tekrarla.
9. Test kayıtlarını sil. Yarın gerçek liste gelecek.

Bu adımlar üçüncü günün beş yüz kişilik yüklemesini garantiye alıyor. Aynı adayın iki kere girmemesi önemli, çünkü ikinci ayda listeyi yenilediğinde aynı işletmeler tekrar çıkıyor ve arka arkaya aranan numara seni engelliyor.

### Dokuzuncu iş, not kuralı (5 dakika)

Her temastan sonra tek satır yazıyorsun: aday ne dedi. Uzun not yazma, yorum yazma, "iyi geçti" yazma. Adayın kendi kelimelerini yaz.

İki sebebi var. İki hafta sonra ona döndüğünde o cümleyi kullanıyorsun ve seni hatırlıyor. İkincisi, son on görüşmenin en az beşinde aynı itiraz çıkarsa teklifin kelimeleri ona göre değişiyor; bu sayımı ancak yazdıysan yapabiliyorsun.

Notu kayda ben yazıyorum, sen söylüyorsun. Arama biter bitmez, on saniye sürüyor. Akşama bıraktığın notu yazmıyorsun.

Adayın söylediği cümle nota gidiyor, itirazı ise ayrıca "itiraz" satırına yazılıyor. İkisi karışırsa on görüşme sonunda hangi itirazın kaç kere çıktığını sayamıyorsun.

### Onuncu iş, takvim linkini özel değerlere yaz (10 dakika)

Ayarlarda "özel değerler" ekranı var. İkinci günde dördünü doldurmuştun: adın, şehrin, telefonun, e-postan. Bugün bir satır daha doluyor.

Takvimin linki bugün belli oldu; o linki "takvim linki" satırına yapıştırıyorsun. Bütün randevu mesajları ve e-posta takipleri o satırdan okuyor. Yanlış yazılan tek satır bütün mesajları bozuyor, o yüzden yapıştırdıktan sonra linke bir kez kendin tıkla.

### Süre ve bölünme

Toplam üç saat: 20 + 25 + 30 + 10 + 15 + 10 + 15 + 30 + 5 + 10 dakika.

**Tam zamanlıysan** sabah bloğu üç saat ve modül tam oturuyor, ama boşluk yok. Blok dolar da bir iş kalırsa kalan iş test yüklemesidir; o üçüncü günün sabah bloğunun ilk yarım saatine kayıyor. Kanal durumu düzeni ve sıradaki hareket kuralı hiçbir koşulda kaymıyor; onları bilmeden sahada ne olduğunu anlamıyorsun.

**İşin yanında çalışıyorsan** sabah bloğun bir saat, modül ikiye bölünüyor:
- İkinci gün sabah bloğu, bir saat: birinci, ikinci ve dördüncü iş. Yani doğrulama, kanal durumu düzeni ve sıradaki hareket kuralı.
- İkinci gün akşam bloğu, bir saat: üçüncü, beşinci ve altıncı iş. Yani kayıt satırları, takip zinciri ve randevu durumu.
- Üçüncü gün sabah bloğu, bir saat: günün listesi, test yüklemesi, not kuralı, takvim linki.

Üçüncü güne kayan işlerin hepsi liste yüklenmeden önce bitmiş oluyor. Liste geldiğinde sistem hazır.

## 6. Ne söyler

Açılışta: "Bugün sabah bloğunda kendi adaylarını izleyeceğin düzeni öğreniyoruz. Sistem hazır kurulu geliyor; senin işin tanımak ve bir kez çalıştırmak. Liste yarın geliyor."
Aşamaları değiştirmek isterse: "Dokuzu da yerinde kalıyor. Akşam okuduğun beş sayı ve haftalık kararların hepsi bunlardan çıkıyor; birini çıkarırsan bir sayıyı kaybediyorsun."
Kanal satırlarını fazla bulursa: "Dört kanaldan ulaşacaksın ve aynı adaya iki kere yazarsan aday gidiyor. Dört satır, her birinde tek kelime. Sen yazmıyorsun zaten, ben yazıyorum; sen sadece 'açmadı' diyorsun."
İki hareket birden açmak isterse: "Bir adayın tek sıradaki hareketi olur. Bugün hem arayıp hem yazarsan kovalamış oluyorsun, cevap oranı düşüyor. Sıradaki hareket telefon, tarihi perşembe. Başka bir şey açmıyoruz."
Ekranın İngilizce olmasına takılırsa: "Ekran İngilizce ve öyle kalacak, Türkçesi yok. Sen İngilizce okumuyorsun, ben hangi düğme nerede duruyor söylüyorum. Bulamadığın yerde ekranın görüntüsünü at."
Satır eklemek isterse: "Elle satır ekleme. Adı birebir tutmazsa o satırı hiçbir modül bulamıyor ve sayım bozuluyor. Ne lazımsa söyle, ben ekliyorum."
Not almayı atlamak isterse: "Arama biter bitmez tek satır, adayın kendi cümlesi. Akşama bırakırsan yazmıyorsun, yazmadığın temas olmamış sayılıyor."
İki temasta vazgeçmek isterse: "Satışların çoğu beşinci ile yedinci temas arasında oluyor. Zincir üç adımlı ve o günü sana kendiliğinden hatırlatıyor."
Satır sayısını fazla bulursa: "Her satırı bir modül okuyor. Gözlem satırını mesajın yazıyor, itiraz satırını haftanın kararı sayıyor, en güçlü bulguyu mesajın ilk cümlesi okuyor, arama testi sonucunu görüşmedeki kanıtın kullanıyor. Boş duran satır yok."
Sabah listesini kendi sıralamak isterse: "Sıralamayı sen yapmıyorsun. 'Gün' yazıyorsun, en üstten başlıyorsun. Kimi önce arayacağını düşünmek günde yirmi dakika yiyor ve o yirmi dakika beş arama demek."
Günün listesini CRM'de arıyorsa: "O listeyi CRM'de arama, orada yok. Sıralamayı ben kuruyorum çünkü dört kademeli sıralama CRM'in liste ekranından çıkmıyor. Sen 'gün' yazıyorsun, liste geliyor."
Oran sorarsa: "Bugün oran yok. Cevap oranına iki yüz temasta bakıyoruz, karar üç yüzde. Gelme oranı otuz randevuda, kapanış oranı otuz görüşmede."
Bitince: "Sistem hazır. Sırada paranın yolu: ödeme linki ve evrak listesi."

## 7. Ne yazar

İş Beyni'ne: dokuz aşamanın doğrulandığı, beş klasörün ve elli beş satırın görüldüğü, dört akışın açık olduğunun doğrulandığı, takip zincirinin günleri, takip zincirinin canlı denendiği ve sonucu, test yüklemesinin tarihi ve sonucu, aynı kaydın birleştiğinin doğrulandığı, takvim linkinin özel değerlere yazıldığı.

Bir sonraki modüllere: randevu durumu ve erteleme sayısı gorusmeye-getir'e (aynı gün, bu modülden sonra), yükleme adımları aday-listesi-cikar'a, denetim satırları aday-denetimi-cikar'a, dört kanal durum satırı ve sıradaki hareket satırı adaya-mesaj-yaz ile video-mesaj-cek'e, günün listesinin sırası gunu-planla'ya, akşamki beş sayı rakamlari-oku'ya, takip günü gelenler ve gelmedi işaretliler gunu-planla'ya, itiraz satırı gorusmeyi-analiz-et'e ve teklifin on görüşmelik kontrolüne, gözlem ve kanca satırları adaya-mesaj-yaz'a.

Bu modülün tanıttığı ama doldurmadığı satırlar da var: sızıntı puanını, en güçlü bulguyu, lira karşılığını, karar verenin adını ve denetim kartının tamamını aday-denetimi-cikar yazıyor; arama testi ve yazılı test sonucunu kanitini-hazirla üretiyor ve dördüncü günde yazıyor. Bu modül yalnızca yerlerini gösteriyor.

## 8. Yedek yol

- CRM henüz açılmadıysa: bu modül çalışmaz ve beklemez. Takip zinciri elle yürür, günleri İş Beyni'ne yazılır, sen gönderirsin. Zincirin günleri aynıdır; değişen tek şey mesajı kimin gönderdiği.
- Bir ekranı bulamazsan: ekranın görüntüsünü buraya at, hangi düğme olduğunu söylerim. Tarayıcı çevirisini açma.
- Dokuz aşama ya da bir klasör eksik geliyorsa: kurulum sırasında bir şey aksamış demektir. Sen elle eklemiyorsun, buraya yazıyorsun, aynı gün düzeltiliyor.
- Takip zinciri test kaydında görünmüyorsa: akış kapalı kalmış olabilir. Buraya yaz, bakıyorum. Zincir çalışmasa da gün durmuyor; takip günlerini o hafta ben hatırlatıyorum.
- Yükleme ekranı bulunamazsa ya da eşleme tutmazsa: üçüncü güne kadar vaktin var. O gün elle giriş yolu devreye giriyor ve ilk yüz aday elle yazılıyor.
- Aynı kayıt ikinci kez yeni kayıt açıyorsa: eşleme yanlış. Liste yüklenmeden düzeltiyorsun, sonra düzeltmek zor.
- Yüklenen kayıtlarda dört kanal durumu boş geliyorsa: "yeni aday hazırlama" akışı çalışmamış demektir. Sayfayı yenile, hâlâ boşsa buraya yaz. Yüklemeyi geri almıyorsun, satırları sonradan doldurmak mümkün.
- Takvim linki hâlâ yoksa: ikinci günde gorusmeye-getir yarım kalmış demektir, önce o bitiyor. Boş linkli mesaj gönderilmiyor.

## 9. Sıradaki adım ve işaretler

Sıradaki: aynı gün, bu modülden sonra onay belgesinin ödeme linki adımı.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- İkinci gün bitti, test yüklemesi yapılmadı: üçüncü günün ilk yarım saati buna gider.
- Kanal durumu düzeni anlatılmadan gün bitti: modül ertesi sabah ilk iş olarak yeniden açılır. Bu düzeni bilmeden sahada ne olduğunu anlamıyorsun.
- Üçüncü günde yüklenen kayıt sayısı dosyadakinden az: eşleme yanlış, yükleme geri alınır ve tekrarlanır.
- Bir adayda aynı anda iki sıradaki hareket görünüyor: o gece düzeltilir; ikinci kez olursa satırın ayarı gözden geçirilir.
- Sabah listesi boş geliyor ama kayıtlar duruyor: süzme şartlarından biri yanlış, o sabah düzeltilir.
- Üç gün üst üste hiç not yazılmadı: modül ikinci kez açılır, not kuralı tekrarlanır.
- Kanal durumu "yapıldı" olmuş ama aday takip zincirine girmemiş: zincir çalışmıyor demektir, aynı gün bakılır.
- Kanal durumu satırlarının hepsi "yapılmadı"da duruyor ama notlar yazılıyor: satırlar güncellenmiyor demektir, sistem elle düzeltilir.
- Üç yüzüncü temas geçildi: oranlar ilk kez hesaplanır ve haftanın kararına gider.
- İtiraz satırı on görüşmedir boş: satır kullanılmıyor demektir, teklifin kontrolü yapılamıyor.
- Takvim linki özel değerlerde hâlâ boş: randevu mesajları gönderilmiyor, ilk iş o.

Beş kural: boş sayfa yok (aşamalar, satırlar, akışlar ve yükleme adımları hazır gelir) · sessiz bitiş yok (sabah bloğu bitmeden test yüklemesi yapılmış ve geri alınmış olur, takip zinciri bir test kaydında canlı görülür) · onay (satır listesini sen okursun, eklemek istersen söylersin, eklemeyi ben yaparım) · sahadan güncelleme (üç yüzüncü temasta satırlar, kanal durumları ve aşamalar gözden geçirilir) · sormaz söyler (aşamaları, satırları, kanal düzenini, günün listesinin sırasını ve takip zincirini FounderOS söyler).
