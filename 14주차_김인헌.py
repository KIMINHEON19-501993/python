'''과제
회사 직원들을 관리하는 프로그램이다. 직원은 정규직 직원과 계약직 직원으로 이루어진다.
모든 직원은 이름과 소속부서를 가진다. 프로그램은 총 3개의 클래스를 생성한다.

1. Employee 클래스
- 직원을 나타내는 클래스이다.
- 이름과 소속부서를 각각 주어진 값으로 초기화하는 생성자를 만든다.
- 이름, 소속부서를 변경하는 메소드와 반환하는 메소드를 만든다.(설정자, 접근자)

2. RegEmployee 클래스
- 정규직 직원을 나타내는 클래스이다.
- Employee 클래스를 상속받는다.
- 이 클래스에는 추가적으로 연봉과 보너스지급률 멤버변수를 선언한다.
- 정규직 직원의 이름, 소속부서, 연봉과 보너스 지급률을 각각 주어진 값을 초기화하는 생성자를 만든다.
  이때, 이름과 소속부서를 초기화하는 것은 super()를 사용하여 초기화한다.
- 정규직 직원의 월급을 계산하는 pay()메소드를 만든다. 수식은 “연봉/12 * (1 + 보너스 지급률)” 이다.
- 정규직 직원의 모든 정보(이름, 소속부서, 연봉, 보너스 지급률)를 getInfo()를 사용하여 한꺼번에 정보를 반환한다.

3. TempEmployee 클래스
- 계약직 직원을 나타내는 클래스이다.
- Employee 클래스를 상속받는다.
- 이 클래스에는 추가적으로 시간당임금과 근무시간 멤버변수를 선언한다.
- 계약직 직원의 이름, 소속부서, 시간당 임금을 주어진 값으로 초기화하고, 근무시간은 0으로 초기화하는 생성자를 만든다.
  이때, 이름과 소속부서를 초기화 하는것은 super()를 사용하여 초기화한다.
- 계약직원의 월급을 계산하는 pay()메소드를 만든다. 수식은 “시간당임금 * 근무시간” 이다.
- 계약직 직원의 모든 정보(이름, 소속부서, 시간당임금, 근무시간)를 getInfo()를 사용하여 한꺼번에 정보를 반환한다.

4. main
- 프로그래밍 순서는 다음과 같다
1) 객체 생성(정규직 직원-ReEmployee인 객체를 생성한다.)      이름 : 둘리, 소속부서 : 마케팅, 연봉 : 6,000, 보너스 지급률 : 0.4
2) 위의 객체를 현재 상태를 출력한다.
3) 정규직 직원의 월급을 계산한 후 출력한다. 
4) 객체 생성(계약직 직원-TempEmployee인 객체를 생성한다.)    이름 : 또치, 소속부서 : 연구개발, 시간당 임금 : 1
5) 계약직 직원의 근무시간에 300을 더한다.
6) 위의 객체의 현재 상태를 출력한다.
7) 계약직 직원의 월급을 계산한 후 출력한다.
'''

##Employee클래스 ==================================
#직원을 나타낸다
class Employee :
    #이름(name)과 소속부서(department)를 각각 주어진 값으로 초기화하는 생성자를 만든다
    def __init__(self, name, department) :
        self.name = name
        self.department = department
        
    #이름을 반환한다.
    def getName(self) :
        return self.name
    
    #소속부서를 반환한다.
    def getDepartment(self) :
        return self.department
    
    #이름을 변경한다.
    def setName(self, name) :
        self.name = name
    
    #소속부서를 변경한다.
    def setDepartment(self, department) :
        self.department = department
        
    #Employee 객체 이름과 소속부서의 정보를 반환한다.
    #출력형식 -- 이름 : 홍길동, 소속부서 : 마케팅
    def getInfo(self) :
        return "이름 : " + str(self.name) + ", 소속부서 : " + str(self.department)


    
##RegEmployee클래스 =================================
#정규직 직원을 나타낸다
class RegEmployee(Employee) :
    #정규직 직원의 이름, 소속부서, 연봉(yearlySalary), 보너스지급률(bonusRate)을 각각 주어진 값으로 초기화하는 생성자를 만든다.
    #이때, 이름과 소속부서는 부모클래스의 super()를 사용하여 초기화 한다.
    def __init__(self, name, department, yearlySalary, bonusRate) :
        self.yearlySalary = yearlySalary
        self.bonusRate = bonusRate
        super().__init__(name,department)

    #정규직 직원의 월급을 계산하여 반환한다.
    #수식은 "연봉/12 * (1 + 보너스 지급률)"
    def pay(self) :
        return "월급액 : " + str((self.yearlySalary / 12) * (1 + self.bonusRate))


    #정규직 직원의 모든 정보를 반환한다.
    #출력형식 -- 이름 : 홍길동, 소속부서 : 마케팅, 연봉 : 6000, 보너스지급률 : 0.4
    #이름과 소속부서는 super()를 사용하여 출력한다.
    def getInfo(self) :
        return super().getInfo() + ", 연봉 : " + str(self.yearlySalary) + ", 보너스 지급률 : " + str(self.bonusRate)



        
##TempEmployee클래스 =================================
#계약직 직원을 나타낸다
class TempEmployee(Employee) :
    #계약직 직원의 이름, 소속부서, 시간당임금(payRate)을 각각 주어진 값으로 초기화하고,
    #근무시간(hoursWorked)은 0으로 초기화하는 생성자를 만든다.
    #이때, 이름과 소속부서는 부모클래스의 super()를 사용하여 초기화 한다.
    def __init__(self, name, department, payRate) :
        self.payRate = payRate
        super().__init__(name,department)
        self.hoursWorked = 0


    #계약직 직원의 월급을 계산하여  반환한다.
    #수식은 “시간당임금 * 근무시간” 
    def pay(self) :
        return "월급액 : " + str(self.payRate * self.hoursWorked)


    #계약직 직원의 추가 근무시간을 누적된 근무시간에 더한다.
    def addHours(self, moreHours) :
        self.moreHours = moreHours
        self.hoursWorked = self.hoursWorked + self.moreHours
        

    #계약직 직원의 모든 정보를 반환한다.
    #출력형식 -- 이름 : 홍길동, 소속부서 : 마케팅, 시간당임금 : 1, 근무시간 : 300
    #이름과 소속부서는 super()를 사용하여 출력한다.
    def getInfo(self) :
        
        return super().getInfo() + ", 시간당임금 : " + str(self.payRate) + ", 근무시간" + str(self.hoursWorked)



##main ==============================================
#RegEmployee 클래스의 empOne 객체 생성
#이름 "둘리", 소속부서 "마케팅", 연봉 6000, 보너스지급률 0.4인 정규직 직원 empOne이다.
empOne = RegEmployee("둘리","마케팅",6000,0.4)


#정규직 직원 empOne의 정보를 출력한다.
print(empOne.getInfo())


#정규직 직원 empOne의 월급을 계산한 후 출력한다.
print(empOne.pay())




#TempEmployee 클래스의 empTwo 객체 생성
#이름 "또치", 소속부서 "연구개발", 시간당임금 1인 계약직 직원 empTwo이다.
empTwo = TempEmployee("또치", "연구개발", 1)


#계약직 직원 empTwo의 근무시간에 300을 더한다.
empTwo.addHours(300)


#계약직 직원 empTwo의 정보를 출력한다.
print(empTwo.getInfo())


#계약직 직원 empTwo의 월급을 계산한 후 출력한다.
print(empTwo.pay())
