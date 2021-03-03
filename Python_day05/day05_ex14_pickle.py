import pickle
from pprint import pprint
person1 = {
    'name' : '홍길순',
    'height' : 170,
    'weight' : 60
}
person2 = {
    'name' : '홍길동',
    'height' : 180,
    'weight' : 90
}

people = [person1, person2]

# 덤프가 저장, 로드가 읽기
with open('people.pickle', 'wb') as f :
    pickle.dump(people,f)

with open('people.pickle', 'rb') as f :
    new_list = pickle.load(f)

print(new_list)
pprint(new_list)