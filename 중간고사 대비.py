
"""변수 실습 1"""
"""
firstname="인헌"
lastname="김"

name=lastname+firstname

print(name)
"""

"""변수실습2"""
"""
y=10
x=20

print(x,y)
temp=x
x=y
y=temp

print(x,y)
"""

"""변수실습3"""
"""

F=float(input("화씨온도를 입력:"))

FtoC=(F-32)*(5/9)

print("화씨온도 %.1f도를 섭씨온도로 변환하면 %.1f도입니다."%(F, FtoC))
"""

"""변수 생각해보기"""
money=int(input("금액을 입력 : "))

오백원=money//500
백원=(money%500)//100
오십원=(money%100)//50
십원=(money%50)//10

print("오백원 개수 = %d" %오백원)
print("백원 개수 = %d" %백원)
print("오십원  개수 = %d" %오십원)
print("십원 개수 = %d" %십원)


