import socket
import sys

server_url = ('127.0.0.1', 9999)

client = socket.socket()
client.connect(server_url)

# 전송 할 파일을 열어준다.
# 일반적인 파일, json, 객체
with open("C:\\Users\\bit\\Pictures\\img01.png", "rb") as fp :
    data = fp.read(1024)
    while(data) :
        client.send(data)
        data = fp.read(1024)

    print('사진 파일을 서버로 전송 완료 했습니다.')

client.close()
