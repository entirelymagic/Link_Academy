from time import time


# Higher Order Functions:


def greet(func):
    """Higher Order Functions - because it is as a parameter another function"""
    func()


def greet2():
    """Higher Order Functions - because it is returning a function"""

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


@star_super_booster
def hello(name, emoji=':)'):
    """A function that prints hello!"""
    print(f'Hello {name}! {emoji}')


hello('Elvis', ':D')
hello('Alexandra')


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        value = func(*args, **kwargs)
        t2 = time()
        print(f'Function "{func.__name__}" took {t2 - t1} seconds to execute.')
        return value

    return wrapper


@performance
def long_time():
    total = 0
    for i in range(10000000):
        total += i * 5
    return total


z = 'Hello'
z.replace('l', 'p', count=1)
print(f'this is z= {z}')
x = 1
y = 2

if x > y:
    x + y
