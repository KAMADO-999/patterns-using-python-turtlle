import turtle
a=turtle.Turtle()
b=turtle.Screen()
b.bgcolor("black")
a.pencolor("green")

x=0
y=0
a.speed(0)
while True:
    a.forward(x)
    a.right(y)
    x=x+3
    y=y+1
    if b==215:
        turtle.hideturtle()
        turtle.done()