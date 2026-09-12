---
user-invocable: false
name: ekran-dili
description: "Ingilizce arayuzlerde cikan genel kelimelerin Turkce karsiliklari. Ogrenciye bir ekranda dugme tarif ederken acilir."
---

# Ekran dili (İngilizce arayüzler)

Bu sistemde Türkçe bilmeyen ekranlar var ve bu değişmiyor: CRM, siteyi yayına alan servis, YouTube'un bir kısmı, WhatsApp iş hesabının yönetim ekranı, ödeme sağlayıcısının bir kısmı, Claude uygulamasının bazı düğmeleri. Öğrenci İngilizce bilmiyor kabul edilir. Bilen öğrenci için de aynı yol yürür, bir zararı yok.

Kural, bütün modüllerde geçerli: FounderOS hiçbir zaman "İngilizce ekranı oku" demez. Bir düğmeden söz ederken üç şeyi birden verir.

1. Ekranda yazan İngilizce metin, tırnak içinde ve harfi harfine.
2. Türkçe karşılığı, parantez içinde.
3. Ekranın neresinde: sağ üst, sol menü, sayfanın en altı, açılan pencerenin içi.

Yazılışı böyle: **Sağ üstte "Sign up" (kaydol) yazan düğmeye bas.**

## Ekran uymuyorsa

Programlar ekranlarını değiştiriyor. Bir adımda tarif edilen düğmeyi bulamazsan tek yol var ve o yol her zaman açık: ekranın fotoğrafını çek ya da ekran görüntüsünü al, buraya at. FounderOS bakar ve hangi düğme olduğunu söyler. Bu bir aksama değil, sistemin normal işleyişi; utanılacak bir şey değil ve her modülün yedek yolunda yazılı.

Tarayıcının otomatik çeviri özelliği açtırılmaz. Sebebi şu: çeviri düğme adlarını değiştiriyor, sonraki adımda tarif edilen metin ekranda kalmıyor ve öğrenci iki adım sonra kayboluyor. Bir ekranı okumak için bir kez çevirtmek serbest, ama düğmeye basarken çeviri kapatılır.

## Her ekranda çıkan kelimeler

Bu liste programa göre değişmez, hepsinde aynıdır. Bir modül bunları tekrar açıklamaz, bu listeye güvenir.

Hesap ve giriş: Sign up (kaydol) · Sign in, Log in (giriş yap) · Log out, Sign out (çıkış yap) · Email address (e-posta adresi) · Password (şifre) · Confirm password (şifreyi tekrar yaz) · Forgot password (şifremi unuttum) · Verify, Verification (doğrula, doğrulama) · Continue with Google (Google hesabıyla devam et).

Yön: Next (ileri) · Back (geri) · Continue (devam) · Skip (atla) · Done, Finish (bitti) · Close (kapat) · Cancel (vazgeç) · Confirm (onayla) · Submit (gönder).

İş: Save (kaydet) · Edit (düzenle) · Delete (sil) · Add, Create, New (ekle, oluştur, yeni) · Copy (kopyala) · Paste (yapıştır) · Search (ara) · Filter (süz) · Export (dışarı aktar) · Import (içeri al) · Download (indir) · Upload (yükle) · Run, Start (çalıştır, başlat) · Stop (durdur) · Refresh (yenile) · Preview (önizleme) · Publish (yayınla) · Share (paylaş) · Connect (bağla) · Disconnect (bağlantıyı kes) · Allow (izin ver) · Deny (izin verme).

Ayar ve hesap: Settings (ayarlar) · Account (hesap) · Profile (profil) · Billing (faturalandırma, ödeme bilgileri) · Plan (paket) · Free plan (ücretsiz paket) · Upgrade (üst pakete geç) · Usage (kullanım) · Credits (kredi) · API key (bağlantı anahtarı) · Integrations (bağlantılar) · Notifications (bildirimler) · Team, Members (ekip, üyeler) · Invite (davet et).

Uyarı ve durum: Error (hata) · Failed (başarısız) · Success (başarılı) · Pending (bekliyor) · Active (etkin) · Inactive, Disabled (kapalı) · Required (zorunlu) · Optional (isteğe bağlı) · Loading (yükleniyor) · Try again (tekrar dene) · Are you sure? (emin misin?) · This action cannot be undone (bu işlem geri alınamaz).

Sözleşme ekranları: Terms of Service (kullanım şartları) · Privacy Policy (gizlilik politikası) · I agree, Accept (kabul ediyorum) · Decline (kabul etmiyorum) · Cookie (çerez) · Accept all (hepsini kabul et) · Reject all, Necessary only (hepsini reddet, sadece gerekli olanlar). Çerez sorusunda her zaman "sadece gerekli olanlar" seçilir.

Adres ve kimlik alanları: First name (ad) · Last name (soyad) · Full name (ad soyad) · Phone number (telefon numarası) · Country (ülke) · City (şehir) · Address (adres) · Postal code, ZIP (posta kodu) · Company name (şirket adı) · Website (internet sitesi).

## Modüllerin uyacağı biçim

Bir modül İngilizce ekranlı bir programda adım anlatıyorsa:

- Düğme adı üç parçalı yazılır: İngilizcesi tırnakta, Türkçesi parantezde, yeri tarif edilir.
- Yukarıdaki genel listedeki kelimeler için Türkçe karşılık tekrar yazılmaz, sadece İngilizcesi ve yeri yazılır.
- Programa özel bir düğme adı varsa (o programdan başka hiçbir yerde geçmeyen bir kelime) modül onu kendi metninde tam olarak verir ve ne işe yaradığını tek cümleyle açıklar.
- Ekran görüntüsü yolu her programın ilk adımında bir kez hatırlatılır, her adımda tekrarlanmaz.
- Öğrencinin yazması gereken İngilizce bir metin varsa (arama kutusuna yazılacak kelime gibi) modül o metni kopyalanacak şekilde tek satırda verir; öğrenciden çeviri istenmez.

## Hangi programlar İngilizce

İkinci blokta: siteyi yayına alan servis, WhatsApp iş hesabının yönetim ekranı. Üçüncü blokta: ödeme sağlayıcısının bir bölümü. Beşinci blokta: YouTube'un yükleme ekranı. CRM başlangıç görüşmesinde açılıyor, o yüzden onun ekranları sabit bir bloğa bağlı değil. Bunların hangi ekranında hangi düğmeye basılacağı ilgili modülün kendi metninde yazılı; burada sadece dilin nasıl ele alınacağı yazıyor.

Türkçe olan ve bu bölümün ilgilenmediği ekranlar: Google işletme profili, e-Devlet, banka uygulamaları, WhatsApp'ın kendisi. CRM bu listede değil: onun ekranı İngilizce ve düğme adları her adımda birlikte veriliyor.
