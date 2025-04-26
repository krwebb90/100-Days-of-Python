# imports
from art import *
import random
import game_data
import os


# art
print(logo)

# check for vowel to clean up verbiage
def vowel_check(word):
    return 'an' if word[0].lower() in 'aeiou' else 'a'

# takes the account data and returns the printable format
def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, {vowel_check(account_desc)} {account_desc}, from {account_country}"

# takes the user's guess and checks if they chose the higher number of the two random accounts. both return statements act as boolean checks 
def check_answer(user_guess, accountA_followers, accountB_followers):
    if accountA_followers > accountB_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')

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

    userchoice = input(f'Who has more instagram followers? \n\n "A": {format_data(entireaccountA)} \n {vs} \n "B": {format_data(entireaccountB)}? \n\n Type A or B: ').lower()

    clear()
    print(logo)

    # check if the user's guess is correct
    # if statement for the follower count of entirechoiceA vs entirechoiceB
    is_correct = check_answer(userchoice, entireaccountA['follower_count'], entireaccountB['follower_count'])

    # conditions (win or lose)
    # increment score (the actual solution wants to move the choiceB to choiceA if it is higher so we are always comparing to choiceA but I don't like that) or game over
    if is_correct:
        user_score += 1
        print(f"You are correct! Your current score is {user_score}")
    else:
        print(f"Sorry, that is incorrect. Game Over!\n\n Your final score is {user_score}")
        game_should_continue = False