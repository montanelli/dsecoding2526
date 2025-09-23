# given a string in input, we want to check if it is palidrome or not
# examples of palindrome: civic, radar, 1234321


# we define a function for performing the comparison
# check_pal receives a string variable as input (w)
# check_pal returns a boolean: True when w is palindrome; False otherwise
# as a further parameter, allows to choose between case-sensitive check and case-insensitive check: if case = True then words with different casing are taken as they are
def check_pal(w, case_sensitive=True):

    if isinstance(w, str):
        if not case_sensitive:
            w = w.lower()

        if w == w[::-1]:
            return True
        else:
            return False
    else:
        return False


# main code
# call the check_pal function
my_word = "radar"
r = check_pal(my_word, False)
# invoke the function with True as case_sensitive
my_word = "Radar"
r = check_pal(my_word)

if r:
    print(f"the word {my_word} is palindrome")
else:
    print(f"the word {my_word} is not palindrome")

exit()
