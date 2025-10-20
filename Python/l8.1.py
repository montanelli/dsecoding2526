"""Play Wordle with Python. Object-oriented version."""

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

# from termcolor import colored
from datetime import datetime


# return the list of possible target words given a dictionary of English from file
def load_dictionary():
    # read the file
    with open("datasets/en_unigram_freq.csv", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        records = list(reader)

    # drop the first row (the header)
    records = records[1:]
    # print(records[0])
    # ['the','23135851162']

    # drop the frequecies
    # dict = ['the', 'of', 'and', 'to', ...]
    dict = [r[0] for r in records]

    # alternativa (but explicit)
    # dict = []
    # for r in records:
    #     dict.append(r[0])

    return None

    # take only five-letter words


class Wordle:

    max_attempts = 6

    target_word = None

    en_5_dict = []
    guess_history = []
    colored_history = []
    tile_history = []

    def __init__(self, attempts=None):
        # set the max number of attempts
        if attempts is not None:
            self.max_attempts = attempts

        # pick up a target to guess
        self.en_5_dict = load_dictionary()

    def printWordle(self):
        print(f"this match has {self.max_attempts} attempts")

    def validate_guess(self, guess):
        tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}
        guessed = []
        pattern = []


# main code
mygame = Wordle()
# mygame.printWordle()

sys.exit()
