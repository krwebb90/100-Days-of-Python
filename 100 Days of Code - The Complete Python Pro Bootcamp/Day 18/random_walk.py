import turtle
import random


tim = turtle.Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.color("LightSeaGreen")
tim.pensize(8)
tim.speed(8)
screen = turtle.Screen()


directions = [0, 90, 180, 270]
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for _ in range(200):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(50)
#     tim.setheading(random.randint(0, 360))