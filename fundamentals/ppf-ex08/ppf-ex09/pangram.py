import string

def ispangram(str):
    alphaset = set(string.ascii_lowercase)
    return alphaset.issubset(set(str.lower()))

while True:
    str = input("Enter string to check: ")
    print(ispangram(str)) 