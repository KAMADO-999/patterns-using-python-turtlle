from turtle import *
from colorsys import hsv_to_rgb
tracer(10)  
bgcolor('black')
pensize(2)
h = 0  
for i in range(360):
    color(hsv_to_rgb(h, 1, 1))  
    h += 0.003  
    forward(i * 0.5)  
    right(59)  
    circle(i * 0.2, 180)  
done()
