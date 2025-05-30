import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

# manual way of creating segments
# segment1 = turtle.Turtle(shape="square")
# segment1.color("white")

# segment2 = turtle.Turtle(shape="square")
# segment2.color("white")
# segment2.goto(x=-20,y=0)

# segment3 = turtle.Turtle(shape="square")
# segment3.color("white")
# segment3.goto(x=-40,y=0)


# for loop to create segments

for position in starting_positions:
    new_segment = turtle.Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.3)

    for segnum in range(len(segments)-1, 0, -1):
        new_x = segments[segnum-1].xcor()
        new_y = segments[segnum-1].ycor()
        segments[segnum].goto(new_x, new_y)
    segments[0].forward(20)




screen.exitonclick()
