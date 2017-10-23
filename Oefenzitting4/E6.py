def Factorial(n):
    fac = 1
    if n == 0:
        return 1
    for nFac in range(1,n+1):
        fac *= nFac

    return fac


def PSet (n,k):
    num = 0
    num = Factorial(n)//Factorial(n-k)
    return num

def CSet (n,k):
    num = 0
    num = PSet(n,k)//PSet(k,k)
    return num

n = int(input("N? "))
k = int(input("K? "))
print(CSet(n,k))