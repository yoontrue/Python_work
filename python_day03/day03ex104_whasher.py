# 세탁기 클래스 선언
class Washer:
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        detergent()  # 외부에 있는 메소드 호출할 땐 self. 붙이지 않고 걍 호출
        print('{}세탁기가 {}키로의 빨래를 한다.'.format(self.maker, self.size), self.__str__())  # 동적바인딩


def detergent():
    print('세제투입')


# 세탁기를 상속 받아서 LGWasher를 선언한다.
class LGWasher(Washer):
    def __init__(self, size, maker, name):
        # 부모의 생성자 호출
        super().__init__(size, maker)
        self.name = name

    def info(self):
        print(f'사이즈 : {self.size}\n제조사 : {self.maker}\n제품명 : {self.name}')

    def __str__(self):
        return 'name:%s' % self.name

# 모듈로 사용되는 파일에서 필수 구현
if __name__ == '__main__':
    washer = LGWasher(10, 'LG', '트롬')
    washer.washing()
