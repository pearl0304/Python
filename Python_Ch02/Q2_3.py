fat=int(input("지방의 그램을 입력하세요 :  ") )
carb=int(input("탄수화물의 그램을 입력하세요 :  "))
pro=int (input("단백질의 그램을 입력하세요 :  "))
tol= fat*9+carb*4+pro*4
print("총칼로리 : ",tol,"cal")