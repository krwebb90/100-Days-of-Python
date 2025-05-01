import turtle

timmy = turtle.Turtle()

timmy.shape("turtle")
timmy.color("DarkSeaGreen2")


my_screen = turtle._Screen()
print(my_screen)
print(timmy)

turtle.forward(100)
turtle.right(90)
turtle.forward(100)


turtle.mainloop()