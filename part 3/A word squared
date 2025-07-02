def squared(string, integer):
    row = 0
    while row < integer:
        column = 0
        while column < integer:
            index = (row * integer + column) % len(string) # Total characters printed so far + position in row, wrap with % to loop through string 
            print(string[index], end="")
            column += 1
        print()
        row+=1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
