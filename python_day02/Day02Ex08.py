lis = []

for i in range(0, 3):
    people = {}
    people['name'] = input(f'input name{i}>>')
    people['phone'] = input(f'input phone{i}>>')
    people['addr'] = input(f'input addr{i}>>')
    lis.append(people)
print(f'{len(lis)}개의 People 정보가 입력되었습니다.')

for people in lis:
    print(people)

