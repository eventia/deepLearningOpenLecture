import numpy as np
X_dot_W = np.array([[0,0,0],[10,10,10]])
B = np.array([1,2,3])

# B - broadcast
print(X_dot_W + B)


dY = np.array([
    [1,2,3],
    [4,5,6]])
dB = np.sum(dY, axis=0)
print(dB)


class Affine:
  def __init__(self, W, b):
    self.W = W
    self.b = b
    self.x = None
    self.dW = None
    self.db = None
    
  def forward(self, x):
    self.x = x
    out = np.dot(x, self.W) + self.b
    return out
  
  def backward(self, dout):
    dx = np.dot(dout, self.W.T)
    self.dW = np.dot(self.x.T, dout)
    self.db = np.sum(dout, axis=0)
	
	
	