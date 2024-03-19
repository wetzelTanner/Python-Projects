# ------------------------------------
# TURTLE MODULE LAB 2
# Author: Tanner Wetzel
# Date: 09/29/2021
# Description: Uses the turtle module to create art on a canvas using clicks and key inputs from the user
# ------------------------------------

# imports the turtle module and sets up a window
import turtle
wn = turtle.Screen()
wn.setup(400,400)

# creates a turtle that will indicate the color of jj
color_indicator = turtle.Turtle()
color_indicator.color("red")
color_indicator.hideturtle()
color_indicator.up()
color_indicator.goto(0,160)
color_indicator.down
color_indicator.write("Color is red",False,"center",["courier",12])

# creates a turtle that will indicate whether the pen is up or down
pen_indicator = turtle.Turtle()
pen_indicator.hideturtle()
pen_indicator.up()
pen_indicator.goto(-100,160)
pen_indicator.down
pen_indicator.write("Pen is down",False,"center",["courier",12])

# creates jj, a turtle that will draw art on a canvas
jj = turtle.Turtle()
jj.shape("turtle")
jj.color("red")

# defines what should happen when hotkeys for color are pressed
def red_color():
    color_indicator.clear()
    color_indicator.color("red")
    jj.color("red")
    color_indicator.write("Using red",False,"center",["courier",12])

def blue_color():
    color_indicator.clear()
    color_indicator.color("blue")
    jj.color("blue")
    color_indicator.write("Using blue",False,"center",["courier",12])

def green_color():
    color_indicator.clear()
    color_indicator.color("green")
    jj.color("green")
    color_indicator.write("Using green",False,"center",["courier",12])

# defines what should happen when hotkeys for penup or pendown are pressed
def pen_up():
    pen_indicator.clear()
    jj.penup()
    pen_indicator.write("Pen is up",False,"center",["courier",12])

def pen_down():
    pen_indicator.clear()
    jj.pendown()
    pen_indicator.write("Pen is down",False,"center",["courier",12])

# defines what should happen when the window is left or right clicked
def left_click(x,y):
    jj.goto(x,y)
    wn.title("Current position: " + str(x) + "," + str(y))

def right_click(x,y):
    jj.undo()

# tells the window what functions to utilize on key presses
wn.onkeypress(red_color, "r")
wn.onkeypress(blue_color, "b")
wn.onkeypress(green_color, "g")
wn.onkeypress(pen_down, "d")
wn.onkeypress(pen_up, "u")

# tells the window what functions to utilize on a left or right click
wn.onscreenclick(left_click, 1)
wn.onscreenclick(right_click, 2)

#asks the window to listen for key press or window click events
wn.listen()

# keeps the window open until the program is manually exited
wn.mainloop()