import random

member=["김남준","김석진","민윤기","정호석","박지민","김태형","전정국"]
name=input("참가자 이름을 입력하세요 : ")

if name in member :
    print("참가자입니다")
else :
    print("참가자 목록에 '%s'라는 이름은 없습니다"%(name))

idx= random.randint(0,6)
print(member[idx])

i=0
num=[]
while i < 8 :
    i=i+1
    idx = random.randint(0, 500)
    num.append(idx)
print(num)

print("로또")

#컴퓨터 난수 만들기
comNum=[]

for i in range(6):
    r=random.randint(1,46)
    comNum.append(r)


#사용자 숫자 입력받기

print("컴퓨터 번호 : ",comNum)
print("사용자 번호 : ",userNum)

#매칭하기

n=int(input("숫자 입력"))
for i in range(1,10):
    print(n,'*',i,'=',n*i)


a,b=input().split(' ')
a=int(a)
b=int(b)





