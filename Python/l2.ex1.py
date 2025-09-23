# write a program that takes a fiscal code in input. The code is formatted as follows:
## ABCDEF99B12
# first 3 chars -> lastname (ABC)
# next 3 chars -> firstname (DEF)
# next 2 chars -> birth year (99)
# next 1 chars -> letter of the month (A:JAN, B:FEB, ...)
# next 2 chars -> day of birth (12)
# the program has to extract the code parts and returns a readable text 
cf = str(input("Enter a fiscal code: "))
lastname = cf[0:3]    
firstname = cf[3:6]       
year = cf[6:8]       
month = cf[8]         
day = cf[9:11]    

months = {
    "A": "January",
    "B": "February",
    "C": "March",
    "D": "April",
    "E": "May",
    "H": "June",
    "L": "July",
    "M": "August",
    "P": "September",
    "R": "October",
    "S": "November",
    "T": "December"
}

month = months.get(month, "Unknown")

# Output
print("Lastname:", lastname)
print("Firstname:", firstname)
print("Year: 20" + year)   # better?
print("Month (letter):", month)  # better? use dict
print("Day:", day)