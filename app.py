import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aplikasi Analisis Kualitas Air")

# Upload CSV
uploaded_file = st.file_uploader("Unggah file CSV data kualitas air", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Data Kualitas Air")
    st.dataframe(data)

    # Statistik
    rata_rata = data[['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']].mean()
    minimum = data[['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']].min()
    maksimum = data[['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']].max()

    st.subheader("Statistik Parameter")
    statistik = pd.DataFrame({
        'Parameter': ['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)'],
        'Rata-rata': rata_rata.values,
        'Minimum': minimum.values,
        'Maksimum': maksimum.values
    })
    st.dataframe(statistik)

    # Grafik
    st.subheader("Grafik Parameter Kualitas Air")
    fig, ax = plt.subplots(figsize=(10, 6))
    for kolom in ['pH', 'Suhu (°C)', 'DO (mg/L)', 'TDS (mg/L)']:
        ax.plot(data['Lokasi'], data[kolom], marker='o', label=kolom)

    ax.set_xlabel("Lokasi")
    ax.set_ylabel("Nilai")
    ax.set_title("Grafik Parameter Kualitas Air")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Download file hasil evaluasi
    hasil_csv = statistik.to_csv(index=False).encode('utf-8')
    st.download_button("Download Hasil Evaluasi (.csv)", hasil_csv, "hasil_evaluasi.csv", "text/csv")
