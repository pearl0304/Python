
#최대 최솟값 알고리즘 구성하기
import random

data=[]

for i in range(10):
    r=random.randint(1,100)
    data.append(r)
print(data)

#변수 초기화
vmax=vmin=data[0]

for i in data:
    if vmax>i:
        vmax=i
    if vmin<i:
        vmin=i
print('max = ', vmax, '\t min = ',vmin)

dataset=[5,10,18,22,35,55,75,103]
value=int(input("찾을 숫자를 입력하세요 : "))