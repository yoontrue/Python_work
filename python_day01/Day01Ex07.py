user_list = []

for i in range(5):
    # str() 함수를 이용해서 정수를 문자열로 형변환
    user_list.append(input("사용자"+str(i)+"입력 : "))

# 입력된 정보 확인
print(user_list)