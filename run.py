# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from game_files import LIST_OF_WORDS, ASCII_ART, GAME_LOGO


def choose_word():
    """This fucntion will return a random word fromn the list of random words
    in the words.py file
    """
    random_word = random.choice(LIST_OF_WORDS)
    return random_word


def display_word(word):
    """Creates an array of underscores to represent unknwon letters of the word
    """
    display = []
    for _ in range(len(word)):
        display.append("_")
    return display


def print_out_logo():
    """Prints the hangman logo"""
    print(GAME_LOGO)


def print_out_logo_art(lives_used_up):
    """
    prints out the appropriate hangman art based on the lives that the player has used up.
    """
    print(ASCII_ART[lives_used_up])

def print_out_letter_display(display):
    """
    Print the required information for the start of the game. Takes 1 argument , which is the array of underscores from the display_word fucntion

    1. Greeting
    2. The appropraite ascii art 
    3. How many letters the person has to guess 
    4. The array of empty letters 

    """
    # Display the Welcome message
    print()
    print(display)

def ask_user_to_make_a_guess():
    """
    Asks the user to guess a letter and then returns that letter
    """
    guess = input("Guess a letter: ")
    return guess

def validate_input(user_guess):

    """
    Takes the output from the ask_user_to_make_a_guess function , and validates it to make sure that
    the data is valid.
    """

    #was it an integar


print_out_logo()
print_out_logo_art(0)
print_out_letter_display(display_word(choose_word()))
validate_input(ask_user_to_make_a_guess())


