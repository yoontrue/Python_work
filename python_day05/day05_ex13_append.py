with open("io_test.txt","a", encoding="utf-8") as fp :
    for i in range(5,8) :
        data = f'{i}번째 라인...\n'
        fp.write(data)

with open("io_test.txt","r",encoding="utf-8") as fp :
    data = fp.read()
    print(data)