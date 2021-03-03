# 학습목표
# 1. 함수를 정의하고 사용하는 방법
# 2. 람다표현식 사용 방법

# 파이썬에서 함수 정의 def 키워드를 이용해서 함수를 정의한다.
# 함수를 정의할 때는 머리와 몸체를 만들어야 한다.

# 함수 선언부
def my_func() :
    print('[2] def 함수 호출')
    print('[3] 이것은 함수 몸체에서 실행 되었습니다.')

print('[1] 함수 호출 전에 실행하는 문장')
# 함수 호출
my_func()

print('[4] 함수 호출 후에 실행하는 문장')