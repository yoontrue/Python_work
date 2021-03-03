import random
import turtle
import tkinter as tk
from tkinter import Button
from turtle import Canvas, TurtleScreen, RawTurtle

colors = ['Red', 'Green', 'Blue']
class App :
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("640x400")
        self.canvas = Canvas(self.win);
        self.canvas.pack()
        self.scr = TurtleScreen(self.canvas)
        self.t = RawTurtle(self.scr)
        self.btn = Button(self.win, text="Press me!", command=self.do_action)
        self.btn.pack()


    def do_action(self):
        self.t.goto(0,0)
        self.t.pensize(3)
        self.t.pencolor(random.choice(colors))
        self.t.speed(0)

        self.length = 5
        while self.length < 500:
            self.t.left(89)
            self.t.forward(self.length)
            self.length += 3


    def run(self):
        self.win.mainloop()


if __name__ == '__main__':
    app = App()
    app.run();