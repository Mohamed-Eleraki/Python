# https://www.youtube.com/watch?v=-PfCcZ2Q_MI&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=69

# all()
x = [1, 2, 3]
if all():
    print("all elements are equal true")

x = [1, 2, 3, []]
if all():
    print("all elements are equal true")
else:
    print('there is one element is false')
    

# any()
x = [1, 2, 3]
if any():
    print('there is one element is false')
    
    
# bin()
# return the binary number
print(bin(1)) # what is the 1 equal in binary system
print(bin(100))  # ignore the 0b

# id()
# get the variable id in memeory

a = 1
print(id(a))


# print()
print('Hello','Mohamed', sep='@')  # Hello@Mohamed

print('first line', end=';')
print('secound line')  # first line; secound line



# map()
# https://www.youtube.com/watch?v=JvbLI0z8t8c&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=72
def text_formate(text):
    return f"- {text} -"

my_text = ["Mohamed", "erki"]

my_formated_data = text_formate(my_text)
print(my_formated_data)  # - ['Mohamed', 'erki'] -

my_formated_data_map = map(text_formate, my_text)
for name in my_formated_data_map:
    print(name)
    # - Mohamed -
    # - eraki -
    
    
    
# filter()
def check_numbers(number):
    if number < 10:
        return number

my_numbers = [1, 2, 3, 10, 12, 122]

result = filter(check_numbers, my_numbers)
for num in result:
    print(num)
    # 1
    # 2
    # 3
    
# help()
# if there is a func you don't understand use help

print(help(print))