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

    def refresh_the_playboard(self):

        """
        Should be called after each guess. It displays the relevant hangman picture, along
        with the updated word display
        """

        self.print_out_logo_art()
        self.print_word_display()

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

    def check_guess(self, guess):
        if guess in self.word:
            # TODO: Create something in that game files that will change the message that confirms that a letter
            #   letter has hit . Use the random.choice method, or something similar .

            for position in range(len(self.word)):
                letter = self.word[position]
                if letter == guess:
                    self.display[position] = guess

            self.refresh_the_playboard()
            print("")
            print("That's a hit!")

        else:
            self.refresh_the_playboard()
            print("")
            print("Nope, that letter is not in the word!")

    # TODO: Define a function that will combine the various functions involved in "refreshing"
    #    every time the user makes a guess.



    # TODO Make a function that will keep allowing the user to make these guesses until they
    #   there are no underscores present in the display array , thus winnind the game, or
    #   until they run out of lives, thus losing the game.


New_game = Game()

New_game.print_out_logo()
print(New_game.word)

New_game.print_out_logo_art()
New_game.print_word_display()
New_game.check_guess(New_game.make_guess())

