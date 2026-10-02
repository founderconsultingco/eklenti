---
user-invocable: false
name: onay-belgesini-hazirla
description: "Öğrenci \"evet dedi\", \"kabul etti\", \"parayı gönderecek\" dediğinde kapanış mesajı ve onay belgesi. Ödeme yolu ve sözleşme üçüncü blokta kurulur."
---

# onay-belgesini-hazirla

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç. Panel: modül açılınca, ilk işinden önce `odak_yaz` `basladi` gider (`is`: "onay-belgesini-hazirla"); öğrenciden seçim ya da bilgi beklerken `bekliyor`, iş bitince `bitti`. Aşağıda kendi odak satırı varsa o geçer, ne zaman gönderilmediği dahil (çekirdek, "Panel: odak ve tur").

## 1. Adı, rolü, pazarlamadaki karşılığı

Kapanış anının ve kapanıştan sonraki ilk saatin belgelerini hazırlayan modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Üç şey üretir:

1. Ödemenin iki yolu, ikisi de hazır durur ve ikisi de birinci sınıftır. Birincisi ödeme linkleri: biri kurulum ücreti için tek seferlik, biri aylık ücret için düzenli ödeme. Düzenli ödeme, müşterinin kartından her ay kendiliğinden çekilen ödemedir. Sağlayıcın ikisini tek linkte topluyorsa tek link olur. İkincisi havale mesajı: hesap bilgisi, tutar ve açıklama satırı tek mesajda. Şirketin yokken de para alabilirsin.
2. Sözleşme. Hazır gelir, FounderOS doldurur, sen gönderirsin; her müşteride sadece adı ve rakamı değişir. CRM açıksa belge bölümünden imzalanır; CRM açılmadıysa PDF WhatsApp'tan gider, müşteri kabulünü aynı sohbete yazar (aşağıda).
3. Onay belgesi. Para hesabına geçtikten sonra müşteriye giden tek sayfa.

Neden var: sözlü "evet" ile paranın hesabına geçmesi arasındaki her dakika kayıp riskidir. Bir de şu var: insan bir şey satın aldıktan sonra pişmanlık çoğunlukla ilk iki günde gelir. O akşam eşi sorar: ne aldın, ne kadar verdin, ne yapacak bu kişi. Müşteri cevap veremezse ertesi sabah geri dönmek ister. Onay belgesi o soruların cevabını müşterinin eline verir.

Pazarlamada iki cümle: sözlü evet kapanış değildir, para kapanıştır. Ne teslim edeceksen onu söyle, sonra söylediğini teslim et.

Şunlar bu modülün işi değildir: görüşmeyi yönetmek (gorusmeyi-yonet), karşılama formunu ve kurulum görüşmesini yürütmek (musteriyi-karsila), müşterinin sistemini kurmak (musteri-sistemini-kur), fiyatı belirlemek (fiyati-belirle).

Tek kural, karıştırma: onay belgesi para gelmeden gitmez. Sözleşme ve ödeme bilgisi ise "evet"ten hemen sonra gider; ödeme bilgisi o gün hangi yol açıksa odur, link ya da havale. Görüşmede "bilgi gönder, teklif yaz" diyen adaya hiçbir şey gitmez; o bir itirazdır, cevabı görüşmenin içinde verilir.

## 2. Ne zaman çalışır
- Üçüncü gün, bir saat: havale mesajı, ödeme yolu tablosu, sözleşme ve onay belgesi taslağı. Bu akşam tanıdıklara ilk mesaj gidiyor, yani yarın "evet" gelebilir. Paranın alınacağı yol o mesajdan önce hazır olacak. Bugün biten şeyler: hesap bilgisi, tutar satırı ve açıklama satırı tek mesaj olarak yazılır; sözleşmeyi FounderOS doldurur, sen okursun; onay belgesi taslağı kurulur; ödeme yolu tablosunu FounderOS doldurur, sağlayıcıyı sen seçersin. Başvuru bugün yapılmaz; şirket açılınca ödeme linki başvurusunu birlikte yapıyoruz. Bunlar olmadan gelen "evet" beklemeye düşer ve bekleyen "evet" soğur.
- Beşinci gün: kontrol. Havale mesajı hazır mı, sözleşmenin doldurulmuş hali doğru mu, onay belgesi taslağındaki rakamlar bugünkü fiyatla aynı mı. Bunlar sahaya çıkış kontrol listesinde de var. Şirket bu günün işi değil, ilk "evet" günü açılır. Ödeme linki gelene kadar kapanan müşterinin parası havaleyle alınır; bu bir aksaklık değil, planın kendisi.
- Her kapanışta, görüşmenin son dakikasında: hazır kapanış mesajı elinde olur, sen gönderirsin. İlk kapanışta telefon kapanınca, aynı saatte: şirketin açılışı başlar ve müşavire gidecek hazır mesaj elinde olur (aşağıda, İlk "evet" günü).
- Para hesabına geçtiği an: onay belgesi hazırlanır, en geç bir saat içinde gider. Para gece ya da hafta sonu geçtiyse ertesi sabah ilk iş.
- Aylık ödemenin ilk iki ayında: tahsilat hatırlatma mesajları hazırlanır.
- Fiyat ya da teklif değişirse: şablonlardaki rakamlar yeniden doldurulur.

## 3. Ne okur

İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı dosya): iş adın, sistemin adı, Kademe 2'nin bu nişteki içeriği, kurulum ve aylık rakam, deneme fiyatı işareti, güvence cümlesi ve şartı, hazırlık seviyesi, şirketin durumu (müşavire mesaj gitti mi, açıldı mı, ödeme linki başvurusu nerede), ödeme sağlayıcın ve link adreslerin, havale mesajının hazır hali (hesap bilgisi, tutar satırı, açıklama satırı), mali müşavirinin adı ve cevapları (ilk "evet" gününden sonra), rakamın vergisi dahil mi hariç mi söyleneceği, sözleşmenin hangi sürümü elinde. Kademe 2, görüşmede satılan tam sistemdir. Güvence, müşteriye verdiğin sözdür: rapor gününde rapor; raporda sistemin yazdığı randevu sıfırsa ikinci ay ücreti alınmaz.
Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv`): kapanan adayın kaydı, işletme adı, sahibinin adı, telefon ve e-posta, kapanış saati, kayıp rakamı ve birimi, kurulum görüşmesi tarihi.
Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): "Yasal sınırlar" bölümündeki kısıtlar ve yasak vaatler (diş ve estetikte tanıtım yasağı, güzellikte hekim yetkisi gereken işlemler, sigortada acente unvanı, haşerede izin belgesi, emlakta mesaj izni kaydı, oto galeride yetki belgesi). Bu bölüm FounderOS'un başvurusudur; öğrenciye kural anlatılmaz, öğrenci yalnız sonucu duyar.
Doksan Gün Planı'nın beşinci bölümünden: teslimatın [21/28] günlük takvimi.

## 4. Ne sorar

Sormaz. Rakamlar, tarihler ve maddeler İş Beyni'nde ve kartta yazılı. Senden aldığı şeyler: paranın geldiği ("geldi"), kurulum görüşmesinin saati, sözleşme için bir kere eksik kişisel bilgin (açık adres, kimlik numarası) ve ilk "evet" gününden sonra müşavirin cevabı (sohbete yapıştırırsın).

Tek istisna üçüncü günde: ödeme sağlayıcısının adını sen seçersin. Ölçütleri FounderOS verir, tabloyu FounderOS doldurur, kararı sen verirsin. Sebebi para: komisyonu sen ödüyorsun.

## 5. Ne yapar

### Üçüncü gün: iki ödeme yolu ve iki şablon

**İki yol var ve ikisi de birinci sınıf.** Para iki yoldan gelir: ödeme linki ya da havale. Havale ikinci sınıf yol değil. İlk müşterilerin çoğu havaleyle kapanıyor, çünkü ilk "evet" geldiğinde çoğu öğrencinin henüz şirketi ve sağlayıcı hesabı yok. İkisinin de metni bugün hazırlanır, ikisi de kapanış anında beş dakika içinde gönderilebilir halde durur. Hangisinin kullanılacağını o günkü durum belirler; görüşmenin ortasında karar verilmez.

**Ödeme sağlayıcısı nasıl seçilir.** Sana bir şirket adı söylenmez. Sebebi şu: şartlar ve komisyonlar sık değişiyor, bugün yazılan ad altı ay sonra yanlış oluyor. Tabloyu FounderOS sağlayıcıların kendi sayfalarından doldurur, seçimi sen yaparsın.

Tabloya yalnız üç şartı geçen sağlayıcı girer: şahıs şirketiyle çalışıyor; Türkiye'deki şirketi kabul ediyor ve Türk bankasındaki hesaba Türk lirası gönderiyor (kendi sayfasında Türkiye yazmıyorsa girmez, denenmez); şirket açılınca eldeki belgelerden fazlasını istemiyor. Bu elemeyi FounderOS yapar, öğrenciye şart anlatılmaz.

Tabloda senin baktığın iki ölçüt var, sırası önemli:
1. Düzenli ödeme. Aylık ücreti müşterinin kartından her ay kendiliğinden çekebiliyor mu? Çekemiyorsa aylık ücreti her ay elle isteyeceksin, o da müşteriye her ay yeniden karar verdirmek demek. Bu ölçüt komisyondan önemli.
2. Komisyon. İşlem başına yüzde kaç, üstüne işlem başına sabit bir tutar var mı, ayrıca aylık sabit ücret var mı? Üçü aynı satırda durur; sadece yüzdeye bakmak yanıltıyor.

Sonra üç kontrol daha: para hesabına kaç günde geçiyor, karta itiraz olursa ne oluyor, destek Türkçe mi. Bunlar seçimi tek başına belirlemez ama eşit iki sağlayıcı arasında karar verdirir.

Tabloyu FounderOS doldurur, sağlayıcıları yan yana koyar, adı sen yazarsın. Bu, "sormaz söyler" kuralının açık istisnasıdır ve sebebi para: hesabı sen açıyorsun, komisyonu sen ödüyorsun, sözleşmeyi sen imzalıyorsun. Seçtiğin sağlayıcının adı ve komisyon oranı İş Beyni'ne yazılır; ölçütler değişirse aynı tablo yeniden doldurulur.

**Seçtikten sonra.** Başvuru bugün yapılmaz; şirket açılınca ödeme linki başvurusunu birlikte yapıyoruz. O güne kadar para havaleyle gelir ve iş beklemez. Sağlayıcının başvuruda istediği belgeleri ve formdaki düzenli ödeme kutusunu FounderOS İş Beyni'ne not eder; belge adları öğrenciye sayılmaz.

**Havale mesajı, bugün hazırlanır.** Tek mesaj, dört satır, kapanış anında kopyalanıp gönderilecek halde durur:
1. Hesap bilgisi: hesabın hangi adla açık olduğu (senin adın ya da şirket unvanın), banka adı ve IBAN. Şube ve hesap numarası yazılmaz.
2. Tutar: kurulum ücretinin yarısı, rakamla, tek satır; kalan yarısı teslimde, rapor gününde ([21/28]. gün) ödenir ve mesajın altında tarihiyle anılır. Aylık ücret bu satırda yok; o [31/38]. günün işi ve mesajın altında ayrı bir cümleyle tarihiyle anılır.
3. Açıklama satırı: müşterinin havale ekranındaki açıklama kutusuna yazacağı metin. Kısa ve sabit: işletme adı ve "kurulum". Bunu yazdırmanın tek sebebi var, gelen parayı kimin gönderdiğini karıştırmamak.
4. Tek cümle: "Gönderdikten sonra ekran görüntüsünü buraya atın; ben hesabıma düştüğünü görünce onay belgenizi göndereceğim."

Bu mesaj ne zaman gider: "evet" gelir gelmez, sen telefonu kapatmadan, sözleşme ve karşılama formuyla aynı mesajda. "Aynı gün" yok, "beş dakika içinde" var. Link yolunda da sıra aynı.

Fatura ne zaman kesilir: bu, ilk "evet" gününün işi; o gün adım adım söylenir (aşağıda, İlk "evet" günü). Müşteri sorarsa tek cümle: "Faturasını şirketimden keseceğim, tarihini size yazacağım." Tarih şirket açılınca netleşir; o güne kadar tarih sözü yok, "birkaç güne" gibi lastikli söz yok, "faturasız olur mu" pazarlığı yok.

**Sözleşme.** Hazır gelir, dosyada durur. Köşeli parantezleri FounderOS doldurur; sen okur ve gönderirsin. Sana söylenen iki cümle: "Müşterinin onaylayacağı sözleşme hazır, mesajın içinde. İmzadan önce kendi avukatına okut." Öğrenciye madde, hukuki terim ya da imza türü anlatılmaz.

Şablon on yedi madde ve üç ekten oluşur. Metin FounderOS'un başvurusudur; öğrenciye madde listesi okunmaz.

FounderOS'un doldurduğu yerler: iki tarafın bilgileri, kurulum ücreti, aylık ücret, şehir, tarih, birinci ekteki kapsam listesi. Başka hiçbir yere dokunulmaz; madde eklenmez, çıkarılmaz. Senden yalnız eksik kişisel bilgin (açık adresin, kimlik numaran) bir kere istenir.

Şablonun kilit maddeleri şunlar. Bunlar FounderOS'un bilmesi içindir; öğrenciye madde anlatılmaz, öğrenci yalnız sonucu duyar (ör. "Bu parça kurulamazsa o ay ücretin beşte birini almıyoruz, hesabı ben yapıyorum."):
- Kapsam dışı kalan parça güvencenin sonucuna sayılmıyor. Yasal sınır, hat, sağlayıcı ya da platform kuralı yüzünden kurulamayan bir parça varsa aynı gün yazılı bildiriyorsun ve o parçanın kurulmadığı her ay aylık ücret yüzde yirmi iniyor: parça başına yüzde yirmi, en çok yüzde altmış, parça kurulduğu ayı izleyen aydan tam ücret. Müşteri kendi adımını atmadığı için kurulamayan parçada indirim yok.
- Müşteri yükümlülüğünü geç yerine getirirse [21/28] gün o günden başlıyor ve tahsilat aynı kadar öteleniyor. Bu maddeyi kimse okumuyor ama seni koruyan madde bu.
- Sayı taahhüdü yok. Sözleşmede açıkça yazıyor: sonuç taahhüdü içermez.
- Hesaplar müşterinin adına, şifre paylaşılmıyor, mevcut numarasına dokunulmuyor.
- Liste müşterinin, sen sadece onun yazılı talimatıyla kullanıyorsun ve iş bitince siliyorsun. Gönderilecek metinleri müşteri onaylıyor.
- Sorumluluğun son üç ayda ondan aldığın parayla sınırlı.
- Kurulum ücreti kurulum bittikten sonraki fesihte iade edilmiyor.
- Deneme fiyatı varsa üç karşılık ayrıca yazılıyor.

Üç karşılık, deneme fiyatının karşılığında aldığın üç şeydir: rakamları paylaşma izni, isim ve logo izni, rapor gününde kısa bir video. Videoda müşterinin ya da çalışanlarının yüzü görünecekse ayrıca yazılı izin alınır. İzin sonradan geri alınırsa yayındaki isim, logo ve video kaldırılır. Fiyatın ne olacağını şablondaki madde belirler; sen müşteriye kendiliğinden "fiyat değişmez" demezsin.

İmza iki yoldan atılır; hangisi olduğunu CRM'in açık olup olmadığı belirler.

**CRM açılmadıysa (başlangıç görüşmesi henüz yapılmadıysa ya da erken "evet" geldiyse):** sözleşme klasörde `sozlesme-[musteri].pdf` olarak doldurulur, FounderOS yazar, sen okursun. Müşteriye WhatsApp'tan gider; müşteri belgeyi okuyup aynı sohbete "okudum, kabul ediyorum, [ad soyad], [tarih]" yazar; bu yazılı kabul yeter. Ardından kapora ya da kurulum ücretinin havalesi gelir. Yazılı kabulün ekran görüntüsü ve belge müşterinin bilgi dosyasında saklanır. CRM açıldığı gün aynı belge CRM'in belge bölümüne yüklenir ve "imzalandı, [tarih], WhatsApp yazılı kabul" notuyla kayda bağlanır; yeniden imzalatılmaz.

**CRM açıldıysa:** imza CRM'in belge bölümünden atılır ve işini görür. Müşteriye "bu ıslak imza yerine geçer" gibi bir cümle kurmuyorsun; gerek de yok, imzalı belge ikinizde de duruyor.

Şablonu CRM'e kurma sırası, CRM açıldığı gün FounderOS adım adım söyler (araclari-kur'un "CRM açıldığı gün" adımının hemen ardından, on beş dakika):
1. CRM'de ödemeler bölümüne gir, belgeler ve sözleşmeler ekranını aç.
2. Yeni belge oluştur; hazır metni yapıştır ya da PDF olarak yükle.
3. Müşteri adı, işletme adı, kurulum rakamı ve aylık rakam için değişken satırlar koy.
4. Alta iki imza satırı ve tarih koy: biri senin, biri müşterinin.
5. Kendi imzanı bir kere çiz, şablona göm.
6. Şablon olarak kaydet.
7. Kendi e-postana deneme gönderimi yap, geldiğini gör.
8. Gönderim ayarında e-postayı seç; kısa mesaj yolu Türkiye'de kapalı.
Ayrı bir imza programına abone olmana gerek yok. Belge bazen istenmeyen posta kutusuna düşer; onun için kapanış mesajında ayrıca link de verirsin.

**Onay belgesi taslağı.** Tek sayfa, sekiz başlık, rakamlar ve [21/28] günlük teslimat takvimi (Doksan Gün Planı'nın beşinci bölümünden) önceden dolu. CRM açıksa belge bölümünde ikinci şablon olarak durur ve link olarak gönderilir; CRM açık değilse klasörde `onay-belgesi-[musteri].pdf` olarak doldurulur ve WhatsApp'tan gider. İmza satırı yoktur.

### Beşinci gün: kontrol

Şirket bu günün işi değildir. Öğrenci sorarsa tek cümle: "Şirket ilk müşteri 'evet' dediğinde açılır; o gün adım adım söyleyeceğim."

Bugün yapılan kontrol üç şey:
- Havale mesajı hazır mı: hesap bilgisi, tutar satırı, açıklama satırı tek mesajda duruyor mu.
- FounderOS'un doldurduğu sözleşmeyi kendine gönderdin mi (CRM açıksa belge bölümünden, açık değilse PDF olarak WhatsApp'tan), köşeli parantez kalmış mı.
- Onay belgesi taslağındaki rakamlar bugünkü fiyatla aynı mı.
Bunlar zaten sahaya çıkış kontrol listesinde var.

Sahaya çıkış bunların hiçbirine bağlı değil; saha ertelenmez.

### Kapanış anı: tek mesaj, iki yoldan biri

"Evet" gelir gelmez konuşmayı kes, satışı geri alma. Hazır kapanış mesajını sohbete ya da WhatsApp'a yapıştırırsın. İki hazır mesaj var, hangisi geçerliyse o gider.

Link yolu: mesajın içinde dört link vardır: kurulum ödemesi, aylık için kart kaydı, sözleşme, karşılama formu. Sağlayıcın kurulumla aylığı tek linkte topluyorsa üç link olur. Sen hatta kalırsın: "Kapatmadan önce linke tıklayın, ben hattayım."

Havale yolu: mesajın içinde havalenin üç satırı (hesap bilgisi, tutar, açıklama satırı) ve iki link vardır: sözleşme ve karşılama formu. Altında tek cümleyle kurulumun kalan yarısının rapor gününde, aylık ücretin [31/38]. günde nasıl alınacağı yazar. Sen yine hatta kalırsın: "Kapatmadan önce havaleyi başlatın, ben hattayım."

CRM açıksa ikisinde de sözleşme ayrıca CRM'den e-postayla gider; CRM açılmadıysa PDF WhatsApp'tan gider, müşteri kabulünü aynı sohbete yazar. Hangi yolun kullanılacağı görüşmeden önce bellidir ve görüşme özet ekranında yazar; görüşmenin ortasında karar verilmez.

Kurulum görüşmesini aynı konuşmada takvime yazarsın, en geç iki gün sonrasına. Karşılama formunu kapanışta gönderirsin; müşteri hemen doldurursa iyi, son teslim tarihi yedinci gündür.

Para hesabına geçmeden müşteri sayılmaz, iş başlamaz. Havale yolunda dekont tek başına yetmez; hesabına düştüğünü göreceksin.

Fatura konusunu işletmeci sormadan sen açarsın. Şirketin varsa: "Faturasını şirketimden kesiyorum." Şirketin henüz yoksa: "Faturasını şirketimden keseceğim, tarihini size yazacağım." Tarihi müşavirin cevabı belirler; cevap gelmeden tarih sözü verilmez.

### İlk "evet" günü: şirketi açıyoruz

Telefon kapanınca, aynı saatte. FounderOS tek cümle söyler: "Şirketini açıyoruz; bir mali müşavir bunu bir iki günde yapar. Ona gidecek mesaj hazır, şimdi gönder." İş Beyni'nde bir müşavir yazılıysa ya da tanıdığın biri varsa mesaj ona gider. Yoksa FounderOS, internete erişimi varsa, şehrindeki üç müşavirin adını ve telefonunu bulur; erişimi yoksa internette şehrinin adıyla "mali müşavir" aratırsın. Mesaj ilk üçüne aynı anda gider. Cevaplardan FounderOS tek öneri çıkarır: en erken açabilen ve aylık toplamı makul olan. Para o arada havaleyle gelir; iş şirketi beklemez.

Müşavire gidecek mesaj, sen kopyalayıp gönderirsin:

"Merhaba, bir şahıs şirketi açmak ve bir mali müşavirle çalışmak istiyorum. Yazılım ve danışmanlık hizmeti veriyorum: işletmelere yapay zekâ ile müşteri karşılama sistemi kuruyorum. İlk müşterim bugün anlaştı. Birkaç sorum var:
1. Şirketi kaç günde açabiliriz, sizden hangi belgeleri istersiniz?
2. Açılışın bir kerelik masrafı ne, sonra her ay toplam ne kadara mal olur, vergi ve primler dahil?
3. Müşterilerime hangi belgeyi keseceğim, ilkini hangi gün kesebilirim?
4. Fiyatımı müşterilere KDV dahil mi, hariç mi söylemeliyim?
5. Ne zamandan itibaren işe başlamış sayılıyorum: ilk parayı aldığım gün mü, müşteri aramaya başladığım gün mü?
6. Yaşıma ya da ilk kez şirket açmama bağlı bir vergi indirimi var mı?
Uygun olduğunuz bir saatte arayabilir miyim?"

Mesaja öğrencinin durumuna göre şu satırlar eklenir, uymayan eklenmez: maaşlı bir işi varsa "Maaşlı bir işim var. Şirket açarsam ayrıca sigorta primi öder miyim, yoksa işyerimdeki sigortam yeter mi?"; öğrenciyse "Öğrenciyim, sağlık sigortam anne babam üzerinden. Şirket açarsam bu değişir mi?"; kasım ya da aralıktaysa "Şirketi ocakta açsak ne değişir?" Sorular öğrenciye ayrıca anlatılmaz. Müşavirin cevabını öğrenci sohbete yapıştırır; FounderOS İş Beyni'ne yazar: aylık toplamı, vergi ve prim dahil, masraf tablosuna tek satır olarak ("şirket ve muhasebe gideri"); dördüncü sorunun cevabını fiyat cümlesinin yanına (farklıysa yeni müşterilerden itibaren geçerli); faturanın gününü müşteriye gidecek hazır satıra. Öğrenci yalnız sonucu duyar: şirketin açılacağı gün, faturanın kesileceği gün ve müşteriye yazacağı hazır satır. Müşavir belge isterse FounderOS bunlara "müşavirin istediği belgeler" der, adlarını tek tek saymaz; neyin nereye götürüleceğini müşavir söyler.

### Onay belgesi: tek sayfa, sekiz başlık

Para hesabına geçtikten sonra en geç bir saat içinde, e-postayla ve WhatsApp'a. Başlıklar:
1. Ne aldınız: sistemin adı ve Kademe 2'nin maddeleri, işletmecinin kendi diliyle, tek paragraf.
2. Ne ödediniz, ne zaman: kurulum ve aylık rakam, ödeme tarihi, kurulumun kalan yarısının rapor gününde ([21/28]. gün) ödeneceği, ilk aylık tahsilatın [31/38]. gün olduğu, faturanın kimden geleceği. Bugünden bilinen kurulamayan parça varsa o parçanın kurulmadığı aylarda çekilecek indirimli aylık rakam da burada yazar: parça başına yüzde yirmi eksik, parça kurulduğu ayı izleyen aydan tam rakam.
3. Kurulum döneminin takvimi: sıfırıncı günden [21/28]. güne, gün gün ne olacağı. Sıra teslimatın kendi sırasıdır ve görüşmede söylenenle aynıdır ("altıncı gün canlı, yedinci gün liste"; panelin Teslimat Motoru da bunu gösterir): 0. gün ödeme ve karşılama; 1. ve 2. gün kurulum görüşmesi ve giriş izinleri; 2. ile 4. gün yazılı karşılama, randevu takvimi ve hatırlatmalar kurulur; 3. gün eski müşteri listesi istenir; 5. gün test; 6. gün canlı; 7. güne kadar karşılama formu ve listenin onayı, 8. günden eski müşterilere ilk mesajlar; 15. günden rapor gününe eksikler kapanır; [21/28]. gün rapor ve kalan ödeme. Doksan Gün Planı yoksa ya da beşinci bölümü boşsa takvim bu sıradan yazılır; canlıya alma rapor haftasına bırakılmaz.
4. Sizden ne bekliyorum, tarihli: giriş izinleri kurulum görüşmesinde; eski müşteri listesi üçüncü günde; karşılama formu ve duran havuz onayı yedinci güne kadar. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir. Kararı kimin vereceği ve ne kadar sürede cevap geleceği de burada yazar.
5. Güvence ve şartı: sözleşmedeki cümlenin aynısı.
6. Neyi yapmıyorum: reklam vermiyorum ve reklam yönetimi bu pakette yok, yeni site yapmıyorum, mevcut numaranıza dokunmuyorum, nişin yasakladığı vaatleri vermiyorum. Bugünden bilinen kurulamayan parça varsa adı ve sebebi burada tek satırla yazar; örnek: hattın giden aramayı desteklediği doğrulanana kadar telefonla dış arama kurulmuyor, o iki iş yazılı yürüyor. Kurulum görüşmesinde ortaya çıkan kurulamayan parça ise aynı gün kapsam dışı mesajıyla bildirilir.
7. Rapor gününde raporda ne olacak: İş modeli'ndeki güvence cümlesi, nişin yolculuğuna göre (randevu ya da teklif sürümü) buraya aynen girer; arkasına şu eklenir: "O ay bittiğinde kapsamı daraltarak devam, normal ücretle devam ya da yazılı bildirimle ayrılma yollarından biri seçilir." Sayı sözü yok.
8. Sıradaki adım: kurulum görüşmesinin günü ve saati, o görüşmeye ne getireceği. Karşılama formunu henüz doldurmadıysa linki burada bir kez daha durur.

Belge boyunca "ben" ve "siz" konuşulur; şirket ağzıyla "biz" yok, ekibin yok.
Dil kuralı: ne teslim edeceksen onu yaz, fazlasını yazma. Belgede rakam sözü yok, para iadesi cümlesi yok. "Garanti" kelimesi de yok; o, FounderOS'un sana verdiği sözdür (İlk Müşteri Güvencesi). Müşteriye verdiğin şeyin adı güvencedir.

### Aylık ödeme

Sessiz çalışır: kart kayıtlı, her ay kendiliğinden çekilir. Müşteriye her ay "yenileyelim mi" diye sorulmaz; sorarsan her ay yeniden karar vermek zorunda kalır.

İlk tahsilat [31/38]. gündür. Rapor gününde sistemin yazdığı randevu sıfırsa (teklif yolunda takip ettiği teklif) tahsilat çekilmeden durdurulur, ikinci ay ücretsiz çalışır. Kurulamayan parça varsa o ayın tutarını FounderOS hesaplar: sebep bizim elimizde değilse (bir kural, hat ya da sağlayıcı) parça başına ücretin beşte biri düşer, en çok yüzde altmış; sebep müşterinin kendi adımıysa tam çekilir. İndirimli rakam kendiliğinden ayarlanmaz: sağlayıcının panelinden o ayın tutarını sen düzeltirsin; panel buna izin vermiyorsa tam çekilir ve farkı aynı gün iade edersin. Müşteri kendi şartını geç yerine getirdiyse (izinleri ya da listeyi geç verdiyse) [21/28] gün onun verdiği günden başlar; tahsilat da aynı kadar ötelenir.

İlk iki ayda tahsilattan üç gün önce, bir gece önce ve sabahı WhatsApp mesajı gider. Metni FounderOS hazırlar, sen gönderirsin. Sebebi şu: tanımadığı bir tahsilatı gören müşteri "bu kişi beni dolandırıyor mu" diye düşünür.

### Havale yolunun ayrıntısı

Havale, linkin yokluğunda başvurulan yol değil; iki eşit yoldan biri. İlk müşterilerin çoğu böyle kapanıyor. Kapanışta hesap bilgini verirsin ve mesaj üçüncü günde hazırlanmış haliyle gider; o an bir şey yazmazsın.

Dikkat edilecek üç şey:
- Para hesabına geçtiğini gördüğünde müşteri sayılır. Dekont tek başına yetmez. Dekont, paranın gönderildiğini gösteren banka belgesidir; gönderildiğini gösterir, hesabına düştüğünü göstermez.
- Şirketin yoksa da bu yol açık. Müşavire giden mesaj ilk "evet" günü, kapanıştan hemen sonra gider; faturanın tarihi onun cevabıyla müşteriye yazılır. Cevap gelmeden tarih sözü verilmez.
- Havale yolundaysan [31/38]. günün tahsilatını elle istersin; hatırlatma mesajları aynen gider. Elle istenen tahsilatın tek kuralı var: gününde istenir, ertelenmez, "bu ay geçsin" denmez.

Şirket açıldığı gün FounderOS tek iş söyler: "Şirketin açıldı; ödeme linki başvurusunu şimdi birlikte yapıyoruz." Başvuru üçüncü günde seçtiğin sağlayıcıya gider ve formda düzenli ödeme kutusu işaretlenir. İstenen belgeler müşavirden gelenlerdir; adları öğrenciye sayılmaz. Onay birkaç gün sürer, o arada para havaleyle gelmeye devam eder. Onay geldiği gün kendi kartınla küçük bir deneme ödemesi yaparsın, para hesabına düşüyor mu görürsün, sonra iade edersin.

Şirket kurulup link geldiğinde havaledeki müşterileri linke geçirirsin: tek mesaj, kart kaydı linki ve tek cümle sebep ("her ay elden istemeyelim"). Sözleşme ve onay belgesi aynen yürür, yeniden imzalanmaz.

### Fiyat değişirse

fiyati-belirle ya da teklifi-yaz yeniden çalışırsa şablonlardaki rakamlar aynı gün güncellenir; eski rakamlı şablon kullanılmaz.

## 6. Ne söyler

Üçüncü gün: "Bugün dört iş: havale mesajı, ödeme yolu tablosu, sözleşme, onay belgesi taslağı. Havale mesajı bugün bitiyor; bugünden itibaren şirketin olmadan da müşteri kapatabilirsin, beklemiyoruz. Tabloyu ben dolduruyorum: her sağlayıcının komisyonu ve aylığı karttan kendiliğinden çekip çekemediği yan yana. Adı sen seçiyorsun, çünkü komisyonu sen ödeyeceksin. Şirket açılınca ödeme linki başvurusunu birlikte yapıyoruz. Sözleşme de hazır; ben dolduruyorum, sen okuyorsun. İlk 'evet'te beş dakikan olacak. O beş dakikada hazırlık yapamazsın."

Havale yoluyla kapanışta: "Şirketin yok diye beklemiyorsun, havale ikinci sınıf yol değil. Mesaj hazır: hesap, tutar, açıklama satırı. Şimdi gönder, hatta kal. Dekont değil, hesabına düştüğünü göreceksin. Fatura sorulursa: 'Faturasını şirketimden keseceğim, tarihini size yazacağım.' Telefonu kapatınca şirketini açıyoruz; bir mali müşavir bunu bir iki günde yapar, ona gidecek mesaj hazır."
Kapanış anında: "Evet dedi. Konuşmayı kes. Hazır mesajı yapıştır; müşterinin onaylayacağı sözleşme hazır, mesajın içinde. Bugün havale yolundasın: hesap, tutar, açıklama satırı, sözleşme, karşılama formu. Link yolundaysan aynı mesajın dört linkli hali. Hatta kal. Kurulum görüşmesini şimdi takvime yaz, en geç öbür gün."
Para gelince: "Para geldi. Müşterin var. Onay belgesi hazır; içinde [21/28] günün takvimi ve senden bekledikleri var. Bu gece aklına düşecek soruyu bu belge cevaplıyor."
Para gelmezse: "Sözlü evet kapanış değil. On dakika hattayken bekle, sonra tek mesaj: 'Link geldi mi?' Akşam bir mesaj, yarın bir arama. İki günde ödeme yoksa 'sonra' aşamasına atıyoruz."

## 7. Ne yazar

Kayıt yerine (CRM açıldıysa CRM, açılmadıysa `adaylar.csv` ve müşterinin bilgi dosyası, `musteriler/<musteri-adi>.md`): aşama müşteri (listede aday aracıyla, para hesaba geçtiği an: `temas <işletme> --kanal <kanal> --sonuc "ödeme geldi" --asama müşteri`; panelin Aday panosu ve temastan müşteriye sayısı buradan okur), ödeme saati ve tutarı, sözleşme durumu (gönderildi, imzalandı), onay belgesi gönderildi, kurulum görüşmesi tarihi, aylık tahsilat günü.
İş Beyni'ne: müşteri sayısı, kurulum ve aylık gelir, ilk müşteri tarihi, sözleşmenin sürümü ve doldurulma tarihi, ödeme yolu tablosu ve seçtiğin sağlayıcının adı ile komisyon oranı, link adreslerin, havale mesajının hazır hali, hangi müşterinin hangi yoldan ödediği, şirketin durumu (müşavire mesaj gitti, açıldı, ödeme linki başvurusu), müşavirin adı ve cevapları, aylık şirket ve muhasebe gideri tek satır olarak.
Durum kaydına, para hesaba geçtiği an: `sayaclar.musteri`, `aktif_musteriler` (işletmenin adı), ilk müşteride `ilerleme_asamasi` 4 ve `yol_haritasi_asamasi` 7, `gunluk_hedef` teslim süresince (tam zamanlıda 60, işin yanında 20; öğrenciye söylediğin sayı bu); aynı içerik `durum_yaz` ile sunucuya gider. Panel müşteriyi, teslimat kartını ve günün hedefini yalnız oradan görür; yazılmazsa sohbette "müşterin oldu" denirken panel müşteri sıfır ve hedef kırk gösterir.
Niş kartına: bu nişte çıkan sınır notları ve kapsam dışı tartışmaları, ilk müşteriden sonra. Sözleşmeye madde eklenmez; gerekirse ekibe destek adresinden tek satır gider.

## 8. Yedek yol

- Şirket ya da ödeme linki henüz yoksa: havale yolu. Bu bir yedek değil, iki eşit yoldan biri. Müşavire giden mesaj ilk "evet" günü aynı saatte gider; ön şart yok.
- Seçtiğin sağlayıcı başvuruyu reddederse: tablodaki ikinci sağlayıcıya geçilir, tablo yeniden doldurulmaz. O arada para havaleyle alınır.
- Sağlayıcı hesabını sonradan kapatırsa: aynı gün havale yoluna dönülür, mevcut müşterilere tek satır bilgi gider ("bu ayın ödemesini havaleyle alıyorum"), sözleşme değişmez.
- Sözleşme imzalanmadan para geldiyse: iş başlar, imza kurulum görüşmesinin ilk maddesi olur.
- Para gelmiş, sözleşme iki gün imzalanmamışsa: kurulum görüşmesi ertelenmez, görüşmede birlikte imzalanır.
- Belge istenmeyen posta kutusuna düştüyse: kapanış mesajındaki link kullanılır.
- Müşteri sözleşmede değişiklik isterse: açıklamazsın, pazarlık yapmazsın. Cümlen tek: "Not aldım, netleştirip size yazılı döneceğim." FounderOS destek adresine (destek@founderos.so) gidecek tek satırı hazır verir: işletmenin adı ve istenen değişiklik, müşterinin kendi cümlesiyle. Ekibin cevabı gelmeden değişmiş metin gönderilmez; bu not öğrenciye söylenmez.
- Müşteri "sözleşmeyi görmeden ödemem" derse: sıra değişir, önce sözleşme sonra ödeme. Oturum bozulmaz.
- Aylık tahsilat düşmezse: kart hatası mesajı, üç gün içinde tek hatırlatma, sonra arama. Hizmeti durdurmadan önce yazılı bildirim yapılır; bildirimin süresini ve metnini FounderOS sözleşmeden okuyup hazır verir.
- Hiçbir teslimat yapılmadan ayrılmak isteyen müşteri: tartışma açma, kurulum ücretini iade et. Teslimat başladıysa güvence maddesi işler. Müşterinin bankadan parayı geri istemesi ve bunun ödeme sağlayıcında bıraktığı iz, o paradan pahalıya gelir.

## 9. Sıradaki adım ve işaretler

Sıradaki: musteriyi-karsila (karşılama formu, kurulum görüşmesi), sonra musteri-sistemini-kur.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Kapanıştan sonra para on dakikada düşmedi: aynı oturumda tek hatırlatma.
- Sözleşme iki gün imzalanmadı: kurulum görüşmesinin ilk maddesi olur.
- Beşinci gün geldi, sözleşme doldurulmadı: sahaya çıkarsın ama ilk "evet"ten önce doldurulur. Beş dakikada bitiyor.
- İki müşteride üst üste "bu da dahil mi" tartışması çıktı: kapsam dışı listesi karta yazılır; sözleşmedeki listeye eklenmesi için ekibe destek adresinden tek satır gider.
- Aylık tahsilat iki kez düşmedi: degisiklige-karar-ver'e not gider. Bu fiyat sorunu değil, tahsilat sorunudur.
- Sağlayıcı tablosu üçüncü günde doldurulmadı: sahaya çıkışı durdurmaz, ilk hafta içinde doldurulur; o arada havale yolu yürür.
- Havale mesajı hazır değilken ilk "evet" geldi: mesaj o an yazılır, ödeme beklemez; ertesi gün şablon haline getirilir.
- İlk "evet" günü müşavire mesaj gitmedi: ertesi sabahın ilk işi olur, çünkü müşteri faturayı ilk gün soruyor.

Beş kural: boş sayfa yok (havale mesajı, sözleşme ve ödeme yolu tablosu üçüncü günde, müşavire gidecek mesaj ilk "evet" günü hazır gelir) · sessiz bitiş yok (ödeme, sözleşme durumu ve kurulum görüşmesi tarihi kaydedilir) · onay (linkler, havale mesajı, sözleşme, onay belgesi ve tahsilat hatırlatmaları senin elinden gider; sağlayıcının adını sen seçersin) · sahadan güncelleme (kapsam dışı ve yasal sınır maddeleri karta yazılır) · sormaz söyler (rakamları ve tarihleri FounderOS doldurur; tek istisna sağlayıcı seçimi, sebebi para).
