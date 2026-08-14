import numpy as np

#EXAMPLE 9: FILTERING
 #Belli bir kosula uyan ogeleri secme islemidir.Temelde bir kurala uymayan ogeler filtrelenir

ages= np.array([[21,17,19,20,16,30,18,65],
                [39,22,15,99,18,19,20,21]])

teenagers = ages[ages<18] #boolean indexing
adults = ages[(ages>=18) | (ages<65)]
seniors = ages[ages>=65]
evens = ages[ages % 2 ==0 ]#cift olanalar
odds = ages[ages % 2 !=0 ]#olasiliklardan bazilari olan tek olanlar

adults2 = np.where(ages>=18,ages,0)#where: elimdeki bir dizi var bu diziyi bozmadna sandece istediklerimi aradan cekmek isitiyorum bunu yaninda 3 kosul ile cekim yapilir
                                        #agesdan istenillen degerler ,gidilen dizi ,ardindan elemanda olmayanlar icin hangi deger dondurelecegi
                                        #dizinin asil yapisi korunur istenilen degerler gelir istenmeyen degerlerin bicimi gerceklesir


print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)
print(adults2)