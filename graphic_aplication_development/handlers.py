import random
from random import random as rd


def random_float():
    for _ in range(10):
        value = rd() + random.randint(0, 1)
        return value
