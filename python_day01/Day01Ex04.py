import math

# 연습문제

# 반지름을 입력받아서 둘레의 길이와 면적을 구한다.
# 둘레 : 2파이r
# 면적 : 파이r^2

# 연산하기
r = int(input('반지름 : '))
area = math.pi * r**2
round = 2 * math.pi * r

# 출력하기
print('반지름이 {}인 원의 면적은 {}이고 둘레는 {}이다.'.format(r, area, round))