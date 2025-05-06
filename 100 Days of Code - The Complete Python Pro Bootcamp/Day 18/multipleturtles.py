import turtle
import threading

tim = turtle.Turtle()
tom = turtle.Turtle()
tony = turtle.Turtle()


tim.shape("turtle")
tim.color("LightSeaGreen")

tom.shape("turtle")
tom.color("green4")

tony.shape("turtle")
tony.color("LightSalmon")
screen = turtle.Screen()


def tim_draw_eight_squares():
    count = 0
    while count < 8:
        tim.forward(100)
        tim.right(90)
        tim.forward(100)
        tim.right(90)
        tim.forward(100)
        tim.right(90)
        tim.forward(100)
        tim.right(90)
        tim.right(45)
        count += 1

def tom_draw_eight_squares():
    count = 0
    while count < 8:
        tom.forward(150)
        tom.right(90)
        tom.forward(150)
        tom.right(90)
        tom.forward(150)
        tom.right(90)
        tom.forward(150)
        tom.right(90)
        tom.right(45)
        count += 1


def tony_draw_eight_squares():
    count = 0
    while count < 8:
        tony.forward(75)
        tony.right(90)
        tony.forward(75)
        tony.right(90)
        tony.forward(75)
        tony.right(90)
        tony.forward(75)
        tony.right(90)
        tony.right(45)
        count += 1


tim.penup()
tim.goto(-100, 0)
tim.pendown()

tom.penup()
tom.goto(0, 150)
tom.pendown()

tony.penup()
tony.goto(75, 0)
tony.pendown()

tim_thread = threading.Thread(target=tim_draw_eight_squares)
tom_thread = threading.Thread(target=tom_draw_eight_squares)
tony_thread = threading.Thread(target=tony_draw_eight_squares)

tim_thread.start()
tom_thread.start()
tony_thread.start()

screen.mainloop()