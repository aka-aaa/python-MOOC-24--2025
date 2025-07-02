number = 0
summ = 0 
words = "The consecutive sum: "
limit = int(input("Limit: "))
while summ < limit:
    number += 1
    summ += number
    if number >=2:
        words += " +"
    words += f" {number}" 
words += f" = {summ}"
print(words)
    
