---
user-invocable: false
name: sozluk
description: "FounderOS'un butun modullerinin ve terimlerinin listesi. Hangi modulun ne yaptigini hatirlaman gerektiginde acilir."
---

# FounderOS Modül İçerikleri

Bu dosya FounderOS'un modüllerinin ne yaptığını anlatır; her modül aynı dokuz başlıkla yazılır. Mimari sayfası ve niş kartları ayrı dosyalarda. Dosyadaki her özel kelime aşağıdaki sözlükte tek cümleyle açıklanmıştır; bir kelimeyi anlamadıysan önce oraya bak.

## Sözlük (dosyada geçen her özel kelime, tek cümleyle)

Sistem ve dosyalar:
- FounderOS: Berk'in kurduğu, doksan gün boyunca sana her sabah ne yapacağını söyleyen sistem. Bu dosyadaki her modülü o çalıştırır.
- Modül: FounderOS'un belli bir işi yapan parçası (niş seçmek, mesaj yazmak, görüşmeyi yönetmek gibi). Sen modül adlarını bilmek zorunda değilsin; her sabah FounderOS'a "günaydın" yazarsın, o günün planı gelir, gerisini FounderOS seçer.
- Arka plan yardımcısı: FounderOS'un ağır işleri (niş doğrulama tablosunun kurulması, ideal müşteri araştırması, görüşme kaydını okuma, aylık rapor) verdiği yardımcı; sen onu görmezsin, sonucu FounderOS anlatır. Aday listesini yardımcı değil veri servisi çeker.
- İş Beyni: Senin hakkında bilinen her şeyin yazıldığı tek dosya, senin bilgisayarında. On sekiz bölümü var: kurucu, hedef ve para, niş, teklif ve fiyat, teslimat, marka ve varlıklar, araçlar ve hesaplar, listeler, mesajlar ve kanıt, sayılar, kararlar, müşteriler, açık işler, aşama ve tamamlanma, bugünün listesi, taslaklar, takılmalar ve destek, ideal müşteri. Hiçbir satır silinmiyor; değişen bilginin yenisi tarihiyle altına yazılıyor.
- Kurucu bölümü: İş Beyni'nde seni anlatan dört satır: seni ne motive eder, ne durdurur, daha önce nerede bıraktın, nerede düşme riskin var.
- Marka kiti: İşinin nasıl görüneceğini tek yerde toplayan kit: ad, logo, renkler, yazı tipleri, kullanım kuralları ve gerçek dosyalar. Birinci gün kurulur. İki parçası var: on iki panoluk `marka-kiti.html` (bakılan taraf) ve `marka/` klasöründeki yirmi iki gerçek dosya (kullanılan taraf). Hazır bir şablon dosyasından üretilir; her öğrencide yeniden tasarlanmaz.
- Pano: Marka kitindeki tek bir sayfa. On iki pano tek sayfada alt alta durur: kapak, marka temeli, logo ve alternatifleri, logo kuralları, renk paleti, tipografi, grafik dil, site başlığı önizlemesi, sosyal medya, içerik örnekleri, kurumsal set, hızlı referans.
- Dosya haritası: İş Beyni'nin altıncı bölümünde duran liste: marka klasöründeki hangi dosya ne işe yarıyor ve nerede duruyor. Öğrenci okumaz, modüller okur; site kurulurken logo buradan bulunur.
- Marka şablonu: `marka-sablonu.html`. Kitin bütün panolarını, her varlığın tam piksel ölçüsünü ve üç kütüphaneyi (on iki işaret, altı tipografi eşleşmesi, on palet) taşıyan hazır dosya. FounderOS onu kopyalar ve yalnız `window.MARKA` veri bloğunu doldurur; tasarım her öğrencide yeniden yapılmaz.
- İşaret: Markanın harf olmayan geometrik simgesi. On iki tanesi şablonda hazır duruyor; nişe uyanı seçiliyor. Renkli yuvarlak kare içine iki harf koymak işaret sayılmaz, o hazır şablon kalıbıdır ve bir bakışta anlaşılır.
- Kilit: Logonun düzeni. Üç biçim var: yatay (işaret solda, ad sağda), dikey (işaret üstte, ad altta), sadece yazı (işaret yok, adın sonunda tek nokta).
- Palet: Markanın renk takımı. On tanesi şablonda hazır duruyor; her biri koyu kimlik yüzeyi, vurgu rengi ve iki atmosfer rengi taşıyor.
- Atmosfer: Koyu yüzeyin arkasındaki bulanık ışık. Markayı düz siyah kutudan ayıran şey budur; paletle birlikte geliyor, ayrıca ayarlanmıyor.
- Marka yönü seçimi: Birinci günde öğrenciye açılan ekran. Seçilen isimle üç kilit yan yana durur, öğrenci birini seçer, kitin tamamı onunla kurulur. Tek tur; ikinci tur yok.
- İsim aileleri: Adın kuruluş biçimi. Dört aile var, nişe göre üçü öğrenciye sunulur: sistem adı (KlinikFlowOS gibi, nişin kökü artı mekanizma artı sistem eki), kısa uydurma (Ravin, Nexa), kısa gerçek Türkçe kelime (Kavis, Rota), kurucunun soyadı.
- Çağrışım kontrolü: Bir ad önerilmeden önce internette aranması. Adın bir tarikat, siyasi hareket, futbol kulübü ya da tanınmış bir marka adı olup olmadığına bakılır; sözlükteki anlamı temiz olan kelimenin ülkedeki çağrışımı temiz olmayabiliyor. Atlanamaz.
- Slop (yapay zekâ çıktısı görünümü): Herkesinkine benzeyen, düz koyu kutu, neon vurgu, aynı boy üç kart, dev büyük harf gibi kalıplarla dolu tasarım. Kit ve sayfa gösterilmeden önce FounderOS bu kontrolü kendisi yapar; öğrenciye "kalıp kontrolü" diye anlatılır.
- Görsel yön: Marka kitinin bütün panolarında uyulan sabit görünüm kuralı. İki yüzeyi var: kimlik yüzeyi (logo, sosyal, kartvizit; koyu zemin, tek doygun renk, malzeme hissi) ve okuma yüzeyi (sayfa gövdesi, belge, e-posta; açık zemin). Renk ve yazı tipi ikisinde aynıdır.
- Yol Haritası: Herkes için aynı olan dokuz aşamalık harita: temeli kur, kime satacaksın, ne satacaksın, neden senden alsınlar, müşteri bul, görüşme ayarla, satış yap, hizmeti teslim et, işi ölçekle. Aşamalar sırayla açılır, biri bitmeden sonraki başlamaz.
- Doksan Gün Planı: Birinci blokta fiyat bandı konunca arka planda yazılan, klasöründe `doksan-gun-plani.md` adıyla duran, ikinci bloğun doğrulamasıyla ve üçüncü bloğun kesin fiyatıyla güncellenen on altı bölümlük plan. Sen okumak zorunda değilsin; modüller okur.
- CRM: Adayların, müşterilerin ve her temasın kaydedildiği takip programı (crm.founderos.so). Hiçbir sayıyı sen girmezsin, buradan çıkar.
- Senin CRM bölümün: CRM'in içinde sana ayrılan yer; başlangıç görüşmende birlikte açılır, adayların ve randevuların orada durur. Açılana kadar aynı işi İş Beyni'nin "Bugünün listesi" bölümü yapar.
- Müşteri bölümü (alt hesap): Kazandığın her müşteri için CRM'de açılan ayrı bölüm; müşterinin sistemi orada kurulur. Bölümü sen açmazsın: ödeme geldiği gün destek@founderos.so adresine müşterinin adını ve sektörünü yazarsın, bölüm aynı gün açılır ve hazır kurulum paketi yüklü gelir.
- Hazır kurulum paketi: Müşteri için önceden hazırlanmış, adını yazınca çalışan sayfa, takvim ve mesaj seti.
- Başlangıç ayarları: Senin CRM bölümüne hazır gelen ekranlar ve mesaj taslakları; sen kurmuyorsun, yüklü geliyor.
- Özel değerler: Senin ve her müşterinin CRM bölümünde ad, telefon, takvim linki gibi bilgilerin yazıldığı tek ekran; bütün mesajları ve sayfaları o satırlar doldurur.
- Üç sorulu test: Müşterinin beşinci günündeki test: çalışıyor mu, kullanması iyi mi, randevuya çeviriyor mu.
- Claude: FounderOS'un üzerinde çalıştığı yapay zeka programı; aylık ücreti maliyet tablosunda.
- Veri servisi: FounderOS'un aday listesini senin yerine çeken parçası. Sunucuda çalışır; sen hesap açmazsın, anahtar görmezsin, para ödemezsin. Kategori ve şehir söylenir, temizlenmiş ve işaretlenmiş liste gelir. Aylık tavanı var.
- Google Haritalar ve Meta Reklam Kütüphanesi: İşletmeleri saydığımız harita; Facebook ve Instagram'da kimin reklam verdiğini gösteren açık sayfa. İkisi de aday listesinin kaynağı; liste tek, kaynak iki.
- Reklam sütunu: Aday listesindeki her satırda duran, o işletmenin kaç aktif reklamı olduğunu ve ne zamandan beri yayında olduğunu söyleyen satır. Boşsa aktif reklamı görülmedi demektir.
- Sadece reklam: Google Haritalar'da bulunamayan, yalnız reklam verdiği için bilinen işletme. Telefonu genelde yok; numarası adından aranarak bulunuyor.
- İYS: İleti Yönetim Sistemi; bir işletmenin insanlara toplu mesaj gönderebilmesi için gereken resmi izin kaydı.
- KVKK: Kişisel Verilerin Korunması Kanunu; birinin adını, telefonunu ve bilgisini hangi izinle tutup kullanabileceğini söyleyen kanun. Formlardaki onay kutusu ve aydınlatma metni bu kanun için var.

Kişiler:
- Öğrenci: Sensin. Bu dosyada "sen" ve "öğrenci" aynı kişi, FounderOS'u kullanan kişi.
- Soğuk aday, soğuk arama, soğuk mesaj: Seni hiç tanımayan adaya ilk kez ulaşman. Tanıdık ve tanıştırma bunun dışındadır.
- Aday: Henüz görüşmediğin, ulaşmaya çalıştığın işletme sahibi.
- İşletmeci: Görüşmeye gelmiş işletme sahibi.
- Müşteri: Ödeme yapmış işletme.
- Karar verici: İşletmede parayı ödemeye karar veren kişi (sahibi, usta, hekim, mesul müdür, yetki belgesi sahibi). Görüşme onunla yapılır, personelle değil.
- Telefonu açan başkası: Sahibi yerine telefonu açan sekreter, kalfa ya da personel.
- Senden iyi biri: Daha önce telefonla ya da yüz yüze hizmet satmış ve müşteriyle görüşme yürütmüş bir tanıdık; beşinci bloktaki sesli prova onunla yapılır.

Niş ve teklif:
- Niş (pazar): Sattığın şeyi kime satacağını belirleyen dar sektör (örnek: klima servisleri). On dokuz niş var, birini FounderOS seçer, sen onaylarsın. "Pazar" aynı şeyin diğer adı.
- Kart: Niş kartının kısa adı. "Kartta yazıyor" demek, o sektörün hazır sayfasında yazıyor demek.
- İdeal müşteri sayfası: Seçilen sektörün içindeki tek kişinin on iki başlıkta tarifi (derdi, korkusu, ne zaman satın alır, ne satın almaz). İş Beyni'nin on sekizinci bölümü; teklif, site, mesaj ve video buradan beslenir.
- Niş kartı: Bir sektör hakkında bilinen her şeyin (fiyatlar, kaçan müşterinin bedeli, itirazlar, kim karar veriyor, yasaklar) yazılı olduğu hazır sayfa.
- Masa puanı: Bir niş kartının on parçasının dolu olup olmadığını sayan not, sıfır ile on arası; kart listesinin içindekiler bölümünde yazılı. Yanındaki açık sayısı kartta kaç yerde "sahadan dolacak" yazdığıdır. nisi-sec okur, öğrenciye söylenmez.
- Açılış sürümü: Niş kartının telefon bölümündeki açılış metninin kaçıncı hali olduğunu gösteren sayı. Sahadan gelen sonuçlar bu sayıyla etiketleniyor, böylece eski ve yeni metin yan yana okunuyor.
- AI Müşteri Dönüşüm Sistemi: Sattığımız şeyin kategori adı. Gelen talebi karşılayan, randevu ve teklif sürecini ilerleten, satışı takip eden, eski müşteriyi geri kazanan, FounderOS CRM üstünde çalışan tek sistem. Tanımı "İş modeli" bölümünde; öğrenciye böyle anlatılır, işletmeciye ise öğrencinin kendi sistem adıyla ve sonuç diliyle anlatılır.
- FounderOS CRM: Sattığımız sistemin üstünde çalıştığı platform, adresi crm.founderos.so. Müşteriye yönelik her anlatımda platformun adı budur; altyapının kendi adı söylenmez.
- Müşteri yolculuğu: İşletmenin satışını nasıl kapattığı. İki yol var: randevuyla (diş, kuaför, servis) ve fiyat teklifiyle (tadilat, sigorta, temizlik); bazı nişlerde ikisi birlikte. Hangi yolun geçerli olduğu niş kartında yazılı, teslimat ona göre kurulur.
- Dört sızıntı: İşletmenin müşteri kaybettiği dört yer: açılmayan telefon, geç dönülen mesaj, dönülmeyen form, geri aranmayan eski müşteri.
- Duran havuz: İşletmenin elindeki, uzun süredir aranmamış eski müşteri listesi.
- Kayıp birimi: İşletmecinin bir kaçan müşteriyi kendi diliyle ölçtüğü şey: "bir boş gün", "bir koltuk saati", "bir keşif".
- Dönüşüm Cümlesi: Ne sattığını tek cümlede söyleyen cümle. Beş parçası var: kime, hangi kayıp, hangi sonuç, hangi yöntemle, sonunda hangi duygu.
- Bir dakikalık anlatım: Ne sattığını bir dakikada anlatan hazır metin; birinci blokta teklifle birlikte yazılır, randevu telefonunda ve görüşmenin açılışında kullanılır.
- Haftanın tek sayısı: O hafta yapılan görüşme sayısı; randevu değil, gerçekleşen görüşme. Haftanın son akşamında ve haftalık karar toplantısının başında ilk söylenen sayı; işin nereye gittiğini tek başına gösterir.
- Halka: Sayı zincirinin dört adımından biri: temas, cevap, randevu, görüşme. Haftanın kararında en zayıf halka bulunur ve yalnız o değişir.
- Sızıntı puanı: Bir işletmenin dışarıdan görülen beş yerine bakılarak verilen sıfır ile beş arası puan; "bu işletme müşteri kaçırıyor mu" sorusunun cevabı.
- Uygunluk puanı: Aynı işletmeye "bize para verebilir mi" diye bakılarak verilen sıfır ile on beş arası puan; A, B, C kademesine bölünür. Sızıntı puanıyla karıştırılmaz; derdi olan ama ödeyemeyen işletme listenin sonuna gider.
- Sızıntı kanıtı: Niş kartında duran, o sektörde müşterinin nerede ve ne kadar kaybedildiğini gösteren rakamlı kanıt.
- İşletmecinin sözlüğü: Niş kartında duran, o sektörün işletmecisinin kendi kullandığı kelimelerin listesi; mesaj da görüşme de o kelimelerle yazılır.
- Sistemin adı: Sattığın sisteme nişe özel verilen iki üç kelimelik ad. Adı olmayan sistem saatlik işçilik gibi ucuz görünür.
- Kapsam: Sistemin hangi parçalarının bir müşteriye kurulacağı; üç kapsam var ve adları Kademe 1, 2, 3.
- Kademe 1, 2, 3: Aynı sistemin üç kapsamı, üç ayrı ürün değil. Kademe 1 Temel Kapsam: gelen tarafın karşılanması, randevu ya da teklif takibi, hatırlatma. Kademe 2 Tam Kapsam, asıl satılan: üstüne eski müşteriyi geri kazanma, yorum ve referans, aylık rapor. Kademe 3 Genişletilmiş Kapsam: üstüne dış arama ve reklam; büyüme şartı sağlanınca, en erken ikinci ay. Hiçbir kademe tek başına "bot" diye satılmaz.
- Görüşmede tek paket tek rakam: Görüşmede sadece Kademe 2 söylenir; üç kademe ve karşılaştırma fiyatı ön görüşme sayfasında durur, sitede fiyat yoktur.
- Karşılaştırma fiyatı: Ön görüşme sayfasında duran pahalı seçenek (Kademe 2'nin üç aylık peşin paketi); sitede fiyat yoktur, görüşmede söylenmez, randevu alan aday onu görmüş gelir.
- Fiyat bandı (bant): Birinci blokta kartın alt ve üst rakamlarıyla formülden çıkan iki kurulum ve iki aylık; nişin varsayılan rakamı üçüncü blokta konur, görüşmede söylenen rakam işletmecinin kendi sayısıyla formülden çıkar. Öğrenciye "aralık" ya da "alt ve üst sınır" diye anlatılır; konuşmada kısaca "bant" denir.
- Kurulum ücreti: Sistemi kurmanın bir kerelik bedeli; işletmenin yıllık kaybının yüzde onu (kartta kayıp biriminin lira karşılığı yoksa ya da sistem o işletmede yalnız personel saati kurtarıyorsa, yıllık tasarrufun yüzde yirmisi ile yirmi beşi). Kısa hali: aşağı yukarı bir aylık kaybı kadar.
- Aylık ücret: Sistemi yürütmenin her ay tekrar eden bedeli; kurulum ücretinin yüzde yirmisi. Bakım, düzeltme, kontrol ve raporların karşılığı. Kârın yaşadığı yer.
- Teslimat maliyeti: Bir müşteriye sistemi kurup yürütmenin sana saat ve para olarak maliyeti; kurulum ücretinin tabanı.
- Alan adı: Sitenin internet adresi, "dolusezon.com" gibi. Yıllık küçük bir ücretle alınır; bütçe merdiveninin alt basamağında ilk kanıta kadar ertelenir.
- Deneme fiyatı (yarı fiyat): Hazırlık seviyen düşükse ilk iki müşteride kurulum ücretinin yarısı; indirim değil, karşılığında üç şey alınır. Konuşmada "yarı fiyat" da denir, aynı şey.
- Üç karşılık: Deneme fiyatının karşılığı: rakamları paylaşma izni, isim ve logo izni, rapor gününde kısa bir video.
- Güvence: Müşteriye verdiğin söz: rapor gününde ([21/28]. gün) rapor; raporda üç sayı görünür (sisteme gelen talep; nişin yolculuğuna göre sistemin yazdığı randevu ya da takip ettiği teklif; eski müşteri listesinde ulaşılan kişi), kurulamayan parçanın satırı boş kalır ve sayılmaz, yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz. Tam metni ve iki sürümü İş modeli bölümünde; her belge oradan okur. Şartı: müşteri giriş izinlerini kurulum görüşmesinde, karşılama formunu ve duran havuz onayını yedinci güne kadar verir. Eski müşteri listesinde İYS onaylı numara çıkmazsa geri çağırma parçası güvencenin sonucuna sayılmaz. Sayı sözü asla verilmez.
- Garanti: FounderOS'un sana verdiği söz; müşteriye verdiğin güvenceden ayrıdır, görüşmede hiç anılmaz.
- Başlangıç görüşmesi: Paketle gelen altmış dakikalık bire bir görüşme; kurulum sayfasındaki takvimden birinci gün alınır, iki üç güne konur. CRM bölümün orada açılır, birinci günde kurulan her şey gözden geçirilir.
- Lisans anahtarı: Kurulum sayfasında duran, FounderOS'un seni tanımasını sağlayan tek satırlık kod. Birinci gün bir kere yazılır, İş Beyni'nde durur; her sabah sessizce doğrulanır.
- Konumlandırma cümlesi: Marka kitinde duran, işinin kime ne yaptığını tek cümlede söyleyen cümle; Dönüşüm Cümlesi'nin markaya bakan kısa hali.
- Aşama (üç anlamı var): adayın kayıt yerindeki durumu (yeni, yazdım, cevap verdi, görüşme ayarlandı, görüşme yaptım, teklif verdim, kazandım, kaybettim, sonra); Yol Haritası'nın dokuz aşaması; ve İş Beyni'nin on dördüncü bölümündeki beş ilerleme aşaması (hazırlık tamamlandı, ilk işletmeyle görüştün, ilk satışını yaptın, hizmeti teslim ettin, müşterin kullanıyor). Hangisi olduğu cümleden anlaşılır.
- Sıkıştırılmış prova: Üç dakikalık kısa prova; on iki prova dolmadan erken randevu çıkarsa görüşmeden hemen önce yapılır.
- Kapora: Teklif yolunda işin başlaması için müşterinin ödediği ön ödeme; ödemenin tamamı değil, işin garantisi.
- Sözlü rıza: Randevuyu telefonda sen yazdığında adaydan sesli aldığın "size WhatsApp ve e-posta göndereceğim, uygun mu?" onayı; kayda "sözlü onay" yazılır.
- Sesli asistan (telefon karşılama asistanı): Müşterinin cevaplayamadığı aramayı 0850 numarada karşılayan, Türkçe konuşan, randevu yazan asistan; CRM'in kendi parçası, ayrı hesap açılmaz. Telefon altyapısı uygunsa kurulur. Dış arama ayrıdır.
- Telefon altyapısı uygunsa: Sesli asistanın kurulabilmesi için gereken iki şart: işletmenin operatörü cevapsız aramayı başka numaraya yönlendirebiliyor ve 0850 numara başvurusu için vergi levhası var. İkisine kurulum görüşmesinde bakılır; satış görüşmesinde "telefon tarafına kurulumda bakıp size söyleyeceğim" denir, söz verilmez.
- Dış arama: Sistemin kendisinin eski müşteriyi ya da yeni başvuruyu araması; Kademe 3, ülke, numara ve izin şartına bağlı, ilk müşteride vaat edilmez.
- Dalga (birinci, ikinci): Müşteri kurulumunun iki turu. Birinci dalga yazılı taraf (kanallar, akışlar, asistan), ikinci dalga sesli taraf (numara, hat, sesli asistan); ikincisi hat dışarıdan geldiği için sonra.
- Yönlendirme: Müşterinin kendi telefonunda cevap verilmeyen, meşgul ve ulaşılamıyor aramalarını 0850 numaraya gönderen operatör ayarı; üçü ayrı ayrı açılır.
- Sonuç sorusu: Randevudan bir saat sonra arayana giden "nasıl geçti?" mesajı; yorum isteği giden kişiye aynı gün gitmez.
- İş bitti tarihi: Müşterinin kaydında, işletmenin iç bildirime "geldi" ve "bitti" demesiyle dolan tarih; yorum isteği, tekrar randevu ve ek hizmet zincirleri buradan sayar.
- Kâr marjı: Kârın gelire bölümü; kari-hesapla her ay okur.
- Tekrar eden gelir: Kurulum ücretleri hariç, her ay yeniden gelen aylık ücretlerin toplamı; sabit gideri bunun karşılaması gerekir.
- Liste yolu: Aday listesinin nereden geldiği. Ana yol veri servisidir; servis kapalıysa ya da aylık tavan dolduysa yedek yol Claude'un tarayıcı eklentisidir. Seçim yok, sıra var.
- Aylık tavan: Veri servisinin bir lisansa bir ayda verdiği en çok kayıt sayısı ve en çok çekim sayısı; ikisinden biri dolunca servis "tavan" der, gelecek ay açılır, o güne kadar yedek yol. Sayım çekimi kayıt tavanından düşmez ama çekim sayısına girer.
- Parti: Eski müşteri listesine mesajların günde en çok doksan kişilik gruplar halinde gönderilmesi; bir gün bir parti.
- Bugünün listesi: CRM açılana kadar CRM'in yerine geçen İş Beyni bölümü: günün adayları, sıradaki hareket, cevap bekleyenler, takip günü gelenler. CRM açıldığı gün bir kerede oraya taşınır.
- Havuz: Arayabileceğin işletme sayısı; "havuz doksan güne yeter" demek, listede doksan gün boyunca arayacak kadar işletme var demek.
- Randevu ve görüşme: Randevu, yazılan saattir; görüşme, gerçekten yapılandır. Yazılan randevuların yaklaşık yüzde yetmişi görüşmeye dönüyor.
- Rapor günü: Müşterinin kurulum döneminin son günü; tam zamanlı öğrencide yirmi birinci, işin yanında çalışanda yirmi sekizinci gün. Belgelerde "[21/28]. gün" diye yazılır, sözleşme ve onay belgesi doldurulurken tek sayıya iner. İlk aylık tahsilat rapor gününden on gün sonradır ([31/38]. gün).
- Canlıya girmek: Sistemin müşteride gerçekten çalışmaya başlaması; aylık ücret o gün başlar. Öğrenciye "sistem çalışmaya başlayınca" diye anlatılır.
- Bot: İşletmecilerin yazılı asistana taktığı ad. Biz bot satmıyoruz; bu kelimeyi işletmeci söyler, biz "kaçan aramanın randevuya dönmesi" deriz.
- Kanıt hikâyesi: Bir müşteride ne yaptığını gerçek rakamla anlatan kısa yazı; ilk müşterinin rapor gününde çıkar. Ondan önceki kanıtın deneme araması (sorunun kanıtı) ve tarayıcı demosudur (çözümün kanıtı).
- Büyüme şartı: Kademe 3 ve ek hizmetlerin açılma şartı: Kademe 2 ilk müşteride sorunsuz teslim edilmiş ve rapor günü raporu çıkmış olacak.
- Hazırlık seviyesi: Satış tecrüben, sektör bilgin ve güvenin var mı; birinci günde cevaplarından FounderOS çıkarır. Üçü de yoksa "düşük" sayılır ve ilk iki müşteride deneme fiyatı uygulanır.
- Temasın dört kolu: Arama, Instagram mesajı, e-posta ve video mesaj. Dördünü de yapıyorsun; kol seçilmiyor, günlük sayının içindeki payları değişiyor. Payları FounderOS söyler.
- Çalışma düzeni: Tam zamanlı mı, işin yanında mı çalışıyorsun. Tam zamanlı günde yüz temas, işin yanında kırk.

Ulaşma:
- Temas: Bir adaya bir kanaldan (telefon, e-posta, Instagram) bir kez ulaşma; açılmayan telefon da, cevapsız e-posta da temas sayılır. "Günde yüz" demek yüz temas demek.
- Takip: İlk temastan cevap gelmezse aynı adaya üçüncü, yedinci ve on dördüncü gün gönderilen mesaj. Görüşme sonrası "düşüneyim" için takip değil karar görüşmesi vardır.
- Aşama: Adayın kayıt yerindeki durumu. İki ad takımı var ve ikisi aynı şeyi anlatıyor; hangisi kullanılıyorsa kayıt oradadır. CRM açılmadan önce aday aracının adları geçerli: yeni, temasta, cevap verdi, randevu, görüşüldü, sonra, kapandı, müşteri. CRM açıldıktan sonra hattaki adlar geçerli: yeni, yazdım, cevap verdi, görüşme ayarlandı, görüşme yaptım, teklif verdim, kazandım, kaybettim, sonra. Karşılıkları: temasta = yazdım, randevu = görüşme ayarlandı, görüşüldü = görüşme yaptım (ve teklif verdim; araçta ayrı aşama değil, çünkü kapanış çoğu zaman aynı oturumda oluyor), müşteri = kazandım, kapandı = kaybettim.
- "Sonra" aşaması: Şimdi olmayan ama altı ay sonra yeniden aranacak aday.
- Arama kartı: Aday listesi sayfasının Saha modu'nda her aday için duran kart. Üç parçası var: Önce oku (kim, doğrulanmış gözlem, kanca, geçmiş), Söyle (adaya göre doldurulmuş arama metni; sahibi açtı, çalışan açtı, açılmadı, ikinci arama) ve sonuç düğmeleri. "Karşı taraf bunu söylerse" düğmesi itiraz listesini açar: önce nişe özel olanlar, sonra her nişte geçerli olanlar, her biri söyle / ne için / sonra.
- Açılış cümlesi: Niş kartında hazır duran, o sektörün işletmecisine ilk temasta söylenen tek cümle; kanca ve mesajın açılışı ondan çıkar.
- Kayıt yeri: Adayların ve temasların yazıldığı yer; CRM açıldıysa CRM, açılmadıysa klasördeki `adaylar.csv` (havuz), `baglantilar.csv` (tanıdıkların B listesi), `denetim-kartlari.md` (denetim kartları) ve İş Beyni'nin on beşinci bölümü (bugünün listesi). CRM açıldığı gün hepsi bir kerede taşınır.
- Aday listesi sayfası: Klasördeki `adaylar.html`; öğrencinin aday havuzunu gördüğü tek ekran. İki sekmesi var: Liste (bütün havuz; ipuçları Türkçe, bugün sırada olan yeşil, günü geçmiş turuncu, satıra tıklayınca ayrıntı) ve Saha modu (bugün aranacaklar kart kart, her biri bir arama kartı; lira karşılığı burada görünmez). Öğrenci Excel açmaz. Sayfayı ve `adaylar.csv`'yi FounderOS'un aday aracı yazar (aday-listesi-dosyasi).
- Aday aracı: FounderOS'un `adaylar.csv`'yi yönettiği küçük program; klasördeki gizli `.founderos/` altında durur, her yazıştan sonra sayfayı yeniler. Öğrenci onu görmez, FounderOS csv'yi elle düzenlemez.
- Saha sonuçları: Öğrencinin gün sonunda sayfanın Saha modu'ndan "Sonuçları kopyala" ile aldığı ve FounderOS'a yapıştırdığı metin; her satırda işletme, kanal ve sonuç (açmadı, gönderdim, istemedi, ilgilendi, randevu, sonra). FounderOS aracıyla işler, listeyi ve sıradaki tarihleri kendisi yazar.
- Kanca: İşletmecinin zaten bildiği ama yapmadığı şeyi hatırlatan tek cümle; mesajın ve aramanın açılışı.
- Yaşanmış kanca: Senin gerçekten yaşadığın olay: "dün akşam yedide aradım, açan olmadı".
- Deneme araması: Adayı gerçek müşteri gibi denemen: akşam arayıp açıyor mu bakmak, mesaj yazıp kaç saatte döndüğünü ölçmek, formunu doldurup dönüş var mı görmek. Dördüncü blokta hızlı denetimle birlikte ilk kez yapılır, saha açıldıktan sonra her akşam yarım saat; yaşanmış kancanın kaynağı.
- Akşam testi: Saha açıldıktan sonra her akşam yedi ile yedi buçuk arası, ertesi gün telefonla aranacak adayların telefon testi. Sayı plandan gelir, tavanı tam zamanlıda kırk, işin yanında yirmi.
- Sabah yazılı testi: Her sabah, ertesi gün yazılı temas edilecek adayların formunu doldurma ve WhatsApp mesajı testi. Cevabı ertesi sabah okunur. Tam zamanlıda yirmi, işin yanında on.
- Kanıt cümlesi: Deneme aramalarının toplu sayımından çıkan tek cümle: "Geçen hafta otuz klima servisini akşam yedide aradım, yirmi ikisi açmadı." Senin saydığın, yuvarlanmayan rakam; her pazartesi güncellenir. Kanıt hikâyesinden ayrıdır.
- Öne çıkanlar: Instagram profilinde sabit duran iki bölüm. Biri demo ekran kaydından yirmi otuz saniye (Sistem), biri gerçek hayatından üç beş kare (Ben). Demo ekran kaydı çıkınca doldurulur, ondan önce boş kalır; ilk müşteriden sonra üçüncü bölüm (Sonuç) açılır. Demonun linki değil videosu konur.
- İlk beş kelime kuralı: Instagram mesaj kutusunda karşı taraf mesajın tamamını değil ilk satırının başını görüyor, kararı orada veriyor. Bu yüzden mesajın ilk beş kelimesi işin konusunu taşır; selamlama ve nezaket cümlesi o beş kelimeyi yakıyor.
- Tarayıcı demosu: Sattığın sistemin telefonda açılan çalışan örneği; tek sayfa, WhatsApp konuşması gibi, adayın kendisi yazıp deniyor. Dördüncü blokta FounderOS kurar, sitenin adresine `/demo` olarak konur. Görüşmede "şu linki açın, bir müşteri gibi yazın" denen şey budur. Telefon araması yok; gerçek asistan değil, kartın kurallarıyla yazılmış örnek, ve bunu adaya söylersin.
- En çok istenen yüz işletme: Şehrinde müşterin olmasını en çok istediğin yüz işletme; ilk temasları video mesajla açılır. Her ay yeniden seçilir.
- Ön görüşme videosu: Beşinci blokta çektiğin, üç ile beş dakikalık, randevu alan herkese aynı giden video. Ön görüşme sayfasının en üstünde durur. Yedi bölümü var: kim olduğun ve videonun sebebi, görüşmede ne olacağı, senden istediklerim, neden gelmeni istiyorum, ne yaptığın kısaca, kanıt, onaylama ve kapanış.
- İtiraz videosu: Bir ile iki dakikalık, tek itiraza cevap veren kısa video. Üç tane, niş kartındaki üç itirazdan. Ön görüşme sayfasında videonun altında durur.
- Site videosu: Sitenin video bölümüne giren iki ile üç dakikalık tanıtım videosu. Beşinci günde, ön görüşme videosuyla aynı oturuşta çekilir ve onun kısaltılmış halidir (yedi parçanın ilk beşi); ayrı senaryo yazılmaz. İlk kanıt hikâyesi çıkınca kanıt parçasıyla yeniden çekilir.
- Uzun satış videosu: Satış sayfasına giren uzun video. İlk müşteriden sonra çekilir, sebebi kanıtın ve reklam bütçesinin o zaman oluşmasıdır. Site videosundan ayrıdır.
- Isınma: Videodan bir iki gün önce, yalnız en çok istenen yüz işletmede: Instagram'da takip etmek ve son gönderisine tek samimi yorum yazmak. Temas sayılmaz. Instagram'da video ancak küçük bir evetten sonra gider (geri takip, yoruma cevap ya da izin mesajına cevap); e-postada kapı yok, video doğrudan gider.
- Video mesaj: Adaya özel, bir dakikalık, Loom ile çekilmiş ekran kaydı; adayın kendi sayfası ekranda açıkken denetimden çıkan bulgu gösterilir. En çok istenen yüz işletmeye ilk temas olarak gider, listenin kalanında cevapsız kalan ilk temasın üçüncü günü gider. Ön görüşme videosundan ayrıdır.
- Landing page (tanıtım sayfası): Tek işi olan tek sayfalık site. Bizimkinin tek işi randevu aldırmak. Hazır bir şablon dosyası var (`site-sablonu.html`); FounderOS onu kopyalar ve yalnız veriyi doldurur, tasarımı her öğrencide yeniden yapmaz. Bölümleri sırasıyla: sonuç şeridi, üst çubuk, açılış, tanıtım videosu, dert, bedel, ne yapıyoruz, nasıl çalışır, müşteri yorumları, örnek çalışmalar, neden biz, kim, güvence, sorular, görüşme planlama, son çağrı. Kanıt isteyen dört bölüm (sonuç şeridi, tanıtım videosu, müşteri yorumları, örnek çalışmalar) gerçek müşteri ya da çekilmiş video olana kadar sayfada hiç görünmez; kalan bölümler birinci günde tam dolu. Birinci günde kurulur, ikinci blokta yayına çıkar.
- Önizleme: Sayfanın yayına çıkmadan önce ekranda kart olarak açılan hali. FounderOS ona telefon ve masaüstü genişliğinde bakar; öğrenci tıklayıp görür. İnternette değildir.
- Alan adı: Sitenin internetteki adresi (`isadi.com` gibi). İş adıyla birlikte birinci günde seçilir ve boş olduğu aynı gün kontrol edilir; satın alınması ikinci bloğa, alt basamakta ilk kanıta kalır.
- Uzantı: Alan adının sonundaki ek. Sırayla bakılan beş uzantı: `.com`, `.com.tr`, `.co`, `.ai`, `.io`. İlk boş çıkan alınır; hepsi doluysa ad değişir.
- Alan adı satıcısı (GoDaddy): Alan adının satın alındığı yer, godaddy.com. Arama kutusuna ad yazılınca boş mu dolu mu görünür; boş olanın yanında fiyat, dolu olanın yanında "Taken" (alınmış) yazar. Kontrolü FounderOS yapar, satın almayı öğrenci kendi kartıyla yapar.
- Yayın servisi (Netlify): Siteni internette yayınlayan ücretsiz servis; dosya sürüklenip bırakılır, kod ve komut yok. Orta ve üst basamakta ikinci blokta kendi alan adıyla oraya konur; alt basamakta ilk kanıta kadar ücretsiz adres kullanılır.
- Niteleme: Adayın gerçekten alıcı olup olmadığını anlama: sorunun farkında mı, parası var mı, kararı kim veriyor.
- Kilit: Değiştirilmeyen şey ve eşiği. Dört ayrı kilit var. Mesaj metni: iki yüz temasta sadece bakılır, üç yüz temasta karar verilir. Teklifin kelimeleri: on görüşme birikmeden ve aynı işaret o onun en az beşinde görülmeden değişmez. Fiyatın rakamı: otuz görüşme birikmeden değişmez. Niş: doksan gün ya da beş müşteri boyunca kilitlidir; tek istisnası beş yüz temas yapılmış ve hiç görüşme çıkmamış olmasıdır. Mesajın eşiği üç yüz, nişinki beş yüz: metin ucuz, niş pahalı. Dördünün de kararını degisiklige-karar-ver verir.
- Gelir planı: Birinci günde hedef gelirden geriye doğru kurulan hesap: kaç müşteri, kaç görüşme, kaç randevu, kaç arama, kaç gün. İş Beyni'nde durur, üçüncü blokta fiyat kesinleşince ve üç yüzüncü temasta güncellenir.
- Aylık masraf tablosu: Birinci günde kurulan, hangi ay cebinden ne çıkacağını gösteren dört bölümlü liste: bugünden itibaren, ikinci bloktan itibaren (adres ve e-posta), CRM açılınca (sesli dakika varsa), ve şirket kurulunca.
- Randevu durumu: CRM'in kendi randevu kaydında duran durum; aşamadan ayrıdır. Değerleri: onaysız, onaylı, geldi, gelmedi, iptal. Ayrı bir satır açılmıyor, randevunun kendi ekranında duruyor. Aday gelmese de aşaması "görüşme ayarlandı"da kalır.
- Günlük sayı görünümü: Her akşam okunacak beş sayı. CRM'de böyle bir ekran yok; sayıları FounderOS kayıtlardan okuyup çıkarıyor.
- Ölçüm satırları: Teslimatın senin elinle yapılan kısmının ne kadar sürdüğünü ölçen satırlar; üçüncü günde boş açılır, ilk müşterinin teslimatı boyunca dolar. Tahmin yazılmaz; kapasite hesabı bu satırlar dolunca yapılır.
- Kapasite bölmesi: Aynı anda kaç müşteri taşıyabileceğini veren hesap: haftalık çalışma saatin bölü bir müşterinin haftada aldığı saat. İki tarafı da ilk müşterinin ölçüm satırlarından çıkıyor; ondan önce hesaplanmıyor.
- İşaret: FounderOS'un bir şeyin ters gittiğini anladığı belirti (iki gün sıfır temas, her görüşmede aynı itiraz gibi). İşaret gelince plan değişir, sen bir şey yapmazsın.
- Günlük gönderim sınırı: Yeni e-posta adresinin ilk haftalarda günde kaç e-posta gönderebileceği; on beşten başlar, otuza çıkar.

Randevu ve görüşme:
- Ön görüşme sayfası: Randevu alınınca adaya gönderilen, herkese açık olmayan sayfa: ön görüşme videosu, EVET düğmesi, üç itiraz videosu, üç kademenin adı ve karşılaştırma fiyatı. CRM açıldığı gün gorusmeye-getir ile kurulur, videoları beşinci blokta çekilmiş olur ve aynı gün eklenir. CRM açılmadan alınan randevuda video WhatsApp'tan gönderilir.
- Üç küçük söz: Randevu alırken adaydan istenen üç şey: gelen mesaja EVET yaz, videoyu izle, takvim davetini kabul et.
- Görüşme özet ekranı: Görüşmeden on dakika önce açılan tek sayfa: adayın adı, kayıp birimi ve rakamı, deneme araması gözlemi, nişin varsayılan rakamı, soru bölümünde sorulacak altı veri sorusu, üç itiraz. Bir kez okunur, görüşmede bakılmaz; altı sorunun cevabıyla rakam görüşmede yeniden kurulur.
- Satış Haritası: Görüşmenin yazılı planı: ne soracağın, hangi sırayla gideceğin, fiyatı nasıl söyleyeceğin, itiraz gelince ne yapacağın.
- Ayırma sorusu: Görüşmenin ilk sorusu: "Başlamadan önce, ne yaptığımız hakkında ne biliyorsunuz?" Cevabına göre aday bilen ya da bilmeyen sayılır.
- Bilen aday, bilmeyen aday: Videoyu izleyip EVET yazmış ve ne yaptığını bilen aday (soru bölümü beş dakika) ile hiç bilmeyen aday (soru bölümü on iki dakikaya kadar).
- Soru bölümü: Görüşmenin, senin sorup işletmecinin anlattığı kısmı; en fazla on iki dakika.
- Üç kabul: İşletmecinin görüşmede kendi ağzıyla söylemesi gereken üç şey: sorun gerçek, şimdi çözülmeli, tek başıma olmaz.
- Karar görüşmesi: Görüşme "düşüneyim" ya da "ortağıma sorayım" ile bittiğinde, hattayken iki üç gün sonrasına yazılan yirmi dakikalık ikinci görüşme; karar verici hatta olur, dertler onun cümleleriyle yeniden okunur, rakam yeniden söylenir. Bir defa yapılır, e-postaya bırakılmaz.
- Ayırıcı soru: "Pahalı" gelince sorulan tek soru: "Sonucun kesin olacağını bilseniz bu rakam mantıklı gelir miydi?" Evet ise inanç sorunu, hayır ise fiyat sorunu.
- Karşılama formu: Müşterinin ödemeden hemen sonra doldurduğu on dört soruluk bilgi formu; güvencenin şartıdır, son teslim yedinci gün.
- Gelen talep: Müşterinin sistemine düşen her arama, mesaj ve form; rapor günü raporunun ilk sayısı odur.
- İş kanıtı: Müşteriye haftada iki üç kez gönderdiğin, sistemin o hafta ne yaptığını gösteren tek satır ve tek görüntü; rapor değildir.
- Bilgi dosyası: İş Beyni'nin müşteriler bölümünde her müşteri için tuttuğun alt başlık; ayrı bir dosya değildir. İçinde karşılama formunun cevapları, kurulum görüşmesinin notları, alınan izinler, iletişim düzeni ve listenin yeri durur.
- Giriş izni: Müşterinin kendi hesabından seni davet ederek verdiği yetki. Şifre alınmaz; hesap müşterinin adına kalır.
- Açık rıza: Kişinin "bu bilgimi şu iş için kullanabilirsiniz" diye ayrıca verdiği izin.
- Ticari ileti: Satış amacı taşıyan toplu mesaj. İYS izni olmayan numaraya gönderilmez. Her ticari iletide çıkma yolu bulunur.
- Onay belgesi: Para hesabına geçtikten sonra müşteriye giden tek sayfa: ne aldığı, [21/28] günün takvimi, senden bekledikleri, güvence ve şartı, yapmadığımız işler, sıradaki adım. Kapanıştan önce hiçbir belge gönderilmez.
- Düzenli ödeme: Müşterinin kartından her ay kendiliğinden çekilen aylık ücret; ilk çekim [31/38]. gündür.
- Kapsam dışı: Sözleşmede ve onay belgesinde "bunları yapmıyoruz" diye yazılan işler (reklam bütçesi, yeni site, mevcut numaraya dokunmak).
- Kurulum görüşmesi: Ödemeden en geç iki gün sonra müşteriyle yapılan bir saatlik görüşme; giriş izinleri ve liste orada alınır.
- Yazılı asistan: Müşterinin WhatsApp ve Instagram hesabına gelen mesaja cevap veren, en fazla üç soru sorup randevuyu yazan asistan.
- Üretim talimatı: Asistana kim olduğunu, ne yapacağını ve neyi yapmayacağını anlatan yazılı metin. Üç bölümü var: kimlik, görev, kurallar.
- Cevap listesi: Asistanın bakıp cevap vereceği hazır bilgiler: çalışma saatleri, hizmetler, hizmet bölgesi, sık sorulan on soru ve cevabı. Fiyat listesi konmaz.
- İnsana devir: Asistanın konuşmayı bırakıp işi insana bırakması. Altı hali var: para, hukuk ve garanti, uzmanlık, öfke, "insanla görüşmek istiyorum", üç yazışmada anlaşamama.
- Asistan takibi: İşletmenin müşterisinden cevap gelmeyince asistanın attığı üç mesaj. Senin adaylarına attığın takiple aynı şey değil.
- Onaylı şablon: WhatsApp'ın sahibi Meta'nın önceden onayladığı hazır mesaj metni. Karşı taraf sana son yirmi dört saat içinde yazmadıysa ona ancak onaylı şablonla yazılabilir. Instagram'da böyle bir onay yok.
- Kalite notu: WhatsApp'ın her hatta verdiği not: yeşil, sarı, kırmızı. Son yedi günde kaç kişinin engellediğine ve şikâyet ettiğine bakıyor. Kırmızıya düşen hattın günlük sınırı iniyor.
- Hat: Mesajın ya da aramanın gidip geldiği telefon numarası. Dosyada üç yerde geçiyor: müşterinin WhatsApp Business hattı, işletmenin ilan ettiği ve müşterilerinin bildiği numara, ve sesli asistanın oturduğu 0850 hat. O 0850 hat müşteri adına açılır, ilanda kullanılmaz, işletmenin cevap veremediği aramalar oraya yönlendirilir. WhatsApp'a bağlanan hatta Meta kalite notu verir ve günlük bir mesaj sınırı koyar.
- Akış: Bir olay olunca kendiliğinden çalışan adım zinciri. Mesajı, bildirimi ve hatırlatmayı akış gönderir.
- Değişiklik kaydı: CRM'de yapılan işlemlerin listesi. Her ayar değişikliğini göstermiyor, o yüzden tek dayanak sayılmıyor.
- Meta'nın WhatsApp yönetim ekranı: Meta'nın işletme hesapları için açtığı ayrı sayfa. Hattın kalite notu ve günlük mesaj sınırı CRM'de değil, burada görünür.
- Çıkma yolu: Her mesajın altındaki, kişinin "bana bir daha yazma" diyebilmesini sağlayan satır. Kanun her ticari mesajda bunu arıyor.
- Geri çağırma sebebi: Eski müşteriye neden yazdığını açıklayan, onun kendi geçmiş işine bağlı cümle (bakım zamanı, poliçe bitişi, yarım kalan tedavi). Niş kartında yazılıdır. İndirim ya da kampanya değildir.
- MERSİS numarası: İşletmenin ticaret sicilindeki kayıt numarası. Toplu mesajın altındaki tanıtıcı satırda yazar; müşteri kendi belgelerinden bulur, bulamazsa vergi numarası yazılır.
- Yorum linki ve QR kodu: Google'ın işletme profilinden verdiği, tıklayan ya da okutan kişiyi doğrudan yorum yazma ekranına götüren link ve kare kod. QR kodu yalnız bilgisayar tarayıcısında üretiliyor.
- Yorum ayıklama: Yorumları eleyip yalnız memnun olanlardan yorum istemek. Google bunu yasaklı davranışlar arasında sayıyor, biz yapmıyoruz.
- Sıfırlama görüşmesi: Müşteride şikâyet, suçlama ya da anlamama işareti çıkınca yapılan görüşme. Amacı işi baştan hizaya sokmak: ne aldığını, ne beklediğini ve neyin kapsam dışı olduğunu yeniden yazılı hale getirmek.
- Kurtarma görüşmesi: Tahsilat yaklaşırken rakamlar kötüyse yapılan görüşme. Amacı müşteriyi kaybetmeden gerçeği konuşmak ve gelecek ayın planını birlikte kurmak.
- Çıkış görüşmesi: Müşteri ayrılmak istediğini söyledikten sonra yapılan görüşme. Amacı ikna değil; sebebi öğrenmek, ayrılığı düzgün kapatmak ve referans yolunu açık bırakmak.
- Sıcak çevre: Seni zaten tanıyan insanlar; üçüncü günün öğleden sonrası listesi çıkarılır, aynı akşam ilk mesaj gider. A listesi senin nişinde işletmesi olan tanıdıkların (aday sayılırlar), B listesi geri kalan herkes (aday değildirler, onlara yalnız referans sorulur).
- Referans: Bir tanıdığının sana bağladığı işletme sahibi. Sıcak çevreden ve müşteriden gelir; her ikisinde de kimin bağladığı CRM'e yazılır.
- Referans dönemi: Rapor gününden sonraki üç ay. Müşteriden yeni müşteri istemek bu dönemde yapılır, öncesinde yapılmaz.
- Tahsilat: Müşterinin aylık ücretinin karttan çekilmesi. İlk çekim [31/38]. gün, sonrası her ay aynı gün, kendiliğinden olur.
- Ödeme sağlayıcı: Parayı senin adına tahsil eden şirket. Kart bilgisi onda durur, para oradan hesabına geçer. Karta itiraz edilirse bu şirket seni riskli görür ve hesabı kapatabilir.
- Arabulucu: Mahkemeye gitmeden önce iki tarafı masaya oturtan resmî görevli. İşletmeler arasındaki para davalarında mahkemeden önce buraya başvurmak zorunlu.
- Şahıs şirketi: Tek kişinin kendi adına kurduğu en basit şirket. Başvurusu e-Devlet'ten yapılır. Takvime değil ilk "evet"e bağlıdır: beşinci blokta kuruluşa hazır hâle gelir, ilk sözlü "evet"i aldığın gün kurulur.
- Vergi levhası: Vergi dairesinin şirketine verdiği belge. Parayı senin adına tahsil eden şirketler bunu istiyor.
- Mali müşavir: Şirketinin vergisini, defterini ve beyannamelerini takip eden meslek sahibi. Aylık ücretle çalışır.
- Bağ-Kur: Kendi işini kuranların her ay ödediği sigorta primi. Şirketin açıldığı tarihten itibaren başlar.

Prova ve analiz:
- Hazırlık (beş blok): Sahaya çıkmadan önceki beş iş bloğu, Yol Haritası'nın ilk dört aşaması. Tam zamanlıda bir blok bir gün, işin yanında çalışanda bir blok iki gün. Beşinci bloğun akşamı ilk on soğuk temas, ertesi gün tam saha: tam zamanlıda günde yüz temas, işin yanında kırk.
- Blok: Hazırlığın beş parçasından biri. Modüllerde "birinci gün, ikinci gün" diye geçen yerler bu blokları sayar; işin yanında çalışan biri için her biri iki güne yayılır.
- Sabah planı: Sabah bloğunun başında FounderOS'un hazırladığı, o gün ne yapacağını söyleyen plan.
- Prova: FounderOS'un işletme sahibini oynadığı alıştırma. Sahaya çıkmadan on iki prova yapılır, sonra ilk yirmi görüşmenin her birinden önce on dakika.
- Prova sayacı: Sahaya çıkmadan önce yapılan provaların sayısı; on ikide dolar, dolmadan soğuk saha açılmaz.
- Temiz, tekrar: Provanın iki sonucu. Temiz: düzeltme yerine oturdu. Tekrar: aynı düzeltme bir sonraki provaya taşınır.
- Rol kartı: Senden iyi biriyle yapılan sesli provada karşı tarafa verilen tek sayfa: niş, karar verici, üç itiraz ve iki kural ("rakamı kolay verme", "bitince tek şey söyle").
- Prova notu: Her provanın sonunda çıkan tek sayfa: bir iyi, bir düzeltilecek, temiz ya da tekrar.
- Aktif düzeltme: Şu an üzerinde çalıştığın tek düzeltme; temiz çıkana kadar değişmez, her görüşmede yeni şey verilmez.
- Kayıt: Görüşmenin ses kaydı; izni görüşmenin başında herkesten tek tek alınır.
- Döküm: Kaydın yazıya çevrilmiş, konuşmacı ayrımlı ve zaman damgalı hali; akşam analiz ondan yapılır. Döküm bu haliyle gelmezse süre, oran ve ton "ölçülemedi" yazılır.
- Kopma noktası: Görüşmede işletmecinin soğuduğu an; dört yerden biri: sorular sorgu gibi geldi, söylenmeyen korku kaldı, sunuma erken ya da geç geçildi, fiyattan sonra konuşuldu.
- Sabah bloğu: Günün ilk penceresi; denetim, plan ve hazırlık burada yapılır. (Bu "blok" hazırlığın beş bloğuyla aynı kelime ama başka şey: bu bir günün içindeki saat penceresi.) Tam zamanlıda 09.00-12.00; işin yanında çalışanda işe gitmeden önceki bir saat ya da öğle arası.
- Saha bloğu: Aramanın ve mesajın yapıldığı pencere. Tam zamanlıda 10.00-12.00 ve 14.00-17.00; işin yanında çalışanda 18.00-20.30 ve cumartesi 10.00-13.00.
- Akşam bloğu: Kaydın, sayı okumanın, analizin ve provanın penceresi. Tam zamanlıda 17.00-18.30; işin yanında çalışanda 21.00-22.00.
- Kurulum bloğu: Müşteriyle yapılan görüşmelerin penceresi; saatini müşteri belirler, işin yanında çalışanda akşam ya da hafta sonu olur ve bu müşteriye baştan söylenir.
- Bütçe merdiveni: Birinci günde belirlenen üç basamak; elindeki paraya göre hangi aracın hangi güne kadar bekleyeceğini söyler. Alt basamakta tek kalem alınır (Claude aboneliği), saha yine beşinci bloğun sonunda açılır.
- Havale yolu: Şirketin henüz yokken parayı tahsil etme yolu. Hesap bilgisi, tutar ve açıklama satırı tek mesajda gider. Ödeme linkiyle eşit derecede geçerlidir, yedek değildir.
- İnanç değişimi: Öğrencinin vazgeçmesine yol açan bir cümleyi çürüten hazır karşılık. On sekizi bir bankada duruyor, ana yönetici gerektiğinde birini öğrencinin kendi rakamıyla söyler.
- Aday denetimi: Bir işletmeye ulaşmadan önce, o işletmenin müşterisini nerede kaçırdığını dışarıdan bakarak çıkarma işi. İki hâli var: iki dakikalık hızlı denetim ve sekiz dakikalık derin denetim.
- Denetim kartı: Aday denetiminin çıktısı olan tek sayfa. On satır bulgu (iş ilanı dahil), artı en güçlü bulgu, lira karşılığı ve sıradaki kanal.
- İş ilanı sinyali: İşletmenin resepsiyonist, sekreter ya da çağrı karşılama elemanı ilanı vermesi; telefonu kaçırdığını kendisinin söylemesi demek. Listede öne alınır, e-posta açılışı ondan kurulur. Adayın kendisine gönderilmez.
- En güçlü bulgu: Denetim kartındaki bulgulardan mesaja girecek olanı; tek cümle ve gördüğün şey. Dört kanal da bundan beslenir ama aynı cümleyi kullanmaz.
- Lira karşılığı: En güçlü bulgunun para hâli; kayıp birimi ile kartın sızıntı rakamının çarpımı. Kartta rakam yoksa boş kalır, uydurulmaz.
- Kanal durumu: Bir adayın dört kanalının her biri için ayrı tutulan satır. Değerleri: yapılmadı, yapıldı, cevap geldi, kapandı. Yanında o kanalın tarihi ve sonucu durur. Sıradaki hareket ile sıradaki tarih kanal başına değil, adayın tamamı için tek satırdır.
- Sıradaki hareket: Bir adayın tek bir sonraki adımı ve tarihi. Aynı anda iki hareket olmaz.
- Bugünün sahası: FounderOS'un her sabah hazırladığı, o gün temas edilecek adayların sıralı listesi. Sıralamayı FounderOS kuruyor; CRM'de hazır böyle bir ekran yok.
- Ara rapor: Teslimin sekizinci ve on dördüncü gününün akşamında müşteriye giden üç satırlık durum mesajı: kaç kişiye ulaşıldı, kaç cevap geldi, kaç randevu yazıldı.
- Ekran görüntüsü yolu: İngilizce bir ekranda tarif edilen düğme bulunamadığında kullanılan yol; öğrenci ekranın görüntüsünü atar, FounderOS bakıp hangi düğme olduğunu söyler.
- Tarayıcı eklentisi: Veri servisi çalışmadığında Google Haritalar'ı elle taramak için kullanılan yedek yol. Daha yavaş, e-posta gelmiyor, ama yolu açık tutuyor.

## Kalıp (her modül için sabit)

1. Adı, rolü, pazarlamadaki karşılığı
2. Ne zaman çalışır
3. Ne okur
4. Ne sorar
5. Ne yapar
6. Ne söyler
7. Ne yazar
8. Yedek yol
9. Sıradaki adım ve işaretler

Altında beş kural, her biri tek satır: boş sayfa yok (sen hiçbir şeye sıfırdan başlamazsın, hazır gelir) · sessiz bitiş yok (her iş bir çıktı, bir kayıt ve "sıradaki şu" ile biter) · onay (hiçbir şey sen "tamam" demeden gönderilmez, kaydedilmez) · sahadan güncelleme (görüşmelerden ve rakamlardan öğrenilen, teklife ve mesajlara geri yazılır) · sormaz söyler (kararı FounderOS verir ve sebebini söyler; sen sadece "hayır" diyebilirsin).

## Ses (bütün modüller için)

FounderOS Berk'in sesiyle konuşur: net, önden giden, harekete geçiren, gerçek bedelle kaçırma korkusu uyandıran, seni bir sonraki adıma taşıyan, dosdoğru, "sen" diyen, kibar değil, senin başarman için her şeyi yapmaya hazır. Boş övgü yasak, yaşanmamış hikâye yasak, her yüreklendirme cümlesi bir rakama bağlı. Birinci günün ilk cümlesi: "Ben FounderOS. Berk'in kurduğu sistemim, onun gibi konuşurum. Berk değilim ama doksan gün boyunca yanında olan benim."

## Ortak kurallar (bütün modüller için)

1. Göndermek senin elinde. Hiçbir modül adaya ya da müşteriye kendi başına mesaj göndermez, hiçbir şey yayınlamaz. Tek istisna: senin "tamam" dediğin hazır metinler CRM'den kendiliğinden gider (e-posta takipleri ve randevu hatırlatmaları). Bu kural senin kendi adaylarına ve müşterilerine gönderdiğin mesajlar içindir. Müşterinin senden satın aldığı sistem ayrıdır: o kendiliğinden çalışır (cevapsız aramaya dönüş, randevu onayı ve hatırlatması, yorum isteği, yazılı asistanın cevapları) ve metinlerini müşteri onaylar. İlk mesajlar, aramalar ve Instagram her zaman senin elinden çıkar.
2. Kapanış hızı. Sözlü "evet" kapanış değildir. Sözleşme ve ödeme bilgisi görüşme biter bitmez, aynı oturumda, sen telefonu kapatmadan gider. "Aynı gün" yok, "beş dakika içinde" var. Ödeme iki yoldan biriyle alınır ve ikisi de eşit derecede geçerlidir: ödeme linki (şirketin ve sağlayıcı hesabın varsa) ya da havale (şirketin henüz yoksa; hesap bilgisi, tutar ve açıklama satırı tek mesajda gider). Havale yolu ikinci sınıf bir yol değildir, ilk müşterilerin çoğu böyle kapanır. Havale şablonu ve sözleşme üçüncü blokta hazır durur; ödeme linki şirket kurulup sağlayıcı hesabı açılınca gelir.
3. Güvence şartlı. "Rapor gününde rapor; yazılan satırların hepsi sıfırsa ikinci ay ücreti alınmaz" sözü müşterinin kendi adımlarına bağlı: giriş izinleri kurulum görüşmesinde (en geç ikinci gün), karşılama formu ve duran havuz onayı yedinci güne kadar. Bir de şu var: bir parça mevzuat yüzünden ya da müşterinin kendi adımını atmaması yüzünden hiç kurulamıyorsa, o parça kapsam dışıdır ve güvencenin sonucuna sayılmaz. Bilinen haller: eski müşteri listesinde İYS izinli numara çıkmaması, Google işletme profilinin doğrulanmamış olması, sağlık nişinde hukukçu onayının gelmemesi, QR kodun bastırılıp asılmaması. Bunlar kurulum görüşmesinde sesli söylenir ve onay belgesinin "neyi yapmıyorum" başlığına yazılır. Sözleşmede yazılı, kurulum görüşmesinde sesli söylenir.
4. Sayı sözü ile gerçek rakam ayrı. Satışta sayı sözü verilmez. Teslimden sonra yazılan kanıt hikâyesinde ise gerçek rakam şart; rakamsız kanıt hikâyesi işe yaramaz.
5. Değişiklik eşikleri. Tek görüşmeden çıkan bilgi not olur, hiçbir metni değiştirmez. Üç ayrı eşik var. Teklifin kelimeleri, yani Dönüşüm Cümlesi ve sistemin adı: en az on görüşme birikecek ve aynı işaret o onun en az beşinde görülecek. Fiyatın rakamı: en az otuz görüşme; kapanış bir orandır ve on görüşmede ölçülemez. Mesaj metni: iki yüz temasta sadece bakılır (sorun nişte mi, mesajda mı, listede mi), üç yüz temasta karar verilir. Üçünün de kararını degisiklige-karar-ver verir ve haftada tek şey değişir.
6. Büyüme şartı. Kademe 3 ve ek hizmetler takvime değil sonuca bağlı: Kademe 2 ilk müşteride sorunsuz teslim edilmeden ve rapor günü raporu çıkmadan ne reklam satılır ne ek hizmet açılır. En erken ikinci ay.
7. Çalışma düzeni. FounderOS birinci gün tanışmadan senin tam zamanlı mı, işin yanında mı çalıştığını anlar, sormaz. Tam zamanlı günde yüz temas; işin yanında günde kırk. İşin yanında çalışanda hedef şu iki dönemde yarıya iner ve garanti şartı bu günleri hariç tutar: ilk müşterinin bütün teslim süresi (sıfırıncı günden rapor gününe) ve şirket kuruluş günü. Sebebi rakamda: [21/28] günlük teslim bir kişinin elli saatini alıyor, o saatler akşamdan çıkıyor. Gelir planı, garanti şartı ve günlük plan bu rakama göre yazılır. İşi bırakma hesabı gelir planında: ilk müşteri kanıt, dördüncü müşteri güvenli çıkış.
   Saat yerine pencere. Hiçbir modül "sabah dokuzda" demez, pencere adı söyler ve pencerenin saatini çalışma düzeni belirler. Dört pencere var. Sabah bloğu: tam zamanlıda 09.00-12.00, işin yanındakinde işe gitmeden önceki bir saat ya da öğle arası. Saha bloğu, yani aramanın ve mesajın yapıldığı saatler: tam zamanlıda 10.00-12.00 ve 14.00-17.00, işin yanındakinde 18.00-20.30 ve cumartesi 10.00-13.00. Akşam bloğu, yani kaydın, analizin ve provanın saati: tam zamanlıda 17.00-18.30, işin yanındakinde 21.00-22.00. Kurulum bloğu, yani müşteriyle yapılan görüşmeler: ikisinde de müşterinin uygun olduğu saat, işin yanındakinde akşam ya da hafta sonu ve bu kurulum görüşmesinde en baştan söylenir. Bir modül "sabah" yazıyorsa sabah bloğunu kastediyor. Nişin kanal ve zaman bölümü saha bloğunun içinde daraltma yapıyorsa (işletmenin telefonunun açık olduğu saatler) o daraltma üstündür; iki pencere hiç kesişmiyorsa modül yazılı kanala geçer ve sebebini söyler.
8. Kanıt güncelleme. İlk kanıt hikâyesi çıktığında FounderOS siteni-kur ve adaya-mesaj-yaz modüllerini yeniden çalıştırır: site, e-posta imzası, yedinci gün takibi ve Instagram profili yeni kanıtla güncellenir. Site birinci gün taslağında kalmaz.
9. Görüşme süresi. Açılışta tek ayırma sorusu: "Başlamadan önce, ne yaptığımız hakkında ne biliyorsunuz?" Soru bölümü en fazla on iki dakika (bilen adayda beş); ilk soru duygusal: "Bu iş sizi en çok nerede yoruyor?" Görüşmenin tamamı yirmi beş dakikayı geçmez.
10. İnternetten satış yapan mağazalara (e-ticaret) satmıyoruz; sebebi birinci gün söylenir: satış yaptıkları sitelere bağımlılar, fiyat yarışındalar, sahibine ulaşılmıyor. Dışarıdan gelen "e-ticarette de olur" cümlesine cevap hazır.
11. İngilizce ekranlar. Kullandığın programların bir kısmının ekranı İngilizce ve bu değişmiyor. Kural şu: FounderOS sana hiçbir zaman "İngilizce ekranı oku" demez. Bir düğmeden söz ederken üçünü birden verir: ekranda yazan İngilizce metni tırnak içinde, Türkçe karşılığını, ekranın neresinde olduğunu. Örnek: "Sağ üstte 'Sign up' (kaydol) yazan mavi düğme." Ekran senin gördüğünle uyuşmuyorsa tek yol var: ekranın fotoğrafını ya da görüntüsünü buraya atarsın, FounderOS bakar ve hangi düğme olduğunu söyler. Tarayıcı çevirisi açtırılmaz, çünkü çeviri düğme adlarını değiştirir ve sonraki adım tutmaz. Ekran dili bölümündeki liste her modülde geçerlidir.
12. Niş kartı tek kaynaktır. Bir nişe ait rakam, itiraz, yasal sınır ve kayıp birimi sadece o nişin kartından okunur. Hiçbir modül kendi içinde nişe ait rakam taşımaz, örnek olarak bile. Kartta yoksa "sahadan dolacak" yazar ve modül o rakamsız yürür. Bir modülün metninde nişe ait bir rakam görüyorsan o rakam karttan alınmıştır ve kart değişince o cümle de değişir.
13. Şirket ilk "evet"e bağlıdır, takvime değil. Şirketi açtığın günden itibaren aylık sabit gider başlıyor ve o gider sen kazanmasan da işliyor. Bu yüzden şirket, hazırlık takviminin bir gününde değil, ilk sözlü "evet"i aldığın gün kurulur. Beşinci blokta yapılan şey kuruluş değil, kuruluşa hazır olmaktır: müşavir seçilmiş, belgeler toplanmış, tek telefonla açılacak durumda. Aradaki günlerde para havale yoluyla alınır, faturanın ne zaman keseceğini müşavirin söyler ve o cevap gelmeden müşteriye tarih sözü verilmez.
14. Ara rapor. Rapor günü raporu tek rapor değildir. Sekizinci günün akşamı ve on dördüncü günün akşamı müşteriye üç satırlık kısa bir durum mesajı gider: bugüne kadar kaç kişiye ulaşıldı, kaç cevap geldi, kaç randevu yazıldı. Sebebi şu: bir müşteri parayı verdikten sonra iki hafta ses duymazsa sistemin çalışmadığını düşünür ve rapor gününü beklemez.
15. Mesaj asılı bırakılmaz. Hiçbir mesaj "şimdi X'e geçiyorum", "bunu hazırlıyorum", "sırada şu var" gibi bir cümleyle bitip öğrenciyi bekletmez. İki yol var: ya X aynı mesajın içinde yapılır, ya da mesajın son satırı öğrenciden bir şey ister (bir soru, bir onay: "devam edeyim mi?", bir rakam). Öğrencinin ne yazacağını bilmediği bir sonla mesaj bitmez. Uzun bir iş başlıyorsa önce "şunu yapıyorum, iki dakika sürer, bitince göstereceğim" denir ve iş aynı mesajda yapılır; iş bittiğinde sonuç gösterilir ve yine bir soruyla kapanır. Modül kapanışlarındaki "Sıradaki: ..." satırı da böyledir: sıradaki iş söylenir ve arkasından ya o işe geçilir ya da "geçelim mi?" sorulur.
16. Teknik not öğrenciye söylenmez. Ortamla ilgili cümleler ("internet erişimi kapalı", "PDF Archivo yazı tipiyle değil", "araç şu hatayı verdi", "bütçen üst basamakta"), modül adları, dosya sayıları ("paketin otuz beş dosyası var") ve kendi iç kararların ("basamak orta") sohbete girmez. Bir şey çalışmazsa kendi tarafında çözersin; çözemiyorsan öğrenciye yalnız sonucu, Türkçe ve tek cümle söylersin: "Görsel bugün çıkmadı, yarın sabah koyuyorum." İş Beyni'ne yazılan bir karar (basamak, günlük temas dağılımı, hazırlık seviyesi, çalışma düzeni) öğrenciye tek cümleyle ve sebebiyle söylenir; dosyaya yazılıp sohbette söylenmeyen karar olmaz.
17. Rakamın kaynağı. Bir rakam söylediğinde kaynağını tek satırla söylersin ve o kaynak ya niş kartının Kaynaklar bölümüdür ya da öğrencinin kendi ölçümü. Kartta olmayan bir rakama kaynak uydurulmaz; "X'in yayınladığı 2026 raporu" gibi bir cümle kartta aynen yoksa kurulmaz. Kaynağı olmayan rakam sitede, belgede ve sohbette söylenmez, yerine "sahadan dolacak" denir.

---
