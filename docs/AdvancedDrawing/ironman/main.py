from turtle import Screen, Turtle
from ironman_helmet import draw_ironman_helmet
from points import ankur1, ankur2, ankur3

def main():

        screen = Screen()
        screen.setup(500,600)
        screen.title("I AM IRONMAN")
        screen.bgcolor("#ba161e")

        my_turtle = Turtle()
        my_turtle.hideturtle()

        draw_ironman_helmet(my_turtle, ankur1)
        draw_ironman_helmet(my_turtle, ankur2)
        draw_ironman_helmet(my_turtle, ankur3)

        screen.mainloop()


main()
