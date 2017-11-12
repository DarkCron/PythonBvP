m = int(input("m: "))
n = int(input("n: "))
evenNumbers = set()
div3Numbers = set()

# m<n
for num in range(m,n+1):
    if num % 2 == 0:
        evenNumbers.add(num)
    if num % 3 == 0:
        div3Numbers.add(num)

print("Divisible by 6: ")
for num in div3Numbers:
    if num in evenNumbers:
        print(num,", ",end = "")

print("\nHow many odd integers between m and n that are divisible by 3?: ")
for num in div3Numbers:
    if not num in evenNumbers:
        print(num, ", ", end="")

print("\nHow many integers divisible by either 2 or 3?: ")
for num in div3Numbers:
    print(num, ", ", end="")

for num in evenNumbers:
    if not num in div3Numbers:
        print(num, ", ", end="")