import turtle
import random
dist = 1
flag = 500
spirals = turtle.Turtle()
#adding colors to make more intersting
colours = ["red", "blue", "yellow","green"]
turtle.bgcolor("black")
spirals.speed(12)

while flag:


	spirals.forward(dist)
	spirals.left(120)
	spirals.left(1)
	spirals.color(random.choice(colours))
	dist=dist+1
	flag=flag-1
    


turtle.done()
