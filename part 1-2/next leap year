year = int(input("Year:"))
ly = year
while True:
    ly += 1 
    if ly%4==0:
        if ly%100==0 and ly%400!=0:
            success = False
        else:
            success = True
    else:
        success = False
    if success:
        break
print(f"The next leap year after {year} is {ly}")
