import json

json_data = '''[{
            "id":"kim",
            "name":"김윤진",
            "age":45
        },{
            "id":"kim",
            "name":"김유신",
            "age":42
        }]'''

# dict_list = json.loads(json_data)
# print( type(dict_list) )
# for dic in dict_list :
#     print(type(dic))
#     print(dic['name'], dic['id'], dic['age'])

with open("people.json", "w") as fp :
    json.dump(json_data, fp)

with open("people.json", "r") as fp:
    new_json_data = json.load(fp)

print( type(new_json_data) )
print(new_json_data)
print(json.loads(new_json_data))