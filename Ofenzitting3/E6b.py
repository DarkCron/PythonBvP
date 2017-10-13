import math

x = int(input("Please enter an x-value: "))
exValue = 0

for j in range(0, 100):
    n = j
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    exValue += (math.pow(x,n) / factorial)

print(exValue)