from tkinter import Tk, PanedWindow
from tkinter.ttk import Label, Entry, Button

win = Tk()

lbl = Label(win, text="성명: ")
entry = Entry(win)

lbl.pack()
entry.pack()

penedwindow = PanedWindow(relief="raised", bd=0)
penedwindow.pack()

btn_ok = Button(penedwindow, text="확인")
btn_cancel = Button(penedwindow, text="취소")
penedwindow.add(btn_ok)
penedwindow.add(btn_cancel)

if __name__ == '__main__':
    win.mainloop()