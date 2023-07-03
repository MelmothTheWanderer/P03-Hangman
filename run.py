# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random 
from words import list_of_words


for _ in range(10):
    print(random.choice(list_of_words))