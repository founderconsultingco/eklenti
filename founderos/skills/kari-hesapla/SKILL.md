---
user-invocable: false
name: kari-hesapla
description: "Ayda bir. Gelir, gider, kâr marjı, müşteri başına kâr."
---

# kari-hesapla

## 1. Adı, rolü, pazarlamadaki karşılığı

Ayda bir çalışan modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül cebine ne kaldığını hesaplar.

Neden bu iş var: sıfırdan başlayan biri cirosuna bakıp kazandığını sanıyor. "Bu ay 70.000 TL geldi" diyor ama o paranın içinde mali müşavir, Bağ-Kur, vergi, araç abonelikleri ve ödeme komisyonu var. Hepsi çıkınca kalan bambaşka bir rakam.

İkinci sebep: para geldiği ay ile paranın harcandığı ay aynı değil. Kurulum ücreti bir kere geliyor, giderler her ay gidiyor. Üçüncü ayda "iyi gidiyorum" sanan kişi aslında ilk iki ayın kurulum paralarını yemiş oluyor.

Ölçü tek ve nettir: kâr marjını altmış saniyede söyleyebiliyor musun. Söyleyemiyorsan kararlarını körü körüne veriyorsun demektir.

Şunlar bu modülün işi değildir:
- Günlük ve haftalık sayılar (rakamlari-oku ve degisiklige-karar-ver).
- Fiyatı belirlemek (fiyati-belirle). Bu modül üç ayda bir onu yeniden çalıştırır.
- Vergi beyanı ve muhasebe. Onu mali müşavirin yapar; bu modül sadece senin kendi hesabın.

Pazarlamadaki karşılığı: ciro gurur, kâr geçim.

## 2. Ne zaman çalışır

- Ayda bir, ayın son iş günü. Bir saat sürer.
- Üç ayda bir uzun hali çalışır ve fiyati-belirle'yi yeniden çalıştırır.
- Bir de acil hali var: aylık tahsilat iki kez düşmezse ay sonunu beklemez.

## 3. Ne okur

İş Beyni'nden: müşteri sayısı, her müşterinin kurulum ve aylık ücreti, aylık masraf tablosu, geçen ayın hesabı, fiyat sürümü.
CRM'den: müşteri kayıtlarındaki kurulum ücreti, aylık ücret, aylık tahsilat günü ve tahsilat durumu satırları. Bunlar ödeme kaydı değil, senin yazdığın satırlar; parayı gerçekten aldığını banka hesabından doğruluyorsun. Kaybedilen müşteri kayıp sebebi satırından çıkıyor.
Mali müşavirinden gelen rakamlar: o ayki vergi ve prim tutarları.

## 4. Ne sorar

İki soru sorar, ikisi de rakam ister:
1. Bu ay mali müşavirin sana ne kadarlık vergi ve prim söyledi.
2. Banka hesabında ay başında ne vardı, ay sonunda ne var.

Sebebi şu: sistemde hiç para verisi yok. CRM tahsilatı görüyor ama vergiyi ve senin cebindekini görmüyor. Bu iki rakamı sen vereceksin.

## 5. Ne yapar

### Gelir

O ay hesabına gerçekten geçen para yazılır. Fatura kesilen değil, geçen.

İki kalem ayrı yazılır:
- Kurulum ücretleri. Bunlar bir kerelik, tekrar etmiyor.
- Aylık ücretler. Bunlar her ay tekrar ediyor.

Bu ayrım önemli. İki müşteriden gelen paranın büyük kısmı kurulum ücretiyse gelecek ay tekrar edecek olan yalnız iki aylık ücrettir; aylık kurulumun beşte biri olduğu için ilk ayın cirosu tekrar eden gelirin birkaç katı görünür. Kurulum parasını aylık gelir sanmak en sık yapılan hata.

### Gider

Kalemler sırayla:
- Mali müşavir ücreti.
- Bağ-Kur primi.
- Vergi. Rakamı müşavirinden aldın.
- Araç abonelikleri: yapay zeka, aday listesi programı, posta kutusu, alan adı. CRM ve tarayıcı demosu ücretsiz, bu satıra yazılmıyor.
- Sesli dakika: müşterilerinin sesli asistanının konuştuğu dakikalar, CRM'in ücret ekranından okunur, müşteri başına ayrı. Sesli asistan kurulmadıysa sıfır.
- Ödeme komisyonu. Her tahsilattan kesilen yüzde.
- Varsa reklam harcaması, varsa dışarıdan aldığın yardım.

Toplam çıkarılır.

### Kâr ve marj

Gelir eksi gider, kalan kârın. Kârın bölü gelir, kâr marjın.

Burada bir tuzak var: iki tür kâr hesabı dolaşıyor. Biri sadece araç masraflarını çıkarıp "yüzde doksan sekiz kâr" gösteriyor. O rakam gerçek değil, çünkü vergi, prim ve müşavir onun içinde yok. Bu modül her zaman hepsi çıktıktan sonraki rakamı gösterir.

### Müşteri başına kâr

Kâr bölü müşteri sayısı. Bu rakam bir sonraki karar için lazım.

Bir müşteri sana ayda ne bırakıyor bilmiyorsan, kaç müşteri gerektiğini de bilemezsin ve gelir planın hayal olur.

### Üç kontrol

Her ay üç soruya bakılır:

**Bir. Aylık gelirim sabit giderimi karşılıyor mu.** Kurulum paraları hariç, sadece tekrar eden gelirle. Karşılamıyorsa iş henüz ayakta durmuyor, kurulum paralarıyla yürüyor.

**İki. Üç aylık yaşam giderim birikti mi.** Bu pazarlık konusu değil. Maaşlı işten ayrılma kararı buna bağlı ve bu rakam birikmeden o karar konuşulmuyor.

**Üç. Kâr marjım geçen aya göre ne oldu.** Düştüyse sebebi ya yeni bir gider, ya kaybedilen müşteri, ya da düşük fiyatla kapatılan yeni müşteri.

### Zam kararı

Burada dikkatli olmak lazım, çünkü iki farklı şey karıştırılıyor.

**Yeni müşterilerin fiyatı yükselir.** Kanıt hikâyen çıktıkça, üçüncü müşteriden itibaren tam fiyat, sonrasında da kartın izin verdiği yere kadar. Yeni fiyat yeni müşterilere uygulanır.

**Mevcut müşterinin aynı hizmete zammı yoktur.** Onun yerine kademe yükseltmesi var: müşteri sonuç görmeye başladıktan sonra, en erken ikinci ayda, üst kademeye geçiş konuşulur. Aldığı iş büyür, ücreti de büyür. Aynı işe daha fazla para istemek değil, daha fazla iş vermek.

Sebebi şu: aynı hizmete zam yapmak müşteride "eskiden bunu ucuza yapıyordun" sorusunu doğuruyor ve o soruya iyi bir cevap yok.

### Para nereye gider

Kâr çıkmaya başlayınca sıra şu:
1. Önce üç aylık yaşam gideri birikir. Bitene kadar başka bir şeye gitmez.
2. Sonra ödemeyi geciktirdiğin bir şey varsa o kapanır.
3. Sonra işin yükünü azaltan yere: bakım ve rapor işlerinde yardım.
4. En son reklama. Reklam, tekrar eden gelirin belli bir seviyeye gelmesinden önce açılmıyor, çünkü reklam parası biten kişi ertesi ay hiç müşteri bulamıyor.

### Üç ayda bir

Üçüncü ayın sonunda fiyati-belirle yeniden çalışır ve şu sorulur: elindeki gerçek rakamlarla fiyatın hâlâ doğru mu.

Aynı zamanda karşılaştırma rakamları güncellenir. Yurt dışından alınmış başlangıç oranlarının yerine artık senin kendi oranların geçer.

## 6. Ne söyler

Ay sonu: "Bu ay hesabına [toplam] geçti. İki müşteri: [tutar] kurulum, yani bir kerelik; [tutar] aylık, yani tekrar edecek olan. Giderin [tutar]. Cebinde kalan [tutar], kâr marjın yüzde [oran]."
Ciroya sevinirse: "[Ciro] ciro, [kâr] kâr, ama bunun [tutar]'i bir kerelik kurulum parası. Gelecek ay tekrar edecek olan [aylıkların toplamı]. Ciro gurur, kâr geçim. Bu ay konuşacağımız rakam ikincisi."
Yüksek kâr marjı görürse: "O rakam vergiyi ve primi saymıyor. Hepsi çıktıktan sonrasına bakıyoruz, öbürü kendini kandırmak."
Sabit gideri karşılamıyorsa: "Tekrar eden gelirin sabit giderini karşılamıyor. Şu an işi ayakta tutan şey kurulum paraları ve onlar tekrar etmiyor. Bu ay tek hedef: bir müşteri daha."
Maaşlı işten ayrılmak isterse: "Dört müşterin var, evet. Üç aylık yaşam giderin birikti mi? Birikmediyse bu konuşmayı gelecek ay yaparız."
Zam sorarsa: "Mevcut müşteriye aynı işe zam yapmıyoruz. En erken ikinci aydan sonra üst kademeye geçişi konuşuyoruz: aldığı iş büyür, ücreti de büyür. Yeni fiyat yeni müşterilere."
Reklam açmak isterse: "Reklam en son sırada. Önce üç aylık yaşam giderin biriksin. Reklam parası biten kişi ertesi ay hiç müşteri bulamıyor."

## 7. Ne yazar

İş Beyni'ne: ayın geliri kurulum ve aylık ayrımıyla, gider kalemleri tek tek, kâr, kâr marjı, müşteri başına kâr, üç kontrolün cevabı, banka hesabındaki değişim, karar.
Niş kartına: bu nişte gerçekleşen kurulum ve aylık rakamlar, üçüncü aydan sonra.

Aylık hesaplar üst üste durur, silinmez. Kâr marjının üç ay boyunca nereye gittiği tek tek aylardan değil, sıradan görülür.

## 8. Yedek yol

- Mali müşavirinden rakam gelmediyse: vergi satırı "ölçülemedi" yazılır ve kâr rakamı "vergi hariç" etiketiyle kaydedilir. Etiketi olmayan rakam kullanılmaz.
- Henüz müşterin yoksa: modül yine çalışır ama sadece gider tarafını gösterir. Bu ayki masrafını bilmek de bir sonuçtur.
- Ay içinde müşteri kaybettiysen: kayıp o ayın hesabına yazılır ve sebebi musteriyi-elde-tut'tan okunur.
- Tahsilat iki kez düşmediyse: ay sonu beklenmez, aynı hafta bakılır. Bu bir fiyat sorunu değil, tahsilat sorunudur.
- Şirketin henüz yoksa: müşavir ve prim satırları boş kalır, tabloda "şirket kurulmadı" yazar. Bu satırlar şirket kurulduğu ay dolar.
- Rakamlar geçen ayla karşılaştırılamıyorsa (ilk ay): karşılaştırma yapılmaz, sadece o ayın rakamı yazılır.

## 9. Sıradaki adım ve işaretler

Sıradaki: ertesi gün normal günlük döngü. Üç ayda bir fiyati-belirle.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Tekrar eden gelir sabit gideri karşılamıyor: o ayın tek hedefi bir müşteri daha olur.
- Kâr marjı iki ay üst üste düştü: sebebi aranır, haftanın kararına gider.
- Üç aylık yaşam gideri birikti: maaşlı işten ayrılma konuşması açılır, dört müşteri şartıyla birlikte.
- Kapanış oranı beklenenin üstünde: fiyat düşük demektir, fiyati-belirle yeniden çalışır.
- Üç ay doldu: fiyat gözden geçirilir ve karşılaştırma rakamları senin kendi rakamlarınla değiştirilir.
- Bir müşteri ikinci ayını doldurdu ve büyüme şartı sağlandı: kademe yükseltmesi konuşması açılır.
- Aylık tahsilat iki kez düşmedi: tahsilat sorunu olarak açılır.

Beş kural: boş sayfa yok (kalem listesi ve üç kontrol hazır gelir) · sessiz bitiş yok (ay tek rakamla ve tek kararla kapanır) · onay (hesap sana gösterilir, kayıt senin "tamam"ınla yapılır) · sahadan güncelleme (gerçekleşen rakamlar karta ve gelir planına yazılır) · sormaz söyler (hesabı ve kararı FounderOS verir; senden yalnız iki rakam ister).
