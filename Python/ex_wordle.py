"""Play Wordle with Python"""

# https://www.nytimes.com/games/wordle/index.html

# Players have six attempts to guess a five-letter word, with feedback given for each guess in the form of colored tiles indicating when letters match or occupy the correct position

# rules
## You have to guess the Wordle in six goes or less
## Every word you enter must be an English word, presumably it should exists on a dictionary.
## A correct letter turns green
## A correct letter in the wrong place turns yellow
## An incorrect letter turns gray
## Letters can be used more than once

# pay attention to:
## handle guessed word not existing or with lenght not equal to 5
## repeated guess by the user does not consume additional attempts

# we need a set of english words
# https://www.kaggle.com/datasets/rtatman/english-word-frequency?resource=download

import sys
import csv
from random import choice


# setup
tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}

max_attempts = 6

# use a function to validate each guess 
def validate_guess(guess, target):
    
    # Loop through every letter of the guess
    
    
        # If the letter is in the correct spot, color it in green and add the green tile
      
            # Replace the existing letter in the answer with -
            # on the need to replace the letter with hypen, consider this example:
            # target: panel
            # guess: banal
           
           
        # whereas if the letter is in the correct spot, color it in yellow and add the yellow tile
       
        # Otherwise, the letter doens't exist, just add the grey tile





# main
# load the en dictionary from file


# skip the first row with headers

# drop frequencies
# keep only words with len 5 (switch to uppercase)


# Select the target word to guess


# Keep playing until the user runs out of tries or finds the word
# you need to store the history of attempts


# print a final message whenever the target is guessed or not

