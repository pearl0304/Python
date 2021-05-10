# random 모듈

import random

# random 함수1
cnt = 0
while True:
    r=random.random()
    print(random.random())
    if r<0.01:
        break
    else:
        cnt+=1
print("난수 갯수 : ",cnt)

# random 함수2
# 이름 list에서 전체이름, 특정이름 출력 
names = ['김남준','김석진','민윤기']
print(names)
print(names[2])

# list에서 자료 유무 확인하기
if '민윤기' in names:
    print("민윤기 있음")
else :
    print("민윤기 없음")

# 난수 정수로 이름 선택하기
idx = random.randint(0,2)
print(names[idx])