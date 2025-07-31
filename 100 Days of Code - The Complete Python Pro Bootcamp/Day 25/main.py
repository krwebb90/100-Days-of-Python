import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/50_states.csv")

all_states = data.state.to_list()
guessed_states = []

# answer_state = screen.textinput(title="Guess the State", prompt="What is a state's name?")
# print(answer_state)

# need to check the input against the csv, despite case, need to use lower(), then print to the xcoor and ycoor by creating a turtle and placing it on the map. Then add to counter

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is a state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())







# the break keyword negates the need for an exitonclick
# screen.exitonclick()


# code to get the coordinates for the states and their names

# def get_mouse_click_coor(x,y,):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()