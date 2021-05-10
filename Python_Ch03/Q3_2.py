# 누진세 구하기
wh=int(input("전기 사용량을 입력하세요 : "))
g1=100*52 #첫번째 누진 - 두번째 구간부터
g2=100*88.5 #두번째 누진
g3=100*127.8 #세번째 누진
g4=100*184.3 #네번째 누진
g5=100*274.3 #다섯번째 누진


if wh < 100 :
    basic1 = 330 #기본요금
    c1=basic1+wh*52 #전기 사용 요금 = 전기사용량 *52
    print("전기요금 : %d원"%(c1))
    tax=int(c1*0.09)
    print("세금 : %d원"%(tax))


elif wh >=100 and wh<200 :
    basic2=660
    p2=(wh-100)*88.5
    c2=basic2+g1+p2
    print("전기요금 : %d원" % (c2))

elif wh>=200 and wh<300 :
    basic3=1130
    p3=(wh-200)*127.8
    c3=basic3+g1+g2+p3
    print("전기요금 : %d원" % (c3))

elif wh>=300 and wh<400 :
    basic4=2710
    p4=(wh-300)*127.8
    c4=basic4+g1+g2+g3+p4
    print("전기요금 : %d원" % (c4))

elif wh>=400 and wh<500 :
    basic5=5130
    p5=(wh-400)*274.3
    c5=basic5+g1+g2+g3+g4
    print("전기요금 : %d원" % (c5))

elif wh>=500:
    basic6=9930
    p6=(wh-500)*494.0
    c6=basic6+g1+g2+g3+g4+g5
    print("전기요금 : %d원" % (c6))