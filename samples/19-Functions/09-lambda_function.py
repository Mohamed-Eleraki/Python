# https://www.youtube.com/watch?v=oNp5wwu9S7c&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=64
# lambda = Anonymous function
# Dosen't have a name, so we must set in a variable

hello = lambda name: f"Hello {name}"

print(" ")
print(hello("eraki"))
print(hello.__name__) # get func name

# with multiple params
hello2 = lambda name, age: f"Hello {name} with age: {age}"

print(" ")
print(hello2("eraki", 30))
print(hello2.__name__) # get func name