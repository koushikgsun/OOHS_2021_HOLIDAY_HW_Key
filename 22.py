def isPrime(n):
    if (n <= 1):
        return False
    if not (n).is_integer() :
        return False
    for i in range(2, int(n)):
        if (n % i == 0):
            return False
    return True
n = int(input("number : "))
n     = n ** 0.5
if isPrime(n):
    print("true")
else:
    print("false")