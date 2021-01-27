import re


only_letters = "([a-zA-Z])+"
name = 'Elvis'
other_name = "drago523s"
x = re.fullmatch(only_letters, name)
y = re.fullmatch(only_letters, other_name)
print(y, x)