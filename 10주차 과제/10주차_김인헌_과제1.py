#점수 리스트 생성
data=[0,0,0,0,0]

print("5명의 평가 점수를 입력 하세요(100점 만점)")
print("")
#점수 5번 입력 받기
for i in range(len(data)):
    data[i]=int(input("점수 입력 :"))
print("")

#리스트 출력
print("==총 입력 점수==")
for i in range(len(data)):
    print("%d 점" %data[i])
print("")

#최댓값 및 최솟값 출력
MAX=data[0]
MIN=data[0]
for i in range(len(data)):
    if MAX < data[i]:
        MAX = data[i]
    if MIN > data[i]:
        MIN = data[i]

print("==제거 대상 점수==")
print("최고 점수 =",MAX)
print("최소 점수 =",MIN)
print("")

#최댓값, 최솟값 제거
data.remove(MAX)
data.remove(MIN)


#최대, 최소를 제거한 최종 리스트 출력
print("==최종 입력 점수==")
for i in range(len(data)):
    print("%d 점" %data[i])
print("")

#최대 최소를 제거한 나머지 점수 합계, 평균 출력
total=0
avg=0

for i in range(len(data)):
    total=total+data[i]

avg=total/len(data)

print("=================")
print("총점 :", total)
print("평균 :", avg)








