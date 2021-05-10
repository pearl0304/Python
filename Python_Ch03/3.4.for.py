# for

listset=[1,2,3,4,5]

for e in listset:
    print("원소 : ",e)

string1="방탄소년단"
for b in string1 :
    print(b)

listset1=["rm","jin","suga","jhope","jimin","v","jk"]
for c in listset1 :
    print(c)


num1=range(10)
print("num1 : ",num1)
num2=range(1,10)
print("num2 : ",num2)
num3=range(1,10,2)
print("num3 : ",num3)

for n in num1:
    print(n,end=" ")
print()

for n in num2:
    print(n,end=" ")
print()

for n in num3:
    print(n,end=" ")
print()

lst=[]
for i in range(10):
    r=random.randint(1,10)
    lst.append(r)
print("lst : ",lst)

for i in range(10):
    print(lst[i]*0.25,end=" ")

a=[random.randint(1,10)*0.25 for x in range(10)]  #축약 코드
print(a)

for i in range(2,10):
    print("==",i,"단==")

    for j in range(1,9):
        print("%d * %d = %d" % (i,j,i*j))


# 문장 단어 추출
string = """김석진은 잘생겼다 
김석진은 귀엽다 
김석진은 매력덩어리다"""

sents=[];
words=[];

for sen in string.split("\n"): #3번반복
    sents.append(sen)

    for wo in sen.split():
        words.append(wo)
print("문장 : ",sents)
print("문장수 : ",len(sents))
print("단어 : ",words)
print("단어수 : ",len(words))