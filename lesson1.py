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

# problem1: receive miles and convert to kilometers
# kilometers = miles * 1.60934
# e.g. 5 miles equals x kilometers

miles = input('Enter Miles: ')
miles = int(miles)

kilometers = miles * 1.60934

print("{} miles equals {} kilometers".format(miles, kilometers))

# Enter calculation: 5 * 6
# 5 * 6 =  30

# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert the strings to ints
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
# Print the result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Use either + - * or / next time")

# We'll provide different outputs based on age
# 1 - 18 -> important
# 21, 50, > 65 -> important
# All others -> Not important

# Receive age and store in var age
age = eval(input("Enter your age: "))

if (age >= 1) and (age <= 18):
    print("Important Birthday")
elif (age == 21) or (age == 50) or not(age < 65):
    print("Important Birthday")
else:
    print("Your birthday isn't important this year.")


# Problem2: if age 5 -> go to kindergarten
# 6-17 Grade 1 - 12
# age > 17 go to college
# post college
# less than 10 lines of code!
age = eval(input("How old are you: "))
if age < 5:
    print("Stay home and play!")
elif age == 5:
    print("Go to kindergarten")
elif (age > 5) and (age < 18):
    grade = age - 5
    print("Go to Grade {}".format(grade))
else:
    print("Go to College")
