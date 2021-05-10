# 조건문

#if
score = int (input("점수 입력 : "))
if score>=85 and score<=100 :
    print("우수")
else :
    if score >=70:
        print("보통")
    else :
        print("저조")

# 중첩 조건문
score2 = int (input("점수 입력 : "))
grade =''

if score2 >= 85 and score2<=100:
    grade='우수'

elif score2 >=70:
    grade="보통"
else:
    grade="저조"

print('당신의 점수는 %d이고, 등급은 %s' %(score2,grade))

# 일반 조건문과 삼항 조건문
# 일반 조건문
num=9
result=0

if num>=5:
    result=num*2
else:
    result=num+2

print('result = ',result)

# 3항 연산자 변수 = 참 if(조건문) else 거짓
result2 = num*2 if num >=5 else num+2
print ('result2', result2)

