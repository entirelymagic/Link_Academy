import json


def authenticate(user, password):
    """Authentication method, given a username and a password, will check in the current list for a match"""
    with open("users.json") as file:
        users = json.loads(file.read())
    for u in users:
        if u["username"] == user and u["password"] == password:
            return True
    return False

