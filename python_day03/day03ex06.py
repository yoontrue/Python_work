# 전역변수와 지역변수
# 변수의 scope가 있다.
# 함수에서 전역변수를 참조하는것은 그냥 가능하다.
# 함수에서 전역변수의 값을 수정하려면 global 선언을 해야 한다.
# global을 붙이지 않고 값을 변경하면 함수의 지역변수가 새로 만들어지는 것이다.

a = 10


def setA():
    # 전역 변수의 값을 변경 하기 위해 global 키워드 사용
    global a
    a = 200


print(a)

people = [
    {'num': 1, 'name': 'KIM', 'phone': '010-1111-1111'},
    {'num': 2, 'name': 'Lee', 'phone': '010-2222-2222'},
    {'num': 3, 'name': 'Park', 'phone': '010-3333-3333'},
]

num_seq = 3


def addDictPeople(name, phone):
    global num_seq
    num_seq += 1
    people.append({'num': num_seq, 'name': name, 'phone': phone})


addDictPeople('Ahn', '010-4444-4444')
print(people)
print('num_seq => ', num_seq)
print(people[num_seq - 1])
