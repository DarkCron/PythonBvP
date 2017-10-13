gallons_gas = float(input("The number of gallons of gas in tank: "))
miles_per_gallon = float(input("The fuel efficiency in miles per gallon: "))
price_per_gallon = float(input("The price of gas per gallon: "))

DISTANCE = 100

drivable_distance = gallons_gas * miles_per_gallon;

# x miles = 1 gallon
# 100 miles = 1 / x * 100 gallons
DISTANCE_to_gallons = 100 // miles_per_gallon
price_per_DISTANCE = DISTANCE_to_gallons * price_per_gallon

print("Cost per 100 miles: %.2f" % price_per_DISTANCE)
print("Tank drive distance: %.2f" % drivable_distance)
