# 쓰기 모드로 open하면 파일이 없을 때 생성
# 읽기 모드에서 파일이 없으면 오류!
# 한글 기록을 위해 encoding 속성 지정
# fp = open("io_test.txt", "w", encoding="utf-8")
#
# fp.write("Hello world\n")
# fp.write("건강한 나라 대한민국\n")
# fp.write("즐거운 파이썬 공부\n")
#
# fp.close()


# with 구문을 사용하면 자동으로 close 한다
with open("io_test.txt","w", encoding="utf-8") as fp :
    fp.write("Hello world\n")
    fp.write("우리나라 좋은나라~\n")
    fp.write("충성\n")