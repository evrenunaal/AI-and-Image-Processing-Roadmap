import numpy as np


#EXAMPLE 10: RANDOM NUMBERS

rng=np.random.default_rng(seed=1) #baslandıgıc degeri vererek ayni sayilari elde edersin
print(rng.integers(low=1,high=102,size=4)) #en dusuk en yuksek kac tane
print(rng.integers(low=1,high=102,size=(4,3)))

np.random.seed(seed=1)#tohum degeri
print(np.random.uniform(low=1,high=102,size=(4,3))) #uniform ile her degerin secilme sansı esıt


rng2=np.random.default_rng()
array=np.array([1,2,3,4,5])
rng2.shuffle(array) #dizinin elemanlarinin rastgele karistirilmasini saglar
print(array)

fruits=np.array(["apple","banana","orange","mango","pineapple"])
fruits=rng.choice(fruits,size=(3,3))
print(fruits)










































