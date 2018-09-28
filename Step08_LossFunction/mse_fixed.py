import numpy as np
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

def mean_square_error(y,t):
    return (np.sum((y-t)**2)/len(y))

y1 = [.1, .05, .1, .0, .05, .1, .0, .6, .0, .0]
mean_square_error(np.array(y1),np.array(t))

print(t)
print(y1)
print(np.array(t)-np.array(y1))
print((np.array(t)-np.array(y1))**2)
print(sum((np.array(t)-np.array(y1))**2))
print(sum((np.array(t)-np.array(y1))**2)/len(y1))

y2 = [.1, .05, .6, .0, .05, .1, .0, .1, .0, .0]
mean_square_error(np.array(y2),np.array(t))
