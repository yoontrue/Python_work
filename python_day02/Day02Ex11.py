s = {'사과','오렌지','딸기','사과','딸기'}
print(len(s))
# set의 내용을 비워준다.
s.clear()
print(len(s))

s.add('오징어')
s.add('오징어')
s.add('오징어')
s.add('꼴뚜기')
s.add('꼴뚜기')
print(len(s))
print(s)
s.remove('꼴뚜기')
# .remove 는 없는걸 지우겠다고하면 오류남
s.discard('aaa')
# .discard 도 remove처럼 지우는 메소드인데, 없는걸 지워도 오류안난다.

try :
    s.remove('bbbb')
except :
    print('bbbb는 존재하지 않아서 지울수가 없습니다.')
