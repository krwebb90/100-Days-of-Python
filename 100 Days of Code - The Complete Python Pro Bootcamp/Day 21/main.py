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
        score.increase_score()


screen.exitonclick()
