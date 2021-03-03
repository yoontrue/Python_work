# 연습문제) 자바 시간에 만든 Circle 클래스를 구현하라.
# 생성자에서 반지름 입력
# 넓이와 둘레의 길이를 계산하는 Circle 클래스
import math


class Circle:
    def __init__(self, r):
        self.r = r
        self.mkArea()
        self.mkLine()

    def mkArea(self):
        self.area = math.pi * self.r ** 2

    def mkLine(self):
        self.line = math.pi * self.r * 2

    def toString(self):
        return f'둘레는 {self.line} 면적은 {self.area}'

    def __str__(self):
        return f'area:{self.area}, line:{self.line}'


pizza = Circle(10)
print('pizza 크기 >> ', pizza.toString())
print('pizza 크기 >> ', pizza)
