import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Data1.txt')

x = data[:,0]
y = data[:,1]

h = 0.1
N = 3/h

x1 = np.linspace(0, 10, N)
y1 = np.exp(x1)

plt.figure()
plt.plot( x1, y1, color = 'k')
plt.plot(x, y1, color = 'c', lw = 5)
plt.scatter(x, y, color = 'g')

plt.savefig('Graph.png')
