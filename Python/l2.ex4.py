# Assume to have an input list. Write a function to remove all the occurrences of a given value

scores = [34, 55, 21, 87, 42, 90, 67, 55, 42, 21, 77, 100]

def drop_all_occurrences(l, needle):
    while needle in l:
        l.remove(needle)

    return l 

print(drop_all_occurrences(scores, 42))

# Write a function to remove all the list items with value over a given threshold

def filter_over_th(l, th):
    return [p for p in l if p > th]


print(filter_over_th(scores, 50))

# Assume to have an input list of int values. Write a function to return the average value considering all the list items

def avg_list(l):
    # manage the case of an empty list
    return sum(l) / len(l) if l else 0

print(avg_list(scores))
print(avg_list([]))

# Assume to have an input list of int values. Write a function to return the max and min values in the list
# find a solution based on iteration
def max_min(l):
    return (max(l), min(l))

print(max_min(scores))

# Build a matrix M1 of size K where an element of index (i,j) contains the value corresponding to i+j. 
# Return also i) the list with the average of values by row, ii) the list with the average of values by column
def build_matrix_and_averages(K):
    # Step 1: Build the matrix
    M1 = [[i + j for j in range(K)] for i in range(K)]
    
    # Step 2: Row averages
    row_averages = [sum(row) / K for row in M1]
    
    # Step 3: Column averages
    col_averages = [sum(M1[i][j] for i in range(K)) / K for j in range(K)]
    
    return M1, row_averages, col_averages

# main
K = 5
M1, row_avg, col_avg = build_matrix_and_averages(K)

print("Matrix M1:")
for row in M1:
    print(row)

print("\nRow averages:", row_avg)
print("Column averages:", col_avg)