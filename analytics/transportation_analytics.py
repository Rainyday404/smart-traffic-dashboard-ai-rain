import pandas as pd
import os

# ============================
# LOAD DATA
# ============================
def load_data(path):
    if not os.path.exists(path):
        return pd.DataFrame()
    
    # Mencari semua file dengan ekstensi .parquet di dalam folder path
    files = [f for f in os.listdir(path) if f.endswith(".parquet")]
    
    if not files:
        return pd.DataFrame()
    
    # Menggabungkan semua file parquet menjadi satu DataFrame
    df = pd.concat(
        [pd.read_parquet(os.path.join(path, f)) for f in files],
        ignore_index=True
    )
    
    return df

# ============================
# PREPROCESS
# ============================
def preprocess(df):
    if df.empty:
        return df
    
    # Mengonversi kolom timestamp ke format datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    # Menghapus baris yang timestamp-nya tidak valid (NaT)
    df = df.dropna(subset=["timestamp"])
    
    return df

# ============================
# METRICS
# ============================
def compute_metrics(df):
    if df.empty:
        return {
            "total_trips": 0,
            "total_fare": 0,
            "top_location": "-"
        }
    
    return {
        "total_trips": len(df),
        "total_fare": df["fare"].sum(),
        "top_location": df.groupby("location")["fare"].sum().idxmax()
    }

# ============================
# PEAK HOUR
# ============================
def detect_peak_hour(df):
    if df.empty:
        return None
    
    # Mengambil jam dari kolom timestamp
    df["hour"] = df["timestamp"].dt.hour
    # Mengambil jam dengan frekuensi perjalanan terbanyak
    return df.groupby("hour").size().idxmax()

# ============================
# WINDOWING & VISUALIZATION
# ============================
def traffic_per_window(df):
    """
    Menghitung jumlah traffic per interval 1 menit.
    """
    if df.empty:
        return None
    
    # Memastikan kolom timestamp adalah datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df.set_index('timestamp') \
        .resample('1min') \
        .size()

def fare_per_location(df):
    if df.empty:
        return pd.Series()
    
    # Menghitung total pendapatan per lokasi
    return df.groupby("location")["fare"].sum().sort_values(ascending=False)

def vehicle_distribution(df):
    if df.empty:
        return pd.Series()
    
    # Menghitung jumlah perjalanan per tipe kendaraan
    return df.groupby("vehicle_type").size().sort_values(ascending=False)

def mobility_trend(df):
    if df.empty:
        return pd.Series()
    
    # Resampling data berdasarkan interval 10 detik untuk melihat tren
    df_temp = df.set_index("timestamp")
    return df_temp["fare"].resample("10s").sum()

# ============================
# ANOMALY DETECTION
# ============================
def detect_anomaly(df):
    if df.empty:
        return pd.DataFrame()
    
    # Contoh: fare yang sangat tinggi (> 80.000) dianggap sebagai anomali
    return df[df["fare"] > 80000]