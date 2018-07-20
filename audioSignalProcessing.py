import numpy as np  #import numpy
import matplotlib.pyplot as plt #impport pyplot

a = np.array([0,1,2,3,4,5,6,7,8]) 

b = a[::-1] #reverse of array a

print(b)

plt.plot(b) #ploting the array a
plt.show()