#함수.insert(index,2) 리스트에 index방에 2를 추가
#함수.pop(index) 리스트 index방의 값을  제거
#in, not in 리스트 내 특정 원소 존재 여부 확인
#a.extend(b) a리스트에 b리스트를 추가
#del a[:] 요소삭제,del a 리스트 삭
"""
jumsu=[]
for i in range(0,4,1):
    jumsu.append(0)

total=0

for i in range(0,4,1):
    jumsu[i]=int(input("점수 = "))
    total = jumsu[i] + total

avg = total/4
print("총점 : ", total)
print("평균 : ", avg)
"""


"""
jumsu = []
for i in range(0,4,1):
    jumsu.append(0)


total = 0

for i in range(len(jumsu)):
    jumsu[i]=int(input("점수 = "))
    total=jumsu[i]+total

avg = total/4
print("총점 : ", total)
print("평균 : ", avg)
"""


"""
data=[45,46,64,47,11]

Max=data[0]
Min=data[0]

for i in range(len(data)):
    if data[i] >= Max :
        Max=data[i]
    if data[i] <= Min :
        Min=data[i]

print("최댓값 =",Max)
print("최솟값 =",Min)
"""


"""
data=[1,2,3,4,5]

5 in data
"""


"""
def func(i,list_a):
    i=i+1
    list_a.append(5)
    


a=10
list_b=[1,2,3,4]

print("호출 전 =",a,list_b)

func(a,list_b)

print("호출 후 =",a,list_b)
"""


"""
data=[5,1,3,2,4]
print("현재 리스트 값 = ",data) 


for i in range(0,len(data)-1,1):
    Min=i
    for j in range(i+1,len(data),1):
        if (data[Min] > data[j]) :
            Min=j
    temp = data[Min]
    data[Min]=data[i]
    data[i]=temp
print("변환후 리스트 값 =",data)


data=[5,1,3,2,4]

for i in range(0,len(data)-1,1):
    Max=i
    for j in range(i+1,len(data),1):
        if (data[Max] < data[j]) :
            Max=j
    temp = data[Max]
    data[Max]=data[i]
    data[i]=temp
    
print("변환후 리스트 값 =",data)
"""

"""
data[1,2,3,4,5]
data.sort()
print("정렬 후")
"""
data=[1,2,3,4,5]

print("최댓값 = ", data[-1])
print("최솟값 = ", data[0])

mid=int(len(data)/2)

print("중간값 = ",mid)


