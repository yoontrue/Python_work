# 딕셔너리 사용하기
dict = {'name':'홍길동','phone':'010-1234-1234','addr':'서울시 은평구 응암동'}

print(dict)

# 딕셔너리의 요소에 접근하는 방법
print('name:', dict['name'])
print('phone:', dict['phone'])
print('addr: ', dict['addr'])
print('-'*40)
print('name: ', dict.get('name'))
print('phone: ', dict.get('phone'))
print('addr: ', dict.get('addr'))