import pandas as pd

#Data Cleaning = veri temizleme islemleri, eksik hatali veya alakasiz verilerin guncellenmesi duzenlenmesi icin kullanilir
#Pandan ile yapilan islemlerin yaklasik %75 i ozellikle veri temizligine yoneliktir

df = pd.read_csv("cars_data.csv")

# 1. DROP IRRELEVANT COLUMNS: Sutun kaldirma islemlerinde

df = df.drop(columns=["COMB (Le/100 km)","YEAR"])
print(df.to_string())
print("--------------------------------")

#2. HANDLE MISSING DATA :

#df=df.dropna(subset=["RATING"])#Icerisinde eksik deger veya hic deger bulundurmayan satirlarin cikarimi yapilabilir
#print(df.to_string())

df=df.fillna({"RATING":"NONE"}) #bu satirlari bulmak yerine bu satirlar yerine farkli fonksiyonlar kullanabiliriz bunun icin fillna {farkli aranan deger : yerine yazilacak}
print(df.to_string())
print("--------------------------------")

#3.FIX INCOSISTENT VALUES:Satir ve sutunlardaki degerlerin degistirimi yapilirken kullanilir

df["Unnamed: 5"]=df["Unnamed: 5"].replace({"A1":"A2"})
print(df.to_string())
print("--------------------------------")


#4.STANDARDIZE TEXT :Metinleri standartlastirmak icin kullanilir

df["Make"] = df["Make"].str.lower()
print(df.to_string())
print("--------------------------------")

#5.FIX THE DATA TYPES: Verilerin turlerinin donusturulmesi yapilabilir

df["(kW)"] = df["(kW)"].astype(float)#float turunden deger degisimi yapildi
print(df.to_string())
print("--------------------------------")

#6.Remove duplicate values: Ayni olan verilerin silinmesi yada kaldirilmasi saglanir

df=df.drop_duplicates() #Veri setinde ayni bulunan elemanlarin silinmesi icin
print(df.to_string())





