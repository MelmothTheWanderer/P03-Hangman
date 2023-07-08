# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os
from game_files import LIST_OF_WORDS, ASCII_ART, GAME_LOGO




def choose_word():
    """This function will return a random word from the list of random words
    in the words.py file
    """
    random_word = random.choice(LIST_OF_WORDS)
    return random_word


class Game:
    def __init__(self):

        self.word_string = choose_word()
        self.word_list = list(self.word_string)
        self.lives = 7
        self.display = []
        self.create_word_display()
        self.logo = GAME_LOGO
        self.guessed_letters = []

    def clear_console(self):
        """
        Used to clear the terminal of all text
        """
        os.system("cls" if os.name == "nt" else "clear")

    def create_word_display(self):
        """
        Updates the display array with underscores to represent unknown letters of the word.
        """
        display = []
        for _ in range(len(self.word_list)):
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
        self.clear_console()
        self.print_out_logo()
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

        # TODO check to see if the letter is in the list of guessed letters , and if it is
        #   then display a message telling the players that they have already guessed that
        #   letter , and that they should guess again.

        if guess in self.guessed_letters:
            self.refresh_the_playboard()
            print(f"YOU GUESSED THE LETTER '{guess.upper()}' ALREADY! ")

        elif guess in self.word_list:
            # TODO: Create something in that game files that will change the message that confirms that a letter
            #   letter has hit . Use the random.choice method, or something similar .

            for position in range(len(self.word_list)):
                letter = self.word_list[position]
                if letter == guess:
                    self.display[position] = guess.upper()

            self.refresh_the_playboard()
            print("")
            print("That's a hit!\nKeep it up!")

        else:
            self.lives -= 1
            self.refresh_the_playboard()
            print("")
            print("Nope, that letter is not in the word\nGuess again!")

        if guess not in self.guessed_letters:
            self.guessed_letters.append(guess.lower())

    # TODO Define a function that will ask the user whether or not they wish to continue
    #   with the game. If they do wish to continue, then reset the word , and all of the
    #   game information.

    def reset_the_game(self):
        self.word_string = choose_word()
        self.word_list = list(self.word_string)
        self.lives = 7
        self.display = []
        self.create_word_display()
        self.guessed_letters = []
        # This runs the game
        self.print_out_logo()
        self.refresh_the_playboard()
        self.play_game()

    def ask_to_continue(self):

        while True:
            decision = input("Do you want to continue?\nPlease type y/n: ")
            if decision == "y":
                self.reset_the_game()
            elif decision == "n":
                break
            else:
                print("NOT A VALID RESPONSE")

    # TODO Make a function that will keep allowing the user to make these guesses until they
    #   there are no underscores present in the display array , thus winnind the game, or
    #   until they run out of lives, thus losing the game.

    # As long as there are still letters to guess, and the player has at least 1 life:
    def play_game(self):

        """
        Loops the game until the player either guesses all the letters, or runs out of lives.
        A corresponding message is then displayed.
        """
        while "_" in self.display and self.lives > 1:
            # 1. Display the game data
            # self.refresh_the_playboard()
            # 2. Ask user to make a guess
            self.check_guess(self.make_guess())

        # This sesction of the function will check to see if the player has won the game or not.
        if "_" not in self.display:
            print(f"That's right , the word was {self.word_string.upper()}.")
            print("YOU HAVE WON THE GAME!")
            self.ask_to_continue()
        else:
            print(f"No, no , no , the word was {self.word_string.upper()}!")
            print("YOU LOSE!")
            self.ask_to_continue()

        # TODO create and insert a function called check_if_won. Use it to check whether
        #   the player has won or lost and display the relevant message.
    # 3 Update the data (this is done in the check_guess function


new_game = Game()
new_game.refresh_the_playboard()
new_game.play_game()
