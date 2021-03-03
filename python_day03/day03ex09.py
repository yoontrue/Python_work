# 콜백함수
# 자바스크립트의 콜백함수처럼 사용

# 함수의 참조값을 변수에 대입
def fnA():
    print("이것은 fnA함수")


# 함수의 참조값 저장
fnB = fnA

# 호출
fnB()

print("-" * 20)


# 매개변수에 함수도 담을 수 있다.
# 함수를 인자로 전달 받는 함수 선언
def otherFnc(callback):
    if str(type(callback)) == "<class 'function'>":
        callback()
    else:
        print(callback, "함수 아님")


# 다른 함수를 실행시켜주는 함수에서 콜백함수 사용
def otherFnc(callback):
    try:
        callback()
    except:
        print(callback, "은 함수가 아닙니다")


otherFnc(fnA)
otherFnc(3000)