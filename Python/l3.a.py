# class of 20250929

# exercise on control and data structures

# guess the number

# the script generates a random integer number in a given range
# the user is asked to guess the number
# the script return a feedback (right/wrong)
from random import randrange


min_limit = 1
max_limit = 10


# step1: number generation
def think_guess(the_min, the_max):
    return randrange(the_min, the_max)


n = think_guess(min_limit, max_limit)

# step2: ask the guess to the user
the_guess = input(f"guess a number in the range {min_limit}-{max_limit}:")

# check that the_guess is an integer
try:
    the_guess = int(the_guess)
except ValueError:
    the_guess = None

feedback = None
if the_guess is None:
    feedback = "Your input is not a number. Cannot guess."

# write a test to stop the script when the_guess is outside the range
if the_guess is not None:
    if (the_guess < min_limit) or (the_guess > max_limit):
        feedback = "Your input is outside the range."

# step3: conditional statement: check the guess
# in case of wrong guess we return a different feedback when the guess is lower than n and the guess is grater than n
# details on the if statement and nested branches
# https://docs.python.org/3/tutorial/controlflow.html#if-statements
if feedback is None:
    if n == the_guess:
        feedback = "Congratulations! you are right"
    elif n > the_guess:
        feedback = "no, your guess is lower than necessary. The number is: " + str(n)
    else:
        feedback = "no, your guess is greater than necessary. The number is: " + str(n)

print(feedback)

exit()
