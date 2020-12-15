logins = {
    "2.12": [{"username":"james","time":"20:18"},{"username":"john","time":"23:59"},{"username":"robert","time":"11:08"}],
    "3.12": [{"username":"michael","time":"14:40"},{"username":"william","time":"01:30"}],
    "4.12": [{"username":"david","time":"10:28"},{"username":"james","time":"20:00"},{"username":"joseph","time":"21:17"},{"username":"james","time":"22:22"}],
    "5.12": [{"username":"james","time":"20:18"}],
    "6.12": [{"username":"william","time":"16:08"},{"username":"john","time":"05:45"}],
    "7.12": [{"username":"david","time":"08:00"},{"username":"david","time":"11:02"},{"username":"robert","time":"17:11"}],
    "8.12": [{"username":"joseph","time":"10:23"},{"username":"richard","time":"15:28"},{"username":"michael","time":"21:01"},{"username":"john","time":"07:51"}],
}

# Your code here
prevLoggedinUsers = set()
usersLoggedInBefore = False
for date,day_logins in logins.items():
    if date == "6.12":
        users6_12 = set()
        for login in day_logins:
            users6_12.add(login["username"])
        if users6_12.issubset(prevLoggedinUsers):
            usersLoggedInBefore = True
    for login in day_logins:
        prevLoggedinUsers.add(login["username"])

print("Users in 6.12 ", "have" if usersLoggedInBefore else "have not", "used the app before")
