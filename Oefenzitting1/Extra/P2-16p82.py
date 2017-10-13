five_numbers = int(input("Give me a number of 5 digits: "))

num1 = int(five_numbers / 10000)
num2 = int(five_numbers % 10000 / 1000)
num3 = int(five_numbers % 1000 / 100)
num4 = int(five_numbers % 100 / 10)
num5 = int(five_numbers % 10 / 1)

print(num1,num2,num3,num4,num5)