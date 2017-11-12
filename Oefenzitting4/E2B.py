def FibonNum (n):
    if(n==1):
        return 1


    fibonMinus1 = 1
    fibonMinus2 = 1
    highestFibon = 2

    counter = 1

    while n > highestFibon:
        highestFibon = fibonMinus1+fibonMinus2
        fibonMinus2 = fibonMinus1
        fibonMinus1 = highestFibon
        counter+=1

    if(n==highestFibon):
        return counter
    else:
        return -1



total = int(input("Please give fibon num: "))

print(FibonNum(total))