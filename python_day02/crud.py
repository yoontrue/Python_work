import sys

user_list = []

def mk_grade(avg):
    # 평균의 학점 구하기
    grade = 'F'
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    elif avg >= 50:
        grade = 'F'
    return grade

def inputData(user):
    user.append(input('성명입력: '))
    user.append(int(input('국어 점수 입력: ')))
    user.append(int(input('영어 점수 입력: ')))
    user.append(int(input('수학 점수 입력: ')))

def mk_user():
    #     성명    국   영   수  총점  평균  학점
    # 'gildong', 90, 90, 90, 270, 90, 'A'
    user = []
    inputData(user)
    user.append(user[1] + user[2] + user[3])
    user.append(user[4] / 3.0)
    # 평균의 학점 구하기
    user.append(mk_grade(user[5]))
    return user;

def input_user():
    user_list.append(mk_user())

def print_user_list():
    print(":::: 학생 정보 출력 ::::")
    for user in user_list:
        print("%s %d %d %d %d %.1f %c" % tuple(user))

def menu():
    print(":::: MENU ::::")
    no = 0
    while not(no in range(1,7)):
        print("1.input, 2.output, 3.search, 4.modify, 5.delete, 6.finish")
        no = int(input("choice (1~6): "))
    return no

def search():
    print(":::: SEARCH ::::")
    # 이름으로 검색해서 해당 요소의 정보를 보여준다.
    search_name = input("찾을 사람 입력 >>")
    for i in user_list:
        std = []
        std.append(user_list[i])
        if search_name == std[0]:
            print(user_list[i])

def modify():
    print(":::: MODIFY ::::")
    # 이름으로 검색해서 해당 요소의 정보를 수정한다.

def delete():
    print(":::: DELETE ::::")
    # 이름으로 검색해서 해당 요소의 데이터를 리스트에서 제거한다.
    # del 연산자 사용

def finish():
    print(":::: 프로그램 종료 ::::")
    print("수고하셨습니다.")
    sys.exit()

menu_list = [menu, input_user, print_user_list, search, modify, delete, finish]

def main(name):
    print(f'::: {name} :::')

    while True:
        no = menu_list[0]()
        menu_list[no]()

if __name__ == '__main__':
    main("Python Project")
