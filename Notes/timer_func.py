from math import factorial
import time


def time_to_run(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        total_time = "Total time taken in : ", func.__name__, end - begin
        print(total_time)

    return inner1


@time_to_run
def factorial_func(x):
    res = factorial(x)
    print(res)


factorial_func(10000)

