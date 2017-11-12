# Use  the  function  above  to  write  a  function  that  prints  all  prime  numbers  up  to  a
# given number.  Your function should print 2
# ,
# 3
# ,
# 5
# ,
# 7
# ,
# 11
# ,
# 13 when it is called by 15

def isPrime(num):
    if(num == 2):
        return True

    for div in range(2,num//2+1):
        if(num%div==0.0):
            return  False

    return True

def printPrimes(end):
    sumString = ""

    for num in range(2,end+1):
        if isPrime(num):
            sumString+=str(num)
            sumString+=","


    return sumString;

prime = int(input("Prime? "))
print(printPrimes(prime))