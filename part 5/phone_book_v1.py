"""
This program allows the user to:
1 = Search for a phone number by name.
2 = Add a new contact or update an existing one. If a contact already exists, the new number will replace the old one.
3 = Quit the application
"""
def phone_book():
    # Dictionary to store phone numbers: key = name, value = number
    phone_number = {}
    while True:
        # Ask the user what they want to do
        command = input("command (1 search, 2 add, 3 quit):")
        if command == "1":
            name = input("name: ")
            # Search for a number
            if name in phone_number:
                print(phone_number[name])
            else:
                print("no number")
        elif command == "2":
            # Add or update a contact
            name = input("name: ")
            number = input("number: ")
            phone_number[name] = number
            print("ok!")
        elif command == "3
            # Quit the program
            print("quitting...") 
            break
# Run the program
phone_book()
