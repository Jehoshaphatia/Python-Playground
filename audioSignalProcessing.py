import numpy as np  #import numpy
import matplotlib.pyplot as plt #impport pyplot
from scipy.io.wavfile import read #import package for reading sound files
from scipy.io.wavfile import write #function for writing sound file

a = np.array([0,1,2,3,4,5,6,7,8]) 

b = a[::-1] #reverse of array a

print(b)

plt.plot(b) #ploting the array a
#plt.show()

(fs, x) = read('sound.wav') #read soud file called sound
print(fs) #print the sample rate of file
print(x) #print sound data
size = x.size
print(size)
#t = np.arange(size)/float(fs)
y = x[44100:45100]
plt.plot(y)
#plt.show()
write('testSound.wav', fs, y) #write a sound file called testSond


