import math

bContinue = True

while bContinue:
    floatInput = float(input("Please enter a floating point value: "))
    bIsPositive = floatInput > 0
    bIsLarge = math.fabs(floatInput) > 1000000
    bIsSmall = math.fabs(floatInput) < 1

    if floatInput == 0:
        bContinue = False
        print("This number is zero.")
        break

    adjectiveSize = ""
    if bIsLarge:
        adjectiveSize = "large "
    elif bIsSmall:
        adjectiveSize = "small "

    adjectiveSign = "postive "
    if not bIsPositive:
        adjectiveSign = "negative "

    print("This number is a "+adjectiveSize+" "+adjectiveSign+"number.")