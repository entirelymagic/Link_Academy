logins = {
    "2.12": [{"username": "james", "time": "20:18"}, {"username": "john", "time": "23:59"},
             {"username": "robert", "time": "11:08"}],
    "3.12": [{"username": "michael", "time": "14:40"}, {"username": "william", "time": "01:30"}],
    "4.12": [{"username": "david", "time": "10:28"}, {"username": "james", "time": "20:00"},
             {"username": "joseph", "time": "21:17"}, {"username": "james", "time": "22:22"}],
    "5.12": [{"username": "james", "time": "20:18"}],
    "6.12": [{"username": "william", "time": "16:08"}, {"username": "john", "time": "05:45"}],
    "7.12": [{"username": "david", "time": "08:00"}, {"username": "david", "time": "11:02"},
             {"username": "robert", "time": "17:11"}],
    "8.12": [{"username": "joseph", "time": "10:23"}, {"username": "richard", "time": "15:28"},
             {"username": "michael", "time": "21:01"}, {"username": "john", "time": "07:51"}],
}

# Your code here
stats = {}
for i in logins:
    day = logins[i]
    for login_instance in range(len(day)):
        login = day[login_instance]
        name = login['username']
        if name in stats:
            stats[name] += 1
        else:
            stats[name] = 1

print(stats)

