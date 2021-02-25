p_list = []
p_list.append({'name':'hong','phone':'010-2345-1234'})
p_list.append({'name':'kim','phone':'010-1111-2222'})
p_list.append({'name':'yoon','phone':'010-3333-4444'})

for people in p_list:
    keys = list(people.keys())
    values = list(people.values())
    # print(type(keys))
    for i, key in enumerate(keys):
        print(f'{key} : {values[i]}')
    print('-'*50)
