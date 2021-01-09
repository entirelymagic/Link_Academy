def f(a, *args, **kw):
    print(kw["msg"],(a * (args[0] + args[1] + args[2])))

f(2,1,2,3,msg="The result is: ")
