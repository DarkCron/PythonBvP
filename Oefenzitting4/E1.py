def numsum (n):
    sum = 0
    for ctr in range(0,n+1):
        sum+=ctr

    return sum

total = int(input("Please give n: "))

print(numsum(total))