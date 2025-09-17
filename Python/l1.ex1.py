# summary exercise 2. Write a program that:
## Asks the user to enter a positive integer (n).
## prints a triangle of numbers till n. Example with n=3
# 1
# 1 2
# 1 2 3
n = int(input("Enter a positive integer: "))
print("\nTriangle of numbers till ", n)
for row in range(1, n + 1):        # external cycle: rows till n
    for column in range(1, row + 1):  # internal cycle: numbers in a row
        print(column, end=" ")
    print()  # new line after each row