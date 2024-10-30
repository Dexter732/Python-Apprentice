"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
import turtle


def set_turtle_image (turtle,image_name):

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)  
screen = turtle.Screen()
screen.setup(width=600, height=600)


t = turtle.Turtle()

set_turtle_image(t, "meowscles-fortnite.gif")



turtle.exitonclick()     
