weight=int(input("짐의 무게는 얼마입니까? : "))

if weight <10 :
    print("수수료가 없습니다")
else :
    print("수수료는 10,000원입니다")

weight=int(input("짐의 무게는 얼마입니까? : "))

if weight <10 :
    print("수수료가 없습니다")
else :
    price=(weight//10)*10000
    print("수수료는 %d원입니다"%(price))