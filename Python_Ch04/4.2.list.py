# list

# list 객체 특징
# 1. 순서 자료구조를 갖는 열거형객체를 생성할 수 있음
# 2. 대괄호안에 콤마를 이요하여 순서대로 값을 나열
# 3. 자료형 : 숫자형, 문자형, 논리형 함께 사용 가능
# 4. index를 이용하여 자료 참조 가능
# 5. 슬라이싱, 연결, 반복, 요소 검사 가능
# 6. 값을 추가, 삽입, 수정, 삭제 가능

# 단일 list
lst = [1,2,3,4,5]
print(lst)
print(type(lst))
for i in lst :
    print(lst[:i]) #i전까지

print('-'*40)

# 리스트 색인
x= list (range(1,11))
print(x)
print(x[:5])
print(x[:-5])
print('-'*40)
print('index 2씩 증가')
print(x[::2]) #홀수 색인
print(x[1::2]) #짝수 색인

print('-'*20)
# 중첩 list
# 단일 리스트 객체 생성
a = ['박지민','김태형','전정국']
print('a : ',a)
# 중첩 리스트 객체 생성 
b= [10,20,a,5,True,'방탄사랑해'] # a=리스트임! list 형태의 a가 출력됨
print(b)
print(b[0])
print(b[2]) # list a 출력
print(b[2][0])
print(b[2][1:])

print('-'*20)

# 추가, 삭제, 수정, 삽입
# (1) 단일 리스트 객체 생성
bts = ['rm','jin','suga','jhope','jimin','v','jk']
print(bts)
print("bts 리스트 길이 : ",len(bts))

print('-'*40)

# (2) 리스트 원소 추가
bts.append('bighit')
print(bts)

print('-'*40)

# (3) 리스트 원소 삭제
bts. remove('bighit')
print(bts)

print('-'*40)

# (4) 리스트 원소 삽입
bts.insert(0,'BTS')
print(bts)

print('-'*40)

# (5) 리스트 결합
x=[1,2,3,4,5]
y=[1.5,2.5]
z=x+y
print(z)

print('-'*40)

# (6) 리스트 확장
x.extend(y)
print(x)

print('-'*40)

# (7) 리스트 추가
x.append(y)
print(x)

print('-'*40)

# (8) 리스트 두 배 확장
print('리스트 두 배 확장')
lst=[1,2,3,4,5]
result=lst*2
print(result)

print('-'*40)

# 리스트 정렬과 요소 검사
#오름차순
print('오름차순')
result.sort()
print(result)

print('-'*40)

#내림차순
print('내림차순')
result.sort(reverse=True)
print(result)

print('-'*40)

# 리스트 요소검사
import random
r=[]
for i in range(5) :
    r.append(random.randint(1,5))
print(r)
if 4 in r :
    print('4 있음')
else:
    print('4없음')

print('-'*40)

# List comprehension : list 안에서 for 와 if를 사용하는 문법
# 형식 : 변수 = [실행문 for 변수 in 열거형 객체]
x=[2,4,1,5,7]
lst1 = [i**2 for i in x]
print(lst1)

# 형식 : 변수 = [실행문 for 변수 in 열거형 객체 if 조건식]
num= list(range(1,11))
lst2 = [i*2 for i in num if i%2==0]
#1~10까지 범위에서 값에 2곱한 값 구하기
print(lst2)

print('-'*40)
# 튜플 
# 튜플 특징 
# 1. 순서 자료구조를 갖는 열거형 객체를 생성할 수 있음
# 2. 소괄호 안에 콤마를 이용하여 순서대로 값을 나열함
# 3. 값의 자료형은 숫자형, 문자형, 논리형 등을 함께 사용 가능
# 4. index을 이용하여 자료를 참조, 슬라이싱,연결, 반복, 요소 검사 가능
# 5. ★ 읽기전용 = > 추가, 삽입, 수정, 삭제 불가능
# 6. 리스트보다 처리속도가 빠름
print('튜플')
# 원소가 한 개인 경우
t=(10, )
print(t)

# 원소가 여러개인 경우
t2 = ('김남준','김석진','민윤기','정호석','박지민','김태형','전정국')
print(t2)

#튜플 색인
print('t2 1번째 원소 : ',t2[0])
print('t2 2~5번째 원소 : ',t2[1:4])  #=> 튜플 형식으로 출력
print('t2 마지막 원소 : ',t2[-1])

# 요소반복
for i in t2 :
    print(i, end=' ')
print()
# 요소반복
if '정호석' in t2 :
    print('홉있음')
else :
    print('홉없음')

print('-'*40)

# 튜플 자료형 변환
print('튜플 자료형 변환')
lst4 = list(range(1,6))
t3=tuple(lst4)
print(t3)

# 튜플 관련 함수
print(len(t3), type(t3))
print(t3.count(3)) #원소 몇 개 있는지
print(t3.index(4)) #원소 위치 반환
