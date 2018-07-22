import matplotlib.pyplot as plt
import numpy as np

N = 500
k = 3
n = np.arange(-N/2, N/2)
s = np.exp(ij * 2 * np.pi * k *n / N)


A = .8
f0 = 1000
phi = np.pi/2
fs = 44100 
t = np.arange (-0.002, .002, 1.0/fs)
x = A * np.cos (2 * np.pi * f0 * t * phi)

plt.plot(t, x)
plt.axis([-.002, .002, -.8, .8])
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.show()

