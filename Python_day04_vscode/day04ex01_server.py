import socket

server = socket.socket()
# p2p 방식 : 당나귀, 파일구리 ...  pc : pc
# client-server : 서버와 클라이언트가 소로 통신한다. socket, socketserver

server.bind(('127.0.0.1', 9999) )
server.listen(1)
print('server is ready ...')

# 클라이언트 접속 수락
client, addr = server.accept()
print("client connected ...")

# 메세지 수신하기
msg = client.recv(1024)
print('메세지 수신:', msg)

# 메세지를 클라이언트로 송신 해준다.
client.sendall(b'Hi^^ I am server')
print("클라이언트로 메세지를 송신 했습니다!")

# 클라이언트 연결 해지
client.close();
server.close();