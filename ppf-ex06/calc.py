total = 0

while True:
    userInput = input("Enter number: ")
    if userInput == "":
        print("Total result:", total)
    else:
        if userInput.isnumeric():
            total += int(userInput)
        else:
            print("Value is not numeric")
