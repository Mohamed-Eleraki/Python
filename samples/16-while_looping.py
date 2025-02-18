a = 0

# example 1
while a < 10:
    print(a) # will not end
    

# example 2
while a < 10:
    print(a)
    a += 1 # a = a + 1  | will repeat for 10
    
# example 3
while a < 15:
    print(a)
    a += 1
else:
    print("loop end")
    
# example 4
while False:
    print("will not print any thing")