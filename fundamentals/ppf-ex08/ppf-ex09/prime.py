def isPrime(n):
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return False
    
    return True


while True:
    n = int(input("Enter number to check: "))
    print("Number " + ("is" if isPrime(n) else "is not") + " prime") 