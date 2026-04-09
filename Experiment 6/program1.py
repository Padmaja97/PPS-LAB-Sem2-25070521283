# Input
day = int(input())
month = int(input())
year = int(input())

valid = True

# Check year
if year <= 0:
    valid = False

# Check month
if month < 1 or month > 12:
    valid = False

# Leap year check
leap = False
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap = True

# Days in month
if month in [1,3,5,7,8,10,12]:
    max_day = 31
elif month in [4,6,9,11]:
    max_day = 30
elif month == 2:
    if leap:
        max_day = 29
    else:
        max_day = 28
else:
    max_day = 0

# Validate day
if day < 1 or day > max_day:
    valid = False

# Output
if not valid:
    print("Invalid Date")
else:
    day += 1
    if day > max_day:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    print(f"{day:02d}-{month:02d}-{year}")
