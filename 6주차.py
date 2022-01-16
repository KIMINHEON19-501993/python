"""
def hello(name):
	print("안녕?",name)
"""

"""
def total(a,b):
	print(a+b)
"""

"""
def avg(a,b,c):
	return (a+b+c)/3
"""


"""
def Print0ptions():
    print('C or c : 섭씨온도에서 화씨온도로 변환')
    print('F or f : 화씨온도에서 섭씨온도로 변환')
    print('Q or q : 종료')

def CtoF(c_temp):
    return c_temp * 9 / 5 +32

def FtoC(f_temp):
    return (f_temp - 32) * (5 / 9)

choice='a'

while choice != 'q' or choice != 'Q' :
    Print0ptions()
    choice = input('메뉴에서 선택하세요 : ')

    if choice == 'c' or choice == 'C' :
        temp = float(input('섭씨온도 : '))
        ftemp = CtoF(temp)
        print("화씨온도 : %.1f" %ftemp)
    elif choice == 'f' or choice == 'F' :
        temp =  float(input('화씨온도 : '))
        ctemp = FtoC(temp)
        print("섭씨온도 : %.1f" %ctemp)
"""

"""
def Length(r):
    return 2 * 3.14 * r

def Area(r):
    return 3.14 * r**2

radius = int(input("원의 반지름을  입력하세요 : "))

while radius <= 0 :
    radius = int(input("양수를 입력하세요 : "))

length = Length(radius)
area = Area(radius)

print("원의 둘레 : %2.f, 원의 넓이 : %2.f" %(length, area))
"""




        
