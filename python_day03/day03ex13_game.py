import random

min = 1
max = 100
count = 5
number = 0

def check() :
    global min
    global max

    usernum = int(input(f"사용자 입력({min}와{max}사이 입력)>>> "))
    if usernum == number :
        return True
    else :
        if usernum > number :
            print("너무 큰 숫자입니다.")
            max = usernum - 1
        else :
            print("너무 작은 숫자입니다.")
            min = usernum + 1
        return False


def game() :
    print("::: 높다 낮다 게임 시작 :::")
    # 컴퓨터가 난수를 발생 시킨다.
    global min
    global max
    global count
    global number
    min = 1
    max = 100
    count = 5
    number = random.randint(min, max)
    print(f"{min}와 {max}사이의 숫자를 컴퓨터가 발생시켰습니다.(힌트:{number})")

    while count > 0 :
        if check() :
            break
        count -= 1
    print("::: 기회가 모두 소진되었다 :::" if count == 0 else "!!! 성공입니다 !!!")

if __name__ == '__main__':
    # 이 파일이 외부에서 모듈로 사용 될때는 실행 하지 않는다.
    while True :
        game()
        isPlay = input("계속 하려면 y을 입력하세요>>> ")
        if isPlay != 'y' :
            print("수고하셨습니다!")
            break