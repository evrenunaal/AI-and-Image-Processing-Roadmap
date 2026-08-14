import numpy as np


#Example 8:AGGREGATE FUNCTIONS
#verileri ozetler ve genelde tek bir deger dondurur

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.sum(array))#dizinin toplami
print(np.mean(array))#dizinin ortalaması
print(np.std(array))#standar sapması
print(np.var(array))#dizinin varyansını hesaplamak
print(np.min(array))#min deger
print(np.max(array))#max deger
print(np.argmin(array))#min deger icin konum bilgisi
print(np.argmax(array))#max deger icin konum bilgisi
print(np.median(array))#medyan degeri


print(np.sum(array,axis=0))#diyelim ki satir toplamini istedik bunu dizi toplamindan istenilen yer cekildi
print(np.sum(array,axis=1))