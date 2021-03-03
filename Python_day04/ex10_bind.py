# 마우스 이벤트 같은거는 bind 로
from tkinter import Tk
from tkinter.ttk import Label

x=150
y=100

def mouseEvtHandler(event) :
    global x,y
    x, y = (event.x, event.y)
    print(f'{x}, {y}')
    lbl.place(x=x, y=y)

def scoll(event) :
    global y
    if event.delta == -120 : #업스크롤
        y += 10
    if event.delta == 120 : #다운 스크롤
        y -= 10
    lbl.place(x=x, y=y)

win = Tk()

win.geometry("300x200+100+100")

lbl = Label(win, text="하이")
lbl.place(x=150, y=150)

# 왼쪽 마우스 B1 오른쪽 마우스 B2
win.bind("<B1-Motion>", mouseEvtHandler)
# 파이썬은 꺽새안에 태그처럼
win.bind("<MouseWheel>", scoll)

if __name__ =='__main__' :
    win.mainloop()
