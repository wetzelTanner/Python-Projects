# imports the turtle and random modules for later use
import random
import turtle

# creates an 800 x 800 window 
wn = turtle.Screen()
wn.setup(800,800)

# creates a red turtle to participate in the game
tur_red = turtle.Turtle()
tur_red.pensize(5)
tur_red.color('red')
tur_red.shape('turtle')

# creates a blue turtle to participate in the game
tur_blue = turtle.Turtle()
tur_blue.pensize(5)
tur_blue.color('blue')
tur_blue.shape('turtle')
tur_blue.up()
tur_blue.setpos(50,0)
tur_blue.down()

# defines a function that returns True if both turtles are still in the grid or False if one or both leave 
def is_in_grid(tur):
    location_x = tur.xcor()
    location_y = tur.ycor()
    if location_x >= 400 or location_x <= -400:
        is_in = False
    elif location_y >= 400 or location_y <= -400:
        is_in = False
    else:
        is_in = True
    return is_in

# defines a function that returns True as long as both turtles are not in the same location
def is_safe(tur1, tur2):
    if tur1.xcor() == tur2.xcor() and tur1.ycor() == tur2.ycor():
        safe = False
    else:
        safe = True
    return safe

# defines a function that checks if both turtles are still in the grid
# if they are not, the function will print the winner or print draw in the case of a draw
def check_winner(red_in_grid = True, blue_in_grid = True):
    red_in_grid = is_in_grid(tur_red)
    blue_in_grid = is_in_grid(tur_blue)
    if red_in_grid == False:
        tur_blue.write('blue wins!', True, 'center', ('arial',15))
    if blue_in_grid == False:
        tur_red.write('red wins!', True, 'center', ('arial',15))
    if is_safe(tur_red,tur_blue) == False:
        tur_red.write('draw', False, 'center', ('arial',15))
        tur_blue.write('draw', False, 'center', ('arial',15))
    
# a loop that states that while both turtles are in the grid and are not in the same location, two coins will be flipped
# in every iteraton, this loop will check the winner after both coins are flipped
while is_in_grid(tur_red) and is_in_grid(tur_blue) and is_safe(tur_red, tur_blue):
    coin1 = random.randrange(0,2)
    if coin1 == 0:
        tur_red.left(90)
        tur_red.forward(50)
    else:
        tur_red.right(90)   
        tur_red.forward(50)

    coin2 = random.randrange(0,2)
    if coin2 == 0:
        tur_blue.left(90)
        tur_blue.forward(50)
    else:
        tur_blue.right(90)
        tur_blue.forward(50)
    check_winner()

# allows the user to exit the window with a click of the mouse
wn.exitonclick()