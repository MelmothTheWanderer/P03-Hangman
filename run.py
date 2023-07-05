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


def make_guess():
    """
    This function will get the user to make a guess , and only return the value after it has
    been validated to make sure that isn't either an empty string, an integer, or a string that is longer that
    one letter. The returned value will be converted to lowercase.
    """
    guess = input("Please guess a letter: ")

    data_valid = False

    while data_valid is not True:

        if guess == "":
            print("Come on , you have to type something! Try again: ")
            guess = guess = input("Please guess a letter: ")

        elif guess.isdecimal():
            print("You can't type a number! Try again: ")
            guess = guess = input("Please guess a letter: ")

        elif len(guess) > 1:
            print("Guess one letter only please. Try again: ")
            guess = guess = input("Please guess a letter: ")

        else:
            return guess.lower()


class Game:
    def __init__(self):
        self.word = choose_word()
        self.lives = 7
        self.display = []
        self.create_word_display()
        self.logo = GAME_LOGO

    def create_word_display(self):
        """
        Updates the display array with underscores to represent unknown letters of the word.
        """
        display = []
        for _ in range(len(self.word)):
            self.display.append("_")

    def print_word_display(self):
        print(self.display)

    def print_out_logo(self):
        """Prints the hangman logo"""
        print(GAME_LOGO)


New_game = Game()
New_game.print_out_logo()
New_game.print_word_display()

