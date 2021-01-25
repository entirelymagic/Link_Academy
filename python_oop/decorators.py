from time import time


# Higher Order Functions:
def greet(func):
    """Higher Order Functions - a function is parameter for another function"""
    func()


def greet2():
    """Higher Order Functions -return a function"""
    def func():
        return 5
    return func


def star_super_booster(func):
    """A decorator that prints stars before and after a function execution"""
    def wrapper(*args, **kwargs):
        print('*' * 20)
        func(*args, **kwargs)
        print('*' * 20)
    return wrapper


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        value = func(*args, **kwargs)
        t2 = time()
        print(f'Function "{func.__name__}" took {t2 - t1} seconds to execute.')
        return value
    return wrapper





