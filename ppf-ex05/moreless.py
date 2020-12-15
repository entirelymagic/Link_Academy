def moreless():
    number: int = int(input("Enter your number: "))
    if number > 0:
        print("Your number is positive!")
    elif number < 0:
        print("Your number is negative")
    else:
        print("Your number is 0")


moreless()
