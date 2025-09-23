## sets ##
# a set is a composite datastructure where elements are unique
# the set definition is taken from the math notion
# Unorder: the items in a set have not index
# Uniqueness: duplicate items are not allowed
# Unindexed: the items of a set can not be accessed by using an index position
# mutability: the items are can be edited (add, delete, update)
# heterogeneity: the items can contain values of different type

fruits = set()

fruits.add("banana")
fruits.add("pear")
fruits.add("melon")

print(fruits)
# a type error is raised when you access items by position (no index is defined)
# fruits[0]
# fruits[2] = "peach"
fruits.add("peach")
fruits.remove("melon")
fruits.add("peach")
fruits.add("peach")
print(fruits)

# error when you remove an item that is not in the set
# fruits.remove("apple")

# use discard to avoid errors
fruits.discard("apple")
print(fruits)

# sets are useful when interesed in union, instersection, difference

tom_friends = {"Mark", "Ann", "Alice", "John"}
carol_friends = {"Ann", "Angela", "Mark", "William"}

# | is the union operator
print(tom_friends | carol_friends)  #
print(tom_friends.union(carol_friends))

# intersection
print(tom_friends & carol_friends)
print(tom_friends.intersection(carol_friends))

# set difference
# A - B means the elements of A that are not present in B
# B - A means the elements of B that are not present in A
print(tom_friends - carol_friends)
print(tom_friends.difference(carol_friends))

print(carol_friends - tom_friends)

# symmetric difference
# A∆B = (A-B) ∪ (B-A)
print(tom_friends ^ carol_friends)
print(tom_friends.symmetric_difference(carol_friends))


# you have a list of items with duplicates
my_list = [
    "printer",
    "scanner",
    "mouse",
    "printer",
    "scanner",
    "printer",
    "laptop",
    "mouse",
]

# what are the products (unique) that you have in my_list
my_products = list(set(my_list))
print(my_products)
