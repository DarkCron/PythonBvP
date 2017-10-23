def FibonNum (n):

    if(n==0):
        return 1
    elif(n==1):
        return 1

    return FibonNum(n-2) + FibonNum(n-1)

total = int(input("Please give n: "))

print(FibonNum(total))