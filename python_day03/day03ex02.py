# 함수를 사용하는 이유
# 함수를 선언해두면 여러지점에서 재활용(반복호출) 가능
# input(), print()도 역시 함수다.

def my_func(size):
    print('>>> 함수 호출 ...')
    print('>>> 이것은 함수입니다.')
    print('-' * size)


print('>> 1 함수를 외부에서 호출 하였습니다.')
my_func(10)
print('>> 2 함수를 외부에서 호출 하였습니다.')
my_func(20)
print('>> 3 함수를 외부에서 호출 하였습니다.')
my_func(30)
print('>> 4 함수를 외부에서 호출 하였습니다.')
my_func(40)


def fn(cnt):
    print(">" * cnt)
    if cnt <= 0:
        return
    # 재귀 호출 - 반복문 대신 사용 가능
    fn(cnt - 1)

# 매개변수(argument)
fn(10)