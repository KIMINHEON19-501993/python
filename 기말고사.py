#함수.insert(index,2) 리스트에 index방에 2를 추가
#함수.pop(index) 리스트 index방의 값을  제거
#함수.sort() 리스트 순차정리
#in, not in 리스트 내 특정 원소 존재 여부 확인
#a.extend(b) a리스트에 b리스트를 추가
#del a[:] 요소삭제,del a 리스트 삭제
#리스트 변경O 검색 X
#tuple 생성
#변경 X, 인덱싱 O
#tuple에 값을 추가, 제거, 변경은 불가능 하나 합병은 가능
#(min,max,len)연산자 사용 가능, 
#del 연산자를 통해 데이터 자체를 삭제 하는 것은 가능
#tuple은 괄호 없이도 생성 가능 단 하나의 값만 입력 한경우 tuple이 아님
#set는 #변경 O, 인덱싱 X
#set는 중괄호{}를 사용
#빈 중괄호만 입력시 type가 set가 아닌 dict 로 나온다.
#빈 set type를 만들고 싶다면 set함수를 사용하여 만든다.
#.issubest() 부분집합
#.issuperset() 상위집합
#.intersection() 교집합
#.difference() 차집합


#1번
"""
jumsu=[]
for i in range(0, 4, 1):
    jumsu.append(0)

total = 0

for i in range(0,4,1):
    jumsu[i]=int(input("점수 입력"))
    total = total +jumsu[i]

avg = total/4

print(total)
print(avg)
"""

"""
data = [30, 10, 20, 50, 40,60]
print(data)


for i in range(0,len(data)-1,1):
    min_num = i
    for j in range(i+1,len(data),1):
        if data[min_num] > data[j]:
            min_num = j

    temp = data[min_num]
    data[min_num] = data[i]
    data[i] = temp
print(data)

mid = int(len(data)/2)

print(data[-1])
print(data[0])
print(data[mid])
"""

"""
data = [30, 10, 20, 50, 40,60]
print(data)


for i in range(0,len(data)-1,1):
    for j in range(0,len(data)-1-i,1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            
    
print(data)

mid = int(len(data)/2)

print(data[-1])
print(data[0])
print(data[mid])
"""


"""
data = [30, 10, 20, 50, 40,60]
print(data)

key = int(input("?"))

for i in range(0,len(data),1):
    if data[i] == key:
        print(i)
"""

"""Z
data = [1,5,19,3,15,7,17,13,21,11,9]

for i in range(0,len(data)-1,1):
    for j in range(0,len(data)-1-i,1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp

print(data)
key = int(input("?"))

for i in range(0,len(data),1):
    if data[i] == key:
        print(i)

"""

"""
length = len(data)

start = 0
end = length - 1

while start <= end :
    mid = (start + end) //2

    if data[mid] == key:
        print(mid)
        break
    elif data[mid] > key :
        end = mid - 1
    else :
        start =  mid + 1

"""

"""
List=[0,0,0,0,0]

for i in range(0, len(List),1):
    List[i] = int(input("?"))

print(List)

Max = List[0]
Min = List[0]

for i in range(0,len(List),1):
    for j in range(0,len(List),1):
        if Max < List[j]:
            Max = List[j]
        if Min > List[j]:
            Min = List[j]
        
print(Min)
print(Max)

List.remove(Min)
List.remove(Max)

print(List)

avg = 0
total = 0

for i in range(0, len(List),1):
    total = total + List[i]

avg = total/len(List)

print(total)
print(avg)
"""


"""
A={"정선미","RM","진","슈가","제이홉","지민"}
B={"슈가","지민","정국","뷔","정선미"}

C=A.intersection(B)
D=list(C)

for i in range(0,len(C),1):
    print("%d. %s" %(i+1, D[i]))
"""


"""
name_dict={}

while(1):
    name = input("이름 입력")
    if not name:
        break
    number = input("전화번호 입력")

    name_dict[name]=number

while(1):
    search = input("이름 검색")
    if not search:
        break
   
    if search in name_dict:
        print(search,"의 전번은 %s임" %name_dict[search])
    else :
        print(search,name_dict.get(search,"의 전번은노노 "))
"""


"""
class Counter :
    def reset(self):
        self.count = 0
    def countplus(self):
        self.count = self.count + 1
    def get(self):
        return self.count

a=Counter()
a.reset()
a.countplus()
print(a.get())
"""


"""
class Counter :
    def __init__(self,count = 1):
        self.count = count
    def countplus(self):
        self.count = self.count + 1
    def get(self):
        return self.count

a=Counter(5)
a.countplus()
print(a.get())

"""


"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print(self):
        print("name = ",self.name,"age=",self.age)

a= Person("A",12)
print(a.print())
"""


"""
class Mydle :
    def __init__(self,s1):
        print(s1)
    def __del__(self):
        print("call del")
"""

"""
class Box:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def setA(self,a):
        self.a = a
    def setA(self,b):
        self.b = b
    def setA(self,c):
        self.c = c

    def getVolumn(self) :
        return self.a * self.b * self.c

    def __str__(self) :
        return ("%d, %d, %d" %(self.a,self.b,self.c))




box1=Box(10,10,10)
box2=Box(4,5,6)
    
print(box1)
print("box의 부피 =", box1.getVolumn())
print(box2)
print("box의 부피 =", box2.getVolumn())
"""

"""
class Venicle:
    def __init__(self,name):
        self.name = name
    def drive(self):
        raise NotImplementedError("구현되지 않은 메소드 입니다.")
    def stop(self):
        raise NotImplementedError("구현되지 않은 메소드 입니다.")
    
class Car(Venicle):
    def drive(self):
        return "승용차를 운전 합니다." #오버라이딩
    def stop(self):
        return "승용차를 정지 합니다." #오버라이딩

class Truck(Venicle):
    def drive(self):
        return "트럭을 운전 합니다." #오버라이딩
    def stop(self):
        return "트럭을 정지 합니다." #오버라이딩


#mycar1 = Venicle("자동차")
mycar2 = Car("자동차")
mycar3 = Truck("자동차")
#print(mycar1.drive())
print(mycar2.drive())
print(mycar3.drive())
print(mycar2.stop())
print(mycar3.stop())

cars = [Truck("truck1"), Truck("truck2"), Car("car")]
for car in cars:
    print(car.name + ": " + car.drive() +  car.stop())
"""

"""
class SuperTest:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
    def getTest(self):
        return "나의 이름은 " + str(self.name) + "이고, " +\
        "사는곳은 " + str(self.addr) + " 입니다."

class SubTest(SuperTest):
    def __init__(self, name, addr, age, score):
        self.age = age
        self.score = score
        super().__init__(name, addr)
    def getTest(self):
        return super().getTest()+" \n나이는 "+\
               str(self.age) + "살이고, " + \
               "점수는 " + str(self.score) + "점 입니다."


ob1 = SuperTest("둘리","진주")
ob2 = SubTest("마이콜","진주",20,90)
print(ob1.getTest())
print("=========================================")
print(ob2.getTest())       
"""
