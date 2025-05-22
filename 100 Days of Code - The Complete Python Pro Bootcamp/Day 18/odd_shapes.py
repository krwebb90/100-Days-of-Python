import turtle
import random


tim = turtle.Turtle()
tim.shape("turtle")
tim.color("LightSeaGreen")
screen = turtle.Screen()


color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# lines
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# dashes
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         count = 0
#         while count < 10:
#             tim.forward(10)
#             tim.penup()
#             tim.forward(10)
#             tim.pendown()
#             count += 1
#         tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(color))
    draw_shape(shape_side_n)