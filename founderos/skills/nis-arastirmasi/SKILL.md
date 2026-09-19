---
user-invocable: false
name: nis-arastirmasi
description: "Kaynaklı niş araştırması. Yapay zekâ resepsiyonisti (açılmayan telefon) için Türkiye'de en uygun işletme gruplarını internetteki güncel, bağlantılı kaynaklarla karşılaştırır; ilk üçü ve tek başlangıç nişini gerekçesiyle önerir, raporu klasöre nis-arastirmasi.md olarak yazar. 'Pazar araştırması yap', 'hangi nişe gireyim, kaynaklı araştır', 'resepsiyonisti hangi sektöre satarım', 'niş raporu' dendiğinde. Nişi seçmez ve kilidi açmaz; kararı nisi-sec verir."
---

# nis-arastirmasi

## 1. Adı, rolü, pazarlamadaki karşılığı

Kaynaklı niş araştırması. Modül, FounderOS'un belli bir işi yapan parçasıdır. Bu modül internetteki güncel ve kaynağı belli bilgilerle tek bir soruya cevap arar: Türkiye'de yapay zekâ resepsiyonistini hangi işletme grubuna satmak, tek kişilik bir başlangıç için en mantıklısı?

Niş derken geniş bir sektörü değil, aynı hizmeti veren ve benzer derdi yaşayan işletme grubunu kastediyoruz. "Sağlık" niş değil. "Tek şubeli, randevuyla çalışan özel diş kliniği" niştir.

Ana hizmet yapay zekâ resepsiyonisti. İşletmenin yoğunken ya da mesai dışında açamadığı telefonu karşılar. Arayanın ne istediğini öğrenir, işletmenin belirlediği genel soruları cevaplar, uygun durumda randevu ya da geri arama kaydı açar, gerekince görüşmeyi bir çalışana aktarır ve konuşmanın bilgisini müşteri kayıt sistemine (CRM) işler. Dört sızıntının birincisi: açılmayan telefon.

Aynı müşteriye sonra satılabilecek iki ek hizmet var:
- Yeni taleplere hızlı dönüş. Reklamdan ya da site formundan gelen kişiyi kısa sürede arayıp ihtiyacını öğrenmek, uygun olana randevu açmak. Üçüncü sızıntı: dönülmeyen form.
- Eski talepleri yeniden değerlendirme. İşletmenin kayıtlarında duran ve iletişime uygun olan eski adaylara yeniden ulaşmak. Dördüncü sızıntı: geri aranmayan eski müşteri.

Niş ana hizmete göre seçilir. İki ek hizmet, aynı müşteriyle işi ileride büyütme fırsatı olarak değerlendirilir; seçimi tek başına değiştirmez.

Neden bu iş var: nisi-sec kartlarla hızlı karar verir. Bazen bundan fazlası gerekiyor. Öğrenci kartlardan emin olmuyor, kartı olmayan bir sektörü soruyor ya da kararın dayanağını bağlantılarıyla görmek istiyor. Bu modül o dayanağı çıkarır. Kararı vermez, kanıtı toplar ve önerir.

Şunlar bu modülün işi değildir:
- Nişi seçmek ve kilitlemek. O nisi-sec'in işi; bu modülün raporu ona girdi olur.
- Canlı sayım (nisi-dogrula).
- Aday listesi çıkarmak (aday-listesi-cikar).
- Niş değiştirmek. Kilit kuralları aynen geçerli; değişiklik kararı degisiklige-karar-ver'de.

Pazarlamadaki karşılığı: kaynağı gösterilebilen bir pazar gerekçesi. Öğrenci "neden bu sektör" sorusuna kendi raporundan, bağlantısıyla cevap verir.

## 2. Ne zaman çalışır

- Öğrenci "pazar araştırması yap", "hangi nişe gireyim, kaynaklı araştır", "resepsiyonisti hangi sektöre satarım" gibi bir cümle kurduğunda ya da niş araştırması komutuyla açıldığında.
- Birinci günün sırasına kendiliğinden girmez. Öğrenci isterse açılır.
- Niş henüz seçilmediyse rapor nisi-sec'e girdi olur. Kararı yine nisi-sec verir, son sözü yine öğrenci söyler.
- Niş seçildiyse ve kilitliyse modül yine çalışır ama kilidi açmaz. Rapor başka bir niş önerirse bu bir bulgu olarak yazılır ve üç yüzüncü temastaki bakışta okunur.
- Rapor yeniden istenirse yeni tarihli dosya açılır; eskisinin üstüne yazılmaz.
- Yirmi otuz dakika sürer. Öğrencinin tarafında beş dakika.

## 3. Ne okur

İş Beyni'nden: şehir, içeriden tanıdığı sektörler, telefonundaki işletme sahipleri, çalışma düzeni, günlük temas dağılımı, hedef gelir, seçilmiş niş varsa o ve kilidin durumu.
Komutla gelen ek bilgiden: şehir, özellikle bakılmasını istediği sektör, dışarıda bırakmak istediği sektör.
nis-kartlari modülünden: hangi nişlerin kartı olduğu. Yalnız liste alınır; kartın rakamları bu raporda kaynak sayılmaz.
İnternetten: güncel araştırma. Kurallar beşinci bölümde.

Başlangıç koşulları, İş Beyni başka bir şey söylemiyorsa şunlardır:
- Türkiye pazarı.
- Tek kişi başlıyor.
- İlk müşterilerine kendisi ulaşacak ve karar vericiyle doğrudan konuşmak istiyor.
- Uzun satın alma süreci, ağır teknik entegrasyon ve büyük ekip isteyen projeler başlangıçta dışarıda.
- Şehir ya da sektör bağlantısı yoksa Türkiye geneli değerlendirilir; şehir seçiminin sonucu değiştireceği yer ayrıca yazılır.

İş Beyni'nde şehir ya da içeriden tanıdığı sektör varsa rapor onları kullanır ve bunu raporun başında tek satırla söyler.

## 4. Ne sorar

Sormaz. Gereken bilgi İş Beyni'nde.

Tek istisna: İş Beyni yoksa ve komutla şehir gelmediyse tek soru sorar: "Hangi şehirdesin, bir de içeriden bildiğin bir sektör var mı? Yoksa 'yok' yaz, Türkiye geneline bakarım." Mesaj burada biter. Cevap "yok" ise Türkiye geneli.

Klasör bağlı değilse önce klasör kuralı işler; rapor klasör olmadan yazılmaz.

## 5. Ne yapar

### İnternet erişimi

Önce internete erişim olup olmadığına bakar. Yoksa bunu açıkça söyler ve rapor yazmaz: "Şu an internete erişemiyorum. Kaynaksız niş raporu yazmıyorum; bağlantı gelince açarız." Niş kararı bugün gerekiyorsa nisi-sec kartlarla ilerler.

### İki tur, bir yardımcı

Araştırma ağır iş. Arka plan yardımcısına (founderos:yardimci, Agent aracı) iki turda verilir. Sıralamayı ve öneriyi FounderOS yapar; yardımcı karar vermez.

**Birinci tur: tarama ve tablo.** Yardımcıya şunlar gider: başlangıç koşulları, şehir, içeriden tanıdığı sektörler, kartı olan nişlerin listesi, yedi soru, kanal ayrımı, veri ve kaynak kuralları, raporun birinci bölümünün biçimi ve dosyanın yeri. Yardımcı dosyanın yalnız başını ve birinci bölümünü yazar: tablo, her nişin kanıt notu ve yasal noktalar. İkinci, üçüncü ve dördüncü bölümün başlığını açmaz, kendi başına başka bölüm eklemez. FounderOS'a kısa özet döner: hangi sekiz niş, her birinin kanıt gücü, bulunamayanlar.

**Sıralama.** FounderOS dosyayı okur, ilk üçü aşağıdaki sırayla dizer ve başlangıç nişini seçer.

**İkinci tur: gerçek işletmeler.** İlk üç nişin her biri için Türkiye'den iki gerçek işletme. Yardımcı dosya yazmaz, altı işletmeyi özetinde döner: adı, şehri, sitesinin bağlantısı, kamuya açık bilgiden neden araştırma adayı olduğu. Her bağlantıyı açıp bakar; arama sonucundaki önizleme yetmez. Açılmayan sitenin işletmesi listeye girmez, yerine başkası bulunur.

**Tamamlama.** FounderOS dosyaya ikinci, üçüncü ve dördüncü bölümü ekler.

Yardımcıya verilen iş tek parça ve eksiksiz gider; yardımcı öğrenciyle konuşmaz, soru sormaz. İşin içine raporun dil kuralları da yazılır (aşağıda, raporun biçimi); yardımcının yazdığı bölüm de o kurallara uyar.

### Aday havuzu

Kartı olan nişler başlangıç listesidir, sınır değildir. Yardımcı kart listesinin dışındaki işletme gruplarına da bakar. Önce geniş bakar, sonra sekize indirir. Her niş hizmetiyle ve işletme tipiyle tanımlanır; geniş sektör adı tabloya girmez.

### Yedi soru

Her niş için:

1. Telefon araması bu işletmelerde müşteri kazanmanın önemli bir parçası mı?
2. Yoğunlukta ya da mesai dışında cevapsız kalan arama somut bir iş kaybına dönüşüyor mu?
3. Kazanılan bir ek müşterinin ekonomik değeri bu hizmete ödeme yapmayı anlamlı kılıyor mu?
4. Yeterli talep hacmi ve ödeme gücü var mı?
5. İşletme sahibine ya da karar vericiye ulaşmak kolay mı?
6. Sistemi kurmak ve faydasını ölçmek başlangıç seviyesinde uygulanabilir mi?
7. Hızlı geri dönüş ve eski talepleri değerlendirme için de fırsat var mı?

### Kanal ayrımı

Telefon, WhatsApp, Instagram ve form ayrı ayrı yazılır. Bir sektörün dijital kanalları yoğun kullanması telefon resepsiyonistine ihtiyaç duyduğunu göstermez. Çoğu zaman tersini gösterir: müşteri zaten WhatsApp'tan yazıyordur. Telefon ihtiyacı ancak telefona dair işaretle yazılır.

Telefonun ağırlığını gösteren, kamuya açık işaretler:
- İşletmenin sitesinde ya da harita kaydında randevu ve bilgi için telefonun öne çıkması: "hemen ara" düğmesi, tek iletişim yolu olarak numara.
- Acil ya da aynı gün istenen hizmet.
- Mesai dışı hizmet, nöbet ya da acil hattı.
- Resepsiyon ya da telefon karşılama için açılmış iş ilanları.
- Harita yorumlarında ve şikâyet sitelerinde "telefon açılmıyor", "ulaşamadım" türü ifadeler. Bunlar tekil deneyimdir; bu işaretin kanıt gücü en fazla sınırlıdır.

Form ve reklam tarafının işaretleri, ek hizmetler için: sitede teklif ya da randevu formu, reklam verip vermediği (reklam kütüphanesi), kampanya sayfaları.

### Veri ve kaynak kuralları

- Güncel araştırma yapılır. Her önemli iddianın yanında kaynak bağlantısı ve tarihi durur: yayın tarihi, yoksa erişim tarihi.
- Türkiye kaynakları önce gelir: resmî veri, meslek kuruluşları ve odalar, sektör raporları, işletmelerin kendi siteleri.
- Yurt dışı verisi Türkiye verisi gibi sunulmaz. Kullanılırsa "yurt dışı verisi, Türkiye için değil" diye etiketlenir ve karar ona dayanmaz.
- Veri bulunamayan yere "Türkiye için güvenilir veri bulunamadı" yazılır.
- Ortalama işlem tutarı, arama hacmi, kaçan müşteri sayısı ve dönüşüm oranı uydurulmaz.
- Her iddia üç etiketten birini taşır. **Doğrulanmış:** kaynağı ve tarihi var. **Çıkarım:** kaynaktan yapılan yorum; hangi kaynaktan çıktığı yazılır. **Varsayım:** hesap için konan, doğrulanması gereken rakam. Varsayımla yapılan hesap varsayım olarak kalır.
- Yüksek işlem tutarı tek başına yetmez. Talep hacmi, satışa dönüşme ihtimali ve mümkünse kârlılık da yazılır.
- Reklam veren ya da randevuyla çalışan her işletmenin bu sorunu yaşadığı varsayılmaz.
- Niş kartlarının rakamları bu raporda kaynak sayılmaz. Kartın bir rakamı dış kaynağa dayanıyorsa o kaynak bulunur ve onun bağlantısı verilir.
- Kaynak adı yetmez, bağlantı olur. Açılmayan bağlantı kullanılmaz.

Kanıtın gücü üç derecedir:
- **Güçlü:** en az iki bağımsız Türkiye kaynağı, ya da resmî veri ile işletmelerin kendi sitelerinden tutarlı gözlem.
- **Sınırlı:** tek kaynak, ya da yalnız işletme sitelerinden ve yorumlardan gözlem.
- **Henüz doğrulanmamış:** Türkiye verisi yok; yalnız çıkarım ya da yurt dışı verisi.

### Kontrol edilecek yasal noktalar

Rapor hukuki görüş vermez. Güncel resmî kaynaktan kontrol edilmesi gereken noktaları kısaca listeler ve her birine resmî kaynağın bağlantısını koyar:
- Kişisel veri: arayanın bilgisinin kaydı, konuşmanın kaydedilmesi, aydınlatma yükümlülüğü, verinin yurt dışındaki bir servise gitmesi. Kaynak: Kişisel Verileri Koruma Kurumu (kvkk.gov.tr) ve mevzuat.gov.tr.
- Otomatik ve ticari arama: hızlı dönüş ve eski talep aramalarında onay şartı, bu aramaların ticari ileti sayılıp sayılmadığı, İleti Yönetim Sistemi (İYS) kaydı. Kaynak: 6563 sayılı Kanun ve ilgili yönetmelik (mevzuat.gov.tr), iys.org.tr.
- Arayana yapay zekâyla konuştuğunun söylenmesi: Türkiye'de bağlayıcı bir kural olup olmadığı.
- Sektörel kısıtlar: seçilen üç nişe özel reklam, tanıtım ve hasta ya da müvekkil bilgisi kuralları.

Bulunan kural kaynağı ve tarihiyle yazılır. Bulunamayan "kontrol edilemedi" diye yazılır.

### Raporun biçimi

Dosya çalışma klasörüne `nis-arastirmasi.md` adıyla yazılır. Bu adla bir dosya varsa `nis-arastirmasi-GG-AA-YYYY.md`.

Başlık iskeleti sabittir, başka başlık açılmaz:

    # Niş araştırması
    ## 1. Karşılaştırma tablosu
    ### 1a. Kanıt notları
    ### 1b. Kontrol edilecek yasal noktalar
    ## 2. En uygun üç niş
    ## 3. Gerçek işletme örnekleri
    ## 4. Başlangıç önerisi

Bulunamayan bilgi ayrı bölüm olmaz: her nişin kanıt notunda yerinde yazılır, toplamı dördüncü bölümün "kesinleşmeyen noktalar" listesine girer.

Başlığın altında dört satır: tarih, bakılan coğrafya, İş Beyni'nden alınan koşullar, internet erişimi.

Sonra sabit sırayla dört bölüm.

**1. Karşılaştırma tablosu.** En fazla sekiz somut niş. Her niş için:
- Hedeflenecek işletme türü.
- Ana hizmete neden ihtiyaç duyabilir?
- Ekonomik değer nereden oluşur?
- Karar vericiye ulaşmak ve sistemi kurmak ne kadar kolay?
- En önemli engel ya da belirsizlik.
- Kanıtın gücü: güçlü, sınırlı ya da henüz doğrulanmamış.

Tablonun altında her niş için kısa kanıt notu: yedi sorunun cevabı, dört kanalın ayrı durumu, etiketli iddialar ve bağlantıları.

**2. En uygun üç niş.** Başlangıç koşullarına göre sıralı, nedenleriyle. Her biri için:
- Hangi özellikteki işletmeler hedeflenir?
- Hangi özellikteki işletmeler elenir?
- İşletme sahibiyle konuşurken hangi somut problem araştırılır?
- İhtiyacın gerçekten var olduğunu doğrulamak için sorulacak beş soru.
- FounderOS'ta bu nişin kartı var mı?

Beş soru işletme sahibinin kendi deneyimini sorar, çözümü satmaz. "Yapay zekâ resepsiyonisti ister misiniz" diye soru yazılmaz. "Geçen hafta mesai dışında kaç arama geldi, bunu nereden biliyorsunuz?" gibi, rakamı ve kaynağı işletmecinin kendisinden çıkaran sorular yazılır.

**3. Gerçek işletme örnekleri.** İlk üç nişin her biri için Türkiye'den iki gerçek işletme ve sitesinin bağlantısı. Yalnız kamuya açık bilgiyle neden araştırma adayı oldukları yazılır. Bu işletmelerin cevapsız arama sorunu yaşadığı ya da hizmeti satın alacağı iddia edilmez. Çalışan adı, kişisel cep numarası gibi kişisel bilgi yazılmaz.

**4. Başlangıç önerisi.** Tek niş. Altında:
- En güçlü üç gerekçe.
- En önemli belirsizlik.
- Hangi bulgu ortaya çıkarsa kararın değişmesi gerektiği.
- Masa başı araştırmayla kesinleşmeyen noktalar, ayrı liste.
- Kararı doğrulamak için ilk beş işletme görüşmesinde öğrenilecekler.

Dil sade Türkçe. Teknik terim ilk geçtiği yerde açıklanır. Genel sektör tanıtımı yazılmaz; yalnız niş seçtiren bulgu yazılır. Uzun çizgi (—) kullanılmaz, cümle bölünür. İngilizce iş jargonu yazılmaz, Türkçesi yazılır: "front-desk" değil "ön büro" ya da "resepsiyon". Bu kurallar sohbete yazılan özet için de geçerli.

### Sıralama

İlk üçü FounderOS dizer. Ağırlık sırası:

1. Telefonun müşteri kazanmadaki payı ve kaçan aramanın somut kaybı (birinci ve ikinci soru). Bu ikisi zayıf olan niş, diğer sorularda ne kadar iyi olursa olsun ilk üçe girmez.
2. Karar vericiye ulaşmak ve kurulumun kolaylığı (beşinci ve altıncı soru). Tek kişilik başlangıçta darboğaz burası.
3. Ekonomik değer ve hacim birlikte (üçüncü ve dördüncü soru). Yüksek işlem tutarı tek başına öne geçirmez.
4. Ek hizmet fırsatı (yedinci soru). Eşitliği bozar, sıralamayı tek başına değiştirmez.
5. Kanıtın gücü. Benzer durumdaki iki nişten kanıtı güçlü olan öne geçer.

İçeriden tanıdığı sektör ilk üçe girdiyse bir basamak öne alınır ve sebebi yazılır: o sektörün dilini biliyor, işletmeci bunu ilk otuz saniyede anlıyor.

Kartı olmayan niş ilk üçe girebilir. Başlangıç önerisi o olursa bunu tek cümleyle söylersin: bu nişin kartı yok, mesajlar ve itiraz cevapları sahadan kurulacak.

Başlangıç önerisinin kanıtı en az sınırlı olur. Sekiz nişin hiçbiri sınırlıya çıkmıyorsa öneri yine verilir ve raporun başına tek satır yazılır: "Kanıt zayıf; karar ilk beş görüşmeyle verilecek."

## 6. Ne söyler

Başlarken tek cümle ve aynı mesajda araştırmayı başlatırsın: "Kaynaklı bir niş araştırması yapıyorum, yirmi otuz dakika sürer. Bitince özeti buraya, tamamını klasörüne yazacağım."

Bitince sohbete en fazla dört cümle: önerilen başlangıç nişi ve en güçlü gerekçesi, en önemli belirsizlik, raporun yeri, sıradaki iş. Tablo sohbete dökülmez.

Niş seçilmemişse: "Rapor [niş] diyor, sebebi [tek cümle]. Kararı şimdi birlikte veriyoruz." Sonra nisi-sec açılır.

Niş seçilmiş ve rapor aynı nişi öneriyorsa: "Rapor seçtiğin nişi destekliyor. İlk beş görüşmede soracağın beş soru hazır."

Niş seçilmiş ve rapor başka niş öneriyorsa: "Rapor başka bir nişi öne koyuyor: [niş], çünkü [tek cümle]. Pazarın üç yüz temasa kadar kilitli; bu bulguyu o gün birlikte okuyacağız."

Ölçülemeyen yeri saklamazsın: "Arama hacmi için Türkiye verisi bulunamadı. Karar telefonun önemine dair işaretlere dayanıyor."

## 7. Ne yazar

Klasöre: `nis-arastirmasi.md` ya da tarihli adı.
İş Beyni'nin üçüncü bölümüne, tarihiyle tek satır: dosyanın adı, önerilen başlangıç nişi, ilk üç, seçili nişle çelişen bulgu varsa o.
İş Beyni'nin on üçüncü bölümüne: ilk beş görüşmede öğrenilecekler, tek satır.
Niş kartına hiçbir şey yazmaz. Kartla çelişen bulgu İş Beyni'ne yazılır; kartı değiştirmek bu modülün işi değil.

## 8. Yedek yol

- İnternet yoksa rapor yazılmaz, sebebi tek cümleyle söylenir. Niş kararı gerekiyorsa nisi-sec kartlarla ilerler.
- Yardımcı çalışmazsa araştırmayı FounderOS kendisi yapar, sekiz yerine beş nişle. Bağlam yükü sebebiyle tablo yine dosyaya yazılır, sohbete dökülmez.
- Bir niş için Türkiye kaynağı hiç çıkmazsa niş tabloda kalır, kanıt gücü "henüz doğrulanmamış" yazılır.
- Bir niş için iki gerçek işletme bulunamazsa bulunan kadar yazılır, eksik yere "bulunamadı" yazılır.
- Bağlantı açılmazsa o kaynak kullanılmaz.

## 9. Sıradaki adım ve işaretler

Sıradaki: niş seçilmediyse nisi-sec, rapor ona girdi. Niş seçildiyse günün planına dönülür; ilk beş görüşmenin soruları İş Beyni'nde durur ve görüşme hazırlığında okunur.

İşaretler (FounderOS okur, sen bir şey yapmazsın):
- Önerilen başlangıç nişinin kartı yok: on üçüncü bölüme "kartı olmayan niş önerildi: [niş], [tarih]" yazılır. Kart eksikliği işaretlenir.
- Rapor seçili nişle çelişiyor: üç yüzüncü temastaki bakışta okunur, öncesinde niş değişmez.
- Sekiz nişin çoğunda kanıt "henüz doğrulanmamış": masa başı araştırma yetmiyor, karar ilk beş görüşmeyle netleşir.

Beş kural: boş sayfa yok (tablo, üç niş, gerçek örnekler ve beş soru hazır gelir) · sessiz bitiş yok (rapor, sıradaki işle kapanır) · onay (niş kararı bu modülde verilmez, nisi-sec'te öğrencinin "tamam"ıyla verilir) · sahadan güncelleme (ilk beş görüşmenin cevabı raporun belirsizliğini kapatır) · sormaz söyler (araştırır, sıralar, tek niş önerir; seçenek menüsü sunmaz).
