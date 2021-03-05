import json
from socket import socket
from tkinter import Tk, Canvas
from tkinter.ttk import Button
from turtle import TurtleScreen, RawTurtle

from _socket import AF_INET, SOCK_STREAM


class App :
    def __init__(self):
        self.win = Tk()
        self.btn = Button(self.win, text="확인", command=self.press)
        self.btn.pack()

        self.canvas = Canvas(self.win)
        self.canvas.config(width=600, height=300)
        self.canvas.pack()
        self.src = TurtleScreen(self.canvas)
        self.t = RawTurtle(self.src)
        self.t.pensize(5)

        # 서버와 소켓 연결
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(('127.0.0.1',9999))


    def move(self):
        print("터틀 제어하기")
        # 서버에서 받은 데이터로 터틀을 제어한다.
        data = self.client.recv(1024)
        obj = json.loads(data.decode('utf-8'))
        direction = obj['direction']
        angle = obj['angle']
        self.t.left(angle) if direction=='L' else self.t.right(angle)
        self.t.forward(obj['length'])


    def press(self):
        self.client.send('I am Client^^'.encode('utf-8'))
        print("서버에 메세지 보내기")
        # 터틀 제어하기
        self.move()

if __name__ == '__main__':
    app = App()
    app.win.mainloop()