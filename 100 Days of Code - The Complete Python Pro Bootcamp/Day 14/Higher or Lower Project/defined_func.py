import os
import random
import game_data
from art import *


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
