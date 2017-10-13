seconds = int(input("Time in seconds: "))

SECONDS_IN_MINUTES = 60
SECONDS_IN_HOUR = 60*60
SECONDS_IN_DAYS = 24 * 60 * 60



days = int(seconds // SECONDS_IN_DAYS)
seconds %= SECONDS_IN_DAYS

hours = int(seconds // SECONDS_IN_HOUR)
seconds %= SECONDS_IN_HOUR

minutes = int(seconds // SECONDS_IN_MINUTES)
seconds %= SECONDS_IN_MINUTES

seconds = seconds

print(days,"days,",hours,"hours,",minutes,"minutes,",seconds,"seconds")