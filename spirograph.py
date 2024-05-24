import turtle
import random
star= turtle.Turtle()
colours=['red', 'magenta', 'blue', 'cyan', 'green', 'white','yellow']
turtle.bgcolor('black')
star.pensize(2)
star.speed(12)

for i in range(60):
 star.color(random.choice(colours))
 star.circle(100)
 star.left(10)
	
turtle.hideturtle()
	

turtle.done()
