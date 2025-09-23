# manipulation of text/strings
s = "stefano"

# basic built--functions of Python to manipulate strings
print(s.upper())
print(s.lower())
print(s.capitalize())

# slicing
# s t e f a n o
# 0 1 2 3 4 5 6
# [start:stop:step]
## start: this is the first char to slice in the string
## stop: this is the index of the final char to slice (excluded)
## step: the number of chars to move inside the slice
## start has 0 as default
## stop has the last char as default
## step has 1 as default
print(s[2])  # print the "e" element
print(s[0])  # print "s"
print(s[1:4])  # tef
print(s[1:5:2])  # tf
s1 = s[:5]  # s1 = stefa
print(s1)
s = s[1:]  # tefano
print(s)
print(s[::2])  # tfn

# slicing with negative positions
s = "montanelli"
#  m   o  n  t  a  n  e  l  l  i
#  0   1  2  3  4  5  6  7  8  9
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(s[-5:-1])  # nell
print(s[:-7])  # mon
print(s[-3:])  # lli
print(s[-2:-6:-1])  # llen
print(s[::-1])  # illenatnom
print(s[::-2])  # ilnto
