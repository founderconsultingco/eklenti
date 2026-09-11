---
user-invocable: false
name: zor-konusmayi-yonet
description: "Öğrenci \"müşteri kızdı\", \"iptal etmek istiyor\", \"iş aksadı\" dediğinde."
---

# zor-konusmayi-yonet

## 1. Adı, rolü, pazarlamadaki karşılığı

Bir şey ters gittiğinde ne söyleyeceğini veren modül. Modül, FounderOS'un belli bir işi yapan parçasıdır.

Buradaki gün numaraları müşterinin ilk yirmi bir gününden sayılır, senin doksan gününden değil.

Neden bu iş var: sıfırdan başlayan biri kötü haber anında iki şeyden birini yapar. Ya kaybolur, mesaja cevap vermez, "elimde iyi bir şey olunca yazarım" der. Ya da savunmaya geçer, piyasayı ya da müşterinin kendi ekibini suçlar. İkisi de aynı yere çıkar: müşteri gider.

Kaybolmak neden bu kadar kötü: sessizlik boş bir alan değildir. Müşteri o alanı kendi kafasındaki en kötü ihtimalle doldurur. Parayı alıp kaçtığını düşünür. Sen üç gün susarken müşteri üç gün boyunca senden kötü bir şey bekler. Sonra iyi haberle dönsen bile ilişki zarar görmüştür.

Tek cümlelik kural: müşteri sorunu kaldırır, sürprizi kaldıramaz.

Kaçmanın asıl sebebi o an ne diyeceğini bilmemektir. Cümle hazırsa kaçmazsın. Aşağıdaki cümleler bunun için var.

Şunlar bu modülün işi değildir:
- Bozukluğu bulmak ve düzeltmek (sistemi-kontrol-et). Orası bozukluğu bulur, düzeltir ve düzeltme sırasını verir; burası o sırada söylenecek cümleyi verir.
- Raporu yazmak ve sayıları üretmek (aylik-raporu-hazirla). Rapor görüşmesinin sırası da orada.
- Aylık düzen, referans ve ayrılık adımları (musteriyi-elde-tut). Sıfırlama, kurtarma ve çıkış görüşmesi orada tanımlı; burası o görüşmelerin telefonla açılışını ve kriz anındaki cümleleri verir.
- İlk yirmi bir günün teslimatı (musteriyi-karsila ve diğerleri).
- Satış görüşmesindeki itirazlar (gorusmeyi-yonet). Orası aday, burası müşteri.

Pazarlamadaki karşılığı: müşteriyi kaybettiren şey sorunun kendisi değil, sorunun nasıl konuşulduğudur.

## 2. Ne zaman çalışır

- Müşteriden şikâyet ya da kırgınlık içeren bir mesaj geldiğinde.
- Sen bir hata yaptığında.
- Sistem durduğunda ya da bir parça çalışmadığında.
- Müşteri, satın almadığı bir işi istediğinde. Buna kapsam dışı istek diyoruz.
- Müşteri kendi işinden çıkan bir sonucu sana yüklediğinde.
- Müşterinin kendi müşterisi asistandan şikâyetçi olup doğrudan sana yazdığında ya da seni aradığında.
- Para konusu açıldığında: iade istendiğinde, ödeme geçmediğinde, ücret tartışmaya açıldığında.
- Yirmi birinci gün raporunda yazılan satırlar sıfır çıktığında.
- Sen teslim edemeyecek durumda olduğunda: hastalık, tatil, ailevi durum, başka bir iş.
- Müşterinin ya da senin verinin dışarı çıktığından şüphelendiğinde.
- Senin hakkında kötü söz çıktığında.

Bu modül kendiliğinden başlamaz. Sen ne olduğunu yazarsın, FounderOS "bu bir zor konuşma, şimdi şunu yapacaksın" der.

## 3. Ne okur

Bilgi dosyasından (İş Beyni'nin müşteriler bölümü; her müşteri için tuttuğun geniş dosya): kurulan parçalar, kapsam dışı kalanlar, verilen sözler, müşteriye ne bekleyeceğini söylediğin cümleler, işletmede senin konuştuğun tek kişi, hangi kanaldan yazıştığınız, geçmiş şikâyetler.
Onay belgesinden (para geçtikten sonra müşteriye gönderdiğin tek sayfa): ne satıldığı, "neyi yapmıyorum" başlığı, güvence ve şartı, sonuç cümlesi.
CRM'den (adayların ve müşterilerin kaydedildiği takip programı): son otuz günün sayıları, o müşteriyle olan bütün yazışma, randevu kayıtları, ödeme durumu.
Sözleşmeden: işi bitirme, iade ve haber verme maddeleri. FounderOS sözleşmeyi yorumlamaz, sadece hangi maddeye bakacağını söyler.
Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): o sektörde konuşulması yasak olan konular.

Güvence şudur: yirmi birinci günde rapor, yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz. Şartı var, o da onay belgesinde yazılı.

## 4. Ne sorar

Sormaz. Sen ona üç şey yazarsın, gerisini o söyler: ne olduğu, müşterinin kendi cümleleri, senin ne yaptığın.

Tek istisna var. Sen "bu konuşmayı yapamıyorum" dersen FounderOS zorlamaz. Cümleyi daha küçük bir parçaya böler ve önce onu yaptırır.

## 5. Ne yapar

### Her zor konuşmada değişmeyen dört kural

Bir. Sen söylersin, o bulmaz. Kötü haberi müşteri kendi fark ederse güven biter. Sen söylersen sorun kalır, güven kalır.

İki. İlk haber saatler içinde gider, ertesi güne kalmaz. Elinde çözüm olmasa bile aynı gün tek satır yazarsın: "Aldım, bakıyorum. Bugün akşama kadar döneceğim." Bu satır otuz saniye sürer ve müşterinin gerginliğini en çok düşüren şeydir. Sonra söylediğin saatte dönersin. Dönemiyorsan yine yazarsın.

Üç. İlk haber yazılı gider, asıl konuşma telefonla yapılır. Şu dört halde mutlaka arayacaksın: para tartışmaya döndüyse, müşteri kızgınsa, sistem bir günden uzun durduysa, yirmi birinci gün raporunda yazılan satırlar sıfır çıktıysa. Yazışmada ton okunmaz; kırgın duran bir cümle konuşurken küçülür.

Bu modül pencere tanımaz. Kurulum bloğunu, akşam bloğunu, hafta sonunu beklemezsin. İlk satır ne zaman öğrendiysen o zaman gider; işteysen bir dakikalık aranı kullanırsın. Telefonla yapılacak asıl konuşma kurulum bloğuna kalabilir, ama o zaman ilk satırda saatini yazarsın: "Bu akşam sekizde arayacağım." Sonra o saatte ararsın.

Dört. Sahiplenirsin. Bahane yok. Piyasa, sezon, müşterinin kendi ekibi, hava, tatil dönemi. Müşteri bunları duymak istemez, işi kimin götürdüğünü görmek ister. Sahiplenmek gerçeği değiştirmek demek değil: sayıyı olduğu gibi gösterirsin, sorumluluğu üstlenirsin.

### Kötü haber mesajının dört parçası

Sırayla, tek mesajda:
1. Ne oldu. Tek cümle, süslemeden.
2. Ne yapıyorum. Çözüm mesajın içinde olacak. Çözümsüz kötü haber verilmez.
3. Yeni tarih. Ne zaman düzelecek.
4. Bir sonraki haber ne zaman. "Çarşamba tekrar yazacağım" der ve çarşamba yazarsın.

Örnek: "Bu sabah takvim bağlantısı kopmuş. Yeniden bağladım, kopan sürede iki talep gelmiş, ikisini de elle randevuya yazdım. Yarın gün boyu takip edeceğim, akşam tekrar yazacağım."

Otuz saniyede yazılır, bir haftalık gerginliği önler.

### Sen hata yaptıysan

Hata yapacaksın. Bu işin ilk aylarında herkes yapıyor. Sorun hata değil, sonrası.

Düzeltmenin beş adımı sistemi-kontrol-et'te yazılı ve aynen geçerli. Bu modülün eklediği üç şey:

Birincisi ilk cümle. Aynı gün, tek cümle: "Bu benim hatam." Arkasına bahane eklenmez. Aynı cümle tekrar tekrar yazılmaz; tekrarlanan özür güven vermez, tersine işi kaldıramadığını düşündürür. Bir kere söylersin, sonra işe geçersin.

İkincisi telafi. Telafiyi önce emeğinle yaparsın. Kaybolan talepleri elle ararsın, kaçan randevuları elle yazarsın, gereken parçayı baştan kurarsın.

Üçüncüsü para. Para telafisi tek kapıdan geçer, o da güvencedir. Kendi kafandan ay bağışlamazsın, indirim teklif etmezsin. Fiyat düşürmek değeri düşürür ve bir daha geri gelmez. Tahsilatı bir dönem ertelemek gerekiyorsa yolu musteriyi-elde-tut'ta yazılı.

### Sistem durduysa

Sistem durunca müşteriye gelen talep karşılıksız kalır. En pahalıya patlayan bozukluk budur.

Sıra:
1. Fark ettiğin an müşteriye yazarsın. Düzeltmeyi beklemezsin. Sessizce düzeltmektense "şu an şu parça çalışmıyor, bakıyorum" demek daha değerlidir.
2. Aynı mesajda, duruş süresince gelen talepleri kimin karşılayacağını kararlaştırırsınız. Mesai saatiyse müşterinin kendi personeli karşılar. Mesai dışıysa duruş bitince hepsi elle aranır. "Kimse cevapsız kalmaz" diye söz vermezsin; tutamayacağın sözdür.
3. Düzeltirsin. Teknik yol sistemi-kontrol-et'te.
4. Duruş bitince kaybı sayarsın: kaç talep geldi, kaçına dönülemedi. Hepsini elle ararsın.
5. Aynı gün kapanış mesajı yazarsın: ne kadar sürdü, kaç talep etkilendi, hepsine ne yapıldı, tekrar olmaması için ne değişti.

Duruş anında söylenmeyecek tek cümle: "Bende bir sorun yok." Sorun sende olmasa bile müşterinin işinde bir sorun var.

### Müşteri kızgınsa

Kızgın mesaj çoğunlukla göründüğünden küçüktür. Yazıda insanlar abartır; aynı konu konuşurken küçülür. Onda dokuzunda gerçek şikâyet, mesajda görünenden çok daha ufak çıkar.

Tek şikâyet mesajı için büyük görüşme kurulmaz. Saatler içinde "Aldım, bakıyorum" yazarsın, öğrenip dönersin.

Şikâyet tekrarlanıyorsa ya da müşteri suçlamaya başladıysa iş sıfırlama görüşmesine gider. Görüşmenin dört adımı musteriyi-elde-tut'ta. Bu modülün eklediği üç şey:

Birincisi aramayı sen yaparsın ve konuyu sen açarsın: "Mesajlarını gördüm, bunu bir sonraki görüşmeye bırakmak istemedim. Şu an tam olarak seni ne rahatsız ediyor, baştan anlat."

İkincisi ilk beş dakikada tek işin dinlemek. Sözünü kesmezsin, açıklama yapmazsın, not alırsın. İnsan boşalana kadar konuşsun.

Üçüncüsü kızmanın kuralı. Müşteriyle aynı şeye kızmak işe yarar: "Ben de bu tabloyu kabul etmiyorum." Ama kızmış numarası yapmak yaramaz. Tablodan memnunsan bunu söylemezsin, yalancı çıkarsın ve o daha pahalıya patlar.

Yapılmayacak tek şey: mesajı görmezden gelip geçer diye beklemek.

**Kızgın telefon geldiyse.** En zoru budur, çünkü hazırlanacak vaktin yok. İki cümleyi duyacaksın: "sistem çalışmıyor" ve "para boşa gitti". İkisi de aynı yerden geliyor: adam bir şey ödedi ve karşılığını göremiyor.

İlk cümlen şudur, başka bir şey değil:

"İyi ki aradın. Baştan anlat, sözünü kesmeyeceğim."

Sonra susarsın. Beş dakika. Not alırsın.

Bu konuşmada yapmayacakların:
- Savunma yapmak. "Aslında sistem çalışıyor" cümlesi konuşmayı bitirir, çünkü adam çalışmadığını söylüyor ve sen ona yalan söylediğini söylemiş oluyorsun.
- Sözünü kesmek. Ne kadar yanlış konuşursa konuşsun, bitirmesini beklersin.
- Ezberden rakam okumak. Kızgın adamın kulağı rakam duymuyor. Rakam bu telefonda okunmaz.
- Suçu paylaştırmak. "Sen de şunu yapmadın" cümlesi haklı olsa bile bugün söylenmez.
- Kızgınken söz vermek. Kurtulmak için verilen tarih tutmaz ve ikinci krizi büyütür.
- Telefonu kapatmak ya da "sonra konuşalım" demek.

Kızgınlık geçtikten sonra tek cümleyle sahiplenirsin: "Bu tabloyu ben de kabul etmiyorum. Bugün bakıyorum, akşam sana yazıyorum." Sonra kapatırsın.

Hangi rakam gösterilir: aynı gün, yazıyla, üç satır. Sonuç cümlesinin üç sayısı, yani sisteme gelen talep, sistemin yazdığı randevu, eski müşteri listesinde ulaşılan kişi. Yanına da kurulan ve kurulamayan parçaların listesi gider. Boş satır varsa sebebiyle yazılır. Bu rakamlar tartışmak için değil, ikinizin aynı tabloya bakması için. Rakam telefonda değil yazıyla gider, çünkü yazılı rakam sakin okunur.

Rakam gerçekten kötüyse gizlemezsin. "Sistem çalışmıyor" diyen adam haklıysa ona haklı olduğunu sen söylersin; o zaman konuşma kavgadan çıkıp işe döner.

Para iadesi ne zaman konuşulur: bu telefonda değil. Adam ilk konuşmada "paramı geri ver" dese bile cevabın şu: "Parayı da konuşacağız, ama önce ne olduğunu görmem lazım. Bugün bakıp yarın sana rakamlarla dönüyorum." Sonra rakamlar önündeyken tek soruya cevap verirsin: müşteri gerçekten hiçbir şey aldı mı, almadı mı. Cevabı ve sonrasını bu dosyada "İade istiyorsa" bölümü söylüyor. İade konuşması ayrı bir telefonla yapılır, kızgın konuşmanın devamı olarak değil.

Şunu bil: bu konuşmayı düzgün yapan kişi çoğu zaman o gün en sadık müşterisini kazanır. Dört müşteriye çıkmanın en ucuz yolu, elindeki birinciyi kaybetmemektir.

### Müşterinin kendi müşterisi sana yazarsa ya da seni ararsa

Olur. İşletmenin bir müşterisi asistandan rahatsız olur ve seni bulur: numaranı bir yerden görmüştür, demo hattına düşmüştür, sitenden ulaşmıştır. Genelde cümle şudur: "Bana robot cevap verdi", "Yazdım, kimse dönmedi", "Randevumu yanlış yazmışsınız."

Kural tek: sen o kişinin muhatabı değilsin. O kişi senin müşterin değil, işletmenin müşterisi. Cevabı işletme verir, sen vermezsin. Araya girersen işletmenin ağzından konuşmuş olursun; sağlık nişinde bu doğrudan müşteriye ceza yazdırır.

Sen ne yaparsın: tek mesaj, kısa, tartışmasız. Telefonda da aynı cümleyi kurar ve konuşmayı orada bitirirsin.

"Merhaba. Ben [iş adı]'nın sistem tarafına bakıyorum, randevu ve kayıtları ben açamıyorum. Yazdıklarınızı bugün [iş adı]'na iletiyorum, size oradan dönecekler."

Söylemeyeceklerin: fiyat, randevu, tedavi, kimin ne zaman geldiği, işletmenin içinden hiçbir bilgi. Özür de dilemezsin, çünkü senin adına dilenecek bir özür yok ve işletmenin adına özür dileme yetkin de yok. Kişi bağırıyorsa ya da hakaret ediyorsa tartışmazsın, aynı cümleyi bir kez daha yazıp bitirirsin.

Sonra aynı gün müşteriye yazarsın. Üç şey: ne oldu, ne cevap verdim, sana ne düşüyor.

"Bugün senin bir müşterin bana yazdı, asistanın cevabından memnun kalmamış. Ona 'sizi işletmeye iletiyorum' dedim, başka bir şey söylemedim. Bilgilerini aşağıya bırakıyorum, dönüşü senin yapman lazım. Asistan tarafında düzeltilecek bir şey varsa bugün düzeltiyorum."

Kişinin adını ve numarasını müşteriye iletirsin ama kendi tarafında saklamazsın. Bilgi dosyasına yazılan şey kişi değil, olaydır: tarih, hangi kanaldan geldiği, şikâyetin konusu tek cümleyle, asistanda bir düzeltme yapıldıysa ne yapıldığı.

Şikâyet asistanın davranışındaysa o düzeltme aynı gün yapılır; haftada tek düzeltme kuralının istisnası budur. Aynı şikâyet üç ayrı kişiden geldiyse artık tek bir olay değil, asistanın ayarı yanlış demektir ve iş sistemi-kontrol-et'e geçer.

Bir şeyi de yapmazsın: bunu müşteriden saklamak. "Küçük bir şeydi, ben hallettim" diye geçiştirilen şikâyet, bir hafta sonra müşterinin kulağına başkasından gider.

### Müşteri kendi işinden çıkan sonucu sana yüklüyorsa

En sık duyacağın cümle: "Randevular geliyor ama iş çıkmıyor, sen ne yapıyorsun."

Burada iki hata var: bahaneye geçmek, ya da her şeyi üstlenip gerçeği eğmek. İkisi de yanlış.

Doğru sıra: önce sahiplen, sonra sayıyı göster, sonra ikinizin ne yapacağını yaz.

Sayı zinciri dört halkadır ve nerede koptuğunu gösterir:
1. Sisteme talep geldi mi.
2. Talep randevuya yazıldı mı.
3. Randevuya gelindi mi.
4. Gelen işe döndü mü.

İlk iki halka senin işin. Son iki halka müşterinin işi. Bunu suçlar gibi değil, aynı tabloya birlikte bakar gibi konuşursun: "Talep ve randevu tarafı çalışıyor, rakamlar burada. Kopma üçüncü halkada görünüyor. Bunu birlikte çözelim; ben randevu yazabilirim ama koltuğa oturtamam."

Randevu verenlerin kaçının gerçekten geldiğine bakarsın. Ölçüt yüzde yetmiş: altındaysa sorun randevuda değil hatırlatmadadır, o senin işindir ve düzeltirsin. Üstündeyse ve yine de iş çıkmıyorsa konu satıştadır, o müşterinin işidir.

Bir şart var: bu oranı ancak yeterli randevu birikince kurarsın. Beş randevuda oran konuşulmaz, sayı konuşulur. Az sayıda oran yanıltır ve elinde ölçü yokken suç dağıtmak ilişkiyi bitirir.

Bunun asıl sebebi neredeyse her zaman satışta verilen sözdür. Ayda otuz beş talep alan bir müşteri, altmış sözü verilmişse mutsuzdur; yirmi beş beklemesi söylenmişse memnundur. Sonuç aynı, beklenti farklı. Satışta sayı sözü verilmemesinin sebebi tam olarak bu.

### Kapsam dışı bir şey istiyorsa

Müşteri zamanla yeni şeyler ister. Bu normaldir; memnun olmayan müşteri zaten bir şey istemez. Tehlike şu: istekler tek tek küçük görünür, toplandığında sen satmadığın bir işi yapıyor olursun.

Ayrım nettir:
- Küçük istek: mesaj metninde değişiklik, çalışma saati değişikliği, asistanın cevap listesine yeni bir soru, randevu süresinin değişmesi. Bunlar yapılır, aylık ücretin içindedir.
- Yeni parça: yeni kanal, reklam, ikinci bir asistan, web sitesi, başka bir yazılıma bağlanma, yeni akış. Akış, bir olay olunca kendiliğinden çalışan adım zinciridir. Bunlar kapsam dışıdır, ayrı iştir, ayrı ücreti vardır.

Asistan tarafındaki küçük istekler haftada tek düzeltme kuralına uyar: bir haftada asistanın kurallarında ve cevap listesinde tek düzeltme yapılır. Tek istisna, müşteri asistanın bir cevabından şikâyet ettiyse o aynı gün düzeltilir. Çalışma saati ve randevu süresi bu kuralın dışındadır, istendiği gün yapılır.

Kapsam dışı isteğe verilecek cevabın üç parçası var ve "hayır" kelimesi geçmez:
1. İsteği ciddiye al: "İyi fikir, bunu yapabiliriz."
2. Sınırı belgeye dayandır: "Bu, şu an anlaştığımız paketin içinde değil. Onay belgesinde neyi yaptığım ve neyi yapmadığım yazıyor."
3. Yolu göster: "Ayrı bir iş olarak fiyatlayıp yazayım, bakarsın."

Sınırı kendi ağzından değil belgeden söylemek ikinizi de rahatlatır. Kavga çıkmaz, çünkü ikiniz de aynı kâğıda bakıyorsunuz.

Zaman kuralı da var: yeni parça en erken ikinci ayda açılır. Büyüme şartı iki maddedir. Görüşmede satılan tam sistem, yani Kademe 2, ilk müşteride sorunsuz teslim edilmiş olacak ve yirmi birinci gün raporu çıkmış olacak. Bu şart sağlanmadan yeni parça satılmaz, müşteri istese bile. Yarım kalan bir işin üstüne ikinci iş koyarsan ikisi birden batar.

### Yirmi birinci günde sonuç çıkmadıysa

Rapor görüşmesinin beş adımlık sırası aylik-raporu-hazirla'da ve aynen uygulanır. Sıranın birinci maddesi kötü haberdir; kötü haberi sona saklamak en yaygın hatadır, çünkü müşteri iyi haberleri dinlerken kötüyü bekler ve hiçbirini duymaz. Dördüncü maddeyi de atlamazsın: kazanan bir şey varsa kutlarsın. Sadece sorun konuşan biri, konuşulacak sorun sayılır.

Bu modülün eklediği tek şey ücret cümlesidir ve onu sen söylersin, müşteri hatırlatmadan:

"Yazılan satırların hepsi sıfır. İkinci ay ücretini almıyorum."

Dikkat edilecek ayrım: kurulamayan bir parçanın satırı boş kalır ve sayılmaz. Boş satır güvenceyi tetiklemez. Güvenceyi tetikleyen şey, yazılan satırların hepsinin sıfır olmasıdır. Kapsam dışı kaldığı için tutmayan bir parça yüzünden ücretten vazgeçmezsin; o durumda ödeme normal çekilir ve sen bunu görüşmede açıkça söylersin.

Ücretsiz ay açık uçlu değildir. O ayın sonunda üç yol var ve üçü de musteriyi-elde-tut'ta yazılı: kapsamı daraltıp devam, normal ücretle devam, ya da sözleşmedeki yazılı bildirimle ayrılma. Bunu ücretsiz ay başlarken söylersin, sonunda değil.

İkinci rapor da yazılan satırların hepsini sıfır gösterdiyse durum değişir. Artık tek bir kötü ay değil, çalışmayan bir sistem var. O zaman ya sistem baştan gözden geçirilir ya da iş dürüstçe bitirilir. Üçüncü kez aynı tabloyu göstermek ikinize de zarar verir.

### İade istiyorsa

Karar tek soruya bağlı: müşteri gerçekten hiçbir şey aldı mı, almadı mı.

Hiçbir şey almadıysa iade edersin. Tartışmazsın, madde aramazsın, geciktirmezsin. İade başlangıçta alınan kurulum ücretiyle sınırlıdır. Küçük bir şehirde ya da tek bir sektörde ismin hızlı yayılır ve bir iade, çıkacak sesten ucuzdur.

İş çıktıysa ve teknik bir gerekçeyle iade istiyorsa sözleşmedeki madde tam bunun için vardır. Sakin, yazılı ve tek seferde açıklarsın.

İki ek kural:
- Temiz bir iade, karta itiraz edilmesinden her zaman iyidir. Müşteri bankasına başvurup ödemeyi geri çevirtirse parayı senin adına tahsil eden şirket seni riskli görür ve o hesabı kapatabilir. Hesap kapanırsa hiçbir müşteriden para alamazsın. Bu, bir iadeden çok daha pahalıdır.
- İade konuşması yazışmayla yürütülmez. Telefon edersin.

Para konusunda tehdit dili kullanmazsın ve sözleşmeyi silah gibi sallamazsın. Madde vardır, yeri gelince okunur, o kadar.

### Ödeme geçmediyse

Kart geçmemesi çoğunlukla kötü niyet değildir: limit, kartın süresi, bankanın bloke etmesi. İlk mesaj bu varsayımla yazılır.

Sıra musteriyi-elde-tut'takiyle aynıdır ve şöyle işler:
1. Aynı gün tek mesaj, suçlama yok: "Bu sabahki ödeme geçmemiş, muhtemelen limit ya da kart süresi. Yeni ödeme linkini gönderiyorum, iki dakika sürer." Linki CRM'de KENDİ hesabından üretirsin, müşterinin alt hesabından değil. Müşterinin alt hesabından üretilen link müşterinin kendi ödeme hesabına para toplar; senin tahsilatın oradan geçmez.
2. Üç gün içinde tek yazılı hatırlatma.
3. Hâlâ geçmediyse telefon edersin. Üçüncü kez yazmazsın; üst üste yazılı mesaj takip gibi durur ve ilişkiyi bozar.
4. Hizmeti durdurmadan önce yazılı bildirim gider. Bildirimin süresi ve yolu sözleşme şablonunda yazar; gün sayısını kendin uydurmazsın, oradan okursun.

Bildirim süresi dolduğunda duran şeyler: yeni kurulum işleri, yeni toplu gönderimler ve haftalık bakım. Durmayan şeyler: müşterinin kendi müşterilerine giden hiçbir şey. Randevu hatırlatmaları, cevapsız aramaya dönüş ve asistanın cevapları çalışmaya devam eder. Sen emeğini durdurursun, müşterinin işini durdurmazsın. İki sebebi var. Birincisi, doğru olan bu. İkincisi, müşterinin müşterisinin bunda hiçbir suçu yok.

Bildirim gönderirken kullanacağın metin: "Şu tarihten bu yana ödeme geçmedi ve konuşamadık. Sözleşmemizdeki maddeye göre bugünden itibaren yeni kurulum işlerini, yeni gönderimleri ve haftalık bakımı durduruyorum. Randevu hatırlatmalarınız ve asistanınız çalışmaya devam ediyor. Ödeme geçtiği gün her şey kaldığı yerden devam eder."

Bunu baştan önlemenin yolu belli: kart görüşmede alınır, tahsilat kendiliğinden çekilir, ilk iki ayda üç bildirim gider. Üç gün önce, bir gece önce, sabahı. Tanımadığı bir çekimi ekranda gören müşteri o gün senden şüphelenmeye başlar.

### Müşteri kayboldu ve tahsilat yaklaşıyorsa

İki mesaja cevap yoksa yazmayı bırakır, telefon edersin. Telefonu da açmıyorsa tahsilat gününden önce tek bir yazılı bildirim gönderirsin: ödemenin ne zaman çekileceği ve bir sorun varsa bugün konuşmak istediğin.

Sessiz müşteriden habersiz para çekmek en hızlı iade sebebidir. Önce konuşma, sonra tahsilat.

### Sen teslim edemeyecek durumdaysan

Hastalanırsın. Ailende bir şey olur. Sınavın çıkar. Tatile gidersin. Bu normaldir ve sistem buna göre kuruldu: kurulan sistem sen olmadan da çalışır. Duran şey sistem değil, senin bakımın ve raporundur.

Süreye göre üç durum:
- Bir iki gün. Müşteriye haber vermene gerek yok. Bakım gününü kaydırır, ertesi gün yaparsın.
- Üç ila yedi gün. Önceden yazarsın: hangi günler yoksun, hangi gün döneceksin, acil bir şey olursa nasıl ulaşacak. Bakım gününü kaydırırsın ve döndüğün gün yaparsın.
- Yedi günden uzun. Bu bir kriz. Telefon edersin, süreyi söylersin, sistemin çalışmaya devam ettiğini anlatırsın, bakımı hangi gün yapacağını söylersin.

Planlı tatili haftalık görüşmede önceden söylersin ve bakımı öne alırsın.

Fiyat değişmez, indirim teklif etmezsin. Kaçan bakım günü döndüğünde telafi edilir ve raporda gösterilir. Yokluğun bir tahsilat dönemini tamamen boş bıraktıysa telafi yolu musteriyi-elde-tut'ta yazılı, oradan seçersin.

Yapmayacağın tek şey: kaybolmak. Hasta olduğunu söylemek zayıflık değil; haber vermeden yok olmak işin sonu.

Kalıcı olarak devam edemeyeceksen iş şöyle kapanır: müşteriye telefonla sen söylersin, ödediği ayın kalan kısmının ücreti iade edilir, kişi listesi dışa aktarılıp verilir, izinler kaldırılır, sendeki kopya silinir. Neyin müşteride kaldığı ve neyin kalmadığı musteriyi-elde-tut'ta yazılı; akışlar, şablonlar ve asistanın cevap listesi senin çalışma hesabında olduğu için devri yok, bunu ayrılırken açıkça söylersin. Kalan maddeler sözleşmeden okunur.

### Verinin dışarı çıktığından şüphelenirsen

Müşterinin listesi, yazışmaları ya da hesapları senin elinden dışarı çıkmış olabilir mi diye şüphelendiğin an bu bir hukuk konusudur.

Aynı gün üç şey:
1. Ne olduğunu yazılı çıkarırsın: hangi bilgi, kaç kişi, ne zaman, nasıl.
2. Müşteriye yazılı haber verirsin. Bu adım ertelenmez.
3. Avukatına sorarsın.

Bunu tek başına yönetmeye çalışma. Kanunda bir bildirim süresi ve bildirimin yapılacağı kurum var. Bu iş modelinde bildirimin senin görevin mi müşterinin görevi mi olduğunu ve süreyi avukatına soracaksın.

Avukatın yoksa ilk müşteriden önce bulacaksın. Baroya kayıtlı, kişisel verilerin korunması konusuna bakan bir avukatla tek seferlik yarım saatlik görüşme yeter. Aynı görüşmede sözleşme şablonunu da konuşursun. Soracağın cümle şu: "Müşterimin müşteri listesini benim çalışma hesabımda tutuyorum. Bu liste dışarı çıkarsa bildirimi ben mi yapacağım, müşteri mi? Süresi ne?"

### Senin hakkında kötü söz çıkarsa

Kural: herkesin gördüğü yerde tartışmazsın.

Yapılacak: kısa ve savunmasız tek cevap, sonra konuşmayı özele taşıma. "Yazdıklarınızı gördüm, ciddiye alıyorum. Bugün size ulaşacağım, konuşalım." Sonra ulaşırsın.

Yapılmayacak: müşterinin adını, rakamlarını, yazışmalarını ya da işinin ayrıntısını herkesin gördüğü yere yazmak. Haklı olsan bile bunu yaptığın an kaybedersin, ayrıca müşterinin bilgisini yaymak hukuki sorun doğurur.

Kötü sözün büyük kısmı sonuçtan değil sessizlikten çıkar. Yukarıdaki dört kurala uyarsan buraya çok az ihtiyacın olur.

### Müşteriyi sen bırakmak istersen

Bu eşik yüksektir. Zor müşteri kötü müşteri değildir; çoğu zaman gergin ve ne aldığını tam anlamamış müşteridir. Sıfırlama görüşmesinden sonra genellikle en sadık müşteriye dönüşür. Yenisini bulmak, elindekini düzeltmekten her zaman daha pahalıdır.

İki halde bırakılır:
1. Senden yasa dışı ya da yasak bir şey isteniyorsa. Sahte yorum, izinsiz listeye mesaj, sağlık nişinde yasak tanıtım. Bir kere açıklarsın; ısrar ederse iş biter.
2. Kişisel saygısızlık ya da tehdit varsa.

Ödeme sorunu bu listede yok, çünkü onun kendi sırası var ve zaten çıkış görüşmesine kadar gidiyor.

"Bu müşteriyle uğraşmak istemiyorum" bir sebep değildir, ilk müşterilerde hiç değildir.

Bırakma yolu çıkış görüşmesidir, ortadan kaybolmak değil. Adımları musteriyi-elde-tut'ta.

### Türkiye tarafı

Kriz büyürse hukuk devreye girer. Bilmen gerekenler aşağıda. Hiçbiri kesin karar değil; hepsini avukatına soracaksın. Aşağıdaki madde bilgileri hukuk yayınlarından derlendi, kanunun resmî metniyle karşılaştırılmadı; avukatın kontrol edecek.

İşi bitirme. Kanunda iki farklı sözleşme türünün kuralı var ve sonuçları farklı. Birinde taraflar sözleşmeyi her zaman tek taraflı bitirebiliyor, ama uygun olmayan bir zamanda bitiren, diğerinin zararını karşılamak zorunda kalıyor. Diğerinde iş sahibi işi yarıda kesebiliyor ama yapılan kısmın bedelini ve karşı tarafın zararını ödemek zorunda. Aylık ücretle satılan bir kurulum ve bakım işi bu ikisinden hangisine girer, bunu sözleşmeni yazan avukat belirleyecek. Sözleşme yazılırken soracağın ilk soru budur.

Geç ödeme. İşletmeler arasındaki mal ve hizmet alımlarında şu kural var: sözleşmede ödeme süresi yazmıyorsa, fatura müşteriye ulaştıktan otuz gün sonra müşteri kendiliğinden gecikmiş sayılır. Ayrıca yazılı uyarı göndermene gerek kalmaz. Sözleşmeyle kararlaştırılabilecek süre kural olarak altmış günle sınırlı, ama kanun birkaç istisna sayıyor; hangisinin sana uyduğunu avukatın söyler. Sözleşmede gecikme faizi oranı yazmıyorsa Merkez Bankası'nın her yıl ocak ayında ilan ettiği oran uygulanıyor.

Anlaşmazlık büyürse. Tüketici hakem heyetlerine yalnız tüketiciler başvurabiliyor; senin müşterin bir işletme olduğu için o yol sana kapalı. İşletmeler arasındaki para alacağı ve tazminat taleplerinde ise mahkemeye gitmeden önce arabulucuya başvurmak zorunlu. Arabulucu, mahkemeye gitmeden iki tarafı masaya oturtan resmî görevlidir. Parasal bir alt sınır yok; süreç en geç altı haftada biter, zorunlu hallerde en fazla iki hafta uzayabilir. Yani anlaşmazlık büyürse ilk durak mahkeme değil arabuluculuk.

Nişe özel yasak konular. Sağlık nişlerinde müşterinin adına giden mesajlarda söylenemeyecek şeyler var: fiyat, kampanya, indirim, "kesin sonuç" ve "en iyi" gibi iddialar, hasta yorumu ve öncesi sonrası görsel. Kriz anında müşteri adına bir şey yazacaksan, örneğin kötü bir yoruma cevap, aynı sınır orada da geçerli. Ceza müşteriye kesiliyor, o yüzden metni müşteri onaylamadan hiçbir şey yayınlanmaz. Yasak konuların listesi niş kartının yasal sınırlar bölümündedir.

### Konuşamadığın an

O anda hissedeceğin şey belli: mideye oturan bir ağırlık, telefonu eline almamak için bulduğun küçük işler, "bir saat sonra yazarım" diye ertelemek. Bu herkeste var. Sebebi ne olursa olsun sonuç aynı: yazmıyorsun.

Şunu gör: müşteri zaten tedirgin. Sen susarak onu korumuyorsun, kendini koruyorsun. O koruma bir gün sürüyor, sonra iki katı pahalıya çıkıyor. O an istediği şeyi ona verebilecek tek kişi sensin.

Üç pratik şey:
1. Konuşmayı küçült. Tamamını halletmeye çalışma. İlk adım tek satır: "Aldım, bakıyorum." Bu kadarını her zaman yapabilirsin.
2. Bunu kendine mal etme. Ortada çözülecek bir iş var, senin hakkında verilmiş bir hüküm değil. Merak ederek bak: burada tam olarak ne bozuldu.
3. Erteleme. Telefonu eline al ve tuşa bas. Beklediğin her dakika gerginliği artırıyor, azaltmıyor.

İçindeki huzursuzluk çoğunlukla yapman gerektiğini bilip yapmadığın işten geliyor. Mesajı yazdığın an hafifler.

Bir şey daha: bunu on kere yaparsan on birincisi ilkinin yarısı kadar zor olur. Her zor konuşma bilgi dosyasına bir satır düşer; üçüncüsünde cümleyi FounderOS'tan istemeden kendin kurmaya başlarsın.

## 6. Ne söyler

Şikâyet mesajı gelince: "Bunu bugün kapatacağız. Önce tek satır yaz: aldım, bakıyorum, akşama dönerim. Otuz saniye sürer, gerginliğin yarısını alır. Sonra oturup ne olduğuna bakacağız."
Kaçmak istediğinde: "Şu an yazmamak için sebep arıyorsun. Hiçbiri gerçek değil. Müşteri zaten tedirgin; senin susman onu korumuyor, yarın vereceğin haberi pahalılaştırıyor. Tek satır, otuz saniye."
Hata yapınca: "Hata yaptın, olur. Şimdi sırayla: bu benim hatam de, bugün düzelt, sade anlat, bir daha olmaması için ne değiştiğini söyle, kaybı kendin kapat. Bahane kurma; bahane hatadan çok müşteri kaybettirir."
Kızgın mesaj gelince: "Yazışma, ara. Yazıda insanlar abartır, konuşurken konu küçülür. Aradığında ilk beş dakika sadece dinleyeceksin. Savunma yapma, not al."
Kızgın telefon gelince: "Tek cümle: iyi ki aradın, baştan anlat, sözünü kesmeyeceğim. Sonra sus. Rakam okuma, savunma yapma, söz verme. Kızgınlık geçince 'bu tabloyu ben de kabul etmiyorum, akşam yazıyorum' de ve kapat. Rakamı akşam yazıyla gönder. Para lafı açılırsa 'onu da konuşacağız ama önce bakacağım' de; iade konuşması ayrı telefondur."
Müşterinin müşterisi sana yazınca: "Ona cevap veren sen değilsin. Tek cümle yaz: sistem tarafına bakıyorum, konuyu bugün işletmeye iletiyorum. Fiyat, randevu, tedavi konuşma. Sonra aynı gün müşterine yaz; sakladığın şikâyet bir hafta sonra başkasından ona gider."
Kapsam dışı istek gelince: "Hayır deme, sınırı söyle. Onay belgesinde neyi yaptığın yazıyor. 'İyi fikir, bu paketin içinde değil, ayrı bir iş olarak fiyatlayayım' de. Aynı kâğıda bakan iki kişi kavga etmez."
Sonuç çıkmayınca: "Kötü haberle başla, raporu açmadan söyle. Sona saklarsan müşteri iyi haberlerin hiçbirini duymaz. Sonra üç satırı oku, sıfır olan satırı sen göster."
İade isteyince: "Tek soru: gerçekten hiçbir şey aldı mı. Almadıysa iade et, tartışma. Bir iade ucuz; karta itiraz edilirse ödeme hesabın kapanır ve dört müşterinin parasını da alamazsın."
Ödeme geçmeyince: "Kart geçmemesi kötü niyet değil, çoğu zaman limit. İlk mesajı buna göre yaz. Suçlayıcı yazarsan bir daha kart vermez. Üç gün içinde tek hatırlatma, sonra ara."
Sen teslim edemeyeceksen: "Söyle. Hasta olmak zayıflık değil; haber vermeden kaybolmak işin sonu. Sistem sen olmadan da çalışıyor, duran şey senin bakımın. Yedi günü geçiyorsa telefon et."

## 7. Ne yazar

Bilgi dosyasına: krizin tarihi ve ne olduğu, müşterinin kendi cümleleri, kimin aradığı, konuşmada verilen sözler ve tarihleri, telafi olarak ne yapıldığı, sonuç, tekrar olmaması için ne değiştiği. İşletmenin müşterisinden gelen şikâyette olay yazılır, kişi yazılmaz: tarih, kanal, şikâyetin konusu tek cümleyle, asistanda ne düzeltildiği. Kişinin adı ve numarası müşteriye iletilir, sende kalmaz.
CRM'e: konuşmayı yaptığın ve tarihi. Açık kalan bir söz varsa onu takvime iş olarak yazarsın.
Niş kartının Sahadan dolacak bölümüne: bu nişte tekrar eden kriz tipi ve o krizde işe yarayan cümle.
Bilgi dosyasının ayrı bir başlığına: müşterinin istediği ama kapsam dışı kalan işler. Aynı istek üç ayrı müşteriden geldiyse bunu degisiklige-karar-ver'e taşırsın; tekliflerin değişip değişmeyeceğine orası karar verir, sen kendi başına teklif metnini değiştirmezsin.

Telefonda ne söz verdiysen aynı gün tek mesajla yazarsın. Yazılı olmayan sözün kanıtı olmaz.

## 8. Yedek yol

- Müşteri telefonu açmıyorsa: tek yazılı mesaj, ne olduğu ve ne zaman arayacağın. Sonra söylediğin saatte tekrar ararsın.
- Kızgın telefon işteyken geldi ve konuşamıyorsan: açar ve tek cümle söylersin: "Şu an konuşamıyorum, saat şu kadarda seni arıyorum." Sonra o saatte ararsın. Açmamak yok.
- İşletmenin müşterisi ısrarla sana yazmaya devam ediyorsa: aynı cümleyi bir kez daha yazar, sonra cevap vermezsin ve durumu müşteriye bildirirsin. Tartışmaya girmezsin.
- Konuşma büyüyor ve sen kontrolü kaybediyorsan: konuşmayı bitirirsin. "Bunu şu an çözemeyeceğiz. Bugün bakıp yarın saat şu kadarda döneceğim." Kızgın anda söz vermezsin.
- Müşteri tehdit ediyorsa ya da hakaret ediyorsa: konuşmayı orada bitirir, yazılı olarak devam edersin. Ekran görüntüsünü alır, CRM'de o müşterinin notuna tarihiyle yazarsın.
- Sözleşme maddesi tartışılıyorsa: yorum yapmazsın. "Sözleşmedeki maddeye bakıp size yazılı döneceğim" der, avukatına sorarsın.
- Hangi cümleyi kuracağını bilemiyorsan: FounderOS'a ne olduğunu üç satırla yazarsın, cümleyi o verir. Kendi kafandan yazıp göndermezsin; kriz anında yazılan mesaj çoğunlukla yanlış tonda çıkar.

## 9. Sıradaki adım ve işaretler

Sıradaki: kriz kapandıysa haftalık bakım (sistemi-kontrol-et) ve aylık düzen (musteriyi-elde-tut). Müşteri ayrılmak istiyorsa çıkış görüşmesi (musteriyi-elde-tut). Sistem yanlış kurulduysa musteri-sistemini-kur.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Sen bir müşteriden şikâyet geldiğini yazdın: bu modül devreye girer, ne yazacağın verilir.
- Şikâyet geldiğini yazdın ve o gün senden cevap gittiğini bildirmedin: akşam bloğunda sorulur.
- Bir söz verdin ve tarihi geldi: hatırlatılır.
- Aynı müşteride üçüncü kriz: sistem gözden geçirmeye alınır, iş musteri-sistemini-kur'a döner.
- Müşterinin kendi müşterisi sana yazdı: aynı gün müşteriye iletildiği doğrulanır.
- Aynı asistan şikâyeti üç ayrı kişiden geldi: asistanın ayarı gözden geçirilir, iş sistemi-kontrol-et'e gider.
- Müşteri kızgın aradı: o gün rakamlar yazıyla gönderilir, gönderilmediyse akşam bloğunda sorulur.
- Ödeme geçmedi: dört adımlı sıra başlar.
- İki mesaja cevap gelmedi ve tahsilat yaklaşıyor: önce konuşma, sonra tahsilat.
- Yirmi birinci gün raporunda yazılan satırların hepsi sıfır: görüşme telefonla değil, yüz yüze ya da görüntülü yapılır.
- Bir müşteride açık kriz var ve üç gündür ondan hiç söz etmedin: sorulur.

Beş kural: boş sayfa yok (kriz anında kuracağın cümle hazır gelir) · sessiz bitiş yok (her zor konuşma bir kayıtla ve tarihli bir sözle biter) · onay (müşteriye giden her mesaj senin elinden çıkar) · sahadan güncelleme (krizde işe yarayan cümle niş kartına yazılır) · sormaz söyler (hangi konuşmanın yapılacağını FounderOS söyler).
