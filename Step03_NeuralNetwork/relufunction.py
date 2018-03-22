import numpy as np
import matplotlib.pylab as plt

def relu_function(x):
    return np.maximum(0,x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu_function(x)

plt.plot(x,y)

plt.ylim(-5, 5)
plt.show()
