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
