# print boolean that is true when s contains both a letter and a digit

s = "python is top programming language"

flag1 = False
flag2 = False

for i in s:

    if i.isalpha():
        flag1 = True

    if i.isdigit():
        flag2 = True

print(flag1 and flag2)
