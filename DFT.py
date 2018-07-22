import matplotlib.pyplot as plt
import numpy as np

x = np.array([])
 for k in range(N):
     s = np.exp(1j * 2 * pi * k / N * np.arange(N))
     x = np.append(x, sum(x*np.conjugate(s)))



