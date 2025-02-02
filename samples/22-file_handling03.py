import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

file = open("test.txt", "w")
print(file.tell())  # get the current position of cursur in the file, from where to start type in the file

# adjsut the cursur position with seek
file.seek(0) # retrun back to 0
#print(file.read())

file.close()
file.remove("test.txt")