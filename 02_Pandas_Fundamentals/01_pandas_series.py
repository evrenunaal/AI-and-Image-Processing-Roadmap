import pandas as pd
from pandas.core import series

#Example 1: SERIES
#Bir veri setinin tek boyutlu etiketli dizisi gibidir.Element tablosu gibi diyebiliriz.

data1= [100.1,102.2,104.3]
data2=["a","b","c"]
data3=[True,True,False]

series=pd.Series(data1)
series2=pd.Series(data2)
series3=pd.Series(data3)

print(series)
print(series2)
print(series3)

print("-------------------------------")


#Series INDEX :Serinin icerisinde siralama adimlarinin ismini degistirirken

data4=[26,43,71,11]
series4=pd.Series(data4,index=["apartment#1","b","c","d"])

print(series4)

print("-------------------------------")


#Series LOC : Serinin icerisindeki bir elemana direk ulaşmak icin

data5=[26,43,71,11]
series5=pd.Series(data5,index=["a","b","c","d"])
series5.loc["c"]=9 #degeri degistirmek icin kullandik

print(series5.loc["a"])
print(series5.iloc[1])#iloc ile beraber serinin ismi degismis olsa bile tam sayi konumu ile cagirim yapilabilir

print("-------------------------------")


#Series Filtering:Degerlerde belirlenlenen aralıklarda deger dondurme

data6=[27,40,13,16,2]
series6=pd.Series(data6,index=["a","b","c","d","e"])
print(series6[series6<15])

print("-------------------------------")


#Exercise-Dictionary

calories = {"Day 1": 1650,"Day 2":2300,"Day 3":2000}
series7=pd.Series(calories)
series7.loc["Day 3"]+=300

print(series7)
print(series7[series7<2000])


print("-------------------------------")





