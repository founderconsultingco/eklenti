---
user-invocable: false
name: panel-vitrini
description: "Paneldeki Ajansım (Pazar Radarı ve Teklif stüdyosu dahil), Adaylar, Mesajlar, İçerik ve Teslimat bölümlerinin kaynakları, ajans.json, mesajlar.json ve teslimat.json şeması ve gönderme komutu (aday aracının panel komutu). Bir modül teklif, fiyat, teklif hesabı, ideal müşteri, pazar ya da canlı sayım, marka, sayfa, mesaj metinleri ya da içerik çıktısını değiştirdiğinde, sabah kapat'tan sonra, akşam kapanışında ve öğrenci 'paneli güncelle', 'panelim boş' dediğinde açılır."
---

# Panel vitrini: Ajansım, Adaylar, Mesajlar, İçerik, Teslimat

Öğrencinin panelinde (founderos.so/panel) Bugün, Ekip ve Yol'un yanında dört bölüm daha var: **Ajansım** (logo ve marka kiti, site, değer bölgesi, dönüşüm cümlesi, mekanizma, teklif ve paketler, teslime hazır üç ajan, çalışan demo ve deneme aramaları, teklifin açıları, fark, ideal müşteri, Pazar Radarı: pazar araştırması ve canlı sayım; Niş ve Teklif Bankası), **Adaylar** (Müşteri Bulma Motoru'nun canlı taraması, Tek Tıkla Demo ve son demolar, Aday panosu, harita taramaları, en çok istenen yüz işletme ve her birine özel mesajlar, aşamalar, işletmelerde görülen açıklar, semtler, kanallar), **Mesajlar** (Truva mesaj stüdyosu, günün dağılımı, açılış cümleleri, telefon konuşması, ilk mesajlar, takipler, video senaryoları, Görüşme modu, itirazlar) ve **İçerik** (haftanın içeriği). İlk müşteri gelince **Teslimat** da dolar: Bugün'de teslimi süren müşterinin kartı, Yol'da Tek Kişilik Teslimat Motoru. Öğrenci işini oradan görür ve metinleri oradan kopyalar. Aday panosu ve Truva stüdyosu ayrı yazılmaz: en çok istenen yüzün `asama`, `bulgu`, `kanca` ve mesaj alanlarından çizilir; demoların sayıları sunucudadır. Teklif stüdyosu (kayıp hesabı, teklifin önizlemesi, kâr hesabı) `ajans.json`'daki `teklif.hesap`, `fiyat` ve kademelerden çizilir. Panelin o an hangi ekranı açtığını ve "Şu an" kartını bu dosyalar değil veri servisinin `odak_yaz` aracı söyler (çekirdek, "Panel: odak ve tur"). Panel boşsa öğrenci yaptığı işi göremez; bu bölümleri güncel tutmak kaydın parçasıdır.

## Kaynaklar

| Bölüm | Nereden gelir | Kim yazar |
|---|---|---|
| ajans | `.founderos/panel/ajans.json` artı marka kitinin `window.MARKA` bloğu artı sayfanın `window.SITE` bloğu | sen (aşağıdaki şema); marka ve sayfa bloğunu araç kendisi okur |
| adaylar | `adaylar.csv` | araç hesaplar; sen yazmazsın |
| mesajlar | `.founderos/panel/mesajlar.json` | sen (aşağıdaki şema) |
| icerik | `.founderos/panel/icerik.json` | icerik-motoru (şeması o modülde) |
| teslimat | `.founderos/panel/teslimat.json` | sen (aşağıdaki şema); ilk müşteriden itibaren |

Logo, renk kodları, yazı tipi, `biz` ve `degil` satırları marka kitinden gelir; sitenin başlığı ve açıklaması sayfadan; demonun adresi `site/demo.html`'den ve sayfanın yayındaki adresinden (araç `demo.adres`'i kendisi koyar). Niş ve Teklif Bankası panelin kendisindedir, yazılmaz: on dokuz kart, öğrencinin nişi `pazar.secilen`'den, karşılaştırdıkları `pazar.adaylar`'dan işaretlenir. `ajans.json`'a bunları yazmazsın, iki yerde durup birbirini tutmaz hale gelir. Adaylar bölümü listenin kendisinden çıkar: en çok istenen yüzün bulgusu, açılış cümlesi, Instagram mesajı, e-postası ve video senaryosu adayın satırındaki `bulgu`, `kanca`, `dm_metni`, `eposta_konu`, `eposta_metni`, `video_metni` sütunlarından okunur. Metni satıra yazdıysan panelde de vardır. Adaylar'ın başındaki İlk Müşteri Motoru da listeden hesaplanır: kaynak başına sayı (`kaynak` sütunu: Haritalar, reklam kütüphanesi, iş ilanı, tanıdık, referans), reklam veren ve ilan veren işletmeler, ulaşılan işletme sayısı. İlan veren işareti iş ilanından eklenen satırdan ya da `isaret --isaret is_ilani` ile yazılan işaretten gelir; haftalık iş ilanı araması yapılmazsa panelde "İş ilanları 0" görünür.

## Gönderme

Dosyayı yazdıktan ya da listeyi değiştirdikten sonra öğrencinin klasörünün içinde sessizce:

```
python3 .founderos/adaylar-arac.py panel --yukle
```

Araç beş bölümü kurar, sunucunun kurallarıyla denetler ve yalnız değişen bölümü gönderir. Öğrenciye bir şey söylemezsin, komutu sohbete yazmazsın. Çıktının her satırı bir bölüm: `hazır`, `yok` ya da `GİTMEDİ: <alanın yolu>: <sebep>`. `GİTMEDİ` görürsen o dosyayı düzeltir, komutu bir kez daha çalıştırırsın; öğrenciye söylemezsin. `panel yüklenmedi` servise ulaşılamadı demektir: sessizce geçersin, bir sonraki gönderimde gider. Son satır `panel yüklendi: ...` ya da `panel: değişiklik yok`. Gönderimden sonra odak gider: iş bittiyse `bitti` (panel yeni veriyi o anda okur), sürüyorsa `calisiyor`.

Araç sayı alanlarını sunucunun beklediği biçime getirir: `"18.000 TL"` 18000, `"%43"` 43, yazıyla yazılmış iş kimliği sayı olur; okunamayan sayı, aralık dışı oran ya da bilinmeyen karar gönderilmez. `kayip_dayanak`'ı olmayan `aylik_kayip` gönderilmez. Ajansın adı henüz yoksa (birinci günün ilk iki oturuşu) pazar, ideal müşteri, konumlandırma, teklif ya da fiyat varsa bölüm yine gider.

Araç klasörde yoksa (aday listesi henüz çıkmadıysa, birinci gün) önce `founderos:aday-listesi-araci`nın kurulum adımlarıyla `.founderos/` içine kurarsın; `adaylar.csv` olmadan da çalışır, o zaman adaylar bölümü `yok` der. `panel` komutunu tanımıyorsa araç eskidir: aynı beceriyle güncellersin.

## Ne zaman

- Her modülün sonunda, modül bu dört bölümden birine düşen bir şeyi değiştirdiyse: önce dosya, sonra komut, sonra odak.
- Sayım çekimi başlar başlamaz ve özeti gelince (Pazar Radarı): pazar satırları, komut, odak; modülün sonunu beklemez.
- Sabah günaydında `kapat`tan sonra ve akşam kapanışında `ozet`ten sonra: aday listesi her gün değiştiği için adaylar bölümü tazelenir.
- Öğrenci "paneli güncelle", "panelim boş", "panelde teklifim görünmüyor" derse: eksik dosyayı İş Beyni'nden ve klasördeki dosyalardan yazar, komutu çalıştırır, tek cümle söylersin: "Panelin güncel; Ajansım, Adaylar ve Mesajlar bölümlerine bak." Ardından odak `bitti` gider; `is` doldurduğun bölümün modülüdür ki panel o bölümü açsın: teklif ya da fiyat için `teklifi-yaz`, marka için `markani-kur`, pazar için `nisi-sec`, aday listesi için `aday-listesi-dosyasi`, mesajlar için `adaya-mesaj-yaz`, içerik için `icerik-motoru`, teslimat için `musteri`. Birden çok bölüm doldurduysan öğrencinin sorduğu bölüm; hiçbirini sormadıysa odak gönderilmez, panel dakikada bir kendisi tazelenir. `is` olarak `panel-vitrini` yazılmaz: panelde bu adla bir ekran yok.

Hangi modül hangi alanı yazar:

| Modül | Dosya | Alan |
|---|---|---|
| isini-kur, markani-kur | ajans.json | `ad`, `sehir`, `nis`, `alan_adi` |
| nisi-sec | ajans.json | `nis`, `pazar.secilen`, `pazar.neden`, `pazar.sehir`, `pazar.adaylar` (sayım başlar başlamaz `is_id`, `karar`, `neden`, karttan `musteri_degeri`, `sezon`, `tr_sayisi`, `problem`, `sorular`, `kaynaklar`) |
| nisi-dogrula (sayım sonucunu FounderOS yazar) | ajans.json | `pazar.adaylar`'ın ölçüleri, `puan`, `karar`, varsa `aylik_kayip` ve `kayip_dayanak` |
| nis-arastirmasi | ajans.json | `pazar.rapor`; niş seçilmediyse ilk üçün `pazar.adaylar` satırları (`is_id`, ölçüler, raporun ikinci bölümünden `problem`, `sorular` ve kanıt notundan `kaynaklar`; karar yok) |
| ideal-musteriyi-cikar | ajans.json | `icp` |
| konumlandir | ajans.json | `konum` |
| teklifi-yaz | ajans.json | `donusum`, `sistem_adi`, `mekanizma`, `teklif.bir_dakika`, `teklif.kademeler`, `teklif.guvence`, `teklif.acilar`, `deger_bolgesi`, `ajanlar` |
| fiyati-belirle | ajans.json | `fiyat`, `teklif.kademeler[].kurulum` ve `aylik`, `teklif.itirazlar`, `teklif.hesap` |
| kari-hesapla | ajans.json | `teklif.hesap.arac_maliyeti`, `teklif.hesap.sabit_maliyet` |
| siteni-kur | ajans.json | `site.durum`, `site.adres` (yayına alınınca `yayinda` ve adresi) |
| kanitini-hazirla | ajans.json | `demo.durum`, `demo.tarih`, `demo.kanit`, `demo.testler` (adresi araç koyar) |
| araclari-kur | ajans.json | `demo.sesli` (konuşma düğmesi demo sayfasında denenince `true`) |
| siteni-kur | ajans.json | `demo.vekil` (`siten.com/d/ornek` örnek demoyu açınca `true`) |
| adaya-mesaj-yaz | mesajlar.json | `karisim`, `telefon`, `ilk_mesaj`, `takipler`, `itirazlar`, `kancalar` |
| video-mesaj-cek | mesajlar.json | `video` |
| icerik-motoru | icerik.json | kendi şeması |
| musteriyi-karsila | teslimat.json | müşterinin satırı: `ad`, `baslangic`, `rapor_gunu`, `evre`, `bilgiler`, `siradaki` |
| musteri-sistemini-kur | teslimat.json | `evre`, `testler`, `kontrol`, `kapsam_disi`, `siradaki` |
| sistemi-kontrol-et | teslimat.json | teslim bitince `evre: calisiyor` |

## Genel kurallar

Yalnız düz JSON. Anahtarlar bu sayfadaki adlarla birebir: küçük harf, Türkçe harfsiz, alt çizgi. Değerler Türkçe ve öğrencinin gerçek kaydından: İş Beyni, klasördeki dosyalar, günlük. Uydurma yok, yer tutucu yok ("...", "örnek", "buraya yazılacak"). Bilmediğin alanı yazmazsın; boş alanın bölümü panelde görünmez, bu doğru davranıştır. Sayılar sayı (`18000`, `"18.000 TL"` değil), tarih `YYYY-AA-GG`, oranlar yüzde tam sayı (`43`). Metinlerde uzun tire yok. Lisans anahtarı, CRM şifresi, öğrencinin ya da bir işletme sahibinin kişisel bilgisi (telefon, e-posta, kimlik) bu dosyalara girmez. Bir metin 4000 karakteri, bir liste 160 öğeyi geçmez; ajans 96 KB, mesajlar 128 KB, teslimat 48 KB. Dosya her yazılışta tam hâliyle yazılır (araç eski hâli birleştirmez); değişmeyen alanları da korursun: önce dosyayı okur, değişen alanı değiştirir, bütününü yazarsın.

## `ajans.json`

```json
{
 "surum": 1,
 "ad": "Serin Dönüş",
 "sehir": "Bursa",
 "nis": "Klima ve kombi servisi",
 "alan_adi": "serindonus.com",
 "site": {"adres": "https://serindonus.com", "durum": "yayinda"},
 "konum": {"kisa": "telefonda söylenen kısa hali", "uzun": "uzun hali"},
 "donusum": "İş Beyni'nin dördüncü bölümündeki Dönüşüm Cümlesi, birebir",
 "sistem_adi": "Sezon Çağrı Sistemi",
 "mekanizma": {"ad": "Yakala, yaz, hatırlat", "adimlar": [{"baslik": "Yakala", "metin": "..."}]},
 "teklif": {
  "bir_dakika": "teklifin bir dakikalık anlatımı",
  "kademeler": [{"ad": "Temel Kapsam", "icerik": ["madde", "madde"], "kurulum": 40000, "aylik": 10000}],
  "guvence": "müşteriye verilen güvence cümlesi",
  "acilar": [{"baslik": "açının adı", "metin": "iki üç cümle"}],
  "itirazlar": [{"soru": "itirazın kendisi", "cevap": "cevap"}],
  "hesap": {"kacan_aylik": 40, "musteri_orani": 25, "musteri_degeri": 17500, "arac_maliyeti": 1800, "sabit_maliyet": 17500, "not": "Kaçan talep ve oran kartın tahmini; müşteri değeri kartın aralığının ortası."}
 },
 "fiyat": {"bant": "Kurulum 40.000 ile 60.000 TL arası, aylık 10.000 ile 15.000 TL", "kurulum": 40000, "aylik": 12500},
 "deger_bolgesi": {"pazar": "Bursa'da iki ila beş teknisyenli klima ve kombi servisleri", "problem": "Sezonda usta sahadayken açılmayan telefon; müşteri bir sonraki servisi arıyor.", "sonuc": "Kaçan arama servis randevusuna dönüyor; ay sonunda kaç randevu geldiği belli."},
 "ajanlar": [
  {"kod": "hizli_donus", "ne": "bu nişte ne yaptığı, iki cümle", "ornek": "müşteriye giden tek mesaj"},
  {"kod": "randevu", "ne": "...", "ornek": "..."},
  {"kod": "eski_musteri", "ne": "...", "ornek": "..."}
 ],
 "demo": {
  "durum": "tamam", "tarih": "2026-09-08", "sesli": true,
  "kanit": "Geçen hafta Bursa'da otuz klima servisini akşam yedide aradım, yirmi ikisi açmadı.",
  "testler": {"arama": {"yapilan": 30, "acmayan": 22}, "yazili": {"yapilan": 20, "donmeyen": 13, "en_hizli_dk": 70}, "form": {"yapilan": 10, "donmeyen": 7, "en_hizli_dk": 240}}
 },
 "icp": {"tek_cumle": "...", "buyukluk": "...", "basliklar": [{"ad": "Günü nasıl geçiyor", "metin": "..."}]},
 "pazar": {
  "secilen": "Klima ve kombi servisi",
  "neden": "seçimin gerekçesi, iki üç cümle",
  "sehir": "Bursa",
  "adaylar": [
   {"nis": "Klima ve kombi servisi", "is_id": 48213, "sehir_sayisi": 486, "tr_sayisi": 3553, "reklam_orani": 11, "telefon_orani": 91, "site_yok_orani": 38, "aksam_orani": 64, "sikayet_orani": 12, "musteri_degeri": 17500, "sezon": "Klima mayıs ağustos, kombi ekim ocak yoğun; ekim kombi sezonunun başı.", "puan": 80, "karar": "secildi", "neden": "Telefon dolu, reklam veren var, sezon açılıyor.", "not": "tek cümle",
    "problem": "Sezonda usta sahadayken telefon açılmıyor; arayan müşteri listedeki bir sonraki servisi arıyor.",
    "sorular": ["Geçen sezon bakım yaptırdığınız müşterileri bu sezon siz mi arıyorsunuz, onlar mı sizi arıyor?", "Yazın en yoğun haftada siz sahadayken telefon çalınca ne oluyor, müşteri tekrar mı arıyor, WhatsApp'tan mı yazıyor?", "Ayda kaç arama, mesaj ya da form geliyor, kaçına aynı gün dönemiyorsunuz?"],
    "kaynaklar": [{"ad": "Haziranda klima şikâyetleri", "adres": "https://www.sonhaberler.com/klima-servisi-alanlarin-sikayetleri-haziranda-yuzde-320-artarak-1248e-yukseldi-haber-912503"}]},
   {"nis": "Oto servis ve cam filmi", "is_id": 48214, "karar": "yedek", "neden": "İkinci aday: telefonla ulaşılıyor, sezonu yıl boyu.", "problem": "...", "sorular": ["...", "...", "..."]}
  ],
  "rapor": {"tarih": "2026-09-07", "ilk_uc": [{"nis": "...", "neden": "..."}], "oneri": "raporun önerisi, tek cümle"}
 },
 "guncellendi": "2026-09-09T15:20:00+03:00"
}
```

- `site.durum`: `taslak` ya da `yayinda`. Yayında değilse `adres` yazılmaz.
- `mekanizma.adimlar`: teklifin mekanizmasının üç ya da dört adımı, sistemin adıyla aynı dil.
- `teklif.kademeler`: kademeler üçüncü gün kesinleşir; o güne kadar yalnız gövde (`bir_dakika`, `guvence`, `acilar`). Kesin fiyat yoksa `kurulum` ve `aylik` yazılmaz. Önerilen kademe, fiyatı `fiyat.kurulum` ve `fiyat.aylik` ile aynı olandır; panel onu işaretler.
- `teklif.acilar`: teklifin farklı kapıları. Aynı teklif, işletmeye başka yerden giren beş ile yedi açı: sezonun en yoğun haftası, eski müşteri listesi, numaraya dokunulmaması, fiyat vermeyen asistan gibi. Her açı teklifin kendisinden ve kartın kanıtından; yeni vaat yok, rakam varsa kaynağıyla. Mesajda, videoda ve görüşmede işletmeye en uyan açı seçilir.
- `icp.basliklar`: ideal müşteri sayfasının on iki başlığı, sayfadaki adlarla ve sırayla.
- `pazar.sehir`: sayımın yapıldığı şehir.
- `pazar.adaylar`: karşılaştırılan nişler, en çok dört. Niş adı kartın adıyla yazılırsa panel onu Niş ve Teklif Bankası'nda da işaretler. Bilinmeyen değer yazılmaz; panel eksik ölçüyü boş bırakır.
  - `is_id`: o nişin sayım çekiminin iş kimliği (sayı). Sayım başlar başlamaz yazılır ve gönderilir; panel bu kimlikle sayımı sunucudan canlı gösterir (Pazar Radarı: çekim sürerken tarama, bitince ölçüler).
  - Ölçüler sayımın özetinden, yüzde ve tam sayıya yuvarlanarak: `sehir_sayisi` = `kalan`; `telefon_orani` = `telefonlu` / (`kalan` + `isaretli.iletisim_yok`) (sayımda telefonu olmayan işletme iletişimsiz diye işaretlenir, paydaya girer); `reklam_orani` = `reklamli` / `kalan` (`reklamli` boşsa yazılmaz); `site_yok_orani` ve `sikayet_orani` = özetin `ipuclari` içindeki `site_yok` ve `yorum_sikayet` sayısı / `kalan`; `aksam_orani` = özetin `kapali_saat.oran` alanı (saati bilinen işletmelerden akşam erken, pazar ya da hafta sonu kapalı olanların yüzdesi; Pazar Radarı'nın kendi sayımıyla aynı kural, sohbette de bu yüzde söylenir); alan `null` ise yazılmaz, sıfır sayılmaz. Eski sunucu bu alanı vermiyorsa `aksam_kapali` / (`kalan` eksi `saat_yok`), saati bilinen işletme `kalan`ın beşte birinden azsa yazılmaz; `ort_puan` özet veriyorsa (0-5, bir ondalık). Sayım beş yüz kayıtta durduysa (özetteki `toplam` 500) `sinirda: true`; panel sayının yanına "+" koyar (şehirde daha fazlası olabilir). `tr_sayisi` kartın Türkiye sayısıdır, canlı sayılmaz.
  - `musteri_degeri`: bir müşterinin işletmeye değeri, TL: kartın kayıp birimi satırındaki aralığın ortası (ilk iş ve yıl içindeki tekrar; fiyati-belirle'deki gibi). Kartta lira karşılığı yoksa yazılmaz. Eski `is_degeri` (bir işin ya da çağrının tutarı) yazılmaz; panel okumaz.
  - `aylik_kayip` ve `kayip_dayanak`: şehirde kapalı saatte bir ayda kaçan talebin para karşılığı (TL, tahmin) ve hesabın kendisi, tek cümle. Hesap: akşam ya da pazar kapalı işletme sayısı (`sehir_sayisi` × `aksam_orani`) × işletme başına kapalı saatte ayda kaçan talep × müşteri olma oranı × `musteri_degeri`. İşletme başına kapalı saatte kaçan talep: en az üç görüşmede işletmecilerin verdiği sayıların ortancası, yoksa kartın kaçan talep satırının yüzde on beşi (akşam ve pazar gelen talebin temkinli payı, aşağı yuvarlanır); müşteri olma oranı kartın kaçan talep satırından. `aksam_orani` ya da `musteri_degeri` yoksa hesap yapılmaz. İşletme başına aylık kayıp kartın kapasitesinden çıkan aylık cironun yüzde otuzunu geçmez (fiyati-belirle'nin tavanı). `kayip_dayanak` rakamların nereden geldiğini söyler: "311 servis akşam ya da pazar kapalı (yukarıdaki örnekte 486 servisin yüzde 64'ü). Kapalı saatte her biri ayda 6 talep kaçırsa 1.866 talep eder; dördünden biri müşteri olurdu, müşteri başı 17.500 TL." (aylik_kayip 8.163.750) Dayanak yoksa ikisi de yazılmaz.
  - `sezon`: kartın sezon satırının kısa hali, tek cümle: yoğun aylar ve bu ay.
  - `puan`: nişin beş sorudan puanı (nisi-dogrula'nın tablosu), 0-100: her soru 20 puan; geçti 20, "ölçülemedi", "görülemedi" ya da "bu sektörde ölçü değil" 10, geçmedi 0. Şehir sorusunda sayım beş yüzde durduysa (özetteki `toplam` 500) eşik bu sayımla ölçülemez: 10. Puan tablodan hesaplanır; tablo yoksa yazılmaz.
  - `karar`: `secildi` (`pazar.secilen` ile aynı niş, tek), `yedek` (doğrulamaya giden iki yedek) ya da `elendi` (beş sorudan üçünü geçemeyen ya da öğrencinin reddettiği). Niş araştırması karar yazmaz; kararı nisi-sec verir. `neden`: kararın sebebi, tek cümle, öğrenciye yazılmış; kanun, kurum, madde yok.
  - `not`: nişin tek cümlelik notu.
  - `problem`, `sorular`, `kaynaklar`: Pazar Radarı'nın Karşılaştırma tablosu (satış videosundaki "her sektör için tek problem ve işletme sahibine soracağın üç soru, kısa tablo"). Tablonun sütunları nişler, satırları dört ölçüt (değer ve geçti ya da zayıf; sayım mı tahmin mi), problem, üç soru ve kaynak; dört ölçütü panel karneyle aynı eşiklerden kendisi kurar, sen yalnız bu üç alanı yazarsın. `problem`: bu nişte çözülecek tek problem, tek cümle, işletmecinin diliyle (en fazla 240 karakter): kartın "Sızıntı nerede" bölümündeki en güçlü sızıntı; niş araştırmasından geliyorsa raporun ikinci bölümündeki "hangi somut problem araştırılır" cümlesi. Seçilen nişte Dönüşüm Cümlesi'nin problemiyle (`deger_bolgesi.problem`) aynı acıyı söyler. `sorular`: işletme sahibine sorulacak üç soru, birebir telefonda söylenecek cümleler (her biri en fazla 240 karakter): kartın "Telefonda söylenecekler" bölümündeki açılış sorusu ve işleyiş sorusu, üçüncüsü kaybı rakama çeviren soru: "Ayda kaç arama, mesaj ya da form geliyor, kaçına aynı gün dönemiyorsunuz?" Niş araştırmasından geliyorsa raporun beş sorusundan ilk üçü. Sorular işletmecinin kendi deneyimini sorar, çözümü satmaz. `kaynaklar`: problemin dayanağı, en çok dört: `{"ad": "kısa ad", "adres": "https://...", "tarih": "YYYY-AA-GG"}`; adres kartın Kaynaklar listesinden ya da raporun kanıt notundan, açılan bağlantı, yalnız https; tarih yayın ya da erişim günü. Kaynağı olmayan problem yazılmaz. Gelmezse panel problemi ve soruları nişin kartından kurar, kaynak satırına "Niş kartı" yazar. Sunucu uzun metni kısaltır, fazla soruyu ve https olmayan adresi atar.
  - Canlı sayımı panelde olan nişte (`is_id`) oranları ve kaybı panel sayımın kendi kayıtlarından kurar; kapalı saat orada akşam erken, pazar ya da hafta sonu kapalı olanların toplamıdır. Senin yazdığın `aylik_kayip` yalnız `sehir_sayisi` ve `aksam_orani` panelin sayımıyla aynıysa görünür; değilse panel aynı formülü kendi sayımıyla kurar. Böylece kart, karne, tablo ve kayıp aynı rakamı söyler.
- `teklif.hesap`: panelin Teklif stüdyosunun sayıları. Panel bunlarla kayıp hesabını (ayda kaçan talep × yüzde kaçı müşteri olur × müşteri değeri; aylık ücretin bu kaybın yüzde kaçı olduğu ve kaç müşterinin ücreti çıkardığı), teklifin önizlemesini (yazılı teklifte kademelerle; görüşmede tam ekran açılan önizlemede yalnız önerilen paket ve tek rakam) ve kâr hesabını (aylık ücret, araç maliyeti, sabit gider) çizer. Her sayı öğrencinin kaydından; bilinmeyen alan yazılmaz.
  - `musteri_degeri`: bir müşterinin işletmeye yıl içinde bıraktığı para, TL: kartın kayıp birimi satırındaki aralığın ortası; en az üç görüşmeden sonra işletmecilerin verdiği sayıların ortancası.
  - `kacan_aylik` (ayda dönülemeyen talep: arama, mesaj, form) ve `musteri_orani` (bunların yüzde kaçı müşteri olurdu): kartın kaçan talep satırından; en az üç görüşmeden sonra işletmecilerin verdiği sayıların ortancası. Eski alanlar (`kacan_haftalik`, `donus_orani`, `is_degeri`) yazılmaz; panel eski kaydın ilk ikisini aya çevirip okur, `is_degeri`'ni okumaz.
  - `arac_maliyeti`: müşteri başı aylık araç maliyeti, TL: müşteri bölümünün aylık bedeli (ekip yazılı söylediğinde) artı ölçülen kullanım giderleri; ilk müşteriden önce bilinmez.
  - `sabit_maliyet`: aylık sabit gider, TL: İş Beyni'ndeki masraf tablosunun aylık kalemleri (dolar kalemleri tablodaki TL karşılığıyla), şirket ve muhasebe gideri tek satır olarak dahil, aralıksa üst ucu; ilk kâr hesabından sonra o ayın gerçek rakamı.
  - `not`: sayıların nereden geldiği, tek cümle; vergi, prim gibi ayrıntı yazılmaz.
- `deger_bolgesi`: Dönüşüm Cümlesi'nin üç parçası, her biri tek cümle: `pazar` (kime), `problem` (para ödeyeceği acı), `sonuc` (ölçülen kazanım). Rakam yazılmaz; panel işletme sayısını, kayıp birimini ve fiyatı kayıttan koyar. `problem` yoksa panel bu kartı göstermez.
- `ajanlar`: üç ajan, sırası ve adları panelde sabit; `kod` yalnız `hizli_donus`, `randevu`, `eski_musteri`. `ne` bu nişte ne yaptığı (iki cümle, kartın bilgileriyle), `ornek` müşteriye giden tek mesaj (fiyat yok, tıbbi bilgi yok, yer tutucu yok). Yazılmazsa panel ajanın genel işini gösterir.
- `demo`: `vekil` `true` yalnız sitenin `/d/` yolu founderos.so'ya aktarılıyorsa (`_redirects` satırı yayında ve `siten.com/d/ornek` örnek demoyu açıyorsa); o zaman adaya özel demo bağlantıları öğrencinin alan adıyla çıkar. `durum` `kuruluyor` ya da `tamam` (beş senaryo temiz), `tarih` tamam günü. `testler` kanıt cümlesiyle aynı sayım: `arama` (yapilan, acmayan), `yazili` ve `form` (yapilan, donmeyen, en_hizli_dk). Olumsuz sayı yapılandan büyük olamaz; yapılmayan test yazılmaz. On denemeden az olan kanal panelde listelenir ama karşılaştırmaya girmez. `adres` araç tarafından konur; elle yazılırsa https olmalı.

## `mesajlar.json`

```json
{
 "surum": 1,
 "karisim": {"ana_kanal": "telefon", "ana": 50, "yazili": 40, "video": 10},
 "telefon": {
  "acilis": "ilk cümle",
  "adimlar": [{"baslik": "Tanış ve kaynağı söyle", "metin": "söylenen cümle"}],
  "bekci": "telefonu başkası açarsa ne denir",
  "ikinci_arama": "ikinci aramanın açılışı"
 },
 "ilk_mesaj": [
  {"kanal": "instagram", "baslik": "Mesaj isteği", "metin": "...", "not": "kanalın kuralı, tek cümle"},
  {"kanal": "eposta", "baslik": "e-postanın konusu", "metin": "...", "not": "..."}
 ],
 "takipler": [{"gun": 3, "kanal": "eposta", "metin": "..."}],
 "video": {"ilk_temas": "altmış saniyelik senaryo, saniyeleriyle satır satır", "izin_sonrasi": "izinden sonraki demo videosunun senaryosu"},
 "itirazlar": [{"soru": "...", "cevap": "..."}],
 "kancalar": ["gözlemle açılan açılış cümlesi", "..."],
 "guncellendi": "2026-09-12T07:45:00+03:00"
}
```

- `karisim`: günün temas dağılımı, İş Beyni'nin birinci bölümündeki dağılım satırıyla aynı. Ana kanal telefonsa `ana` arama sayısı, `yazili` iki yazılı kanalın toplamı. Yazılmazsa panel günün hedefinden yüzde 50, 40, 10 hesaplar ve ana kanalı telefon sayar.
- Metinler kalıptır: işletmenin adı ve gözlemi yerine `[Ad]` ya da `[işletme]` durur. İşletmeye özel hâli adayın satırında (`dm_metni`, `eposta_metni`, `video_metni`), buraya yazılmaz.
- `telefon.adimlar`: telefon metninin adımları sırasıyla; her adımda söylenen cümle birebir. Gözlem yoksa ne denir, o adımın metnine girer.
- `video.ilk_temas` ve `video.izin_sonrasi`: satır başında saniye aralığı (`0-8 sn: ...`) ya da parça numarası (`1. Kim olduğun, 30 sn: ...`); panel satırları böyle ayırır.
- `kancalar`: Truva Atı açılışları, işletmede görülen somut aksaklıkla açılan tek cümleler. Niş kartından ve denetimde en sık çıkan bulgulardan, en çok sekiz.
- `itirazlar`: sahada duyulan itirazlar ve cevapları. Teklifin görüşmedeki itirazları `ajans.json`'da; panel ikisini tek listede gösterir, aynı soru bir kez görünür.

## `teslimat.json`

```json
{
 "surum": 1,
 "musteriler": [
  {
   "ad": "Karaca Klima",
   "baslangic": "2026-09-21",
   "rapor_gunu": "2026-10-12",
   "aylik": 10000,
   "evre": "ikinci_dalga",
   "bilgiler": {"gelen": 11, "toplam": 11},
   "testler": {"birinci": {"gecen": 32, "toplam": 32}, "ikinci": {"gecen": 6, "toplam": 14}},
   "kontrol": {"test": false, "onay": true, "musteri_gordu": true, "kapsam_disi": false, "bakim": false},
   "kapsam_disi": ["Sesli taraf: hat bekleniyor, açılınca kurulacak"],
   "siradaki": "Sesli asistanın on deneme araması, sonra yönlendirme."
  }
 ],
 "guncellendi": "2026-09-30T18:40:00+03:00"
}
```

- Bir müşteri bir satır; `ad` işletmenin adı. İşletme sahibinin adı, telefonu, e-postası, vergi numarası, giriş bilgisi bu dosyaya girmez.
- `baslangic`: sıfırıncı gün, para hesaba geçtiği gün. `rapor_gunu`: takvimin son günü (tam zamanlıda +21, işin yanında +28); şart geç yerine getirildiyse kayan tarih.
- `aylik`: bu müşteriyle anlaşılan aylık ücret, TL, sayı (onay belgesindeki rakam; deneme fiyatıysa o). Panelin "Her ay gelen" kartı bundan toplar; yazılmazsa ajansın fiyatını sayar ve anlaşmadan farklı rakam gösterir. Dosya ilk açılırken yazılır.
- `evre`: `karsilama`, `kurulum`, `birinci_dalga`, `test`, `canli`, `ikinci_dalga`, `eksikler`, `rapor` ya da teslim bitince `calisiyor`. Yazılmazsa panel günden hesaplar.
- `bilgiler`: toplanacak on bir bilgiden gelen sayısı (karşılama formu ve kurulum görüşmesi). `testler`: birinci dalga otuz iki tur, ikinci dalga on dört tur; geçen tur sayısı.
- `kontrol`: "teslim edildi" demenin beş şartı; yalnız gerçekleşen `true` olur. `kapsam_disi`: kurulamayan her parça, sebebiyle tek cümle; müşteriye aynı gün yazılı bildirildikten sonra.
- `siradaki`: o müşterinin sıradaki teslim işi, tek cümle.
- Dosya müşteri geldiğinde açılır ve her evre değişiminde, testten sonra, canlıya almadan sonra ve haftalık kontrolden sonra tam hâliyle yeniden yazılır; öbür müşterilerin satırları korunur.
