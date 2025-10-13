# consider a dataset with supermarket data
# open the file, load the data and work on columns:
import csv

with open("datasets/supermarket.csv", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    records = list(reader)

# print(records[0])
records = records[1:]

# create a list with unique branches
# unique_branch = [ 'Giza', 'Alex', 'Cairo' ]
# create a list of lists containing the sales amounts for each branch
# branch_sales = [[ 239383, 38844 ], [ 833748, 84848, 9288 ], [ 38388, 448439, 3999 ]]
unique_branch = []
branch_sales = []
for r in records:
    ## index 1: branch name
    ## index 9: amount of sales of the branch
    # print(r[1])
    # print(r[9])
    # break
    if r[1] not in unique_branch:
        # add a new element to unique_branch and branch_sales when r is about a new branch
        unique_branch.append(r[1])
        first_sale = float(r[9].replace(".", ""))
        branch_sales.append([first_sale])
    else:
        # add a new element to branch_sales when the brach is already in unique_branch
        # find the index of the branch in unique_branch and append the sale_amount in branch_sale to the item with corresponding index
        branch_index = unique_branch.index(r[1])
        branch_sales[branch_index].append(float(r[9].replace(".", "")))

# print(unique_branch)
# print(branch_sales)

# calculate the sum of sales for each branch
branch_sum_sales = []
for e in branch_sales:
    branch_sum_sales.append(sum(e))

# print each element of unique branch with corresponding sum of sales
for b, a in zip(unique_branch, branch_sum_sales):
    print(f"the sales of branch {b} are {a}")

exit()
