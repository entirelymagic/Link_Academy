blacklist = ["peter", "john", "sally"]
users = []
# Your code here

while True:
    userName = input("Enter your user name: ")
    if userName not in blacklist:
        users.append(userName)
        # print("User added to the user list.")
        # print(users)
    else:
        print("Sorry, you cannot enter.")
    print(users)

