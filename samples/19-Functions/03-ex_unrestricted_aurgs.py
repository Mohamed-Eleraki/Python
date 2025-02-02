def say_hello(age, *names): # unrestricted number of names
    for name in names:
        print(f"Hello {name} wiht age: {age}")
        
say_hello(30, "Mohamed", "Salah")
say_hello(30, "Mostafa", "Esam", "Fathy")