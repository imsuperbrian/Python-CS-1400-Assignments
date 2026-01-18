import turtle
from turtle import *
my_turtle = turtle.Turtle()


# CS 1400 Assignment 2. Written by CS 1400 Course Staff and Brian Yang

# Draw a square with a Python turtle.
# Do not modify this.

def draw_square(square_turtle, x, y, side_length):
    # Position the turtle
    square_turtle.penup()
    square_turtle.setposition(x, y)
    square_turtle.pendown()
    # Make the square
    for side in range(4):
        square_turtle.forward(side_length)
        square_turtle.left(90)


#########################################################
# Define your functions below this line
# and above the following row of #s.
# All code in this area should be part of a function.


#To draw 5 squares
def draw_wall(wall_turtle, x, y, height):
    for i in range(5):


        draw_square(wall_turtle, x, y, height)

        x = x + height + 15


#draw smiling face
def turtle_face(turtle1):



    turtle.home()


    turtle.circle(180)  # draw a semicircle

    #left eye
    turtle1.penup()
    turtle1.goto(-60, 230)  # left eye
    turtle1.pendown()
    turtle1.circle(15)

    #right eye
    turtle1.penup()
    turtle1.goto(60, 230)  # right eye
    turtle1.pendown()
    turtle1.circle(15)

    #mouth
    turtle1.penup()
    turtle1.goto(-80, 100)
    turtle1.pendown()
    turtle1.setheading(-60)
    turtle1.circle(100, 120)


#draw word

# draw B
def draw_B(b):
    b.penup()
    b.goto(-80, -200)
    b.pendown()


    b.setheading(270)
    b.forward(100)
    b.penup()
    b.goto(-80, -200)

    b.setheading(360)
    b.goto(-80, -250)
    b.pendown()
    b.circle(25, 180)
    b.setheading(360)
    b.goto(-80, -300)
    b.circle(25, 180)


# draw O
def draw_O(o):
    o.penup()
    o.goto(0, -300)
    o.pendown()
    o.setheading(0)

    o.circle(50)

    o.setheading(0)


# draw Y
def draw_Y(y):
    y.penup()
    y.goto(50, -200)
    y.setheading(-60)
    y.pendown()

    y.forward(60)  # 左斜

    y.setheading(60)
    y.forward(60)  # 右斜
    #y.backward(60)

    y.penup()
    y.goto(80, -250)
    y.pendown()
    y.setheading(-90)  # 中間往下
    y.forward(60)

    y.setheading(0)


#########################################################

# The following code sets up a window and Turtle.
# Call your functions where specified by the comments to
# draw the various required shapes.
# You can uncomment the turtle speed command for a faster turtle.

# Set up the window and turtle
window = Screen()
drawing_turtle = Turtle()

draw_wall(drawing_turtle, -300, -150, 100)
turtle_face(drawing_turtle)
draw_B(drawing_turtle)
draw_O(drawing_turtle)
draw_Y(drawing_turtle)

# Uncomment this next line for a faster turtle!
# drawing_turtle.speed(0)

# Add code to call the draw_wall function

# Add code to call the draw_face function twice in
# two different locations.

# Call your draw_word function.

# You can uncomment this next line to hide the arrow shape
# when you have all your parts working. While writing your
# functions it can be helpful to see where the turtle ends
# up as you add more parts to your drawing.
# drawing_turtle.hideturtle() # Get rid of the arrow showing the turtle location.

window.exitonclick()