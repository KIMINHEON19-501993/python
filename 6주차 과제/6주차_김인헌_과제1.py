def Gender(num):
    if num == '1' or num == '3' :
        gen = '남'
    elif num == '2' or num == '4' :
        gen = '여'
    return gen

name = input(' 이름을 입력 하세요 : ')
yymmdd = input(' 주민 등록 번호를 입력하세요 : ')

gen = Gender(yymmdd[7])

print("%s님은 %s월 %s일 출생으로, %s자 입니다."
        %(name, yymmdd[2:4], yymmdd[4:6], gen))
