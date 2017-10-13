status = input("Are you married or single? ")
bIsMarried = status.lower() == "married"
income = int(input("Please enter your annual income: "))
totalTaxes = 0.0
taxableIncome = 0

if not bIsMarried:
    BASE_SINGLE_LOWER = 8000
    BASE_SINGLE_HIGHER = 32000
    if income < 0:
        totalTaxes = income * 0.1
    elif income > BASE_SINGLE_LOWER and income <= BASE_SINGLE_HIGHER:
        totalTaxes = BASE_SINGLE_LOWER * 0.1
        taxableIncome = income - BASE_SINGLE_LOWER
        totalTaxes += taxableIncome * .15
    elif income > BASE_SINGLE_HIGHER:
        totalTaxes = BASE_SINGLE_LOWER * 0.1
        totalTaxes += (BASE_SINGLE_HIGHER - BASE_SINGLE_LOWER) * .15
        taxableIncome = income - BASE_SINGLE_HIGHER
        totalTaxes += taxableIncome * .25
else:
    BASE_SINGLE_LOWER = 16000
    BASE_SINGLE_HIGHER = 64000
    if income < 0:
        totalTaxes = income * 0.1
    elif income > BASE_SINGLE_LOWER and income <= BASE_SINGLE_HIGHER:
        totalTaxes = BASE_SINGLE_LOWER * 0.1
        taxableIncome = income - BASE_SINGLE_LOWER
        totalTaxes += taxableIncome * .15
    elif income > BASE_SINGLE_HIGHER:
        totalTaxes = BASE_SINGLE_LOWER * 0.1
        totalTaxes += (BASE_SINGLE_HIGHER - BASE_SINGLE_LOWER) * .15
        taxableIncome = income - BASE_SINGLE_HIGHER
        totalTaxes += taxableIncome * .25

print("As a "+status)
print("With %i as your income your total taxes are %.2f" % (income,totalTaxes))