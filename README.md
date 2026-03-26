# 3. Hafta: Veri Üretimi ve Dağılım Analizi

Bu proje, Python programlama dili kullanılarak sentetik bir veri seti oluşturulması ve bu verilerin istatistiksel dağılımının incelenmesi amacıyla hazırlanmıştır.

## Proje İçeriği
* **veri_uret.py**: `numpy` kütüphanesi kullanılarak normal dağılıma sahip veriler üreten ve `matplotlib` ile görselleştiren ana kod dosyası.
* **sinav_verileri.csv**: Üretilen 750 satırlık veri seti.
* **prompt.md**: Kodun oluşturulma aşamasında Antigravity (Yapay Zeka) ile gerçekleştirilen diyaloglar.

## Veri Seti Hakkında
Görev kapsamında oluşturulan veri seti, bir okulun **Matematik** ve **Fen Bilimleri** derslerine ait sınav notlarını temsil etmektedir.
- **Satır Sayısı:** 750
- **Dağılım Türü:** Normal Dağılım (Gauss Dağılımı / Çan Eğrisi)
- **Matematik Notları:** Ortalama 65, Standart Sapma 15 olacak şekilde simüle edilmiştir.
- **Fen Notları:** Ortalama 70, Standart Sapma 12 olacak şekilde simüle edilmiştir.

## Görselleştirme
Üretilen verilerin frekans dağılımları histogram grafikleri kullanılarak doğrulanmıştır. Grafiklerde verilerin merkezde yoğunlaştığı ve kenarlara doğru simetrik bir şekilde azaldığı (çan eğrisi formu) açıkça görülmektedir.