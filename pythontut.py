# ask user to input their name and stor it to a variable

name = input('What is your name: ')

# print out hello follow by the name they entered

print('Hello ' + name)

# ask user to input 2 values and store them in variables num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

# convert strings into Integers
num1 = int(num1)
num2 = int(num2)

# add the values entered and store in sum
sum = num1 + num2

# subtract values and store in difference
difference = num1 - num2

# multiply values and store in product
product = num1 * num2

# divide values and store in quotient
quotient = num1 / num2

# use modulus to find the remainder
remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

# problem: receive miles and convert to kilometers
# kilometers = miles * 1.60934
# e.g. 5 miles equals x kilometers

miles = input('Enter Miles: ')
miles = int(miles)

kilometers = miles * 1.60934

print("{} miles equals {} kilometers".format(miles, kilometers))
