import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import Normalize

data_transport = pd.read_csv("data/dataset_transportasi_50.csv")

#1 bar charrt jumlah perjalanan per moda transportasi
jumlah_perjalanan_per_moda = data_transport["moda_transportasi"].value_counts().sort_values(ascending = True)
print(jumlah_perjalanan_per_moda)

color = plt.cm.Reds(Normalize(vmin = jumlah_perjalanan_per_moda.min(), 
                               vmax = jumlah_perjalanan_per_moda.max())
                               (jumlah_perjalanan_per_moda.values))

# visualize
plt.figure (figsize = (10,5))
plt.title ("Jumlah Transportasi per Moda Transportasi")
plt.bar(jumlah_perjalanan_per_moda.index, jumlah_perjalanan_per_moda.values, color = color)
plt.xlabel ("Moda Transportasi")
plt.ylabel ("Jumlah Transportasi")

plt.savefig("output/graph/jumlah per moda transportasi 1.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

#1 line chart perjalanan per bulan
data_transport ["tanggal"] = pd.to_datetime(data_transport["tanggal"])
data_transport["bulan"] = data_transport ["tanggal"].dt.to_period("M").astype(str)
jumlah_perjalanan_per_bulan = data_transport.groupby("bulan").size()

# visualize
plt.figure (figsize = (10,5))
plt.title ("Jumlah Transportasi per Bulan")
plt.plot(jumlah_perjalanan_per_bulan.index, jumlah_perjalanan_per_bulan.values)
plt.xlabel ("Bulan")
plt.ylabel ("Jumlah")

plt.savefig("output/graph/jumlah per moda transportasi 2.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

#make it pie

plt.pie(jumlah_perjalanan_per_bulan.values, labels = jumlah_perjalanan_per_bulan.index, 
        autopct = "%.1f%%")
plt.title ("proporsi perjalanan per bulan")
plt.legend(loc = "best", bbox_to_anchor = (0.2, 0.2))

plt.savefig("output/graph/jumlah per bulan pie.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

## 4 box plot

#data_transport ["emisi_co2_pct"] = data_transport ["emisi_co2_kg"] * 100
plt.figure (figsize = (10,5))
plt.title ("Sebaran jarak transportasi dan Emisi")
plt.boxplot(data_transport[["jarak_km","emisi_co2_kg"]])
plt.ylabel ("Nominal")

plt.savefig("output/graph/tes box plot 2.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

# 5 Seaborn

plt.figure (figsize = (10,5))
sns.set_theme (style = "darkgrid")
sns.countplot(data = data_transport, x = "moda_transportasi")
plt.title ("Jumlah Transportasi per Moda Transportasi")
plt.xlabel ("Moda Transportasi")
plt.ylabel ("Jumlah Transportasi")

plt.savefig("output/graph/jumlah per moda transportasi 2.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

## 6 box plot sns

#data_transport ["emisi_co2_pct"] = data_transport ["emisi_co2_kg"] * 100
plt.figure (figsize = (10,5))
plt.title ("Sebaran jarak transportasi")
sns.boxplot(data_transport[["jarak_km", "durasi_menit"]])
plt.ylabel ("Nominal")

plt.savefig("output/graph/tes box plot 3.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

## 7 box plot sns
plt.figure (figsize = (10,5))
plt.title ("Biaya vs Jarak")
sns.scatterplot(data = data_transport,
            x = "jarak_km",
            y = "biaya_rp",
            size = "emisi_co2_kg")

plt.savefig("output/graph/tes reg plot 2.png")
plt.show() #sesudah show tidak dapat diutak atik lagi, termasuk edit gambar

