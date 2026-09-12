---
user-invocable: false
name: aday-listesi-dosyasi
description: "adaylar.csv'nin sutunlari ve degerleri, adaylar.html sayfasinin kurulmasi (sablon bu klasorde) ve veri dosyasinin yenilenme komutu. Liste ilk yazilirken, adaylar.csv'ye her yazistan sonra ve ogrenci listesini sorunca acilir."
---

# Aday listesi dosyası ve sayfası

Öğrencinin aday havuzunun CRM açılana kadarki tek yeri klasördeki `adaylar.csv` dosyasıdır; yanında öğrencinin gözüyle baktığı `adaylar.html` sayfası durur. Bu dosya ikisinin de kurallarını taşır: sütunlar, değerler, kim ne yazar, sayfa nasıl üretilir ve yenilenir. Modüller sütun adını buradan alır, kendi başına sütun uydurmaz.

## Üç dosya, tek klasör

- `adaylar.csv`: kayıtların kendisi. Veri servisinden gelen satırlar FounderOS tarafından buraya eklenir, denetim ve temas bilgisi buraya işlenir. UTF-8, virgülle ayrılmış, başlık satırı bir kere.
- `adaylar.html`: öğrencinin çift tıklayıp tarayıcıda açtığı sayfa. Bir kere yazılır, bir daha değişmez. Veriyi yanındaki `adaylar-veri.js` dosyasından okur.
- `adaylar-veri.js`: `adaylar.csv`'nin sayfaya okunacak kopyası ve üretilme saati. Her csv değişikliğinden sonra FounderOS yeniden üretir; öğrenci bu dosyayı hiç görmez.

Öğrenci csv'yi Excel'de açmaz, açmak isterse sayfaya yönlendirilir: "Listeyi görmek için klasördeki `adaylar.html` dosyasına çift tıkla." Sayfa Excel'e göre üç şeyi daha iyi yapar: ipuçlarını Türkçe rozet olarak gösterir, bugün sırada olanı yeşil, günü geçmişi turuncu boyar, satıra tıklayınca ayrıntıyı açar.

## Sütunlar (sıra ve ad sabittir)

İlk on dört sütun veri servisinin başlığıdır, FounderOS değiştirmez; kalan yirmi biri FounderOS ekler ve doldurur. Tarihler her yerde `YYYY-AA-GG` biçimindedir. Boş bilgi boş bırakılır, "yok" yazılmaz.

Servisten gelenler:
1. `kisa_ad`: aramada ve mesajda kullanılan kısa işletme adı.
2. `ad`: Haritalar'daki tam ad.
3. `telefon`: `+90` ile başlayan tek biçim.
4. `eposta`
5. `instagram`: hesap adresi.
6. `site`
7. `adres`
8. `semt`: ilçe ya da semt.
9. `yorum_sayisi`
10. `puan`: Haritalar puanı.
11. `kategori`: Haritalar'ın verdiği kategori; kartla karşılaştırma bundan yapılır.
12. `ipuclari`: boşlukla ayrılmış kodlar: `profil_sahipsiz`, `site_yok`, `instagram_yok`, `yorum_az`, `aksam_kapali`, `hafta_sonu_kapali`, `pazar_kapali`, `saat_yok`. Hızlı denetimin dışarıdan görülen kısmı; sayfa bunları Türkçe gösterir.
13. `elenme`: servisin işaretlediği sebep (`kapali`, `tekrar`, `iletisim_yok`, `zincir`). Onayla silinen satır dosyadan çıkar; bu sütun dolu satır sayfada görünmez.
14. `harita`: Haritalar bağlantısı.

FounderOS'un eklediği sütunlar:
15. `eklenme_tarihi`: kaydın listeye girdiği gün. Çekim günü yazılır, sonra değişmez.
16. `kaynak`: `haritalar`, `iş ilanı`, `elle`.
17. `yuz`: en çok istenen yüz işletmedeyse `evet`, değilse boş.
18. `sahibi`: karar verenin adı; derin denetimin onuncu maddesi.
19. `uygunluk`: uygunluk puanı, 0-15. Sayfa A (10 ve üstü), B (6-9), C (5 ve altı) diye gösterir.
20. `sizinti`: sızıntı puanı, 0-5. Denetlenmemişse boş.
21. `bulgu`: en güçlü bulgu, tek cümle.
22. `lira`: lira karşılığı, tek satır hesap.
23. `denetim_tarihi`
24. `asama`: `yeni`, `temasta`, `cevap verdi`, `randevu`, `görüşüldü`, `sonra`, `kapandı`, `müşteri`. Adayın işin neresinde olduğu; aynı anda tek değer.
25. `telefon_durumu`, 26. `eposta_durumu`, 27. `instagram_durumu`, 28. `video_durumu`: dört kanalın durumu, her biri `yapılmadı`, `yapıldı`, `cevap geldi` ya da `kapandı`. Kuralı adaya-mesaj-yaz'da: bir kanaldan cevap gelince diğerleri durur.
29. `temas_sayisi`: bütün kanallarda toplam temas.
30. `son_temas_tarihi`, 31. `son_temas_kanali` (`telefon`, `e-posta`, `instagram`, `video`).
32. `siradaki_hareket`: tek satır, örneğin "telefon, 3. gün takibi". Bir adayın aynı anda tek sıradaki hareketi olur.
33. `siradaki_tarih`: o hareketin günü. Bugünse sayfa yeşil, geçmişse turuncu gösterir; günün listesi bu sütundan çıkar.
34. `randevu_tarihi`
35. `not`: serbest, kısa. "Kalfa açtı, sahibi öğleden sonra dükkanda" gibi.

Kim yazar: 1-14 veri servisi (aday-listesi-cikar Adım 1); 15-17 aday-listesi-cikar (Adım 5 ve 7); 18-23 aday-denetimi-cikar; 24-35 adaya-mesaj-yaz, gorusmeye-getir, gorusmeyi-analiz-et, sabah listesi (gunu-planla, sıradaki tarih) ve akşam kapanışı (rakamlari-oku). CRM açıldığı gün dosya CRM'e yüklenir ve "CRM'e taşındı, tarih" notuyla kapanır; o günden sonra sayfa da eskir, öğrenciye CRM gösterilir.

## Sayfa nasıl kurulur (bir kere, listenin çıktığı gün)

Şablon bu becerinin klasöründe `adaylar.html` adıyla durur; beceri açıldığında klasörün yolu görünür. aday-listesi-cikar'ın yedinci adımında, `adaylar.csv` ilk kez yazıldığında FounderOS şablonu öğrencinin klasörüne `adaylar.html` adıyla olduğu gibi kopyalar: yolu biliyorsa kopyalama komutuyla, bilmiyorsa dosyayı okuyup aynı adla birebir yazarak. Şablonun içi değiştirilmez, kısaltılmaz, "iyileştirilmez". Kopyaladıktan sonra dosyanın `</html>` ile bittiği ve 12.000 bayttan büyük olduğu kontrol edilir; tutmuyorsa yeniden kopyalanır. Sonra veri dosyası üretilir (aşağıda) ve öğrenciye tek cümle söylenir: "Listen klasörde `adaylar.html` dosyasında, çift tıkla açılır." Sayfa daha sonra hiç yeniden yazılmaz; klasörde varsa dokunulmaz.

## Veri dosyası nasıl yenilenir (her csv değişikliğinden sonra)

`adaylar.csv`'ye her yazıştan sonra FounderOS öğrencinin klasörünün içinde şu komutu sessizce çalıştırır; satırlar sohbete girmez, öğrenci komut görmez:

```
python3 -c "import json,datetime;t=datetime.timezone(datetime.timedelta(hours=3));print('window.ADAYLAR='+json.dumps(open('adaylar.csv',encoding='utf-8').read())+';window.ADAYLAR_TARIH='+json.dumps(datetime.datetime.now(t).strftime('%d.%m.%Y %H:%M'))+';')" > adaylar-veri.js
```

`python3` yoksa aynı işi yapan yedek:

```
node -e "const fs=require('fs');fs.writeFileSync('adaylar-veri.js','window.ADAYLAR='+JSON.stringify(fs.readFileSync('adaylar.csv','utf8'))+';window.ADAYLAR_TARIH='+JSON.stringify(new Date().toLocaleString('tr-TR',{timeZone:'Europe/Istanbul',day:'2-digit',month:'2-digit',year:'numeric',hour:'2-digit',minute:'2-digit'}))+';')"
```

İkisi de çalışmazsa FounderOS dosyayı kendisi yazar: `window.ADAYLAR=` artı csv'nin tamamı JSON dizesi olarak artı `;window.ADAYLAR_TARIH="GG.AA.YYYY SS:DD";`. Bu son yol pahalıdır, yalnız komut çalışmadığında.

Ne zaman yenilenir: çekim bitip liste yazıldığında, hızlı ve derin denetim sonuçları işlendiğinde, sabah günün listesi kurulduğunda (sıradaki tarihler yazılır), akşam kapanışında temaslar işlendiğinde ve öğrenci "listemi göster", "listemi yenile", "listem nerede" dediğinde. Sayfa açıkken yenilenen veri, sayfa tazelenince görünür; öğrenciye "sayfayı yenile" denir.

## Öğrenci listeyi sorunca

"Listem nerede", "listemi göster", "kimleri arayacağım", "Excel'de açayım mı" gibi her soruda cevap aynı: veri dosyası yenilenir ve sayfa gösterilir. Yer tarifi çıplak yol değil, adım adım: "Masaüstü, sonra FounderOS klasörü, `adaylar.html` dosyası; üstüne çift tıkla, tarayıcıda açılır." Sayfada ne göreceği tek cümleyle söylenir: yeşil satır bugün sırada, turuncu satır günü geçmiş, satıra tıklayınca ayrıntı açılır. Beş yüz satır sohbete dökülmez; öğrenci belli bir adayı sorarsa o adayın satırı okunup söylenir.
