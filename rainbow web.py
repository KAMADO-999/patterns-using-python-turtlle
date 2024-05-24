import turtle
colors=['red','yellow','purple','blue','orange']
a=turtle.Pen()
a.speed(11)
turtle.bgcolor("black")

for i in range(210):
    a.pencolor(colors[i%5])
    a.width(i/100+1)
    a.forward(i)
    a.left(59)
    
turtle.done()