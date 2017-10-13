income = int(input("What was your annual income? "))

FIRST_PART = 50000
SECOND_PART = 75000
THIRD_PART = 100000
FOURTH_PART = 250000
FIFTH_PART = 500000
#SIXT_PART > 500000

taxPercentage = 0.0
incomeRemainder = 0
totalTaxes = 0.0

if income <= FIRST_PART:
    taxPercentage = 0.01
    incomeRemainder == income
elif income <= SECOND_PART:
    taxPercentage = 0.02
    incomeRemainder = (income - FIRST_PART)
    totalTaxes += float(FIRST_PART * .01)
elif income <= THIRD_PART:
    taxPercentage = 0.03
    incomeRemainder = (income -  SECOND_PART)
    totalTaxes += float(FIRST_PART * .01)
    totalTaxes += float((SECOND_PART - FIRST_PART) * .02)
elif income <= FOURTH_PART:
    taxPercentage = 0.04
    incomeRemainder = (income - THIRD_PART)
    totalTaxes += float(FIRST_PART * .01)
    totalTaxes += float((SECOND_PART - FIRST_PART) * .02)
    totalTaxes += float((THIRD_PART - SECOND_PART) * .03)
elif income <= FIFTH_PART:
    taxPercentage = 0.05
    incomeRemainder = (income - FOURTH_PART)
    totalTaxes += float(FIRST_PART * .01)
    totalTaxes += float((SECOND_PART- FIRST_PART) * .02)
    totalTaxes += float((THIRD_PART- SECOND_PART) * .03)
    totalTaxes += float((FOURTH_PART- THIRD_PART) * .04)
elif income > FIFTH_PART:
    taxPercentage = 0.06
    incomeRemainder = (income - FIRST_PART - FIFTH_PART)
    totalTaxes += float(FIRST_PART * .01)
    totalTaxes += float((SECOND_PART - FIRST_PART) * .02)
    totalTaxes += float((THIRD_PART - SECOND_PART) * .03)
    totalTaxes += float((FOURTH_PART - THIRD_PART) * .04)
    totalTaxes += float((FIFTH_PART - FOURTH_PART) * .05)

totalTaxes += float(incomeRemainder * taxPercentage)
print("On %i income you have to pay %.2f taxes" % (income,totalTaxes))




