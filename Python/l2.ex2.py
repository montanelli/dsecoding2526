# insert a string in the middle of another
s1 = "****"
s2 = "coding@dse"

print("Original Strings are", s1, s2)

# middle index number of s1
mi = int(len(s1) / 2)

# get character from 0 to the middle index number from s1
x = s1[:mi:]
# concatenate s2 to it
x = x + s2
# append remaining character from s1
x = x + s1[mi:]
print("After insert the new string in middle is", x)