def draw_moon(turtle, color, width, circle_size):
    turtle.color(color)
    turtle.width(width)
    turtle.begin_fill()
    turtle.circle(circle_size)
    turtle.end_fill()


def move_moon(turtle, speed):
    turtle.right(speed)
    turtle.forward(speed - 0.1)
