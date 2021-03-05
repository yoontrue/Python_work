
# client에서 요청을 받으면 서버에서 좌표를 보낸다.
from socket import socket, AF_INET, SOCK_STREAM

serv_url = ('127.0.0.1',9999)
server = socket(AF_INET, SOCK_STREAM)
server.bind(serv_url)
server.listen(1)

connection, addr = server.accept()
print(f'{addr}에서 접속이 확인되었습니다.') # 접속이 되었을때..

# 데몬형태로 대기하기
while True :
    data = connection.recv(1024)
    print('받은 데이터:', data.decode('utf-8'))

    # 클라이언트로 데이터 전송
    send_data = '''{
        "direction":"L",
        "angle":90,
        "length":100
    }'''.encode('utf-8')
    connection.send(send_data)
    print(">>> 클라이언트로 데이터 전송 완료!")