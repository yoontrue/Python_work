import socket

print('클라이언트 소켓 준비')
server_url = ('127.0.0.1', 9999)

client = socket.socket()

# 서버접속
client.connect(server_url)
print('서버 접속 중 ...')

# 서버로 메세지 전송
client.send(b'Hello I am client!')
print('서로보 메세지를 보냈습니다.')

# 서로보 부터 메세지 받기
msg = client.recv(1024)
print("서버에서 보낸 메세지:", msg)

client.close()