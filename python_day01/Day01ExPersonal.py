# 메뉴와 반복문을 이용해서
# [입력] [출력] [검색] [수정] [삭제]
# 국어, 영어, 수학 성적을 입력 받아서
# 총점, 평균, 학점을 출력하는 프로그램 구현.
# 함수를 최대한 많이 만들고 list를 활용한다.

def Insert_s():
    allStud = []

    name = input('성명 입력 >>')
    kor = int(input("국어 점수>>"))
    eng = int(input("영어 점수>>"))
    math = int(input("수학 점수>>"))

    tot = kor + eng + math
    avg = tot/3

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    student = [name,kor,eng,math,tot,avg,grade]
    student.append(student)

    return allStud
# end of Insert()

