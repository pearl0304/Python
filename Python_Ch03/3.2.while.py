# 반복문

# while 반복문
cnt = tot =0
while cnt < 5 :
    cnt+=1
    tot+=cnt
    print(cnt,tot)

cnt2=tot2=0
dataset=[]

while cnt2 <100:
    cnt2+=1
    if cnt2 % 3==0 :
        tot2 +=cnt2
        dataset.append(cnt2)

print("1~100 사이 3의 배수의 합  : %d" % tot2)
print('dataset : ',dataset)

# loop (무한 루프)
numData = [] # 빈 list

while True :
    num = int (input("숫자 입력 : "))

    if num % 10 == 0 :
        print ("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)
