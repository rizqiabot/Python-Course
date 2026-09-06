import pandas as pd
import numpy as np

#1. Load data
data = pd.read_csv("data/transportation_dirty.csv")

#2. EDA (Exploratory Data Analysis)
print("=" * 60)
print("COLUMN")
print("=" * 60)
print (data.shape)
print(data.info())
print(data.columns)
print ()

print("=" * 60)
print("STATISTIC DATA")
print("=" * 60)
print (data.describe())
print ()

print("=" * 60)
print("CHECK MISSING VALUE")
print("=" * 60)
print(data.isna().sum())
print ()

print("=" * 60)
print("CHECK DUPLICATE VALUE")
print("=" * 60)
print(data.duplicated().sum()) ## berarti ada xx baris yang isinya sama persis (duplicated)
print(data[data.duplicated()])
print ()
#print (data.duplicated(subset=["Day", "Person"]).sum()) -> Cari tahu duplicated value

print("=" * 60)
print("CHECK UNIQUE VALUE")
print("=" * 60)
print(data["city"].unique())
print ()

print("=" * 60)
print("CHECK UNIQUE VALUE")
print("=" * 60)
print(data["transport_mode"].unique())
print ()

# Cleansing
print("=" * 60)
print("REMOVE DUPLICATE VALUE")
print("=" * 60)
print("SEBELUM:", len(data))
data_clean = data.drop_duplicates().copy()
print("SESUDAH:", len(data_clean))
print()

print("=" * 60)
print("TRIM WHITESPACE")
print("=" * 60)

for kolom in data_clean.select_dtypes(include = "object").columns:
    data_clean[kolom] = data_clean[kolom].str.strip()
    data_clean[kolom] = data_clean[kolom].str.title()

data_clean["city"] = data_clean["city"].replace({
    "Jakrta":"Jakarta",
    "Jogja": "Yogyakarta"
})

data_clean["city"] = data_clean["city"].fillna("To be Checked")
data_clean["trip_date"] = pd.to_datetime(
    data_clean["trip_date"],
    errors = "coerce",
    dayfirst = True).astype("string")
data_clean["trip_date"] = data_clean["trip_date"].fillna("To be Checked")
data_clean = data_clean.fillna("To be Checked")


print("=" * 60)
print("CHECK AGAIN THE UNIQUE VALUE")
print("=" * 60)

print(data_clean["city"].unique())
print ()
print(data_clean["transport_mode"].unique())
print ()
print(data_clean["trip_date"].unique())
print()

data_check = data_clean[data_clean.isin(["To be Checked"]).any(axis=1)]
data_check.to_csv("output/transportation_to_be_check.csv", index = False)

