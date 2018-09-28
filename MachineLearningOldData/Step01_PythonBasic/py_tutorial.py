# 1.3.1 산술연산
1+2
5*4
5**4
15/4
15//4
print(1+2)


# 1.3.2 자료형
print(type(10))
print(type(2.718))
print(type("10"))

# 1.3.3 변수
x = 10
print(x)
x = 100
print(x)

y = 3.14
print(x*y)
print(type(x*y))

# 1.3.4 리스트
a = [1,2,3,4,5]
print(a)
print(len(a))
print(a[0],a[4],a[-1])
a[4] = 99
print(a)

print(a[0:3])
print(a[1:])
print(a[:3])
print(a[:-1])

# 1.3.5 딕셔너리
me = {'height':180}
print(me['height'])
me['weight'] = 74
print(me)

# 1.3.6 bool
hungry = True
sleepy = False
print(type(hungry))
print(hungry)
print(not hungry)

# 1.3.7 if문
hungry = not hungry
if hungry:
    print("i'm hungry")
else :
    print("i'm not hungry")
    print("i'm sleepy")

# 1.3.8 for문
for i in [1,20,3]:
    print(i)

for i in range(10):
    print(i)

# 1.3.9 함수
def hello():
    print("hello world")

hello()

def hello(object):
    print("Hello " + object +"!")

hello("cat")
# hello()  ## 에러발생
