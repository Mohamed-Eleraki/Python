def show_skills(name, *skills_without_progress, **skills_with_progress):
    print(f"Hello {name} \nSkills without progress are: ")
    
    for skill in skills_without_progress:
        print(f"- {skill}")
    
    print(" ")    
    print(f"{name}, and skills with progress are: ")
    
    for skill_key, skill_value in skills_with_progress.items():
        print(f"- {skill_key} => {skill_value}")
        
show_skills("eraki", "Ansible", "Azure", Python="40%", AWS="70%")

# without passing other param values
print("#" * 50)
show_skills("eraki")

# The output
# Hello eraki 
# Skills without progress are: 
# - Ansible
# - Azure
 
# eraki, and skills with progress are: 
# - Python => 40%
# - AWS => 70%
# ##################################################
# Hello eraki 
# Skills without progress are: 
 
# eraki, and skills with progress are: 