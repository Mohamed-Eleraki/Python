####################
## String Methods ##
####################

#########
# Strip #
#########

## strip()  remove all spaces
## lstrip() remove left spaces
## rstrip() remove right spaces

x = "     I love python       "
print (x.strip())
print(x.rstrip())
print(x.lstrip())
print(len(x.strip()))  # the lenth of stripped charts

y = "#######I love python######"
print(y.strip("#"))  # remove all "#" from the string
print(y.lstrip("#"))  # remove left "#" from the string
print(y.rstrip("#"))  # remove right "#" from the string

a = "@#@#I love python@#@#"
print(a.strip("@#"))  # remove multiple characters from the string
print(a.rstrip("@#"))
print(a.lstrip("@#"))



#########
# Title #
#########

# Will make your string as a tile, Start with cap letter, and char after num as well

s = "i love python, and 3d graphics"
print(s.title())  # I Love Python, And 3D Graphics


##############
# capitalize #
##############

# Will make each start of the word as a cap letter

s = "i love python, and 3d graphics"
print(s.capitalize())  # I love python, and 3d graphics



#########
# UPPER #
#########

# Will make each start of the word as a cap letter

s = "i love python, and 3d graphics"
print(s.upper())  # lower as well


############
# swapcase #
############

# convert from cap to lower and vice versa

s = "i love python"
x = "I LOVE PYTHON"

print(s.swapcase())
print(x.swapcase())


#########
# zfill #
#########

a, b, c = "1", "22", "33"
print(a)
print(b)
print(c)

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))
# 001
# 022
# 033


#########
# split #
#########

# will split your string into list based on space

s = "hello world"
print(s.split())  # ['hello', 'world']
print(type(s.split()))

s = "Hello|world|will|not|split"
print(s.split("|"))  # ['Hello', 'world']
print(s.split("|", 2))  # will split the first 2 elements  ['Hello', 'world', 'will|not|split']
print(s.rsplit("|", 2))
print(s.split("|", -2))



##########
# center #
##########

n = "eraki"
print(n.center(9))  # spaces
print(n.center(9, "#"))  # hashes
#   eraki  
##eraki##


#########
# rjust #
#########

n = "eraki"
print(n.rjust(9))  # spaces
print(n.rjust(9, "#"))  # hashes
#   eraki  
##eraki

print(n.ljust(9))  # spaces
print(n.ljust(9, "#"))  # hashes
#eraki   
# eraki##


##########
# count #
##########

# count/search a specific word - count how many times it appears

x = "my name is eraki, another eraki"
print(x.count("eraki"))  # 2
print(x.count("eraki", 0, 20))  # 1   - define from and to


##############
# startswith #
##############


x = "my name is eraki"
print(x.startswith("my"))  # True

print(x.startswith("my", 0, 10))  # True   -   from to 

print(x.endswith("i")) # True  -  end with i


#########
# index #
#########

# find the index of the word
### index has an issue, that if index not exist will throw an error and stop executing ###

x = "my name is eraki"
print(x.index("er"))  # index number 11 - you can define from and to as well


#########
# find #
#########

# find the find of the word
### find instead will print out -1 if the search value does not exist ###

x = "my name is eraki"
print(x.find("er"))  # find number 11 - you can define from and to as well


##############
# splitlines #
##############

# gather back the multi lines string into a list

e = """First line
Secound line
third line"""  # multiple lines output

print(e.splitlines())  # ['First line', 'Secound line', 'third line']

f = """First line\nSecound line\nthird line"""  # multiple lines output

print(f.splitlines())  # ['First line', 'Secound line', 'third line']



##############
# expandtabs #
##############

# controle the tab spaces number

x = "I\tlove\tpython"
print(x)
print(x.expandtabs(2))  # I love python  - replace 4 spaces with just 2



######################
# Checking - boolean #
######################

x = "I Love Python"
print(x.istitle())  # True
print(x.isupper())  # False

x = " "
print(x.isspace())  # True


one = "mohamed"  # string can be a variable name
two = "mohamed--eleraki"  # string cannot be as a variable name
three = "mohamed1234"


print(one.isidentifier())  # True
print(two.isidentifier())  # False

print(one.isalpha())  # True - lpha bit charts
print(three.isalnum())  # True - alpha and numbers




###########
# Replace #
###########

x = "one two three one one"
print(x.replace("one", "1"))  # replace one to 1
print(x.replace("one", "1", 1))  # replace first one to 1
# 1 two three 1 1
# 1 two three one one



########
# join #
########

# revert a list to string

x = ["one", "two", "three"]
print(" ".join(x))  # one two three with space seperator
print("-".join(x))  # one-two-three with - seperator