number = 10


def setNumber() :
    print('setNumber() 호출됨.')
    # 함수에서 외부에 선언된 변수의 값을 변경하기 위해서 global 키워드 사용
    global number
    number = 100

setNumber()

print(number)