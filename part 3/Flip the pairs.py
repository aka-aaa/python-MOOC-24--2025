number = int(input("Please type in a number:"))  # Get a number from the user
i = 2  # Initialize counter for even numbers, starting from 2
i2 = 1  # Initialize counter for odd numbers, starting from 1
while i  <= number or i2 <= number: # Loop continues as long as either i (even) or i2 (odd) is less than or equal to the input number
    if i <= number: # Check if current even number is within the limit
        print(i) # Print the even number
        i+=2 # Move to the next even number (increment by 2)
    if i2 <= number: # Check if current odd number is within the limit
        print(i2) # Print the odd number
        i2+=2 # Move to the next odd number (increment by 2)
