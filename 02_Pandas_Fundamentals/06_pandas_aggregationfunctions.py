import pandas as pd
from pandas.core.groupby import groupby

# AGREEGATION FUNCTIONS : Verileri tek bir ozet degere indirgemek icin kullanilir.Verileri ozetlemek ve analiz etmek icin groupby() fonksiyonun kullaniyoruz/
df= pd.read_csv("cars_data.csv")

print(df.mean(numeric_only=True)) #numeric olan satir ve sutunlarin ortalama degerlerini bulur

print("-------------------------------")

print(df.sum(numeric_only=True)) #tum sayilarin topalmi

print("-------------------------------")

print(df.min(numeric_only=True)) #min degerler

print("-------------------------------")

print(df.max(numeric_only=True)) #max degerler

print("--------------------------------")

print(df.count(numeric_only=True)) #satirsal elemanlarin sayisini verir




# Bu degerlerin hepsi toplama fonksiyonlari ile yapilir

print("--------------------------------")

print(df["CITY (Le/100 km)"].mean()) #numeric olan tek bir degerin ortalama degerlerini bulur

print("-------------------------------")

print(df["COMB (Le/100 km)"].sum()) #tum sayilarin topalmi

print("-------------------------------")

print(df["RATING"].min()) #min degerler

print("-------------------------------")

print(df["(km)"].max()) #max degerler

print("--------------------------------")

print(df["(kW)"].count()) #bos elemanlarin sayisini verir


#groupby() fonksiyonu kullanimi


group = df.groupby("Make")

print(group["Model"].mean())

print("--------------------------------")

print(group["(km)"].sum())

print("--------------------------------")

print(group["(km)"].min())

print("------------------------------")

print(group["(km)"].max())

print("------------------------------")

print(group["(km)"].cout())




