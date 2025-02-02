# Here instead of pass to a tuple using * before the parameter
# will use dictionary using double **

def show_skills(**skills):
    print(f"###{skills.items()}")
    for skill, value in skills.items():
        print(f"{skill} => {value}")
        
print(" ")
print("## passing the key=value ##")        
show_skills(html="99%", css="40%")

# using a real dic | packing/unpacking dic
dic_skills = {
    "Html": "90%",
    "css": "40%"
}
print(" ")
print("## passing from a dic ##")        
#show_skills(dic_skills)  # Error, Must be unpacking first, required key=value
show_skills(**dic_skills)  # unpacking