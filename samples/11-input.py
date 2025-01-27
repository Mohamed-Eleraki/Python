first_name = input('What\'s your first name? ')
m_name = input('What\'s your middle name? ')
l_name = input('What\'s your last name? ')

print(" ")
print(f"First Name: {first_name} \nMiddle Name: {m_name} \nLast Name: {l_name}")

print(" ")
print(f"Hello {l_name},{first_name:.1s}")  # Hello eraki,M

print("")
print(f"Hello {l_name},{first_name.strip().lower():.1s}")  # Hello eraki,m

