# count the word occurrences in a text
# read a text from file
# clean the text (drop punctuation)
# text tekenization
# create a dictionary where each item has a word as a key and the number of occurrences in the text as a value

import string
import re
from collections import Counter

# read the file
# it is a good practice to manage errors
try:
    my_file = open("datasets/Bohemian_Rhapsody_lyrics.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("File not found, I'm exiting")
    exit()

# reading large files can be inefficient: use other methods
my_text_file = my_file.read()

# print(my_text_file)
# print(string.punctuation)

# drop punctuation (method 1)
# use string.punctuation
# list comprehension:
# [ expression for item in iterable if condition ]
cleaned_text = [c for c in my_text_file if c not in string.punctuation]
cleaned_text = "".join(cleaned_text)
# print(cleaned_text)

# drop punctuation (method 2)
# use regular expressions
# \w matches any word
# \s matches a blank space
# ^ matches the negation of the expression content
cleaned_text = re.sub(r"[^\w\s]", "", my_text_file)

# print(cleaned_text)

lower_cleaned_text = cleaned_text.lower()
tokenized_text = lower_cleaned_text.split()

print(tokenized_text)

# count the words
# build a dict where an element key is a word and the values are the number of occurrences of that word
word_counts = dict()
word_counts = {}

for item in tokenized_text:
    if item in word_counts:
        word_counts[item] += 1
    else:
        word_counts[item] = 1

# print(word_counts)
for w, c in word_counts.items():
    print(f"the word '{w}' has {c} occurrences in the text.")


# find the top occurring word(s) in the text
# method 1. use keys(), values(), and sort()
values = list(word_counts.values())
# print(values)
# values.sort(reverse=True)
values.sort()
# print(values)

# top_value = values[0]
top_value = values[-1]
# print("top value " + str(top_value))
# find the key with top_value as number of occurrences
for k in word_counts.keys():
    if word_counts[k] == top_value:
        # continue
        print("The word with top occurring value is " + k)
    else:
        continue

# method 2. user Counter library
dict_counter = Counter(word_counts)

# extract the word with top number of occurrences
top = dict_counter.most_common(1)
# extract the top-3 words by number of occurrences
top = dict_counter.most_common(3)

# print(top)
for item in top:
    print(f"the word {item[0]} has {item[1]} occurrences.")

# extract the words with the lowest number of occurrences
bottom = dict_counter.most_common()[-1]
print(bottom)
