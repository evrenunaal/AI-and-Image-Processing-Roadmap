import numpy as np


#Example 2: SLISE
#array[start:end:step] -baslangıc degeri: bitis degeri(ne olursa olsun HARIC): adımlama-sıralama
# array[satır= ::  , sütun= :: ] & array[satır_başlangıç : satır_bitiş : satır_adım, sütun_başlangıç : sütun_bitiş : sütun_adım]

matris = np.array([
    [10, 11, 12, 13],  # Satır 0
    [20, 21, 22, 23],  # Satır 1
    [30, 31, 32, 33]])   # Satır 2

print(matris[:, :2]) # tum satirlari al sadece ilk iki sutunu getir
print(matris[:, 1:3]) # tum satirlari al 1.sutundan itibaren ilk iki sutunu getir
print(matris[1:3,1:3]) #1.satirdan itibaren 3. satira kadar ve 1.sutundan itibaren 3.sutuna kadar
print(matris[:, :2]) #tum satirlari al sutunlardan 2 ye kadar
print(matris[::2, ::2]) #satirlardan 2 serli olarak atla sutunlardan 2 serli olarak atla
print(matris[:,::-1]) #satirlarin tamamini al sutunlara tersten basliyarak al
print(matris[::-1,:]) #satirlara tersten basla sutunlarin hepsini al
print(matris[::-1,::-1]) #satirlara ve sutunlara tersten baslayarak yaz