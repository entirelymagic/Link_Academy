def isPerfect(x):
    sum = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0: sum += i

    return x == sum


def perfects(n):
    i = 0
    c = 0
    while c < n:
        i += 1
        if isPerfect(i):
            c += 1
            yield i


while True:
    n = int(input("How many perfect numbers you need? "))
    for i in perfects(n):
        print(i)
