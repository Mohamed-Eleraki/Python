import os 

print(os.getcwd())  # get current dir

my_file = open("test.txt", "a")
my_file.write("data")
#my_file.close()  # hash this before use tell() method

# get the position of cursor
print(my_file.tell())
# the new line in windows considered as 2 move

# close the file before using seek() method
#my_file.close()

# change the cusor position
# must use seek() with read permissions
my_file = open('test.txt', "r")
my_file.seek(20)  # change the cursor to 6

print(my_file.read())  # print the file content


