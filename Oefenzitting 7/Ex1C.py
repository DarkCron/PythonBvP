factors = set()
def FirstPrime(x):
    if x == 1:
        return 1

def IsPrime(x):
    for i in range(2,x//2+2):
        if x % i == 0:
            return False
    return True

def Factors(n):
    if n == 1:
        return
    if n%2 == 0:
        factors.add(2)
        return Factors(n//2)
    if IsPrime(n):
        factors.add(n)
        return
    for i in range(2,n):
        if IsPrime(i) and n%i == 0:
            factors.add(i)
            return Factors(n // i)



Factors(9699690)
print(factors)