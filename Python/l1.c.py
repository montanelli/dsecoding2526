# write a program that
## 1. asks the user to enter a positive integer (n)
## 2. prints all numbers from 1 to n
## 3. For each number it prints "even" if it is divisible by 2 or "odd" otherwise
## 4. In the end, it prints the sum of all the numbers

## 1. asks the user to enter a positive integer (n)
n = int(input("Enter a positive integer number: "))

## 2. prints all numbers from 1 to n
i = 1
sumValues = 0
while i <= n:
    print(i)
    ## 3. For each number it prints "even" if it is divisible by 2 or "odd" otherwise
    # if bool((i % 2)):
    restPart = i % 2
    if restPart == 1:
        print(f"the number {i} is odd")
    else:
        print(f"the number {i} is even")

    # sum the value of i to sumValues
    sumValues += i

    # i = i +1
    i += 1

## 4. In the end, it prints the sum of all the numbers
print("the sum of numbers is " + str(sumValues))

exit()
