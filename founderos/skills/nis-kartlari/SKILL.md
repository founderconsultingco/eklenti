---
user-invocable: false
name: nis-kartlari
description: On dokuz nis kartinin listesi, kart kurallari ve kart sablonu. Nis secilirken ve hangi kart modulunun acilacagi belirsizken acilir.
---

# FounderOS Niş Kartları (taslak 2, 5 Eylül 2026)

Kartlar plugin'in skill'lerinin okuduğu bilgi dosyalarıdır. Kural: uydurma yok, her rakam kaynaklı, bilinmeyen "sahadan dolacak" diye yazılır. Şablon en sonda.

Durum: 18 kartın 18'i tam araştırmayla yazıldı (kart başına 15 ile 47 kaynak). Bilinen açıklar: oto kuaför kartı şablondan önce yazıldı, beş bölümü (fiyat ve kapasite ayrı başlık, asistan kuralları, kanal ve zaman, reklam kütüphanesi kelimeleri, kaynak listesi) eksik, tamamlanacak; Meta Reklam Kütüphanesi hiçbir kartta görülemedi (canlı taramayla dolacak); diş kliniğinde TDB ve Resmi Gazete tam metni robot engeline takıldı, hukukçu teyidi şart.

## İçindekiler

- Oto kuaför, seramik kaplama, araç kaplama
- Güzellik salonu ve güzellik merkezi
- Klima ve kombi servisi
- Temizlik şirketi
- Oto servis ve cam filmi
- Cam balkon, PVC pencere, panjur
- Mutfak-banyo tadilat ve iç mimarlık
- Emlak ofisi
- Düğün organizasyon ve mekan
- Randevulu kuaför ve berber
- Haşere ilaçlama
- Oto galeri
- Sigorta acentesi
- Elektrik ve teknik bakım
- Fotoğraf stüdyosu
- Diş kliniği
- Pilates, PT ve butik stüdyo
- Estetik cerrahi ve medikal estetik
- Yetişkinlere yönelik dil ve mesleki eğitim kursları

---

# Şablon

# FounderOS Niş Kartı: Şablon ve Kurallar

Kart, FounderOS plugin'inin skill'lerinin okuduğu bilgi dosyasıdır. Öğrenci (Türkiye'de sıfırdan tek kişilik yapay zeka servis işi kuran, hiç müşterisi olmamış biri) nişini seçtiğinde bu kart açılır ve sistemin tamamı bu dille konuşur.

Sattığımız şey sabit: yerel işletmelerin KAÇIRDIĞI TALEBİ randevuya/işe çeviren sistem. Dört sızıntı: açılmayan telefon, geç dönülen DM/WhatsApp, dönülmeyen form, bir daha gelmeyen eski müşteri (veya teklif alıp kaybolan / randevu alıp gelmeyen). Reklamı biz vermiyoruz, reklamın karşılığını alıyoruz. Kademe 1: yazılı asistan + cevapsız aramaya anında mesaj + randevu ve hatırlatma. Kademe 2: + kaybolanları geri getirme + Google yorumu toplama + aylık rapor. Kademe 3: + reklam yönetimi.

## MUTLAK KURALLAR
1. Uydurma bilgi YOK. Her rakam, her fiyat, her alıntı kaynaklı (URL). Kaynağı olmayan bir şey karta girmez.
2. Bulamadığın şeyi "bilinmiyor, sahadan dolacak" diye yaz. Boş bırakmak uydurmaktan iyidir.
3. İşletmecinin KENDİ KELİMELERİ önemli. Forum, Ekşi, Şikayetvar, YouTube yorumu, haber alıntısı; tırnak içinde, kaynaklı.
4. "Telefona çıkmıyorlar" gibi varsayımları yazma; ancak yorumlarda/şikayetlerde kanıtı varsa yaz ve kanıtı göster.
5. Fiyatlar TL, güncel (2025-2026), kaynak sitesi belirtilerek. Fiyat yayınlanmıyorsa "sektör fiyat yayınlamıyor" diye yaz, bu da bulgudur.
6. Dil: sade Türkçe, kısa cümle, em dash yok, jargon yok. Öğrenci bunu telefonda söyleyecek.

## KART BÖLÜMLERİ (sıra ve başlıklar sabit)

# [Niş adı]

**Kapsam.** Hangi işletmeler dahil, hangileri değil. Google Haritalar'da nasıl geçiyorlar (kategori adları).

Bölümün son satırı sabit: `Müşteri yolculuğu: randevu | teklif | ikisi birlikte (kısa gerekçe).` Teslimat ve rapor bu satırı okur; boş bırakılmaz.

**Gerçek fiyatlar ve kapasite.** Ana hizmetlerin yayınlanmış fiyat aralıkları (kaynaklı). Günde/haftada kaç iş çıkarabildikleri (forum, röportaj, sektör yazısı). Bundan çıkan "kaçan tek bir müşteri = ne demek" hesabı, işletmecinin diliyle ("bir boş gün", "bir koltuk saati", "bir keşif").

Bölümün son satırı sabit: `Kayıp birimi: [tutar] ([işletmecinin dilindeki karşılığı]).` Rakam kartın kendi fiyat ve kapasite sayılarından çıkar; çıkmıyorsa "sahadan dolacak" yazılır, uydurulmaz.

**Sızıntı nerede.** Bu sektörde talebin gerçekten nerede kaybolduğuna dair KANIT: müşteri yorumları ("aradım açmadılar", "mesajıma üç gün sonra döndüler"), şikayet siteleri, sektör yazıları. En fazla üç sızıntı, en güçlüsü önce. Kanıt yoksa "yorumlarda iletişim şikayeti baskın değil, baskın tema şu" diye yaz; bu da kritik bulgu.

**Sezon.** Yılın hangi ayları yoğun, hangi ayları ölü; kaynağıyla. Bilgi yoksa "Kartta sezon bilgisi yok, sahadan dolacak. Şimdilik yıl boyu çalışıyor kabul ediliyor." yazılır. Sistem nişi seçerken buraya bakıyor; yılın dört ayından fazlası ölü geçen niş ilk müşteri için eleniyor.

**Rekabetin şekli.** Türkiye'de kaç işletme (kaynak: Haritalar sayımı, meslek odası, teklif pazaryeri istatistiği, sektör raporu). Reklam veriyorlar mı (Meta Reklam Kütüphanesi'nde ne görüldü, ya da görülemedi). Zincir/franchise var mı.

**Kim karar veriyor.** Sahibi mi, müdür mü, ortak mı; telefonu kim açıyor.

**İşletmecinin gerçek dertleri.** Kendi ağzından, kaynaklı alıntılarla. Onun sözlüğü: hangi kelimeleri kullanıyor ("boş gün", "ucuzcu", "eleman", "no-show"…). Bizim "kaçan talep" kelimemizin onun dilindeki karşılığı.

Bölümün son iki satırı sabit: `Sözlüğü: [6-10 kelime ve deyim, virgülle]` ve `İç sesi: "[tek cümle, işletmecinin kendi kendine söylediği ama kimseye söylemediği cümle]"`.

**Açılış cümlesi.** Tek bir cümle, en güçlü açıdan. İtiraz üretmeyen, işletmecinin zaten yapması gerektiğini bildiği bir şeyi söyleyen cümle. Neden bu açı, bir cümle gerekçe.

**Duran havuz.** Bu sektörde geri çağrılabilecek eski müşteri tipleri, en güçlüsü önce; her biri için meşru uyandırma sebebi (bakım zamanı, sezon, garanti, kontrol, yenileme). Listenin işletmede nerede durduğu (telefon rehberi, WhatsApp, randevu defteri, fiş).

**Asistan kuralları.** Yazılı/sesli asistanın bu sektörde ne söyleyeceği, ne SÖYLEMEYECEĞİ (fiyat verir mi, hangi bilgileri toplar, hangi konuda sahibine devreder). Ton (yorumlarda övgü ve şikayet neye odaklanıyor).

**Kanal ve zaman.** İşletmeciye nereden ulaşılır (telefon/Instagram/e-posta açıklığı; kanıt), günün hangi saati müsait, hangi saat kesinlikle değil. Adayın kendi talep kanalı hangisi (form, IG DM, WhatsApp, telefon): demo için talep nereye bırakılır.

**Reklam kütüphanesi kelimeleri.** Meta Reklam Kütüphanesi'nde aranacak 8-15 Türkçe anahtar kelime (hizmet adları, kampanya kelimeleri, yan hizmetler).

**Yasal sınırlar.** Reklam, tanıtım, mesaj (İYS), sağlık, KVKK açısından bu nişe özel kısıt var mı; kaynaklı. Yoksa "yok".

**Yoğun şehirler.** Kaynaklı.

**Gerçek itirazlar ve karşılıkları.** 5-7 itiraz; her biri işletmecinin ağzından, karşılık sektör verisiyle. Bölümün ilk satırı sabit: `En güçlü üç itiraz: [üç kısa ad, virgülle]`. Sistem üç itiraz videosunu bu üçünden çekiyor.

**Sahadan dolacak.** Bilinmeyenler listesi (gerçek dönüş süreleri, çalışan açılış cümlesi, kapatma oranı, hangi kademe satılıyor, ilk vaka çalışması).

**Kaynaklar.** Kullanılan tüm URL'ler.

## Kart modüllerinin adları

- Oto kuaför, seramik kaplama, araç kaplama: `nis-oto-kuafor`
- Güzellik salonu ve güzellik merkezi: `nis-guzellik-salonu`
- Klima ve kombi servisi: `nis-klima-kombi`
- Temizlik şirketi: `nis-temizlik`
- Oto servis ve cam filmi: `nis-oto-servis`
- Cam balkon, PVC pencere, panjur: `nis-cam-balkon`
- Mutfak-banyo tadilat ve iç mimarlık: `nis-tadilat`
- Emlak ofisi: `nis-emlak`
- Düğün organizasyon ve mekan: `nis-dugun`
- Randevulu kuaför ve berber: `nis-kuafor-berber`
- Haşere ilaçlama: `nis-hasere`
- Oto galeri: `nis-oto-galeri`
- Sigorta acentesi: `nis-sigorta`
- Elektrik ve teknik bakım: `nis-elektrik`
- Fotoğraf stüdyosu: `nis-fotograf`
- Diş kliniği: `nis-dis-klinigi`
- Pilates, PT ve butik stüdyo: `nis-pilates`
- Estetik cerrahi ve medikal estetik: `nis-estetik`
- Yetişkinlere yönelik dil ve mesleki eğitim kursları: `nis-dil-kursu`

Bir nişin rakamını, itirazını, yasal sınırını ya da kayıp birimini kendi kartından okursun. Kartta rakam yoksa "sahadan dolacak" der ve iş rakamsız yürür.
