"""
for i in round(1,10,1) :
    for j in round(2,10,1):
        print("%d * %d = %d" %(j, i, j*i), end="\t")
    print()
"""

"""
total=0
i=1
while i < 101 :
    total+=i
    i=i+1
print("1부터 100까지의 합 = %d" %total)
"""

"""
num=int(input("출력할 단을 입력 하세요: "))
i=1

while i<10:
    print("%d * %d = %d" %(num, i, num*i))
    i = i + 1
"""

"""
score = 0
total = 0
count = 0
avg = 0
print("종료 하려면 음수를 입력 하세요")

while score >= 0 :
    score = int(input("성적을 입력 하세요: "))

    if score > 0 :
        total = total + score
        count = count + 1

if count > 0:
    avg = total /count
print("성적의 평균은 %2.f입니다." %avg)
"""


"""
total=0

answer= "yes"

while answer == "yes" or answer =="YES" :
    num = int(input("숫자를 입력 하시오 : "))
    total = total +num
    answer = input("계속? (yes/no) : ")

print("입력한 숫자의 합계는 %d입니다." %total)
"""


"""
import random

while True :
     x= random.randint(1,100)
     y= random.randint(1,100)
     answer= x+y

     ans = int(input(" %d + %d =" %(x, y)))
     if ans==answer :
        print("잘했어요!")
        break
"""


























