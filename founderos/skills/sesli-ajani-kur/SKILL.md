---
user-invocable: false
name: sesli-ajani-kur
description: "Müşterinin birinci dalgası, teklifin başlığı. Gelen aramayı karşılayan yapay zekâ resepsiyonisti: öğrenci konuşma metnini hazırlar ve onaylatır, hattı, ajanı ve CRM bağlantısını ekip kurar, öğrenci on arama testini yapar. Giden arama, telefon sağlayıcısı doğrulayana kadar kurulamayan parçadır."
---

# sesli-ajani-kur

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç.

## 1. Adı, rolü, pazarlamadaki karşılığı

Müşterinin telefonuna gelen aramaya cevap veren sesli ajanı kuran modül. İşletme telefonu açmazsa arama ajana düşer; ajan Türkçe konuşur, en fazla üç soru sorar, takvime randevu yazar, gerektiğinde işi insana aktarır. Modül, FounderOS'un belli bir işi yapan parçasıdır.

Buradaki gün numaraları müşterinin teslimat takvimindendir, senin doksan gününden değil.

Dil ayrımı: "müşteri" senin paranı ödeyen işletmedir. Telefonu açan kişiye "arayan kişi" diyoruz.

İş modelindeki adıyla bu, AI Telefon Karşılama Asistanı (AI Voice Receptionist). Aynı ajanın giden hali, AI Dış Arama (AI Outbound Calling), ayrı bir kuruluş değil ayrı bir ayardır: sistem kendisi arama başlatır, eski müşteriyi ya da yeni başvuruyu arar, görüşmeyi randevuya ya da çalışana yönlendirir. Dış arama teklifin ikinci ve üçüncü akışının sesli halidir ve teklifte yazar. Ama şimdilik yok: telefon sağlayıcısı bu hat üzerinden sesli ajanla giden aramayı belgelemiyor, yalnız gelen arama belgeli. Belgelenene kadar bu parça kurulamayan parça sayılır: müşteriye kurulum görüşmesinde söylenir, iki akış yazılı yürür ve açılmadığı her ay ücret yüzde yirmi iner. Belgelendiği gün ekip açar; numara, hesap ve kişinin iletişim izni kontrol edilir (sağlık nişlerinde ayrıca kişinin bilgi kullanım onayı), gelen taraf sorunsuz çalıştıktan sonra ayrıca sınanır. Sonuç bilgi dosyasına yazılır. Cevapsız aramaya mesaj göndermek dış arama değildir; o ayrı bir işlevdir ve yazılı taraftadır.

Sesli ajan yazılı asistanın yerine geçmiyor, yanında duruyor. İkisi aynı karttan çıkıyor, aynı üç soruyu soruyor, aynı hallerde işi insana bırakıyor. Sebebi tek cümle: bir işletme iki ağızdan iki farklı şey söyleyemez. Yazılı asistan yazana cevap veriyor, sesli ajan arayana.

Üç çıktısı var, üçü de niş kartından çıkar: ajanın konuşma metni, insana devir kuralları, söylemeyecekleri.

Şunlar bu modülün işi değildir: numara, hat, yönlendirme, akışlar, test ve canlıya alma. Onlar musteri-sistemini-kur'un işi. Bu modül ajanın ne konuşacağını kurar, telefonun nasıl bağlandığını değil.

Ajanın sesli ajan servisine kurulması, hattın bağlanması ve ajanın CRM'e bağlanması FounderOS ekibinin işidir. Sen anahtar, şifre ve hat bilgisi görmezsin, hiçbir yere girmezsin. Senin işin metin: FounderOS'la hazırlarsın, müşteriye onaylatırsın, destek adresine gönderirsin; ekip "bağlandı" deyince on arama testini yaparsın.

Pazarlamadaki karşılığı: sattığımız şey telefona bakan robot değil, kaçan aramanın randevuya dönmesi. Küçük işletmede kaçan arama en pahalı kayıptır, çünkü arayan kişi kapatır ve bir sonrakini arar.

## 2. Ne zaman çalışır

Teklifin başlığı sesli resepsiyonist olduğu için (22 Eylül 2026) sesli taraf birinci dalganın parçasıdır: metinler yazılı asistanla aynı gün hazırlanır ve hat gelir gelmez canlıya alınır. Hat dışarıdan geldiği için canlıya alma yedinci ile on dördüncü gün arasına düşebilir; bu gecikme müşteriye kurulum görüşmesinde söylenir.

- İkinci gün: kart okunur, ajanın konuşma metni ve üç kuralı çıkarılır. Metin tek sayfada müşteriye gider ve yazılı onayı istenir. Bu sayfa yazılı asistanın sayfasıyla birlikte gider; müşteri iki metni bir oturumda onaylar.
- Onay gelir gelmez: onaylı metni ve cevap listesini destek@founderos.so adresine, müşteri bölümünün adıyla gönderirsin. Ekip ajanı sesli ajan servisine kurar, metni yükler, Türkçe sesi seçer.
- Hat bağlandığı gün (yedinci günden on dördüncü güne): ekip hattı ajana, ajanı müşterinin CRM bölümüne bağlar ve sana "bağlandı" yazar.
- Aynı gün ya da ertesi gün, akşam bloğunda: 0850 numarayı kendi telefonundan arayıp on denemeyi yaparsın.
- Deneme temizse: yönlendirme müşterinin telefonundan açılır ve gerçek aramayla iki tur daha yapılır. Yönlendirmeyi açmak musteri-sistemini-kur'un işi.
- Canlıya alındıktan sonraki yedi gün: her akşam bütün konuşma dökümleri okunur, günde tek düzeltme yapılır. Sonra haftalık kontrol sistemi-kontrol-et'e geçer.
- Kart güncellenince ya da müşteri yeni hizmet ekleyince yeniden çalışır.

Pencereler: kart okuma ve metin yazma sabah bloğunda; on aramanın yapılması ve canlıdaki günlük okuma akşam bloğunda; müşteriyle yapılan her konuşma kurulum bloğunda.

## 3. Ne okur

Niş kartından: "Asistan kuralları" bölümü (toplanacak bilgiler, insana devir, söylenmeyecekler), işletmecinin kendi kullandığı cümleler, yoğun saatler, yasal sınırlar.
Müşterinin bilgi dosyasından (`musteriler/<musteri-adi>.md`): iş adı, çalışma saatleri, randevu uzunluğu, hizmet bölgesi, hizmet listesi, sık sorulan on soru ve cevabı, devri alacak kişinin adı ve numarası, 0850 numara ve hattın bağlandığı tarih.
yazili-asistani-kur'dan: üretim talimatının kimlik bölümü, soru sırası, insana devir listesi, söylemeyecekleri, cevap listesi. Bunlar yeniden yazılmaz, olduğu gibi alınır; değişen sadece mecraya göre biçimidir.
musteri-sistemini-kur'dan: hattın kurulduğu gün, ajanın CRM bağlantısının açıldığı gün, yönlendirmenin hangi durumlar için açıldığı.

## 4. Ne sorar

Sormaz. Metin ve kurallar karttan üretilir. Senden aldığı üç şey: müşterinin metne yazılı onayı, on aramanın sonucu, canlıdan sonra günlük tek satır gözlem.

## 5. Ne yapar

### Sesin yazıdan altı farkı

Aynı kurallar, farklı mecra. Bunları bilmeden yazılı metni sese çevirirsen ajan kâğıt okuyan biri gibi konuşur.

1. Söylenen geri alınmaz. Yazıda yanlış giden mesaj düzeltilir, seste söylenen söylenmiştir. O yüzden ajan emin olmadığı hiçbir şeyi söylemez, "sorup döneyim" der.
2. Sessizlik kopukluk demektir. Yazılı asistanda beş ile otuz saniye gecikme iyi bir şeydi; seste bir saniyelik boşluk bile arayana hat düştü hissi verir. Ajan duraksamaz.
3. Ajan sözü kesmez. Arayan konuşurken susar, cümlesi bitince konuşur.
4. Cümleler tek nefeslik olur. Yazıda yüz altmış harf ölçüydü; seste ölçü şu: bir cümlede tek bilgi, tek soru.
5. Rakam, tarih ve saat tekrarlanır. "Salı, on dört Ekim, saat üçte" gibi. Yanlış duyulan tek rakam yanlış randevu demektir, yanlış randevu da gelmeyen müşteri.
6. Ad ve adres tekrarlanır ama harf harf söyletilmez. "Yılmaz, Nilüfer, doğru mu?" yeter. Harf harf teyit arayanı bunaltıyor ve konuşmayı uzatıyor.

### Karşılama ve kimlik

Karşılama kalıbı: "[İş adı], ben [iş adı]'nın sesli asistanıyım, buyurun."

Kimlik ilk cümlede geçer. Kural yazılı asistandaki kuralın aynısı: insan taklidi yok. "İnsan mısınız" sorusunun cevabı açıktır: "Hayır, ben insan değilim, [iş adı]'nın sesli asistanıyım. İsterseniz [devri alacak kişinin adı] sizi birazdan arasın."

Bunu satış dilinle karıştırma. "Bot satmıyoruz, yapay zeka kelimesi geçmez" kuralı senin işletmeciyle konuşurken kullandığın dildir. Ajanın kendi dilinde amaç insan taklidi yapmak değil, işletmenin dilini konuşmak.

### Soru sırası

Yazılı asistanla birebir aynı: en fazla üç soru, her seferinde tek soru, sıra karttaki öncelik sırasından. Kartta sıra yazmıyorsa varsayılan sıra şu: ne istiyor, ne zaman istiyor, nerede ya da ne kadar büyük bir iş.

İki fark var. Birincisi, telefon numarası sorulmaz; arayanın numarası zaten belli. İkincisi, fotoğraf istenmez; kart fotoğraf isteyen bir nişse ajan konuşmanın sonunda "size bir mesaj atıyorum, fotoğrafı oraya gönderin" der ve fotoğraf WhatsApp'tan gelir.

### Randevu ve onay

Ajan takvimde boş saati görür ve en fazla iki saat seçeneği söyler. Arayan birini seçince ajan tarihi, günü ve saati tekrar eder, adı teyit eder, randevuyu yazar.

Onay yazılı gider. Konuşma biter bitmez arayanın numarasına WhatsApp'tan onay mesajı düşer. Sebebi basit: sesli onay unutulur, yazılı kalır. Onay mesajını gönderen akış musteri-sistemini-kur'da kurulu.

### İnsana devir

Yazılı asistandaki altı hal aynen geçerli. Konu tarafında para, hukuk ve garanti, uzmanlık; durum tarafında öfke ve şikâyet, "insanla görüşmek istiyorum", üç turda anlaşamama.

Sese özel iki hal daha var:
- Ajan üst üste iki kez anlamadıysa. Hat kötüdür, ortam gürültülüdür ya da konuşma ağır gelmiştir. Üçüncüyü denemez, aktarır.
- Konuşma beş dakikayı geçtiyse. Beş dakikada bitmeyen konuşma randevu konuşması değildir.

Aramayı doğrudan işletmeye bağlamak şimdilik yok: telefon sağlayıcısının belgeleri gelen aramayı anlatıyor, aramanın devredilmesini anlatmıyor. Bu modülde "aktarma" bu yüzden tek biçimde çalışır ve utanılacak bir yanı yok: ajan "sizi [devri alacak kişinin adı] birazdan arayacak" der, konuşmayı kapatır, kayıt acil işaretiyle bildirime düşer. Mesai dışında ajan ertesi iş gününün ilk saatini söyler. Ekip doğrudan bağlamayı bir hatta doğrularsa sana yazar; o güne kadar metne "bağlayayım" yazılmaz.

Aktarmadan sonra ajan susar. O kayda bir daha karışmaz.

### Mesai dışı

Ajan gece de gündüz de açar. Randevuyu yalnız takvimdeki saatlere yazar. "Yarın açığız" demez, "yarın saat onda uygun, yazayım mı" der.

### Söylemeyecekleri

Yazılı asistanla aynı liste: fiyat vermez, sayı sözü vermez, garanti vermez, müşterinin numarasına ya da hesabına dair söz vermez.

Fiyat sorusunun cevabı nişe göre üç biçimde olur: kart aralık vermeye izin veriyorsa aralık söylenir; fiyat ilanda yazıyorsa oraya yönlendirilir; ikisi de değilse "fiyatı [devri alacak kişinin adı] söylüyor, sizi birazdan arasın".

Sağlık nişlerinde ajan şunları da söylemez: fiyat, indirim, kampanya, hediye, çekiliş, hasta yorumu, tıbbi tavsiye, teşhis. Bu sınırlar kartın yasal sınırlar bölümünde yazılı ve ajanın metnine olduğu gibi girer; öğrenciye sebebi anlatılmaz. Metne kliniğin yazılı "onaylıyorum"u yeter, kliniğin kendi danışmanına sorması kliniğin işidir.

Bir şey daha: konuşmanın kaydedildiği ilk cümlede söylenir. "Görüşme kayıt altına alınıyor" cümlesi karşılamanın hemen ardından gelir. Bunu atlamak yok; kayıt açık olduğu sürece bu cümle metinde durur. Sebebi öğrenciye anlatılmaz.

### Uydurmayı engelleme

Ajana yazılı asistandaki cevap listesinin aynısı verilir: çalışma saatleri, hizmet listesi, hizmet bölgesi, sık sorulan on soru ve cevabı, varsa site adresi. Fiyat listesi verilmez.

Bilmediği soruda uydurmaz: "Bunu tam bilmiyorum, [devri alacak kişinin adı]'na sorup döneyim" der ve aktarır. Seste uydurma yazıdakinden pahalıdır, çünkü arayan onu anında doğru bilgi sanıp kapatır.

### Konuşma bitince kayda ne yazılır

Ajan konuşmayı bitirdiğinde çıkardığı bilgiler CRM'e düşer. Doldurduğu satırlar: talep kanalı (sesli ajan), talep tarihi, talep saati, hizmet tipi, arama sonucu (ajan karşıladı, randevu yazıldı, insana aktarıldı, cevapsız kapandı), randevu yazıldıysa randevu tarihi, kayıt kaynağı (sistem).

Konuşmanın dökümü ve özeti alan olarak tutulmaz, kaydın konuşmalar bölümüne çağrı kaydı olarak düşer. Aynı bilgiyi iki yerde tutmak, ikisinin birbirini tutmaması demektir.

### Türkçe kurulumu

Dili ve sesi ekip ajanı kurarken ayarlar: tek dil, Türkçe; çok dilli kurulumda her dilin doğruluğu düşüyor, müşterinin işi Türkçe. Sesi ekip seçer. On arama testinde kulağına doğal gelmiyorsa destek adresine yazarsın, ekip öbür Türkçe sesi dener. Kalan ses bilgi dosyasına yazılır, sonraki müşterilerde oradan başlanır.

En çok hata çıkan üç yer: sayılar, saatler, mahalle ve sokak adları. Deneme listesinde üçü de var.

### Konuşma süresi ve para

Ajanın konuşma dakikası senin cebinden çıkıyor. Dakika ücretini ekip bağlantı gününde sana yazılı söyler; kâr hesabına "sesli dakika" satırıyla girer. Uzun konuşma pahalı konuşma demek, üstelik uzun konuşma iyi konuşma da değil.

Hedef üç dakika. Beş dakikayı geçen konuşma insana aktarılır. Bu hem parayı hem kaliteyi koruyan tek ayar, o yüzden ikisini ayrı ayrı kurmuyoruz. Bu sınır bir tasarım kararı; ilk müşteride gerçek konuşma süreleri ölçülür ve rakam o zaman güncellenir.

### Deneme: on arama

Ekip "bağlandı" yazdıktan sonra, 0850 numarayı kendi telefonundan, müşteriye giden bildirimler kapalıyken ararsın. Her senaryo bir arama:
- normal randevu,
- saat sorma,
- fiyat sorusu,
- "insan mısın",
- öfkeli arayan,
- alakasız konu,
- gürültülü ortamdan arama,
- ajanın sözünü kesme,
- mesai dışı arama,
- nişin yasak konusu.

Denemede temiz demek dört şeyin aynı anda olması: fiyat vermedi, uydurmadı, randevuyu doğru güne ve saate yazdı, adı ve saati doğru tekrarladı. Üçü tutup dördüncüsü tutmuyorsa temiz değildir.

Ayrı olarak iki aramada özellikle sayı ve adres denenir: "on dört Ekim saat üç buçuk" ve mahalle adı geçen bir adres. Yanlış yazıyorsa sorun metinde değil, tanıma tarafındadır: destek adresine yazarsın, ekip öbür seçeneği dener.

Bu deneme yalnız ajanı ölçer. musteri-sistemini-kur'un ikinci dalga testi ayrıdır; orada yönlendirme, çağrının CRM'e düşmesi ve yazılı dönüş de denenir. Biri diğerinin yerine geçmez.

### Canlıda izleme ve düzeltme

Canlıya alındıktan sonraki yedi gün, her akşam bloğunda bütün konuşma dökümlerini okursun ve bana tek satır gözlem yazarsın. Dökümler CRM'de kaydın konuşmalar bölümünde durur. Düzeltilmiş metni ben hazırlarım, sen destek adresine gönderirsin, ekip ajana yükler; günde tek düzeltme. Sonra haftalığa döner.

Düzeltme metnin görev ve kurallar bölümlerinde ve cevap listesinde yapılır. Ses ayarına, tanıma tarafına ve hat ayarlarına yayına girdikten sonra dokunulmaz.

Aynı soru üç konuşmada takıldıysa cevap listesine eklenir. Aktarma oranı ilk hafta yarıdan fazlaysa soru sırasının ilk sorusu değiştirilir. Ortalama konuşma süresi dört dakikayı geçtiyse soru sayısı üçten ikiye iner.

## 6. Ne söyler

İkinci gün: "Sesli ajanın metnini de bugün çıkarıyoruz. Yazılı asistanla aynı üç soru, aynı aktarma kuralları, aynı yasak liste. Değişen tek şey biçim: cümleler kısalıyor, rakamlar tekrarlanıyor, kimlik ilk cümlede geçiyor. İki metni birlikte gönder, tek onay al."
Ekip "bağlandı" yazınca: "Hat ve sesli ajan bağlandı. Bu akşam 0850 numarayı kendi telefonundan arayıp on denemeyi yapacaksın. Ses kulağına doğal gelmezse söyle, ekibe yazalım."
Deneme günü: "On aramayı yap ve güzel olanı seçme. Kız, fiyat sor, sözünü kes, gürültülü bir yerden ara, 'insan mısın' de. İki aramada da sayı ve adres dene; sesli ajanların en çok kaybettiği yer orası."
Müşteri "telefonu robot açmasın" derse: "Robot açmıyor, siz açıyorsunuz. Ajan sadece siz açamadığınızda devreye giriyor. Bugün o aramalar boşa gidiyor, yarın randevuya dönecek. Ve ilk cümlede kendini tanıtacak, kimse aldatılmayacak."
Ajan randevu yazmıyorsa: "Ajan güzel konuşuyor ama randevu almıyor. Bu iyi ajan değil. Görev bölümünü yeniden yazıyorum; bilgi vermek değil saat önermek üzerine. Yeni metni destek adresine gönder, ekip ajana yükler."
Konuşmalar uzuyorsa: "Ortalama süre dört dakikayı geçmiş. Bu hem para hem randevu kaybı; uzayan konuşma kapanıyor. Soru sayısını üçten ikiye indirdim; yeni metni destek adresine gönder."
Müşteri aramanın kendisine bağlanmasını isterse: "Aramayı doğrudan size bağlamak bu hatta şimdilik yok. Ajan 'sizi birazdan arayacak' diyor, kayıt acil işaretiyle size bildirim olarak düşüyor. Parça kapsam dışı değil, sadece böyle çalışıyor." Bunu kurulum görüşmesinde söylersin ki müşteri canlıda şaşırmasın.

## 7. Ne yazar

Bilgi dosyasına: ajanın konuşma metninin sürümü ve tarihi, seçilen ses ve tanıma tarafı, müşterinin metin onayının tarihi, on aramanın sonucu, aktarmanın hangi biçimde çalıştığı, ortalama konuşma süresi, canlıdaki düzeltmeler ve tarihleri.
CRM'e: talep kanalı sesli ajan olan kayıtlar, arama sonucu, aktarma sayısı, ajanın yazdığı randevu sayısı.
Niş kartının Sahadan dolacak bölümüne: bu nişte arayanların en sık sorduğu soru, ajanın en sık takıldığı istek, en sık aktarma sebebi, ortalama konuşma süresi.
musteri-sistemini-kur'a ve destek adresine giden ayar listesi: karşılama cümlesi, soru sırası, aktarma eşiği, konuşma süresi sınırı, konuşma sonunda doldurulacak alanlar.

## 8. Yedek yol

- Hat gelmezse: ekip ajanı bağlamaz, metin hazır bekler. Parça ikinci dalgada ya da on beşinci günden sonra kurulur; gelmezse kapsam dışı kalır ve müşteriye yazılı bildirilir. Sebep sağlayıcıdaysa (başvuru reddi) kurulmadığı her ay ücret yüzde yirmi iner; sebep müşterideyse (vergi levhası gelmedi) inmez.
- Doğrudan bağlama şimdilik yok: ajan geri arama sözü verir, kayıt acil işaretiyle bildirime düşer. Parça kapsam dışı sayılmaz, sınırı müşteriye kurulum görüşmesinde söylenir.
- Türkçesi kötüyse: destek adresine yazarsın; ekip önce tanıma tarafını, sonra sesi değiştirir. İkisi de düzeltmiyorsa ajan yalnız karşılama ve aktarma yapan biçimde kurulur, randevuyu ajan yazmaz. Bu hâli müşteriye söylenir ve raporda randevu satırına sesli taraftan giren kayıt olmaz.
- Deneme temiz çıkmazsa: yönlendirme açılmaz, metnin kurallar bölümü düzeltilir, tekrar denenir.
- Ajan randevu yazmıyorsa: görev bölümü randevuya odaklanacak biçimde yeniden yazılır. İki düzeltmede de düzelmezse soru sayısı ikiye iner.
- Konuşmalar uzuyor ve maliyet artıyorsa: soru sayısı azaltılır, aktarma eşiği beş dakikadan dört dakikaya çekilir.
- Müşterinin takvimi bağlı değilse: ajan randevu saatini konuşup toplar, takvime yazmayı devri alacak kişi elle yapar. Bu durum yazili-asistani-kur'daki Google hesabı meselesiyle aynı; çözümü de orada yazılı.
- Müşteri kaydı istemiyorsa: destek adresine yazarsın, ekip konuşma kaydını kapatır, ajan çalışmaya devam eder. O zaman canlıdaki günlük okuma dökümden değil, kayda düşen özetten yapılır.

## 9. Sıradaki adım ve işaretler

Sıradaki: ikinci dalganın altı senaryoluk testi ve yönlendirmenin açılması (musteri-sistemini-kur).

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Denemede iki kez uydurma çıktı: cevap listesi eksik, doldurulur.
- Denemede sayı ya da adres iki kez yanlış yazıldı: destek adresine yazılır, tanıma tarafını ekip değiştirir.
- Ajan açıyor ama randevu yazmıyor: görev bölümü yeniden yazılır, takvim bağlantısını ekip kontrol eder.
- İlk hafta aktarma oranı yarıdan fazla (sağlık nişleri hariç): soru sırasının ilk sorusu değiştirilir.
- Ortalama konuşma süresi dört dakikayı geçti: soru sayısı üçten ikiye iner.
- Aynı soru üç konuşmada takıldı: cevap listesine eklenir.
- Müşteri ajanın bir cevabından şikâyet etti: o cevap kurallara yazılır, aynı gün düzeltilir. Bu düzeltme günde tek düzeltme kuralının dışındadır.
- Yönlendirme açık ama bir gün boyunca hiç arama düşmedi: yönlendirmenin üç durumu da açık mı diye bakılır.

Beş kural: boş sayfa yok (karşılama, sorular, aktarma cümleleri ve deneme listesi hazır gelir) · sessiz bitiş yok (deneme sonucu ve düzeltmeler bilgi dosyasına yazılır) · onay (ajanın metnini müşteri yazılı onaylar, yönlendirmeyi müşteri "açalım" dediğinde açarız) · sahadan güncelleme (takılan istek, aktarma sebebi ve konuşma süresi karta yazılır) · sormaz söyler (metni ve kuralları FounderOS üretir).
