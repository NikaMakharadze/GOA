from turtle import *

# background color
bgcolor("lightblue")

# speed
speed(999)

# width
width(4)

# draw a palace

color("#deb887")
begin_fill()
forward(300)
left(90)
forward(250)
left(90)
forward(300)
left(90)
forward(250)
end_fill()

# door

left(90)
forward(100)
left(90)
color("#8b4513")
begin_fill()
forward(170)
right(90)
forward(100)
right(90)
forward(170)
end_fill()
penup()
goto(330, 250)
pendown()

# roof

color("#8b4513")
begin_fill()
right(130)
forward(230)
left(80)
forward(230)
left(140)
forward(350)
end_fill()

# left palace

penup()
goto(300, 250)
pendown()
color("#deb887")
begin_fill()
right(90)
forward(250)
left(90)
forward(100)
left(90)
forward(280)
left(90)
forward(100)
left(90)
forward(280)
end_fill()

# left palace roof

color("#8b4513")
penup()
goto(430, 280)
pendown()
begin_fill()
right(130)
forward(100)
left(80)
forward(100)
left(140)
forward(150)
end_fill()

# right palace

color("#8b4513")
penup()
goto(0, 0)
pendown()
color("#deb887")
begin_fill()
left(180)
forward(100)
right(90)
forward(280)
right(90)
forward(100)
right(90)
forward(280)
end_fill()

# right palace roof

color("#8b4513")
penup()
goto(-130, 280)
pendown()
begin_fill()
left(130)
forward(100)
right(80)
forward(100)
right(140)
forward(150)
end_fill()

# windows & width
width(2)

# right palace 1 window

penup()
goto(-80, 80)
pendown()
color("#add8e6")
begin_fill()
left(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

# right palace 2 window

penup()
goto(-80, 150)
pendown()
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

# left palace 1 window

penup()
goto(380, 80)
pendown()
begin_fill()
left(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

# left palace 2 window

penup()
goto(380, 150)
pendown()
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

# main palace window 1

penup()
goto(280, 150)
pendown()
color("#add8e6")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

# main palace window 2

penup()
goto(60, 150)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

# GOA flag

penup()
goto(-150, 330)
pendown()
color("black")
write("GOA", align="center", font=("Arial", 20, "bold"))
penup()
goto(-200, 357)
pendown()
color("red")
right(45)
forward(20)
right(100)
forward(20)
right(125)
right(90)
forward(90)
left(90)
forward(27)
left(90)
forward(90)

penup()
goto(-112, 350)
pendown()
left(90)
forward(70)

# king

color("blue")
penup()
goto(500, 150)
pendown()
circle(10) # head

penup()
goto(510, 140)
pendown()
forward(60) # body

penup()
goto(510, 125)
pendown()
right(45) # left hand
forward(20)

penup()
goto(510, 125)
pendown()
left(100) # right hand
forward(20)

penup()
goto(510, 80)
pendown()
right(90) # left foot
forward(20)

penup()
goto(510, 80)
pendown()
left(75) # right foot
forward(20)

# king text

penup()
goto(510, 200)
pendown()
color("black")
write("King", align="center", font=("Arial", 15, "bold"))

# queen

color("#aa336a")
penup()
goto(-200, 150)
pendown()
circle(10) # head

penup()
goto(-190, 145)
pendown()
right(40)
forward(60) # body

penup()
goto(-190, 130)
pendown()
right(45) # left hand
forward(20)

penup()
goto(-190, 130)
pendown()
left(100) # right hand
forward(20)

penup()
goto(-190, 85)
pendown()
right(90) # left foot
forward(20)

penup()
goto(-190, 85)
pendown()
left(75)
forward(20)

# queen text

penup()
goto(-190, 200)
pendown()
color("black")
write("Queen", align="center", font=("Arial", 15, "bold"))

hideturtle()
done()
