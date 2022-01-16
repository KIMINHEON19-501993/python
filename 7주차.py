"""
import random

def password():

    alpa ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw = ""

    for i in range(6):
        index = random.randrange(len(alpa))
        pw = pw + alpa[index]
    print(pw)
"""

def sub(x,y):
    global a
    a=7
    temp=x
    x=y
    y=temp
    b=3
    print(a,b,x,y)

a=1
b=2
x=3
y=4

print(a,b,x,y)
sub(x,y)
print(a,b,x,y)
