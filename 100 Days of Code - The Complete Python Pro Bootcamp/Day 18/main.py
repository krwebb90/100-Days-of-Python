#####Turtle Intro######

import turtle

timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("LightSeaGreen")


# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.setheading(0)
# timmy_the_turtle.backward(200)

screen = turtle.Screen()


######## Challenge 1 - Draw a Square ############



######## Challenge 2 - Draw a Dashed Line ############



count = 0
while count < 10:
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    count += 1