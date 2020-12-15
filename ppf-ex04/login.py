db_username = "peter"
db_password = "123"
# Your code here
username_input = input("Enter your username: ")
username_pass = input("enter your password: ")

access_granted = username_input == db_username and username_pass == db_password
print(access_granted)
