# the dafault param value must be at the end, 
# Or all of them have default values.
def say_hello(name, age, country="Unkown"):
        
    if type(age) != int:
        print("the Age value must be integer")
    else:
        print(f"Hello {name} and your age is {age} and country is {country}")

say_hello("eraki", 30)  # Hello eraki and your age is 30 and country is Unkown
