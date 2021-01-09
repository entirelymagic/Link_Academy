
def calc(a, b, op):
    if op == "add":
        result: float = a + b
        return result
    elif op == "sub":
        result: float = a - b
        return result
    elif op == "mul":
        result: float = a * b
        return result
    elif op == "div":
        result: float = a / b
        return result
    else:
        return 0


running = True

while running:
    user_input1 = input("Enter your first number: ")
    user_input2 = input("Enter your second number: ")
    user_input3 = input("Enter the type of operation(add,sub,mul or div): ")

    print(calc(int(user_input1), int(user_input2), user_input3))



