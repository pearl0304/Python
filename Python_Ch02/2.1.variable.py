#Ch02  파이썬 기본 도구 익히기

#자료형
var1 = "Hello pyhton"

print (var1)
print(id(var1)) #주소 표시

var1=100
print(var1)
print(id(var1))

var2=150.25
print(var2)
print(id(var2))

var3=True
print(var3)
print(id(var3))

import keyword
phython_keyword=keyword.kwlist
print(phython_keyword)

#자료형 변환

# 실수 -> 정수
a= int (10.5)
b=int(20.42)
add= a+b
print('add = ',add)

#정수 -> 실수
a=float(10)
b=float(20)
add2=a+b
print('add2 = ',add2)

# 논리형 -> 정수
print(int(True))
print(int(False))

#문자형 -> 정수
st='10'
print(int(st)**2)