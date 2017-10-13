import math

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

r = math.sqrt(math.pow(x,2)+math.pow(y,2))
theta = math.degrees(math.atan(x/y))



print("The radius is: ",r)
print("Theta is: ",theta)
