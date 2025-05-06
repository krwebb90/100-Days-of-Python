import turtle

timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("LightSeaGreen")
screen = turtle.Screen()

def draw_square():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


def draw_eight_squares():
    count = 0
    while count < 8:
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.right(45)
        count += 1




draw_eight_squares()