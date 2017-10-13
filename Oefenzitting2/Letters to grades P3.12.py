print("Enter a letter grade: ")
lettergrade = input("")
numberGrade = 0.0

DEFAULT_A = 4.0
DEFAULT_B = 3.0
DEFAULT_C = 2.0
DEFAULT_D = 1.0
DEFAULT_F = 0.0

DEFAULT_MOD = 0.3

currentValue = 0.0
printValue = ""

if (lettergrade).startswith("A"):
    currentValue = DEFAULT_A
elif (lettergrade).startswith("B"):
    currentValue = DEFAULT_B
elif (lettergrade).startswith("C"):
    currentValue = DEFAULT_C
elif (lettergrade).startswith("D"):
    currentValue = DEFAULT_D
elif (lettergrade).startswith("F"):
    currentValue = DEFAULT_F

if (lettergrade).endswith("-"):
    currentValue -= DEFAULT_MOD
elif (lettergrade).endswith("+"):
    currentValue += DEFAULT_MOD

if lettergrade[0].isdecimal():
    numberGrade = float(lettergrade)
    bHasSign = False
    bHasPlus = False
    letterValue = 0.0

    if not (numberGrade % 1 == 0):  
        bHasSign = True

    if bHasSign:
        if (numberGrade + 0.3) % 1 == 0:
            bHasPlus = False
            letterValue = numberGrade + 0.3
        else:
            bHasPlus = True
            letterValue = numberGrade - 0.3

    letterValue = int(letterValue + 0.1)
    letterValue = float(letterValue)

    if letterValue == DEFAULT_A:
        printValue = "A "
    elif letterValue == DEFAULT_B:
        printValue = "B "
    elif letterValue == DEFAULT_C:
        printValue = "C "
    elif letterValue == DEFAULT_D:
        printValue = "D "
    elif letterValue == DEFAULT_F:
        printValue = "F "

    if bHasSign:
        if bHasPlus:
            printValue += "+"
        else:
            printValue += "-"
else:
    printValue = str(currentValue)



print("Numeric value: "+ printValue)
