from tkinter import Tk, PanedWindow, LabelFrame, Menu
from tkinter.ttk import Label, Entry, Button

win = Tk()

menu_area = Menu(win)
win.config(menu=menu_area)

menu1 = Menu(menu_area)
menu1.add_command(label="New ...")
menu_area.add_cascade(label="File", menu=menu1)

menu2 = Menu(menu_area)
menu2.add_command(label="About ...")
menu_area.add_cascade(label="Help", menu=menu2)

label_frame = LabelFrame(win, text='label frame')
label_frame.grid(row=0, column=0, padx=5, pady=5)

lbl_name = Label(label_frame, text="성명: ")
lbl_phone = Label(label_frame, text="전화번호: ")
lbl_email = Label(label_frame, text="이메일: ")

entry_name = Entry(label_frame)
entry_phone = Entry(label_frame)
entry_email = Entry(label_frame)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, padx=5, pady=5)
lbl_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1, padx=5, pady=5)
lbl_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1, padx=5, pady=5)

penedwindow = PanedWindow(relief="raised", bd=0)
penedwindow.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

btn_ok = Button(penedwindow, text="확인")
btn_cancel = Button(penedwindow, text="취소")
penedwindow.add(btn_ok)
penedwindow.add(btn_cancel)

if __name__ == '__main__':
    win.mainloop()