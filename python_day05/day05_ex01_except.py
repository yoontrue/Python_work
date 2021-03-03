import logging
from time import sleep

while True:
    try:
        age = int(input("나이 입력 >> "))
        print("입력 된 나이는", age)
        break
    except:
        logging.warning("나이는 정수로 입력하세요!")
        sleep(0.5)
        continue

print("프로그램 종료!")
