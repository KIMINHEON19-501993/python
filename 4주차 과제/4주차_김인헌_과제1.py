maj=int(input("전공점수를 입력 하세요"))
eng=int(input("영어점수를 입력 하세요"))

if maj>=90 and eng>=90 :
    print("당신은 합격 입니다.")
elif (maj>=90 and eng<90) or (maj<90 and eng>=90) :
    print("당신은 대기 입니다.")
else :
    print("당신은 불합격 입니다.")

    
