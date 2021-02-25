dict1 = {}
dict1 = dict()
print(type(dict1))
print(len(dict1))

# 공 셋 생성
set_st = set()
# 셋 초기화 하기
# set_st = {None, }
print(type(set_st))
print(len(set_st))

dict1['name'] = 'hong'
dict1['addr'] = '서울시 종로구 견지동'

print(dict1)

del dict1['addr']

print(dict1)