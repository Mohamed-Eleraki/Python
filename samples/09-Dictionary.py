# dic items in curly braces {}
# dic items are key:value pair
# dic is mutable and can be changed
# dic is unordered and not indexed
# dic keys are unique, not duplicated - if duplicated the last value will be taken
# dic values are not unique, can be duplicated - if duplicated the last value will be taken



user = {
    "name": "eraki",
    "age": 30,
    "is_active": True,
    
    "Skills": ["Python", "Django", "Flask"],
    
    "address": {
        "city": "Cairo",
        "country": "Egypt"
    }
}

print(user)
print(user["name"])
print(user["name"], user["age"])

print(user.get("name"))  # the same as user["name"]

print(user.keys())
print(user.values())

print("######")
print(user.items()) # return as a list of tuples

print("Print sub dictionary")
print(user["address"])
print(f"The user city is: {user["address"] ["city"]}")
print(f"The user Country is: {user["address"] ["country"]}")

# print as a JSON format
import json
print(json.dumps(user, indent=2))  # indent=2 to make it more readable

# print as a JSON format for the address only
print("#Print address only#")
print(json.dumps(user["address"], indent=2))  # indent=2 to make it more readable
print(json.dumps(user["address"], indent=2, sort_keys=True))  # indent=2 to make it more readable
print(json.dumps(user["address"] ["city"], indent=2, sort_keys=True))  # indent=2 to make it more readable


# extend the dictionary with another dictionary
frameworks_1 = {
    "React": "Frontend",
    "Django": "Backend"
}
frameworks_2 = {
    "Angular": "Frontend",
    "Flask": "Backend"
}

frameworks_1.update(frameworks_2)
print(frameworks_1)  # if the key is duplicated the last value will be taken

# Another way to extend
all_frameworks = {
    "one": frameworks_1,
    "two": frameworks_2
}
print("#All Frameworks#")
print(all_frameworks)
print(json.dumps(all_frameworks, indent=2))  # indent=2 to make it more readable

# clear the dictionary
frameworks_1.clear()
print(frameworks_1)  # {}


# update the dictionary
frameworks_1.update(frameworks_2)

# remove an item from the dictionary

frameworks_1.pop("Angular")
print(frameworks_1)  # {'Flask': 'Backend'}

# remove the last item from the dictionary
frameworks_1.popitem()  # also you can use popitem() for printing the last added item
print(frameworks_1)  # {}


# copy the dictionary
frameworks_1 = frameworks_2.copy() # take a copy of frameworks_2 and assign it to frameworks_1
print(frameworks_1)  # {'Angular': 'Frontend', 'Flask': 'Backend'}

# setdefault
# if the key is not exist it will add it with the value
# if the key is exist it will not change the value

dic_1 = {
    "one": 1,
    "two": 2
}
print("#" * 10) 
print(dic_1.setdefault("three", 3))  # 3
print(dic_1.setdefault("one", 1))  # 1
print(dic_1)  # {'one': 1, 'two': 2, 'three': 3}


# fromkeys
# create a dictionary from a list of keys
a = ("one", "two", "three")
b = 0
print("#" * 10)
dic_2 = dict.fromkeys(a, b)
print(dic_2)  # {'one': 0, 'two': 0, 'three': 0}