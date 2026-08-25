import pandas as pd

#FILTERING: Temel veri cercevesinde calısırken bır kosula uyan satirlari saklamak icin


df = pd.read_csv("cars_data.csv")

fast_cars = df[df["(kW)"] >=100]
leaskm_cars = df[df["(km)"] <=250]
print(fast_cars.to_string())
print("-------------------------------")
print(leaskm_cars.to_string())
print("-------------------------------")
my_cars = df[(df["(kW)"] >=100)&
             (df["(km)"] <=250)]
print(my_cars.to_string())