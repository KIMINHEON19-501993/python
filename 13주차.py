#설정자 : set......
#접근자 : get......
"""
class Student :
    def __init__ (self, name, age) :
        self.__name = name
        self.__age = age

    def getAge (self) :
        return self.__age

    def getName (self) :
        return self.__name

    def setAge (self, age) :
        self.__age = age

    def setName (self, name) :
        self.__name = name

    def show (self) :
        print("name =",self.__name)
        print("age =",self.__age)
"""


"""
class Circle :
    def __init__ (self,r=1) :
        self.__r = r
        
    def setRadius(self,r) :
        self.__r = r

    def getRadius(self) :
        return self.__r

    def calcArea (self):
        return 3.14 * self.__r **2

    def calcCircum (self):
        return 2 * 3.14 * self.__r
"""


"""
class Rectangle:
    def __init__(self, side = 0) :
        self.side = side
    def getArea(self):
        return self.side*self.side


def printArea(r,n):
    while n >= 1 :
        print(r.side,"\t", r.getArea())
        r.side = r.side +1
        n = n - 1

myRect = Rectangle()
count = 5
printArea(myRect, count)
print("사각형의 변 =",myRect.side)
print("반복 횟수 =",count)
"""


"""
class AA :
    c = 0

    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        AA.c = c

    def view (self):
        print(self.a, self.b, AA.c)

ob1 = AA(1,2,3)
ob2 = AA(5,6,7)

ob1.view()
ob2.view()
"""


"""
class Fruit :
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__ (self, other) :
        return self.price + other.price 
    def __le__ (self, other) : #작거나 같다
        if self.price <= other.price :
            return "True!"
        else :
            return "False!"
    def __ge__ (self, other) : #크거나 같다
        if self.price >= other.price :
            return "True!"
        else :
            return "False!"
    def __str__(self): 
        return ("Fruit Info : %s, %d" %(self.name, self.price))



ob1 = Fruit("A", 1000)
ob2 = Fruit("B", 2000)
print(ob1)
print(ob2)
print(ob1+ob2)
print(ob1 <= ob2)
print(ob1 >= ob2)
"""


class Parent :
    parentAttr =100

    def __init__ (self) :
        print("부모 생성자")

    def parentMethod(self):
        print("부모 메소드")

    def setAttr(self, attr) :
        Parent.parentAttr = attr

    def getAttr(self) :
        print("Parent Attribute :" , Parent.parentAttr)

class Child(Parent) :
    def __init__(self) :
        print("후손의 생성자")
    def childMethod(self) :
        print("후손의 메소드")


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
