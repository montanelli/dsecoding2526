# write a Python function that returns a dictionary with student names as keys and corresponding average of evaluations for each student (round the result to two decimals)

import sys


def calculate_avg(students, grades):
    results = {}
    for s, g in zip(students, grades):
        avg = sum(g) / len(g)
        results[s] = round(avg, 2)

    return results

# solution with list comprehension
def calculate_avg_lc(students, grades):
    return {s: round(sum(g) / len(g), 2) for s, g in zip(students, grades)}


# main
students = ["John", "Mark", "Alice"]
grades = [[27, 28, 29], [26, 27, 28], [18, 19, 30]]

results = calculate_avg(students, grades)
results_lc = calculate_avg_lc(students, grades)
print(results)
print(results_lc)

sys.exit()
