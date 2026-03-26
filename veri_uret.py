import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Normal Dağılımlı Veri Üretme
# En az 500 satır istendiği için 750 satır üretiyoruz.
# Değişken 1: Matematik Notları (Ortalama 65, Standart Sapma 15)
# Değişken 2: Fen Notları (Ortalama 70, Standart Sapma 12)
n_ogrenci = 750

matematik = np.random.normal(65, 15, n_ogrenci)
fen = np.random.normal(70, 12, n_ogrenci)

# Verileri bir tabloya (DataFrame) dönüştür
df = pd.DataFrame({
    'Matematik_Notu': matematik,
    'Fen_Notu': fen
})

# Notların 0 ile 100 arasında kalmasını sağlamak için (isteğe bağlı temizlik)
df = df.clip(0, 100)

# 2. CSV Dosyası Olarak Kaydetme
# Bu kod '3. hafta' klasörünün içinde çalıştırıldığında 'sinav_verileri.csv' dosyasını oluşturur.
df.to_csv('sinav_verileri.csv', index=False)
print("CSV dosyası başarıyla oluşturuldu: sinav_verileri.csv")

# 3. Matplotlib ile Görselleştirme (Çan Eğrisi Formu)
plt.figure(figsize=(12, 6))

# Matematik Histogramı
plt.subplot(1, 2, 1)
plt.hist(df['Matematik_Notu'], bins=25, color='teal', edgecolor='black', alpha=0.8)
plt.title('Matematik Not Dağılımı')
plt.xlabel('Notlar')
plt.ylabel('Öğrenci Sayısı')

# Fen Histogramı
plt.subplot(1, 2, 2)
plt.hist(df['Fen_Notu'], bins=25, color='orange', edgecolor='black', alpha=0.8)
plt.title('Fen Not Dağılımı')
plt.xlabel('Notlar')
plt.ylabel('Öğrenci Sayısı')

plt.tight_layout()
plt.show()