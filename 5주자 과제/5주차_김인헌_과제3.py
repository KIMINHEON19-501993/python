num=int(input("정수를 입력 하시오: "))

소수개수=0
for i in range(num,1,-1):
    count=0
    for j in range(i,0,1):
        if j%2==0:
            count=count+1
    
if (count == 2):
    print(i)
    소수개수=소수개수+1

print("소수의 개수는 %d개 입니다." %소수개수)



