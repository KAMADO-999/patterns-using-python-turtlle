from turtle import *
from colorsys import hsv_to_rgb
tracer(5)
bgcolor('black')
pensize(2)
h = 0.5  

for i in range(155):
    color(hsv_to_rgb(h, 1, 1))  
    h += 0.004  
    for j in range(4):
        forward(i)
        right(20)
        forward(i)
        right(40)
        forward(i)
        right(120)
    right(5)  
done()
