# 여러 값을 반환하는 함수
def fn():
    return 10,5,30

# a=10 , b=5 , c=30 이 담긴다.
a,b,c = fn()

print(a,b,c)

num1 = 100
num2 = 200

# swap
(num1,num2) = (num2,num1)

print(num1,num2)

def show_number(number):
    print('전달 받은 number => ',number)

show_number(5)

# 매개변수의 갯수와 순서는 인자의 순서와 갯수와 일치해야 한다.
def show_people(name,age=10):
    print(f'name:{name}   age:{age}')

# 매개변수의 인자의 갯수는 일치해야 한다.
show_people('김윤진',30)
# 매개변수 선언시 기본값을 지정해놓으면 인자를 생략 가능하다.
show_people('이순신')