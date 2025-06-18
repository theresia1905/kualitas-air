import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv("data_air.csv")

# Menampilkan data di terminal (opsional)
print("Data Kualitas Air:")
print(data)

# Menghitung statistik sederhana
rata_rata = data[['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']].mean()
minimum = data[['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']].min()
maksimum = data[['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']].max()

# Simpan ke file hasil_evaluasi.csv
hasil = pd.DataFrame({
    'Parameter': ['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)'],
    'Rata-rata': rata_rata.values,
    'Minimum': minimum.values,
    'Maksimum': maksimum.values
})
hasil.to_csv("hasil_evaluasi.csv", index=False)
print("\n✅ Evaluasi selesai! Hasil disimpan ke 'hasil_evaluasi.csv'")

# Plot semua parameter dalam satu grafik
plt.figure(figsize=(10, 6))

# Loop untuk plotting
for kolom in ['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']:
    plt.plot(data['Lokasi'], data[kolom], marker='o', label=kolom)

plt.title("Grafik Parameter Kualitas Air")
plt.xlabel("Lokasi")
plt.ylabel("Nilai")
plt.legend()
plt.grid(True)

# Simpan grafik sebagai gambar
plt.savefig("grafik_kualitas_air.png", dpi=300)
plt.show()
