import turtle

# Named constants
OUTER_TOP_X = 0
OUTER_TOP_Y = 200
INNER_TOP_X = OUTER_TOP_X
INNER_TOP_Y = OUTER_TOP_Y / 2
BASE_LEFT_X = -100
BASE_LEFT_Y = 0
BASE_RIGHT_X = 100
BASE_RIGHT_Y = 0

# Hide the turtle and raise the pen.
turtle.hideturtle()
turtle.penup()

# Move the pen to the bottom right corner.
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

# Set the fill color to blue and lower the pen.
turtle.fillcolor('blue')
turtle.pendown()

# Draw the outer triangle.
turtle.goto(OUTER_TOP_X, OUTER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

# Draw the inner triangle.
turtle.begin_fill()
turtle.goto(INNER_TOP_X, INNER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)
turtle.end_fill()
