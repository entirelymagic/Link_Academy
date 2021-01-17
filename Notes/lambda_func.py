"""lambda  returneaza tot o functie"""

def f(x):
    x % 2


y = filter(lambda x: x % 2, [1, 2, 3, 4, 5])

print(y)
