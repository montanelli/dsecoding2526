## dictionaries ##
## associative vectors of pairs key->value
# order: the items has a position defined by the keys
# Keys must be unique in the dict
# indexed: the items of a dict can be accessed through the keys
# mutability: the items are can be edited (add, delete, update)
# heterogeneity: the items both keys/values can have different type

capitals = {"France": "Paris", "Italy": "Rome", "Germany": "Berlin", 55: "fiftyfive"}

for item in capitals:
    print(f"the capital of {item} is {capitals[item]}.")

for k, v in capitals.items():
    print(f"the capital of {k} is {v}.")

# adding items to dicts
capitals["Spain"] = "Madrid"

capitals["Italy"] = "Milan"

del capitals["Italy"]

# error when you access items that are not existing
# print(capitals["Belgium"])

# use get to avoid errors on non existing elements
print(capitals.get("Belgium"))

# useful methods on dictionaries
print(capitals.items())
print(capitals.keys())
print(capitals.values())
