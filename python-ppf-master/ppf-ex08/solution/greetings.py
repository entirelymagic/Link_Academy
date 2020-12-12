locale = {
    "ro": "Salutare",
    "en": "Hello",
    "de": "Hallo",
    "it": "Ciao",
    "sp": "Hola"
}
# Your code here
lang = input("Choose language (" + ",".join(locale.keys()) + "): ")
print(locale[lang] if lang in locale else "Language not supported")