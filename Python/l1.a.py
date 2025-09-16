# Implementing a program to calculate the final grade given a course with three modules (equal weights on modules)

# a possible extension is to get the module grades from the terminal/user
# in this example, the module grades are assigned to variables
M1 = 20
M2 = 24
M3 = 18

grade = (M1 + M2 + M3) / 3

if grade >= 18:
    result = "exam passed"
else:
    result = "exam not passed"

# raw output with single prints:
# print("the average is ")
# print(grade)
# print(": ")
# print(result)

# round the final grade - two decimals
gradeRound = round(grade, 2)
# cast the numeric grade to string
stringGrade = str(gradeRound)

print("the average is", stringGrade)

# the assignments can be skipped by invoking functions in the print instruction
print("the average is", str(round(grade, 2)))

# alternative syntax for printing variable values in a string
print(f"the average grade is {stringGrade}: {result}")

exit()
