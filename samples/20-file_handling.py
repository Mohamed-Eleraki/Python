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
#file = open(r"C:\Python\nfile.txt")  # will not consider it as a new line

# Print object data
file = open("20-file_handling.py", "r")  # open the file with read access
print(file)  # <_io.TextIOWrapper name='20-file_handling.py' mode='r' encoding='UTF-8'>
print(file.name)
print(file.encoding)

# Reset file pointer to the beginning if any read operation was done earlier
# avoiding any issues while using multiple reads
file.seek(0)

# # get the file content
# print(" ")
# print("#" * 50)
# print(file.read())  # print all the file content
# print(file.read(5))  # print 5 charts of the file content
# print("#" * 50)
# print(" ")

# # get specific lines char content 
# ## will not work if you use read before it
# print(" ")
# print("get specific lines char content")
# print("#" * 50)
# print(file.readline(5))  # print first 5 char of line 5 content
# print(file.readline(10))  
# print(file.readline(20))  
# print("#" * 50)
# print(" ")

# # get specific lines content 
# ## will not work if you use read before it
# print(" ")
# print("get specific lines content")
# print("#" * 50)
# print(file.readlines(5))  # print line num 5 content
# print(file.readlines(10))  
# print(file.readlines(20))  
# print("#" * 50)
# print(" ")


# # loop on all line of the file
# ## to use this must hash all the read* funcs above
# for line in file:
#     print(line, end="")  # end for avoid double new lines
    
#     if line.startswith("07"):  # print only till line number 07, it's not working proparly
#         break
    
    

# loop on all line of the file with fetching the line number
## to use this must hash all the read* funcs above
for line_number, line in enumerate(file, start=1):
    print(f"Line {line_number}: {line}", end="")
    
    if line.startswith("Line 7"):  # print only till line number 07, it's not working proparly
        break
# close the file
file.close()