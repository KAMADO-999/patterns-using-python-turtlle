import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(12)

n = 36
h = 0

for i in range(150):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    for j in range(7):
        t.forward(200)
        t.left(150)
turtle.hide()
turtle.done()