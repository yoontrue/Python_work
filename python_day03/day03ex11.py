# 콜백함수 기법을 활용한 예제
# 람보예제 - 람보가 무기를 사용한다.
#
def ramboAction(callback):
    name = '람보'
    try:
        print('람보 액션!')
        print('콜백함수 실행 전 작업...')
        callback(name)
        print('콜백함수 실행 후 작업...')
        print('-' * 30)
    except:
        print('함수가 아닙니다! 함수 강제 종료!')


# 콜백으로 전달할 기능 선언
def gun(user):
    print(user + '가 총을 쏜다. 탕탕탕!!!')


def sword(user):
    print(user + '가 검을 휘두른다. 휙휙!!')


ramboAction(gun)
ramboAction(sword)

# 전략패턴
