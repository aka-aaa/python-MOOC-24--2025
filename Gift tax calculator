value = int(input("Value of gift:"))
if value <= 1000000:
    tax = (22100 + (value - 200000)*0.15)
    if value < 200000:
        tax = (4700 + (value - 55000)*0.12)
        if value < 55000:
            tax = (1700 + (value - 25000)*0.1)
            if value < 25000:
                tax = (100 + (value - 5000)*0.08)
                if value < 5000:
                    print("No tax!")
else:
    tax = (142100 + (value - 1000000)*0.17)
if value>5000:
    print(f"Amount of tax: {tax} euros")
