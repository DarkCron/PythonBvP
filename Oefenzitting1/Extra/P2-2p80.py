import math

SIZE_WIDTH = 8.5
SIZE_HEIGHT = 11

perimeter = SIZE_WIDTH * SIZE_HEIGHT
diagonal = math.sqrt(math.pow(SIZE_WIDTH,2)+math.pow(SIZE_HEIGHT,2))

print("Perimeter is: %.1f; the diagonals are: %.1f" % (perimeter,diagonal))