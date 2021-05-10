# Ch02  파이썬 기본 도구 익히기

# 표준입력장치

# 문자형 숫자 입력
num=input("숫자 입력  :  ")
print('num type : ',type(num))
print('num  : ',num)
print('num  : ',num*2)

# 문자형 숫자를 정수형으로 변환
num1= int (input("숫자 입력 : "))
print('num1 = ',num1*2)

# 문자형 숫자를 실수형으로 변환
num2 = float(input("숫자 입력 : "))
result=num1+num2
print('result =  ',result)

print("value = ",10+20+30+40+50)

# sep 인수 : 값과 갑을 특수문자로 구분
print("010","1234","5678",sep="-")

# end 인수 : 값을 출력 후 줄바꿈 수행
print("value = ",10, end=", ")
print("value = ",20)

# format 양식
print("원주율 = ", format(3.14159,"8.3f"))
print("금액 = ", format(10000,"10d"))
print("원주율 = ", format(125000,"3,d"))

# 양식문자 인수 : print ("양식문자" % (값))
name="김석진"
age=30
price=125.456
print("이름 : %s, 나이 : %d, data = %.2f" %(name,age,price))

# 외부상수 출력
print("이름 : {}, 나이 : {}, data={}".format(name,age,price))
print("이름 : {1}, 나이 : {0}, data={2}".format(age,name,price))

uid = input("id input : ")
query = f"select * from memver where uid = {uid}"
print(query)