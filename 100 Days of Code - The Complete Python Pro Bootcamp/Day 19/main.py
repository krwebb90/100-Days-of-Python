import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bets", prompt="Which turtle will win the race? Enter one of the following: Red, Orange, Yellow, Green, Blue, or Purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU WIN! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lose. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()