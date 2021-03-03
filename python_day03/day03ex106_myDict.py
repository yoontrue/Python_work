class MyDict(dict):
    def __init__(self):
        # 상속 받은 클래스는 부모의 생성자 호출 반드시 필요
        super().__init__()

    def setAttribute(self, key, value):
        self[key] = value

    def getAttribute(self, key):
        return self[key]

    def size(self):
        return len(self)


mydict = MyDict()
mydict.setAttribute('name', 'gildong')
mydict.setAttribute('address', '의정부시')
print('성명 : ' + mydict.getAttribute('name'))
print('주소 : ' + mydict.getAttribute('address'))
print('크기 : ' + mydict.size())

