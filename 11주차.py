#tuple 생성
#변경 X, 인덱싱 O
#tuple에 값을 추가, 제거, 변경은 불가능 하나 합병은 가능
#(min,max,len)연산자 사용 가능, 
#del 연산자를 통해 데이터 자체를 삭제 하는 것은 가능
#tuple은 괄호 없이도 생성 가능 단 하나의 값만 입력 한경우 tuple이 아님
"""
colors = ("rde", "green", "blue")
print(colors)
print(type(colors))
"""

"""
numbers = ("1", "2", "3", "4")
print(numbers)
print(type(numbers))
"""

"""
person = ("김인헌" , "1", "2", "3")
print(person)
print(type(person))
print(person[1])
"""

"""
t1 = ()
t=numbers+person
print(t1)
print(type(t1))

print(max(t1))
print(min(t1))
print(len(t1))
del numbers
"""


"""
t2 = 1, 2, 3, 4
print(t2)
print(type(t2))

t3 = "red", "green", "blue"
print(t3)
print(type(t3))

t4 = 1, 2, "김인헌"
print(t4)
print(type(t4))

t5=()
print(t5)
print(type(t5))

t6=(10)
print(t6)
print(type(t6))

t7=10
print(t7)
print(type(t7))
"""

"""
numbers =1, 2, 3, 4, 5 #패킹(튜플에 값을 저장)
print(numbers)
a, b, c, d, e = numbers #언패킹(튜플에 저장 되어 있는 값을 사용해 저장)
print(a, b, c, d, e)
a, b, c = number #언패킹시 대입 하는 값의 수가 같아야 사용 가능
"""

"""
def print_langeuage(language_tuple):
    for i in language_tuple :
        print(i)

tuple_a = ("Python", "java", "Ruby")
print(tuple_a)
print(type(tuple_a))
print_langeuage(tuple_a)
"""


#set는 #변경 O, 인덱싱 X
#set는 중괄호를 사용
#빈 중괄호만 입력시 type가 set가 아닌 dict 로 나온다.
#빈 set type를 만들고 싶다면 set함수를 사용하여 만든다.

numbers = {1, 3, 2}
print(numbers)
print(type(numbers))
print(len(numbers))
"""
cities = ("Paris", "Seoule", "London", "Berlin", "Paris", "Seoule")
print(cities)
print(type(cities))
print(len(cities))

"""

"""
d={}
print(type(d))
s=set()
print(type(s))
"""

"""
#set는 리스트와 문자열도 입력 가능
s1 = set([1,2,5,3,6,4,5,4])
print(s1)

s2 = {"Paris", "Seoule", "London", "Berlin", "Paris", "Seoule"}
print(s2)
"""

"""
a = {5,4,3,2,1}

a.discard(5)

print(a)

a.remove(2)

print(a)

a.clear()
print(a)
"""

#.issubest() 부분집합
#.issuperset() 상위집합
#.intersection() 교집합
#.difference() 차집합
"""
A={1,2,3}
B={1,2,3}

print(A==B)
print(A!=B)

A={1,2,3,4,5}
print(A>B)

print(B.issubset(A))
print(A.issuperset(B))
print(A.intersection(B))
print(A.difference(B))
"""

"""
A대학 = {"정선미", "RM", "진", "슈가", "제이홉", "지민"}
B대학 = {"슈가", "지민", "정국", "뷔", "정선미"}

C=A대학.intersection(B대학)


print("중복지원한 사람은 총 ", len(C), "명 입니다")

D=list(C)

for i in range(len(D)):
    print("%d.%s" %(i+1, D[i]))
"""


#dict
"""
programmer_dict = {"Python":5, "C":2, "C++":3, "Java":4}


print(programmer_dict)
print(type(programmer_dict))

#키 안의 값 변경
programmer_dict["Python"]=7

#키 값 추가
programmer_dict["Ruby"]=1

#keys 값만  확인 하는 메소드 
programmer_dict.keys()

#데이터형 변환
a=programmer_dict.keys()
print(a)
print(list(programmer_dict.keys()))
print(tuple(programmer_dict.keys()))

#values 값만 확인 하는 메소드
programmer_dict.values()

#데이터형 변환
a=programmer_dict.values()
print(a)
print(list(programmer_dict.values()))
print(tuple(programmer_dict.values()))

#항목 검사
print("Python" in programmer_dict)

#항목 삭제
del programmer_dict["Ruby"]
print(programmer_dict)


programmer_dict.clear()
print(programmer_dict)
"""

"""
programmer_dict = [("A",1),("B",2)]
print(programmer_dict)

programmer_dict=dict(programmer_dict)
print(programmer_dict)

print(programmer_dict["A"])

a=programmer_dict.keys()
print(a)

a=programmer_dict.values()
print(a)
"""

#items 딕셔너리를 리스트 안에 튜플이 있는 형식으로 변환
"""
programmer_dict = {"Python":5, "C":2, "C++":3, "Java":4}

A=programmer_dict.items()
B=list(programmer_dict.items())

print(A)
print(B)
"""

"""
#get()
country = {"한국":"서울", "미국":"워싱턴", "영국":"런던", "중국":"베이징"}

print(country)

print(country["한국"])
print(country.get("한국","해당국가가 존재하지 않음"))
print(country.get("러시아","해당국가가 존재하지 않음"))
"""

"""
score = { 1111 : ("이철수", 100, 100, 100, 100),
          2222 : ("정선미", 90, 90, 90, 90),
          3333 : ("박영희", 80, 80, 80, 80),
          4444 : ("김희동", 70, 70, 70, 70),
          5555 : ("최둘리", 60, 60, 60, 60),}


while(True) :
    total=0
    avg=0
    학번=int(input("학번을 입력 하세요 : "))

    이름,국어,수학,영어,과학=score[학번]
    total=total+국어+수학+영어+과학
    avg=total/4
    print("이름 : %s, 총점 : %d, 평균 : %.1f" %(이름, total, avg))
"""

"""
name_dict={}
while(True):
    name=input("(입력모드)이름을 입력 하시오. : ")
    if not name :
        break
    number=input("전화번호를 입력 하시오. : ")

    name_dict[name]=number
    
while(True):
    search=input("(검색모드)이름을 입력 하시오. : ")

    if not search :
        break

    if search in name_dict:
            print(search,"님의 전화번호는 %s 입니다." %name_dict[search])
    else :
            print(search,name_dict.get(search,"님의 전화번호는 없음입니다."))
""" 






















