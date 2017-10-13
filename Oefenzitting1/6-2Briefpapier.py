SIZE_ONE_INCH_TO_MM = 25.4
WIDTH_INCH = 8.5
HEIGHT_INCH = 11

print("Inch sizes",WIDTH_INCH," x ",HEIGHT_INCH, " inch")
print("Inch sizes",WIDTH_INCH * SIZE_ONE_INCH_TO_MM," x ",HEIGHT_INCH * SIZE_ONE_INCH_TO_MM, " mm")


print("Inch sizes %.1f x %.1f mm" % (WIDTH_INCH * SIZE_ONE_INCH_TO_MM, HEIGHT_INCH * SIZE_ONE_INCH_TO_MM))