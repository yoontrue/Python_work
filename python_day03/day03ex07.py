# 디폴트 매개변수
# 함수를 선언 할 때 매개변수의 기본 값을 정해준다.
# 함수 호출시 디폴트 매개변수에 해당하는 인자를 생략 가능하다.
# 디폴트 매개변수 뒷 순서로 오는 매개변수들은 일반 매개변수 안됨. 꼭 디폴트 매개변수여야함
def showInfo(id, name='no-name', age=0):
    print('id:', id)
    print('name: ', name)
    print('age: ', age)


showInfo('kim')

# 함수를 호출 할 때 매개변수를 지정해 주면 위치가 바뀌어도 상관없다.
showInfo(age=30, name='홍길동', id='hong')
