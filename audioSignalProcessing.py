import numpy as np 
import matplotlib.pyplot as plt

a = np.array([0,1,2,3,4,5,6,7,8,9])

b = a[::-1]

print(b)

plt.plot(b)
plt.show()