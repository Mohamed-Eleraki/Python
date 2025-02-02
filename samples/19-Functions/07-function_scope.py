x = 1  # Global scope

# What happens in function stay in function ;)
def one():
    x = 2
    print(f"Print from function scope {x}")
    
def two():
    print(f"Print from function two global scope {x}")
    
def three():
    global x  # fetch value from global
    x = 5  # adjust the global value
    print(f"Print from functoin Three Global scope {x}")
    
    
print(f"Print from Global scope {x}")
one()
two()
three()
print(f"print after global scopt adjusted: {x}")