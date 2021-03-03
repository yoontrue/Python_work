from tkinter import Tk
from tkinter.ttk import Label, Entry, Button

win = Tk()

def msg_log() :
    msg = entry.get()
    print(msg, "입력 하였습니다!")
    lbl.config(text="Message : "+msg)


win.geometry("640x480+200+200")

lbl = Label(win, text="성명 입력: ")
lbl.pack()
entry = Entry(win)
entry.pack()
btn = Button(win, text="확인", command=msg_log)
btn.pack()



if __name__ == '__main__':
    win.mainloop()