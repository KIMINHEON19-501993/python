"""
###학점 구하기###
kor =int(input("국어 점수를 입력 하세요"))
mat =int(input("수학 점수를 입력 하세요"))
eng =int(input("영어 점수를 입력 하세요"))
sci =int(input("과학 점수를 입력 하세요"))

avg = (kor + mat + eng + sci)/4
print("평군 : %2.f" %avg)

if avg >= 90 :
    print("학점 : A 입니다")
elif avg >= 80:
    print("학점 : B 입니다")
elif avg >= 70:
    print("학점 : C 입니다")
elif avg >= 60:
    print("학점 : D 입니다")
else avg < 60:
    print("학점 : F 입니다")
"""

"""
A=int(input("정수를 입력하시오"))

if A>0:
    print("입력된 정수는 양수 입니다.")
elif A==0:
    print("입력된 정수는 0 입니다.")
else :
    print("입력된 정수는 음수 입니다.")
"""

"""
for i in range(0,5,1):
    print("python",end='')

for a in range(0,5,1):
    print("a=",a,"김인헌 입니다.")
"""

"""
total=0

for i in range(1,101,1):
    total=total+i

print(total)
print(i)
"""


"""
dan=int(input("출력할 단을 입력하세요: "))

for i in range(1,10,1):
    print("%d * %d = %d" %(dan, i, dan*i),end=)
"""

"""
### 짝수홀수 합 ###
num1=0
num2=0

for i in range(1,101,1):
    if i % 2 ==0:
        num1=num1+i
    else :
        num2=num2+i
print("짝수합 = %d" %num1)
print("홀수합 = %d" %num2) 
"""


"""
num= int(input("정수 하나를 입력하세요: "))
count=0

for i in range(num,0,-1):
    if num % i == 0:
        count=count+1
        
if count == 2 :
    print("%d는 소수 입니다" %num)

else :
    print("%d는 소수가 아닙니다" %num)  
"""

"""
number=[10,20,30,40,50]
total=0

for i in number :
    total=total+i
print(total)
"""


"""
for ch in "HELLO":
    print(ch,end=' ')
"""

"""
text=input("단어를 입력하세요")
v_text="AAAbbb"
result=" "
for ch in text:
    if ch not in v_text:
        result = resilt +ch

print(result)
"""

number= input("계좌번호를 입력하세요: ")
result= ""

for ch in number :
    if ch != "-" :
        result= result + ch
print(result)















