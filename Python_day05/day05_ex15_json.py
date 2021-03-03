from pprint import pprint

s = "무궁화 꽃이 피었습니다.".encode('utf-8')

# print(s.decode('utf-8'))

# pprint(s, width=10, indent=4)
#
# lis = [[1,2],[3,4],[5,6]]
# pprint(lis, width=15,indent=4)

json_data = '''[
    {
    "id":"kim",
    "name":"김윤진",
    "age":45
    },{
    "id":"kim",
    "name":"김윤진",
    "age":45
    }
]'''.encode('utf-8')
print(json_data.decode())