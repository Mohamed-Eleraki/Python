def say_hello(name, age):
    
    if type(age) != int:
        print("Only integer allowed")
    else:
        print(f"Hello {name} with age: {int(age)}")
    
    
    
say_hello("eraki", "30") 