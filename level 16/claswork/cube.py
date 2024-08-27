# 7)
from turtle import *

speed(0)
width(7)

for i in range(4):
    forward(250)
    left(90)

penup()
goto(-280, 0)
pendown()

for i in range(4):
    forward(250)
    left(90)

penup()
goto(-280, -280)
pendown()

for i in range(4):
    forward(250)
    left(90)

penup()
goto(0, -280)
pendown()

for i in range(4):
    forward(250)
    left(90)

hideturtle()
exitonclick()
