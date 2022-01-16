import random

x= random.randint(1,100)
y= random.randint(1,100)
answer= x+y

while True :
     ans = int(input(" %d + %d =" %(x, y)))
     if ans==answer :
        print("잘했어요!")
        break
