---
user-invocable: false
name: crm-baglantisi
description: CRM baglantisinin nasil kuruldugu, hangi bilginin CRM'de hangisinin Is Beyni'nde durdugu, olcu kurallari ve lisans anahtari akisi. CRM'e ilk kez baglanirken ve bir sayinin nereden okunacagi belirsizken acilir.
---

# CRM bağlantısı ve araç haritası

Bu dosya tek geçiş noktasıdır. CRM'e giden her iş buradan geçer. Platform değişirse değişmeyen katman burasıdır.

## Bağlantı nasıl kurulur

Öğrenci hiçbir anahtar yazmaz, hiçbir betik çalıştırmaz. Bağlantı, öğrencinin kendi CRM hesabıyla bir kere giriş yapmasıyla kurulur ve sonra kendi kendine yenilenir.

Sıra şu:

1. FounderOS CRM'den bir şey okumaya çalışır. Bağlantı yoksa tarayıcıda giriş penceresi bu anda açılır.
2. Öğrenci kendi kullanıcı adı ve şifresiyle girer. İkisi de satın alma e-postasında duruyor.
3. Ekranda hangi bölüme erişileceği sorulur. Öğrenci kendi bölümünü işaretler. Burası önemli: işaretlemediği bölümü FounderOS göremez, boş geçilirse bağlantı işe yaramaz.
4. Onaylar. Bağlantı kurulur, bir daha sorulmaz.

FounderOS bu pencereyi öğrenciye önceden haber verir, çünkü habersiz açılan giriş ekranı beginner'ı durduruyor. Söyleyeceği tek cümle şu: "Şimdi CRM'e bağlanıyorum, ekranda bir giriş penceresi açılacak. Kullanıcı adın ve şifren satın alma e-postanda. Girdikten sonra hangi bölüme erişeceğim sorulacak, orada kendi bölümünü işaretle ve onayla."

Giriş penceresi açılmazsa ya da yetki reddedilirse FounderOS durmaz. O günün işine CRM'siz devam eder, kayıtları elde tutar ve bağlantıyı ertesi günün ilk işi yapar. Hiçbir modül bağlantı hatasıyla durmaz.

## Hangi iş hangi kayda düşer

Aday ve müşteri kayıtları CRM'de yaşar, İş Beyni'nde ikinci kez tutulmaz. İkinci kez tutulan bilgi er geç birbirini tutmaz.

CRM'de duran: kişiler, fırsat hattı ve aşamaları, randevular, konuşmalar, akışlar, alanlar ve özel değerler, çağrı kayıtları.

İş Beyni'nde duran: kurucunun kendisi, niş kararı, teklif ve fiyat, marka, kararların gerekçesi, açık işler, gün sayacı ve koşan toplam.

Koşan toplam bilerek İş Beyni'nde: CRM böyle bir toplamı tutmuyor, akşam sayımı atlanan gün bütün kilitler kayıyor.

## Ölçüler

Bir sayı iki yerden okunabiliyorsa CRM üstündür. İş Beyni'ndeki sayı yalnız CRM'in tutmadığı sayılar içindir.

Bir sayı hiç ölçülemiyorsa "ölçülemedi" yazılır ve o sayı hakkında karar verilmez.

## Taşınabilirlik notu

Bağlantı standardı platformdan bağımsızdır, aynı sunucu başka bir yapay zeka penceresine de takılabilir. Ama yazma yetkisi her platformda açık değildir. Yazma kapalıysa sistem okur ve anlatır, kaydı açamaz. O halde çalışan tek yol: kaydı öğrenci elle açar, FounderOS ne yazacağını söyler.

## Lisans anahtarı

Anahtarın işi korumak değil, eşleştirmek: hangi alıcı hangi CRM hesabına ait.

Akış şu. Alıcı siteden satın alır. Bizim taraf CRM'de onun bölümünü açar ve e-postasına dört şey gönderir:

- lisans anahtarı,
- kurulum sayfasının adresi,
- CRM giriş adresi,
- CRM kullanıcı adı ve ilk şifresi.

Alıcı eklentiyi kurar, klasörünü bağlar, ilk mesajında FounderOS anahtarı ister, o da sohbete yapıştırır. CRM kullanıcı adı ve şifresi sohbete yazılmaz; onlar sadece giriş penceresine girilir. Hiçbir adımda komut satırı yok.

Anahtar İş Beyni'nin birinci bölümüne yazılır ve bir daha sorulmaz. Sonraki günlerde kurulum oradan okur.

Eklenti ayar ekranındaki alan KULLANILMIYOR. Denendi: değer kaydediliyor ama çalışma anında okunamıyor, yani her oturum "anahtar yok" diyor. Sohbete yazdırma yolu hem çalışıyor hem de başka platforma aynen taşınıyor.

Şu an sunucu kontrolü yok ve bu bilerek böyle. Anahtarı olmayan kişinin CRM hesabı da yoktur; hesabı olmayan sistem hiçbir işini yapamaz. Yani kilit kodda değil, hesapta.

Kopyalanmayı tamamen engellemeye çalışmıyoruz. Paketin içi metin ve metin kopyalanır. Kopyalanamayan şey CRM hesabı ve arkasındaki hazır paket; değer orada duruyor.

Sonradan sunucu kontrolü eklenecekse yeri burasıdır. Anahtar bağlantı kurulurken bir uca sorulur, cevap "geçerli" değilse bağlantı kurulmaz. Modüllerin hiçbiri değişmez.
