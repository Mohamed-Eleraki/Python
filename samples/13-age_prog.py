# input Age
age = int(input('What\'s your age? ').strip())

print(" ")
print(age)

# Calculation
months   = age * 12
weeks    = months * 4
days     = age * 365
hours    = days * 24
minutes  = hours * 60
secounds = minutes * 60

print(" ")
print("You Lived for: ")
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{secounds:,} Secounds.")