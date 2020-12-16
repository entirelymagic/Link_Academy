def calculateSum(num):
    if num:
        return num + calculateSum(num - 1)
    else:
        return 0


print(calculateSum(55))


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)



print(sum(55))