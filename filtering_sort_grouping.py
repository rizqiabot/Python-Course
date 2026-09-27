import pandas as pd

data_transport = pd.read_csv("data/dataset_transportasi_50.csv")

#filtering
# 1. Menampilkan data transportasi yang tujuan perjalanannya ke Jakarta

filter_jakarta = data_transport[data_transport["kota"] == "Jakarta"]
print("Filter Jakarta:")
print (filter_jakarta.to_string(index=False))
print ()

#2. Menampilkan data yang biayanya antara 15000 - 30000

filter_biaya = data_transport[(data_transport["biaya_rp"] >15000) & (data_transport["biaya_rp"] <30000)]

print("Filter Biaya:")
print (filter_biaya.to_string(index=False))
print ()

# 3 Menampilkan data yan moda transportasinya Bus atau Kereta

#filter_moda = data_transport[(data_transport["moda_transportasi"].str.lower() == "bus") | (data_transport["moda_transportasi"].str.lower() == "kereta")]

## bisa juga

filter_moda = data_transport[(data_transport["moda_transportasi"].str.lower().isin(["bus","kereta"]))]

print("Filter moda:")
print (filter_moda.to_string(index=False))
print()

# 4 Menampilkan data yang bukan moda transportasinya Bus atau Kereta

filter_bukan_moda = data_transport[~(data_transport["moda_transportasi"].str.lower().isin(["bus","kereta"]))]

print("Filter yang bukan moda:")
print (filter_bukan_moda.to_string(index=False))
print()

# 5. Menampilkan data transportasi antara tanggal 5 Januari 2026 - Agustus 2026

data_transport["tanggal"] = pd.to_datetime(data_transport["tanggal"]) #convert ke dalam format date / tanggal

#filter_tanggal = data_transport[data_transport["tanggal"].between("2026-01-01", "2026-08-31")]
filter_tanggal  = data_transport[data_transport["tanggal"].dt.month == 3]
print("Filter tanggal:")
print (filter_tanggal.to_string(index=False))
print()

# 6 Menampilkan data yang biaya transportasinya blank (N/A)

filter_biaya_na = data_transport[data_transport["biaya_rp"].isna()]

print("Filter biaya na:")
print (filter_biaya_na.to_string(index=False))
print()

# Sorting

# 1. menampilkan data transportasi diurutkan berdasarkan biaya

sort_biaya = data_transport.sort_values(by = "biaya_rp")
print(sort_biaya.to_string(index = False))
print ()

# 2. menampilkan data transportasi diurutkan berdasarkan biaya

sort_biaya = data_transport.sort_values(by = "biaya_rp", ascending = False)
print(sort_biaya.to_string(index = False))
print ()

# 3. sort multi columns (menampilkan data transportasi diurutkan berdasarkan kota dan biaya termurah)

sort_kota_biaya = data_transport.sort_values(by = ["kota","biaya_rp"])
print(sort_kota_biaya [["kota","biaya_rp"]].to_string(index = False))
print ()

# 4. sort multi columns (menampilkan data transportasi diurutkan berdasarkan kota dan biaya termahal)

sort_kota_biaya = data_transport.sort_values(by = ["kota","biaya_rp"], ascending = [True,False])
print(sort_kota_biaya [["kota","biaya_rp"]].to_string(index = False))
print ()

#5. Menampilkan 3 data transportasi yang rating tertinggi

top_3_rating = data_transport.sort_values(by = "rating", ascending = False).head(3)
print(top_3_rating [["kota","biaya_rp","rating"]].to_string(index = False))
print ()

# Grouping

#1. Menampilkan jumlah perjalanan per moda transportasi
group_by_moda = data_transport.groupby("moda_transportasi")["trip_id"].count()
print(group_by_moda)
print()

#2. Rata-rata biaya per moda
average_per_moda = data_transport.groupby("moda_transportasi")["biaya_rp"].mean()
print(average_per_moda)
print()

#3. Rata-rata biaya per moda
average_per_moda = data_transport.groupby("moda_transportasi")["biaya_rp"].mean()
print(average_per_moda)
print()

#4. Group by kota dan moda transport, mau tau rata rata dan sum biaya
group_by_kota_moda = data_transport.groupby(["kota","moda_transportasi"])["biaya_rp"].agg(["mean","sum","count"])

print(group_by_kota_moda.to_string())
print ()

#5. Group by kota dan moda transport, mau tau rata rata dan sum biaya
group_by_kota_moda = data_transport.groupby(["kota","moda_transportasi"]).agg({
    "biaya_rp": ["mean", "sum", "count"],
    "rating": ["mean"]
    })

print(group_by_kota_moda.to_string())
print ()

top_3_biaya = group_by_kota_moda.sort_values(by=("biaya_rp","sum"), ascending = False).head(3)
top_3_rating = group_by_kota_moda.sort_values(by=("rating","mean"), ascending = False).head(3)

final_result = pd.concat([top_3_biaya, top_3_rating], keys = ["Top 3 Total Biaya", "Top 3 Rating"])

print(final_result)
