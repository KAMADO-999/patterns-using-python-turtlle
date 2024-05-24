import turtle
import random
a=turtle.Turtle()
b=turtle.Screen()
turtle.bgcolor("black")
colours=['red', 'magenta', 'blue', 'cyan', 'green', 'white','yellow']
a.speed(12)
a.forward(50)
a.left(160)


for i in range(200):
     a.color(random.choice(colours))
     a.circle(100, 60-i)
     a.left(i)


turtle.done()