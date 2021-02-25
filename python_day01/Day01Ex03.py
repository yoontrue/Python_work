user_name = input('성명 입력 >>')
age = int(input('나이 입력 >>'))
address = input('주소 입력 >>')

strr = """
성명 : {0}
나이 : {1}
주소 : {2}
""".format(user_name, age, address)

print(strr)

print('성명 : ' + user_name)
print('나이 : ' + str(age))
print('주소 : ' + address)

# 10년 후에 ~~님은 ~~세 입니다.
print('{}년후에 {}님은 {}세 입니다.'.format(10,user_name,age+10))
# 에러가 나는데, input() 결과형은 문자열이기 때문에
# 정수형으로 사용하기 위해서 형변환해야한다.
# int(input()) 해주기~
# 정수와 문자열을 연산하면 오류가 발생한다.
# 연산을 하기 위해서는 두 항의 타입이 같아야 한다.