# Ch02  파이썬 기본 도구 익히기

# 문자열 색인
string = "Bangtan"
print(string[0]) #B
print(string[5]) #a
print(string[-1]) #n
print(string[-6])  #a

#문자열 연산
print("python" + " program")
print("python-",str(307),".exe")

print("-"*30)

# 문자열 처리 함수
oneLine = "this is one line string"
print("t 글자수 : ",oneLine.count('t'))

print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

multiLine="""this is
one
line
string"""
sent = multiLine.split('\n')
print('문장 : ',sent)

words = oneLine.split(' ')
print('단어 : ',words)

sent2 = ','.join(words)
print(sent2)


