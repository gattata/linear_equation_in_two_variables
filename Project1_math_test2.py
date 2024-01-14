import random as rd
from sympy import Symbol, solve, Rational

print('解二元一次聯立方程式(每題20分，共5題)')
print('試題說明:請輸入x,y值，若題目無解，則任意輸入數字(不可空白或其他字母)')
name = input('請輸入姓名: ')
total = num = ans = score= 0
while(num != 5):#停止條件
    num += 1
    x = Symbol('x')
    y = Symbol('y')
    
    a1 = rd.randint(-5,5)
    a2 = rd.randint(-5,5)
    b1 = rd.randint(-5,5)
    b2 = rd.randint(-5,5)
    c1 = rd.randint(-5,5)
    c2 = rd.randint(-5,5)
    
    ex1 = a1*x + b1*y + c1
    ex2 = a2*x + b2*y + c2
    A = solve((ex1, ex2))
    print(f"Question {num}:\n{a1}x + {b1}y = {c1} \n{a2}x + {b2}y ={c2}")#隨機出題
    

    #測試題目:x=1,y=0
    # ex1 = x + y - 1 
    # ex2 = 2*x + y + - 2
    # A = solve((ex1, ex2))
    # print(f"Question {num}:\nx + y = 1 \n2x + y = 2")
    
    ansx_str = input("x: ")
    ansy_str = input("y: ")

    # 将用户输入的字符串转换为分数对象
    ansx = Rational(ansx_str)
    ansy = Rational(ansy_str)
    ansxy = {x: -ansx, y: -ansy}
    if ansxy == A:
        score += 20
        print('對')
        print(A)
        
    elif A == []:
        score += 20
        print('無解,送分')
    else:
        score += 0
        print('錯')
        print(A)

total += score 
print(f'姓名:',name,'成績:',total,'分','答對題數:',int(total/20),'/5')

input("按 Enter 退出...")