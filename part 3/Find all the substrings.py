word = input(str("Please type in a word: "))            #input word
character = input(str("Please type in a character: "))  #input character
while True:                                             # loop
    find = word.find(character)                         #find character in word
    if len(word[find:find+3])>=3 and find != -1:        #substring lenght needs to be >=3
        print(word[find:find+3])                        #print substring
        word = word[find+1:]                            #now finds next substring by changing starting point of search
    else:                                               # if substring less than 3
        break                                           # loop ends
    
