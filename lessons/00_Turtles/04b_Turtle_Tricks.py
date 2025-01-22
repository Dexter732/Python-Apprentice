"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward(30) and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor(black)


... # Your code here
def square():
    tina.penup()
    tina.left(90)
    tina.forward(100)
    tina.right(90)
    tina.pendown()
    tina.forward(150)
    tina.right(90)
    tina.forward(300)
    tina.right(90)
    tina.forward(300)
    tina.right(90)
    tina.forward(300)
    tina.right(90)
    tina.forward(150)


for i in range(1):
  square()

tina.penup()
tina.right(90)
tina.forward(50)
tina.penup()
tina.left(90)
tina.forward(-75)
tina.pendown()
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)

tina.begin_fill()
tina.fillcolor()
tina.end_fill()
tina.penup()
tina.forward(225)
tina.penup()
tina.pendown()
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
turtle.exitonclick()