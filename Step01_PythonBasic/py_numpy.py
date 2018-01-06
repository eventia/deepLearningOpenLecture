
# 1.5.1. numpy 가져와서 사용
import numpy as np

"""
# 1.5.2. 배열 생성
x = np.array([1.0, 2.0, 3.0])
# print(x)
# print(type(x))


# 1.5.3. numpy 배열의 산술연산
y = np.array([2.0, 4.0, 6.0,])
print(x+y)
print(x-y)
print(x*y)
print(x/y)


# 1.5.4. numpy 의 N 차원 배열
A = np.array([[1,2], [3,4]])
print("A = \n", A)
print(A.shape)
print(A.dtype)

B = np.array([[3,0],[0,6]])
print("B = \n", B)
print("A+B=\n", A+B)
print("A*B=\n", A*B)

print("A*10 = \n", A*10)


# 1.5.5. 브로드캐스트
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)
"""

# 1.5.6. 원소접근
X = np.array([[51,54],[14,19],[0,4]])
print(X[0])
print(X[0][0])

X = X.flatten()    # [51,54,14,19,0,4]
print(X)

X1 = X[np.array([0,2,4])]  # X[0], X[2], X[4] 만 선택
print(X1)

X2 = X>15    # [True, T, F, T, F, F]
print(X2)
X3 = X[X2]
print(X[X>15])
print(X3)
