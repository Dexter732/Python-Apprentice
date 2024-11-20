""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.speed(10)
turtle.forward(90)
turtle.forward(-90)
turtle.forward(90)
turtle.forward(-90)
turtle.forward(90)
turtle.forward(-90)
turtle.forward(90)
turtle.forward(-90)
turtle.forward(90)
turtle.forward(-90)

t1 = turtle.Turtle()
t1.pendown()
t1.shape("triangle")

t2 = turtle.Turtle()
t2.pendown()
t2.shape("circle")

t3 = turtle.Turtle()
t3.pendown()
t3.shape("square")

t4 = turtle.Turtle()
t4.pendown()
t4.shape("arrow")

t5 = turtle.Turtle()
t5.pendown()
t5.shape("square")



for i in range(-100, 100):
    t1.goto(40,20)
    t2.goto(60,-80)
    t3.goto(60,70)
    t4.goto(70,20)
    t5.goto(90,-100)
t2.forward(40)
t1.backward(60)
t3.forward(60)
t4.left(50)
t5.forward(40)
t4.forward(60)
turtle.exitonclick() 