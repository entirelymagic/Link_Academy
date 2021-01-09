def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    
    return res

while True:
    n = int(input("Enter number: "))
    print(factorial(n))