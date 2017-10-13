first_time = int(input("Please enter the first time: "))
second_time = int(input("Please enter the second time: "))+2400

difference = second_time - first_time
difference %= 2400

hours = difference // 100;
minutes = difference % 100;

print("%i hours %i minutes" % (hours,minutes))