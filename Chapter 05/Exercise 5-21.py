import turtle

def triangle(x1, y1, x2, y2, x3, y3, color):
    # Set the fill color.
    turtle.fillcolor(color)
    
    #raise the pen and move the turtle.
    turtle.penup()
    turtle.goto(x1, y1)

    # Draw the triangle.
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()

def main():
    # Initialize the turtle.
    turtle.hideturtle()
    turtle.speed(0)
    
    # Draw three triangles.
    triangle(0, 0, 100, 0, 0, -100, 'red')
    triangle(0, 0, -100, 0, 0, -100, 'green')
    triangle(0, -100, -100, -200, 100, -200, 'blue')

main()
