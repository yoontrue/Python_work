from tkinter import Tk
from tkinter.ttk import Label

win = Tk()

top_label = Label(win, text="top", background="Cyan")
top_label.pack(side="top", fill="x")

top_label = Label(win, text="bottom", background="Cyan")
top_label.pack(side="bottom", anchor="e")

left_label = Label(win, text="right", background="Blue")
left_label.pack(side="right", fill="y")

left_label = Label(win, text="left", background="Blue")
left_label.pack(side="left", fill="y")

