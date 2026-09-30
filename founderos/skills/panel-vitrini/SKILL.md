---
user-invocable: false
name: panel-vitrini
description: "Paneldeki Ajansım, Adaylar, Mesajlar ve İçerik bölümlerinin kaynakları, ajans.json ve mesajlar.json şeması ve gönderme komutu (aday aracının panel komutu). Bir modül teklif, fiyat, ideal müşteri, pazar, marka, sayfa, mesaj metinleri ya da içerik çıktısını değiştirdiğinde, sabah kapat'tan sonra, akşam kapanışında ve öğrenci 'paneli güncelle', 'panelim boş' dediğinde açılır."
---

# Panel vitrini: Ajansım, Adaylar, Mesajlar, İçerik

Öğrencinin panelinde (founderos.so/panel) Bugün, Ekip ve Yol'un yanında dört bölüm daha var: **Ajansım** (logo ve marka kiti, site, dönüşüm cümlesi, mekanizma, teklif ve paketler, teklifin açıları, fark, ideal müşteri, pazar araştırması), **Adaylar** (harita taramaları, en çok istenen yüz işletme ve her birine özel mesajlar, aşamalar, işletmelerde görülen açıklar, semtler, kanallar), **Mesajlar** (günün dağılımı, açılış cümleleri, telefon konuşması, ilk mesajlar, takipler, video senaryoları, itirazlar) ve **İçerik** (haftanın içeriği). Öğrenci işini oradan görür ve metinleri oradan kopyalar. Panel boşsa öğrenci yaptığı işi göremez; bu dört bölümü güncel tutmak kaydın parçasıdır.

## Kaynaklar

| Bölüm | Nereden gelir | Kim yazar |
|---|---|---|
| ajans | `.founderos/panel/ajans.json` artı marka kitinin `window.MARKA` bloğu artı sayfanın `window.SITE` bloğu | sen (aşağıdaki şema); marka ve sayfa bloğunu araç kendisi okur |
| adaylar | `adaylar.csv` | araç hesaplar; sen yazmazsın |
| mesajlar | `.founderos/panel/mesajlar.json` | sen (aşağıdaki şema) |
| icerik | `.founderos/panel/icerik.json` | icerik-motoru (şeması o modülde) |

Logo, renk kodları, yazı tipi, `biz` ve `degil` satırları marka kitinden gelir; sitenin başlığı ve açıklaması sayfadan. `ajans.json`'a bunları yazmazsın, iki yerde durup birbirini tutmaz hale gelir. Adaylar bölümü listenin kendisinden çıkar: en çok istenen yüzün bulgusu, açılış cümlesi, Instagram mesajı, e-postası ve video senaryosu adayın satırındaki `bulgu`, `kanca`, `dm_metni`, `eposta_konu`, `eposta_metni`, `video_metni` sütunlarından okunur. Metni satıra yazdıysan panelde de vardır.

## Gönderme

Dosyayı yazdıktan ya da listeyi değiştirdikten sonra öğrencinin klasörünün içinde sessizce:

```
python3 .founderos/adaylar-arac.py panel --yukle
```

Araç dört bölümü kurar, sunucunun kurallarıyla denetler ve yalnız değişen bölümü gönderir. Öğrenciye bir şey söylemezsin, komutu sohbete yazmazsın. Çıktının her satırı bir bölüm: `hazır`, `yok` ya da `GİTMEDİ: <alanın yolu>: <sebep>`. `GİTMEDİ` görürsen o dosyayı düzeltir, komutu bir kez daha çalıştırırsın; öğrenciye söylemezsin. `panel yüklenmedi` servise ulaşılamadı demektir: sessizce geçersin, bir sonraki gönderimde gider. Son satır `panel yüklendi: ...` ya da `panel: değişiklik yok`.

Araç klasörde yoksa (aday listesi henüz çıkmadıysa, birinci gün) önce `founderos:aday-listesi-araci`nın kurulum adımlarıyla `.founderos/` içine kurarsın; `adaylar.csv` olmadan da çalışır, o zaman adaylar bölümü `yok` der. `panel` komutunu tanımıyorsa araç eskidir: aynı beceriyle güncellersin.

## Ne zaman

- Her modülün sonunda, modül bu dört bölümden birine düşen bir şeyi değiştirdiyse: önce dosya, sonra komut.
- Sabah günaydında `kapat`tan sonra ve akşam kapanışında `ozet`ten sonra: aday listesi her gün değiştiği için adaylar bölümü tazelenir.
- Öğrenci "paneli güncelle", "panelim boş", "panelde teklifim görünmüyor" derse: eksik dosyayı İş Beyni'nden ve klasördeki dosyalardan yazar, komutu çalıştırır, tek cümle söylersin: "Panelin güncel; Ajansım, Adaylar ve Mesajlar bölümlerine bak."

Hangi modül hangi alanı yazar:

| Modül | Dosya | Alan |
|---|---|---|
| isini-kur, markani-kur | ajans.json | `ad`, `sehir`, `nis`, `alan_adi` |
| nisi-sec, nisi-dogrula, nis-arastirmasi | ajans.json | `pazar` |
| ideal-musteriyi-cikar | ajans.json | `icp` |
| konumlandir | ajans.json | `konum` |
| teklifi-yaz | ajans.json | `donusum`, `sistem_adi`, `mekanizma`, `teklif.bir_dakika`, `teklif.kademeler`, `teklif.guvence`, `teklif.acilar` |
| fiyati-belirle | ajans.json | `fiyat`, `teklif.kademeler[].kurulum` ve `aylik`, `teklif.itirazlar` |
| siteni-kur | ajans.json | `site.durum`, `site.adres` (yayına alınınca `yayinda` ve adresi) |
| adaya-mesaj-yaz | mesajlar.json | `karisim`, `telefon`, `ilk_mesaj`, `takipler`, `itirazlar`, `kancalar` |
| video-mesaj-cek | mesajlar.json | `video` |
| icerik-motoru | icerik.json | kendi şeması |

## Genel kurallar

Yalnız düz JSON. Anahtarlar bu sayfadaki adlarla birebir: küçük harf, Türkçe harfsiz, alt çizgi. Değerler Türkçe ve öğrencinin gerçek kaydından: İş Beyni, klasördeki dosyalar, günlük. Uydurma yok, yer tutucu yok ("...", "örnek", "buraya yazılacak"). Bilmediğin alanı yazmazsın; boş alanın bölümü panelde görünmez, bu doğru davranıştır. Sayılar sayı (`18000`, `"18.000 TL"` değil), tarih `YYYY-AA-GG`, oranlar yüzde tam sayı (`43`). Metinlerde uzun tire yok. Lisans anahtarı, CRM şifresi, öğrencinin ya da bir işletme sahibinin kişisel bilgisi (telefon, e-posta, kimlik) bu dosyalara girmez. Bir metin 4000 karakteri, bir liste 160 öğeyi geçmez; ajans 96 KB, mesajlar 128 KB. Dosya her yazılışta tam hâliyle yazılır (araç eski hâli birleştirmez); değişmeyen alanları da korursun: önce dosyayı okur, değişen alanı değiştirir, bütününü yazarsın.

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
  "kademeler": [{"ad": "Temel Kapsam", "icerik": ["madde", "madde"], "kurulum": 18000, "aylik": 4000}],
  "guvence": "müşteriye verilen güvence cümlesi",
  "acilar": [{"baslik": "açının adı", "metin": "iki üç cümle"}],
  "itirazlar": [{"soru": "itirazın kendisi", "cevap": "cevap"}]
 },
 "fiyat": {"bant": "Kurulum 18.000 ile 36.000 TL arası, aylık 4.000 ile 8.000 TL", "kurulum": 27000, "aylik": 6000},
 "icp": {"tek_cumle": "...", "buyukluk": "...", "basliklar": [{"ad": "Günü nasıl geçiyor", "metin": "..."}]},
 "pazar": {
  "secilen": "Klima ve kombi servisi",
  "neden": "seçimin gerekçesi, iki üç cümle",
  "adaylar": [{"nis": "Klima ve kombi servisi", "sehir_sayisi": 486, "tr_sayisi": 3553, "reklam_orani": 11, "telefon_orani": 91, "not": "tek cümle"}],
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
- `pazar.adaylar`: nisi-sec'in karşılaştırdığı nişler, en çok dört. `sehir_sayisi` sayım çekiminin kalan sayısı, oranlar o çekimin yüzdesi; bilinmeyen değer yazılmaz.

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
