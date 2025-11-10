# define a Python function that returns the Least Frequent Character in a String
# return all the elements with the minimum frequency
def least_frequent_char(the_string):
    frequencies = {}
    for i in the_string:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    the_min = min(frequencies.values())
    the_leasts = []
    for f in frequencies:
        if frequencies[f] == the_min:
            the_leasts.append(f)
    return the_leasts


s = "things never change if you do not try"
print(least_frequent_char(s))
