---
user-invocable: false
name: veri-servisi
description: "FounderOS veri servisinin sekiz aracının kuralları: aday çekimi ve niş sayımı, kullanım, akşam ölçümü, durum kaydının yedeği, telefondaki saha ekranı (saha_yukle, saha_sonuclari). Aday listesi çekilirken, sayım başlatılırken, sabah saha ekranı yüklenirken, akşam sonuçlar ve ölçüm yazılırken, klasöre erişilemeyen oturumda durum okunurken açılır."
---

# Veri servisi (FounderOS'un kendi sunucusu)

Aday listesini öğrenci değil, FounderOS'un veri servisi çeker; sunucu ayrıca durum kaydının yedeğini ve telefondaki saha ekranını tutar. Servis eklentiye "veri" adlı bağlantı olarak takılıdır. Her çağrıda İş Beyni'nin birinci bölümündeki lisans anahtarını `anahtar` alanında gönderirsin; öğrenciye anahtarı, iş kimliğini, jetonu ya da ham cevabı göstermezsin, sonucu kendi cümlenle söylersin.

## Araçlar

- `aday_ara`: kategori ve şehir için çekim başlatır ya da hazır listeyi verir. `sayim: true` ile niş doğrulaması için sayım çekimi.
- `aday_sonuc`: çalışan çekimi sorar, hazır olunca özeti ve satırları sayfa sayfa verir.
- `kullanim`: bu ayki kayıt sayısı ve tavan.
- `olcum_yaz`: günün sayıları (akşam; `tarih` ile bugün ya da son yedi günden biri).
- `durum_yaz`: durum kaydının (`.founderos/durum.json`) kopyası.
- `durum_oku`: sunucudaki durum kaydı, son ölçüm ve son lisans kontrolü.
- `saha_yukle`: günün saha listesini yükler, telefonda açılacak saha ekranının bağlantısını döner.
- `saha_sonuclari`: saha ekranında basılan sonuç düğmelerini "FounderOS saha sonuçları" metni olarak döner (`tarih`: bugün ya da son yedi gün; bir günün sonuçları o gün basılanlardır).

## Çekim

`aday_ara`'yı çağırırken `reklam_kelimeleri` alanını da doldurursun. Bu alan boş giderse servis reklam kütüphanesini yalnız kategori adıyla arar ve o şehirdeki reklam verenlerin neredeyse hepsi kaçar; hiçbir diş kliniği "diş kliniği" diye reklam vermiyor, "implant fiyatları" diye veriyor. Kelimeleri niş kartının **reklam kütüphanesi kelimeleri** satırından okursun: açıklama cümlelerini ("şehir adıyla", "erişilemedi", "doğrulanmadı") atarsın, birbirini içerenlerden birini alırsın, kartta yazdığı sırayla ilk sekizini dizi olarak verirsin. Şehri sen eklemezsin, servis ekler.

Sıra: `aday_ara` "çalışıyor" derse iş kimliğini hemen İş Beyni'nin yedinci bölümüne yazarsın ve öğrenciye tek cümle söylersin ("Çekim başladı, birkaç dakika sürer"), sonra `aday_sonuc` ile sorarsın; her çağrı yirmi saniye bekler, en fazla on çağrı. On çağrıda bitmediyse başka işe geçersin ve daha sonra yalnız `aday_sonuc` ile sorarsın; aynı kategori ve şehir için `aday_ara`'yı yeniden çağırmazsın, o yeni çekim başlatır ve tavandan düşer. "Hazır" gelince önce özeti söylersin (kaç kayıt, kaçında telefon, kaçı neden işaretli) ve "bunları listeye almıyorum, tamam mı?" diye sorarsın; öğrenci görmek isterse `elenenler_dahil: true` ile işaretli satırları da alır ve gösterirsin, "bunu tut" dediği satır listeye girer. Öğrenci "tamam" deyince listeyi klasöre aday aracıyla indirirsin: `.founderos/adaylar-arac.py cek` çekimi servisten kendisi alır, tekrarları eler, `adaylar.csv`'yi yazar ve `adaylar.html` sayfasını üretir; satırlar sohbete girmez. Araç ilk kez `aday-listesi-araci` becerisinden kurulur; komutlar ve sütunlar `aday-listesi-dosyasi` becerisinde. `adaylar.csv` elle düzenlenmez. Araç "HATA" derse yazmamıştır; sebebini okur, düzeltir, yeniden çalıştırırsın. Araç hiç çalışmıyorsa (python yok) yedek yol aynı beceride, pahalıdır ve günlüğe yazılır.

Öğrenci listeyi Excel'de değil klasördeki `adaylar.html` sayfasında görür (Liste ve Saha modu sekmeleri). Sayfayı sohbete kart olarak açarsın; "Masaüstü, sonra şu klasör, çift tıkla" tarifi ancak kart açılmazsa verilir. Beş yüz satırı sohbete dökmezsin, Excel'e yönlendirmezsin.

Niş doğrulaması için sayım çekimi ayrıdır: `aday_ara` `sayim: true` ile, üç niş için, beş yüz kayıta kadar, e-posta ve Instagram çıkarmadan; aylık kayıt tavanından düşmez, çekim sayısına girer. Sayım çekimine de her nişin kartındaki reklam kütüphanesi kelimelerini `reklam_kelimeleri` olarak verirsin (yukarıdaki kural); servis reklam kütüphanesini de tarar ve özetteki `reklamli` sayısı `kalan`a bölününce niş doğrulama tablosunun reklam veren oranı çıkar. Özette reklam sayısı yoksa oran "görülemedi" yazılır. Sayımı birinci günde, pazar onaylanır onaylanmaz başlatırsın; özeti teklife geçmeden, en geç markadan önce `aday_sonuc` ile alır ve yardımcıya verirsin. Servis o gün cevap vermezse sayım ikinci bloğun sabahında başlar; yardımcının servise erişimi yoktur, o yalnız tabloyu kurar ve rakip taramasını yapar.

Servis "tavan", "kapalı" ya da iki denemede "hata" derse gün durmaz: yedek yol tarayıcı eklentisidir (araclari-kur'un üçüncü adımı). Öğrenciye "servis çöktü" demezsin; "bugün elle tarıyoruz, servis açılınca kalanını oradan alacağız" dersin.

## Saha ekranı

Sabah günün listesi kurulunca (`bugun --planla`) aday aracının `saha-paketi --yukle` komutunu çalıştırırsın: araç günün listesini ve arama senaryosunu paketler, servise kendisi yükler ve "saha ekranı: <adres>" satırını basar. Araç servise ulaşamazsa paket `.founderos/saha-paketi.json` dosyasında durur; o dosyanın içeriğini olduğu gibi `saha_yukle` aracına `paket` olarak verirsin. Dönen adres telefonda açılacak saha ekranıdır; öğrenciye bağlantıyı verir ve tek cümle söylersin: "Bugünün listesi telefonunda: bu bağlantıyı aç, aramayı oradan yap, her aramadan sonra sonucuna bas." Aynı gün liste değişirse yeniden yüklersin; bağlantı ve o günün sonuçları korunur.

Saha ekranının üstünde günün temas sayısı hedefe karşı durur (bugün kaç, hedef kaç, seri). Hedefi durum kaydındaki `gunluk_hedef` belirler; yoksa düzen (tam 100, yan 40). Her telefon kartında dört kısayol var: "Sahibi açtı", "Çalışan açtı", "Sahibi yoktu", "Numara yanlış". Öğrenci dokununca nota eklenir, akşam metnine not olarak gelir. Akşam okurken: "Çalışan açtı" ya da "Sahibi yoktu" olan adayın sıradaki aramasında kartın çalışan açılışıyla sahibini sorarsın; "Numara yanlış" olan adayın numarası aday aracının `guncelle` komutuyla düzeltilir; doğrusu bulunamazsa `sil <anahtar> --sebep "numara yanlış"` ile işaretlenir (satır silinmez) ve aday bir daha aranmaz. Randevu basılınca ekran adaya gidecek onay mesajını hazır verir (cep numarasına WhatsApp'la tek dokunuş); öğrenci yine sana "randevu aldım" der, hatırlatmaları sen hazırlarsın. Onay mesajı ön görüşme sayfasının ya da videonun linkini taşır: link İş Beyni'nde yazılıysa aday aracına bir kez verirsin (`adaylar-arac.py sayfa --onay-linki <adres>`), her sabahın paketi onu taşır.

Akşam kapanışı iki adımdır. Önce kapanmamış günler (aşağıda). Sonra iş günü kapanır: `saha_sonuclari` aracını iş gününün tarihiyle (`tarih`) çağırırsın. Dönen `metin` boş değilse onu `.founderos/sonuc.txt` dosyasına yazar, `.founderos/adaylar-arac.py sonuclar .founderos/sonuc.txt --gun <iş günü>` komutunu çalıştırır, sonucu tek cümleyle söylersin. Metin boşsa ve öğrenci masaüstü sayfasını kullandıysa "Sonuçları kopyala" yolu işler: öğrenci yapıştırır, sen aynı dosyaya yazar ve aynı komutu çalıştırırsın. Aynı satırı iki kez işlemek sorun değil; araç o gün için işlenmiş satırı atlar. `olcum_yaz` da iş gününün tarihiyle gider. Kapanış bitince durum kaydına `son_kapanis` olarak iş günü yazılır. İş günü `kapat` çıktısının ilk satırıdır: gece yarısından sonra, sabah beşe kadar yapılan kapanış önceki günündür; 00.30'da "akşam" diyen öğrenci dünü kapatır.

**Kapanmamış günler.** Saha açıksa sabah ilk mesajdan önce ve akşam kapanışından önce `.founderos/adaylar-arac.py kapat` çalışır. Araç durum kaydındaki `son_kapanis`'i kendisi okur ve o günden dünü de içine alarak (en çok yedi gün geriye) kapanışı yapılmayan her günün saha sonuçlarını servisten alır, o günün tarihiyle işler ve günün ölçümünü yazar. Takipler, sonra aranacaklar ve randevular böylece listeye girer, istemeyen bir daha aranmaz; akşam kapanışından sonra basılan sonuç da ertesi sabah işlenir. Kapanışı atlanan hiçbir günün müşterisi kaybolmaz. Tek komuttur; bu günler için `saha_sonuclari` ve `olcum_yaz` ayrıca çağrılmaz. Son satırdaki `son_kapanis` durum kaydına yazılır ve `durum_yaz` gider (sabah ilk mesajdan sonra da olabilir). "Sayaçlara eklenecek" satırı varsa o sayılar durum kaydındaki `sayaclar`'a ve İş Beyni'nin koşan toplamına eklenir, `son_temas_tarihi` güncellenir, her günün sayıları o günün günlüğüne tek satır gider (`founderos:aday-listesi-dosyasi`, kapat). Araç `kapat`ı tanımazsa eski sürümdür: önce `founderos:aday-listesi-araci` ile güncellenir. Servise ulaşamazsa ("HATA: ... alınamadı") sessizce geçersin, kalan günler bir sonraki kapanışta alınır. Öğrenciye ayrı cümle yok, "kapanış yapmamışsın" denmez; sabahın ilk cümlesi kapanan günleri bu sayılarla okur.

## Durum kaydı ve ölçüm

`durum_yaz`: durum kaydını her güncellediğinde (modül bitince, oturum kapanırken) aynı içeriği `durum` alanında gönderirsin. Sunucudaki kopya panelin, hatırlatmaların ve ekibin kaynağıdır; öğrenci yokken onu fark eden budur. Cevap gelmezse sessizce geçersin.

`durum_oku`: sunucudaki durum kaydı, son ölçüm, gece çekimi (`gece_cekimi`, aşağıda) ve hatırlatmaların öğrencinin telefonunda açık olup olmadığı (`hatirlatma`). Klasöre erişemediğin bir oturumda durumu da buradan okursun.

Akşam kapanışında `olcum_yaz` ile günün sayılarını gönderirsin: gün sayacı, aşama, temas, cevap, randevu, görüşme, toplam müşteri. Sadece sayı; isim, işletme adı, not gitmez. O gün saha çıkışı olduysa aynı çağrıya kartın etiketini ve günün sonuç dökümünü de koyarsın: `nis`, `acilis_surumu`, `acmadi`, `gonderdim`, `istemedi`, `ilgilendi`, `sonra`. Yedisini de uydurmazsın; aday aracının `sonuclar` komutu iş bitince tek satır basar ("gün dökümü: niş …, açılış sürümü …, temas …, acmadi …"), onu olduğu gibi taşırsın. O gün `sonuclar` çalışmadıysa bu alanları göndermezsin. Bunlar Berk'in kart ekranında toplanıyor; öğrenciye bundan söz etmezsin, puanı ya da oranı ona söylemezsin.

## Gece hazırlığı

Akşam kapanışında aday aracının `ozet` çıktısındaki stok satırı "liste bitiyor, yeni ilçe çekilmeli" derse yeni ilçenin çekimini oturumda başlatmazsın; sıradaki ilçeyi seçer ve durum kaydına yazarsın:

```json
"siradaki_cekim": {"kategori": "...", "sehir": "...", "ilce": "...", "hedef": 800, "reklam_kelimeleri": ["..."], "istek_tarihi": "YYYY-AA-GG"}
```

Kategori ve kelimeler nişin kartından, ilçe kartın yoğun ilçelerinden ve daha önce çekilmemiş olanlardan; istek tarihi bugün. Durum kaydı `durum_yaz` ile gider; sunucu çekimi gece başlatır, öğrenci uyurken liste çekilir. Öğrenciye tek cümle: "Listen beş günlük işin altına indi; yeni ilçenin listesi bu gece çekiliyor, sabah hazır."

Sabah günaydında `durum_oku` yaparsın. `gece_cekimi` geldiyse (iş kimliği, kategori, şehir, ilçe) o iş kimliğiyle listeyi alırsın: `.founderos/adaylar-arac.py cek --is <is_id>` (hâlâ çalışıyorsa `aday_sonuc` ile yirmi saniye aralıkla sorarsın); `aday_ara`'yı yeniden çağırmazsın, o ikinci çekim açar ve tavandan düşer. Liste içeri alınınca `siradaki_cekim` durum kaydından silinir ve `durum_yaz` gider. Öğrenciye tek cümle: "Gece yeni ilçenin listesi çekildi: [kaç] işletme listene eklendi." `gece_cekimi` gelmediyse ve `siradaki_cekim` duruyorsa eski yol: çekimi oturumda başlatırsın, gün durmaz. Aylık tavan dolduysa gece de çekim olmaz; tavan kuralı aynen geçerli. `aday_sonuc` gece çekimi için hata dönerse (çekim sağlayıcıda başarısız) o çekim bir daha sunulmaz; çekimi oturumda `aday_ara` ile başlatırsın. Liste hangi yoldan gelirse gelsin (gece ya da oturum) içeri alınınca `siradaki_cekim` silinir; silinmezse ertesi gece aynı yer yeniden istenir.
