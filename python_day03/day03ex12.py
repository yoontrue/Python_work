# 람다 표현식
# 람다함수는 익명 함수이다.
'''
Lambda 매개변수 : 처리식

참일때실행 if 조건 else 거짓일때실행
'''


# 일반적인 파이썬 함수 선언
def maximum(x, y):
    if x > y:
        return x
    else:
        return y


result = maximum(10, 20)
print('result => ', result)

########## 위 함수를 lambda 표현식으로 변경 ##########
result = (lambda x, y: x if x > y else y)(5, 10)
print('람다 실행 결과 : ', result)

print('결과 : ', (lambda x, y: x if x > y else y)(500, 10000))

# 람다 함수 응용
fishs = ['갑오징어', '꼴뚜기', '복', '명태', '바다거북이']
fishs.sort(key=lambda x: len(x))
print(fishs)

fncList = [
    lambda msg: print('첫번째 함수', msg),
    lambda msg: print('첫번째 함수', msg),
    lambda msg: print('첫번째 함수', msg)
]

fncList[0]('hello')
fncList[1]('world')
fncList[2]('good bye')
