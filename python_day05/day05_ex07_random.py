# 랜덤
import random
from random import *

# 1보다 작은 실수인 난수
num = random()
print('random.random() =>', num)

# 인수로 주어진 a,b 사이의 난수
num = uniform(4,6)
print("uniform => ", num)

# 0부터 인수로 주어진 범위 안에서 난수 발생
num = randrange(5)
print("randrange =>", num)

# 105부터 ~ 109까지 사이에서 2개씩 증가하는 수만 뽑아줌
num = randrange(105,110,2)
print("randrange =>", num)

# 리스트에서 랜덤한 위치의 값을 뽑아온다.
num = choice(list(range(5,11)))
print("choice =>", num)

# shuffle, randint ...