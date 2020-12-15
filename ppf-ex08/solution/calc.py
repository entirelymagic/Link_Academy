dct = {
    "en":{ 
        "n1":"Enter first number: ",
        "n2":"Enter second number: ",
        "res":"Result is: ",
    },
    "ro":{ 
        "n1":"Introdu primul numar: ",
        "n2":"Introdu al doilea numar: ",
        "res":"Rezultatul este: "
    }
} 

while True:
    lang = input("Enter language (" + ",".join(dct.keys()) + "): ")
    if lang not in dct:
        print("Invalid language")
        continue
    else:
        break

loc = dct[lang]

n1 = int(input(loc["n1"]+": ")) 
n2 = int(input(loc["n2"]+": "))
print(loc["res"]+": ",n1+n2)

