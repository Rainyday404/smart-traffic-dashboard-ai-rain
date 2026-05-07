# Smart City Traffic Prediction AI - Big Data Technology

Proyek ini merupakan implementasi dari **Modul Praktikum 7** mata kuliah Teknologi Big Data. [cite_start]Fokus utama adalah membangun pipeline Machine Learning untuk memprediksi volume lalu lintas menggunakan algoritma Random Forest dan visualisasi dashboard real-time[cite: 6, 18, 20].

## 👤 Identitas Mahasiswa
- **Nama:** Ivan Dwika Bagaskara
- **NIM:** 230104040205
- **Program Studi:** Teknologi Informasi

## 🛠️ Stack Teknologi
- **Bahasa Pemrograman:** Python 
- **Environment:** Linux Server Environment (WSL Ubuntu) 
- **Editor:** VS Code (Remote WSL) 
- **Engine:** Apache Spark (PySpark) 
- **Library Utama:** Pandas, Scikit-Learn (Random Forest), Joblib, Streamlit 

## 📂 Struktur Proyek
[cite_start]Sesuai dengan panduan praktikum, proyek ini disusun sebagai berikut:
```bash
bigdata-project/
├── analytics/
│   └── traffic_ml_model_v1.py        # Script pelatihan model ML
├── dashboard/
│   └── traffic_dashboard_v1.py       # Dashboard interaktif Streamlit
├── data/
│   ├── raw/                          # Dataset mentah (.csv)
│   └── clean/                        # Dataset hasil pembersihan
├── models/
│   └── traffic_model_v1.pkl          # File model tersimpan
├── scripts/
│   └── traffic_data_cleaning_v1.py   # Script pembersihan data
└── README.md
```

## 🚀 Langkah-Langkah Menjalankan Proyek

### 1. Persiapan Data (Data Cleaning)
Membersihkan dataset mentah dari folder `data/raw/` dan menyimpannya ke `data/clean/`.
```bash
python scripts/traffic_data_cleaning_v1.py
```

### 2. Pelatihan Model (Feature Engineering & Modeling)
Melakukan ekstraksi fitur waktu (*hour*, *day*, *lag*) dan melatih model *Random Forest Regressor*.
```bash
python analytics/traffic_ml_model_v1.py
```

### 3. Visualisasi Dashboard
Menjalankan dashboard modern berbasis Streamlit untuk melihat tren dan melakukan simulasi prediksi.
```bash
streamlit run dashboard/traffic_dashboard_v1.py
```



## 📊 Insight Praktikum
- **Feature Engineering:** Penggunaan fitur waktu seperti jam dan hari sangat kuat dalam menentukan pola kemacetan.
- **Model Efficiency:** Model Random Forest mampu menangkap pola non-linear pada data traffic dengan baik.
- **Smart City Integration:** Sistem ini mensimulasikan bagaimana AI dapat digunakan untuk *Adaptive Traffic Control System*.

---
*Laporan ini dibuat sebagai syarat pemenuhan tugas Modul Praktikum Big Data Technology 2026.* 
```