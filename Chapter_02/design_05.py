import turtle

# Named constants
CENTER_X = 0
CENTER_Y = 0
X_AXIS_LENGTH = 200
Y_AXIS_LENGTH = 200
RADIUS = 25
SOUTH = 270
EAST = 0

# Hide the turtle and set the animation speed.
turtle.hideturtle()
turtle.speed(0)

# Draw the X axis
x = CENTER_X - (X_AXIS_LENGTH / 2)
y = CENTER_Y
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.forward(X_AXIS_LENGTH)

# Draw the Y axis
x = CENTER_X
y = CENTER_Y + (Y_AXIS_LENGTH / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.setheading(SOUTH)
turtle.forward(X_AXIS_LENGTH)

# Draw the center circle
x = CENTER_X
y = CENTER_Y - RADIUS
turtle.penup()
turtle.setheading(EAST)
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Write "North"
x = CENTER_X - 10
y = CENTER_Y + (Y_AXIS_LENGTH / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("North")

# Write "South"
x = CENTER_X - 10
y = CENTER_Y - (Y_AXIS_LENGTH / 2) - 10
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("South")

# Write "West"
x = CENTER_X - (X_AXIS_LENGTH / 2) - 25
y = CENTER_Y - 7
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("West")

# Write "West"
x = CENTER_X + (X_AXIS_LENGTH / 2) + 2
y = CENTER_Y - 7
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("East")

