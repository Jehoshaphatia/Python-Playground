import matplotlib.pyplot as plt
import numpy as np

N = 64
k0 = 7
x = np.cos(2 * np.pi * k0 / N * np.arange(N)) 

x = np.array([ ])

for k in range(N):
     s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
     x = np.append(x, sum(x*np.conjugate(s)))

plt.plot (np.arange(N), abs(x))
plt.axis([0, N-1, 0, N])

plt.show()





