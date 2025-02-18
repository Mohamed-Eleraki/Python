#########################################
# Tuple is immutable, cannot be changed #
#########################################

# With the parenthesis
my_awesome_tuple = ("one", "two", "one", 1, 2, 1.5, True)
print(my_awesome_tuple)
print(type(my_awesome_tuple))

# Withtout the parenthesis
my_awesome_tuple_2 = "Mohamed", "Ali", "Ahmed", 1, 2, 1.5, True
print(my_awesome_tuple_2)
print(type(my_awesome_tuple_2))

# Access the value
print(my_awesome_tuple[1])  # two
print(my_awesome_tuple[1:3])  # ('two', 'one')  # the last value will not include so must be 3


# my_awesome_tuple[1] = "three"  # TypeError: 'tuple' object does not support item assignment


# Declear a tuple with a single value
my_awesome_tuple_3 = (1, )
print(my_awesome_tuple_3)
print(type(my_awesome_tuple_3))
print(len(my_awesome_tuple_3))


# extend a tuple with another tuple
my_awesome_tuple_4 = (1, 2, 3)
my_awesome_tuple_5 = (4, 5, 6)
my_awesome_tuple_6 = my_awesome_tuple_4 + ("a", "b") + my_awesome_tuple_5
print(my_awesome_tuple_6)
print(type(my_awesome_tuple_6))

# Repeat a tuple prtinting
print(my_awesome_tuple_4 * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)


# Counting the number of occurance of a value
print(my_awesome_tuple_4.count(1))  # 1


# Find the index number of a value - where is the 2 placed.
print(my_awesome_tuple_4.index(2))  # 1


# District the tuple vlaues to variables
a, b, c = my_awesome_tuple_4
print(a)  # 1
print(b)  # 2
print(c)  # 3
# you can also use the following syntax
a, b, *c = my_awesome_tuple_4
print(a)  # 1
print(b)  # 2
print(c)  # [3]
# you can also use the following syntax
a, *b, c = my_awesome_tuple_4

# you can also use the following syntax - ignoring
my_awesome_tuble_5 = (1,2,3,4)
a, _, _, c = my_awesome_tuble_5
print("####")
print(a)  # 1
print(c)  # 4
