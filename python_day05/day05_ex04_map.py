def mult(i):
    return i * 10

lis = [10,20,30,40]

result = map(mult, lis)

while True :
    try:
        print(result.__next__())
    except :
        break