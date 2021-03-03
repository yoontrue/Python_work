# 리스트에 함수를 담아서 사용하기

def fncA() :
    return "첫번째 함수 실행"

def fncB() :
    return "두번째 함수 실행"

def fncC() :
    return "세번째 함수 실행"

factory = [fncA, fncB, fncC]

for fn in factory :
    message = fn()
    print(message)

print("-"*30)
print( factory[0]() )