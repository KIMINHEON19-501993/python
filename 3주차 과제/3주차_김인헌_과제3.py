time=int(input("근무시간을 입력하세요 : "))
money=float(input("시간당 임금을 입력하세요 : "))


if time>40:
    total_money=(40*money)+((time-40)*(money*1.5))
    print("총임금은 %.1lf 입니다." %total_money)
else :
    total_money=time*money
    print("총임금은 %d 입니다." %total_money)