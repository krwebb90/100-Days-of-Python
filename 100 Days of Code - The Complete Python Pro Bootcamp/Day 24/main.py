import turtle
import snake
import time
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_guy = snake.Snake()
food_bit = food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake_guy.up, "Up")
screen.onkey(snake_guy.down, "Down")
screen.onkey(snake_guy.left, "Left")
screen.onkey(snake_guy.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake_guy.move()
    #detect food collision
    if snake_guy.head.distance(food_bit) < 15:
        food_bit.refresh()
        snake_guy.extend()
        score.increase_score()
    #detect wall collision
    if snake_guy.head.xcor() > 280 or snake_guy.head.xcor() < -280 or snake_guy.head.ycor() > 280 or snake_guy.head.ycor() < -280:
        score.reset()
        snake_guy.reset()
    #detect tail collision
    for segment in snake_guy.segments[1:]:
        if snake_guy.head.distance(segment) < 10:
            score.reset()
            snake_guy.reset()

screen.exitonclick()
