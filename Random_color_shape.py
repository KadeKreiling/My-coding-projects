import turtle
import random

t = turtle.Turtle()

def color():
    COLOR_LIST = ["blue", "red", "orange", "green", "purple", "yellow"]
    return random.choice(COLOR_LIST)

def move(x, y):
    t.penup()
    t.goto(random.randint(x, y), random.randint(x, y))
    t.pendown()

def draw_square(t,color, border_color):
    move(-200, 200)
    size = random.randint(10, 100)
    t.pencolor(border_color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.rt(90)
    t.end_fill()

def draw_triangle(t, color, border_color):
    num = 0
    size = random.randint(10, 100)
    move(-200, 200)
    t.pencolor(border_color)
    t.fillcolor(color)
    t.begin_fill()
    while num < 3:
        t.forward(size)
        t.lt(120)
        num += 1
    t.end_fill()

def draw_octagon(t, color, border_color):
    size = random.randint(10, 100)
    move(-200, 200)
    t.pencolor(border_color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(8):
        t.forward(size)
        t.lt(45)
    t.end_fill()

def create_shapes(times):
    for i in range(times):
        shape = random.randint(1, 3)
        if shape == 1:
            draw_square(color(), color())
        elif shape == 2:
            draw_triangle(color(), color())
        else:
            draw_octagon(color(), color())

create_shapes(20)

turtle.mainloop()      # should be last line of program


