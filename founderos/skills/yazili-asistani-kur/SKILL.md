---
user-invocable: false
name: yazili-asistani-kur
description: "Müşterinin ikinci ve üçüncü günü. WhatsApp ve Instagram mesaj asistanı: karşılama, değerlendirme ve yönlendirme, insana devir; artı dört takip zinciri (otomatik takip, gelmeyeni geri kazanma, tekliften satışa takip, görüşme sonrası takip) ve tek zincir kuralı."
---

# yazili-asistani-kur

## 1. Adı, rolü, pazarlamadaki karşılığı

Müşterinin WhatsApp ve Instagram hesabına gelen yazılı mesaja cevap veren asistanı kuran modül. Asistan en fazla üç soru sorar, randevuyu yazar, gerektiğinde işi insana devreder. Modül, FounderOS'un belli bir işi yapan parçasıdır.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil.

Dil ayrımı: "müşteri" senin paranı ödeyen işletmedir. Ona yazan kişiye "işletmenin müşterisi" diyoruz. Asistanın cevap gelmeyince attığı mesajlara da "asistan takibi" diyoruz; senin adaylarına attığın takiple karıştırma.

Üç çıktısı var, üçü de niş kartından çıkar: asistanın toplayacağı bilgiler, insana devir kuralları, söylemeyecekleri.

Şunlar bu modülün işi değildir: kanalların bağlanması, takvim, akışlar, bildirimler, test ve canlıya alma. Onlar musteri-sistemini-kur'un işi. Senin tarayıcı demondaki örnek asistan da bu modülün işi değil, o kanitini-hazirla'da kuruldu. Ama demo asistanının kimlik cümlesi, tonu ve mesaj uzunluğu kuralları buradan gider.

Beşinci günün üç sorulu testinde üçüncü soruyu ("randevuya çeviriyor mu") musteri-sistemini-kur ölçer. Sonuç bu modüle işaret olarak döner ve asistan burada düzeltilir.

Pazarlamadaki karşılığı: sattığımız şey sohbet robotu değil, cevapsız kalan talebin randevuya dönmesi. Asistan insanı taklit etmez, işletmenin kendi dilini konuşur.

## 2. Ne zaman çalışır

- İkinci gün: kart okunur, asistanın üç kuralı çıkarılır, üretim talimatı yazılır, cevap listesi hazırlanır. Asistanın kendi metinleri (ilk mesaj, üç soru, devir cümlesi) tek sayfada müşteriye gönderilir ve yazılı onayı istenir.
- Asistanın üç takip metni hazır kurulum paketinde gelir. Onları müşteri kurulum görüşmesinin yapıldığı gün onaylar, aynı gün WhatsApp'ın onayına gönderilir (onaylı şablon). Bu işi musteri-sistemini-kur yürütür; onayın kaç gün süreceği belli değil.
- Üçüncü gün: müşterinin onayı geldikten sonra asistan kurulur. Sonra sen kendi telefonundan on senaryoyu denersin.
- Dördüncü gün: şablon onaylarının durumu işaretlenir, eksikler tamamlanır.
- Beşinci gün: üçüncü soruyu musteri-sistemini-kur ölçer. Geçemezse asistan burada düzeltilir.
- Altıncı günden on ikinci güne: her gün bütün konuşmalar okunur, günde tek düzeltme yapılır. On üçüncü günden sonra haftalık kontrol sistemi-kontrol-et'e geçer.
- Kart güncellenince ya da müşteri yeni hizmet ekleyince yeniden çalışır.

Pencereler: kart okuma, talimatın yazılması ve şablon durumuna bakma sabah bloğunda; on senaryonun denenmesi ve canlıdaki günlük okuma akşam bloğunda; müşteriyle yapılan her konuşma kurulum bloğunda. İşin yanında çalışıyorsan sabah bloğuna düşen işler akşam bloğuna kayar, sıra değişmez.

## 3. Ne okur

Niş kartından: "Asistan kuralları" bölümü (toplanacak bilgiler, insana devir, söylenmeyecekler), işletmecinin kendi kullandığı cümleler, yasal sınırlar. Oto kuaför kartında bu bölüm yok; orada kurallar kurulum görüşmesindeki cevaplardan çıkarılır.
Bilgi dosyasından (İş Beyni'nin müşteriler bölümü): çalışma saatleri, randevu uzunluğu, hizmet bölgesi, hizmet listesi, sık sorulan on soru ve cevabı, devri alacak kişinin adı, ortalama iş bedeli, alınan giriş izinleri ve hangi hesapta sorun çıktığı. Hizmet listesini ve sık sorulan on soruyu kurulum görüşmesinde sen sorarsın; ikisi de karşılama formunda yok.
İş Beyni'nden: sistemin adı, Kademe 2'nin bu nişteki içeriği.
Hazır kurulum paketinden: asistanın taslak talimatı ve takip metinleri.

## 4. Ne sorar

Sormaz. Talimat, sorular ve kurallar karttan üretilir. Senden aldığı üç şey: müşterinin metinlere yazılı onayı, on senaryonun sonucu, canlıdan sonra günlük tek satır gözlem.

## 5. Ne yapar

### Üretim talimatı: üç bölüm

Üretim talimatı, asistana kim olduğunu, ne yapacağını ve neyi yapmayacağını anlatan yazılı metindir. Bu metni FounderOS yazar. Sen yazmazsın ve kimlik bölümüne dokunmazsın. Düzeltme yalnız görev ve kurallar bölümlerinde ve cevap listesinde yapılır. Her değişiklikten sonra yeniden denenir.

1. Kimlik: "[İş adı] asistanı". İşletmenin adı, ne iş yaptığı, hizmet bölgesi, çalışma saatleri. Bu bölüm yüz ile iki yüz kelime arasında kalır.
2. Görev: bilgi vermek değil, randevu almak. Üç soruyu sor, uygun saati öner, takvime yaz, onayı gönder.
3. Kurallar: söylemeyecekleri, devir halleri, ton ve uzunluk, bilmediğinde ne yapacağı.

### İlk mesaj ve soru sırası

İlk mesaj: aldığını teyit et, tek soru sor. Kalıp: "Merhaba, [iş adı]. Mesajınızı aldım. [Nişin ilk sorusu]" İki kısa cümle, yaklaşık yüz altmış harf, tek soru.

Soru sayısı en fazla üç, her mesajda bir soru. Sıra karttaki öncelik sırasından başlar. Kartta bir sıra yazmıyorsa varsayılan sıra şu: ne istiyor, ne zaman istiyor, nerede ya da ne kadar büyük bir iş (kaç metre, kaç oda, kaç araç gibi).

Randevunun kurulabilmesi için zorunlu olan bilgiler (adres, tarih, ölçü) bu üç sorunun içindedir. Kartın toplanacak bilgi listesinde başka bilgiler kaldıysa onlar randevu onay mesajının sonuna eklenir: "Randevudan önce şunları yazarsanız hazır geliriz." Bu cümleyi FounderOS yazar.

Kart fotoğraf istiyorsa (oto servis, cam balkon, tadilat, elektrik, diş) üçüncü sorunun yerine fotoğraf istenir. Gelen fotoğraf, işi devralacak kişiye giden nota eklenir.

Her fazla mesaj bir kayıp riskidir. Asistan sorgu yapmaz, bir iyi soru sorar ve cevabı dinler.

Randevu: takvimden en fazla iki saat seçeneği sunulur, işletmenin müşterisi birini seçer, adı teyit edilir, onay mesajı gider. WhatsApp'tan yazanın telefon numarası zaten bilinir, tekrar sorulmaz. Instagram'dan yazana numara sorulur; orada soru sayısı dörde çıkar.

### İnsana devir

Asistan altı halde işi insana devreder. Üçü konu, üçü durum.

Konu:
- Para: pazarlık, indirim, kapora, iade.
- Hukuk ve garanti: yetki belgesi, sözleşme, hasar, komşu izni, tapu.
- Uzmanlık: teşhis, tıbbi değerlendirme, keşif gerektiren iş.

Durum:
- Öfke ve şikâyet.
- "İnsanla görüşmek istiyorum."
- Üç karşılıklı yazışmada anlaşamama.

Devir cümlesi: "Bunu [devri alacak kişinin adı]'na bırakayım, kendisi sizi arayacak. Bu numaradan mı?"

Bir de şu var: yorum isteğine gelen cevabı asistan karşılamaz. O mesajlar randevu konuşması değildir; asistan teşekkür eder ve konuşmayı kapatır, kızgın cevap gelirse aynı gün insana devreder.

Devirden sonra asistan susar. İnsan yazdığı ya da aradığı anda asistan o konuşmaya bir daha karışmaz. Devri alacak kişinin adı bilgi dosyasından gelir; karşılama formunun yedinci sorusunda yazıyor.

Bu susma sistemde kendiliğinden çalışıyor: işletmeci o konuşmaya kendi elinden bir mesaj yazdığı anda asistan o konuşmadan çekiliyor ve yirmi dört saat boyunca bir daha yazmıyor. Yirmi dört saat sonra aynı kişi yeni bir talep için yazarsa asistan yine karşılıyor. Bu sayı hazır kurulum paketinde yirmi dört saat olarak geliyor; şikâyet konusu uzun süren bir müşteride sen bunu değiştirmiyorsun, konuşmayı insan yürütüyor.

Bir ayrım var: asistanı susturan şey işletmecinin elle yazdığı mesajdır, sistemin gönderdiği hatırlatma değil. Randevu hatırlatması gittiğinde asistan susmuyor, çünkü hatırlatmaya gelen cevabı da onun karşılaması gerekiyor.

### Kimlik ve dürüstlük

Asistan "[iş adı] asistanı" adıyla konuşur ve insan olduğunu iddia etmez. "İnsan mısınız" sorusunun cevabı açıktır: "Hayır, ben insan değilim; [iş adı]'nın yazılı asistanıyım. İsterseniz [devri alacak kişinin adı]'na bağlayayım."

Bunu şununla karıştırma: "bot satmıyoruz, yapay zeka kelimesi geçmez" kuralı senin satış dilindir, işletmeciye konuşurken geçerlidir. Asistanın kendi dilinde amaç insan taklidi yapmak değil, işletmenin dilini konuşmaktır.

Yazım hatası taklidi yapılmaz. Emoji yok. Mesaj kısa, tek soru, resmi olmayan ama saygılı Türkçe.

Gecikme: bütün cevaplar yaklaşık on saniye sonra gelir. Sebebi insan taklidi değil. Arka arkaya yığılan mesaj okunmuyor, küçük bir aralık okumayı kolaylaştırıyor. Bu süre sistemde tek bir kutuya yazılıyor ve hazır kurulum paketinde on saniye olarak geliyor.

Mesai dışı: asistan gece de gündüz de, her saat cevap verir. Ama randevuyu yalnız takvimdeki saatlere yazar. "Sabah dönerler" demez, kendi işini yapar.

### Üç mod: kapalı, öneri, otomatik

Asistanın üç hali var ve hangisinde olduğunu sen belirliyorsun.

Kapalı: asistan hiçbir mesaja cevap vermez. Hazır kurulum paketi bu halde gelir. Sebebi basit: kurulan asistan müşteri metinleri onaylamadan konuşmaya başlamaz.

Öneri: asistan cevabı yazar ama göndermez. Cevap işletmecinin ekranında hazır bekler, o okuyup gönderir ya da değiştirir. Bu halde asistan hızlı değildir, çünkü gönderme insana bağlıdır.

Otomatik: asistan cevabı kendisi gönderir. Altmış saniye kuralı ancak bu halde çalışır. Sattığın şey bu haldir.

Tasarım kararı: varsayılan yol altıncı gün doğrudan otomatik hale geçmektir. Öneri hali iki durumda kullanılır: sağlık nişlerinde ilk iki gün, bir de müşteri kurulum görüşmesinde "önce ben göreyim" dediğinde. İki durumda da öneri hali en fazla iki gün sürer, sonra otomatik hale geçilir ve bu tarih kurulum görüşmesinde sesli söylenir. Sebebi: öneri halinde kalan bir sistem satılan şeyi vermiyor, işletmecinin üstüne yeni bir iş bindiriyor.

Ses notu ve fotoğraf da yalnız otomatik halde okunur. Öneri halinde kalan müşteri bu ikisini kaybeder; bunu ona söylemek zorundasın.

### Ses notu ve fotoğraf

Türkiye'de insanlar WhatsApp'a yazmak yerine ses kaydı gönderiyor. Asistan bunu okuyabiliyor: gelen ses kaydını yazıya çeviriyor ve normal mesaj gibi cevaplıyor. Fotoğrafta da aynı; gelen fotoğrafa bakıp cevap veriyor.

İkisi de hazır kurulum paketinde açık geliyor, sen bir şey yapmıyorsun. Bilmen gereken üç şey var:

1. İkisi de yalnız otomatik halde çalışıyor. Öneri halinde ses kaydı ve fotoğraf cevapsız kalıyor.
2. Cevap normal mesajdan biraz geç geliyor; ses kaydının yazıya çevrilmesi zaman alıyor.
3. Ses kaydı uzunsa ve içinde adres geçiyorsa asistanın yanlış anlaması mümkün. Adres ve tarih söz konusuysa asistan anladığını yazılı olarak teyit eder: "Anladığım kadarıyla [ilçe], [gün]. Doğru mu?" Bu cümle talimatın kurallar bölümüne yazılır.

Fotoğrafın ayrı bir faydası var: kart fotoğraf isteyen nişlerde (oto servis, cam balkon, tadilat, elektrik, diş) üçüncü sorunun yerine fotoğraf isteniyor. Gelen fotoğraf hem asistan tarafından okunuyor hem işi devralacak kişiye giden nota ekleniyor.

### Asistan takibi

Cevap gelmezse üç takip. Cevap gelince durur.

Birinci takip, karşı tarafın son mesajından yirmi üç saat sonra gider. WhatsApp'ın kuralı şu: karşı taraf sana son yirmi dört saat içinde yazdıysa ona istediğin cümleyi yazabilirsin. Birinci takip bu sürenin içinde kaldığı için serbest metin olur.

İkinci ve üçüncü takip bu sürenin dışında kalır. Onlar onaylı şablon olmak zorunda. Onaylı şablon, WhatsApp'ın sahibi Meta'nın önceden onayladığı hazır mesaj metnidir. Metinler hazır kurulum paketinden çıkar, müşteri onaylar, Meta'nın onayına musteri-sistemini-kur gönderir.

Metinler: birincisi hatırlatma, ikincisi tek cümlelik fayda, üçüncüsü kolay çıkış ("İstemezseniz sorun değil, kapatayım").

Instagram'da böyle bir onay yok. Orada üç takip de serbest metindir.

### Değerlendirme ve yönlendirme

İş modelindeki adıyla Adayı Değerlendirme ve Yönlendirme (Lead Qualification & Routing) ayrı bir bot değil, bu asistanın üç sorusunun içindedir. Üç soru üç şeyi çıkarır: ne istiyor, ne zaman istiyor, işletmenin ölçütüne uyuyor mu (bölge, iş tipi, en düşük iş bedeli; hepsi karşılama formundan). Uyuyorsa yolculuğa göre ilerler: randevu nişinde doğru takvime, teklif nişinde bilgi toplayıp "teklif hazırlanacak" aşamasına ve sorumlu çalışana. Uymuyorsa nazikçe kapatır ve kaydı "uygun değil" işaretler; işletme sahibinin telefonu boşuna çalmaz. Hangi iş hangi çalışana gidiyor, karşılama formunun yedinci sorusundan gelir; tek kişilik işletmede hepsi sahibine.

Asistanın bilgi kaynağı İşletme Bilgi Bankası'dır (Knowledge Base): hizmetler, onaylı fiyatlar, saatler, sık sorular. Orada olmayan şeye asistan cevap uydurmaz; "bunu size çalışanımız iletsin" der ve insana devir kuralı çalışır.

### Dört takip zinciri

Asistanın takibi dışında dört zincir daha var ve dördü de aynı asistanın metniyle, aynı kurallarla, aynı kayıt üstünde çalışır. Her zincirin bir tetiği, üç adımı ve bir durma şartı var. Hangi zincirlerin açılacağını nişin müşteri yolculuğu belirler.

**1. AI Otomatik Takip (AI Auto Follow-Up).** Tetik: konuşma yarıda kaldı, cevap gelmedi ya da "sonra" dendi. Adımlar yukarıda, "Asistan takibi" bölümünde. Durma: cevap geldi, randevu alındı ya da teklif gönderildi.

**2. Randevuya Gelmeyeni Geri Kazanma (No-Show Recovery).** Randevu nişinde. Tetik: randevu saati geçti ve kayıt "geldi" olmadı. Adımlar: aynı gün iki saat sonra kısa mesaj ("bugün görüşemedik, sizin için uygun başka bir saat açayım mı"), ertesi gün ikinci mesaj iki saat seçeneğiyle, üç gün sonra son mesaj. Durma: yeni randevu alındı ya da "istemiyorum" dendi. Bu zincir sitem etmez, suçlamaz; işletmeci bunu ister, sen izin vermezsin.

**3. Fiyat Teklifinden Satışa Takip (Quote-to-Close).** Teklif nişinde, sistemin asıl işi burası. Tetik: işletme teklifi onayladı ve "gönder" dedi; asistan teklifi kendisi yazmaz ve fiyat uydurmaz, işletmenin verdiği belgeyi gönderir. Adımlar: teklif gönderildi mesajı ve "sorunuz var mı"; iki gün sonra "inceleyebildiniz mi, bir soru varsa buradayım"; beş gün sonra son mesaj, işletmenin onayladığı tek bir sebep ile (sezon, kontenjan, geçerlilik tarihi; kampanya uydurulmaz). Durma: kabul, red ya da "düşüneceğim, siz aramayın". Kabul gelince kapora ya da ödeme linki düşer ve aşama "kabul edildi" olur; ödeme gelene kadar "satış" yazılmaz.

**4. Görüşme Sonrası Satış Takibi (Post-Call Follow-Up).** Randevu yapıldı ya da keşif oldu, satın alma olmadı. Tetik: kayıt "görüşüldü, karar yok". Adımlar: ertesi gün teşekkür ve görüşmede konuşulan tek şeyin özeti (işletmeci görüşmeden sonra üç kelime yazıyor, asistan onu kullanıyor; uydurma özet yok); dört gün sonra "kararınızda size yardımcı olacak bir bilgi var mı"; on gün sonra son mesaj. Durma: karar geldi ya da "aramayın".

**Tek zincir kuralı, Otomasyon ve Takip Kontrolleri (Workflow Controls).** Bir kişiye aynı anda tek zincir yazar. Randevu alınınca davet ve otomatik takip durur; teklif kabul edilince teklif takibi durur; satın alma gerçekleşince bütün satış zincirleri durur ve yalnızca hizmet sonrası zincirler (yorum, tekrar randevu) açılır. Çalışan konuşmayı devralınca asistan ve bütün zincirler o kayıtta susar. "İstemiyorum", "aramayın", "çıkar beni" gelince kayıt kapanır ve bir daha hiçbir zincir yazmaz; bu İYS kuralıdır, tartışılmaz.

Dört zincirin metinleri hazır kurulum paketinde gelir, nişe ve yolculuğa göre; müşteri kurulum görüşmesinin yapıldığı gün onaylar. Onaylanmamış zincir çalışmaz.

### Şablonun onayına nereden bakılır

Onayı Meta veriyor ve baktığın ekran onun WhatsApp yönetim ekranı. O ekranın dili İngilizce ve öyle kalacak. Sana hiçbir zaman "İngilizce ekranı oku" demeyeceğim: bir düğmeden söz ederken ekranda yazan metni, ne demek olduğunu ve nerede durduğunu birlikte vereceğim. Tarif ettiğimi ekranda bulamazsan tek yol var ve o yol her zaman açık: ekranın görüntüsünü al, buraya at, hangisi olduğunu söylerim. Bunu bir kez söylüyorum, her adımda tekrarlamayacağım. Tarayıcının çeviri özelliğini açma; çeviri düğme adlarını değiştiriyor ve bir sonraki adımda tarif ettiğim yazı ekranda kalmıyor.

Bu ekrana müşterinin hesabından giriyorsun ve kendi giriş izninle bakıyorsun. Şifre istemiyorsun.

Dördüncü günde bakacağın yer:

1. Yönetim ekranını aç. Sol menüde "Message templates" (mesaj şablonları) yazan bölüm var, oraya gir.
2. Listede her şablonun yanında durumu yazıyor: "Approved" (onaylandı), "Pending", "Rejected" (reddedildi).
3. "Approved" olan şablon kullanıma açık; işaretini koyuyorsun ve o takip mesajı çalışmaya başlıyor.
4. "Pending" olan bekliyor. Sen bir şey yapmıyorsun, ertesi gün tekrar bakıyorsun. Onayın kaç gün süreceği belli değil.
5. "Rejected" olanın metni değişecek ve yeniden gönderilecek. Reddedilme sebebi satırın yanında yazıyor; o cümleyi bana at, metni ben yeniden yazarım, göndermeyi musteri-sistemini-kur yapar.

Aynı ekranda haftalık kontrolde bakılan iki satır daha var: sol menüdeki "Phone numbers" (telefon numaraları) bölümünde hattın "Quality rating" (kalite notu) ve "Messaging limit" (günlük mesaj sınırı) satırları. Bu ikisi CRM'de görünmüyor, sadece burada duruyor. Kalite notu düşerse günlük sınır iniyor ve asistanın takip mesajları ondan etkileniyor.

### Müşteri kendi Google hesabının şifresini bilmiyorsa

Bu sık çıkıyor, şaşırma. Küçük işletmelerin Google hesabını çoğu zaman başka biri açmış oluyor: yeğeni, eski bir çalışanı, siteyi yapan kişi ya da yıllar önce çalıştığı bir ajans. Müşteri şifreyi bilmiyor, bazen hangi adresle açıldığını da bilmiyor.

Bu seni ilgilendiriyor çünkü asistan randevuyu takvime yazıyor ve o takvim müşterinin Google hesabında duruyor. Hesap açılmazsa asistan konuşmayı yürütür ama randevuyu takvime yazamaz. Takvimin kurulması musteri-sistemini-kur'un işi; buradaki mesele asistanın yazacak yeri bulup bulamaması. O yüzden bunu üçüncü günü beklemeden, kurulum görüşmesinde konuşuyorsun.

Sıra şu ve hiçbir adımda şifre istemiyorsun:

1. Hesabı kim açtıysa onu bul. Müşteriye tek soru: "Bu hesabı sizin adınıza kim açtı?" Cevap çoğu zaman bir isim oluyor. O kişi hesaba girip müşteriyi hesabın sahibi yapıyor ya da müşterinin kendi adresine yönetici daveti çıkarıyor.
2. Kimse bulunamıyorsa kurtarma yolu var: giriş ekranındaki "Forgot password" bağlantısı. Kurtarmayı müşteri kendi telefonundan yapıyor, çünkü doğrulama kodu onun numarasına ya da kurtarma adresine gidiyor. Sen yanında durup yol gösteriyorsun; kodu görmüyorsun ve istemiyorsun.
3. Kurtarma da olmuyorsa müşteri yeni bir Google hesabı açıyor ve takvim o hesapta kuruluyor. Eski hesapta kalan Google işletme profilinin sahipliği ayrı bir iş: Google'ın kendi başvuru yolundan yürüyor ve günler sürüyor.

Kim kurtarır: hesabın sahibi müşteri, kurtarmayı da o yapar. Sen yol gösterirsin, sen yapmazsın. Hesap müşterinin adına kalır; bu kural burada da değişmiyor.

Ne kadar beklenir: yedinci güne kadar. O güne kadar açılmazsa takvime yazma parçası ilk turda kurulmuyor demektir.

Kapsam dışı sayılır mı: evet. Müşterinin kendi adımını atmaması yüzünden hiç kurulamayan parça kapsam dışıdır ve güvencenin sonucuna sayılmaz. Bunu kurulum görüşmesinde sesli söylüyorsun ve onay belgesinin "neyi yapmıyorum" başlığına yazıyorsun. Rapor günü raporunda o satır boş kalıyor; sıfır sayılmıyor.

Bu sırada asistan durmuyor. Randevu saatini konuşup topluyor, sonucu devri alacak kişiye bırakıyor, takvime yazmayı o kişi elle yapıyor. Müşteri talebi kaybetmiyor, sadece bir adım elde yürüyor. Hesap sonradan açılırsa parça ikinci turda kuruluyor.

### Söylemeyecekleri

Bütün nişlerde: fiyat vermez, sayı sözü vermez, garanti vermez, müşterinin numarasına ya da hesabına dair söz vermez.

Bir yasak daha var ve bu denemede en çok kaçırılan: asistan marka, model, kapasite ve "hangisini alayım" türü teknik tavsiye vermez. "Hangi marka daha iyi", "kaç metrekareye kaç kapasite lazım", "şu modeli mi alsam bunu mu" soruları bilgi sorusudur, randevu sorusu değildir. Asistan bunlara tek cümleyle karşılık verir ve randevuya döner: "Ustamız yerinde görünce size en uygununu söylüyor." Bu cümlenin sonu randevu teklifiyle biter, konuşma orada kapanmaz.

Bunu ayrı yazmamın sebebi şu: talimatta yalnız fiyat yasağı varsa asistan teknik soruya da fiyat cevabını veriyor. Soru fiyat sorusu değil, cevap fiyat cevabı oluyor ve konuşma tuhaflaşıyor. İki yasak talimatta ayrı ayrı yazılır.

Fiyat sorusunun cevabı nişe göre üç biçimde olur: kart aralık vermeye izin veriyorsa aralık söylenir; fiyat ilanda yazıyorsa oraya yönlendirilir; ikisi de değilse "fiyatı [devri alacak kişinin adı] söylüyor, sizi ona bağlayayım".

Sağlık nişlerinde asistan şunları da yazmaz: fiyat, indirim, kampanya, hediye, çekiliş, hastaların teşekkür mesajları, tıbbi tavsiye, teşhis. Hatırlatma hastanın kendi tedavisine bağlanır. Bu sınırlar sağlık nişlerinin kartının yasal sınırlar bölümünde yazılıdır; müşterinin kendi bağlı olduğu kurallar için son sözü onun hukukçusu söyler.

Kartın yasal sınırlar bölümünde yazdığı gibi: sigortada asistan hangi acente adına konuştuğunu mesajında yazar; haşerede kesin çözüm ve garanti sözü verilmez; oto galeride pazarlık yapılmaz ve "kesin memnun kalırsınız" gibi sözler verilmez.

Asistan topladığı bilgileri yalnız randevu için kullanır. Bu bilgiler müşterinin kendi hesabında durur, sen kendi tarafına kopyalamazsın.

### Uydurmayı engelleme

Asistana bir cevap listesi verilir. Cevap listesi, asistanın bakıp cevap vereceği hazır bilgilerdir: çalışma saatleri, hizmet listesi, hizmet bölgesi, sık sorulan on soru ve cevabı, varsa site adresi. Fiyat listesi verilmez.

Bilmediği soruda uydurmaz: "Bunu tam bilmiyorum, [devri alacak kişinin adı]'na sorup döneyim" der ve devreder.

Asistanın hiç kullanmayacağı kelimelerin listesini FounderOS hazırlar ve kurulum sırasında sisteme yazar. Sen bir şey yapmazsın.

### Deneme

Üçüncü günün akşam bloğunda, kendi telefonundan, müşteriye giden bildirimler kapalıyken denersin. Bildirimleri nasıl kapatacağını o gün adım adım söylerim. On senaryo, her senaryo bir karşılıklı yazışma:
- normal randevu,
- saat sorma,
- fiyat sorusu,
- "insan mısın",
- öfkeli mesaj,
- alakasız soru,
- tek kelimelik cevap,
- yarım bırakılan konuşma,
- mesai dışı mesaj,
- nişin yasak konusu.

Denemede temiz demek: fiyat vermedi, uydurmadı, randevuyu yazdı. Bu üçü aynı anda olmadan deneme temiz sayılmaz.

Bu deneme yalnız asistanı ölçer. Beşinci günün on dört senaryoluk testi ayrıdır; orada sistemin baştan sona her parçası denenir. Biri diğerinin yerine geçmez.

### Canlıda izleme ve düzeltme

Altıncı günden on ikinci güne kadar her gün akşam bloğunda bütün konuşmaları okursun ve bana tek satır gözlem yazarsın. Düzeltmeyi ben yaparım, günde tek düzeltme. Hepsini birden değiştirirsek neyin işe yaradığını bilemeyiz. On üçüncü günden sonra bu iş haftalığa döner.

Düzeltme kurulum ayarlarında değil, talimatın kurallar bölümünde ve cevap listesinde yapılır. Kurulum ayarlarına yayına girdikten sonra dokunulmaz.

Aynı soru üç konuşmada takıldıysa cevap listesine eklenir. Devir oranı ilk hafta yarıdan fazlaysa soru sırasının ilk sorusu değiştirilir. Sağlıkta bu sayıya bakılmaz; hastanın durumunu hekimin değerlendirmesi zaten olması gereken şeydir.

## 6. Ne söyler

İkinci gün: "Bugün asistanın üç kuralını çıkarıyoruz: ne soracak, ne zaman insana devredecek, neyi asla söylemeyecek. Üçü de kartta yazıyor, ben çıkarıyorum. Metinleri bugün müşteriye gönder, yazılı onayını al. Onay gelmeden asistan kurulmaz."
Üçüncü gün: "Onay geldiyse asistanı kuruyorum. Sonra kendi telefonundan on senaryoyu deneyeceksin. Onunu da deneyeceksin, güzel olanı seçmeyeceksin: fiyat sor, kız, alakasız bir şey yaz, 'insan mısın' de. Onu da temiz çıkmadan canlıya almıyoruz."
Müşteri "asistan olduğu belli olmasın" derse: "Belli olmasın diyemeyiz. İnsan taklidi hem şikâyet getirir hem yakalandığında bütün güveni siler. Adı '[iş adı] asistanı' olacak; kimse aldatılmayacak, ama sizin gibi konuşacak."
Üçüncü soru geçilemezse: "Asistan güzel konuşuyor ama randevu almıyor. Bu iyi asistan değil; bilgi veren asistan satışı öldürür. Görev bölümünü değiştiriyorum."
Canlıdan sonra: "Altıncı günden on ikinci güne kadar, yedi gün, her akşam konuşmaları okuyacaksın. Bana tek satır yazacaksın, düzeltmeyi ben yapacağım. Günde tek düzeltme."
Müşteri Google şifresini bilmiyorsa: "Bu sık oluyor, sorun değil. İki soru: hesabı sizin adınıza kim açtı, o kişiye ulaşabiliyor musunuz? Ulaşamıyorsak kurtarmayı siz kendi telefonunuzdan yapacaksınız, ben yanınızda olacağım. Şifrenizi istemiyorum, hiçbir zaman da istemeyeceğim."
Yedinci güne kadar hesap açılmazsa: "Takvime yazma parçası ilk turda kurulmuyor. Bunu şimdi söylüyorum: o parça kapsam dışında kalıyor ve raporda o satır boş duruyor, sıfır sayılmıyor. Asistan çalışmaya devam ediyor; randevu saatini konuşup topluyor, takvime yazmayı sizin taraf elle yapıyor."
İngilizce ekranda takılırsa: "Ekranın görüntüsünü at, hangi düğme olduğunu söylerim. Tarayıcının çevirisini açma; çeviri düğme adlarını değiştiriyor ve bir sonraki adımda tarif ettiğim yazıyı ekranda bulamıyorsun."

## 7. Ne yazar

Bilgi dosyasına: asistanın üç kuralı, üretim talimatının sürümü ve tarihi, cevap listesinin içeriği, müşterinin metin onayının tarihi, deneme sonuçları, canlıdaki düzeltmeler ve tarihleri, şablonların onay durumu ve hangi gün onaylandığı, Google hesabında şifre sorunu çıktıysa hangi yolla çözüldüğü ya da hangi parçanın kapsam dışına alındığı ve bunun müşteriye hangi gün sesli söylendiği.
CRM'e: asistanın açık olduğu kanallar, devir sayısı, randevuya dönen konuşma oranı. Bunlara ek olarak asistan konuşmanın içinden iki bilgiyi kişi kartına kendisi yazar: istenen işin ne olduğu ve ilçe. İkisi de hazır kurulum paketinde bağlı gelir. Ad, telefon ve e-posta ayrı bir iş değildir, onları sistem zaten kaydeder.
Niş kartının Sahadan dolacak bölümüne: bu nişte en sık takılan soru, en sık devir sebebi, işe yarayan ilk mesaj.
musteri-sistemini-kur'a teslim edilen ayar listesi: cevap gecikmesi, mesaj uzunluğu sınırı, asistanın kullanmayacağı kelimeler, sinirlenme algılanınca insana devir, mesai dışı davranışı.

## 8. Yedek yol

- Kartta "Asistan kuralları" bölümü yoksa: kurallar kurulum görüşmesindeki cevaplardan ve benzer nişten çıkarılır, sonra karta yazılır.
- Müşteri metinleri onaylamazsa: onaylamadığı cümle değiştirilir, asistan onaysız açılmaz.
- Şablon onayı gelmediyse: birinci takip gider, çünkü o yirmi dört saatin içinde. İkinci ve üçüncü takip onay gelene kadar beklenir. Instagram'da üçü de gider.
- Cevap listesi hazır değilse: asistan yalnız randevu alır, bütün soruları insana devreder.
- Deneme temiz çıkmazsa: canlıya alınmaz, talimatın kurallar bölümü düzeltilir, tekrar denenir.
- Asistan üç karşılıklı yazışmada anlaşamıyorsa: devir, konuşma insana geçer.
- Müşteri Google hesabının şifresini bilmiyorsa: önce hesabı açan kişi bulunur, sonra kurtarma müşterinin kendi telefonundan yapılır, o da olmazsa yeni hesap açılır. Yedinci güne kadar açılmazsa takvime yazma parçası kapsam dışı kalır ve güvencenin sonucuna sayılmaz; asistan randevu bilgisini toplamaya devam eder, takvime yazmayı devri alacak kişi elle yapar. Hesap sonradan açılırsa parça ikinci turda kurulur.
- İngilizce ekranda tarif edilen yeri bulamazsan: ekran görüntüsünü atarsın, ben bakar ve hangisi olduğunu söylerim. Gün durmaz. Tarayıcı çevirisi açılmaz.

## 9. Sıradaki adım ve işaretler

Sıradaki: beşinci gün testi ve altıncı gün canlıya alma (musteri-sistemini-kur).

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Denemede iki kez uydurma çıktı: cevap listesi eksik, doldurulur.
- Üçüncü soru geçilemedi: görev bölümü randevuya odaklanacak şekilde yeniden yazılır.
- İlk hafta devir oranı yarıdan fazla (sağlık nişleri hariç): soru sırasının ilk sorusu değiştirilir.
- Aynı soru üç konuşmada takıldı: cevap listesine eklenir.
- Müşteri asistanın bir cevabından şikâyet etti: o cevap kurallara yazılır, aynı gün düzeltilir. Bu düzeltme günde tek düzeltme kuralının dışındadır.
- Dördüncü gün bitti, şablonların durumuna bakılmadı: beşinci günün sabah bloğunun ilk işi olur.
- Bir şablon reddedildi: reddedilme sebebi istenir, metin yeniden yazılır, aynı gün tekrar gönderilir.
- Hattın kalite notu düştü: günlük sınır iniyor demektir, asistanın takip mesajlarının sayısı gözden geçirilir.
- Müşterinin Google hesabına yedinci güne kadar girilemedi: takvime yazma parçası kapsam dışına alınır, bilgi dosyasına ve onay belgesine yazılır, asistan randevu bilgisini toplayıp insana devretmeye devam eder.

Beş kural: boş sayfa yok (talimat, sorular, şablon metinleri ve deneme listesi hazır gelir) · sessiz bitiş yok (deneme sonucu ve düzeltmeler bilgi dosyasına yazılır) · onay (asistanın metinlerini müşteri yazılı onaylar, canlıya alınması senin "tamam"ınla olur) · sahadan güncelleme (takılan soru, devir sebebi ve işe yarayan ilk mesaj karta yazılır) · sormaz söyler (kuralları ve talimatı FounderOS üretir).
