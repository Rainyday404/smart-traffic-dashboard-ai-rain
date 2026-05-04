import pandas as pd

# Membaca data dari file CSV mentah
df = pd.read_csv('data/raw/traffic_smartcity_v1.csv')

# Mengonversi kolom 'datetime' ke tipe data datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Mengurutkan data berdasarkan waktu
df = df.sort_values('datetime')

# Menghapus baris yang memiliki nilai kosong (missing values)
df = df.dropna()

# Menyimpan hasil pembersihan ke file CSV baru tanpa menyertakan index
df.to_csv('data/clean/traffic_smartcity_clean_v1.csv', index=False)

print("Data cleaning selesai")