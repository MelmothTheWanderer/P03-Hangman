
import random
import os
from game_files import LIST_OF_WORDS, ASCII_ART, GAME_LOGO, HIT, MISS
import time


def choose_word():
    """This function will return a random word from the list of random words
    in the words.py file
    """
    random_word = random.choice(LIST_OF_WORDS)
    return random_word


class Game:

    """
    This is the game object. It contains all the logic required for
    the game to run.
    """
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
        Updates the self.display array with underscores to represent unknown
        letters of the word.
        """
        display = []
        for _ in range(len(self.word_list)):
            self.display.append("_")

    def print_word_display(self):
        print("")
        print(self.display)

    def print_out_logo(self):

        """
        Prints the HANGMAN logo to the terminal using ASCII art.
        """
        print(GAME_LOGO)

    def print_out_logo_art(self):
        """
        Prints out the appropriate hangman art based on the lives that the
        player has used up.
        """
        print(ASCII_ART[(self.lives - 7) * -1])

    def refresh_the_playboard(self):

        """
        Should be called after each guess. It displays the ASCII logo,
        relevant hangman picture, along with the updated word display.
        """
        self.clear_console()
        self.print_out_logo()
        self.print_out_logo_art()
        self.print_word_display()

    def display_message(self, duration,  message):
        """
        Takes a string as an argument , and will clear everything on the screen
        for a moment of time, before refreshing it again. This allows the user
        to clearly see the message without any other distractions.
        """
        self.clear_console()
        self.print_out_logo()
        print(message)
        time.sleep(duration)
        self.refresh_the_playboard()

    def make_guess(self):

        """
        This function will get the user to make a guess , and only return the
        value after it has been validated to make sure that isn't either an
        empty string, an integer, or a string that is longer than one letter.
        The returned value will be converted to lowercase.
        """

        guess = input("Please guess a letter: ")

        data_valid = False

        while data_valid is not True:

            if guess == "":

                m = "Come on , you have to type something! Try again:"
                self.display_message(2, m)
                guess = guess = input("Please guess a letter: ")

            elif guess.isdecimal():

                m = "You can't type a number! Try again: "
                self.display_message(2, m)
                guess = guess = input("Please guess a letter: ")

            elif not guess.isalpha():
                m = "You can't type a symbol! Try again: "
                self.display_message(2, m)
                guess = guess = input("Please guess a letter: ")

            elif len(guess) > 1:
                m = "Guess one letter only please. Try again: "
                self.display_message(2, m)
                guess = guess = input("Please guess a letter: ")

            else:
                return guess.lower()

    def check_guess(self, guess):

        """
        By passing and calling the make_guess function as an argument,
        this function will check to see if the letter was already used.
        If not , it will check to see if the letter is indeed in the word that
        is being guessed. If the letter is in the word, it replaces
        the blank underscore in the self.display array and updates
        the display with a message . The inverse is true in the case of a
        'miss', and a live is deducted from the player.
        """

        if guess in self.guessed_letters:
            self.refresh_the_playboard()
            print(f"YOU GUESSED THE LETTER '{guess.upper()}' ALREADY! ")

        elif guess in self.word_list:

            for position in range(len(self.word_list)):
                letter = self.word_list[position]
                if letter == guess:
                    self.display[position] = guess.upper()

            self.refresh_the_playboard()
            print("")
            print("YOU GOT A HIT!: " + random.choice(HIT))

        else:
            self.lives -= 1
            self.refresh_the_playboard()
            print("")
            print("NO MATCH: " + random.choice(MISS))

        if guess not in self.guessed_letters:
            self.guessed_letters.append(guess.lower())

    def reset_the_game(self):

        """
        Resets all the values necessary for the game to start fresh,
        updates the screen art and then calls the play_game function itself.
        """
        self.word_string = choose_word()
        self.word_list = list(self.word_string)
        self.lives = 7
        self.display = []
        self.create_word_display()
        self.guessed_letters = []
        self.print_out_logo()
        self.refresh_the_playboard()
        self.play_game()

    def ask_to_continue(self):

        """
        Asks the user for yes or no input to determine whether or not they
        would like to continue to use the program.
        """

        while True:

            self.clear_console()
            self.print_out_logo()
            decision = input("Do you want to continue?\nPlease type y/n: ")
            if decision == "y":
                self.reset_the_game()
            elif decision == "n":
                quit()
            else:
                m = "Please type y/n. "
                self.display_message(2, m)

    def play_game(self):

        """
        Loops the game until the player either guesses all the letters, or runs
        out of lives. A corresponding message is then displayed.
        """
        while "_" in self.display and self.lives > 1:
            self.check_guess(self.make_guess())

        if "_" not in self.display:
            m = f"That's right , the word was {self.word_string.upper()}."
            self.display_message(3, m)
            m = "YOU HAVE WON THE GAME!"
            self.display_message(3, m)
            self.ask_to_continue()
        else:
            m = f"No, no , no , the word was {self.word_string.upper()}!"
            self.display_message(3, m)
            m = "YOU LOSE!"
            self.display_message(3, m)
            self.ask_to_continue()


new_game = Game()
new_game.refresh_the_playboard()
new_game.play_game()
