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


#########
# swapcase #
#########

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




##########
# center #
##########

n = "eraki"
print(n.center(9))  # spaces
print(n.center(9, "#"))  # hashes
#   eraki  
##eraki##




##########
# count #
##########
# count/search a specific word
x = "my name is eraki, another eraki"
print(x.count("eraki"))  # 2
print(x.count("eraki", 0, 20))  # 1   - define from and to


##############
# startswith #
##############


x = "my name is eraki"
print(x.startswith("my"))  # True

print(x.startswith("my", 0, 10))  # True   -   from to 

print(x.endswith("i")) # True