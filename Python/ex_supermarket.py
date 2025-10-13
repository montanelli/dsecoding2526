# build a list of sales by branch
# build a list of lists where each row is about a branch in unique_branches
# each row contains the list of sales of the branch in unique_branches with the same index
# consider A, B, C as branches in unique_branches
# sales will contain three items and each item is a list of sales
# the 1st item of sales is the list of sales of A, and so on...

# create a solution using only lists and another using dictionaries

import sys
import csv

# returns a list with unique values in my_list
def unique(my_list):



# read a csv file and import in lists
# case study based on
# https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales
with open("dataset/supermarket.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

records.pop(0)

# build a list containing the branches that appear in the second column of the file (unique values)
# use a function to remove duplicates
# unique_branches = [ 'Alex', 'Giza', 'Cairo' ]


sales = []
for r in records:
    # in r[1] we have the name of the current branch
    # in r[9] we have the amount of sales
    

# total sales: calculate the overall amount of sales i) for each branch, and ii) considering all the branches

# print(sales[0])

# print the name of the branch and the corresponding sum of sales





sys.exit()
