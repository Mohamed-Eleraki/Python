email = "mohamed-ibrahim2021@outlook.com"
# we wanna to take the user name dynamically

print(" ")
print(email[0:email.index("@")])
print(" ")
print(email[email.index("@"):])  # the domain  - @outlook.com
print(email[email.index("@") + 1 :])  # the domain without @  - outlook.com