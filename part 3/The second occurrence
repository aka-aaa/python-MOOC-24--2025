string = input(str("Please type in a string: "))            #get input string
substring = input(str("Please type in a substring: "))  #get input substring
first_occurence = string.find(substring)       #find index of first occurence
if first_occurence != -1:                      #check if a first_occurence was found
    second_string = string[first_occurence + len(substring):] # slice the string after the first_occurence to avoid overlapping
    second_occurence = second_string.find(substring)          #find the second occurrence in the sliced string
    if second_occurence != -1:                                #check if the second occurrence was found
        index = first_occurence + len(substring) + second_occurence #calculate the index of the second occurrence relative to the original string
        print(f"The second occurrence of the substring is at index {index}.") #second occurrence found
    else:
        print("The substring does not occur twice in the string.") #no second occurrence found
else:
    print("The substring does not occur twice in the string.") #no second occurrence found
