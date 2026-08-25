import pandas as pd

#SELECTION BY COLUM: DATA icerisinde bulunan istenilen sutundan veri cekimi

df = pd.read_csv("cars_data.csv",index_col="YEAR")

print(df["Make"].to_string())  #to_string ile tum yazdirmalar yapilir
print(df["Model"].to_string())

print(df[["Make", "Model","Size"]].to_string()) #birden fazla veriyi cekmek icin kullanilir


print("-------------------------------")

#SELLECTION BY ROW: DATA icerisinde bulunan istenilen satirlardan veri aktarimi

#print(df.loc[[1]].to_string()) #seklinde cagirim yapilabilir fakat bu cagirimlar genelde isimsel olarak belirtilmediklerinden kaynakli bu sekilde kullanim pek tercih edilmez

print(df.loc[2016:2015,["Make", "Model","Size"]].to_string())#Yukarida belirlemis oldugumuz index type i ile beraber istenilen satirlar ve sutunlarin ekrana yazdirmalari yapildi

print(df.iloc[0:11:2,0:2])# yukaridakilerin yani disinda belirli sayisal satirlar icin de arama yapilabilir

print("-------------------------------")

#EXERCISE

sellectcaryear = int(input("aradiginiz aracin yilini giriniz?"))

try:
    print(df.loc[sellectcaryear])
except KeyError:
    print(f"{sellectcaryear} is not in the dataframe")



















