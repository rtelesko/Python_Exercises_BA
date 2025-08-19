import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle.
turtle.penup()
turtle.hideturtle()
turtle.speed(ANIMATION_SPEED)

# Move the turtle to the starting point.
starting_x = (0 - (diameter / 2)) + ((WINDOW_WIDTH - diameter) / 2)
starting_y = (s / 2) + x
turtle.goto(starting_x, starting_y)
turtle.pendown()

# Draw the octagon.
for x in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

# Display 'STOP'
turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.pendown()
turtle.write('STOP')
