# 반환값(return)을 사용하는 함수
# 함수에서 처리한 결과 값을 함수가 호출된 지점으로 돌려줄 수 있다.
# 함수는 처리할 인수를 전달 받고 그 결과를 반환하는 일을 한다.

# 두개의 정수를 입력받아 비교 후 더 큰수를 반환 해 주는 함수 선언 예제
# arguments와 ruturn을 모두 사용하는 함수
def get_max(num1, num2):
    if num1 > num2:
        maxnum = num1
    else:
        maxnum = num2

    return maxnum


result = get_max(10, 100)
print(f'더 큰수는 {result}입니다.')

a = 5
b = 3
c = 10
resultthree = get_max(a, get_max(b, c))
print(f'세 숫자중 가장 큰 수는{resultthree}입니다.')


# keys의 목록과 values의 목록을 전달받아서
# dictionary 구조를 만들고 그 결과를 반환하는 함수
def mk_dict(keys, values):
    if len(keys) != len(values):
        print('key리스트와 value리스트의 길이가 다르다.')
        return

    # 딕셔너리 구조로 만들어 준다.
    new_dict = dict()
    for i, key in enumerate(keys):
        new_dict[key] = values[i]

    # 딕셔너리 구조 반환
    return new_dict


keys = ['오징어', '꼴뚜기', '대구', '명태']
values = [2000, 3000, 5000, 1500]
dict1 = mk_dict(keys, values)
print(dict1)