import numpy as np
import matplotlib.pyplot as plt

Data = np.loadtxt('Data2.txt')

x = Data[:,0]
y = Data[:,1]
z = Data[:,2]

h = 0.1
N = 10/h

x1 = np.linspace(0, 10, N)
y2 = np.cos(x1)

plt.figure()

plt.scatter(x, y, color = 'k')
plt.plot(x1, y2 , color = 'g')
plt.plot(y,y2, color = 'c')

plt.savefig('Graph2.png')

