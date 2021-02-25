user_list = ['김길동','홍길동','박길동','일지매']

print(user_list)
print(type(user_list))
# print(user_list[0])

for i, name in enumerate(user_list) :
    print(i, name, end="\t")

print()

cnt = 0;
while cnt < len(user_list) :
    print(cnt, user_list[cnt], end='\t', sep=":")
    cnt+=1

print()
print(user_list[:])    # 0부터 끝까지
print(user_list[2:])   # 2부터 끝까지
print(user_list[1:3])  # 1부터 3전까지