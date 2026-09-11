---
user-invocable: false
name: onay-belgesini-hazirla
description: "Öğrenci \"evet dedi\", \"kabul etti\", \"parayı gönderecek\" dediğinde kapanış mesajı ve onay belgesi. Ödeme yolu ve sözleşme üçüncü blokta kurulur."
---

# onay-belgesini-hazirla

## 1. Adı, rolü, pazarlamadaki karşılığı

Kapanış anının ve kapanıştan sonraki ilk saatin belgelerini hazırlayan modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Üç şey üretir:

1. Ödemenin iki yolu, ikisi de hazır durur ve ikisi de birinci sınıftır. Birincisi ödeme linkleri: biri kurulum ücreti için tek seferlik, biri aylık ücret için düzenli ödeme. Düzenli ödeme, müşterinin kartından her ay kendiliğinden çekilen ödemedir. Sağlayıcın ikisini tek linkte topluyorsa tek link olur. İkincisi havale mesajı: hesap bilgisi, tutar ve açıklama satırı tek mesajda. Şirketin yokken de para alabilirsin.
2. Sözleşme. Bir kere hazırlanır, her müşteride sadece adı ve rakamı değişir. CRM açıksa belge bölümünden imzalanır; CRM açılmadıysa PDF gider ve müşterinin WhatsApp'taki yazılı kabulü imza sayılır (aşağıda).
3. Onay belgesi. Para hesabına geçtikten sonra müşteriye giden tek sayfa.

Neden var: sözlü "evet" ile paranın hesabına geçmesi arasındaki her dakika kayıp riskidir. Bir de şu var: insan bir şey satın aldıktan sonra pişmanlık çoğunlukla ilk iki günde gelir. O akşam eşi sorar: ne aldın, ne kadar verdin, ne yapacak bu kişi. Müşteri cevap veremezse ertesi sabah geri dönmek ister. Onay belgesi o soruların cevabını müşterinin eline verir.

Pazarlamada iki cümle: sözlü evet kapanış değildir, para kapanıştır. Az söz ver, fazla teslim et.

Şunlar bu modülün işi değildir: görüşmeyi yönetmek (gorusmeyi-yonet), karşılama formunu ve kurulum görüşmesini yürütmek (musteriyi-karsila), müşterinin sistemini kurmak (musteri-sistemini-kur), fiyatı belirlemek (fiyati-belirle).

Tek kural, karıştırma: onay belgesi para gelmeden gitmez. Sözleşme ve ödeme bilgisi ise "evet"ten hemen sonra gider; ödeme bilgisi o gün hangi yol açıksa odur, link ya da havale. Görüşmede "bilgi gönder, teklif yaz" diyen adaya hiçbir şey gitmez; o bir itirazdır, cevabı görüşmenin içinde verilir.

## 2. Ne zaman çalışır
- Üçüncü gün, bir saat: havale yolu, sözleşme ve ödeme linkinin evrak listesi. Bugün akşam tanıdıklara ilk mesaj gidiyor, yani dördüncü günde "evet" gelebilir. Paranın alınacağı yol o günden önce hazır olacak. Bugün biten şeyler: hesap bilgisi, tutar satırı ve açıklama satırı tek mesaj olarak yazılır; sözleşme şablonunun köşeli parantezleri doldurulur; onay belgesi taslağı kurulur; ödeme sağlayıcısı ölçütleri okunur, tabloya yazılır, sağlayıcıyı sen seçersin ve seçtiğinin istediği evrak listesi çıkarılır. Başvuru bugün yapılmaz, çünkü sağlayıcıların çoğu vergi levhası istiyor ve levha şirket kurulunca geliyor. Vergi levhası, vergi dairesinin şirketine verdiği belgedir. Evrak listesi hazır olursa levha gelir gelmez başvuru aynı gün gider. Bunlar olmadan gelen "evet" beklemeye düşer ve bekleyen "evet" soğur.
- Beşinci gün: şirket bugün kurulmuyor, kuruluşa hazır oluyor. Şirket ilk sözlü "evet"i aldığın gün kurulur; sebebi şu, şirketi açtığın günden itibaren aylık sabit gider işliyor ve sen kazanmasan da işliyor. Bugün yapılan kontrol: havale mesajı hazır mı, şablonların köşeli parantezleri dolu mu, sözleşmenin doldurulmuş sürümü doğru mu, onay belgesi taslağındaki rakamlar bugünkü fiyatla aynı mı. Bunlar sahaya çıkış kontrol listesinde de var. Ödeme sağlayıcısına başvuru şu zincire bağlı: şirket kurulur, vergi levhası gelir, levhanın geldiği gün başvuru gider. Başvurunun onayı birkaç gün sürer; o günlerde kapanan müşterinin parası havaleyle alınır ve bu bir aksaklık değil, planın kendisi.
- Her kapanışta, görüşmenin son dakikasında: hazır kapanış mesajı elinde olur, sen gönderirsin.
- Para hesabına geçtiği an: onay belgesi hazırlanır, en geç bir saat içinde gider. Para gece ya da hafta sonu geçtiyse ertesi sabah ilk iş.
- Aylık ödemenin ilk iki ayında: tahsilat hatırlatma mesajları hazırlanır.
- Fiyat ya da teklif değişirse: şablonlardaki rakamlar yeniden doldurulur.

## 3. Ne okur

İş Beyni'nden (senin hakkında bilinen her şeyin yazıldığı dosya): iş adın, sistemin adı, Kademe 2'nin bu nişteki içeriği, kurulum ve aylık rakam, deneme fiyatı işareti, güvence cümlesi ve şartı, hazırlık seviyesi, şirket ve vergi levhası durumu, ödeme sağlayıcın ve link adreslerin, havale mesajının hazır hali (hesap bilgisi, tutar satırı, açıklama satırı), mali müşavirinin adı ve faturanın ne zaman kesileceği sorusuna verdiği cevap, rakamın vergisi dahil mi hariç mi söyleneceği, sözleşmenin hangi sürümü elinde. Kademe 2, görüşmede satılan tam sistemdir. Güvence, müşteriye verdiğin sözdür: rapor gününde rapor; raporda yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz.
Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv`): kapanan adayın kaydı, işletme adı, sahibinin adı, telefon ve e-posta, kapanış saati, kayıp rakamı ve birimi, kurulum görüşmesi tarihi.
Niş kartından (sektör hakkında bilinen her şeyin yazılı olduğu hazır sayfa): "Yasal sınırlar" bölümündeki kısıtlar ve yasak vaatler (diş ve estetikte tanıtım yasağı, güzellikte hekim yetkisi gereken işlemler, sigortada acente unvanı, haşerede izin belgesi, emlakta İYS, oto galeride yetki belgesi).
Doksan Gün Planı'nın beşinci bölümünden: teslimatın [21/28] günlük takvimi.

## 4. Ne sorar

Sormaz. Rakamlar, tarihler ve maddeler İş Beyni'nde ve kartta yazılı. Senden aldığı iki şey: paranın geldiği ("geldi") ve kurulum görüşmesinin saati.

Tek istisna üçüncü günde: ödeme sağlayıcısının adını sen seçersin. Ölçütleri FounderOS verir, tabloyu FounderOS doldurur, kararı sen verirsin. Sebebi para: komisyonu sen ödüyorsun.

## 5. Ne yapar

### Üçüncü gün: iki ödeme yolu ve iki şablon

**İki yol var ve ikisi de birinci sınıf.** Para iki yoldan gelir: ödeme linki ya da havale. Havale ikinci sınıf yol değil. İlk müşterilerin çoğu havaleyle kapanıyor, çünkü ilk "evet" geldiğinde çoğu öğrencinin henüz şirketi ve sağlayıcı hesabı yok. İkisinin de metni bugün hazırlanır, ikisi de kapanış anında beş dakika içinde gönderilebilir halde durur. Hangisinin kullanılacağını o günkü durum belirler; görüşmenin ortasında karar verilmez.

**Ödeme sağlayıcısı nasıl seçilir.** Sana bir şirket adı söylenmez. Sebebi şu: şartlar ve komisyonlar sık değişiyor, bugün yazılan ad altı ay sonra yanlış oluyor. Bugün yapacağın iş, sağlayıcıların kendi sayfalarına bakıp beş ölçütü tabloya yazmak ve seçimi kendin yapmak. Bir saat sürer.

Beş ölçüt, sırası önemli:
1. Şirket şartı. Şahıs şirketini kabul ediyor mu, yoksa yalnız limited şirketle mi çalışıyor? Şahıs şirketini kabul etmeyen sağlayıcı senin için yok, ötesine bakma.
2. Vergi levhası şartı. Levha istiyor mu; istiyorsa başvuruda mı istiyor, sonra mı? Çoğu istiyor ve bu bir sorun değil; levha şirket kurulunca zaten geliyor. Sorun, levhaya ek olarak sende olmayan bir belge isteyen sağlayıcı.
3. Komisyon oranı ve sabit kesinti. İşlem başına yüzde kaç, üstüne işlem başına sabit bir tutar var mı, ayrıca aylık sabit ücret var mı? Üçünü aynı satıra yazarsın; sadece yüzdeye bakmak yanıltıyor.
4. Düzenli ödeme desteği. Aylık ücreti müşterinin kartından her ay kendiliğinden çekebiliyor mu? Çekemiyorsa aylık ücreti her ay elle isteyeceksin, o da müşteriye her ay yeniden karar verdirmek demek. Bu ölçüt komisyondan önemli.
5. Türkiye'de çalışması. Türkiye'deki şirketleri kabul ediyor mu, Türk bankasındaki hesabına Türk lirası gönderiyor mu? Sağlayıcının kendi sayfasında Türkiye yazmıyorsa geçersin, denemezsin.

Sonra üç kontrol daha: para hesabına kaç günde geçiyor, karta itiraz olursa ne oluyor, destek Türkçe mi. Bunlar seçimi tek başına belirlemez ama eşit iki sağlayıcı arasında karar verdirir.

Tabloyu FounderOS doldurur, sağlayıcıları yan yana koyar, adı sen yazarsın. Bu, "sormaz söyler" kuralının açık istisnasıdır ve sebebi para: hesabı sen açıyorsun, komisyonu sen ödüyorsun, sözleşmeyi sen imzalıyorsun. Seçtiğin sağlayıcının adı ve komisyon oranı İş Beyni'ne yazılır; ölçütler değişirse aynı tablo yeniden doldurulur.

**Seçtikten sonra, aynı gün.** Adımlar:
1. Sağlayıcının kendi sayfasından istediği evrak listesini çıkarır, İş Beyni'ne yazarsın. Şahıs şirketini kabul eden sağlayıcılar genelde vergi levhası ve imza örneği istiyor.
2. Başvuruyu bugün yapmazsın. Şirket ilk "evet"i aldığın gün kuruluyor, levha ondan sonra geliyor. Bugün sadece listeyi hazırlarsın; levha eline geçtiği gün başvuru aynı gün gider.
3. Başvuru formunda düzenli ödeme (abonelik) kutusunu da işaretleyeceksin; aylık ücret onunla çekilecek. Bunu şimdiden not edersin, o gün unutulur.
4. Onay birkaç gün sürer. O günlerde kapanan müşteri havaleyle alınır ve iş beklemez.

**Havale mesajı, bugün hazırlanır.** Tek mesaj, dört satır, kapanış anında kopyalanıp gönderilecek halde durur:
1. Hesap bilgisi: hesabın hangi adla açık olduğu (senin adın ya da şirket unvanın), banka adı ve IBAN. Şube ve hesap numarası yazılmaz.
2. Tutar: kurulum ücreti, rakamla, tek satır. Aylık ücret bu satırda yok; o [31/38]. günün işi ve mesajın altında ayrı bir cümleyle tarihiyle anılır.
3. Açıklama satırı: müşterinin havale ekranındaki açıklama kutusuna yazacağı metin. Kısa ve sabit: işletme adı ve "kurulum". Bunu yazdırmanın tek sebebi var, gelen parayı kimin gönderdiğini karıştırmamak.
4. Tek cümle: "Gönderdikten sonra ekran görüntüsünü buraya atın; ben hesabıma düştüğünü görünce onay belgenizi göndereceğim."

Bu mesaj ne zaman gider: "evet" gelir gelmez, sen telefonu kapatmadan, sözleşme ve karşılama formuyla aynı mesajda. "Aynı gün" yok, "beş dakika içinde" var. Link yolunda da sıra aynı.

Fatura ne zaman kesilir: bunu mali müşavirin söyler. Şirketin yoksa havale yolunu ancak müşavirine sorduktan ve belgeyi ne zaman keseceğini öğrendikten sonra kullanırsın. Cevap gelmeden müşteriye tarih sözü verilmez. Müşteri sorarsa tek cümle: "Belgeyi mali müşavirim çıkarıyor, tarihini size yazılı bildireceğim." Uydurma tarih yok, "birkaç güne" gibi lastikli söz yok, "faturasız olur mu" pazarlığı yok.

**Sözleşme şablonu.** Şablon hazır geliyor, dosyada duruyor. Sen sözleşme yazmıyorsun, yapay zekaya da yazdırmıyorsun; hazır metni alıp köşeli parantezleri dolduruyorsun.

Şablon on yedi maddeden ve üç ekten oluşuyor: taraflar, konu, tanımlar, kapsam ve teslim süresi, müşterinin yükümlülükleri, güvence, ücret ve ödeme, hesap ve veri sahipliği, kişisel veriler, gizlilik, fikri mülkiyet, süre ve fesih, sorumluluk, mücbir sebep, bildirimler, uyuşmazlık, yürürlük. Ekler: hizmetin kapsamı, rapordaki üç sayı, giriş izinleri.

Senin dolduracağın yerler: iki tarafın bilgileri, kurulum ücreti, aylık ücret, şehir, tarih, birinci ekteki kapsam listesi. Başka hiçbir yere dokunmuyorsun. Madde eklemiyor, çıkarmıyorsun.

Şablonun kilit maddeleri şunlar ve neden orada olduklarını bilmen lazım:
- Kapsam dışı kalan parça güvencenin sonucuna sayılmıyor. Yasal sınır ya da platform kuralı yüzünden kurulamayan bir parça varsa aynı gün yazılı bildiriyorsun.
- Müşteri yükümlülüğünü geç yerine getirirse [21/28] gün o günden başlıyor ve tahsilat aynı kadar öteleniyor. Bu maddeyi kimse okumuyor ama seni koruyan madde bu.
- Sayı taahhüdü yok. Sözleşmede açıkça yazıyor: sonuç taahhüdü içermez.
- Hesaplar müşterinin adına, şifre paylaşılmıyor, mevcut numarasına dokunulmuyor.
- Liste müşterinin, sen sadece onun yazılı talimatıyla kullanıyorsun ve iş bitince siliyorsun. Gönderilecek metinleri müşteri onaylıyor.
- Sorumluluğun son üç ayda ondan aldığın parayla sınırlı.
- Kurulum ücreti kurulum bittikten sonraki fesihte iade edilmiyor.
- Deneme fiyatı varsa üç karşılık ayrıca yazılıyor.

Üç karşılık, deneme fiyatının karşılığında aldığın üç şeydir: rakamları paylaşma izni, isim ve logo izni, rapor gününde kısa bir video. Videoda müşterinin ya da çalışanlarının yüzü görünecekse ayrıca yazılı izin alınır. İzin sonradan geri alınırsa yayındaki isim, logo ve video kaldırılır. Fiyatın ne olacağını şablondaki madde belirler; sen müşteriye kendiliğinden "fiyat değişmez" demezsin.

İmza iki yoldan atılır ve ikisi de geçerlidir; hangisi olduğunu CRM'in açık olup olmadığı belirler.

**CRM açılmadıysa (başlangıç görüşmesi henüz yapılmadıysa ya da erken "evet" geldiyse):** sözleşme klasörde `sozlesme-[musteri].pdf` olarak doldurulur, FounderOS yazar, sen okursun. Müşteriye WhatsApp'tan gider; müşteri belgeyi okuyup aynı sohbete "okudum, kabul ediyorum, [ad soyad], [tarih]" yazar ve o yazılı kabul sözleşmenin imzası sayılır; ardından kapora ya da kurulum ücretinin havalesi gelir. Yazılı kabulün ekran görüntüsü ve belge müşterinin bilgi dosyasında saklanır. CRM açıldığı gün aynı belge CRM'in belge bölümüne yüklenir ve "imzalandı, [tarih], WhatsApp yazılı kabul" notuyla kayda bağlanır; yeniden imzalatılmaz.

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

### Beşinci gün: kuruluşa hazır olmak ve kontrol

Şirketin bugün kurulmuyor. Bugün kuruluşa hazır oluyorsun: mali müşavirin belli, ona soracağın beş sorunun cevabı yazılı, istediği belgeler bir klasörde, kuruluş için tek telefon kalmış. Şirket ilk sözlü "evet"i aldığın gün kurulur.

Ödeme sağlayıcısına başvuru da o zincire bağlı: şirket kurulur, vergi levhası gelir, levhanın geldiği gün başvuru gider. Formda düzenli ödeme kutusunu işaretlemeyi unutma. Onay birkaç gün sürer ve o günlerde para havaleyle alınır.

Bugün yapılan kontrol üç şey:
- Havale mesajı hazır mı: hesap bilgisi, tutar satırı, açıklama satırı tek mesajda duruyor mu.
- Sözleşme şablonunu kendine gönderdin mi (CRM açıksa belge bölümünden, açık değilse PDF olarak WhatsApp'tan), köşeli parantezlerin hepsi dolu mu.
- Onay belgesi taslağındaki rakamlar bugünkü fiyatla aynı mı.
Bunlar zaten sahaya çıkış kontrol listesinde var.

Sahaya çıkış bunların hiçbirine bağlı değil; saha ertelenmez.

Sağlayıcının başvurusu onaylandığı gün şunu yaparsın: kendi kartınla küçük bir deneme ödemesi yapar, para hesabına düşüyor mu görür, sonra iade edersin.

### Kapanış anı: tek mesaj, iki yoldan biri

"Evet" gelir gelmez konuşmayı kes, satışı geri alma. Hazır kapanış mesajını sohbete ya da WhatsApp'a yapıştırırsın. İki hazır mesaj var, hangisi geçerliyse o gider.

Link yolu: mesajın içinde dört link vardır: kurulum ödemesi, aylık için kart kaydı, sözleşme, karşılama formu. Sağlayıcın kurulumla aylığı tek linkte topluyorsa üç link olur. Sen hatta kalırsın: "Kapatmadan önce linke tıklayın, ben hattayım."

Havale yolu: mesajın içinde havalenin üç satırı (hesap bilgisi, tutar, açıklama satırı) ve iki link vardır: sözleşme ve karşılama formu. Altında tek cümleyle aylık ücretin [31/38]. günde nasıl alınacağı yazar. Sen yine hatta kalırsın: "Kapatmadan önce havaleyi başlatın, ben hattayım."

CRM açıksa ikisinde de sözleşme ayrıca CRM'den e-postayla gider; CRM açılmadıysa PDF WhatsApp'tan gider ve yazılı kabul imza sayılır. Hangi yolun kullanılacağı görüşmeden önce bellidir ve görüşme özet ekranında yazar; görüşmenin ortasında karar verilmez.

Kurulum görüşmesini aynı konuşmada takvime yazarsın, en geç iki gün sonrasına. Karşılama formunu kapanışta gönderirsin; müşteri hemen doldurursa iyi, son teslim tarihi yedinci gündür.

Para hesabına geçmeden müşteri sayılmaz, iş başlamaz. Havale yolunda dekont tek başına yetmez; hesabına düştüğünü göreceksin.

Fatura konusunu işletmeci sormadan sen açarsın. Şirketin varsa: "Faturasını şirketimden kesiyorum." Şirketin henüz yoksa: "Belgeyi mali müşavirim çıkarıyor, tarihini size yazılı bildireceğim." Belgenin adı (fatura mı serbest meslek makbuzu mu) ve ne zaman kesileceği senin işinin nasıl vergilendirildiğine bağlı; onu mali müşavirin söyler. Bu modül sana süre söylemez, sen de müşteriye tarih sözü vermezsin.

### Onay belgesi: tek sayfa, sekiz başlık

Para hesabına geçtikten sonra en geç bir saat içinde, e-postayla ve WhatsApp'a. Başlıklar:
1. Ne aldınız: sistemin adı ve Kademe 2'nin maddeleri, işletmecinin kendi diliyle, tek paragraf.
2. Ne ödediniz, ne zaman: kurulum ve aylık rakam, ödeme tarihi, ilk aylık tahsilatın [31/38]. gün olduğu, faturanın kimden geleceği.
3. Kurulum döneminin takvimi: sıfırıncı günden [21/28]. güne, gün gün ne olacağı.
4. Sizden ne bekliyorum, tarihli: giriş izinleri kurulum görüşmesinde; eski müşteri listesi üçüncü günde; karşılama formu ve duran havuz onayı yedinci güne kadar. Duran havuz, işletmenin elindeki uzun süredir aranmamış eski müşteri listesidir. Kararı kimin vereceği ve ne kadar sürede cevap geleceği de burada yazar.
5. Güvence ve şartı: sözleşmedeki cümlenin aynısı.
6. Neyi yapmıyorum: reklam bütçesi benden çıkmaz, yeni site yapmıyorum, mevcut numaranıza dokunmuyorum, nişin yasakladığı vaatleri vermiyorum.
7. Rapor gününde raporda ne olacak: İş modeli'ndeki güvence cümlesi, nişin yolculuğuna göre (randevu ya da teklif sürümü) buraya aynen girer; arkasına şu eklenir: "O ay bittiğinde kapsamı daraltarak devam, normal ücretle devam ya da yazılı bildirimle ayrılma yollarından biri seçilir." Sayı sözü yok.
8. Sıradaki adım: kurulum görüşmesinin günü ve saati, o görüşmeye ne getireceği. Karşılama formunu henüz doldurmadıysa linki burada bir kez daha durur.

Belge boyunca "ben" ve "siz" konuşulur; şirket ağzıyla "biz" yok, ekibin yok.
Dil kuralı: az söz ver, fazla teslim et. Belgede rakam sözü yok, para iadesi cümlesi yok. "Garanti" kelimesi de yok; garanti, FounderOS'un sana verdiği sözün adıdır. Müşteriye verdiğin şeyin adı güvencedir.

### Aylık ödeme

Sessiz çalışır: kart kayıtlı, her ay kendiliğinden çekilir. Müşteriye her ay "yenileyelim mi" diye sorulmaz; sorarsan her ay yeniden karar vermek zorunda kalır.

İlk tahsilat [31/38]. gündür. Rapor gününde sonuç çıkmadıysa tahsilat çekilmeden durdurulur, ikinci ay ücretsiz çalışır. Müşteri kendi şartını geç yerine getirdiyse (izinleri ya da listeyi geç verdiyse) [21/28] gün onun verdiği günden başlar; tahsilat da aynı kadar ötelenir.

İlk iki ayda tahsilattan üç gün önce, bir gece önce ve sabahı kısa mesaj gider. Metni FounderOS hazırlar, sen gönderirsin. Sebebi şu: tanımadığı bir tahsilatı gören müşteri "bu kişi beni dolandırıyor mu" diye düşünür.

### Havale yolunun ayrıntısı

Havale, linkin yokluğunda başvurulan yol değil; iki eşit yoldan biri. İlk müşterilerin çoğu böyle kapanıyor. Kapanışta hesap bilgini verirsin ve mesaj üçüncü günde hazırlanmış haliyle gider; o an bir şey yazmazsın.

Dikkat edilecek üç şey:
- Para hesabına geçtiğini gördüğünde müşteri sayılır. Dekont tek başına yetmez. Dekont, paranın gönderildiğini gösteren banka belgesidir; gönderildiğini gösterir, hesabına düştüğünü göstermez.
- Şirketin yoksa bu yolu ancak mali müşavirine sorup belgeyi ne zaman keseceğini öğrendikten sonra kullanırsın. Cevap gelmeden müşteriye tarih sözü verilmez.
- Havale yolundaysan [31/38]. günün tahsilatını elle istersin; hatırlatma mesajları aynen gider. Elle istenen tahsilatın tek kuralı var: gününde istenir, ertelenmez, "bu ay geçsin" denmez.

Şirket kurulup link geldiğinde havaledeki müşterileri linke geçirirsin: tek mesaj, kart kaydı linki ve tek cümle sebep ("her ay elden istemeyelim"). Sözleşme ve onay belgesi aynen yürür, yeniden imzalanmaz.

### Fiyat değişirse

fiyati-belirle ya da teklifi-yaz yeniden çalışırsa şablonlardaki rakamlar aynı gün güncellenir; eski rakamlı şablon kullanılmaz.

## 6. Ne söyler

Üçüncü gün: "Bugün dört iş: havale mesajı, ödeme sağlayıcısı tablosu, sözleşme şablonu, onay belgesi taslağı. Havale mesajı bugün bitiyor; bugünden itibaren şirketin olmadan da müşteri kapatabilirsin, beklemiyoruz. Sağlayıcı tablosunda beş ölçüt var: şahıs şirketini kabul ediyor mu, vergi levhası istiyor mu, komisyonu ne, aylığı karttan kendiliğinden çekebiliyor mu, Türkiye'de çalışıyor mu. Tabloyu ben dolduruyorum, adı sen yazıyorsun; komisyonu sen ödeyeceksin, seçimi ben yapmam. Başvuru şirket kurulunca gider, şirket de ilk 'evet' geldiği gün kurulur. İlk 'evet'te beş dakikan olacak. O beş dakikada hazırlık yapamazsın."

Havale yoluyla kapanışta: "Şirketin yok diye beklemiyorsun, havale ikinci sınıf yol değil. Mesaj hazır: hesap, tutar, açıklama satırı. Şimdi gönder, hatta kal. Dekont değil, hesabına düştüğünü göreceksin. Faturayı müşavirine sordun mu? Sormadıysan müşteriye tarih söyleme, 'yazılı bildireceğim' de."
Kapanış anında: "Evet dedi. Konuşmayı kes. Hazır mesajı yapıştır; bugün havale yolundasın: hesap, tutar, açıklama satırı, sözleşme, karşılama formu. Link yolundaysan aynı mesajın dört linkli hali. Hatta kal. Kurulum görüşmesini şimdi takvime yaz, en geç öbür gün."
Para gelince: "Para geldi. Müşterin var. Onay belgesi hazır; içinde [21/28] günün takvimi ve senden bekledikleri var. Bu gece aklına düşecek soruyu bu belge cevaplıyor."
Para gelmezse: "Sözlü evet kapanış değil. On dakika hattayken bekle, sonra tek mesaj: 'Link geldi mi?' Akşam bir mesaj, yarın bir arama. İki günde ödeme yoksa 'sonra' aşamasına atıyoruz."

## 7. Ne yazar

Kayıt yerine (CRM açıldıysa CRM, açılmadıysa `adaylar.csv` ve İş Beyni'nin on ikinci bölümü): aşama kazandım, ödeme saati ve tutarı, sözleşme durumu (gönderildi, imzalandı), onay belgesi gönderildi, kurulum görüşmesi tarihi, aylık tahsilat günü.
İş Beyni'ne: müşteri sayısı, kurulum ve aylık gelir, ilk müşteri tarihi, sözleşmenin sürümü ve doldurulma tarihi, ödeme sağlayıcı tablosunun beş satırı ve seçtiğin sağlayıcının adı ile komisyon oranı, link adreslerin, havale mesajının hazır hali, hangi müşterinin hangi yoldan ödediği, şirket ve vergi levhası durumu, mali müşavirin fatura sorusuna verdiği cevap.
Niş kartına: bu nişte sözleşmeye eklenen yasal sınır maddesi ve çıkan kapsam dışı tartışmaları, ilk müşteriden sonra.

## 8. Yedek yol

- Şirket, vergi levhası ya da sağlayıcı onayı henüz yoksa: havale yolu. Bu bir yedek değil, iki eşit yoldan biri; tek şartı mali müşavire fatura sorusunun sorulmuş olması.
- Seçtiğin sağlayıcı başvuruyu reddederse: tablodaki ikinci sağlayıcıya geçilir, tablo yeniden doldurulmaz. O arada para havaleyle alınır.
- Sağlayıcı hesabını sonradan kapatırsa: aynı gün havale yoluna dönülür, mevcut müşterilere tek satır bilgi gider ("bu ayın ödemesini havaleyle alıyorum"), sözleşme değişmez.
- Sözleşme imzalanmadan para geldiyse: iş başlar, imza kurulum görüşmesinin ilk maddesi olur.
- Para gelmiş, sözleşme iki gün imzalanmamışsa: kurulum görüşmesi ertelenmez, görüşmede birlikte imzalanır.
- Belge istenmeyen posta kutusuna düştüyse: kapanış mesajındaki link kullanılır.
- Müşteri sözleşmeyi avukatına gönderir ve madde değişikliği isterse: kendi başına madde değiştirmiyorsun. İsteği yazılı olarak alıyorsun, FounderOS'a getiriyorsun, karşılığını birlikte yazıyoruz.
- Müşteri "sözleşmeyi görmeden ödemem" derse: sıra değişir, önce sözleşme sonra ödeme. Oturum bozulmaz.
- Aylık tahsilat düşmezse: kart hatası mesajı, üç gün içinde tek hatırlatma, sonra arama. Hizmeti durdurmadan önce yazılı bildirim yapılır; bildirimin süresi ve yolu şablonda yazar.
- Hiçbir teslimat yapılmadan ayrılmak isteyen müşteri: tartışma açma, kurulum ücretini iade et. Teslimat başladıysa güvence maddesi işler. Müşterinin bankadan parayı geri istemesi ve bunun ödeme sağlayıcında bıraktığı iz, o paradan pahalıya gelir.

## 9. Sıradaki adım ve işaretler

Sıradaki: musteriyi-karsila (karşılama formu, kurulum görüşmesi), sonra musteri-sistemini-kur.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Kapanıştan sonra para on dakikada düşmedi: aynı oturumda tek hatırlatma.
- Sözleşme iki gün imzalanmadı: kurulum görüşmesinin ilk maddesi olur.
- Beşinci gün geldi, sözleşme doldurulmadı: sahaya çıkarsın ama ilk "evet"ten önce doldurulur. Beş dakikada bitiyor.
- İki müşteride üst üste "bu da dahil mi" tartışması çıktı: kapsam dışı listesi karta ve sözleşmeye eklenir.
- Aylık tahsilat iki kez düşmedi: degisiklige-karar-ver'e not gider. Bu fiyat sorunu değil, tahsilat sorunudur.
- Sağlayıcı tablosu üçüncü günde doldurulmadı: sahaya çıkışı durdurmaz, ilk hafta içinde doldurulur; o arada havale yolu yürür.
- Havale mesajı hazır değilken ilk "evet" geldi: mesaj o an yazılır, ödeme beklemez; ertesi gün şablon haline getirilir.
- Mali müşavire fatura sorusu üç gündür sorulmadı: sabah planına girer, çünkü müşteri bunu ilk gün soruyor.

Beş kural: boş sayfa yok (havale mesajı, sözleşme, sağlayıcı ölçütleri ve ödeme linkinin evrak listesi üçüncü günde hazırlanır) · sessiz bitiş yok (ödeme, sözleşme durumu ve kurulum görüşmesi tarihi kaydedilir) · onay (linkler, havale mesajı, sözleşme, onay belgesi ve tahsilat hatırlatmaları senin elinden gider; sağlayıcının adını sen seçersin) · sahadan güncelleme (kapsam dışı ve yasal sınır maddeleri karta yazılır) · sormaz söyler (rakamları ve tarihleri FounderOS doldurur; tek istisna sağlayıcı seçimi, sebebi para).
