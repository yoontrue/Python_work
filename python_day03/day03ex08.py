# 함수에서 결과값을 여러개 전달 가능
def getInfo() :
    return "kim", "kimyoonjin", 24

# 튜플
# (a, b) = (b, a)
(id, name, age) = getInfo()

print(id, name, age)