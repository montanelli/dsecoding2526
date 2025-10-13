# lambda function: aka anonymous functions

# write a function that calculates the power of a given number
power = lambda x: x**2


# write a function that produces the sum of two given numbers
def my_sum(x, y):
    return x + y


print(my_sum(5, 3))

# solution with lambda
# variable lambda parameters: expression
my_sum1 = lambda x, y: x + y

print(my_sum1(10, 4))

# lambda with conditions
greater = lambda a, b: a if a > b else b

print(greater(8, 3))

# lambda with sorting
my_data = [(1, 3), (4, 2), (2, 1)]
# sort my_data according to the 2nd element of each tuple
sorted_data = sorted(my_data, key=lambda x: x[1])
print(sorted_data)

# lambda with filter
my_data = [1, 2, 3, 4, 5, 6]
even_data = list(filter(lambda x: x % 2 == 0, my_data))
print(even_data)

# lambda and map function
my_numbers = [1, 2, 3, 4, 5]
powers = list(map(lambda x: x**2, my_numbers))
print(powers)


exit()
