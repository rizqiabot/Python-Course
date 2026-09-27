import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title ("Visualisasi data transportasi")

#1. Load data
data_transport = pd.read_csv("data/dataset_transportasi_50.csv")
data_transport ["tanggal"] = pd.to_datetime(data_transport["tanggal"])
data_transport["bulan"] = data_transport ["tanggal"].dt.to_period("M").astype(str)
jumlah_perjalanan_per_bulan = data_transport.groupby("bulan").size()

sns.set_theme(style = "dark")

menu = st.sidebar.selectbox(
    "Pilih Laporan",
    [
        "Semua Data (Tabel)",
        "Jumlah Perjalanan Per Bulan",
        "Proporsi Perjalanan Per Bulan",
        "Jumlah Perjalanan Per Moda Transportasi",
        "Sebaran Jarak dan Durasi",
         "Hubungan Jarak, Biaya, dan Emisi CO₂",
    ]
)

if menu == "Semua Data (Tabel)":
    st.subheader ("Semua Data Transportasi")
    st.dataframe(data_transport)

elif menu == "Jumlah Perjalanan Per Bulan":
    fig, ax = plt.subplots(figsize = (10,5))
    sns.countplot(data = data_transport, x = "moda_transportasi")
    ax.set_title ("Jumlah Transportasi per Moda Transportasi")
    ax.set_xlabel ("Moda Transportasi")
    ax.set_ylabel ("Jumlah Transportasi")
    st.pyplot (fig)
    plt.close(fig)
    
elif menu == "Hubungan Jarak, Biaya, dan Emisi CO₂":
    fig, ax = plt.subplots(figsize = (10,5))
    sns.scatterplot(data = data_transport,
            x = "jarak_km",
            y = "biaya_rp",
            size = "emisi_co2_kg")
    ax.set_title ("Biaya vs Jarak vs Emisi")
    ax.set_xlabel ("Jarak (KM)")
    ax.set_ylabel ("Biaya (RP)")
    st.pyplot (fig)
    plt.close(fig)

elif menu == "Proporsi Perjalanan Per Bulan":
    fig, ax = plt.subplots(figsize = (10,5))
    ax.pie(jumlah_perjalanan_per_bulan.values, labels = jumlah_perjalanan_per_bulan.index, 
        autopct = "%.1f%%")
    ax.set_title ("proporsi perjalanan per bulan")
    ax.legend(loc = "best", bbox_to_anchor = (0.2, 0.2))

    st.pyplot (fig)
    plt.close(fig)

