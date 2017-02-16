# On every year that is evenly divisible by 4
# Except every year that is evenly divisible by 100
# Unless the year is also evenly divisible by 400
# For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

year = eval(input("Input a year to figure out if it's a leap year: "))

if year % 400 == 0:
    print("{} is a Leap Year".format(year))
elif year % 100 == 0:
    print("{} is not a Leap Year".format(year))
elif year % 4 == 0:
    print("{} is a Leap Year".format(year))
else:
    print("{} is not a leap year!".format(year))

