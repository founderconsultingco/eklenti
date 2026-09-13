---
user-invocable: false
name: rakamlari-oku
description: "Her akşam. Günün beş sayısı ve tek cümle."
---

# rakamlari-oku

## 1. Adı, rolü, pazarlamadaki karşılığı

Her akşam çalışan modül. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül günün sayılarını okur ve tek cümlede nerede olduğunu söyler.

Neden bu iş var: sıfırdan başlayan biri sayıya bakmadığı için nerede olduğunu bilmiyor. Bilmediği için ya olduğundan kötü sanıyor ve bırakıyor, ya olduğundan iyi sanıyor ve yanlış yerde ısrar ediyor.

İkinci sebep: yazılmayan sayı yok sayılıyor. Kaydetmeyen kişi tahmin ediyor, tahmin eden kişi de hep kendi hissine göre tahmin ediyor. Kötü bir görüşmeden sonra bütün hafta kötü sanılıyor, oysa rakam öyle demiyor olabilir.

Üçüncü sebep, en önemlisi: doğru sayıya bakmak kadar yanlış sayıya bakmamak da lazım. Bazı sayılar iyi görünüp hiçbir şey söylemiyor. Onlara bakan kişi çalıştığını sanıyor.

Şunlar bu modülün işi değildir:
- Karar vermek. Bu modül sayar ve gösterir; ne değişeceğine degisiklige-karar-ver karar verir.
- Görüşmeyi analiz etmek (gorusmeyi-analiz-et). O modül akşam bundan önce çalışır, bu modül sayıları oradan alır.
- Kâr hesabı (kari-hesapla, ayda bir).

Pazarlamadaki karşılığı: ölçmediğin şeyi yönetemezsin, ama yanlış şeyi ölçersen yanlış şeyi yönetirsin.

## 2. Ne zaman çalışır
- Her akşam, günün sonunda. Beş dakika sürer.
- Görüşme olan günlerde gorusmeyi-analiz-et'ten sonra çalışır.
- Saha açıldıktan sonra her gün.
- Üçüncü bloktan saha açılana kadar kısa hali: yalnız sıcak çevreye giden mesajlar ve gelen cevaplar sayılır. Öncesinde sayılacak temas yok.

## 3. Ne okur

Kayıt yerinden: CRM açıldıysa CRM'den, açılmadıysa İş Beyni'nin "Bugünün listesi" bölümünden. O günün bütün kayıtları: temas sayısı ve kanalı, gelen cevaplar, olumlu cevaplar, yazılan randevular, gelen ve gelmeyen randevular, yapılan görüşmeler, kapanışlar. Akşamki beş sayıyı FounderOS bu kayıtlardan sayıyor. CRM'siz günlerde sayılar gün içinde öğrencinin söylediklerinden Bugünün listesi'ne yazılmıştır; bu "elle yazıldı" sayılmaz, normal yoldur.
İş Beyni'nden: gelir planındaki hedefler, dünkü ve bu haftanın sayıları, gün sayacı.
gorusmeyi-analiz-et'ten: o günkü görüşmelerin sonucu.

## 4. Ne sorar

Sormaz. Sayıları kayıt yerinden kendisi alır.

Tek istisna: kayıt yerinde o gün hiç kayıt yoksa tek soru sorar. "Bugün hiç kayıt görünmüyor. Gerçekten sıfır mı, yoksa yazmayı mı unuttun?" Sebebi şu: sıfır gün ile yazılmamış gün aynı şey değil ve ikisine verilen cevap farklı.

## 5. Ne yapar

### Her akşam yazılan sayılar

Beş sayı, her akşam, istisnasız. Sayıları FounderOS çıkarıyor: her kanalın tarih satırına bugün yazılmış kayıtları sayıyor. Beşinci günden itibaren her sayının yanında sıcak ve soğuk ayrımı duruyor (kayıttaki sıcak mı soğuk mu satırından); ikisi tek toplamda birleşmiyor.
1. Kaç temas, kanal ayrımıyla.
2. Kaç cevap geldi.
3. Kaç cevap olumluydu.
4. Kaç randevu yazıldı.
5. Kaç görüşme yapıldı ve kaçı kapandı.

Bunlar günlük yazılır ama günlük yorumlanmaz. Bir günün sayısı hiçbir şey söylemez; bir haftanın sayısı bir şey söyler.

### Bakılmayan sayılar

Şunlar iyi görünüyor ama karar için kullanılmıyor:

**E-postanın açılma oranı.** Açılma ölçümü artık güvenilir değil, çünkü bazı posta programları e-postayı kullanıcı açmadan kendisi açıyor. Yüksek açılma oranı gördüğünde hiçbir şey öğrenmiş olmuyorsun. Cevaba bak, açılmaya değil.

**Instagram takipçi ve beğeni sayısı.** Sana müşteri getirmiyor.

**Randevuya gelme oranı, otuz randevudan önce.** Beş randevunun üçü gelmediyse bu yüzde kırk değildir, sadece küçük bir sayıdır. Otuz randevu birikmeden bu orana bakılmaz.

**Kapanış oranı, otuz görüşmeden önce.** Aynı sebep.

**Toplam temas sayısı tek başına.** Çok temas yapıp hiç cevap almamak, az temas yapıp cevap almaktan kötüdür.

Bunlara bakmama sebebi tembellik değil. Az sayıda oran yanıltıyor ve yanıltan orana bakan kişi yanlış şeyi düzeltiyor.

### Akşamın tek cümlesi

Beş sayı yazıldıktan sonra tek cümle çıkar ve iki parçası olur: bugün ne oldu, yarın ne değişiyor.

Örnek: "Bugün 100 temas, 12 cevap, 2 randevu. Bu hafta toplam 500 temas. Yarın aynı sayı, değişiklik yok."
Başka örnek: "Bugün 40 temas, hedef 100. Yarın sabah bloğu tek madde olacak, başka iş yok."

Cümle iki parçadan uzunsa bu modül karar vermeye başlamış demektir; o başka modülün işi.

### Kötü görüşme varsa

Görüşme yapılan günün akşamında, sayılardan sonra tek iş daha var: o günün en kötü görüşmesine bakılır.

Öğrenme orada. İyi giden görüşmeden öğrenilecek şey az; kopan görüşmeden çok. Bakılan tek şey de şu: nerede koptu.

Kötü görüşmeden sonra kapanış şöyle yapılır: üç nefes, üç kelime, ve gün biter. Ertesi sabah o kaydın ilk beş dakikası değil, ilk kapanışının ilk beş dakikası dinlenir. Bu, kendini iyi hissetmen için yapılır, öğrenmek için değil.

### Gün sayacı

Her akşam sayacın günceller: kaçıncı gündesin, toplam kaç temas yaptın, kaç görüşme yaptın, kaç müşteri kazandın.

Bu sayaç motivasyon cümlesinin yerine geçiyor. "Devam et, yapabilirsin" cümlesi hiçbir şey söylemiyor. "On dört gün önce sıfır temasın vardı, bugün 1.400" bir şey söylüyor.

### Haftanın toplamı

Haftanın son gününün akşamında beş sayının haftalık toplamı da yazılır. Bu toplam ertesi gün degisiklige-karar-ver'in girdisi olur.

Haftanın tek sayısı, o akşamın ilk cümlesi: bu hafta kaç görüşme yapıldı; randevu değil, gerçekleşen görüşme. Her şeyden önce o söylenir, çünkü işin nereye gittiğini tek başına söyleyen sayı budur; temas sayısı emeği, görüşme sayısı işi gösterir. Kalıp: "Bu hafta [sayı] görüşme yapıldı; geçen hafta [sayı]. Toplam [temas] temas, [cevap] cevap." Sıfırsa sıfır denir, süslenmez; degisiklige-karar-ver ertesi gün buradan başlar.

## 6. Ne söyler

Normal akşam: "Bugün yüz temas, on iki cevap, iki randevu. Haftalık toplam beş yüz. Yarın aynı sayı."
Sıfır kayıt varsa: "Bugün hiç kayıt yok. Gerçekten sıfır mı, yoksa yazmayı mı unuttun? İkisine verdiğim cevap farklı."
Açılma oranına bakarsa: "Açılma oranına bakma. O sayı artık güvenilir değil, bazı posta programları e-postayı sen açmadan kendisi açıyor. Cevaba bak."
Az sayıda orana bakarsa: "Beş randevunun üçü gelmedi. Bu yüzde kırk değil, sadece beş randevu. Otuza gelmeden bu orana bakmıyoruz."
Kötü görüşme sonrası: "Bugünün en kötü görüşmesine bakacağız, sadece şuna: nerede koptu. Sonra kapatıyoruz. Üç nefes, üç kelime, gün bitti."
Sayılar düşükken: "Sayı düşük, bu bir gün. Bir günün sayısı hiçbir şey söylemez. Yarın normal sayıya dönüyoruz, haftanın sonunda bakacağız."
Sayaç okurken: "Gün yirmi altı. Toplam bin iki yüz temas, on iki görüşme. On dört gün önce sıfırdı."

## 7. Ne yazar

İş Beyni'ne: o günün beş sayısı (onuncu bölüm), gün sayacı, haftalık toplam, akşamın tek cümlesi, kötü görüşme notu. CRM açılmadıysa Bugünün listesi'nin "Dün ne oldu" satırı da bu akşam yazılır; sabah planı oradan okur. Bir de koşan toplam: bugüne kadar kaç temas, kaç görüşme, kaç randevu. Bu toplam her akşam üstüne ekleniyor ve bütün kilitler (üç yüz temas, on görüşme, otuz görüşme, otuz randevu) ondan okunuyor. CRM böyle bir toplamı tutmuyor, o yüzden akşam sayımı atlanan gün kilitler de kayıyor.
CRM'e: eksik kalan kayıtlar tamamlanır. Bu modül eksik kaydı görür ve sana söyler, ama senin onayın olmadan yazmaz.
CRM açılmadıysa: öğrencinin yapıştırdığı saha sonuçları aday aracıyla işlenir (aday-listesi-dosyasi, sonuclar), günün sayıları aracın ozet komutundan okunur; sabah `adaylar.html` bugünkü haliyle açılır.

**Günde iki gelen kutusu anı var ve planın içinde duruyor.** Öğlen, aramaların arasında beş dakika: e-posta ve Instagram açılır, gelen cevaplar olduğu gibi yapıştırılır, FounderOS yanıtları yazar ve öğrenci öğleden sonra gönderir. Akşam, sonuçlar yapıştırılırken aynı şey tekrarlanır. Sebebi şu: cevap veren aday en değerli aday ve yirmi dört saat sonra cevap veren kişi soğuyor. "Cevap gelince söyle" demek yetmiyor, saha günü buna yer bırakmıyor; o yüzden saat sabit.

Haftada bir de toplu araştırma var, pazartesi sabahı on dakika: nişin iş ilanı araması. Tek arama, sonucu bütün listeye dağılıyor. Bu, gözlemi olmayan adayların gözlem kazandığı yer. Reklam bakışı buraya girmiyor, onu veri servisi çekimle birlikte kendisi yapıyor.

**Liste stoğu her sabah ozet'in son satırında görünür ve takvimle değil stokla tetiklenir.** Araç dokunulmamış aday sayısını günlük temposuna bölüyor ve kaç gün kaldığını yazıyor. Beş günün altına inince "yeni ilçe çekilmeli" uyarısı çıkıyor ve o gün FounderOS yeni bir ilçe için çekim başlatıyor; öğrenciye sorulmuyor, söyleniyor. Aylık kayıt tavanı 2.500, beş yüzlük bir tazeleme rahat sığıyor. Takvime bağlı bir yenileme yok: listenin ne zaman biteceği tempoya bağlı, aya değil.
Veri servisine: günün sayıları, yalnız sayı olarak (gün sayacı, aşama, temas, cevap, randevu, görüşme, toplam müşteri); isim, işletme adı, not gitmez. Bu, FounderOS ekibinin kimin nerede takıldığını görüp erken yardım etmesi için. O gün saha çıkışı olduysa aynı çağrıya nişin adı, kartın açılış sürümü ve günün sonuç dökümü (açmadı, gönderdim, istemedi, ilgilendi, sonra) eklenir; ikisi de aday aracının `sonuclar` komutunun bastığı "gün dökümü" satırından okunur, uydurulmaz, `sonuclar` çalışmadıysa gönderilmez. Bu, hangi kartın hangi açılış metniyle ne getirdiğini merkezde toplamak için; öğrenciye söylenmez. Servis cevap vermezse sessizce geçilir, gün durmaz.

## 8. Yedek yol

- CRM açıkken o gün CRM'e yazılmamışsa: sayılar senden alınır ve "elle yazıldı" notu düşülür. Üç gün üst üste elle yazılıyorsa kayıt alışkanlığı bozulmuş demektir, haftanın kararına gider. CRM açılmadıysa bu satır işlemez.
- Bir sayı ölçülemiyorsa: "ölçülemedi" yazılır, uydurulmaz. Ölçülemeyen sayı hakkında karar verilmez.
- Görüşme kaydı yoksa: gorusmeyi-analiz-et'in yedek yolu işler, bu modül sadece sayıları alır.
- Akşam okuma atlanırsa: ertesi sabah plandan önce yapılır, atlanmaz. İki gün üst üste atlanırsa haftanın kararına gider.
- Sayılar hedefin çok üstündeyse: bu da bir işarettir ve sorgulanır. Genellikle kayıt yanlış girilmiştir.

## 9. Sıradaki adım ve işaretler

Sıradaki: ertesi sabah gunu-planla. Haftanın son akşamında degisiklige-karar-ver.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- İki gün üst üste sıfır kayıt: vazgeçme işareti, sabah planı değişir.
- Üç gün üst üste sayılar elle yazıldı (yalnız CRM açıkken): kayıt alışkanlığı bozuk, haftanın kararına gider.
- İki yüz temasta cevap oranı yüzde ikinin altında: teşhis işareti degisiklige-karar-ver'e gider, karar üç yüzde verilir.
- Otuz randevu doldu: gelme oranı ilk kez okunur.
- Otuz görüşme doldu: kapanış oranı ilk kez okunur, fiyat kilidi açılır.
- Bir sayı normalin çok altına düştü: haftayı beklemez, aynı akşam degisiklige-karar-ver açılır.
- Akşam okuma iki gün üst üste atlandı: haftanın kararına gider.
- Üç gün üst üste temas var ama sıfır cevap: ertesi sabah cevap-gelmiyor gunu-planla'dan önce açılır; liste, mesaj ve kanal sırayla kontrol edilir, niş değişmez.

Beş kural: boş sayfa yok (beş sayı ve tek cümlelik kalıp hazır gelir) · sessiz bitiş yok (her gün tek cümleyle kapanır) · onay (CRM'e eksik kayıt senin onayınla yazılır) · sahadan güncelleme (kendi oranların birikince karşılaştırma rakamlarının yerine geçer) · sormaz söyler (hangi sayıya bakılacağını ve hangisine bakılmayacağını FounderOS söyler).
