# 복사 (얕은 복사 / 깊은 복사)

# 얕은 복사 : 주소 일치 -> 값이 바뀌면 연결된 모든 값이 다 변경
# 깊은 복사 : 주소 다름 -> 무늬만 같음. 서로 전혀 영향을 미치지 않음

# 얕은 복사 
print('얕은 복사')
name = ['홍길동','이순신','강감찬']
print('name address', id(name))

name2 = name
print('name2 address', id(name2))

print(name)
print(name2)
print('-'*40)

# 원본 수정
print('원본 수정')
name2[0] = "김길동"
print(name)
print(name2)

# 깊은 복사
import copy
name3 = copy.deepcopy(name)


print('name addr: ',id(name))
print('name3 addr: ',id(name3))

name[1]="이순신장군"
print('name : ',name)
print('name3 : ',name3)

