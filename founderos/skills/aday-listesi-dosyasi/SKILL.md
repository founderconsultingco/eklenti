---
user-invocable: false
name: aday-listesi-dosyasi
description: "Aday listesinin kurallari: adaylar.csv'nin otuz sekiz sutunu, adaylar.html sayfasi (Liste ve Saha modu) ve aday aracinin komutlari (cek, ekle, guncelle, temas, sonuclar, sil, bugun, ozet, bul, sayfa). Cekim bitince, denetim yazilirken, sabah gunun listesi kurulurken, saha sonuclari yapistirilinca ve ogrenci listesini sorunca acilir."
---

# Aday listesi: dosya, sayfa ve araç

Öğrencinin aday havuzu klasöründeki `adaylar.csv` dosyasıdır; öğrenci onu `adaylar.html` sayfasından görür; ikisini de `.founderos/adaylar-arac.py` aracı yönetir. FounderOS csv'yi elle düzenlemez: satır eklemek, hücre değiştirmek, günün listesini çıkarmak, sayfayı yenilemek, hepsi aracın komutlarıyla olur. Araç yanlış sütun adını, yanlış aşama adını, yanlış tarihi kabul etmez; her yazıştan önce yedek alır, her yazıştan sonra sayfayı kendisi yeniler. Bu dosya sütunları, komutları ve ne zaman hangisinin çalıştırılacağını verir.

## Klasördeki dosyalar

- `adaylar.csv`: kayıtların kendisi, tek kaynak. UTF-8, virgülle ayrılmış, başlık bir kere.
- `adaylar.html`: öğrencinin çift tıklayıp tarayıcıda açtığı sayfa. Araç her yazıştan sonra yeniden üretir; veri sayfanın içinde gömülüdür, yanına başka dosya gerekmez. İki sekmesi var: Liste (bütün havuz, arama, süzgeç, sıralama, satıra tıklayınca ayrıntı) ve Saha modu (bugün sırada olanlar kart kart). Saha kartının üç parçası var: "Önce oku" (kim, ilçe, bağlayan, doğrulanmış gözlem, kanca, geçmiş, not; lira karşılığı burada görünmez), "Söyle" (adaya göre doldurulmuş arama metni; dört hal: sahibi açtı, çalışan açtı, açılmadı, ikinci arama; ikinci arama geçmişi olan adayda kendiliğinden seçilir) ve altta kanal, sonuç düğmeleri, kısa not. "Karşı taraf bunu söylerse" düğmesi sağdan bir çekmece açar: önce nişe özel itirazlar, sonra her nişte geçerli olanlar, her biri söyle / ne için / sonra; en altta ton kuralları. Sonunda "Sonuçları kopyala".
- `.founderos/`: gizli çalışma klasörü, öğrenci görmez. İçinde `adaylar-arac.py` (araç), `adaylar-sablon.html` (sayfa şablonu), `sayfa.json` (senaryo: niş adı, öğrencinin adı ve şehri, kartın telefonda söylenecekleri), `telefon.md` (niş kartının "Telefonda söylenecekler" bölümünün kopyası), `gelen.csv` (servisten son inen ham sayfa), `sonuc.txt` (öğrencinin yapıştırdığı son saha sonuçları), `yedek/` (son otuz yazım yedeği ve otuz günlük `gun-YYYYAAGG.csv` kopyası). Klasör kuralının üçüncü istisnasıdır; başka bir şey buraya yazılmaz.

Öğrenci csv'yi Excel'de açmaz, açmak isterse sayfaya yönlendirilir. Yer tarifi çıplak yol değil, adım adım: "Masaüstü, sonra FounderOS klasörü, `adaylar.html` dosyası; üstüne çift tıkla, tarayıcıda açılır."

## Kurulum (bir kere, listenin çıktığı gün)

1. `aday-listesi-araci` becerisini aç. Beceri açıldığında klasör yolu görünür; `adaylar-arac.py` ve `adaylar-sablon.html` orada durur. İkisini öğrencinin klasöründeki `.founderos/` altına kopyala (kopyalama komutuyla; olmazsa beceride gömülü duran iki metni aynı adlarla birebir yaz).
2. Öğrencinin klasörünün içinde `python3 .founderos/adaylar-arac.py surum` çalıştır; sürüm numarası gelmeli. Gelmiyorsa dosya eksik ya da kesik kopyalanmıştır, yeniden kopyala. `python3` yoksa `python` dene.
3. Senaryoyu sayfaya yaz. Niş kartının "**Telefonda söylenecekler.**" bölümünü, ilk satırından son itiraz maddesine kadar olduğu gibi `.founderos/telefon.md` dosyasına kopyala (ilk satıra `# <nişin adı>` koy), sonra: `python3 .founderos/adaylar-arac.py sayfa --kart .founderos/telefon.md --ogrenci-ad "<öğrencinin adı>" --sehir "<şehri>"`. Sistemin adı varsa `--sistem-adi "<ad>"` eklenir. Araç bölümü okur; açılış sorusu, işleyiş sorusu, ne yaptığın, çalışan açarsa satırları ve nişe özel itirazlar Saha modu kartına girer, genel arama sırası ve genel itirazlar şablonda hazırdır. Öğrencinin adı ve şehri İş Beyni'nin birinci bölümünden alınır; verilmezse sayfa "[adın]" ve "[şehir]" gösterir ve uyarır. Kartta bu bölüm yoksa sayfa genel metinle çalışır, uydurmaz. Niş değişirse ya da kart güncellenirse aynı komut yeniden çalışır.
4. Öğrenciye tek cümle: "Listen klasörde `adaylar.html` dosyasında, çift tıkla açılır."

Beceri her sürümde araçla birlikte güncellenir. `surum` çıktısı becerideki sürümden küçükse iki dosyayı yeniden kopyala; csv'ye dokunma, araç eski dosyayı okur ve eksik sütunu kendisi ekler.

## Sütunlar (sıra ve ad sabittir, kırk altı sütun)

İlk on altı sütun veri servisinin başlığıdır: `kisa_ad` (aramada ve mesajda kullanılan kısa ad), `ad` (Haritalar'daki tam ad), `telefon` (+90 ile tek biçim), `eposta`, `instagram`, `site`, `adres`, `semt`, `yorum_sayisi`, `puan`, `kategori` (Haritalar'ın verdiği; kartla karşılaştırma bundan), `ipuclari` (boşlukla ayrılmış kodlar: profil_sahipsiz, site_yok, instagram_yok, yorum_az, aksam_kapali, hafta_sonu_kapali, pazar_kapali, saat_yok, yorum_sikayet, sikayet_ulasilamiyor, sikayet_gelmedi, kapanmis_olabilir, reklam_veriyor, sadece_reklam), `yorum_alinti` (şikayet cümlesinin kendisi), `reklam` ("2 aktif reklam, biri 05.01.2026 tarihinden beri"; boşsa aktif reklam görülmedi), `elenme` (dolu satır listede yoktur: servisin sebebi ya da "aday istemedi" gibi sonradan yazılan sebep; satır silinmez), `harita`.

Kalan otuzu FounderOS'un aracıyla doldurduğu sütunlar:
- `eklenme_tarihi`: kaydın listeye girdiği gün, araç yazar, sonra değişmez.
- `kaynak`: haritalar, reklam, iş ilanı, elle, tanıdık, referans. `reklam` olan satır Google Haritalar'da bulunamamış, yalnız reklam kütüphanesinden bilinen işletmedir; telefonu genelde boştur. `baglayan`: tanıdık ya da referansta kimin bağladığı.
- `yuz`: en çok istenen yüz işletmedeyse evet.
- Denetim: `sahibi` (karar veren), `uygunluk` (0-15; sayfa A 10 ve üstü, B 6-9, C 5 ve altı), `sizinti` (0-5), `bulgu` (en güçlü bulgu, tek cümle), `kanca` (o adaya telefonda olduğu gibi söylenecek tek cümle, gün adıyla: "Salı akşamı yediye doğru sizi bir kere aradım, açılmadı."; Saha kartı bunu üçüncü adım olarak gösterir, yoksa kartın açılış sorusunu koyar), `lira` (lira karşılığı, tek satır hesap; görüşme özet ekranı için, Saha modunda görünmez), `denetim_tarihi`.
- Temas: `asama` (yeni, temasta, cevap verdi, randevu, görüşüldü, sonra, kapandı, müşteri; tek değer), `telefon_durumu`, `eposta_durumu`, `instagram_durumu`, `video_durumu` (her biri yapılmadı, yapıldı, cevap geldi, kapandı), `temas_sayisi`, `son_temas_tarihi`, `son_temas_kanali` (telefon, e-posta, instagram, video), `siradaki_hareket` (tek satır, adayın tek sonraki adımı), `siradaki_tarih` (o adımın günü; bugünse sayfada yeşil, geçmişse turuncu; günün listesi buradan çıkar), `randevu_tarihi` (YYYY-AA-GG SS:DD), `not` (kısa; araç her notun başına günü koyar).
- Yazılı metinler: `eposta_konu`, `eposta_metni`, `dm_metni` (o adaya gidecek metinler, adaya-mesaj-yaz yazar).
- Cevap ve zincir: `son_cevap` (adayın kendi cümlesi, olduğu gibi), `cevap_dali` (fiyat, bilgi, meşgul gibi), `zincir_adimi` (yazılı takip zincirinin kaçıncı adımı; açılmayan telefon bu sayacı ilerletmez), `acmadi_sayisi` (telefon üst üste kaç kez açılmadı; üçüncüde kanal kapanır ve aday yazılıya geçer).

Tarihler `YYYY-AA-GG`. Boş bilgi boş kalır, "yok" yazılmaz. Kim doldurur: 1-16 ve eklenme tarihi araç (cek, ekle); kaynak, bağlayan, yüz aday-listesi-cikar ve tanidik-listesi-cikar; denetim sütunları aday-denetimi-cikar; temas sütunları saha sonuçlarıyla (sonuclar) ve adaya-mesaj-yaz, gorusmeye-getir, gorusmeyi-analiz-et, gunu-planla, rakamlari-oku.

## Komutlar

Hepsi öğrencinin klasörünün içinden: `cd "<klasör>" && python3 .founderos/adaylar-arac.py <komut>`. Komut ve ham çıktı sohbete girmez; sonucu tek iki cümleyle söylersin. Araç "HATA:" ile başlayan bir satır basarsa yazmamıştır, sebebi okur ve düzeltip yeniden çalıştırırsın.

**cek --is <iş kimliği> [--ozet] [--kategori-disi "<kategori>"]... [--tut "<ad>"]...** Veri servisinden biten çekimi kendisi indirir ve listeye ekler. Lisans anahtarını `is-beyni.md`'den bulur, ayrıca verilmez. Sıra: önce `--ozet` ile yalnız özeti al (kaç kayıt, kaçı telefonlu, servis kaçını neden işaretledi), öğrenciye "bunları listeye almıyorum, tamam mı?" de; sonra `--ozet` olmadan çalıştır. Kartın dışındaki Haritalar kategorileri `--kategori-disi` ile dışarıda kalır ("oto klima" gibi), öğrencinin "bunu tut" dediği işaretli satır `--tut` ile girer. Aynı çekim ikinci kez çalıştırılırsa tekrarlar atlanır, çift kayıt olmaz. "çalışıyor" derse çekim bitmemiştir, yirmi saniye sonra yine sorarsın. "veri servisine ulaşılamadı" derse yedek yol: `aday_sonuc` aracıyla sayfaları alır, servisin başlığıyla `.founderos/gelen.csv` dosyasına yazar, `ekle` çalıştırırsın.

**ekle <dosya> [--kaynak K] [--baglayan AD] [--yuz] [--tut ...] [--kategori-disi ...]** Servis başlığıyla yazılmış bir csv'yi listeye ekler. Yedek yolda (tarayıcı eklentisi, elle liste), iş ilanı kaynağında (`--kaynak "iş ilanı"`), tanıdık A listesinde (`--kaynak tanıdık --baglayan "<kim>"`) kullanılır. Dosyada en az `kisa_ad` ve `telefon` sütunları olmalı; diğerleri boş kalabilir.

**guncelle "<işletme ya da telefon>" sutun=değer ... [--semt S]** Bir adayın hücrelerini değiştirir. Denetim bitince: `guncelle "Özkan Klima" sahibi="Özkan Bey" uygunluk=11 sizinti=4 bulgu="Akşam yedide aradım, açan olmadı" kanca="..." lira="4 arama x 1.800 TL" denetim_tarihi=bugün`. Yüz işletme seçilince: `yuz=evet`. Tarih için bugün, yarın, +3 ya da 2026-09-15 yazılır. `not=metin` notu tarihiyle sonuna ekler, `not==metin` notu baştan yazar. Aynı ad iki işletmede varsa araç durur ve seçenekleri basar; telefonla ya da `--semt` ile ayırırsın.

**temas "<işletme>" --kanal telefon|e-posta|instagram|video --sonuc "..." [--durum cevap geldi|kapandı] [--asama ...] [--siradaki "..."] [--tarih +3] [--randevu "2026-09-15 14:00"] [--not "..."]** Tek bir temas işler: kanal durumunu, temas sayısını, son temas tarihini yazar, sıradaki hareketi ve tarihi kurar. Sohbette tek tek bildirilen temaslar için.

**sonuclar .founderos/sonuc.txt** Öğrencinin sayfadaki "Sonuçları kopyala" düğmesiyle aldığı metni işler. Öğrenci o metni sohbete yapıştırınca metni olduğu gibi `.founderos/sonuc.txt` dosyasına yazar, komutu çalıştırır, çıktıyı tek cümleyle özetlersin ("Dokuz sonuç işlendi: iki randevu, üç ilgilendi, dördü açmadı; yarın altı takip var"). Metnin biçimi: her satır `işletme | kanal | sonuç | randevu: ... | tarih: ... | not: ...`. Sonuç kelimeleri ve aracın yaptığı: `açmadı` (telefon yapıldı, yarın tekrar), `gönderdim` (yazılı kanal yapıldı; ilk gönderimden 3, 7 ve 14 gün sonra takip; dördüncüden sonra "sonra"), `istemedi` (kanal ve aşama kapandı, bir daha aranmaz), `ilgilendi` (cevap geldi, aşama cevap verdi, üç gün sonra takip), `randevu` (aşama randevu, randevu tarihi yazılır, sıradaki hareket randevu hazırlığı), `sonra` (aşama sonra, verilen tarihte tekrar; tarih yoksa bir hafta). Modülün kuralı başka bir şey söylüyorsa üstüne `guncelle` ile düzeltirsin. Araç bulamadığı ya da anlamadığı satırları sonda listeler; onları elle işlersin.

**sil "<işletme>" --sebep "aday istemedi"** Satırı listeden çıkarır (elenme dolar, satır durur, sayfada görünmez). Onayla silinen servis satırları için de bu kullanılır.

**isaret DOSYA --isaret is_ilani** Toplu araştırmanın sonucu: dosyanın her satırı bir işletme adı, eşleşen adayların `ipuclari` sütununa o işaret yazılır. Tek kabul edilen işaret `is_ilani`. `reklam_veriyor` elle yazılmaz, veri servisinden gelir ve `reklam` sütunuyla birlikte gelir.

**ogren [--esik N]** Hangi gözlemin ve hangi kanalın cevap getirdiğini sayar. Eşiğin altındaki gözlem sayılmaz, çünkü az sayıda oran yanıltır. Haftanın kararında ve ayın uzun okumasında çalışır.

**yuz-sec [--sayi 100] [--yorum-ust-siniri 300]** En çok istenen yüzü listeden seçer ve `yuz` sütununa "evet" yazar. Sıra: ilan verenler, reklam verenler, sızıntı puanı, yorum sayısı, ulaşılabilir olanlar. Yorum sayısı üst sınırın üstündeki işletmeler listeden atılmaz, yüzün sonuna konur; büyük işletmede karar tek kişide olmuyor ve ilk aramalar onlarla yapılmıyor. Elle işaretlenmiş satırlara dokunmaz, eksiği tamamlar. Liste yetmezse kaç kişilik yerin boş kaldığını söyler.

**bugun [--planla --kanal telefon|yazı] [--sayi 100]** Günün listesini basar, dört grup sırasıyla: cevap verenler, takibi bugüne düşenler, denetimi hazır olanlar (yüz işletme önce, sızıntı puanı yüksek önce), denetimsizler. `--planla` ile sıradaki tarihi olmayan seçilenlere bugünü ve "ilk temas" hareketini yazar; sayfanın Saha modu o anda dolar. Sabah gunu-planla bunu çalıştırır: tam zamanlıda `--sayi 100`, işin yanında `--sayi 40`. Sekiz yüz satırı sohbete almazsın, bu çıktı yeter.

**ozet** Sayılar: toplam, telefonlu, denetlenmiş, yüz, bugün sırada, gecikmiş, aşama dağılımı, bugün temas edilen, toplam temas. Akşam kapanışında (rakamlari-oku) ve İş Beyni'ne sayı yazarken buradan okunur.

**bul "<metin>"** Ada, sahibine, semte ya da telefona göre satırları basar. Öğrenci bir adayı sorunca.

**sayfa [--kart telefon.md] [--nis AD] [--ogrenci-ad AD --sehir S --sistem-adi AD]** Sayfayı yeniden üretir; senaryo bilgisi verilirse önce `sayfa.json`'a kaydeder. `--kart` niş kartının "Telefonda söylenecekler" bölümünü okur (kurulum 3. adım). Elle yazılmış JSON vermek gerekirse `--dosya senaryo.json` (alanlar: ad, ogrenci{ad, sehir, sistem_adi}, acilis_sorusu, isleyis_sorusu, vaat, calisan, itirazlar[{durum, soyle, neden, sonra}]). Komut sonunda eksik senaryo bilgisi varsa söyler. Her yazış zaten sayfayı yeniler; bu komut "listemi göster", "listemi yenile" dendiğinde ve senaryo değiştiğinde çalışır.

**surum** Aracın sürümü.

## Ne zaman ne çalışır

- Çekim bitince: `cek --ozet`, onay, `cek`. Sonra kurulum adımları (ilk kezse) ve öğrenciye sayfa cümlesi.
- Yüz işletme seçilince: her biri için `guncelle ... yuz=evet`.
- Hızlı ve derin denetim bitince: her aday için tek `guncelle` (sahibi, uygunluk, sızıntı, bulgu, kanca, lira, denetim tarihi).
- Sabah, günün planı kurulurken: `bugun --planla`. Öğrenciye: "Bugünün listesi sayfada, Saha modu sekmesinde; her kartta ne söyleyeceğin yazıyor, her aramadan sonra düğmeye bas, akşam Sonuçları kopyala." Öğrencinin adı, şehri ya da niş kartı değiştiyse önce `sayfa --kart ...` yeniden.
- Gün içinde öğrenci bir temas anlatırsa: `temas`.
- Öğrenci saha sonuçlarını yapıştırınca: `sonuclar`.
- Akşam kapanışında: `ozet`; sayılar İş Beyni'ne ve `olcum_yaz`'a. Öğrenciye söylediğin her rakam bu çıktıdan okunur, hatırdan yazılmaz; çekimden gelen rakamla listede kalan rakam ayrı kümelerdir ve hep kümesiyle söylenir. `sonuclar` iş bitince "gün dökümü" satırını basar (niş, açılış sürümü, temas, sonuçların sayısı); o satır olduğu gibi `olcum_yaz`'a gider, öğrenciye gösterilmez.
- Öğrenci "listem nerede", "listemi göster", "kimi arayacağım" derse: `sayfa`, sonra sayfayı **sohbete kart olarak aç**; satırları sohbete dökme, klasör tarifi verme. Klasör tarifi ("Masaüstü, sonra FounderOS, adaylar.html") yalnız kart açılmadığında verilen yedek yoldur. Belli bir adayı sorarsa `bul`.
- Öğrenci "Excel'de açayım mı" derse: hayır, sayfa; sebebini tek cümleyle söyle (ipuçları Türkçe, bugün sırada olan yeşil, satırda arama kartı).

## Araç çalışmazsa

`python3` de `python` da yoksa ya da araç açılmıyorsa gün durmaz: csv'yi bu dosyadaki sütun sırasıyla kendin yazarsın, sayfayı şablondaki `/*FOUNDEROS-VERI*/` yerine `window.ADAYLAR=<csv metni JSON dizesi>;window.ADAYLAR_TARIH="GG.AA.YYYY SS:DD";window.ADAYLAR_NIS={};` koyarak üretirsin. Pahalı yoldur; yalnız araç çalışmadığında, ve İş Beyni'nin on üçüncü bölümüne (açık işler) "aday aracı çalışmadı, tarih" yazılır.

CRM açıldığı gün havuz CRM'e yüklenir (musteri-takip-sistemini-kur) ve csv "CRM'e taşındı, tarih" notuyla kapanır; o günden sonra kayıt yeri CRM'dir.
