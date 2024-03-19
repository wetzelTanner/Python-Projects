# import turtle and create a window
import turtle
wn = turtle.Screen()

# create a turtle object
jj = turtle.Turtle()
jj.shape('turtle')

# define the draw pedal function
def draw_petal(tur, speed, n_sided, radius):
    tur.speed(speed)
    tur.circle(radius,360,n_sided)

# define the draw sunflower function
def draw_sunflower(tur, speed, n_sided, radius, num_pedal):
    speed = int(input("Enter animation speed: "))
    n_sided = int(input("Enter the number of sides of a pedal: "))
    radius = int(input("Enter the radius of pedals: "))
    num_pedal = int(input("Enter the number of pedals: "))
    for i in range(num_pedal):
        if i % 2 == 0:
            jj.color('orange')
        if i % 2 == 1:
            jj.color('yellow')
        draw_petal(tur, speed, n_sided, radius)
        tur.left(360 / num_pedal)
        
# create a flag for the while loop
is_done = False 

# create a while loop that draws a sunflower using the draw sunflower function
while not is_done:
    draw_sunflower(jj, speed=10, n_sided=10, radius=100, num_pedal=10)
    answer = input("Draw another sunflower (yes or no)? ")
    if answer == "yes":
        jj.clear()
    if answer == "no":
        is_done = True
    if answer != "yes" and answer != "no":
        print("Invalid command, exiting... ")
        is_done = True