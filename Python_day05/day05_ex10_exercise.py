from turtle import Turtle

data = [{
    "direction" : "L",
    "angle" : 0,
    "length" : 200
},{
    "direction" : "L",
    "angle" : 90,
    "length" : 100
},{
    "direction" : "R",
    "angle" : 90,
    "length" : 50
},{
    "direction" : "R",
    "angle" : 90,
    "length" : 100
},{
    "direction" : "L",
    "angle" : 90,
    "length" : 200
}]

t = Turtle()
t.color("RED")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(-300,0)
t.pendown()

def moveTurtle() :
    for data in data_list:
        direction = data['direction']
        angle = data['angle']
        length = data['length']

        t.left(90) if direction=='L' else t.right(angle)
        t.forward(100)

for i in range(5):
    moveTurtle()

input("Press any key")