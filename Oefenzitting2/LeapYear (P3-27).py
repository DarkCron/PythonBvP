year = int(input("Enter the year you wish to check: "))

bIsLeap = False
bIsDivisableBy4 = year % 4 == 0
bIsDivisableBy100 = year % 100 == 0
bIsDivisableBy400 = year % 400 == 0
bIsYearAfter1582 = year >= 1582

if bIsDivisableBy4:
    if bIsDivisableBy100:
        if bIsDivisableBy400:
            bIsLeap = True
        else:
            bIsLeap = False
    else:
        bIsLeap = False
    bIsLeap = True

if not bIsYearAfter1582:
    bIsLeap = False

if bIsLeap:
    print("%i is a leap year." % year)
else:
    print("%i is not a leap year." % year)