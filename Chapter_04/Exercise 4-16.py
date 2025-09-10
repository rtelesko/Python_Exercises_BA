import turtle

# Named constants
INITIAL_ANGLE = 45
ANGLE_STEP = 135
NUM_LINES = 8
LENGTH = 200
ANIMATION_SPEED = 0

# Initialize the turtle.
turtle.hideturtle()
turtle.speed(ANIMATION_SPEED)
turtle.left(INITIAL_ANGLE)

# Draw the lines.
for count in range(NUM_LINES):
    turtle.forward(LENGTH)
    turtle.left(ANGLE_STEP)
    
