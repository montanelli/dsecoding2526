import sys


# write a Python function to remove the first x elements  and the last y elements from a list
def slice_list(alist, x, y):
    # check if the x, y params are valid input:
    # accept only positive integers
    # accept only x, y that are real list positions
    # accept only x<y
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Only integers are valid params")
        return None

    if x < 0 or y < 0:
        raise ValueError("Negative values are not allowed")

    if x >= y:
        raise ValueError("x must be lower than y")

    if (x >= len(alist)) or (y >= len(alist)):
        raise ValueError("x, y must be a valid list position")

    return alist[x:-y]


# write a Python function to split a list into a given number of segments.
# example with 2 segments. x is half-index; y is len(list)
# list[0:x], list[x:y]. it is equivalent to
# list[0:x], list[x:2x].
# example with 3 segments. x is 1/3-index
# list[0:x], list[x:2x], list[2x:3x]
def split_list(alist, segments):
    length = len(alist)
    return [
        alist[i * length // segments : (i + 1) * length // segments]
        for i in range(segments)
    ]


segments = [2, 3, 4]
animals = ["dog", "cat", "elephant", "tiger", "bear", "lion"]

try:
    print(slice_list(animals, 1.1, 5))
except ValueError as e:
    print(e)

for i in segments:
    animal_segments = split_list(animals, i)
    # print(animal_segments)

sys.exit()
