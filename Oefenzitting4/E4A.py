# A perfect number is one that is equal to the sum of its divisors excluding the num-
# ber itself.  The first perfect number is 6 because 1 + 2 + 3 = 6.  Write a function that checks a
# number is perfect or not.

def isDivisor(div,num):
    if(num%div == 0.0):
        return True
    return False

def isPerfectNum(num):
    sum = 0
    for div in range(1,num//2+1):
        if isDivisor(div,num):
            sum+=div

    if sum == num:
        return True
    else:
        return False

#E4B
def PerfectNumberFinder(amount,start = 0):
    currentAmount=0
    currentNum = start + 1
    foundString = ""

    while currentAmount < amount:
        if isPerfectNum(currentNum):
            foundString += str(currentNum)+","
            currentAmount+=1
        currentNum+=1

    return foundString

num = int(input("Is perfect? "))
print(isPerfectNum(num))
num = int(input("How many new perfect numbers? "))
start = int(input("Where to start from? "))
print(PerfectNumberFinder(num,start))