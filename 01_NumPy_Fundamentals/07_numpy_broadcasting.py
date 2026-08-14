import numpy as np
#Example 7:BROADCASTING
#Broadcasting icin onemli olan 2 kural vardir bu kurallardan birisi her iki dizinin boyutlarinin ayni olmasi veya
#bu boyutlardan birinin boyutunun 1 olmasi gerekmekte

array1= np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
array2=np.array([[1,2],[2,3],[3,4],[4,5]])
print(array1.shape)
print(array2.shape)

#Exercize

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1.shape)
print(array2.shape)

print(array1*array2)