# example 1
a = [1,2,3,4,5]
for item in a:
    print(item)
    
# example 2    
x = range(1, 101)  # form 1 to 100
for item in x:
    print(item)
    
# example 3
skills = {
    "Html": "90%",
    "CSS": "80%",
}

for skill in skills:
    print(f"My progress in lange {skill} is {skills[skill]}")
    print(f"My progress in lange {skill} is {skills.get(skill)}")  # the same
    
    
# example 4
skills = {
    "Html": "90%",
    "CSS": "80%",
}

print(skills.items())  # dict_items([('Html', '90%'), ('CSS', '80%')])

for skill_key, skill_value in skills.items():
    print(f"{skill_key} is {skill_value}")
    #Html is 90%
    #CSS is 80%