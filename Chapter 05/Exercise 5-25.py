import turtle
import random

# Named constants
ANIMATION_SPEED = 0
SCREEN_WIDTH = 500                   # Screen width
SCREEN_HEIGHT = 500                  # Screen height
NUM_STARS = 20                       # Number of stars to draw
MIN_X = -(int(SCREEN_WIDTH / 2))     # Minimum x coordinate on the screen
MAX_X = int((SCREEN_WIDTH / 2) - 1)  # Maximum x coordinate on the screen
MIN_Y = -(int(SCREEN_HEIGHT / 2))    # Minimum y coordinate on the screen
MAX_Y = int(SCREEN_HEIGHT / 2)       # Maximum y coordinate on the screen

X1 = MIN_X          # Skyline starting x coordinate
Y1 = -50            # Skyline starting y coordinate

WINDOW_SIZE = 10    # Square window size
WX1 = -160          # Window 1 x coordinate
WY1 = 10            # Window 1 y coordinate
WX2 = -100          # Window 2 x coordinate
WY2 = 170           # Window 2 y coordinate
WX3 = -100          # Window 3 x coordinate
WY3 = 150           # Window 3 y coordinate
WX4 = -60           # Window 4 x coordinate
WY4 = 100           # Window 4 y coordinate
WX5 = -80           # Window 5 x coordinate
WY5 = -20           # Window 5 y coordinate
WX6 = 30            # Window 6 x coordinate
WY6 = 90            # Window 6 y coordinate

# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling

def screen_setup():
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    turtle.bgcolor('black')

def draw_stars():
    # Draw the stars
    turtle.pencolor('white')
    for count in range(NUM_STARS):
        x = random.randint(MIN_X, MAX_X)
        y = random.randint(MIN_Y, MAX_Y)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot()
    
def draw_buildings():
    # Draw the buildings
    turtle.pencolor('gray')
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(X1, Y1)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(70)
    # Go to the right edge of the screen.
    turtle.goto(MAX_X, turtle.ycor())
    # Close the shape.
    turtle.goto(MAX_X, MIN_Y)
    turtle.goto(MIN_X, MIN_Y)
    turtle.goto(X1, Y1)
    turtle.end_fill()
    
def draw_windows():
    square(WX1, WY1, WINDOW_SIZE, 'white')
    square(WX2, WY2, WINDOW_SIZE, 'white')
    square(WX3, WY3, WINDOW_SIZE, 'white')
    square(WX4, WY4, WINDOW_SIZE, 'white')
    square(WX5, WY5, WINDOW_SIZE, 'white')
    square(WX6, WY6, WINDOW_SIZE, 'white')
    
def main():
    screen_setup()
    draw_stars()
    draw_buildings()
    draw_windows()

main()
