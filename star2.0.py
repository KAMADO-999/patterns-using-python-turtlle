import turtle
import random

star= turtle.Turtle()
turtle.bgcolor("black")
star.speed(12)
colours = ["red", "blue", "white","yellow"]

for i in range(80):
    star.color(random.choice(colours))
    star.forward(i * 10)
    star.right(200)

turtle.done()