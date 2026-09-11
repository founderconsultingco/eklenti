---
user-invocable: false
name: kanitini-hazirla
description: "Dördüncü gün. Deneme araması ve demo hattı: sorunun ve çözümün kanıtı. Beşinci günden itibaren her akşam yarım saat akşam testi."
---

# kanitini-hazirla

## 1. Adı, rolü, pazarlamadaki karşılığı

Dördüncü günün modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır; bu modül, henüz tek müşterin yokken eline iki kanıt verir.

Birincisi sorunun kanıtı. Adayları gerçek bir müşteri gibi denersin: akşam ararsın, kaçı açmıyor sayarsın; mesaj yazarsın, kaç saatte döndüklerini ölçersin; formlarını doldurursun, dönen var mı bakarsın. Buna deneme araması diyoruz.

İkincisi çözümün kanıtı. Sattığın sistemin küçük bir örneği demo hattında çalışır. Demo hattı, nişin için hazır duran bir telefon numarasıdır; sen almıyorsun, sana açılıyor. Aday görüşmede o numarayı kendi telefonundan arar, asistanın nasıl konuştuğunu ve randevuyu nasıl yazdığını kendi kulağıyla duyar.

Bu ikisinden iki cümle çıkar. Aday bazında yaşanmış kanca: "Dün akşam yedi onda aradım, açan olmadı." Toplu kanıt cümlesi: "Geçen hafta bu şehirde otuz klima servisini akşam yedide aradım, yirmi ikisi açmadı." İkisi de senin yaşadığın, senin saydığın şeydir.

Pazarlamada bunun adı şu: sorunun kanıtıyla gel, çözümün iddiasıyla değil. Referansın yoksa örnek göster. "Bana güven" deme, ne yapabileceğini göster. İşletmeciye "müşteri kaçırıyorsunuz" diyen bir satıcı değilsin; dün akşam onun kaçırdığı müşterisin. Görüşmeye gelen işletmecilerin çoğunun "evet" demesinin sebebi bu kanıttır.

Şunlar bu modülün işi değildir: mesajı yazmak (adaya-mesaj-yaz), video mesaj (video-mesaj-cek), ödeme yapan müşterinin kendi sistemini kurmak (musteri-sistemini-kur). Adayın adıyla ona özel demo kurmak da yapılmaz; sebebi aşağıda.

Kanıt hikâyesi ile karıştırma: kanıt hikâyesi, ilk müşterinde çıkan gerçek rakamdır ve rapor gününde gelir. Buradaki iki kanıt daha önce, müşterin yokken elinde olur.

**Bu testler denetim kartının içinde duruyor.** Canlı arama testi denetim kartının altıncı satırı, yazılı test yedinci satırı. İkisini de sen yaparsın, sonucu tek kelimeyle söylersin, sonuç o adayın denetim kartına yazılır. Kartın "en güçlü bulgu" satırı çoğu zaman buradan çıkıyor: arama açılmadıysa en güçlü bulgu odur, açıldıysa ve yazılı test cevapsız kaldıysa o. Testlerin nasıl yapılacağı, hangi saatte yapılacağı ve sınırları burada, bu metinde yazılıdır; denetim modülü bu metne bakar, kendi kuralını koymaz. Sınır burada değişirse denetimde de değişir. İki yerde iki ayrı kural olmaz.

## 2. Ne zaman çalışır
- Demo hattı başlangıç görüşmesinde CRM bölümünle birlikte verilir; senin cebinden para çıkmıyor, ücretsiz. Dördüncü blokta elindeyse test edilir, değilse CRM günü.
- Dördüncü bloğun içinde, üç saat. Sabah bloğunda yazılı testler ve form testleri. Demo hattın açıldıysa saha bloğunda sen demoyu denersin ve kaydını alırsın. Akşam yedi ile sekiz arası telefon testi. Gece adaya-mesaj-yaz ilk yüz teması hazırlar.
- Beşinci bloğun sabah bloğunda: bir önceki gün yapılan yazılı ve form testlerinin yirmi dört saati dolar, sonuçlar kesinleşir, kanıt cümlesi yazılır. On dakikada ön görüşme videosunun kanıt bölümünü çekersin; sayılar ve demo kaydı oraya girer. Hali ön görüşme sayfasına konur.
- Beşinci günün akşamından itibaren her akşam yarım saat "akşam testi": ertesi gün arayacağın listenin ilk yirmi adayını yedi ile yedi buçuk arası ararsın. Ertesi gün onları bu sonuçla ararsın. Bu yarım saat, günlük arama ve mesaj saatlerinin (dört saat) üstüne gelir. İşin yanında çalışıyorsan bu yarım saat saha bloğunun içine düşer (18.00-20.30) ve o akşamın temas sayısından düşülmez, çünkü test aramaları temas sayılmaz. Tam zamanlıda saha bloğu on yedide bittiği için akşam testi saha bloğunun arkasına eklenen yarım saattir.
- Kanca gün adıyla söylenir: "geçen Salı akşam yedide aradım". Bir haftadan eski test kancada kullanılmaz.
- Toplu kanıt cümlesi her pazartesi CRM'deki sayımla güncellenir.
- İlk kanıt hikâyesi çıkınca demo senaryosuna gerçek rakam girer; kanıt cümlesi yerini kanıt hikâyesine bırakır.

## 3. Ne okur

Kayıt yerinden (CRM açıldıysa CRM, açılmadıysa `adaylar.csv` ve İş Beyni'nin on beşinci bölümü): üçüncü blokta yazılan aday listesi, en çok istenen yüz işletme işareti, sahibinin adı, telefon, WhatsApp, Instagram, sitesinde form var mı, reklam veriyor mu işareti. Kartta kararı sahibinden başkası veriyorsa o kişinin adı yazılır.
Niş kartından: telefon saatleri (çoğu kartta bu satır boştur, sahadan dolar), telefonu kim açıyor, sezon, yasal sınırlar, "aradım açmadılar" tipi gerçek şikâyetler.
İş Beyni'nden: iş adın, sistemin adı, Dönüşüm Cümlesi, kayıp birimi, kanal yolu, çalışma düzeni, şehir, demo hattının numarası.
Hazır kurulum paketinden: nişin asistan kuralları (fiyat vermez, numaraya dokunmaz, mevzuat cümleleri).
Canlı doğrulama tablosundan (ikinci gün nişin şehirdeki sayılarının internetten sayıldığı tablo): reklam veren oranı. "Görülemedi" yazıyorsa reklam testi yapılmaz.

## 4. Ne sorar

Sormaz. Hangi adayın hangi kanaldan, saat kaçta deneneceğini FounderOS karttan seçer. Senden aldığı iki şey var. Birincisi her denemenin sonucu, tek kelime: "açtı", "açmadı", "döndü 14.20", "dönmedi". İkincisi demo için "tamam".

## 5. Ne yapar

**Saatler ve pencereler.** Bu modüldeki test saatleri senin çalışma saatin değil, işletmenin saati. Akşam yedide arıyorsun, çünkü işletmeci o saatte sahada; sabah on ile on bir arası yazıyorsun, çünkü dükkan o saatte açılmış oluyor. Nişin kanal ve zaman bölümü saha bloğunun içinde daraltma yapıyorsa o daraltma üstündür ve kart bir saat söylüyorsa o saat geçerlidir. Testin dışındaki her iş pencere adıyla söylenir: hazırlık ve okuma sabah bloğunda, testler ve aramalar saha bloğunda, sayım ve kayıt akşam bloğunda. Kartın saati ile senin pencerelerin hiç kesişmiyorsa o gün telefon testi yapılmaz, yazılı test yapılır ve sebebi kayda yazılır.

**Sorunun kanıtı: üç test.** Hangisinin yapılacağı nişe göre.

Telefon testi, her nişte var. Bu test denetim kartının altıncı satırıdır. Saat nişe göre:
- Ustanın sahada olduğu nişlerde (oto kuaför, oto servis, klima ve kombi sezonda, temizlik, tadilat, elektrik, fotoğraf): kartta kapanış saati yazıyorsa kapanıştan bir saat sonra; yazmıyorsa akşam yedi ile sekiz arası.
- Geç saate kadar açık nişlerde (emlak, pilates, güzellik salonu): akşam değil, en yoğun saatte. Kartın yazdığı yoğun saat ya da öğle on iki buçuk ile bir buçuk arası.
- Diş ve estetikte: kapanış saati kartta yoksa öğle arası.
- Kaç arama: dördüncü gün otuz. Adayları en çok istenen yüz işletmeden FounderOS seçer, sahibinin adı ve numarası olanlardan.
- Açmazsa: on beş saniye çaldır, sesli mesaj bırakma, sonuç "açmadı". Aynı akşam ikinci deneme yok.
- Açarsa: konuşma başlatma, satış yok. "Merhaba, kaça kadar açıksınız?" de, teşekkür et, kapat; sonuç "açtı". Açan aday listeden çıkmaz; ona farklı bir kanca yazılır: "Dün yedi onda aradım, siz açtınız; o saatte telefona hep siz mi bakıyorsunuz?"

Yazılı test. Bu test denetim kartının yedinci satırıdır. Yazının ana kanal olduğu nişlerde: düğün, fotoğraf, cam balkon, kuaför, oto galeri, sigorta, emlak. On aday. Kendi adınla ve kendi kişisel numaranla (demo hattıyla değil) gerçek bir müşteri sorusu yazarsın. Soruyu FounderOS karttan, kayıp birimine göre üretir: "Cam balkon için keşfe ne zaman gelebilirsiniz?", "Ekim'de düğün için boş tarihiniz var mı?" Saat: sabah on ile on bir arası. Ölçülen şey dönüş süresi. Yasak olanlar: sahte isim, sahte işletme, randevu almak, randevuyu meşgul etmek, fiyat pazarlığı. Cevap gelince saati söylersin, tek satır yazarsın: "Teşekkürler, bilgi alıyordum." Aday WhatsApp'tan devam ederse tek satır: "Telefonla arayayım, uygun olursanız." Orada anlatım yok. Satış mesajı yine telefondan ve e-postadan gider. Müşteri sorusu soğuk satış mesajı sayılmaz: içinde satış yok, tek mesaj, cevabına satış yazılmıyor. Ertesi temasta açıkça söylersin: "Salı on yirmide yazdım, dörtte döndünüz; ben aslında bu işi yapıyorum."

Form ve reklam testi. Sitesinde form olan ya da reklam veriyor işareti taşıyan adaylar, on tane. Kendi adın, kendi numaran, gerçek bir bilgi talebiyle formu doldurursun; reklamdaki forma da aynı. Saat: sabah on ile on bir arası. Ölçülen: ilk dönüş kaç dakika ya da kaç saat sonra geldi, hangi kanaldan (arama, WhatsApp, e-posta). Yirmi dört saatte dönmeyen "dönmedi".

Yazılı testte de aynı kural: yirmi dört saatte dönmeyen "dönmedi".

Sağlık ve tıbbi işlem nişlerinde (diş, estetik, güzellik salonunun tıbbi işlemleri) kural kesindir: hasta gibi yazmak yok, randevu istemek yok, tıbbi soru yok. Yazılı testin sorusu tıbbi olmayan bir sorudur: "Cumartesi açık mısınız?", "Otoparkınız var mı?" Form testi yok. Telefon testi var.

Her niş için "kapalıydık" itirazına hazır cevap CRM'de kancanın yanında durur: "O saatte arayan müşteri sizin için kaçmış bir müşteri sayılmıyor mu?"

Adayın sana verdiği cevabın ekran görüntüsü hiçbir yerde kullanılmaz. Kullanılan tek şey senin kendi ölçümün: gün, saat, süre.

Kayıt: her sonucu tek kelimeyle söylersin, FounderOS CRM'e adayın notuna yazar: kanal, gün, saat, sonuç, dönüş süresi. Sen CRM'e elle bir şey girmezsin.

Aynı satır o adayın denetim kartının altıncı ve yedinci satırına da düşer. İki yerde iki ayrı kayıt tutulmaz; aynı kayıt iki yerden okunur. Arama açılmadıysa o satır çoğu zaman kartın en güçlü bulgusu oluyor ve mesajın ilk cümlesi oradan çıkıyor. Test yapılmamış adayın kartında o iki satır "yapılmadı" yazar ve en güçlü bulgu sıradaki satırdan seçilir; kart o haliyle de çalışır, ama zayıf çalışır.

**Yaşanmış kanca ve kanıt cümlesi.**

Yaşanmış kancayı FounderOS yazar, aday bazında, tek satır, gün, saat, kanal ve sonuçla: "Dün akşam yedi onda aradım, açan olmadı." "Salı on yirmide WhatsApp'tan yazdım, dörtte döndünüz." "Formunuzu Salı doldurdum, dönüş gelmedi." Kural: sadece yaşanmış olan; gün ve saat gerçek; "genelde açmıyorsunuz" gibi genelleme yok. Dördüncü bloğun elli denemesi o adayların kancası olur ve sahanın ilk günü "geçen Salı" diye söylenir. Diğer adayların kancası akşam testinden gelir.

Toplu kanıt cümlesini FounderOS CRM sayımından yazar: "Geçen hafta [şehir]de otuz [niş] işletmesini akşam yedide aradım, yirmi ikisi açmadı." "On işletmenin formunu doldurdum, üçü döndü, en hızlısı dört saat." Kurallar: sayı yuvarlanmaz, yukarı çekilmez. Bir kanalda on denemeden az varsa o kanal için toplu cümle yok. Her pazartesi güncellenir. Görüşmede bu cümle kartın kanıtı değil, senin kendi sayımındır ve öyle söylenir: "Ben saydım." Kullanıldığı yerler: arama ve e-posta açılışı, video mesajın beşinci satırı, görüşme özet ekranı ve sunum, "kanıtla" itirazının cevabı, ön görüşme sayfası ve videosu, kanıt hikâyesi çıkana kadar e-posta imzasındaki kanıt satırı.

Yurt dışında "müşteri ilk dönene gider, beş dakika içinde dönmeyen kaybeder" diye rakamlar dolaşır. Rakamları farklı farklı; hiçbiri senin metnine sayı olarak girmez. Görüşmede rakam vermeden tek cümle söylenir: "Müşteri ilk dönene gider."

**Çözümün kanıtı: demo hattı ve canlı sistem.**

Demo hattı: nişinin demo numarası. Sen almıyorsun, kurmuyorsun, cebinden para çıkmıyor. Numara hazır duruyor, başlangıç görüşmesinde CRM bölümünle birlikte sana veriliyor. Türkiye numarası, 0850 ile başlıyor; arayan kişi normal bir işletmeyi aramış gibi arıyor.

Numara nişe göre, kişiye göre değil. Aynı nişteki herkes aynı numarayı kullanıyor, çünkü gösterdiğin şey senin işin değil, sistemin kendisi. Klima nişindeysen karşına bir klima servisinin asistanı çıkıyor. Bu bilerek böyle. Numara senin işletme adınla konuşsaydı işletmeci senin klimacı olduğunu sanardı; şimdi ne sattığın net kalıyor.

Nasıl çalışıyor: aday numarayı arar, telefonu asistan açar, Türkçe konuşur, iki üç soru sorar, uygun saati söyler, randevuyu takvime yazar. Aday bunu kendi telefonundan, kendi kulağıyla duyar. Sen ekran açmazsın, sunum göstermezsin, "şöyle çalışıyor" diye anlatmazsın.

Asistanın kuralları paketten gelir: fiyat vermez, marka ve model tavsiye etmez, işletmenin numarasına dokunulmadığını söyler, nişin mevzuat cümlelerini söyler. Kurallarını sen değiştirmezsin; FounderOS değiştirir.

Demo bir şeyi doğrudan gösteriyor: kaçırılan arama. İşletmecinin kaçırdığı arama, bu numarada kaçmıyor. Bunu anlatmıyorsun, dinletiyorsun. Müşterinin kendi sisteminde bu parça yönlendirmeye bağlı, o yüzden görüşmede "sizde de aynısı olacak" değil, "sistemin yaptığı iş bu" diye anlatılır.

Test, demo hattı elindeyse bugünün ikinci yarısında; başlangıç görüşmesi henüz yapılmadıysa CRM açıldığı gün, araclari-kur'un "CRM açıldığı gün" adımının sonunda. O güne kadar kanıtın deneme aramasıdır ve görüşmede kendi telefonundan canlı gösterim yaparsın. Kendi telefonundan demo numarasını ararsın, en az beş tam tur, kötü senaryolar dahil: normal randevu, fiyat sorusu, "insan mısın", mesai dışı arama, randevu değiştirme. Fiyat verdiyse, saçmaladıysa, randevuyu yazmadıysa "tamam" yok; demo hattı nişin ortak hattı olduğu için düzeltmeyi FounderOS ekibi yapar, sen bozuk cevabı destek@founderos.so adresine tek satırla bildirirsin, düzelince tekrar denersin. Bozuk demo, hiç demo olmamasından kötüdür. Demo "tamam" almadan da görüşmeler yapılır; o zaman kanıtın deneme aramasıdır.

Demo kaydı: test temiz çıkınca kırk ile altmış saniyelik bir kayıt alırsın. İki telefon gerekiyor: biriyle ararsın, öbürüyle çekersin. Sahne: telefon çalar, asistan açar, üç dört cümlelik konuşma, randevu onayı. Kullanım: ön görüşme videosunun kanıt bölümü bu kayıtla çekilir; kayıt videodan sonra gelirse kanıt bölümü o gün yeniden çekilir, üç dakika sürer. Mesajlarda ve video mesajda demo kaydı gönderilmez, aday sorsa da. Demo, görüşmeye gelme sebebidir; önceden gönderirsen sebebi harcamış olursun.

Görüşmedeki yeri: soru bölümünden sonra, sunumda. Ekran paylaşımı ve sunum dosyası yok. "Şimdi şu numarayı arayın, kapatmadan dinleyin." Soru bölümünden önce gösterilmez. Adaya özel demo, yani onun işletme adıyla kurulmuş bir hat, görüşmeden önce yapılmaz; kişiye özel olan şey adayın kendi deneme sonucudur. Onun adına kurulum ödemeden sonra yapılır.

**Dördüncü blok akışı.** Sabah bloğunun başında FounderOS yazılı test sorularını ve form adaylarını verir · yazılı testler ve form testleri kartın yazdığı saatte, yani sabah on ile on bir arası · demo hattı elindeyse saha bloğunun içinde demo testi, beş tur, yirmi dakika, hemen arkasından kayıt (elinde değilse bu iki adım CRM gününe kayar) · akşam yedi ile sekiz arası telefon testi, otuz arama (nişin saati farklıysa FounderOS söyler) · testin bitiminden on beş dakika sonra sonuçları söylersin, CRM'e ve o adayların denetim kartına yazılır; gece ilk yüz temas üretilir, form sonuçları ertesi günün sabah bloğunda kesinleşir. İşin yanında çalışıyorsan: yazılı ve form testleri öğle arasında, on ile on bir arası olmuyorsa FounderOS'un vereceği saatte (yirmi dakika); telefon testi 19.00-20.00, yani saha bloğunun içinde; demo testi dördüncü günün akşam bloğunda; ön görüşme videosunun kanıt bölümü beşinci günün sabah bloğunda çekilir. Dördüncü gün toplam bir buçuk saat.

## 6. Ne söyler

Sabah bloğunda: "Bugün iki kanıt çıkarıyoruz. Sorunun kanıtı: kartın söylediği kapanış saatinden sonra otuz işletmeyi arayacaksın, kaçının açmadığını sayacağız. Çözümün kanıtı: demo hattın açıldıysa günün ikinci yarısında çalışan sistemi kendi telefonundan göreceksin; açılmadıysa o kanıt başlangıç görüşmenden sonra geliyor. Yarından sonra 'bana güvenin' demeyeceksin; 'dün akşam aradım, açan olmadı' diyeceksin."
Test sırasında biri açarsa: "Konuşma başlatma. 'Kaça kadar açıksınız' de, teşekkür et, kapat. Bana 'açtı' de."
Akşam bloğunda: "Otuz arama, yirmi ikisi açmadı. Yirmi ikisinin kartına altıncı satır olarak yazıldı; sahanın ilk günü onları bu cümleyle arıyorsun. Yazılı on sorudan şimdilik dördü döndü, en hızlısı bir saat; kalanı yarın sabah kesinleşir. Form sonuçları da yarın sabah. Kanıt cümlen yarın sabah hazır, içinde uydurma tek rakam yok."
Demo bozuksa: "Fiyat verdi. Böyle demo gösterilmez. Düzeltiyorum, on dakika sonra tekrar dene."

## 7. Ne yazar

CRM'de adayın notuna: kanal, gün, saat, sonuç, dönüş süresi. Aynı sonuç adayın denetim kartının altıncı ve yedinci satırına düşer. CRM'de adayın kaydına: yaşanmış kanca tek satır ve "kapalıydık" cevabı. İş Beyni'ne: kanıt cümlesi (tarihli), demo hattının numarası, demo durumu (kaç tur, "tamam" tarihi), demo kaydının yeri. Doksan Gün Planı'nın dokuzuncu bölümüne (kancalar): yaşanmış kanca kalıbı. Niş kartına: telefon saati ve dönüş süresi ölçümleri, ilk elli denemeden sonra, "sahadan dolacak" satırlarına.

## 8. Yedek yol

- Demo hattı henüz elinde değilse (başlangıç görüşmesi yapılmadı): demo testi CRM gününe kayar; o güne kadar görüşmeler deneme aramasıyla yapılır.
- Demo numarası meşgul çıkarsa ya da aynı anda başka biri demo yapıyorsa: numaranın eşzamanlı çağrı sınırı yok, sıraya girme durumu olmuyor. Yine de bağlanmazsa aynı gün destek@founderos.so adresine yazarsın.
- Otuz aramada yirmi beşten fazlası açtıysa: telefon kanıtı zayıf. Yazılı ve form testine ağırlık verilir; kanca kartın açılış cümlesi olur.
- Yazılı testte aday satış sanıp kızarsa: tek satır "müşteri olarak sormuştum, teşekkürler"; aday "sonra" aşamasına.
- Demo beş turda temiz çıkmadıysa: "tamam" yok, görüşmeler yine yapılır, kanıt deneme araması; her gün bir tur daha test.
- CRM'e yazılamıyorsa ya da henüz açılmadıysa: sonuçlar `adaylar.csv`'ye ve `denetim-kartlari.md`'ye; CRM açıldığı gün aktarılır.
- İşin yanında çalışıyorsan ve akşam testinden sonra ertesi gün mesai saatinde arayamıyorsan: açmayan adayı öğle arasında ararsın ya da kanca e-postayla gider.

## 9. Sıradaki adım ve işaretler

Sıradaki: test sonuçları o adayların denetim kartına düşer, aday-denetimi-cikar kartı tamamlar ve en güçlü bulguyu seçer; aynı gece adaya-mesaj-yaz ilk yüz teması üretir, içinde dördüncü günün kancaları ve toplu cümle var. Dördüncü ve beşinci gün gorusme-provasi-yap; provada görüşme özet ekranındaki ölçüm satırı kullanılır. Beşinci günün akşamından itibaren her akşam yarım saat akşam testi.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Otuz aramada yirmi beşten fazlası açtı: yazılı ve form testine geçilir, karta not düşülür.
- Yazılı ve form testlerinin tamamı iki saatte döndü: bu nişte dönüş hızlı; kanca "geri aranmayan eski müşteri" sızıntısına kayar, degisiklige-karar-ver'e not gider, teklif değişmez.
- Demo testinde fiyat verdi ya da randevuyu yazmadı: desteğe bildirilir, düzelene kadar kanıt deneme aramasıdır.
- Kanıt cümlesi iki hafta güncellenmedi: pazartesi sayımı sabah planına girer.
- İlk kanıt hikâyesi çıktı: demo senaryosuna gerçek rakam, e-posta imzası güncellenir.
- Bir adayın test sonucu denetim kartına düşmedi: kart eksik sayılır, o aday aranmaz, sonuç aynı gece kartın altıncı ya da yedinci satırına yazılır.
- Görüşme analizinden "bulgu reddedildi" işareti geliyor, yani işletmeciler "biz açtık" diyor: test saati kartın yazdığı saatle karşılaştırılır, gerekirse saat değişir ve karta not düşer.

Beş kural: boş sayfa yok (sorular, arama listesi, kurulum hazır gelir) · sessiz bitiş yok (akşam sayım, CRM kaydı, denetim kartının altıncı ve yedinci satırı, "yarın yüz temas") · onay (demo "tamam"ı senden; test aramalarını kendi elinle yaparsın; tek istisna demo hattını arayan adaya asistanın cevabı) · sahadan güncelleme (ölçümler karta ve kanıt cümlesine yazılır) · sormaz söyler (kanal, saat, aday seçimi FounderOS'un).
