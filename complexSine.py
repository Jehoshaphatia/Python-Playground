import matplotlib.pyplot as plt
import numpy as np

N = 500
k = 3
n = np.arange(-N/2, N/2)
s = np.exp(ij * 2 * np.pi * k *n / N)

#complex sine wave
plt.plot(n, np.real(s))
plt.axis(-N/2, N/2-1, -1, 1)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()

