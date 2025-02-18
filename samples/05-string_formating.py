# Reference
# https://pyformat.info/
# video num 18


# Data formating is more powerfull than concatenation

name = "eraki"
age = 30
floatvar = 3.5

# The old formating way

print("My name is %s and I am %d years old" % (name, age))  # %s for string, %d for integer

print("My name is %s and I am %d years old and my floatvar is %f" % (name, age, floatvar))  # %s for string, %d for integer, %f for float

print("My name is %s and I am %d years old and my floatvar is %.1f" % (name, age, floatvar))  # Control the number of float decimal points

print("My name is %.1s and I am %d years old and my floatvar is %f" % (name, age, floatvar))  # Control the number of characters

print("My name is " + name + " and I am " + str(age) + " years old")  # convert to str to concatenate




# The new formating way

print("My name is {} and I am {} years old".format(name, age))

print("My name is {} and I am {} years old and my float is {:f}".format(name, age, floatvar))  # and you can use the same formating for string and integer

print("My name is {} and I am {} years old and my float is {:.1f}".format(name, age, floatvar))  # Control the number of float decemal point 

print("My name is {:.1s} and I am {} years old and my float is {:.1f}".format(name, age, floatvar))  # Control the number of strong characters

print("My name is", name, "and I am", age, "years old")


# The new formating way with f-string
print(f"My name is {name} and I am {age} years old")
print(f"My name is {name} and I am {age} years old and my float is {floatvar}")
print(f"My name is {name} and I am {age} years old and my float is {floatvar:.1f}")

# Money formating
money = 1000000
print(f"I have {money:,} money")  # Add comma for thousand separator
print("I have money {:,d}".format(money))  # Add comma for thousand separator


# Rearrange items

a, b, c = 1, 2, 3

print("Hello {} {} {}".format(a, b, c))  # Hello 1 2 3

print("Hello {1} {2} {0}".format(a, b, c)) # Hello 2 3 1
#                                0  1  2

print("Hello {1:d} {2:d} {0:f}".format(a, b, c)) # Hello 2 3 1.000000    - adjust with the type


# the new way and the best
print(f"Hello {a} {b} {c}")  # Hello 1 2 3
