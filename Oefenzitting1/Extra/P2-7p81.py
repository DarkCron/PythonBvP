import  math

r = float(input("Enter a radius: "))

area = math.pow(r,2) * math.pi
circumference = 2 * math.pi * r

sphere_area = 4 * math.pi * math.pow(r,2)
sphere_volume = 4//3 * math.pi * math.pow(r,3)

print("Circle area: %.2f, Circle circumference: %.2f" % (area,circumference))
print("Sphere area: %.2f, Sphere volume: %.2f" % (sphere_area,sphere_volume))

