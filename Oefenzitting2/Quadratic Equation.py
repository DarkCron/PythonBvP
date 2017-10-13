import math

num_a = int(input("Enter coefficient a: "))
num_b = int(input("Enter coefficient b: "))
num_c = int(input("Enter coefficient c: "))

num_D = math.pow(num_b, 2) - 4 * (num_a * num_c)
bHasSolution = num_D >= 0

if bHasSolution:
    print("Has solution : " + "YES")
else:
    print("Has solution : " + "NO")

if bHasSolution:
    sol_1 = float((-num_b + math.sqrt(num_D)) / 2)
    sol_2 = float((-num_b - math.sqrt(num_D)) / 2)
    print("Solution 1: %.2f" % sol_1)
    print("Solution 2: %.2f" % sol_2)

