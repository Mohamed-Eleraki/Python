# video number 21:
# The list is mutable and can be changed

my_awesome_list = ["one", "two", "one", 1, 2, 1.5, True]

print(my_awesome_list)
print(my_awesome_list[1])  # two
print(my_awesome_list[1:3])  # ['two', 'one']  # the last value will not include so must be 3
print(my_awesome_list[-1])  # True

my_awesome_list[1] = "three"  # Replace the value at index 1
print(my_awesome_list[1])  # three

my_awesome_list[:3] = "None" # Replace the value at index 1, 2, 3 with "None" characters values as below comment
print(my_awesome_list) # ['o', 'n', 'e', 'one', 1, 2, 1.5, True]


my_awesome_list[:3] = ["None"] # Replace the value at index 1, 2, 3 with "None"
print(my_awesome_list) # ['None', 'one', 1, 2, 1.5, True]


################################
# Append the value to the list #
################################
my_awesome_list_2 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_2.append("four")  # Append the value to the end of the list.
print(my_awesome_list_2)  # ['one', 'two', 'one', 1, 2, 1.5, True, 'four']

################################
# Insert the value to the list #
################################
my_awesome_list_3 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_3.insert(3, "three")  # Insert the value at index 3
print(my_awesome_list_3)  # ['one', 'two', 'one', 'three', 1, 2, 1.5, True]

####################################
# apend a list to a list as a list #
####################################
my_awesome_list_4 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_5 = ["three", "four"]
my_awesome_list_4.append(my_awesome_list_5)  # Append the list to the end of the list.
print(my_awesome_list_4)  # ['one', 'two', 'one', 1, 2, 1.5, True, ['three', 'four']]

#############################
# append a list to the list #
#############################
my_awesome_list_4 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_5 = ["three", "four"]
my_awesome_list_4.extend(my_awesome_list_5)  # Append the list to the end of the list.
print(my_awesome_list_4)  # ['one', 'two', 'one', 1, 2, 1.5, True, 'three', 'four']


######################
# remove from a list #
######################
my_awesome_list_6 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_6.remove("one")  # Remove the first occurrence of the value.
# to remove all the occurrence of the value, you can use a loop
print(my_awesome_list_6)  # ['two', 'one', 1,



###############
# sort a list #
###############

# sort does not support string and integer together
# just reverse the list in place and does not sort the list

my_awesome_list_7 = [4, 1, 3, 2]
my_awesome_list_7.sort()  # Sort the list in place.
print(my_awesome_list_7)  # [1, 2, 3, 4]
my_awesome_list_7.sort(reverse=True)  # Sort the list in place in descending order
print(my_awesome_list_7)  # [4, 3, 2, 1]
my_awesome_list_7.sort(key=lambda x: x % 2)  # Sort the list in place by the remainder of the division by 2.


##################
# reverse a list #
##################

# suporrt string and integer together
# just reverse the list in place and does not sort the list

my_awesome_list_8 = [4, 1, 3, 2]
my_awesome_list_8.reverse()  # Reverse the list in place.
print(my_awesome_list_8)  # [2, 3, 1, 4]

my_awesome_list_9 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_9.reverse()  # Reverse the list in place.
print(my_awesome_list_9)  # [True, 1.5, 2, 1, 'one', 'two', 'one']


###################
# Clear all items #
###################

my_awesome_list_10 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_10.clear()  # Remove all items from the list.
print(my_awesome_list_10)  # []


##################
# Copy all items #
##################

my_awesome_list_11 = ["one", "two", "one", 1, 2, 1.5, True]
my_awesome_list_12 = my_awesome_list_11.copy()  # Copy the list.
print(f"main {my_awesome_list_11}")  # ['one', 'two', 'one', 1, 2, 1.5, True]
print(f"copied {my_awesome_list_12}")  # ['one', 'two', 'one', 1, 2, 1.5, True]

my_awesome_list_11.append(5)

print(f"main {my_awesome_list_11}") 
print(f"copied {my_awesome_list_12}")  # will not append the 5 value



#########
# Count #
#########
my_awesome_list_13 = ["one", "two", "one", 1, 2, 1.5, True]
print(my_awesome_list_13.count("one"))  # 2 - How many one
 
 
#########
# pop   #
#########
my_awesome_list_14 = ["one", "two", "one", 1, 2, 1.5, True]
print(my_awesome_list_14.pop(1))  # two - Remove the item at the given position in the list and return it.
print(my_awesome_list_14)  # ['one', 'two', 'one', 1, 2, 1.5]