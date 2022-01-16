"""
#super(). 부모클래스 호출

class MyScore :
    def __init__ (self, kor, eng):
        self.kor = kor
        self.eng = eng
    def getTot(self):
        return self.kor + self.eng
class MyScore_Sub(MyScore):
    def __init__ (self, kor, eng, mat):
        self.mat = mat
        super().__init__(kor,eng)
    def getTot(self):   
        return self.mat + super().getTot()


my = MyScore_Sub(90,90,90)
print("점수 =",my.getTot())
"""


"""
class MyScore :
    def __init__ (self, kor):
        self.kor = kor
    def getTot(self):
        return self.kor
class MyScore_Sub(MyScore):
    def getTot(self):
        print(super().getTot())

my = MyScore_Sub(100)
my.getTot()
"""


#class Venicle: 교제
#class Employee : 교제
"""
class MyScore :
    def __init__ (self, kor, eng):
        self.kor = kor
        self.eng = eng
    def getTot(self):
        return self.kor + self.eng
class MyScore_Sub(MyScore):
    def __init__ (self, kor, eng, mat):
        self.mat = mat
        super().__init__(kor,eng)
    def getTot(self):  #오버라이딩 
        return self.mat + super().getTot()

my1 = MyScore(100,100)
my2 = MyScore_Sub(100,100,100)

print(my1.getTot())
print(my2.getTot())
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
    print(car.name + ": " + car.drive())
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
























