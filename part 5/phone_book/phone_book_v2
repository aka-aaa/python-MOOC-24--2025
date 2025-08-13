def phone_book():
    phone_number = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit):")
        if command == "1":
            name = input("name: ")
            if name in phone_number:
                for number in phone_number[name]:
                    print(number)
            else:
                print("no number")
        elif command == "2":
            name = input("name: ")
            number = input("number: ")
            if name not in phone_number:
                phone_number[name] = []
            phone_number[name].append(number)

            print("ok!")
        elif command == "3":
            print("quitting...") 
            break
phone_book()
