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
from termcolor import colored
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

    # alternative (but explicit)
    # dict = []
    # for r in records:
    #     dict.append(r[0])

    # take only five-letter words
    dict_5_letter = []
    for w in dict:
        if len(w) == 5:
            dict_5_letter.append(w)

    # list comprehension
    dict_5_letter = [w for w in dict if len(w) == 5]

    return dict_5_letter


class Wordle:

    max_attempts = 6

    target_word = None

    en_5_dict = []
    guess_history = []
    colored_history = []
    tile_history = []

    def __init__(self, attempts=None, testing=False):
        # set the max number of attempts
        if attempts is not None:
            self.max_attempts = attempts

        # load the dictionary
        self.en_5_dict = load_dictionary()

        # pick up a target to guess
        self.set_target()
        if testing:
            self.print_target()

        # play the game
        self.play_game()

    # the method has the goal to setup the target word to guess
    # we use the choice function to pick up a random word from en_5_dict
    def set_target(self):
        self.target_word = choice(self.en_5_dict)

    def print_target(self, f=None):
        if f is not None:
            f.write(f"The target word is {self.target_word}.\n")
        else:
            print(f"The target word is {self.target_word}.")

    def add_to_history(self, guess):
        self.guess_history.append(guess)

    def print_last_guess(self):
        print(self.guess_history[-1])

    def print_last_tile(self):
        print(self.tile_history[-1])

    def print_history(self, f=None):
        for i, g in enumerate(self.guess_history):
            if f is not None:
                f.write(f"Attempt {i+1}: {g}.\n")
            else:
                print(f"Attempt {i+1}: {g}")

    def validate_guess(self, guess):
        tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}
        guessed = []
        pattern = []

        correct_places = list(map(lambda x, y: x == y, guess, self.target_word))
        # print(correct_places)

        # eliminate the letters in the green position (correct_places)
        target = [y if not x else "-" for x, y in zip(correct_places, self.target_word)]

        # print(target)

        correct_letters = list(map(lambda x: x in target, guess))

        # print(correct_letters)

        for i, (x, y) in enumerate(zip(correct_places, correct_letters)):
            if x:
                guessed.append(colored(guess[i], "green"))
                pattern.append(tiles["correct_place"])
            elif y:
                guessed.append(colored(guess[i], "yellow"))
                pattern.append(tiles["correct_letter"])
            else:
                guessed.append(guess[i])
                pattern.append(tiles["incorrect"])

        # print(guessed)
        # print(pattern)
        self.colored_history.append("".join(guessed))
        self.tile_history.append("".join(pattern))

    def save_game(self):
        # open with "a" (append); "w" (write)
        f = open("wordle.txt", "a")
        now = datetime.now()
        # example of datetime formatting 10/11/2025 15:44:35
        now_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"Wordle is playes on {now_string}.\n")
        self.print_target(f)
        self.print_history(f)
        f.write("----------\n\n")
        f.close

    def play_game(self):
        print("Welcome to the Wordle game!")
        print(f"You have {self.max_attempts} attempts to guess a target word")
        print("Enjoy the game!")

        attempt = 1
        is_guessed = False
        # loop on attempts
        while (attempt <= self.max_attempts) and (not is_guessed):

            # loop on a single attempt
            bad_guess = True
            while bad_guess:
                guess = input("Type your guess:")

                # check the input and reject the guess if:
                # the guess is not 5 letters
                # the guess is not in the dictionary
                # the guess is already guessed (already in the history)
                if len(guess) != 5:
                    print("the guess is not composed of 5 letters!")
                elif guess not in self.en_5_dict:
                    print("the guess is not a valid English word!")
                elif guess in self.guess_history:
                    print("the guess has been already attempted!")
                else:
                    bad_guess = False

            # add the guess to the history
            self.add_to_history(guess)

            # create a feedback on the guess (validate the guess)
            self.validate_guess(guess)

            self.print_last_guess()
            self.print_last_tile()

            # check if the guess is the target
            if self.target_word == guess:
                print(
                    f"Great! You hit the target in {attempt} tries, congratulations! Hope to see you for another match."
                )
                is_guessed = True
            else:
                print("The target is missed. Try another guess")

            # increase the counter
            attempt += 1

        # code after the loop
        # write a message only when the target is missed and the user reached the max number of attempts
        if not is_guessed:
            print(
                f"Unfortunately you lose. The target was {self.target_word}. Play again"
            )

        self.save_game()


# main code
# mygame = Wordle()
mygame = Wordle(2, True)


sys.exit()
