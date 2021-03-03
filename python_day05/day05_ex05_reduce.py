from functools import reduce

def sum(x,y):
    return x+y

lis = list(range(1,11))
print(lis)

total = reduce(sum, lis)
print("total:",total)