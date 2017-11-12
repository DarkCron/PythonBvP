from Oefenzitting4.E2A import FibonNum

def FibonRange(n1,n2):
    sum = 0
    for num in range(n1,n2+1):
        sum += FibonNum(num)

    return sum

n1 = int(input("N1: "))
n2 = int(input("N2: "))
print(FibonRange(n1,n2))