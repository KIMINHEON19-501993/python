
"""
data = [30, 40, 50, 20, 10]

Max=data[0]
Min=data[0]

for i in range(len(data)):
    if data[i] > Max :
        Max = data[i]
    if data[i] < Min :
        Min = data[i]


print("현재 리스트 값 :", data)
print("최댓값 :", Max)
print("최솟값 :", Min)
"""


#선택정렬
"""
data = [1,6,7,5,2,4,9,3,8]
print("현재 데이터 값 :",data)

A=0

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] <= data[j]:
            A=data[i]
            data[i] = data[j]
            data[j]=A

print("바뀐 데이터 값 :",data)


MID=data[len(data)//2]

print(int(MID))
"""


#버블정렬
"""
data = [1,6,7,5,2,4,9,3,8]
print("현재 데이터 값 :",data)

A=0

for i in range(0, len(data)-1, 1):
    for j in range(0, len(data)-1-i, 1):
        if data[j] >= data[j+1]:
            A=data[j]
            data[j] = data[j+1]
            data[j+1]=A

print("바뀐 데이터 값 :",data)


MID=data[len(data)//2]

print(int(MID))
"""



#순차 탐색
"""
data = [30, 10, 20, 50, 40]

print(data)

key = int(input("탐색할 숫자를 입력 하세요.(10~50) : "))

for i in range(len(data)):
    if key==data[i]:
       key=i

print("탐색성공 인덱스 :", key)

"""

"""
data = [3,7,5,21,13,9,17,1,11,15,19]
print("현재 데이터 값 :",data)

A=0

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] <= data[j]:
            A=data[i]
            data[i] = data[j]
            data[j]=A

print("바뀐 데이터 값 :",data)

key = int(input("탐색할 홀를 입력 하세요.(1~21) : "))

for i in range(len(data)):
    if key==data[i]:
       key=i

print("탐색성공 인덱스 :", key)

MID=data[len(data)//2]

print("중간값 :", int(MID))

for i in range(len(data)):
    if MID==data[i]:
       MID=i
print("중간값 인덱스 :", MID)
"""














