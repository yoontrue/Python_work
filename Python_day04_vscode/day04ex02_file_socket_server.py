import socket
import sys

server_url = ('127.0.0.1', 9999)

server = socket.socket()
server.bind(server_url)
server.listen(5)
print('서버에서 파일 받을 준비 중 ...')

i = 1
while True :
    client, address = server.accept()
    with open('newFile'+str(i)+'.png', 'wb') as fp :
        data = client.recv(1024)
        while(data) :
            fp.write(data)
            data = client.recv(1024)

        print("파일을 성공적으로 전송 받았습니다!")

    client.close()
    i += 1

server.close()