input_1 = int(input("Number 1: "))
input_2 = int(input("Number 2: "))
input_3 = int(input("Number 3: "))

smallestNumber = input_1
biggestNumber = input_1
middleNumber = input_1

if input_2 > biggestNumber:
    biggestNumber = input_2

if input_3 > biggestNumber:
    biggestNumber = input_3

if smallestNumber > input_2:
    smallestNumber = input_2

if smallestNumber > input_3:
    smallestNumber = input_3

if (smallestNumber == input_1 or smallestNumber == input_3) and (biggestNumber == input_1 or biggestNumber == input_3):
    middleNumber = input_2
elif (smallestNumber == input_2 or smallestNumber == input_3) and (
        biggestNumber == input_2 or biggestNumber == input_3):
    middleNumber = input_1
elif (smallestNumber == input_2 or smallestNumber == input_1) and (
        biggestNumber == input_2 or biggestNumber == input_1):
    middleNumber = input_3

print("The inputs in sorted order are: " + str(smallestNumber) + ", " + str(middleNumber) + " and " + str(biggestNumber))
