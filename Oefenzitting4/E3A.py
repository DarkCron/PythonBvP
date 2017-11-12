#
# A  prime  number  is  one  that  is  not  divisible  by  any  number  other  than  one  and  it-
# self.  Write a function to check whether a number is prime or not.  Your function should return
# T rue
# when it is called by 13 and
# F alse
# when it is called by 14.

def isPrime(num):
    if(num == 2):
        return True

    for div in range(2,num//2+1):
        if(num%div==0.0):
            return  False

    return True

prime = int(input("Prime? "))
print(isPrime(prime))