import os

print(os.getcwd())
file = open("21-file_handling02_TEST.py", "w")  # with write more, if not exit will create it
# print(file.read())  # hash it avoiding issues while write
file.write("""import os
print(os.getcwd())
file = open("21-file_handling02_TEST.py", "w")
print(file.name)
file.close()
           """)
file.close()

file02 = open("21-filenadling02_TEST02", "w")
my_list = ["Mohamed\n", "eraki\n", "Ahmed"]
file02.writelines(my_list)


# with append
file02 = open("21-filenadling02_TEST02", "a")
my_list = ["Mohamed\n", "eraki\n", "Ahmed"]
file02.writelines(my_list)

file02.close()