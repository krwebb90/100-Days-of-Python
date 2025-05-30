import turtle
import snake
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_guy = snake.Snake()

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



screen.exitonclick()
