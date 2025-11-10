import sys

# determine the output of the following codes
# A #
s = "never change your mind"
s1 = s.split()
s2 = " ".join(s1[1::2])

print(s2)  # change mind

# B #
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = [n for r in m for n in r]
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# C #
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

print([x for x in l1 if x in l2])  # [4, 5]

# D #
print([x for x in range(10, 100) if str(x) == str(x)[::-1]])
# Output: [11, 22, 33, ..., 99]

# E #
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d = {}
for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
    d[k1] = v1
    d[k2] = v2
print(d)  # {'a': 1, 'b': 2, 'c': 4}

sys.exit()
