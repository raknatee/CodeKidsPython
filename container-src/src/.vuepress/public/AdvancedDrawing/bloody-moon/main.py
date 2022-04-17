from turtle import Screen,Turtle

from moon import move_moon, draw_moon


def main():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.tracer(0)
    moon = Turtle()
    moon.hideturtle()
    crescent = Turtle()
    crescent.hideturtle()

    while True:
        moon.clear()
        draw_moon(moon, "red", 100, 20)
        draw_moon(crescent, "white", 100, 20)
        move_moon(moon, 0.8)
        screen.update()


main()
