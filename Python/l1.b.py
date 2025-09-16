# alternative solution to l1.a
# Implementing a program to calculate the final grade given a course with three modules (different weights on modules)

# in this example, the module grades are given in a list with corresponding weights
# position 1: module 1
# position 2: module 2
# position 3: module 3
grades = [20, 24, 18]
weights = [0.25, 0.25, 0.5]

# list comprehension: iterative processing of list elements to perform a given operation (multiply in this example)
# zip runs over the two lists and gets pairs of elements with same position  in the lists
result = [g * w for g, w in zip(grades, weights)]

# iterate over result to get the final grade
grade = 0
for g in result:
    # grade = grade + g
    grade += g
    # print(g)
    # print(grade)

# alternative to the loop: sum can be used to sum up the elements of a list
# grade = sum(result)

if grade >= 18:
    result = "exam passed"
else:
    result = "exam not passed"

print("the average is", str(round(grade, 2)))

exit()
