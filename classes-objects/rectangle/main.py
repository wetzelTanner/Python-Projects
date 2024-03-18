###########################################
# Author: Tanner Wetzel
# Date Finished: 11/23/2021
# Description: A program that uses the Point and Rectangle modules to create a user-defined
#              rectangle, then displays that rectangle's area and perimeter, as well as if
#              it is origin-centered
###########################################

from point import Point
from rectangle import Rectangle

is_loop_over = False  # Flag for the loop
while not is_loop_over:
    # Read in x y for bottom left vertex as a string.
    # When typing for the input, ensure to use a space
    # to separate x and y, otherwise errors will occur.
    bl = input("\nEnter the bottom left vertex: ")

    # Read in x y for top right vertex as a string.
    # When typing for the input, ensure to use a space
    # to separate x and y, otherwise errors will occur.
    tr = input("Enter the top right vertex: ")

    # Split the bl string to get x and y respectively
    bl_x = int(bl.split(' ')[0])
    bl_y = int(bl.split(' ')[1])

    # Split the tr string to get x and y respectively
    tr_x = int(tr.split(' ')[0])
    tr_y = int(tr.split(' ')[1])

    ######################################
    # TODO
    # Create two points using data above:
    # vert_bl and vert_tr
    ######################################
    vert_bl = Point(bl_x, bl_y)
    vert_tr = Point(tr_x, tr_y)

    ######################################
    # TODO
    # Create a rectangle using two points:
    # rect
    ######################################
    rect = Rectangle((bl_x, bl_y),(tr_x, tr_y))

    ######################################
    # TODO
    # Print the necessary information for
    # the Rectangle object rect.
    # Refer to test cases for the format.
    ######################################
    print(rect)
    print('Area:', str(rect.area()))
    print('Perimeter:', str(rect.perimeter()))

    ######################################
    # TODO
    # Update the while loop condition to
    # end the loop properly
    ######################################
    if rect.is_origin_centered() == True:
        print('Bongo! Found an origin-centered Rectangle!')
        is_loop_over = True
    else:
        is_loop_over = False 