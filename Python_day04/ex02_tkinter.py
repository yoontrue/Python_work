import tkinter as tk
from tkinter.ttk import Button, Label

win = tk.Tk()

lbl = Label(win, text="안녕하세요!")
lbl.pack()

btn = Button(win, text="확인")
btn.pack()

if __name__ == '__main__':
    win.mainloop()