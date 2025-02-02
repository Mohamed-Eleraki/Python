import os

print(os.getcwd())  # get current working directory 
# that the python search for the next command
file = open("README.md")

print(os.path.abspath(__file__))  # return the absoulte path of the current file, __file__ refers to the current file.
print(os.path.dirname(os.path.abspath(__file__))) # print the working directory of the current file.

# Change current working dire
print("#" * 50)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

# ignore any special characters, raw string
file = open(r"C:\Python\nfile.txt")  # will not consider it as a new line