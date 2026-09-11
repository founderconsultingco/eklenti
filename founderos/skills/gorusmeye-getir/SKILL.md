---
user-invocable: false
name: gorusmeye-getir
description: "Öğrenci \"randevu aldım\", \"yarın görüşme var\" dediğinde. Ön görüşme sayfası ve randevu takvimi CRM açıldığı gün kurulur; o güne kadar randevular WhatsApp'tan elle alınır ve Bugünün listesi'ne yazılır; sonra randevu onayı, hatırlatma ve EVET akışı."
---

# gorusmeye-getir

## 1. Adı, rolü, pazarlamadaki karşılığı

Bu modül, randevu alındığı andan görüşmenin ilk saniyesine kadar geçen süreyi yönetir. Amacı adayın takvime yazılması değil; adayın görüşmeye gelmesi. Pazarlamada bu, ilk müşteriyi getiren zincirin "randevu" adımıdır. Onay sayfası ve hatırlatma akışı bu zincirin standart parçasıdır. Bu modülün işi olmayanlar: randevu almak (adaya-mesaj-yaz), görüşmeyi yönetmek (gorusmeyi-yonet), görüşme sonrası (gorusmeyi-analiz-et). Gelme hedefi yüzde yetmiş. Yüzde ellinin altı sorun demek. Yüzde kırk beş ve altı tıkanıklık demek.

## 2. Ne zaman çalışır
Takvim CRM hesabın açıldığı gün, yani başlangıç görüşmesinden sonra açılır ve sayfaya o gün yerleşir. O güne kadar sayfadaki "Görüşme ayarla" düğmesi WhatsApp'ına bağlıdır, saatleri sen verirsin ve İş Beyni'nin "Bugünün listesi" bölümüne yazılır. Elle alınan randevu da randevudur; sayaçlara aynı şekilde girer. Ön görüşme sayfası, randevu takvimi, hatırlatma akışı ve EVET akışı CRM açıldığı gün kurulur; sayfanın yazısı o gün bu modülden çıkar, videosu beşinci blokta çekilmiş olur. Takvim hazır pakette gelmiyor, o gün açılıyor; geri kalanı hazır kurulum paketinden senin hesabına aktarılır. Sonra her randevuda kendiliğinden çalışır: randevu CRM'e düştüğü an başlar, görüşme saatinde biter. Aday gelmezse bir kez daha çalışır, yeni randevu için.

Bir şeyi baştan söyleyeyim. Tanıdıklara ilk mesaj üçüncü günün akşamı gidiyor, yani ilk randevu dördüncü günde çıkabilir. O gün sayfa var ama videolar yok. Sorun değil: tanıdığı ikna eden şey sayfa değil senin adın; takvim daveti ve hatırlatma yeter. Videolar beşinci günde çekilince sayfa tamamlanır ve soğuk adaylar onu tam haliyle görür.

## 3. Ne okur

CRM'den okur: randevu kaydı (aday, saat, kanal, sahibinin adı, işletme), adayın aşaması, önceki temaslar ve söylediği itiraz, en çok istenen yüz işletme işareti, kanitini-hazirla modülünün ölçümü ve kanıt cümlesi. İş Beyni'nden okur: Dönüşüm Cümlesi, sistemin adı, bir dakikalık anlatım, kanal yolu, şehir, ön görüşme sayfasının adresi, senin takvim adresin. Niş kartından okur: "Kanal ve zaman" ve "Kim karar veriyor" bölümleri. Kartların ortak bulgusu şu: bu işletmeciler kendi müşterilerine karşı randevuya sadık olmayan taraf. Klima servisi "geleceğiz" deyip gelmez. Diş kliniği hastanın randevusunu haber vermeden iptal eder. Estetik merkezi bir gün önceden iptal eder. Emlakçıya günde onlarca bildirim düşer, kartta sayısı yazar. Teyit ve hatırlatma olmadan görüşmeye gelmezler.

## 4. Ne sorar

Sormaz. Randevu telefonda alınırken adaydan istenen üç şeyi, adaya-mesaj-yaz modülünün arama metnine bu modül yazar (aşağıda "Telefondayken" bölümü). Sana sorulmaz, söylenir.

## 5. Ne yapar

**A. Kurulum, CRM açıldığı gün (tek sefer).** Randevu takvimini o gün ben açıyorum; hazır pakette gelmiyor, çünkü takvim bir kişiye bağlı açılıyor ve o kişi sensin. Sayfanın yazısı, hatırlatma akışı ve EVET akışı hazır paketten geliyor.

Takvim ayarları (bunları FounderOS kurar, sen dokunmazsın):
- Görüşme süresi 30 dakika, takvim aralığı 30 dakika. Yani takvimde otuz dakikalık yer ayrılır; adaya on beş dakika denir; gerçekte görüşme yirmi beşi geçmez.
- En erken randevu 4 saat sonrası.
- Sayfadan kendisi randevu alan aday en fazla 3 gün sonrasına randevu alabilir. Telefonda alınan randevu yine 48 saat içinde olur. Yoğun haftada 5 güne esnetilebilir.
- Ara tampon 15 dakika; iki görüşme arasındaki boşluk. Tampon adaya gösterilmez.
- Dolu saatler Google Takvim'den kendiliğinden kapanır.
- Takvimde açık görünen saatler senin pencerelerinden çıkar; başka saat hiç görünmez. Hangi pencerenin açılacağı aşağıda "Randevu saatleri hangi pencereden verilir" bölümünde yazılı. Bu ayarı FounderOS kurar; çalışma düzenin değişirse aynı gün yeniden kurulur.
- Randevu formunun satırları: ad, soyad, telefon, e-posta. Ayrıca işletme adı ve tek soru: "İşletmenizde telefonu kim açıyor?" Bu soru boş bırakılırsa randevu düşmez, sadece not olarak kalır.
- Rıza: sayfada onay kutusu, altında aydınlatma metni var. Aydınlatma metni, KVKK'nın istediği, bilgilerin ne için kullanılacağını anlatan kısa yazıdır. Randevuyu telefonda sen girdiğinde adayın işaretleyeceği kutu yoktur. O zaman sözlü rıza cümlesini telefonda söylersin: "Size WhatsApp ve e-posta göndereceğim, uygun mu?" CRM notuna "sözlü onay" yazılır. Adayın yazdığı EVET yazılı kayıt olarak saklanır.
- Kendiliğinden onay kapalı. Randevu "onaysız" olarak doğar; adayın EVET'i onu onaylı yapar. "EVET yaz, onaylansın" CRM'de hazır özellik değildir, ayrı bir akış olarak kuruldu ve hesabında açık geliyor: adayın cevabında evet ya da tamam geçerse randevu kendiliğinden "onaylı" oluyor. Bunun bir sınırı var: akış sadece CRM'e düşen cevapları görüyor, yani e-postayı. Aday EVET'i WhatsApp'tan yazarsa o mesaj senin telefonunda kalıyor, onaylı işaretini sen koyuyorsun. EVET gelmezse randevu düşmez, işaret olur (bkz. C).
- Yeniden planlama izni açık; erteleme linki mesajda var. Erteleme ayrı takvimden yapılır; böylece eski hatırlatmalar yeniden gitmez.

**Randevu saatleri hangi pencereden verilir.** Saat söylenmez, pencere söylenir; pencerenin kaça denk geldiğini çalışma düzenin belirler.

- Tam zamanlı çalışıyorsan görüşmeler saha bloğunun içine girer, yani 10.00-12.00 ve 14.00-17.00 arasına. Adaya iki saat teklif edilir, üçüncüsü söylenmez: "Yarın on birde mi, üçte mi?"
- İşin yanında çalışıyorsan görüşme saha bloğunun içine konmaz. Sebebi tek: o pencere aramanın penceresi. Görüşme oraya girerse o akşamın aramaları düşer ve günlük kırk temas tutmaz. Üç yer var, üçü de saha bloğunun dışında:
  1. Hafta içi 20.30. Saha bloğu biter, akşam bloğu başlamadan önceki yarım saat. Varsayılan yer burasıdır.
  2. Öğle arası, yani sabah bloğunun ikinci hali. İş yerinden çıkabiliyorsan ve nişin telefon saati öğleye izin veriyorsa.
  3. Cumartesi 13.00'ten sonra. Cumartesi saha bloğu 10.00-13.00 arası; görüşme onun arkasına konur.
  Adaya bunlardan ikisi teklif edilir: "Yarın sekiz buçukta mı, cumartesi birde mi?"
- Görüşme yirmi beş dakikayı geçmediği sürece akşam bloğu yerinde kalır. Görüşme uzarsa o akşamın kaydı, analizi ve provası akşam bloğunun sonuna kayar; hiçbiri atlanmaz.
- İşletmecinin uygun olduğu saat senin pencerelerinin hiçbirine denk gelmiyorsa görüşme cumartesiye alınır. Cumartesi de olmuyorsa randevu verilmez, aday "sonra" aşamasına yazılır ve sebebi kaydedilir. Yarım yamalak saatte yapılan görüşme, hiç yapılmayan görüşmeden kötüdür.

Ön görüşme sayfası:
1. Üstte tek satır: "Görüşmeden önce üç dakikalık videoyu izleyin, sonra EVET yazın ki yerinizi kesinleştireyim."
2. Video üç ile beş dakika. Sen kendi telefonunla çekersin; metni satis-videosunu-cek'te yazılır (yedi bölüm), burası özetidir:
   - kim olduğun, tek cümle;
   - görüşmede ne olacağı: teşhis, satış değil;
   - ona soracağın üç soru (telefonu kim açıyor, cevapsız arama kaç, eski liste nerede); böylece düşünerek gelir;
   - nasıl katılacağı: sessiz yer, araç kullanırken değil, kalem kâğıt;
   - kanıt: kartın sektör rakamı; dördüncü bloktan sonra kanıt cümlesi ve tarayıcı demosunun kırk ile altmış saniyelik ekran kaydı; o güne kadar yalnızca kartın sektör rakamı kullanılır; kanıt hikâyesi çıkınca o;
   - kapanış: "Bu görüşme için işletmenizi inceliyorum, lütfen gelin ve sözünüzü tutun."
3. EVET düğmesi: WhatsApp'ta hazır "EVET" mesajı açan link. Takvim davetini kabul etmesi ayrıca telefonda söylenir (B bölümü, üç küçük söz).
4. Altında üç kısa itiraz cevabı, yazıyla:
   - "Telefonum elimden gider mi?" Hayır; yeni numara açılır, mevcut numaraya dokunulmaz.
   - "Yazılı asistan müşterimi kaçırır mı?" Fiyat vermez, bilgi toplar, randevuya çevirir; son sözü işletme sahibi verir.
   - "Ne kadar?" Fiyat aralığı yazılır; kesin rakam görüşmede netleşir.
5. Üç kademenin adı ve karşılaştırma fiyatı (Kademe 2'nin üç aylık peşin paketi), İş Beyni'nin dördüncü bölümünden, tek satır; başka rakam yok. Sitede fiyat yoktur, karşılaştırma fiyatının tek yeri burasıdır.
6. Referanslar varsa referanslar; yoksa kartın sektör rakamı.

Hatırlatma akışı: hazır kurulum paketinde gelir, sen sadece adını girersin. Kanal: WhatsApp ve e-posta. CRM'in numara verdiği ülkelerde Türkiye olmadığı için hatırlatmaların WhatsApp tarafı senin kendi WhatsApp Business hattından, senin elinle gider; CRM metni hazırlar ve saati gelince sana hatırlatır, sen gönderirsin. E-posta her durumda CRM'den kendiliğinden gider ve link oradadır. Gece mesaj yok, 09.00-21.00 arası. Tek istisna 43 dakika mesajı; sabah randevusunda 09.00'dan önce de gider. Bu aralık adayın saatidir, senin pencerenden ayrıdır: aday gece mesaj almaz, sen de kendi pencerenin dışında mesaj göndermezsin.

Hangi hatırlatma hangi pencerede gider. E-posta tarafı her durumda CRM'den kendiliğinden gider; senin pencerenle ilgisi yok. WhatsApp tarafı senin elinden çıkar ve şu pencerelere düşer:
- Randevu alınınca giden ilk mesaj: randevuyu aldığın anda, yani saha bloğunda. Telefonu kapatmadan gönderirsin.
- Yirmi dört saat önceki mesaj: düşen saat senin pencerene denk geliyorsa o an gider. Denk gelmiyorsa, yani işin yanındasın ve o saatte iş yerindeysen, bir sonraki pencerenin ilk beş dakikasında gider: sabah bloğu ya da saha bloğu. Saat yirmi biri geçtiyse ertesi sabaha kalır; gece gitmez.
- Kırk üç dakika mesajı: görüşme zaten senin pencerende olduğu için bu mesaj da o pencerenin içindedir. E-posta tarafı kendiliğinden gider, sen dokunmazsın.
- İlk yirmi randevuda EVET gelmediyse yapılan iki saat önceki arama: tam zamanlıda saha bloğunun içindedir. İşin yanındaysan iki saat önce iş yerindesin; o aramayı öğle arasında ya da sabah bloğunda yaparsın. İkisi de olmuyorsa aramanın yerine görüşme sabahı tek satır yazarsın, arama düşer.
- Gelmeyen randevu araması ve arkasındaki mesaj: görüşme saatinin hemen üstüdür, yani hangi pencerede görüşme varsa orada.
- Randevu alınınca hemen: "Merhaba [Ad] Bey, ben [öğrenci], [gün] [saat] görüşmemiz kayıtta. Görüşmeden önce şu üç dakikalık videoyu izleyin, sonra EVET yazın, yerinizi kesinleştireyim." Link WhatsApp ve e-postada.
- 24 saat önce, insan yazmış gibi, kendiliğinden gitmiş görünmeyen: "[Ad] Bey, ben [öğrenci]. Yarın [saat] konuşuyoruz, takvimde görüyorum. Geleceğinizi bir 'tamam' ile yazar mısınız?" Randevu yirmi dört saatten yakınsa bu mesaj, randevu alındıktan iki saat sonra ya da aynı akşam 20.00'de gider.
- 43 dakika önce, kendiliğinden: "43 dakika sonra görüşüyoruz, uygun mu?" Neden kırk üç? Yuvarlak saat kendiliğinden giden mesaj gibi görünür; tuhaf rakam insan yazmış gibi durur. Görüntülü görüşmeyse arama linki bu mesajda olur. Telefonla görüşmeyse "sizi ben arayacağım" yazar. Ayrı "1 saat önce" mesajı yok; 43 dakika mesajı onun yerine geçer.
- İlk 20 randevuda ve soğuk telefonla (aday seni hiç tanımazken aranarak) alınmış randevularda, EVET gelmediyse görüşmeden iki saat önce sen ararsın: "Bugün üçte görüşüyoruz, hazır mısınız? Şu iki rakamı yanınızda bulundurun." EVET geldiyse aramazsın.
- Görüşmeden bir saat sonra gidecek mesaj bu modülün değil, gorusmeyi-analiz-et modülünün işidir. O mesaj yalnızca görüşme "düşüneyim" ile bitip karar görüşmesi hattayken tarihlendiyse gider; tek satırlık teyittir.

**B. Telefondayken, randevu alınırken.** (Bu modül, adaya-mesaj-yaz modülünün dördüncü parçasına şu dört satırı ekler.)
- Sen telefondayken adayın bilgisini takvime kendin girersin; "siz doldurun" demezsin.
- Randevu yirmi dört ile kırk sekiz saat içinde; en iyisi kırk saat sonrası. "Haftaya" yok; iki saat teklif edilir, üçüncüsü söylenmez. Teklif edilen iki saat senin pencerelerinden çıkar (yukarıdaki "Randevu saatleri hangi pencereden verilir" bölümü). Tam zamanlıysan "Yarın on bir mi, üç mü?" İşin yanındaysan "Yarın sekiz buçuk mu, cumartesi bir mi?" Saatleri sen açıklamazsın; niye o saat diye sorarsa tek cümle: "O saatlerde tam size ayrılıyorum".
- Kapatmadan önce sözlü rıza ve üç küçük söz: "Size WhatsApp ve e-posta göndereceğim, uygun mu? Hangisi? Şimdi davet gönderiyorum. Kapatınca gelen mesaja EVET yazın. Üç dakikalık videoyu bu akşam izleyin. Takvim davetini kabul edin." CRM açılmadıysa davet yerine WhatsApp'tan saat teyidi gider ve son cümle "Saati WhatsApp'tan yazıyorum, 'tamam' deyin" olur.
- Kapanış, geleceği kesinmiş gibi: "Yarın on birde sizi arıyorum, hazır olun." "İlginizi çekerse gelin" demek yasak.
- Aciliyet gerçek sebeple: kartın sızıntısı ("bu hafta kaçan her arama"). Uydurma "yer kalmadı" baskısı yok.
- Gelmemenin asıl sebebi hatırlatma eksikliği değil, randevunun nasıl alındığı. İşletmeci telefonu kapatmak için "evet" der. Bu yüzden görüşme ayarlanmadan üç şey net olur: sorunun farkında mı, parası var mı, kararı kim veriyor.

**C. Görüşmeye kadar işaretler.**
- EVET geldi ya da 24 saat mesajına "tamam" geldi: yeşil, dokunma. Videonun izlenip izlenmediğini sayan bir sayaç şimdilik yok; tek işaret adayın cevabı.
- EVET de "tamam" da gelmedi: ilk yirmi randevuda görüşmeden iki saat önce ararsın (yukarıda). Sonraki randevularda görüşme sabahı kendi telefonundan tek satır yazarsın. Ulaşamazsan saat yine tutulur; sabah planı bunu bilir.
- Aday "erteleyelim" derse: hemen yeni saat, yine kırk sekiz saat içinde; akış baştan başlar. İki erteleme sonrası aday "sonra" aşamasına geçer.
- Video izlenmediyse görüşme yine yapılır; açılışta tek cümleyle anlatırsın (gorusmeyi-yonet B).
- Görüşme telefonla da olabilir.

**D. Gelmeyen randevu.**
- Saat gelip beş dakika geçince ara: "Görüşmede bekliyorum, her şey yolunda mı?" Açmazsa tek satır WhatsApp: "[Ad] Bey, aradım ulaşamadım. Bugün uygun olmadıysa yarın aynı saati tutayım mı?"
- CRM'de randevu durumunu "Gelmedi" yap. (Ekran İngilizce, orada "No Show" yazar. Durumlar: onaysız, onaylı, geldi, gelmedi, iptal.) Bu işaret kendiliğinden düşmez; gelmedi işaretini sen koyarsın, sabah planı görür. Aşama "görüşme ayarlandı"da kalır; iki denemeden sonra "sonra" olur. Randevu durumu ve aşama ayrı satırlardır.
- İki gün sonra tek takip: yeni randevu teklifi, tarihli. İki denemede de gelmezse "sonra"; altı ayda bir yeniden taranır.
- Gelmeyen aday listeden düşürülmez.
- Geç gelen, araçta olan, dinlemeyen aday: "Bugün uygun değilse yarın aynı saati tutalım, size haksızlık olmasın" de ve kapat. Yarım görüşme yapma.

**E. Ölçüm ve teşhis.**
- Gelme oranı = gelen / ayarlanan. Hedef yüzde yetmiş; yüzde ellinin altı sorun.
- Otuz randevu dolmadan yorum yok. Teşhis sırası:
  1. Önce randevu nasıl alındı: aciliyet var mıydı, üç şart net miydi?
  2. Sonra niteleme: gelmeyenler hangi tip? Telefonu personelin açtığı işletmeler mi?
  3. En son hatırlatma akışı.
  Hatırlatmayı ilk suçlamak, yanlış yere müdahale.
- Gelmeyenlerin ortak özelliği CRM'de görülürse işaret degisiklige-karar-ver modülüne gider. Üç yüz temas kilidi randevu ayarlarını kapsamaz; bu modülün ayarları (saat penceresi, mesaj metni) otuz randevudan sonra değişebilir.

## 6. Ne söyler

Randevu düşünce sana: "Randevun var: Ahmet Bey, yarın on birde. Üç şey gitti: davet, video, EVET isteği. Senin işin tek. Bu akşam Ahmet Bey EVET ya da 'tamam' yazdıysa dokunma. Yazmadıysa sabah bloğunda ara: 'Bugün on birde görüşüyoruz, hazır mısınız? Şu iki rakamı yanınıza alın.' İki saat öncesi mesajı CRM açıksa kendiliğinden gider, açılmadıysa sen gönderirsin. Prova bugün akşam bloğunda."

İşin yanında çalışan öğrenciye, randevu saati verilirken: "Saha bloğun sekiz buçukta bitiyor. Görüşmeyi oraya değil, hemen arkasına koyuyoruz: yarın sekiz buçuk. Adaya iki saat söyle, üçüncüsünü söyleme: yarın sekiz buçuk mu, cumartesi bir mi? Aramanın saatini görüşmeye yedirmiyoruz; bu akşam yine on arama var."

Gelmeyen randevuda: "Ahmet Bey gelmedi. Şimdi ara; açmazsa şu mesaj hazır. İki gün sonra tek takip, sonra 'sonra' aşaması. Suçlu hatırlatma değil, randevunun alınış şekli. Otuz randevu dolunca bakarız; şimdi sıradaki arama."

Otuz randevudan sonra gelme oranı yüzde ellinin altındaysa: "Otuz randevu, on ikisi geldi. Hatırlatmalar gitmiş, mesele orada değil. Gelmeyen on sekizi aynı tip: telefonu personelin açtığı işletmeler. Yarından itibaren sahibi telefondayken saat alıyoruz. Personelle randevu yok."

## 7. Ne yazar

CRM'e yazar: randevu durumu (onaysız; EVET gelince onaylı; sonra geldi ya da gelmedi), hatırlatma gönderim kayıtları (bunları kendiliğinden giden mesaj sistemi yazar), erteleme sayısı, sözlü rıza notu, gelmeme sebebi (sen söylersen). Aşama satırı ayrıdır; adaya-mesaj-yaz modülünün kuralıyla yazılır. İş Beyni'ne yazar: gelme oranı (otuz randevuda bir güncellenir), ön görüşme sayfasının ve videonun adresi, randevu takviminin adresi (takvim CRM açıldığı gün kurulur, adresi aynı gün İş Beyni'ne yazılır), hangi hatırlatmaya cevap geldiği. Niş kartının "sahadan dolacak" bölümüne yazar: bu nişte gelme oranı ve işletmecinin gerçekten müsait olduğu saat. Kartlarda bu bilgi yoktur; ilk gerçek bilgi buradan gelir. Onay: hazırlık günü kurulum ve şablon metinleri senin "tamam" demenle geçer. Sonrasında hatırlatmalar onaylı şablondan kendiliğinden gider; bu, onaylanmış e-posta takipleriyle aynı istisnanın içindedir. Arama ve gelmeyen randevu mesajı her zaman senin elinden çıkar.

## 8. Yedek yol

WhatsApp Business hattın hazır değilse hatırlatmalar yalnız e-postadan gider ve sen o gün telefonla arayarak teyit edersin. Ön görüşme videosu çekilmediyse sayfa yazıyla açılır, "video yarın" notu düşülür, gün durmaz. Sayfa henüz yayında değilse mesajlar linksiz gider; sayfanın içeriğini telefonda üç cümleyle sen söylersin. EVET iş akışı kurulamadıysa gelen EVET'i görünce durumu elle "onaylı" yaparsın. CRM henüz açılmadıysa randevu İş Beyni'nin "Bugünün listesi" bölümüne yazılır; hatırlatmaları kendi telefonundan elle gönderirsin; akış aynı. Adayın e-postası yoksa sadece WhatsApp; davet de WhatsApp'tan gider.

## 9. Sıradaki adım ve işaretler

Görüşme saatinde gorusmeyi-yonet modülü devralır. Ondan önce gorusme-provasi-yap modülü o günün provasını yaptırır (ilk yirmi görüşmede zorunlu). Görüşme bitince gorusmeyi-analiz-et modülü çalışır. FounderOS'a giden işaretler:
- EVET oranı düşük (otuz randevuda dokuzdan az): telefondaki üç küçük söz atlanıyor demek; prova.
- Gelme oranı yüzde ellinin altı (otuz randevudan sonra): teşhis sırası işler.
- Aynı adayda iki erteleme: "sonra" aşaması.
- EVET gelmemiş randevuda sabah aramasını atlıyorsan: sabah planına uyarı.
- İşin yanında çalışan öğrencide randevu saha bloğunun içine düşmüş: o akşamın aramaları eksik kalır, sabah planına uyarı gider ve sonraki randevular pencerenin arkasına alınır.
- Takvimde senin pencerenin dışında bir saat açık görünüyor: takvim ayarı o gün yeniden kurulur.
Kartın "işletmeci ne zaman müsait" bilgisi otuz randevuda dolar ve adaya-mesaj-yaz modülünün saat kuralını günceller.

Beş kural: boş sayfa (takvim, sayfa metni, video metni, mesajlar hazır kurulum paketinde) · sessiz bitiş (her randevuda öğrenciye tek iş ve prova saati) · onay (kurulum ve şablonlar "tamam" ile; hatırlatmalar onaylı şablondan kendiliğinden, arama ve gelmeyen randevu mesajı öğrenciden) · sahadan güncelleme (gelme oranı kartı ve adaya-mesaj-yaz'ın saat kuralını yeniler; gelmeyenlerin tipi degisiklige-karar-ver'e) · sormaz söyler (saat penceresi, mesaj sırası ve teşhis sırası sistemden; öğrenci sadece "hayır" diyebilir).

---
