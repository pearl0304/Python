# Ch02  파이썬 기본 도구 익히기

# 산술 연산자
num1=100
num2=20

add=num1+num2
print('add = ',add)

sub=num1-num2
print('sub = ',sub)

mul=num1*num2
print('mul = ',mul)

div=num1/num2
print('div = ',div)

div2=num1%num2
print('div2 = ',div2)

square=num1**2
print('square = ',square)

num3=10.3
num4=2.7
divdiv=num3//num4
print("divdiv = ", divdiv)

# 대입연산자
i=tot=10
i=i+1
tot=tot+i
print(i,tot)

print('출력1',end=' , ')
print('출력2',end=' , ')
print('출력3')
print('010','1234','5678',sep=" - ")

#스왑
v1,v2=100,200
v2,v1=v1,v2
print(v1,v2)

lst=[1,2,3,4,5]
v1,*v2=lst


*v1,v2=lst
print(v1,v2)