import numpy as np

"""#VERI KUSURSUZ ISE
data = np.loadtxt("data_1", delimiter=",")
print(data)
"""
#VERI'DE KUSUR VAR ISE
data = np.genfromtxt("data_1", delimiter=",", skip_header=1, filling_values=-99) #"dosya", okuma fonksiyonu tab ise="\t", başlıksatırı, olmayan değer ataması
print(data)
