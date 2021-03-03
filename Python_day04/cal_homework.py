# 계산기
import tkinter as tk

calc = tk.Tk()
calc.title("계산기")
calc.geometry("350x400+100+100")

display = tk.Entry(calc, width=50)
display.pack()


calc.mainloop()

