def digitSum(pCode):
    sum = 0
    CODELENGTH = 5
    for n in range(0,CODELENGTH):
        sum+=digitNum(pCode,n)
    return sum

#Starting from 0 left to right
def digitNum(pCode,n):
    dn = 0
    CODELENGTH = 5
    mod = 1
    rem = 10

    for amp in range(n,CODELENGTH-1):
        mod*=10
        rem*=10

    pCode = pCode % rem

    dn = pCode // mod

    return dn

def getCheckDigit(sum):
    if sum % 10 == 0.0:
        return 0

    for n in range(0,10):
        if (sum + n)%10 == 0:
            return n


    return 0

code = int(input("Code: "))
print(getCheckDigit(digitSum(code)))