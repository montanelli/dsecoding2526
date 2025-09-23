# given a string in input, we want to check if it is palidrome or not
# write a solution based on iteration (not string slicing)
def check_pal_iteration(w, c=True):
    """check if a word in input is palindrome through iteration.

    Keyword arguments:
    string -- the word to evaluate
    boolean -- a switch to decide whether to consider the letter cases

    Return:
    bool -- True when palindrome; False otherwise
    """
    if not c:
        w = w.lower()

    left = 0
    right = len(w) - 1
    is_pal = True

    while left < right:
        if w[left] != w[right]:
            is_pal = False
            # break stops the while and goes to the next operation after the loop
            break

        left += 1
        right -= 1

    return is_pal