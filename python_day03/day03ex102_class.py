# 앞에서 사용한 딕셔너리 구조를 class로 변경
# 클래스 선언은 class 키워드를 이용한다.
'''
class 클래스명(상속) :
    생성자메소드
    멤버메소드
    멤버필드
'''


class People:
    # 생성자 메소드 선언, 생성자와 멤버메소드는 self 매개변수가 선언 되어야한다.
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greeting(self):
        return self.name + '님 안녕!'


# 객체 생성 시 자바처럼 new 사용하지 않는다
kim = People('kim')
pList = [kim, People('lee'), People('park')]

pList[0].setName('hong')

for person in pList:
    print('인사 >>> ', person.greeting())
