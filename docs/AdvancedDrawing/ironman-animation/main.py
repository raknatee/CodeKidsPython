from turtle import Screen, Turtle
from ironman_helmet import draw_ironman_helmet
from points import ankur1, ankur2, ankur3
from time import sleep


def main():

        screen = Screen()
        screen.setup(500,600)
        screen.title("I AM IRONMAN")
      
        my_turtle = Turtle()
        my_turtle.hideturtle()

        for i in range(10):
                screen.bgcolor("#ba161e")
                my_turtle.clear()
                color = "#fab104"
                draw_ironman_helmet(my_turtle, ankur1, color)
                draw_ironman_helmet(my_turtle, ankur2, color)
                draw_ironman_helmet(my_turtle, ankur3, color)
                
                sleep(1)

                screen.bgcolor("blue")
                my_turtle.clear()
                color = "pink"
                draw_ironman_helmet(my_turtle, ankur1, color)
                draw_ironman_helmet(my_turtle, ankur2, color)
                draw_ironman_helmet(my_turtle, ankur3, color)

                sleep(1)

main()