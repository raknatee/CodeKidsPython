def draw_ironman_helmet(turtle,points,color):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.color(color) 
    turtle.begin_fill()

    for i in range(1, len(points)):
        x, y = points[i]
        turtle.goto(x, y)

    turtle.end_fill()
