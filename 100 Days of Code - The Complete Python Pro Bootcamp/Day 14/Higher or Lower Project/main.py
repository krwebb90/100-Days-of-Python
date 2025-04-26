# imports
from art import *
import random
import game_data

# art
print(logo)

# define game

# global score variable?

# define a vs b, then increment the score or game over, maybe a while true loop

# random choice a, remove a from the list, random choice b
# this has to be in the loop so when the game restarts, we don't lose the original values

entirechoiceA = random.choice(game_data.data)
choiceA = entirechoiceA['name']
remaininglist = game_data.data.copy()
remaininglist.remove(entirechoiceA)
entirechoiceB = random.choice(remaininglist)
choiceB = entirechoiceB['name']

userchoice = input(f'Who has more instagram followers? {choiceA} or {choiceB}? ')




# conditions (win or lose)


# add points or game over


# code below
