"""
class Counter :
    def reset(self) :
        self.count = 0

    def increment(self) :
        self.count = self.count + 1

    def get(self) :
        return self.count

a = Counter()

a.reset()
a.increment()

print("카운터 a의 값은", a.get())

b = Counter()
b.reset()
#b.increment() reset 함수 없이 사용시 오류 발생
print("카운터 b의 값은", b.get())
"""

"""
#생성자1 (객체를 생성 하자 마자 필수 함수 를 사용 가능 하게 함)
class Counter :
    def __init__(self) :
        self.count = 0

    def increment(self) :
        self.count = self.count + 1

    def get(self) :
        return self.count


c = Counter()
c.increment()
print("카운터 c의 값은", c.get())
"""

"""
#생성자2
class Counter :
    def __init__(self, num) : #시작 함수에 num값을 넣음
        self.count = num

    def increment(self) :
        self.count = self.count + 1

    def get(self) :
        return self.count

d = Counter(5)
d.increment()
print("카운터 d의 값은", d.get())
"""

"""
#생성자3
class Counter :
    def __init__(self, num=0) : #값을 지정 하지 않으면 num=0
        self.count = num

    def increment(self, num) :
        self.count = self.count + 1

    def get(self) :
        return self.count

e = Counter()
print("카운터 e의 값은", e.get())

f = Counter(10)
print("카운터 f의 값은", f.get())

"""

"""
class Person:
    def name(self, name=""):
        self.name = name

    def age(self, age=0):
        self.age = age

    def aboutPerson(self) :
        print("name은 %s" %self.name)
        print("age는 %d" %self.age)

a = Person()
a.name("Dominica")
a.age(20)
a.aboutPerson()
"""

"""
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def aboutPerson(self) :
        print("name은 %s" %self.name)
        print("age는 %d" %self.age)

objPerson = Person("Dominica", 20)
objPerson.aboutPerson()
"""

"""
#소멸자

class Mydel :
    def __init__(self, s1) :
        print(s1)
    def __del__(self) :
        print("call del")


obj = Mydel("call del")
del obj
"""


"""
class Television :
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self) :
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel) :
        self.channel = channel
    def getChnnel(self) :
        return self.channel

t = Television(9, 10, True)
t.show()
t.setChannel(11)
t.show()
"""

"""
class Mstack :
    def __init__(self) :
        self.stack = []
        print("Hi Mstack")
    def push(self, str1) :
        self.stack.append(str1)
    def pop(self) :
        return self.stack.pop()
    def length(self) :
        return len(self.stack)
    def __del__(self) :
        print("Bye Mstack")

obj1 = Mstack()
obj2 = obj1
print(obj1)
print(obj2)

obj1.push("abc")
print(obj1.push)
print(obj2.push)

obj1 = Mstack("Bye Mstack")
"""

"""
#정보 은닉1 현재는 외부 에서도 값을 쉽게 변경 가능 
class Student:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def show(self) :
        print("name은 %s" %self.name)
        print("age는 %d" %self.age)

s1 = Student("Jeong", 20)
s1.show
s1.name = "Jun"
s1.age = 21
s1.show()
"""

"""
#정보은닉2 변수이름 앞에 __를 붙임으로 외부에서 변경 불가능
class Student:
    def __init__(self, name="", age=0):
        self.__name = name
        self.__age = age
    def show(self) :
        print("name은 %s" %self.__name)
        print("age는 %d" %self.__age)

s1 = Student("Jeong", 20)
s1.age = 21
s1.show()
"""



        
    

















