# Write a function that computes the factorial of a positive integer.; n ! = 1 ∗ 2 ∗ 3 ∗ . . . ∗ n.

def Factorial(n):
    fac = 1
    if n == 0:
        return 1
    for nFac in range(1,n+1):
        fac *= nFac

    return fac

n = int(input("Fac: "))
print(Factorial(n))