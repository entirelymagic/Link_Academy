locale = {
    "ro": "Salutare",
    "en": "Hello",
    "de": "Hallo",
    "it": "Ciao",
    "sp": "Hola"
}
# Your code here

while True:
    user_input = input(f"Choose a value to grit from : {[k for k in locale.keys()]} ")
    if user_input in locale:
        print(locale[user_input])
    elif user_input == 'q':
        break
    else:
        'Pick a valid option'
