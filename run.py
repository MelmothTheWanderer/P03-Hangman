# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from game_files import LIST_OF_WORDS, ASCII_ART, GAME_LOGO


def choose_word():
    """This function will return a random word from the list of random words
    in the words.py file
    """
    random_word = random.choice(LIST_OF_WORDS)
    return random_word




class Game:
    def __init__(self):
        self.word = list(choose_word())
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
        print("")
        print(self.display)

    def print_out_logo(self):
        """Prints the HANGMAN logo to the terminal"""
        print(GAME_LOGO)

    def print_out_logo_art(self):
        """
        Prints out the appropriate hangman art based on the lives that the player has used up.
        """
        print(ASCII_ART[(self.lives - 7) * -1])

    def make_guess(self):
        """
        This function will get the user to make a guess , and only return the value after it has
        been validated to make sure that isn't either an empty string, an integer, or a string that is longer than
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

# TODO : Define a function that will look for the guessed letter in the word array, and if it is in there
#   then replace the blanks in the display with the letters in their respective spots.
New_game = Game()

New_game.print_out_logo()
print(New_game.word)

New_game.print_out_logo_art()
New_game.print_word_display()

New_game.make_guess()

