# FounderOS

Sıfırdan tek kişilik yapay zeka servis işini doksan günde kuran sistem.

## Çalışma anında tek kural: her şey beceri (skill) olmak zorunda

Bu, 9 Eylül'de yapılan testlerin sonucu ve mimarinin tamamını belirliyor.

Çalışma anında paketin kendi klasöründeki dosyalar okunamıyor. Claude Code izin kuralı şu: okuma serbestisi sadece çalışılan klasör ve `additionalDirectories` için var; eklenti klasörü ikisine de girmiyor. Modelin `Read` ya da `cat` ile paket dosyası açmaya çalışması öğrenciye izin penceresi çıkarıyor, izin gelmezse gün mesajın birincisinde duruyor. Eklentinin `settings.json` dosyası bunu düzeltemiyor; orada sadece `agent` ve `subagentStatusLine` anahtarları destekleniyor.

Beceri gövdeleri ise izin istemeden geliyor: `Skill` aracı çağrıldığında gövde doğrudan bağlama giriyor. Ajan ve komut gövdeleri de öyle.

Sonuç: modelin çalışma anında görmesi gereken her metin ya ajan gövdesinde ya bir beceri gövdesindedir. `ortak/` ve `baglanti/` klasörleri kaynak olarak duruyor ama yayınlanan pakete girmiyor.

## Katmanlar

### Ajan (`agents/founderos.md`)

Sistemin beyni. Kim olduğu, sesi, beş kuralı, günün modülünü nasıl seçtiği, kilitler, yedek yol ve klasör kuralı hepsi burada. Bu dosya tek kaynaktır; eskiden `ortak/sistem-talimati.md` ve `ortak/klasor-kurali.md` diye iki ayrı dosyaydı, artık değil.

`settings.json` içindeki `{"agent": "founderos"}` bu ajanı oturumun kendisi yapıyor.

`agents/yardimci.md` · ağır işleri ana konuşmayı şişirmeden yapan arka plan yardımcısı.

### Beceriler (`skills/`)

Yetmiş beceri, üç tür:

- Kırk modül: `isini-kur`, `nisi-sec`, `fiyati-belirle` ve diğerleri. Günün işini yapan parçalar.
- On bir bilgi becerisi: `is-beyni` (şema ve boş şablon), `crm-baglantisi`, `sozluk`, `ekran-dili`, `is-modeli`, `inanc-degisimleri`, `doksan-gun-plani`, `hizmet-sozlesmesi`, `sahaya-cikis-kontrol-listesi`, `aday-listesi-dosyasi` (adaylar.csv sütunları, sayfa ve aracın komutları), `aday-listesi-araci` (aracın ve sayfa şablonunun kendisi: `ortak/adaylar-arac.py` ve `ortak/adaylar-sablon.html`, beceri klasöründe ham dosya, SKILL.md içinde gömülü kopya; FounderOS öğrencinin klasöründeki gizli `.founderos/` altına kopyalar).
- On dokuz niş becerisi: `nis-kartlari` (liste, kurallar, şablon) ve on dokuz nişin kendi kartı, `nis-kuafor-berber` biçiminde. Kartlar ayrı duruyor çünkü hepsi tek dosyada 286 KB tutuyordu; öğrencinin sadece kendi nişinin kartı açılıyor.

Hepsi `user-invocable: false`. Öğrenci modül adı bilmez.

### Bağlantı (`.mcp.json`)

İki uzak sunucu. `crm`: CRM sunucusunun adresi; bağlantı OAuth ile kuruluyor, öğrenci kendi hesabıyla giriyor, hangi bölüme erişileceğini işaretliyor, onaylıyor, anahtar yazmıyor; sıra ve cümleler `crm-baglantisi` becerisinde. `veri`: FounderOS'un veri servisi (`https://founderos.so/mcp`); aday listesini çeker, kimlik olarak her çağrıda İş Beyni'ndeki lisans anahtarı gider. Sunucu kodu `founderos-vercel-site` içinde (`app/mcp`, `lib/veri-servisi.ts`); araçlar `aday_ara`, `aday_sonuc`, `kullanim`, `olcum_yaz`. Kurallar ana yöneticinin "Veri servisi" bölümünde.

### Kap (`.claude-plugin/`, `commands/`)

- `.claude-plugin/plugin.json` · eklenti künyesi.
- `.claude-plugin/marketplace.json` · yerel geliştirme kataloğu. Yayınlanan katalog `founderos-dagitim/yayinla.py` tarafından üretiliyor.
- `commands/` · beş giriş kapısı: `/founderos:kurulum`, `/founderos:gun`, `/founderos:musteri`, `/founderos:durum`, `/founderos:nis-arastirma` (kaynaklı niş araştırması, raporu klasöre `nis-arastirmasi.md` olarak yazar). Öğrenci bunları yazmaz; düz cümleyle konuşur, ajan hangi işin açılacağına kendi karar verir. Komutlar ince tutuldu: mantık becerilerde.

## Kurallar

Öğrenci terminale girmez. Komut satırı, kurulum betiği, API anahtarı hiçbiri onun tarafında olmaz. Onun dünyası tek pencere.

Öğrencinin bir klasörü olmak zorunda. Program her sohbeti kendi geçici alanında çalıştırıyor ve o alan sohbet bitince siliniyor; klasör bağlı değilse İş Beyni ertesi gün yok oluyor. Bu yüzden kurulumun üçüncü adımı klasörden bir proje kurmak, ve FounderOS klasör gelmeden hiçbir şey yazmıyor.

Sistem sormaz, söyler. Seçenek menüsü sunulmaz. Sorulan tek şey sistemin bilemeyeceği bilgidir.

## Dosyaları yeniden üretme

İki adım, ikisi de `founderos-plugin` klasörünün içinden:

    python3 araclar/uret.py && python3 araclar/beceriler.py

Birincisi ana dosyayı (`founderos-skill-icerikleri.md`) otuz dokuz modül becerisine ve `ortak/` altındaki bilgi dosyalarına bölüyor. İkincisi `ortak/` ve `baglanti/` altındaki bilgi dosyalarını becerilere çeviriyor ve niş kartlarını on sekize bölüyor.

Elle yazılan, üzerine yazılmaması gereken iki dosya: `agents/founderos.md` ve `ortak/is-beyni-sablon.md`.

Takvim iki yerde yazılı: ajan gövdesindeki gün listesi ve ana dosyadaki gün haritası. Biri değişirse diğeri de değişecek.
