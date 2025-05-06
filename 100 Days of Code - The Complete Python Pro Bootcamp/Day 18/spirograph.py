import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("LightSeaGreen")
tim.pensize(1)
tim.speed(0)
tim.heading()
screen = turtle.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()