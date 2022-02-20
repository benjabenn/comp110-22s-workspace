"""Tutorial for Python's turtle graphics library."""

from turtle import Turtle, colormode, done
colormode(255)
side_length: float = 500

leo: Turtle = Turtle()

leo.pencolor(40, 40, 200)
leo.fillcolor(63, 95, 91)
leo.speed(50)

leo.penup()
leo.goto(-220, -75)
leo.pendown()
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1

leo.end_fill()
leo.hideturtle()

bob: Turtle = Turtle()


bob.pencolor(30, 30, 12)
bob.penup()
bob.goto(-220, -75)
bob.pendown()
bob.speed(75)

idx: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i += 1

idx: int = 0
while (i < 201):
    side_length = side_length * 0.98
    bob.forward(side_length)
    bob.left(121)
    i += 1

bob.hideturtle()
done()