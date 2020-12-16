def f():
    print("Hello")
    yield
    print("World")
    yield

x = f()
next(x)
next(x)