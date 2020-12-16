"https://github.com/cosmin91ro/python-ppf"

from typing import Any


def greet(*string: str):
    """Functie ce ia un paramentru pozitional -"""
    return string


a = greet("Salut", "Cristi")

print(a)

x, y, z = greet("Elvis", "Cosmin", "Florin")

print(x, y, z)


def f(*args):
    """The function takes a list as an parameter and return the values within it if passed as arguments"""
    print(args[0] + args[1])


def g(**kwargs):
    """"""
    print(kwargs["firstname"])

