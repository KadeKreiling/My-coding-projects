import turtle
import random
import sys

# functions to draw shapes
def draw_rectangle(width, height, t, color):
     t.fillcolor(color)
     t.begin_fill()
     for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)
     t.end_fill()

def draw_triangle(size, t, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.lt(120)
    t.end_fill()

def draw_octagon(size, color, t):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(8):
        t.forward(size)
        t.lt(45)
    t.end_fill()

def move(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_house(t, size):
    house_width = 100 * size
    house_height = 100 * size
    triangle_base = 100 * size
    door_width = 15 * size
    door_height = 50 * size
    step = 35 * size
    window1_x = 10 * size
    window2_x = 70 * size
    window_y = 50 * size

    draw_rectangle(house_width, house_height, t, "tan") #Draw main building of the house
    move(0, house_height, t) #Moves to draw the roof
    draw_triangle(triangle_base, t, "red") #Draws roof
    move(step, 0, t) # Move to the door
    draw_rectangle(door_width, door_height, t, "red") # Draw door
    move(window1_x, window_y, t) # Move to first window
    draw_rectangle(house_width * .2, house_height * .2, t, "blue") #Draw first house
    move(window2_x, window_y, t) #Move to second window
    draw_rectangle(house_width * .2, house_height * .2, t, "blue") #Draw second house

def draw_tree(t, size):
    trunk_width = 15 * size
    trunk_height = 50 * size
    tree_size = 15 * size
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    # Making sure the trees don't draw on the house
    if not 100 * size > x > 0 and not 200 * size > y > 0:
        move(x, y, t)
        draw_rectangle(trunk_width, trunk_height, t, "brown")
        t.penup()
        t.lt(90)
        t.forward(trunk_height)
        t.rt(90)
        draw_octagon(tree_size, "green", t)





def main():
    choice = sys.argv[1] #Enter normal, big, or small
    window = turtle.Screen()
    window.tracer(0, 0)
    t = turtle.Turtle()
    t.speed(0)
    window.bgcolor("light green")

    if choice == "normal":
        draw_house(t, 1)
        for i in range(35):
            draw_tree(t, 1)
    elif choice == "close_up":
        draw_house(t, 2)
        for i in range(20):
            draw_tree(t, 2)
    elif choice == "far_away":
        draw_house(t, .5)
        for i in range(50):
            draw_tree(t, .5)






if __name__ == '__main__':
    main()
    turtle.done()





