# 비순서 자료 구조형 (set, dict)

# set
# 여러 개의 자료를 비순서로 적재하는 가변 길이 비순차 자료 구조를 생성하는 클래스
# list와 달리 공통의 영역에 값들이 적재

# set 특징
# 1. 비순서 자료구조를 갖는 열거형객체 생성
# 2. 중괄호 안에 콤바를 이용하여 원소 구분
# 3. ★중복 허용 안됨
# 4. 순서가 없어서 색인을 사용할 수 없음
# 5. 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합 연산 등이 가능

# 중복 불가
print('중복불가')
s={1,2,2,3,4,5,6,6,6}
print(s)
print(len(s))

# 요소 반복
for d in s :
    print(d, end=' ')
print()

# 집합관련 함수
print('집합')

s2 = {3,6}
print('합집합')
print(s.union(s2))
print('-'*40)
print('차집합')
print(s.difference(s2))
print('-'*40)
print('교집합')
print(s.intersection(s2))
print('-'*40)

# 추가, 삭제, 함수
s3 = {1,3,5}
print(s3)
print('-'*40)
print('원소 7 추가')
s3.add(7)
print(s3)
print('-'*40)
print('원소 3 삭제')
s3.discard(3)
print(s3)
print('-'*40)

# 중복 제거
print('중복제거')
# 중복 원소를 갖는 리스트
EngWords = ['actually','again','almost','almost','angry','animal','actually']
print(EngWords)
print('EngWords list 길이 : ',len(EngWords))
# 중복 원소 제거
# 'list -> set'
EngWords1 = set(EngWords)
# 'set->list'
EngWords2=list(EngWords1)
print(EngWords2)
print('-'*40)


# dict
# 사전(dictionary)형으로 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료 구조를 생성하는 클래스
# set 클래스와 동일하게 공통의 영역에 원소에 적재
# Key 값에 Value  저장 -> 키를 통해 값을 참조하는 형식
# 특징
# 1. 사전 형식으로 비순서 자료구조를 갖는 열거형객체를 생성
# 2. {'Key':'Value'}의 쌍으로 원소를 입력하고, 콤마를 이용하여 원소 구분
# 3. Key : 중복 허용 안됨 / Value : 중복 허용 가능
# 4. index 대신에 Key를 이용하여 Value 참조
# 5. 원소, 수정, 삭제, 추가 가능

#dict 생성
print('dict 생성 방법1')
btsDic = dict(key1='김남준',key2='김석진',key3='민윤기')
print(btsDic)
print('-'*40)
print('dict 생성방법2')
Jk = {'name' :'전정국','age':25,'addr':'부산시'}
print(Jk)
print('JK 본명 : ',Jk['name'])
print(type(btsDic), type(Jk))
print('-'*40)

# 원소 수정, 삭제, 추가
print('원소 추가')
Jk['addr']='서울시'
print(Jk)
print('-'*40)

print('원소 삭제')
del Jk['addr']
print(Jk)
print('-'*40)
# 요소 반복
print('요소반복')
for key in Jk.keys() :
    print(key)
print('-' * 40)
for v in Jk.values() :
    print(v)
print('-'*40)
for i in Jk.items() :
    print(i)
print('-'*40)

# 단어 출현빈도 수 구하기
print('단어 데이터 셋 준비')
charset = ['beginner','beside','always','best','best','beside','always']
wc={} #set : 중복 방지

#get 함수 : 해당 값 가져오기 (숫자, 문자 가능). 해당값이 없으면 디폴트 0을 가져옴
print('get 함수 이용')
for key in charset :
    wc[key] = wc.get(key,0)+1
print(wc)
# 해석 : charset에 잇는 모든 단어들의 초기 key 값은 0
# for문이 1회 돌면 모든 단어의 key값은 1
# 중복 단어가 있다면 key 값은 계속 증가

