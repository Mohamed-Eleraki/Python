# set not ordered and not indexed
# set is mutable and can be changed
# items is unique, not duplicated


my_awesome_set = {"one", "two", "one", 1, 2, 1.5, True}
print(my_awesome_set)  # the more you run the more you found it's not ordered
#print(my_awesome_set[1])  # TypeError: 'set' object is not subscriptable
my_awesome_set.add("three")
print(my_awesome_set)

# remove all elements from the set
my_awesome_set.clear()
print(my_awesome_set)

# union of two sets
my_awesome_set_2 = {"one", "two", "one", 1, 2, 1.5, True}
my_awesome_set_3 = {"three", "four", "one", 1, 2, 1.5, True}
my_awesome_set_4 = my_awesome_set_2.union(my_awesome_set_3)
print(my_awesome_set_4)

# copy a set
my_awesome_set_5 = my_awesome_set_4.copy()
print(my_awesome_set_5)

# difference between two sets
my_awesome_set_6 = my_awesome_set_2.difference(my_awesome_set_3)
print(my_awesome_set_6)

# remove an element from the set
my_awesome_set_2.remove("one")
print(my_awesome_set_2) 

# if you provide an element not exist in the set will retrun an error 
# instead use discard will not return an error
# discard an element from the set
my_awesome_set_2.discard("one")
print(my_awesome_set_2)


# for more check video number 28, 29