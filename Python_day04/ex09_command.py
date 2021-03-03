# Button 이벤트 핸들러
from tkinter import Tk
from tkinter.ttk import Label, Entry, Button

def btnEvtHandler() :
    print("버튼이 클릭되었습니다!")
    # 성명을 입력하고 확인 버튼을 누르면 lbl에 내용이 바뀐다
    value = entry.get()
    lbl.config(text=value+"님 반갑습니다^^")

win = Tk()

lbl = Label(win, text="성명: ")
entry = Entry(win)
btn= Button(win, text="확인", command=btnEvtHandler)

lbl.pack()
entry.pack()
btn.pack()

if __name__ == '__main__':
    win.mainloop()