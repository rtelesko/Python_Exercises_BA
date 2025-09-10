import turtle

# Named constants
ANIMATION_SPEED = 0
BASE_X = 0
BASE_Y = 0

def rectangle(x, y, width, height, color):
    turtle.setheading(0)
    turtle.fillcolor(color)     # Set the fill color
    turtle.penup()              # Raise the pen
    turtle.goto(x, y)           # Move to the specified location
    turtle.pendown()            # Lower the pen
    
    # Draw the rectangle.
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()

def rectangular_pattern(width, height):
    # The pattern is made of 3 nested rectangles with
    # diagonal lines connecting the corners and the
    # four sides.
    # Draw the outer rectangle.
    rectangle(BASE_X, BASE_Y, width, height, 'white')

    # Draw the middle rectangle.
    middle_x = BASE_X + width / 8
    middle_y = BASE_Y + height / 8
    middle_width = width - width / 4
    middle_height = height - height / 4
    rectangle(middle_x, middle_y, middle_width, middle_height, 'white')

    # Draw the innermost rectangle.
    inner_x = BASE_X + width / 4
    inner_y = BASE_Y + height / 4
    inner_width = width - width / 2
    inner_height = height - height / 2
    rectangle(inner_x, inner_y, inner_width, inner_height, 'black')

    # Draw the diagonal connecting lines.
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y)
    turtle.pendown()
    turtle.goto(inner_x, inner_y)

    turtle.penup()
    turtle.goto(BASE_X + width, BASE_Y + height)
    turtle.pendown()
    turtle.goto(inner_x + inner_width, inner_y + inner_height)

    turtle.penup()
    turtle.goto(BASE_X + width, BASE_Y)
    turtle.pendown()
    turtle.goto(inner_x + inner_width, inner_y)

    turtle.penup()
    turtle.goto(BASE_X, BASE_Y + height)
    turtle.pendown()
    turtle.goto(inner_x, inner_y + inner_height)

    # Draw the horizontal connecting lines.
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y + height / 2)
    turtle.pendown()
    turtle.goto(inner_x, BASE_Y + height / 2)

    turtle.penup()
    turtle.goto(BASE_X + width, BASE_Y + height / 2)
    turtle.pendown()
    turtle.goto(inner_x + inner_width, BASE_Y + height / 2)

    # Draw the vertical connecting lines.
    turtle.penup()
    turtle.goto(BASE_X + width / 2, BASE_Y)
    turtle.pendown()
    turtle.goto(BASE_X + width / 2, inner_y)

    turtle.penup()
    turtle.goto(BASE_X + width / 2, BASE_Y + height)
    turtle.pendown()
    turtle.goto(BASE_X + width / 2, inner_y + inner_height)

def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    w = int(input('Enter the width: '))
    h = int(input('Enter the height: '))
    rectangular_pattern(w, h)

main()

    
