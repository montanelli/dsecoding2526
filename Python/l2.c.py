# Useful composite datastructures:
# lists / tuples
# dictionaries
# sets

## list ##
# features:
# Order: the items in a list have a specific position (index)
# index: the items ofa list can be accessed by using the index position
# mutability: the items can be updated, the list can received additional items and existing items can be deleted
# heterogeneity: the items can contain values of different type

# list of seasons
# init the empty list
seasons = list()
seasons = []

# insert
seasons.append("summer")  # item in position [0]
seasons.append("winter")  # item in position [1]
seasons.append("spring")  # items in position [2]

print(seasons)
print(seasons[2])
seasons[2] = 12

print(seasons)
seasons.insert(1, "autumn")

seasons.remove(12)
print(seasons)

# useful methods
# seasons.sort()
seasons1 = sorted(seasons)
print(seasons1)

# reversing of a list
seasons.reverse()
print(seasons)

# reverse sorting
seasons.sort()
seasons.reverse()
print(seasons)

# list slicing
# [start:stop:step]
## start: this is the first char to slice in the string
## stop: this is the index of the final char to slice (excluded)
## step: the number of chars to move inside the slice
## start has 0 as default
## stop has the last char as default
## step has 1 as default
dwarfs = ["doc", "bashful", "grumpy", "sneezy", "happy", "sleepy", "dopey"]

print(len(dwarfs))  # 7

print(dwarfs[1:5])  # [bashful, grumpy, sneezy, happy]
print(dwarfs[:5])  # [doc, bashful, grumpy, sneezy, happy]
print(dwarfs[::-1])  # equivalent to dwarfs.reverse()
print(dwarfs[-1:-5:-1])  # ['dopey', 'sleepy', 'happy', 'sneezy']
print(dwarfs[-1:-5:-2])  # ['dopey', 'happy']

# list of lists
# example of a 3X3 matrix
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(len(A))  # 3
print(A[0][2])  # number 3
print(A)  # printing of entire matrix
print(A[1])  # printing of second row
print(A[0][-1])  # number 3


# print the values of the 2nd column
# method 1: we use a loop
# write a function that extracts a specific column from a list of lists
def extract_column(M, c):
    col = list()
    for e in M:
        # run over the matrix row by row
        col.append(e[c - 1])

    return col


def extract_column_comprehension(M, c):
    # method 2 based on list comprehension
    return [e[c - 1] for e in M]


C2 = extract_column(A, 2)
# what happen when you call the following:
# C2 = extract_column(A, 4)
# an out of range error raises: a good code has to manage this kind of errors

C2 = extract_column_comprehension(A, 2)

print(C2)

## tuples ##
# tuple are immutable lists
# Order: the items in a list have a specific position (index)
# index: the items ofa list can be accessed by using the index position
# immutability: the items are static: cannot be changed
# heterogeneity: the items can contain values of different type

brands = ("IBM", "Apple", "Microsoft", "Oracle")

print(brands[0])  # IBM

# editing of a tuples is not allowed (the tuple is immutable)
# brands.append("Postgres")
# brands[0] = "Firefox"

# tuples are more efficient than lists in terms of memory usage
