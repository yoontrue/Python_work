
with open("io_test.txt","r",encoding="utf-8") as fp :
    data = fp.read()
    print(data)


with open("io_test.txt","r",encoding="utf-8") as fp :
    while True :
        data = fp.readline()
        print(data[:-1])
        if not data :
            break


with open("io_test.txt","r",encoding="utf-8") as fp :
    lines = fp.readlines()
    print(lines)
    for line in lines :
        print(line[:-1])