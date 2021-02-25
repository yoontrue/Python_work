if True :
    print('sum을 0으로 초기화 했다.')
    sum = 0

for i in range(1,11):
    # 변수의 스코프가 함수 단위이다.
    # 즉, 제어문 안에서 변수를 선언해도
    # 밖에서 사용가능하다.
    sum += i

# 제어문 안에서 선언된 변수를 그냥 사용가능하다.
print("sum => ", sum)

