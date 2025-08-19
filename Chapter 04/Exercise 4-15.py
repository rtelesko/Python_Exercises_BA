import turtle

# Named constants
STARTING_X = -4
STARTING_Y = 4
STARTING_SIZE = 8
NUM_SQUARES = 50
STEP = 4
NUM_SIDES = 4
ANGLE = 90
ANIMATION_SPEED = 0

# Set the animation speed and hide the turtle.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Set the inital x & y coordinates & starting size.
x = STARTING_X
y = STARTING_Y
size = STARTING_SIZE

# Draw the pattern.
for count in range(NUM_SQUARES):
    # Position the turtle.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Draw the square
    for s in range(NUM_SIDES):
        turtle.forward(size)
        turtle.right(ANGLE)

    # Prepare for the next square.
    x = x - STEP
    y = y + STEP
    size = size + STEP
