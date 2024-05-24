import turtle


sc = turtle.Screen()
turtle.bgcolor("yellow")
pen = turtle.Turtle()


def drawing():

  for i in range(4):
    pen.forward(30)
    pen.left(90)

  pen.forward(30)



# Driver code
if __name__ == "__main__" :

    # setting up-screen
    sc.setup(600, 600)

    pen.speed(100)

 
    for i in range(8):

     
      pen.up()

     
      pen.setpos(0, 30 * i)

      pen.down()

   
      for j in range(8):

        if (i + j)% 2 == 0:
          col ='black'

        else:
          col ='white'

        
        pen.fillcolor(col)

        
        pen.begin_fill()

      
        drawing()
       
        pen.end_fill()

    
    pen.hideturtle()

turtle.done()