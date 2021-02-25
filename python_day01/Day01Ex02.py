# (문자열 * 숫자)가 가능하다.
# 곱한만큼 문자열을 반복하라

print("-" * 3)

# 문자열 가운데에 제목 출력하기
print("{:-^30}".format(" 제 목 "))
print("{:=^30}".format(" 제 목 "))
print("{:-<30}".format(" 제 목 "))
print("{:->30}".format(" 제 목 "))

# format() 함수 이용
print("나이:{}, 인사{}, 파이:{}".format(100, "HELL", 3.14))

# 변수 선언하기
user_name = "홍길동"
age = 300
address = "서울시 종로구 견지동"

str = """
성명 : {}
나이 : {}
주소 : {}
""".format(user_name, age, address)
print(str)

# printf처럼 사용하기
# %뒤에 튜블 데이터를 이용해서 포맷한다.
print("%s, %d, %s" %('KIM',25,'서울시 은평구 응암동'))