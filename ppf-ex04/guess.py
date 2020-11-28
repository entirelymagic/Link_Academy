from random import randint

while True:
    user_input = int(input("Enter your number from 1-10: "))
    pc_number = randint(1,10)
    hit = user_input == pc_number

    print(f"Your number: {user_input}")
    print(f"PC number: {pc_number}")
    print(f"Hit: {hit}")