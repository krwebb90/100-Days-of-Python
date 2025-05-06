import turtle
import random
import colorgram
import os

# getting the extraced colors into the right format

# rgb_colors = []
# colors = colorgram.extract(r'C:\Users\webkerry\Documents\GitHub\100-Days-of-Python\100 Days of Code - The Complete Python Pro Bootcamp\Day 18\image.jpeg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Debug prints
# print("Current working directory:", os.getcwd())
# print("Files in current directory:", os.listdir())

# # Try using absolute path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# image_path = os.path.join(current_dir, 'image.jpeg')
# print("Full image path:", image_path)
# print("Does file exist?:", os.path.exists(image_path))

# removed colors too close to background white
# [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]




color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

# 10 x 10 dot painting with turtle
# sized 20, spread by 50 paces

tim = turtle.Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.color("LightSeaGreen")
tim.speed(0)
screen = turtle.Screen()
tim.penup()
tim.hideturtle()
tim.goto(-250, -250)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()
screen.exitonclick()