def aa():
    print('aa메소드')

def bb():
    print('bb메소드')

def cc():
    print('cc메소드')

# 선언된 함수를 리스트에 담기
factorys = [aa,bb,cc]

# 리스트에 있는 함수를 한꺼번에 실행하기
for fn in factorys:
    fn()