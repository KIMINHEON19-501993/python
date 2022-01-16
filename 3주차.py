#len() #글자수 출력


#word="python"
#word.upper() #소문자 대문자 변환(단독 사용 불가, 변수.upper()의 형태만 가능)
#word.lower() #대문자 소문자 변환(단독 사용 불가, 변수.lower()의 형태만 가능)

#[~부터:~전까지] #문자열 슬라이스

'''
number=input("주민등록번호 13자리를 입력하세요 : ")#9805141234567

year="19"+number[:2] #1998
month=number[2:4] #05
day=number[4:6] #14
gender=number[6] #1

print("출생년도 : %s" %year)
print("월 : %s" %month)
print("일 : %s" %day)
print("성별 : %s" %gender)
'''

'''
tem=int(input("현재 온도를 입력하세요 : "))

if tem>32:
    print("폭염주의보를 발생합니다.")
    print("건강에 조심하세요.")     
print("현재온도는 %d도 입니다." %tem)
'''

'''
num=int(input("숫자를 입력하세요 : "))

if num%2==0:
    print("%d은(는) 짝수 입니다." %num)
elif not num%2==0:
    print("%d은(는) 홀수 입니다." %num)
'''


time=int(input("근무시간을 입력하세요 : "))
money=float(input("시간당 임금을 입력하세요 : "))


if time>40:
    total_money=(40*money)+((time-40)*(money*1.5))
    print("총임금은 %.1lf 입니다." %total_money)
else :
    total_money=time*money
    print("총임금은 %d 입니다." %total_money)




    
