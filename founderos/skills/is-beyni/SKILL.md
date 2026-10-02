---
user-invocable: false
name: is-beyni
description: "Is Beyni'nin on sekiz bolumlu semasi, yazma kurallari ve bos sablonu. Kayit ilk kez acilirken ve bir bilginin hangi bolume yazilacagi belirsizken acilir."
---

# İş Beyni (dosyanın yapısı)

İş Beyni, öğrenci ve işi hakkında bugün bilinen her şeyin yazıldığı dosya. Bütün modüller ondan okuyor ve ona yazıyor. Bu bölüm o dosyanın hangi bölümlerden oluştuğunu, hangi modülün nereye yazdığını ve kuralları tanımlıyor; yanındaki üç kayıt yerini (durum kaydı, günlük, müşteri dosyası) de sonda tarif ediyor. Modüller "İş Beyni'ne şunu yaz" dediğinde yazılan yer burada tarif edilen bölümdür.

Dosya öğrencinin bilgisayarında duruyor, tek dosya, on sekiz bölüm. Bölümlerin sırası ve adları sabit; modüller bu adlarla arıyor.

## Kurallar

**Her alanda tek güncel değer.** İş Beyni bugünün gerçeğini tutar. Bir bilgi değişince yerinde güncellenir; eski değer ve sebebi o günün günlüğüne (`gunluk/YYYY-AA-GG.md`) tek satır olarak yazılır. "Kurulum 100.000" satırı "Kurulum 110.000" olur, günlüğe "kurulum 100.000'den 110.000'e çıktı" ve sebebi düşer. Neyin ne zaman değiştiği günlükten okunur; İş Beyni'nde eski sürümler üst üste birikmez.

**Kayıtlar günlüğe, son değer buraya.** Her gün yeniden oluşan kayıtlar İş Beyni'ne eklenmez, günlüğe yazılır: akşamın beş sayısı, haftalık kararlar, takılmalar, aylık kâr hesapları, prova kayıtları. İş Beyni'nde o alanda yalnız son değer ve koşan toplam durur. Bir modül "altına ekle" ya da "tarihli, üstüne eklenir" diyorsa satır günlüğe gider. Hedef: İş Beyni 15 KB altında kalır; büyüyorsa bir kayıt yanlış yere yazılıyor demektir.

**Değişen satırın tarihi var.** Her alanın yanında son güncellendiği tarih durur.

**Kilitli satırlar işaretli.** Mesaj metni, teklifin kelimeleri, fiyatın rakamı ve niş kilitli satırlardır; yanlarında hangi eşikte açılacakları yazıyor. Eşik dolmadan bu satırlar değişmiyor.

**Boş bölüm silinmiyor.** Henüz sırası gelmemiş bölüm başlığıyla duruyor, altında "henüz yok, [hangi adımda] dolacak" yazıyor; boş bölüme tarih atılmıyor, tarih ancak satır dolunca yazılıyor. Öğrenci dosyayı açtığında neyin dolup neyin beklediğini görüyor.

**Öğrenci dosyayı elle düzenlemiyor.** FounderOS yazıyor, öğrenci okuyor ve düzeltme istiyor.

## Bölümler

### 1. Kurucu
Kim olduğu ve nasıl çalıştığı. Lisans anahtarı (ilk mesajda sohbete yazdırılır, buraya yazılır, bir daha sorulmaz), ad (lisanstan gelir), şehir, telefon, e-posta, çalışma düzeni (tam zamanlı ya da işin yanında; saate göre: günde altı saat ve üstü tam zamanlı, altı işin yanında), haftalık teslimat saati, hazırlık seviyesi, günlük temas dağılımı (arama, Instagram, e-posta, video), klasörün tam yolu, başlangıç tarihi, panel linki (lisans doğrulamasının cevabından; öğrencinin telefonundaki paneli).
Tanışma cevapları: sekiz zorunlu sorunun cevabı, her biri geldiği anda tek satır (iş ve günlük saat, şehir, aylık zorunlu gider, dayanma süresi, satış tecrübesi, telefonun ne kadar zorladığı, işletme sahiplerine kapı, aylık hedef). Bekleyen sorulardan cevaplananlar da buraya eklenir; henüz sorulmamış olanlar burada değil, durum kaydında durur.
Dayanma süresi: hiç gelir gelmezse kaç ay idare ettiği. Üç aydan azsa çalışma düzeni işin yanında yazılır; şartın durumu ikinci bölümdeki "Üç aylık yaşam gideri şartı" satırındadır.
Başlangıç değerlendirmesi (dört başlık) ve kurucu bölümünün dört satırı: ne motive ediyor, ne durduruyor, daha önce ne denedi ve neden bıraktı, düşme riski nerede. Dolmayan satır boş durur, uydurulmaz.
Yazan: isini-kur (birinci gün ve bekleyen sorular cevaplandıkça), hizmet-akisini-ciz.

### 2. Hedef ve para
Vizyon: bir yıl sonra hayat, bir yıl sonra iş, çalışma sınırları (haftada kaç saat, hangi pencereler, tek başına kaç müşteri), seçilen kombinasyon ve tempo, tarihiyle. Zihniyet kabulü ve tarihi.
Hedef gelir, gelir planının bütün basamakları, güncellenmiş aylık ücret, aylık masraf tablosunun dört bölümü, çıkış hesabının dört satırı ve üç aylık yaşam gideri şartı.
Aylık kâr: yalnız son değerler (bu ayın kârı, kâr marjı, müşteri başına kâr, tekrar eden aylık gelir), yerinde güncellenir. Ayın hesabının tamamı (gelir kurulum ve aylık ayrımıyla, gider kalemleri tek tek, banka hesabındaki değişim) o günün günlüğüne yazılır.
Yazan: isini-kur, zihniyet, vizyon-belgesi, araclari-kur, nisi-sec, kari-hesapla.

### 3. Niş
Seçilen niş, seçim tarihi, coğrafya (şehir mi Türkiye geneli mi), doğrulama tablosu ve tarihi, ikinci ve üçüncü aday niş, sezon durumu. Niş araştırması yapıldıysa: dosyanın adı, önerilen başlangıç nişi, ilk üç ve seçili nişle çelişen bulgu, tarihiyle. İdeal müşterinin tek cümlelik tanımı ve hedeflenen işletme büyüklüğü (ayrıntısı on sekizinci bölümde).
Niş kilidi: doksan gün ya da beş müşteri, hangisi önce gelirse. Kilidin başlangıç tarihi burada yazılı.
Yazan: nisi-sec, nisi-dogrula, nis-arastirmasi.

### 4. Teklif ve fiyat
Konumlandırma cümlesi (uzun, kısa, itiraz cevabı). Dönüşüm Cümlesi beş parçasıyla, sistemin adı, bir dakikalık anlatım, üç kademenin nişe özel içeriği.
Kurulum ücreti, aylık ücret, karşılaştırma fiyatı, deneme fiyatı işareti ve üç karşılık, güvence cümlesinin tam metni ve şartları, "fiyat ne" sorusunun cevabı.
En sık çıkan üç itiraz ve cevapları. Kartın kaçan müşteri rakamı ve o rakamdan çıkan kurtarma tahmini. Önce/sonra tablosu (günü, kendini görüşü, duygusu, acısı ve hayali; sürümü ve tarihi). Teklif notları: son on görüşmede teklifle ilgili tekrar eden işaretler.
Kilitli satırlar: teklifin kelimeleri on görüşmede, fiyatın rakamı otuz görüşmede açılıyor. Burada güncel sürüm, sürüm numarası ve tarihi durur; eski sürüm değiştiği gün günlüğe yazılır.
Yazan: konumlandir, teklifi-yaz, fiyati-belirle, gorusmeyi-analiz-et.

### 5. Teslimat
Birinci gün teslimat uygunluk kontrolü: beş başlığın sonucu, teklif dışında kalanlar, şartlı parçalar, tarih. hizmet-akisini-ciz'in birinci gün bölümü (4b) yazar, teklif gövdesi buna bakar.
Rapor günü: tek sayı, 21 ya da 28; çalışma düzeni belli olduğu an yazılır, belgeler bu sayıyı okur.
Müşteriye gösterilecek beş satır, ölçüm satırları ve doldukları tarih, kapasite hesabı (ilk müşteriden sonra), görüşmede söylenecek üç cümle, müşteriden istenecekler listesi, dört dosyanın adı ve durumu.
Yazan: hizmet-akisini-ciz, isini-kur (rapor günü).

### 6. Marka ve varlıklar
Marka kitinin yeri, renkler, yazı tipleri, logo ve en küçük boyutu, görsel yön. Dosya haritası: `marka/` altındaki her dosyanın adı, ne işe yaradığı, nerede durduğu; modüller logoyu ve görselleri buradan bulur. Eksik gerçek bilgiler satırı: henüz olmayan telefon, e-posta ya da adres ve hangi dosyayı beklettiği. Açılış görseli hangi kaynaktan (video kapağı, kurucu fotoğrafı, marka görseli).
Instagram kullanıcı adı ve hesap yaşı, profil fotoğrafının yeri, WhatsApp Business numarası ve karşılama mesajı, e-posta imzası metni, YouTube kanal adresi, biyografi metni ve sürümü. YouTube kanalının doğrulandığı tarih (video kapağı için), LinkedIn profil adresi ve güncellenme tarihi.
Seçilen alan adı ve uzantısı, boş olduğunun kontrol edildiği tarih, yedek alan adı, alınıp alınmadığı ve nereden alındığı, canlı site adresi, ön görüşme sayfasının adresi, proje klasörünün yeri, sayfanın metin sürümü ve tarihi, müşteri gelince değişecek bölümler.
Video adresleri: ön görüşme videosu, üç itiraz videosu, deneme videosu, kanıt ekran kaydı.
Yazan: markani-kur, kisisel-markani-kur, siteni-kur, satis-videosunu-cek, satis-sayfasini-yaz, isini-kur, icerik-motoru.

### 7. Araçlar ve hesaplar
CRM bölümünün adresi, bağlanan Google hesabı, işaretlenen çalışma saatleri, arama yapacağın numara, sesli mesaj metni.
Veri servisi: bu ay alınan kayıt sayısı ve tavan; sayım çekimleri (tarih, üç nişin iş kimlikleri, ilk nişten gelen kayıt sayısı); son liste çekiminin tarihi, kategorisi, şehri ve iş kimliği; yedek yola geçildiyse tarihi.
Claude aboneliğinin aylık tutarı. Hatırlatmaların nasıl açıldığı (panelden telefon bildirimi ya da yedek yol olarak takvim alarmı) ve otomatik eşitlemenin açıldığı tarih.
Tarayıcı demosunun adresi, dosyası, test tarihi ve demo kaydının yeri. Sesli örnek: kuruldu mu, tarihi, kaydın yeri. Sesli demo: demo sayfasında açık mı, tarihi.
Ödeme sağlayıcı ve link adresleri, sözleşmenin sürümü ve doldurulma tarihi. Şirket satırı (şirketin durumu, müşavirin adı, müşavire giden soruların cevabı) ilk "evet" günü açılır; o güne kadar bu satır dosyada yer almaz.
CRM kurulumu: dokuz aşamanın doğrulandığı, kayıt satırlarının tam listesi, takip zincirinin günleri, aynı numaranın birleştiğinin doğrulandığı.
Yazan: araclari-kur, musteri-takip-sistemini-kur, aday-listesi-cikar, kanitini-hazirla, onay-belgesini-hazirla (şirket satırı ilk "evet" günü).

### 8. Listeler
Sıcak çevre: A listesindeki kişi sayısı, B listesindeki kişi sayısı, listenin çıkarıldığı tarih, hangi kaynaklardan tarandığı.
Soğuk liste: çıkarılma tarihi, ham kayıt sayısı, elenen sayı, kalan sayı, kaç işletmenin sahibinin adı bulundu, kullanılan kategori adı ve kapsanan ilçeler.
En çok istenen yüz işletme: seçim tarihi, kaç kişi, hangi ölçütlerle seçildi.
Yazan: tanidik-listesi-cikar, aday-listesi-cikar.

### 9. Mesajlar ve kanıt
Her kanalın mesaj metni, sürümü ve tarihi. Sıcak çevrenin iki mesajı ve mesajda geçen sayı. Kanca listesi ve hangisinin cevap aldığı. Günlük gönderim sayısı ve e-posta alıştırma tarihi.
Kanıt: deneme aramasının sonuçları, kanıt cümlesi ve güncellenme tarihi, kanıt hikâyesi, paylaşım izninin yazılı olup olmadığı.
İçerik: başlangıç tarihi, çekim yolu (yüz ya da ses), son hafta (tarih, tema, konu türü, beş parçadan kaçı yayında) ve içerikten gelen ilgi (koşan toplam: yazan işletme, görüşmede içerikten söz eden). Haftaların ayrıntısı günlükte ve panel dosyasının geçmişinde.
Kilitli satır: mesaj metni üç yüz temasta açılıyor, elli temastan önce hiç dokunulmuyor.
Yazan: adaya-mesaj-yaz, tanidiga-mesaj-yaz, video-mesaj-cek, kanitini-hazirla, icerik-motoru.

### 10. Sayılar
Gün sayacı; birinci bölümdeki başlangıç tarihinden hesaplanır, ikisi tutmuyorsa tarih üstündür. Koşan toplam: bugüne kadar kaç temas, kaç cevap, kaç randevu, kaç görüşme, kaç müşteri (durum kaydındaki sayaçlarla aynı). Son akşamın beş sayısı ve tek cümlesi yalnız son değer olarak durur; her akşamın sayıları (sıcak ve soğuk ayrımıyla), haftalık toplamlar ve akşam cümleleri günlükte.
Sayaçlar: görüşme sayacı, prova ve temiz prova sayacı (son beş provanın sonucuyla), itiraz sayacı, fiyat itirazı sayacı, evet ile ödeme arası süre.
Eşikler ve nerede olunduğu: iki yüz temas, üç yüz temas ve karar günü (yazılı kanalda üç yüzüncü temasın yedinci günü), otuz randevu, otuz görüşme. Bu satırı her akşam rakamlari-oku yazar.
Yazan: rakamlari-oku, gorusmeyi-analiz-et, gorusme-provasi-yap, gorusmeye-getir, video-mesaj-cek, gunu-planla.

### 11. Kararlar
Yürürlükteki karar: bu haftanın tek değişikliği, numarası, değişen alanın yeni hali ve tarihi. Haftalık karar kaydının kendisi (haftanın tarihi, dört halkanın sayıları, en zayıf halka ve sebebi, ne değiştirildi, geçen haftanın kararının sonucu) günlüğe yazılır ve orada silinmeden durur.
Tek değişken kuralı günlükten denetleniyor: aynı hafta iki değişiklik yazılmışsa o testin verisi geçersiz sayılıyor.
Yazan: degisiklige-karar-ver.

### 12. Müşteriler
Yalnız aktif müşteri listesi, her müşteri tek satır: adı, dosyası (`musteriler/<musteri-adi>.md`), teslimat günü (teslimatın kaçıncı günü; rapor gününden sonra "teslim edildi"), aylık ücret. Müşterinin ayrıntısı burada değil, kendi dosyasında durur (aşağıda, "Müşteri dosyası"); modüller "bilgi dosyasına yaz" dediğinde yazılan yer o dosyadır.
Ayrıca: aktif müşteri sayısı, ilk müşteri tarihi, müşteri başına haftalık saat. Aktif müşterilerin adları durum kaydında da durur.
Yazan: musteriyi-karsila (müşteri geldiği gün satırı ve dosyayı açar), teslimat modülleri (teslimat günü), musteriyi-elde-tut (aktif müşteri sayısı), kari-hesapla (aylık ücret).

### 13. Açık işler
İlk satır her zaman "Sonraki adım": tek cümle, her akşam yeniden yazılır; durum kaydındaki `sonraki_adim` ile aynıdır. Ertesi sabah açılış cümlesi buradan çıkar.
Cevabı beklenen işler (müşavirin cevabı, müşterinin onayı gibi) ve her birinin hangi güne ya da hangi eşiğe bağlı olduğu. Tanışmanın bekleyen soruları burada değil, durum kaydında durur. Ertelenen istekler ve hangi eşikte açılacakları. Ertesi güne kalan iş. Ertelenen bir iş üç kez ertelendiyse yanına sebebi yazılır: büyük mü, belirsiz mi, bilgi mi eksik; o satır plana "ödev" olarak değil "küçültülmüş iş" olarak döner.
Bu bölüm her sabah gunu-planla tarafından okunuyor; sırası gelen açık iş o günün planına giriyor.
Yazan: bütün modüller.

### 14. Aşama ve tamamlanma
Yalnız beş ilerleme aşamasının satırları: hazırlık tamamlandı, ilk işletmeyle görüştün, ilk satışını yaptın, hizmeti teslim ettin, müşterin kullanıyor. Her aşamanın tamamlanma ölçütü ilgili modülde yazılı; burada her satırda "tamam" ya da "eksik", tarih ve kanıtın yeri durur. Güzel bir paragraf aşamayı tamamlamaz; ölçütlerin hepsi "tamam" olmadan aşama kapanmaz.
Aşama kapanınca tek satır: ne bitti, ne zaman, kanıtı nerede.
Konum bu bölüme yazılmaz. Hangi blokta, hangi oturuşta, Yol Haritası'nın hangi aşamasında olunduğu ve sıradaki adım durum kaydındadır (aşağıda).
Yazan: nisi-sec, teklifi-yaz, siteni-kur, aday-listesi-cikar, sahaya çıkış kontrol listesi ("1. Hazırlık tamamlandı" satırı), gorusmeyi-analiz-et, onay-belgesini-hazirla, musteri-sistemini-kur.

### 15. Bugünün listesi
CRM'siz modda günün özeti: randevular (kim, ne zaman, hangi kanaldan), cevap verip dönüş bekleyenler, bugün takip günü gelen sıcak kayıtlar, dün ne oldu. Soğuk havuz burada tutulmaz: soğuk adaylar, sıradaki hareketleri ve günün arama sırası aday listesinde (`adaylar.csv`) durur. Sabah okunur, akşam işlenir. CRM açılınca yalnız sıcak kayıtlar (cevap veren, randevu alan, müşteri) bir kere oraya taşınır ve bu bölüm "CRM'e taşındı, tarih" satırıyla kapanır; soğuk havuz aday listesinde kalır. Aynı bilgi iki yerde tutulmaz.
Yazan: gunu-planla, adaya-mesaj-yaz, rakamlari-oku, araclari-kur.

### 16. Taslaklar
Hazırlanmış ama henüz kullanılmamış her şey: gönderilmemiş mesaj, onaylanmamış teklif sürümü, çekilmemiş video metni, doldurulmamış sözleşme. Her satırda ne olduğu, ne zaman hazırlandığı, neyi beklediği. Kullanıldığı gün buradan çıkarılır ve günlüğe "kullanıldı" diye tek satır düşer. Bu bölüm dolup taşıyorsa sistem üretip öğrenci kullanmıyor demektir; bu bir işarettir.
Yazan: bütün modüller.

### 17. Takılmalar ve destek
Her takılma olduğu gün günlüğe yazılır: tarih, cümlesi ("anlamadım", "yapamadım", "bende bu ekran yok"), sorunun türü (bilgi, erişim, teknik hata, uygulama), ne denendi, çözüldü mü. Burada çözülmemiş takılmalar ve bulunan çözümler durur: desteğe aktarılan durumda gönderilen özet ve gelen cevap, işe yarayan çözüm. Bir daha aynı yerde takılınca önce buraya bakılır; çözülen takılma buradan tek satırlık çözüme iner.
Yazan: bütün modüller.

### 18. İdeal müşteri
Nişin içindeki tek kişinin tarifi. On iki başlık: tek cümlelik tanım, günü nasıl geçiyor, üç derdi kendi cümleleriyle, üç korkusu, satın alma tetikleyicisi, karar biçimi, nereden bilgi alıyor, daha önce ne denedi ve neden bıraktı, itiraz olmayan itirazlar, müşterinin müşterisi, ne satın almaz, FounderOS'un yorumu.
Her satırın yanında kaynağı yazılı ve her satır ya "bulgu" ya "yorum" diye işaretli; ikisi hiçbir zaman karışmıyor. Alıntılar düzeltilmeden duruyor.
Eleme listesi bu bölümün altında: bu tipe satmıyoruz satırları. aday-listesi-cikar sıralamayı, aday-denetimi-cikar uygunluk puanını buradan alıyor.
Sürüm ve tarih: masabaşı sürümü birinci blokta yazılıyor, saha sürümü onuncu görüşmeden sonra onun yerine yazılıyor; masabaşı sürümü o gün günlüğe taşınır, silinmez.
Yazan: ideal-musteriyi-cikar, gorusmeyi-analiz-et.

## Doksan Gün Planı nerede duruyor

Doksan Gün Planı İş Beyni'nin içinde değil, ayrı bir dosya olarak yanında duruyor. Dosyanın adı `doksan-gun-plani.md`, nişin kartı da yanında `nis-karti.md`. On altı bölümlük metin birinci blokta fiyat bandı konduktan sonra arka plan yardımcısı tarafından yazılıyor, ikinci bloğun doğrulamasıyla ve üçüncü bloğun kesin fiyatıyla güncelleniyor ve doksan gün boyunca modüller ona bakıyor. gorusmeyi-analiz-et sahadan gelenlerle günceller.

Niş kartı da ayrı bir dosya olarak duruyor. Kart on altı bölümlü sabit yapıda, sonunda bir de Kaynaklar bölümü var; modüller kartı bölüm adıyla okuyor: Kapsam, Gerçek fiyatlar ve kapasite (sonunda kayıp birimi), Sızıntı nerede, Sezon, Rekabetin şekli, Kim karar veriyor, İşletmecinin gerçek dertleri (sonunda sözlüğü ve iç sesi), Açılış cümlesi, Duran havuz, Asistan kuralları, Kanal ve zaman, Reklam kütüphanesi kelimeleri, Yasal sınırlar, Yoğun şehirler, Gerçek itirazlar ve karşılıkları (başında en güçlü üç itiraz), Sahadan dolacak, Kaynaklar.

## Klasörde neler duruyor

Öğrencinin klasöründe duranların tam listesi:
- `is-beyni.md`: İş Beyni, güncel gerçek.
- `doksan-gun-plani.md`: Doksan Gün Planı.
- `nis-karti.md`: seçilen nişin kartı (yasal sınırlar bölümü gizli dosyada).
- `.founderos/nis-sinirlar.md`: kartın yasal sınırları ve niş araştırmasının sınır kontrolü; model başvurusu, öğrenciye gösterilmez.
- `gunluk/`: her günün kayıt dosyası (aşağıda).
- `musteriler/`: her müşterinin bilgi dosyası (aşağıda).
- `.founderos/`: gizli klasör; durum kaydı (`durum.json`, aşağıda) ve aday aracı.
- `marka/`: marka kitinin gerçek dosyaları.
- `site/`: tanıtım sayfasının dosyaları.
- `icerik/`: haftanın içeriği, hafta başına bir klasör (`icerik/<YYYY-AA-GG>-<tema>/`): video metni, kesitler, LinkedIn gönderisi, kaydırmalı gönderinin görselleri, video ve Reels kapakları, haftanın panosu. Bu haftanın panel kaydı `.founderos/panel/icerik.json`.
Aday listesi ve sayfası (`adaylar.csv`, `adaylar.html`) ile modüllerin kendi çıktıları (tanıdık listesi, denetim kartları, niş raporu) klasörün kökünde durur. Başka alt klasör açılmaz. Modüller İş Beyni'ni, planı ve kartı bölüm adıyla okuyor.

## Durum kaydı (`.founderos/durum.json`)

Tek konum kaydı. Öğrencinin nerede olduğu İş Beyni'ne değil buraya yazılır. Alanlar: `gun_baslangic`, `duzen` (tam ya da yan), `blok`, `oturus`, `adim`, `acik_modul`, `sonraki_adim`, `yol_haritasi_asamasi` (1-9), `ilerleme_asamasi` (1-5), `saha_acik`, `sayaclar` (temas, cevap, randevu, gorusme, musteri, prova, temiz_prova), `son_temas_tarihi`, `bekleyen_sorular` (henüz sorulmamış tanışma soruları, kısa adı ve anıyla), `aktif_musteriler`, `gunluk_hedef` (bugünün temas sayısı; tam zamanlıda 100, işin yanında 40, işin yanında çalışanın ilk müşteri teslimi süresince 20), `gecim_musteri` (geçimini karşılayan müşteri sayısı: gelir planındaki "kaç müşteride bu gider karşılanıyor" satırı, yukarı yuvarlanmış tam sayı, 1 ile 60 arası; isini-kur yazar, fiyat kesinleşince fiyati-belirle günceller; panelde geçim hedefi olarak görünür), `siradaki_cekim` (yalnız liste stoğu beş günün altına inince: kategori, şehir, ilçe, hedef, reklam kelimeleri, istek tarihi; gece hazırlığı okur, sabah liste alınınca silinir), `son_kapanis` (kapanışı yapılan son iş günü; sabah ve akşam, kapanışı atlanan günler önce kapanır, en çok yedi gün geriye), `panel_turu` (panel turunun açıldığı gün; boşsa ve panel linki yazılıysa günaydın turu bir kez açar), `guncellendi`. `sonraki_adim` öğrencinin panelinde görünür: öğrenciye yazılmış tek cümledir, içinde beceri adı ve blok numarası geçmez. Her modül bitince ve her oturum kapanırken güncellenir. Veri bağlantısı açıksa aynı içerik `durum_yaz` ile sunucuya da yazılır; hata olursa sessizce geçilir, klasördeki kayıt yine yazılır. Panel ve hatırlatmalar sunucudaki kopyayı okur; `sonraki_adim` sabah telefona bildirim olarak da gittiği için kısa yazılır, en çok on iki kelime.

## Günlük (`gunluk/YYYY-AA-GG.md`)

Her günün kendi dosyası; sadece eklenir, satır silinmez ve değiştirilmez. İçine yazılanlar: o günün planı, akşamın beş sayısı, haftalık karar kaydı, takılmalar, aylık kâr hesabı, prova kayıtları, sahaya çıkış kontrol listesinin sonucu, kaybedilen müşteri ve sebebi, İş Beyni'nde değişen her değerin eski hali ve sebebi. Neyin ne zaman değiştiği buradan okunur; FounderOS gerektiğinde eski günleri yan yana koyar.

## Müşteri dosyası (`musteriler/<musteri-adi>.md`)

Her müşterinin bilgi dosyası, ayrı dosya. Para geldiği gün musteriyi-karsila açar; modüller "bilgi dosyasına yaz" dediğinde yazılan yer burasıdır. İçinde: adı, işletmesi, başlangıç tarihi, kademe, kurulum ve aylık ücret, kurulum döneminin günü, karşılama formunun cevapları, kurulum görüşmesinin notları, iletişim düzeni, eski müşteri listesinin yeri, alınan giriş izinleri, mesaj izni sonucu (eski müşteri listesinde izinli numara var mı), karekodun yeri, asistanın kuralları, 0850 numara ve hattın bağlandığı tarih (hat şifresi ve adresi hiçbir dosyaya yazılmaz), sesli ajanın ayarları, müşteri bölümünün aylık bedeli ve CRM bağlantısının iki bölüme yenilendiği tarih, haftalık kontrol sonuçları, kriz kayıtları, rapor günü raporunun üç sayısı, kapsam dışı kalan parçalar ve sade dille sebepleri (hat, sağlayıcı, izin, müşterinin adımı; kanun ya da kurum adı yazılmaz), sıradaki baş ağrısı (rapor günü görüşmesinde müşterinin kendi cümlesi), aktif mi, kim bağladı.
Yazan: musteriyi-karsila, musteri-sistemini-kur, yazili-asistani-kur, sesli-ajani-kur, kaybolanlari-geri-getir, yorum-topla, sistemi-kontrol-et, aylik-raporu-hazirla, musteriyi-elde-tut, zor-konusmayi-yonet, onay-belgesini-hazirla, kari-hesapla.

---

# Boş şablon

Yeni bir öğrencinin kaydını açarken bu şablonun birebir kopyasını yazarsın. Bölüm adlarını ve sırasını değiştirmezsin.

Bu dosyayı FounderOS yazar, öğrenci okur. Elle düzenlenmez.

Kurallar: Bu dosya güncel gerçektir. Her alanda tek değer durur; değişen değer yerinde güncellenir, eski değer ve değişme sebebi o günün günlüğüne (`gunluk/YYYY-AA-GG.md`) tek satır yazılır. Kayıt alanları (günlük sayılar, kararlar, takılmalar, kâr ve prova kayıtları) günlüğe yazılır; burada o alanda yalnız son değer ve koşan toplam durur. Nerede kalındığı (blok, oturuş, adım, sıradaki adım, Yol Haritası aşaması) burada değil, durum kaydında (`.founderos/durum.json`) durur. Her müşterinin bilgisi kendi dosyasındadır (`musteriler/<musteri-adi>.md`). Boş alan silinmez, yanına "henüz yok, [hangi adımda] dolacak" yazılır; boş alana tarih atılmaz. Kilitli satırın yanında hangi eşikte açılacağı yazar.

Bu şablon boş haliyle kopyalanır ve doldurulur. Bölüm adları ve sırası değişmez; modüller bu adlarla arar.

---

## 1. Kurucu

- Lisans anahtarı:
- Panel linki (telefondaki panel; lisans doğrulamasından gelir):
- Ad:
- Şehir:
- Telefon:
- E-posta:
- Çalışma düzeni (tam zamanlı / işin yanında):
- Günlük temas sayısı:
- Günlük temas dağılımı (ana kanal, diğer iki kanal, video; tam zamanlıda 50, 40, 10; işin yanında 20, 16, 4; teslim süresinde 30, 24, 6 ve 10, 8, 2; video ilk hafta 5 ve 2):
- Haftalık teslimat saati:
- Hazırlık seviyesi:
- Kanal yolu (telefon / yazı):
- Klasörün tam yolu:
- Başlangıç tarihi (birinci günün tarihi):
- Dayanma süresi (ay):
- Başlangıç değerlendirmesi (avantajlar, zorlanma noktaları, çalışma düzeni ve günlük sayı, pazar araştırmasının girdileri):
- Ne motive ediyor:
- Ne durduruyor:
- Daha önce ne denedi, neden bıraktı:
- Düşme riski nerede:
- Motivasyon satırı:
- Tanışma cevapları (sekiz zorunlu soru ve cevaplanan bekleyen sorular, her biri tek satır):

## 2. Hedef ve para

- Vizyon, bir yıl sonra hayat:
- Vizyon, bir yıl sonra iş:
- Çalışma sınırları (haftada saat, pencereler, tek başına kaç müşteri):
- Seçilen kombinasyon ve tempo:
- Zihniyet kabulü ve tarihi:
- Zihniyet kartlarının son açılış tarihi (kart başına):
- Hedef aylık gelir:
- Aylık zorunlu gider:
- Net maaş (maaşlı işi varsa):
- Bütçe merdiveni basamağı (alt / orta / üst) ve ertelenen kalemler:
- Özgürlük bölümü:
- Gelir planının basamakları:
- Müşteri değeri:
- Aylık masraf tablosu:
- Çıkış hesabı:
- Üç aylık yaşam gideri şartı (durum):
- Son aylık kâr (tarih; geçmişi günlükte):

## 3. Niş

- Seçilen niş:
- Seçim tarihi:
- Coğrafya:
- Doğrulama tablosu ve tarihi:
- Niş araştırması (tarih, dosya, önerilen başlangıç nişi, ilk üç, seçili nişle çelişen bulgu):
- İçeriden tanıdığı sektör:
- Telefonundaki işletme sahipleri (sektör, kaç kişi):
- Rakip notu:
- İkinci aday niş:
- Üçüncü aday niş:
- Sezon durumu:
- İdeal müşteri, tek cümle:
- Hedeflenen işletme büyüklüğü:
- Niş kilidi (doksan gün ya da beş müşteri, başlangıç tarihi):

## 4. Teklif ve fiyat

- Konumlandırma cümlesi (uzun, kısa, itiraz cevabı):
- Dönüşüm Cümlesi (beş parça):
- Sistemin adı:
- Mekanizma (adı ve adımları):
- Teklif sürümü ve tarihi:
- Bir dakikalık anlatım:
- Teklifin açıları (beş ile yedi; başlık ve iki üç cümle):
- Kademe 1 içeriği:
- Kademe 2 içeriği:
- Kademe 3 içeriği:
- Kullanılan formül (gelir / tasarruf) ve iki girdisi:
- Fiyat bandı (kurulum alt-üst, aylık alt-üst):
- Kurulum ücreti (nişin varsayılanı):
- Aylık ücret (kurulumun yüzde yirmisi):
- Fiyat sürümü ve tarihi:
- Karşılaştırma fiyatı:
- Deneme fiyatı ve üç karşılık:
- Güvence cümlesinin tam metni:
- Güvence sürümü (taslak / kesin, tarih):
- Güvencenin şartları:
- "Fiyat ne" sorusunun cevabı:
- En sık çıkan üç itiraz ve cevapları:
- Kaçan müşteri rakamı ve kurtarma tahmini:
- Önce/sonra tablosu (günü, kendini görüşü, duygusu, acısı ve hayali; sürüm ve tarih):
- Teklif notları (son on görüşme):
- KİLİT: teklifin kelimeleri on görüşmede açılır. Fiyatın rakamı otuz görüşmede açılır.

## 5. Teslimat

- Birinci gün teslimat uygunluk kontrolü (özellik, bağlantı, veri, bakım yükü, kritik kısıt; teklif dışında kalanlar, şartlı parçalar, tarih):
- Müşteriye gösterilecek beş satır:
- Saat tablosu (tahmindir):
- Kapasite bölmesi ve ölçülecek satırlar:
- Görüşmede söylenecek üç cümle:
- Müşteriden istenecekler listesi:
- Dört dosyanın adı ve durumu:

## 6. Marka ve varlıklar

- İş adı (aile, çağrışım kontrolünün tarihi):
- Seçilen alan adı, yedeği ve kontrol tarihi:
- Marka kitinin yeri:
- Renkler:
- Yazı tipleri:
- Logo ve en küçük boyutu:
- Görsel yön:
- Dosya haritası (dosya, ne için, nerede):
- Eksik gerçek bilgiler (bilgi, hangi dosyayı bekletiyor):
- Açılış görselinin kaynağı:
- Instagram kullanıcı adı ve hesap yaşı:
- Profil fotoğrafının yeri:
- WhatsApp Business numarası ve karşılama mesajı:
- E-posta imzası:
- YouTube kanal adresi:
- YouTube kanalı doğrulandı mı (video kapağı için), tarih:
- LinkedIn profil adresi ve güncellenme tarihi:
- Biyografi metni ve sürümü:
- Alan adı ve nereden alındığı:
- Canlı site adresi:
- Ön görüşme sayfasının adresi:
- Proje klasörünün yeri:
- Sayfanın metin sürümü ve tarihi:
- Müşteri gelince değişecek bölümler:
- Video adresleri (ön görüşme, üç itiraz, deneme, kanıt ekran kaydı):

## 7. Araçlar ve hesaplar

- Sesli örnek (kuruldu mu, tarih, kaydın yeri):
- Sesli demo (demo sayfasında açık mı, tarih):
- CRM bölümünün adresi:
- Bağlanan Google hesabı:
- Çalışma saatleri:
- Arama yapılacak numara:
- Sesli mesaj metni:
- Hatırlatmalar (panelden ya da yedek yol takvim alarmı, açıldığı tarih; kapalıyken hatırlatıldığı günler):
- Otomatik eşitleme (açıldı mı, tarih):
- Veri servisi: bu ay alınan kayıt / tavan, son çekim (tarih, kategori, şehir, iş kimliği), yedek yol kullanıldı mı:
- Sayım çekimleri (tarih, üç nişin iş kimlikleri, ilk nişten gelen kayıt sayısı):
- Yapay zeka aboneliğinin aylık tutarı:
- Tarayıcı demosunun adresi, dosyası, test tarihi ve demo kaydının yeri:
- Ödeme sağlayıcı ve link adresleri:
- Şirket (ilk "evet" günü açılır; müşavir, cevapları ve "şirket ve muhasebe gideri" satırı):
- Sözleşmenin sürümü ve doldurulma tarihi:
- CRM kurulumu (dokuz aşama, kayıt satırları, takip zinciri, numara birleşmesi):

## 8. Listeler

- Sıcak çevre: A listesi kişi sayısı, B listesi kişi sayısı, çıkarılma tarihi, taranan kaynaklar:
- Soğuk liste: çıkarılma tarihi, ham kayıt, elenen, kalan, sahibinin adı bulunan sayısı, kategori adı, kapsanan ilçeler:
- Havuzun yeri (soğuk havuz hep `adaylar.csv`; CRM açılınca yalnız sıcak kayıtlar oraya taşınır, taşınma tarihi):
- En çok istenen yüz işletme: seçim tarihi, kaç kişi, ölçütler:

## 9. Mesajlar ve kanıt

- Telefon metni, sürüm, tarih:
- E-posta metni, sürüm, tarih:
- Instagram metni, sürüm, tarih:
- Sıcak çevrenin iki mesajı ve mesajdaki sayı:
- Kanca listesi ve hangisinin cevap aldığı:
- Günlük gönderim sayısı ve e-posta alıştırma tarihi:
- Deneme aramasının sonuçları:
- Kanıt cümlesi ve güncellenme tarihi:
- Kanıt hikâyesi:
- Paylaşım izni yazılı mı:
- İçerik (başlangıç tarihi, çekim yolu yüz/ses, son hafta: tarih, tema, konu türü, beş parçadan kaçı yayında):
- İçerikten gelen ilgi (koşan toplam: yazan işletme, görüşmede içerikten söz eden):
- KİLİT: mesaj metni üç yüz temasta açılır, elli temastan önce hiç dokunulmaz.

## 10. Sayılar

Her günün sayıları günlüğe yazılır; burada son değer ve koşan toplam durur. Kilitler koşan toplamdan okunur.

- Gün sayacı:
- Dünün beş sayısı (sıcak ve soğuk ayrımıyla; geçmişi günlükte):
- Haftalık toplam (son hafta; geçmişi günlükte):
- Akşamın tek cümlesi (son akşam):
- Görüşme sayacı:
- Prova sayacı (prova / temiz prova):
- Aktif düzeltme (tek satır, temiz çıkana kadar):
- Koşan toplam (bugüne kadar temas, cevap, randevu, görüşme, müşteri):
- İtiraz sayacı:
- Fiyat itirazı sayacı:
- Evet ile ödeme arası süre:
- Eşikler ve nerede olunduğu (iki yüz temas, üç yüz temas ve karar günü, otuz randevu, otuz görüşme):

## 11. Kararlar

Son haftanın kararı burada durur; geçmiş kararlar günlükte.

- Son karar (haftanın tarihi, dört halkanın sayıları, en zayıf halka ve sebebi, değişikliğin numarası, ne değiştirildi, geçen haftanın kararının sonucu):

Tek değişken kuralı: aynı hafta iki değişiklik yazılmışsa o testin verisi geçersizdir; o haftanın günlüklerinden bakılır.

## 12. Müşteriler

Burada yalnız aktif müşterilerin listesi durur. Her müşterinin bilgisi kendi dosyasındadır (`musteriler/<musteri-adi>.md`); dosyanın alanları İş Beyni şemasında. Müşteri ayrılınca satır listeden çıkar, sebebi günlüğe yazılır.

- Aktif müşteri sayısı:
- İlk müşteri tarihi:
- Müşteri başına haftalık saat:
- Aktif müşteriler (ad, dosya `musteriler/<ad>.md`, teslimat günü, aylık ücret):

## 13. Açık işler

- Sonraki adım (tek cümle, her akşam yeniden):
- Bekleyen soru, hangi güne ya da eşiğe bağlı:
- Ertelenen istek, hangi eşikte açılacak:
- Ertesi güne kalan iş:
- Üç kez ertelenen iş ve sebebi (büyük, belirsiz, bilgi eksik):
- Sürüm uyarısı (sürüm, söylendiği günler):

## 14. Aşama ve tamamlanma

Beş ilerleme aşaması ve ölçütleri. Nerede kalındığı durum kaydında.

- 1. Hazırlık tamamlandı: (ölçütler tamam/eksik, tarih)
- 2. İlk işletmeyle görüştün: (ölçütler tamam/eksik, tarih)
- 3. İlk satışını yaptın: (ölçütler tamam/eksik, tarih)
- 4. Hizmeti teslim ettin: (ölçütler tamam/eksik, tarih)
- 5. Müşterin kullanıyor: (ölçütler tamam/eksik, tarih)

## 15. Bugünün listesi

CRM açılana kadar günün özeti burada durur: randevular, cevap verenler, takipler. Soğuk havuz buraya yazılmaz, aday listesinde (`adaylar.csv`) durur. CRM açılınca yalnız sıcak kayıtlar (cevap veren, randevu, müşteri) bir kere oraya taşınır ve bölüm "CRM'e taşındı, tarih" satırıyla kapanır.

- Dün ne oldu:
- Bugünün randevuları (kim, ne zaman, hangi kanaldan geldi):
- Cevap verenler ve sıradaki hareket:
- Cevap bekleyenler:
- Takip günü gelenler:

## 16. Taslaklar

- (ne, hazırlanma tarihi, neyi bekliyor / kullanıldı tarihi)

## 17. Takılmalar ve destek

Son takılma burada durur; geçmişi günlükte.

- Son takılma (tarih, cümle, tür: bilgi/erişim/teknik/uygulama, denenen, çözüldü mü, destek özeti, gelen cevap):
- Bilinen çözümler (takılınan yer, işe yarayan çözüm; aynı yerde yeniden takılınca önce buraya bakılır):

## 18. İdeal müşteri

Sürüm: (masabaşı / saha) · Tarih: · Hedeflenen işletme büyüklüğü:

Her satırın sonuna kaynağı ve işareti yazılır: (kaynak, bulgu) ya da (yorum).

- 1. Tek cümlelik tanım:
- 2. Günü nasıl geçiyor:
- 3. Üç derdi, kendi cümleleriyle:
- 4. Üç korkusu (satıcıya, teknolojiye, para kaybetmeye):
- 5. Satın alma tetikleyicisi:
- 6. Karar biçimi:
- 7. Nereden bilgi alıyor:
- 8. Daha önce ne denedi ve neden bıraktı:
- 9. İtiraz olmayan itirazlar:
- 10. Müşterinin müşterisi:
- 11. Ne satın almaz (eleme listesi, en az beş madde):
- 12. FounderOS'un yorumu (en fazla beş cümle, her biri "yorum" ile başlar):

Saha sürümü: (onuncu görüşmeden sonra yazılır, masabaşı sürümü silinmez)
