# Antigravity ile Görev 7 Konuşma Kaydı

Bu dosya, ödevde istenen normal dağılımlı veri seti üretim sürecinde yapay zeka asistanı ile yapılan diyaloğu içermektedir.

## Kullanıcı Talebi:
"Bana normal dağılımlı (çan eğrisi formunda), en az 500 satırlık ve 2 değişkenli bir veri seti üretip CSV olarak kaydeden, ardından bu veriyi matplotlib ile görselleştiren bir Python kodu yazar mısın?"

## Revizyon:
"Boy ve kilo değişkenleri olmasın, başka bir senaryo üzerinden yapalım."

## Yapay Zeka Yanıtı ve Uygulama:
Yapay zeka asistanı, senaryoyu "Matematik ve Fen Bilimleri Sınav Notları" olarak güncelledi. 
- **Veri Sayısı:** 750 satır (En az 500 şartı sağlandı).
- **Değişkenler:** Matematik_Notu ve Fen_Notu (2 değişken şartı sağlandı).
- **Yöntem:** `numpy.random.normal` fonksiyonu ile çan eğrisi formu oluşturuldu.
- **Çıktı:** `sinav_verileri.csv` dosyası oluşturuldu ve `matplotlib` ile histogram grafikleri çizdirildi.

## Kurulum ve Çalıştırma Notları:
Terminal üzerinden şu komutla kütüphaneler yüklendi:
`pip install pandas numpy matplotlib`

Kod şu komutla çalıştırıldı:
`python veri_uret.py`