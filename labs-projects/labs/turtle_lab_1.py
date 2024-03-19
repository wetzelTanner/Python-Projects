# ------------------------------------
# TURTLE MODULE LAB 1
# Author: Tanner Wetzel
# Preferred name: Tanner
# Date: 09/17/2021
# Description: Uses the turtle module to create a user defined shape
# ------------------------------------

import turtle
wn = turtle.Screen()

jj = turtle.Turtle()
jj.shape('turtle')

# Create variables for user inputs
user_length = int(input('Enter the length of the first line: '))
user_angle = int(input('Enter the turning angle: '))
user_lines = int(input('Enter the number of lines: '))
user_speed = int(input('Enter the animation speed: '))

# Set speed to user's input speed
jj.speed(user_speed)

# Create a for loop that will loop as many times as the user inputs
for i in range(user_lines):
    # Decides what color to turn the turtle
    if i % 3 == 0:
        jj.color('red')
    if i % 3 == 1:
        jj.color('green')
    if i % 3 == 2:
        jj.color('blue')
    # Moves jj forward in increasing distances
    jj.fd(user_length * (i + 1))
    # Moves jj left the user's input angle
    jj.left(user_angle)

wn.exitonclick()