import turtle

# Hide the turtle.
turtle.hideturtle()

# Set the fill color to blue.
turtle.fillcolor('blue')

# Draw the first diamond.
turtle.begin_fill()
turtle.left(135)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

# Draw the second diamond.
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
