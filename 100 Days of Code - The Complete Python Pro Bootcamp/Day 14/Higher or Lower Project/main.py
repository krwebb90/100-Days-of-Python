# imports
from art import *
import random
import game_data
import os
import defined_func

# art
print(logo)

# global score variable?
user_score = 0

# flag for loop
game_should_continue = True

# define game in loop
while game_should_continue:

    # random choice a, remove a from the list, random choice b
    # this has to be in the loop so when the game restarts, we don't lose the original values
    # determine best place to start and stop loop, this is the right direction, need to package in loops and defined functions
    entireaccountA = random.choice(game_data.data)
    accountA = entireaccountA['name']
    remaininglist = game_data.data.copy()
    remaininglist.remove(entireaccountA)
    entireaccountB = random.choice(remaininglist)
    accountB = entireaccountB['name']

    userchoice = input(f'Who has more instagram followers? \n\n "A": {defined_func.format_data(entireaccountA)} \n {vs} \n "B": {defined_func.format_data(entireaccountB)}? \n\n Type A or B: ').lower()

    defined_func.clear()
    print(logo)

    # check if the user's guess is correct
    # if statement for the follower count of entirechoiceA vs entirechoiceB
    is_correct = defined_func.check_answer(userchoice, entireaccountA['follower_count'], entireaccountB['follower_count'])

    # conditions (win or lose)
    # increment score (the actual solution wants to move the choiceB to choiceA if it is higher so we are always comparing to choiceA but I don't like that) or game over
    if is_correct:
        user_score += 1
        print(f"You are correct! Your current score is {user_score}")
    else:
        print(f"Sorry, that is incorrect. Game Over!\n\n Your final score is {user_score}")
        game_should_continue = False