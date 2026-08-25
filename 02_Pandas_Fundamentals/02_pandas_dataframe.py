import pandas as pd

#DATA FRAME: Satir ve sutunlardan olusan veri yapisidir. Exel dosyalarina benzer bir yapidadir

data ={"Name":["Spongebob","Patric","Squidward"], #"" icerisi satir [ici veriler]
       "Age":[21,22,23],}
df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"]) #D buyuk cunku yapici bir metot bir fonksiyon degil,index ile degısimler saglanir

print(df)

print(df.loc["Employee 1"]) #df.loc ile tam sayi konum belirlemesi ve ordaki veirinin cekilmesi yapılır
print(df.iloc[0]) #tam sayi ile deger okumada

print("-------------------------------")


#Add a new column : Yeni bir deger girişi nasil yapilir

df["Job"]=["Cook","N/A","Cashier"] #yeni sutun eklemesi yapilirken
print(df)

print("-------------------------------")


#Add a new row: Yeni bir satir nasil olusturulur

new_rows = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"}, #rowS sebebi çoklu ekleme yapmış olmamız tekte row
                             {"Name":"Eague","Age":40,"Job":"Worker"}],
                       index=["Employee 4","Employee 5"])
df= pd.concat([df,new_rows])
print(df)



