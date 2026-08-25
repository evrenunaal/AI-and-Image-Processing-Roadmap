import pandas as pd


#CSV-JSON data: Dosya icerisinde bulunan verilerin cekilmesi

#CSV
df=pd.read_csv("cars_data.csv")

#print(df) #verilerin belli bir kismini ceker

print("-------------------------------")

#print(df.to_string()) #Verinin tum satir ve sutununun yazilmasi saglanir



#JSON
df=pd.read_json("airline_data.json")
print(df.to_string())