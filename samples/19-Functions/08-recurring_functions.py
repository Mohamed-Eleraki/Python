# Resource: https://www.youtube.com/watch?v=zFVdMyr6CIo&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=63

def cleanword(word):
    
    if len(word) == 1:  # forget about this, just print the word if have only one character
        return word  
    
    if word[0] == word[1]:  #wwwooorrrddd
        return cleanword(word[1:])
        # if condition, if the first and the secound char 
        # similar will remove the first one

 
    
    return word[0] + cleanword(word[1:])
    # Here will retrun the rirst item and store it then start from the beginneing
    # Stash [ word ]
    
print(cleanword("wwwooorrrddd"))