import random

count=0

while True :
    x= random.randint(1,100)
    y= random.randint(1,100)
    answer= x+y

    ans = int(input(" %d + %d =" %(x, y)))
    if ans==answer :
        count=count+1

    if count==3:
        print("잘했어요!")
        break
       
