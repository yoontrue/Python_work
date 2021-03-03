from tkinter import Tk
from tkinter.ttk import Label

x = 120
y = 80

def leftClick(event) :
    global x
    x -= 10
    lbl.place(x=x, y=y)

def wheelClick(event):
    global x
    x = 120
    lbl.place(x=x, y=y)

def rightClick(event):
    global x
    x += 10
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

lbl = Label(win, text="자연인")
lbl.place(x=x, y=y)

win.bind("<Button-1>", leftClick)
win.bind("<Button-2>", wheelClick)
win.bind("<Button-3>", rightClick)
win.bind("<MouseWheel>", scroll)


if __name__ == '__main__':
    win.mainloop()