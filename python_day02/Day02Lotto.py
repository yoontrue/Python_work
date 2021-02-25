# 연습문제
# 로또번호 생성기
import random

# set으로 선언해서 중복된 값이 들어가지 않도록 한다.
lotto = set()

while 6 > len(lotto) :
    # 1~45중에 랜덤한 값 뽑기
    number = random.randint(1,45)
    # lotto가 set구조라 이전에 뽑았던 숫자와 다른 숫자일 경우에만 추가된다.
    lotto.add(number)

print(lotto)

# 1~45까지 들어있는 ball이라는 리스트를 생성
ball = list(range(1,46))
# print(ball)
lotto2 = set()
while 6 > len(lotto2) :
    # ball에 들어있는 숫자중 랜덤하게 choice해서 lotto2에 추가.
    # 대신 lotto2는 set구조라서 이전 값들과 숫자가 겹치지 않을경우에만 추가된다.
    lotto2.add(random.choice(ball))

print(lotto2)