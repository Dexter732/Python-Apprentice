"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
tina.circle(30,180)
tina.forward(70)
tina.circle(30,180)
tina.forward(70)
tina.penup()
tina.forward(70)
tina.pendown()
tina.left(90)
tina.forward(60)
tina.circle(75,180)
tina.penup()
tina.forward(60)
tina.pendown()
tina.forward(140)
tina.circle(27,180)
tina.forward(50)
tina.circle(-21,180)
tina.forward(50)
tina.circle(27,180)
tina.forward(200)
tina.right(90)
tina.circle(-40,90)
tina.forward(70)
tina.circle(-40,90)
tina.penup()
tina.forward(80)
tina.right(90)
tina.forward(150)
tina.right(180)
tina.pendown()
tina.circle(-30,90)
tina.forward(60)



turtle.exitonclick()

