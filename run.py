# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random 
from words import list_of_words


def choose_word(): 

    """This fucntion will return a random word fromn the list of random words
    in the words.py file
    """
    random_word = random.choice(list_of_words)
    return random_word

def display_word(word) : 
    display = [] 
    for _ in range(len(word)):
        display.append("_")
    return display

def print_out_display(display):
    print(f"Welcome to Hangman! The word that you are trying to guess has {len(display)} letters !")

print_out_display(display_word(choose_word()))

