name=input("이름을 입력하세요: ")
number=input("주민등록번호를 입력하세요: ")

year=number[:2] 
month=number[2:4] 
day=number[4:6] 
gender=number[7] 

if gender== '1' or gender == '3' :
    print("%s님은 %s월 %s일 출생으로 남자 입니다." %(name,month,day))
elif gender == '2' :
    print("%s님은 %s월 %s일 출생으로 여자 입니다." %(name,month,day))
