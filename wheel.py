from turtle import *
from colorsys import hsv_to_rgb
speed(0)  
bgcolor("black")
h = 0.1  
def p(size):
    global h
    for i in range(4):  
        c = hsv_to_rgb(h, 1.0, 1.0)  
        fillcolor(c)  
        h += 0.004  
        begin_fill()  
        forward(size)  
        right(20)
        forward(size)
        right(90)
        end_fill()  

for i in range(180):  
    p(size=80)  
    goto(0, 0)  
    right(2)  

done()
