
import numpy as np

#Example 6: Comparison operators
scores = np.array([91,55,100,73,82,64])
print(scores==100) #boolean deger dondururler True/False
print(scores<100)
print(scores>=60)
print(scores<60)

scores[scores < 60]=0 #filitreleme
print(scores)
