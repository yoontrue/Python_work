from tkinter import Tk
from tkinter.ttk import Label

x = 150
y = 100

def mouseEvtHandler(event) :
    global x,y
    x, y = (event.x, event.y)
    print(f'{x}, {y}')
    lbl.place(x=x, y=y)


def scroll(event) :
    global y
    if event.delta == -120 : # 업스크롤
        y += 10
    if event.delta == 120 : # 다운스크롤
        y -= 10
    lbl.place(x=x, y=y)

win = Tk()

win.geometry("300x200+100+100")

lbl = Label(win, text="나는 자연인이다")
lbl.place(x=x, y=y)


win.bind("<B1-Motion>", mouseEvtHandler)
win.bind("<MouseWheel>", scroll)

if __name__ == '__main__':
    win.mainloop()