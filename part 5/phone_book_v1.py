def phone_book():
    phone_number = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit):")
        if command == "1":
            name = input("name: ")
            if name in phone_number:
                print(phone_number[name])
            else:
                print("no number")
        elif command == "2":
            # create dict (name, number)
            name = input("name: ")
            number = input("number: ")
            phone_number[name] = number
            print("ok!")
        elif command == "3":
            print("quitting...") 
            break
phone_book()
