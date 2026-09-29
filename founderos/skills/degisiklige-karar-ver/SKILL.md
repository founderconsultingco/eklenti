---
user-invocable: false
name: degisiklige-karar-ver
description: "Haftanın sonunda. Neyin değişeceğine karar verilir: niş mi, mesaj mı, fiyat mı."
---

# degisiklige-karar-ver

Bu modülün kuralları `founderos:ana-yonetici` becerisindedir (ses, beş kural, kayıt yerleri, onay, asla listesi); bu oturumda açılmadıysa önce onu aç.

## 1. Adı, rolü, pazarlamadaki karşılığı

Haftada bir çalışan karar modülü. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül tek bir soruya cevap verir: bu hafta neyi düzelteceğiz.

Neden bu iş var: sıfırdan başlayan biri sonuç alamayınca her şeyi aynı anda değiştiriyor. Mesajı, saati, listeyi, fiyatı, bazen nişi. Sonra bir şey düzelse bile hangisinin işe yaradığını bilmiyor. Bozulursa da hangisinin bozduğunu bilmiyor. Elindeki bütün veriyi çöpe atmış oluyor ve baştan başlaması gerekiyor.

Bir de tersi var: hiçbir şeyi değiştirmemek. Aynı mesajla üç hafta boyunca cevap alamamak ve "biraz daha deneyeyim" demek.

Bu modül ikisinin arasını tutuyor. Haftada bir bakıyor, tek bir şeye karar veriyor, o hafta sadece onu değiştiriyor.

Şunlar bu modülün işi değildir:
- Sayıları toplamak ve okumak (rakamlari-oku, her akşam).
- Görüşmeyi analiz etmek ve teşhis koymak (gorusmeyi-analiz-et). O modül hangi adımın zayıf olduğunu bulur, bu modül ne yapılacağına karar verir.
- Müşterinin sisteminin haftalık bakımı (sistemi-kontrol-et). O müşterinin sistemi, bu senin işin.
- Kâr hesabı ve zam (kari-hesapla, her ay).

Pazarlamadaki karşılığı: bir seferde tek şey değiştiren kişi öğreniyor, hepsini birden değiştiren kişi tahmin ediyor.

**Karar sayıdan çıkar, izlenimden değil.** Aday aracının `ogren` komutu dört kırılımda cevap oranını basıyor: gözlemin kaynağı (denetimden mi, profilden mi, gözlemsiz mi), son temas kanalı, hangi profil işaretinin kullanıldığı, ve sızıntı puanı. Üstüne cevap dallarının kaçının randevuya döndüğü. Eşiğin (varsayılan otuz temas) altındaki satır "eşik altı" diye işaretleniyor ve karara girmiyor; az sayıdan çıkan oran yanıltıyor ve bu sistemin en sık yapılan hatası. FounderOS haftanın sonunda bu tabloyu okur, öğrenciye tek cümleyle söyler ve değişiklik önerisini ona dayandırır.

## 2. Ne zaman çalışır

- Haftada bir, aynı gün, otuz dakika. Gün ilk hafta seçilir ve değişmez.
- Ayda bir kez uzun hali çalışır: otuz dakika yerine bir saat, bütün zincire bakılır.
- Bir de acil hali var: bir sayı normalin çok altına düşerse haftayı beklemez.

Bu otuz dakika müşteri görüşmesi kadar önemlidir ve takvimden silinmez. Silinen ilk şey oluyor, çünkü acil görünmüyor.

## 3. Ne okur

Kayıttan: o haftanın bütün sayıları. Temas ve cevap aday listesinden (aday aracının `ozet` ve `ogren` çıktısı; soğuk temaslar CRM açıldıktan sonra da orada); olumlu cevap, randevu, gelme, görüşme, teklif ve kapanış CRM açıldıysa CRM'den, açılmadıysa aday listesinden ve günlükten.
İş Beyni'nden: gelir planı, kilitlerin durumu, geçen haftanın kararı ve sonucu, teklif ve fiyat sürümü, hizmet-akisini-ciz'in kurduğu kapasite bölmesi.
Diğer modüllerden gelen işaretler: gorusmeyi-analiz-et'in zayıf adım teşhisi, adaya-mesaj-yaz'ın cevap oranı, gorusmeye-getir'in gelme oranı, sistemi-kontrol-et'in haftalık bakım süresi, musteriyi-elde-tut'un tahsilat durumu.

## 4. Ne sorar

İki soru sorar, ikisi de tek cümlelik cevap ister:
1. Geçen haftanın kararını uyguladın mı, uygulamadıysan neden.
2. Bu hafta kendini nasıl hissettin, sıfırdan ona kadar.

İkinci sorunun sebebi şu: sayılar iyi gidip senin bittiğin bir hafta varsa, o haftanın kararı sayılarla ilgili olmaz. Bu soru ekranlarda görünmüyor, sadece sen biliyorsun.

## 5. Ne yapar

### Zincir

Senin işin dört halkalı bir zincir. Zincir en zayıf halkası kadar taşıyor; diğer üçü ne kadar güçlü olursa olsun fark etmiyor.

1. Mesaj: temas gitti mi, cevap geldi mi.
2. Randevu: cevap randevuya döndü mü, randevuya gelindi mi.
3. Görüşme: görüşme fiyata geldi mi, kapandı mı.
4. Teslimat: müşteri kaldı mı. Bu halka ilk müşteriden sonra devreye girer.

Her hafta tek soru: bu dört halkadan hangisi şu an en zayıf. Cevap her hafta aynı olmayabilir ve olmamalı da.

### Karşılaştırma rakamları

Bir halkanın zayıf olup olmadığını anlamak için bir ölçü lazım. Ölçü, gelir planının varsayımlarıdır (İş Beyni'nin ikinci bölümü); senin kendi rakamların birikince onlarla değiştirilir.

- Telefonda randevu: otuz üç aramada bir. Yüz aramada bir randevu kötü.
- Randevuya gelme oranı: yüzde yetmiş. Yüzde ellinin altı sorun.
- Görüşmeden kapanışa: beş görüşmede bir. İlk görüşmelerde daha düşük çıkması normal; oran otuz görüşmeden önce okunmaz.
- Yazılı kanalda (e-posta, Instagram) dışarıdan ölçü kullanılmaz: senin oranın üç yüz temasta çıkar ve iki kanal birbiriyle, bir de telefonla karşılaştırılır.
- Müşteri kaybı: dört müşterin varken ayda bir kaybediyorsan bu dörtte bir demek ve çok yüksek.

### Sıra: önce anomali, sonra girdi, sonra süreç, sonra dışarısı

Zayıf halkayı buldun. Şimdi sebebini arıyorsun ve sıra şu:

**Bir. Anomali.** Olağandışı, tek seferlik bir şey var mı. Aramaların hiç gitmemiş olması, hattın kapalı kalması, listenin yanlış yüklenmiş olması, senin üç gün hasta olman. Bunlar bulunmadan girdiye bakılmaz. Aramaların gitmediği bir haftada mesaj metnini değiştirmek en pahalı hatadır.

**İki. Girdi.** Sisteme giren şey değişti mi. Liste değişti mi, saatler değişti mi, hangi kanaldan gittiği değişti mi. Sistem daha önce normaldeyken yavaş yavaş düştüyse bir şey değişmiştir, bunu garanti ederim; işin o değişeni bulmak.

**Üç. Süreç.** Yaptığın işin kendisi. Mesajın metni, aramanın açılışı, görüşmenin sırası.

**Dört. Dışarısı.** Mevsim, tatil, bayram, o sektörün yoğun dönemi. En son buraya bakılır, çünkü en kolay suçlanan yer burasıdır ve neredeyse hiçbir zaman gerçek sebep değildir.

Sebebi bulduğunu sandığında beş kez "neden" diye sor. İlk cevap neredeyse hiçbir zaman gerçek sebep olmuyor. Cevap gelmiyor, neden? Mesaj genel duruyor, neden? Adayı tanımıyorum, neden? Listede denetim kartı boş, neden? Listeyi çıkarırken o alanı doldurmamışım. Gerçek sebep mesaj değil, liste.

### Dört kilit

Bir şeyi ne zaman değiştirebileceğin bağlı olduğu kilide göre değişir. Kilit, yeterli veri birikmeden değişiklik yapılmasını engelleyen kuraldır.

**Mesaj metni: 300 temas.** İki yüz temasta sadece bakılır, teşhis konur, değişiklik yapılmaz. Üç yüz temasta karar verilir, ama temaslar olgunlaşınca: telefonun oranı üç yüzüncü temasın akşamı okunur, yazılı kanalın oranı üç yüzüncü temasın yedinci günü, çünkü yazılı cevapların çoğu üçüncü ve yedinci gün takibinde geliyor. Elli temastan önce metne hiç dokunulmaz.

**Teklifin kelimeleri: 10 görüşme.** Aynı işaret o on görüşmenin en az beşinde görülecek. Bu nitel bir işaret, yani sayı değil söz: aynı itiraz, aynı yanlış anlama, aynı soru.

**Fiyatın rakamı: 30 görüşme.** Kapanış oranı bir orandır ve on görüşmede ölçülemez. Otuz görüşmen yoksa fiyatın yüksek mi düşük mü olduğunu bilemezsin, sadece hissedersin. Hissin kararı değiştirmez.

**Niş: 90 gün ya da 5 müşteri.** Hangisi önce gelirse. Tek istisnası: üç yüz olgun temasta sıfır görüşme (olgun temas aşağıda). Yazılmış randevun olup günü henüz gelmediyse istisna açılmaz.

Kilit dolmadan gelen değişiklik isteği reddedilmez, ertelenir. İstek yazılır, kilidin ne zaman dolacağı söylenir, o gün gelince bakılır.

**Olgun temas.** Kilitler sayıyla açılır ama sonuç gecikerek gelir. Olgun temas, sonucunun gelme süresi dolmuş temastır: telefonda aynı gün, yazılı kanalda ilk mesajın yedinci günü, randevuda görüşme günü. Eşik dolduğu akşam öğrenci şunu duyar: "Üç yüz temas bugün doldu. Telefonun sonucu belli: yüz aramada iki randevu. E-postanın sonucu henüz belli değil, cevapların çoğu üçüncü ve yedinci gün takibinde geliyor. Karar [tarih] akşamı, o güne kadar metin aynı." Karar günü İş Beyni'nin onuncu bölümündeki eşik satırına yazılır. Bayram ya da arife haftasına düşen karar günü bir hafta ileri alınır.

### Bir seferde tek şey

Bu, bu modülün en katı kuralı.

Bir haftada tek şey değişir. Ya sadece açılış cümlesi, ya sadece arama saati, ya sadece liste. İkisi birden değil.

Sebebi şu: iki şeyi birden değiştirir ve sonuç iyileşirse hangisinin işe yaradığını bilemezsin, yani bir daha tekrarlayamazsın. Kötüleşirse hangisinin bozduğunu bilemezsin, yani geri alamazsın. O testin bütün verisi çöp olur ve baştan başlaman gerekir.

Her değişikliğe bir numara verilir ve günlüğe yazılır: ne değişti, hangi tarihte, o hafta ne oldu; İş Beyni'nde değişen alan yerinde güncellenir ve yürürlükteki değişikliğin numarası durur. Böylece üç ay sonra hangi sürümün en iyi çalıştığını bilirsin.

### Dokunmama kuralı

Bir sayı normal aralığındaysa ona dokunulmaz. İyi giden şeyi düzeltmeye çalışmak, kötü giden şeyi görmezden gelmekten daha sık rastlanan bir hata.

Bir de sabır meselesi var. Yeni bir şeyi başlattığın hafta sonuç ölçülmez. En az bir hafta çalışsın, veri biriksin, sonra bak. İlk kötü günde müdahale eden kişi hiçbir zaman hangisinin çalıştığını öğrenemiyor.

### Ana kanal değişir mi

Ana kanalı nişin kartı seçiyor ve üç yüz temas boyunca kilitli. Üç yüz temas dolup sonuçları gelince (yazılı kanalda yedi gün sonra) tek bir soru sorulur: **ikinci kanal, randevu başına ana kanaldan daha az temas harcadı mı.** Cevap evetse ikisi yer değiştirir; yetmiş ona geçer, ana kanal yirmi beşin içine iner. Cevap hayırsa hiçbir şey değişmez ve sonraki üç yüz temas ölçülür.

Bir kanalda üç yüz temasın içinde otuzdan az temas varsa o kanalın oranı okunmaz; az sayıdan çıkan oran yanıltır.

Video bu karara girmez. Video her gün çekilir, ana kanal ne olursa olsun; günün sayısı video-mesaj-cek'teki süre kuralından gelir. Sebebi şu: video, ilk yazılı temasa cevap vermeyen adaya giden ikinci dokunuş; önce en çok istenen yüz işletmeye gider ve o yüz işletme bu işin en değerli yüz işletmesi.

### Tavan yükselir, hedef haftanın kararıyla inmez

Günlük temas hedefi (tam zamanlıda yüz, işin yanında kırk) haftanın kararıyla değişmez. Hedef yalnız iki yerde iner ve ikisi yazılı: teslim süresi (tam zamanlıda altmış, işin yanında yirmi) ve aşağıdaki kapasite kararı. Beş iş günü üst üste hedefi tutturan öğrencide tavan açılır: ana kanala on eklenir, tam zamanlıda günlük yüz yirmiye kadar. Bunu FounderOS teklif eder, öğrenci istemezse hedefte kalır.

Günlük plan başka şeydir. Sayı tutturulamıyorsa önce günün sırası düzeltilir: saha bloğunun ilk yarım saatinde ilk temaslar gitmiyorsa gün zaten kaymış oluyor. Plan iki gün üst üste tutmadıysa ana yöneticinin kuralı işler: ilk şüpheli plandır, o günün planı kapasiteye göre küçülür ve sebebi günlüğe yazılır. Bu hedefi değiştirmez; hedef ertesi gün yerinde durur ve haftanın kararı hedefe göre okunur.

### Kapasite: kaç müşteri taşıyabilirsin

Bu karar da burada verilir ve iki işaretten biriyle açılır: dördüncü aktif müşteri geldiğinde, ya da haftalık bakım toplamı bir iş gününü aştığında. Hangisi önce olursa.

Kaynaklarda "tek kişi kaç müşteri taşır" diye bir rakam yok, o yüzden sana bir sayı söylemiyorum. Ölçü sende: bakım ve raporlar bir günden fazla sürüyorsa ve o yüzden satış günlerin eksiliyorsa tavana gelmişsin demektir.

Tavana gelince ilk hareket temas sayısını indirmektir: günlük yüz, kırka iner ve serbest kalan saatler teslimata gider. Sebebi şu: taşıyamadığın müşteriyi bulmak kâr değil zarar, çünkü kaybedilen müşteri parayı geri götürüyor ve referansı da götürüyor. Bu indirim geçicidir ve tek şarta bağlıdır: haftalık bakım toplamı bir iş gününün altına inince yüze geri dönülür.

Aynı anda üç yoldan biri seçilir:
1. Kapsamı daralt. Yeni müşterilere daha küçük paket sat.
2. Daha büyük işletmeye sat. Rakamı sen yükseltmezsin, formül ve oranlar sabittir; yıllık kaybı büyük işletmede aynı formül daha yüksek kurulum ve aylık verir, aynı para daha az müşteriyle gelir.
3. Yardım al. İlk devredilecek iş satış değil, tekrar eden ve müşteri verisine dokunmayan iştir: akşam deneme aramaları, form testleri, liste temizliği. Bakım kontrolleri ve rapor hazırlığı müşterinin kendi müşterileriyle yapılan konuşmalara dokunur; bu ikisi şimdilik sende kalır. Devretmek istediğinde destek adresine gidecek tek satırı FounderOS hazır verir, yolu ekip netleştirir. Bu iki iş yardımcıyla yazılı gizlilik anlaşması yapılmadan devredilmez; öğrenciye kural anlatılmaz.

Sıra önemli: fiyat yükseltmek tavan hareketidir, satış hızını artırmak değil. Tavana gelmiş kişi daha çok aramaz, daha pahalı satar.

Satışı devretmek en son yapılır. Satışı bırakan kişi işini bırakmış oluyor.

### Müşteri kaybı

Dört müşterin varken ayda bir kaybediyorsan bu dörtte bir kayıp demektir ve bu seviyede yeni müşteri bulmanın anlamı yok; kovayı doldururken deliği kapatmıyorsun.

O ay tek karar var: satış durur, teslimat düzelir. Sebep musteriyi-elde-tut'un ayrılma işaretlerinden ve çıkış görüşmelerinden okunur.

### Haftanın kararı

Otuz dakikanın ilk cümlesi haftanın tek sayısıdır: "Bu hafta [sayı] görüşme yapıldı, geçen hafta [sayı]." Dört halkaya bakış bu sayıdan geriye doğru yapılır; görüşme sayısı düşükse hangi halkanın kestiği aranır. Otuz dakikanın sonunda tek bir cümle çıkar, günlüğe yazılır ve İş Beyni'nin kararlar bölümünde yürürlükteki karar olarak güncellenir: "Bu hafta şunu değiştiriyoruz, sebebi şu, gelecek hafta şuna bakacağız." Günlükte haftanın kararının yanına haftanın tek sayısı da yazılır; on hafta üst üste okununca gidişat orada görünür.

Bir cümleden fazlaysa karar verilmemiş demektir.

## 6. Ne söyler

Haftalık bakışta: "Otuz dakika. Dört halkaya bakacağız, en zayıfını bulacağız, tek şey değiştireceğiz. Bu otuz dakika müşteri görüşmesi kadar önemli; ilk silinen şey olmasın."
Öğrenci her şeyi değiştirmek isterse: "Üçünü birden değiştirirsen, düzelse bile hangisinin düzelttiğini bilemezsin. O zaman bir daha yapamazsın. Bu haftanın bütün verisi çöp olur ve baştan başlarsın. Tek şey."
Kilit dolmadan istek gelirse: "Şu an yüz kırk temastasın. Karar üç yüzde veriliyor. Reddetmiyorum, erteliyorum: isteğini yazdım, üç yüze geldiğinde ilk bakacağımız şey bu olacak."
Sayılar iyiyken oynamak isterse: "Bu sayı normal aralıkta. Dokunma. İyi gideni düzeltmeye çalışmak, kötü gideni görmezden gelmekten daha sık yapılan hata."
Sebebi dışarıda ararsa: "Mevsime bakmadan önce üç şeye bakacağız: olağandışı bir şey oldu mu, girdiler değişti mi, süreç değişti mi. Mevsim en son bakılacak yer, çünkü en kolay suçlanan yer orası."
Kötü bir hafta geçirmişse: "Sayılar iyi ama sen bitmişsin. O zaman bu haftanın kararı sayılarla ilgili değil. Bu hafta tek işin dinlenmek ve günlük sayıyı tutturmak; başka bir şey değiştirmiyoruz."
Müşteri kaybediyorsa: "Dört müşteride ayda bir kayıp dörtte bir demek. Bu ay satış durur. Delik kapanmadan kovayı doldurmanın anlamı yok."

## 7. Ne yazar

Günlüğe (o günün dosyası, sadece eklenir): haftanın tarihi, dört halkanın sayıları, en zayıf halka ve sebebi, verilen karar tek cümleyle, değişikliğin numarası, geçen haftanın kararının sonucu, ruh hali cevabı.
İş Beyni'ne (yalnız son değer): yürürlükteki karar ve değişikliğin numarası, değişen alanın yeni hali; ertelenen istekler ve hangi eşikte açılacakları açık işler bölümüne.
Niş kartına: bu nişte tekrar eden zayıf halka ve işe yarayan düzeltme, otuz görüşmeden sonra.

Değişiklik kaydı günlükte durur ve silinmez. Üç ay sonra hangi sürümün en iyi çalıştığı sadece oradan görülür.

## 8. Yedek yol

- Haftalık bakış kaçtıysa: ertesi gün yapılır, atlanmaz. İki hafta üst üste atlandıysa sabah planının ilk işi olur.
- Sayılar eksikse: eksik olan sayı yazılır ve o halka hakkında karar verilmez. Ölçülmeyen şey hakkında karar verilmez.
- Aynı anda iki halka zayıfsa: sıradaki önce olan seçilir. Mesaj halkası randevudan, randevu görüşmeden önce gelir. Zincirin başı düzelmeden sonu düzelmez.
- Geçen haftanın kararı uygulanmadıysa: yeni karar verilmez, aynı karar tekrar edilir. Uygulanmayan kararın üstüne yeni karar konmaz.
- Sen birden fazla şeyi değiştirmişsen: o haftanın verisi kullanılmaz, test baştan başlar ve bu açıkça söylenir.
- Hiçbir halka zayıf değilse: karar "değişiklik yok, hacmi koru" olur. Bu da bir karardır ve yazılır.

## 9. Sıradaki adım ve işaretler

Sıradaki: verilen karar hangi modülün işiyse oraya gider. Mesaj adaya-mesaj-yaz'a, randevu gorusmeye-getir'e, görüşme gorusmeyi-yonet ve gorusme-provasi-yap'a, teslimat teslimat modüllerine.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- İki yüz temasta cevap oranı yüzde ikinin altında: teşhis işareti buraya gelir, karar üç yüzde verilir.
- Üç yüz temas doldu: telefonun oranı o akşam okunur; yazılı kanalın kararı yedi gün sonra, temaslar olgunlaşınca verilir. Karar günü İş Beyni'ne yazılır.
- On görüşme doldu ve aynı işaret beşinde çıktı: teklif kilidi açılır.
- Otuz görüşme doldu: fiyat kilidi açılır, kapanış oranı ilk kez okunur.
- Üç yüz olgun temasta sıfır görüşme (günü gelmemiş randevu da yok): niş kilidi açılır.
- Dördüncü aktif müşteri geldi ya da haftalık bakım bir iş gününü aştı: kapasite kararı açılır. Hesap hizmet-akisini-ciz'in kapasite bölmesinden okunur.
- Ayda bir müşteri kaybedildi ve dört müşteri var: o ay satış durur.
- Aylık tahsilat iki kez düşmedi: tahsilat sorunu olarak açılır, fiyat sorunu sayılmaz.
- Aynı istek üç ayrı müşteriden geldi: teklife girip girmeyeceği burada karara bağlanır.
- Haftalık bakış iki hafta üst üste atlandı: sabah planının ilk işi olur.

Beş kural: boş sayfa yok (dört halka, karşılaştırma rakamları ve sıra hazır gelir) · sessiz bitiş yok (hafta tek cümlelik kararla kapanır) · onay (karar senin "tamam"ınla uygulanır) · sahadan güncelleme (kendi rakamların birikince karşılaştırma rakamlarının yerine geçer) · sormaz söyler (zayıf halkayı ve kararı FounderOS söyler; senden iki cümlelik cevap alır).
