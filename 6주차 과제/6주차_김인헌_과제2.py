def total(a,b,c,d):
    return a+b+c+d

def avg(total):
    return total/4

def grade(avg):
    if avg >= 90 :
        gre = 'A'
    elif avg >= 80 :
        gre = 'B'
    elif avg >= 70 :
        gre = 'C'
    elif avg >= 60 :
        gre = 'D'
    else :
        gre = 'F'

    return gre


kor = int(input('국어 점수를 입력 하세요 : '))
mat = int(input('수학 점수를 입력 하세요 : '))
eng = int(input('영어 점수를 입력 하세요 : '))
sci = int(input('과학 점수를 입력 하세요 : '))

Total=total(kor,mat,eng,sci)
Avg=avg(Total)
Grade=grade(Avg)

print('총점 : %d' %Total)
print('평균 : %.1f' %Avg)
print('학점 : %s' %Grade)
