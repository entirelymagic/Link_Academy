def mydecorator(f):
    print("din decorator")
    def rewrited(*args,**kw):
        return ("Result is " + str(f(*args)))
    return rewrited


@mydecorator
def myfunc(a,b):
        return a+b

print(myfunc(2,3))
