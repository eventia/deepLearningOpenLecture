# 1.6.1. 그래프그리기
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()

# 1.6.2. pyplot 기능 사용해보기
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='--', label='cos')
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()


# 1.6.3. 이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('..\images\lena.png')

plt.imshow(img)
plt.show()
