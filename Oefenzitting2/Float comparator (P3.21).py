float1 = float(input("Enter a floating-point number: "))
float2 = float(input("Enter a floating-point number: "))

str1 = str(round(float1,2))
str2 = str(round(float2,2))

bTheSame = str1 == str2

if bTheSame:
    print("They are the same up to two decimal places.")
else:
    print("They are different.")


