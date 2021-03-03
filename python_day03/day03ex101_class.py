# 파이썬 객체와 클래스
# 딕셔너리와 객체는 비슷한 구조이다.
# 딕셔너리      :       객체
# 키          :       필드, 속성 (멤버변수) - 명사
# value      :        value
# 기능 없다    :        method적 (멤버함수) - 기능, 동사적


# 딕셔너리를 객체처럼 사용해 보기
# 딕셔너리는 []를 이용해서 하위멤버 접근한다.
# 객체는 점(.)을 이용해서 하위멤버 접근한다.
test = {'name': 'hong'}

print(test['name'])
print(test.get('name'))


# 자바에서 쓰는방법
# test.setName('kim')
# name = test.getName()


# 객체처럼 사용해보기 ###########################
# 딕셔너리를 사용하는 방법으로는 부적절하다.###########
def setAttr(key, name, self=test):
    self[key] = name


def getAttr(key, self=test):
    return self[key]


test['setAttr'] = setAttr
test['getAttr'] = getAttr

test['setAttr']('name', 'kim')
name = test['getAttr']('name')
print('name => ', name)

test['setAttr']('addr', '서울시 종로구 견지동')
addr = test['getAttr']('addr')
print('addr => ', addr)
# 객체처럼 사용해보기 ###########################
# 딕셔너리를 사용하는 방법으로는 부적절하다.###########
