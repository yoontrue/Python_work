# 함수에 여러 인수 전달 예제
# 호출시 여러개의 인수를 튜플형식으로 받기

def findMax(*args):
    print('args의 타입은 ', type(args))

    max = 0

    for num in args:
        if num > max:
            max = num

    return max


# 정해져 있지 않은 양의 인수를 전달한다.
maxnum = findMax(2, 5, 40, 100, 7, 9)
print(maxnum)
maxnum = findMax(2, 5, 50)
print(maxnum)
maxnum = findMax(5000)
print(maxnum)


def mkVerticalTotal(*scoreList):
    totalList = [];
    for list in scoreList:
        # 만약에 totalList에 index가 있다면 누적하고
        # 아니라면 list에 append() 해준다.
        for i, score in enumerate(list):
            try:
                totalList[i] += score
            except:
                totalList.append(score)

    return totalList


'''
[60,60,60]
[90,90,90]
[30,30,30,100]
--------------
결과 : [180,180,180,100]
'''
totalList = mkVerticalTotal([60, 60, 60], [90, 90, 90], [30, 30, 30, 100])
print(totalList)
