# while True:
#     try:
#         number = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Please enter a number!")
#     except:
#         print("An unknown error occurred")
#
# print("thank you for entering a number.")

# dowhile executes at least once, do code while(condition = true)

# Guess a number between 1 - 10, if incorrect, try again, if correct --> you guessed it
# from random import randrange
#
# randomNumber = randrange(1, 10)
# while True:
#     guessNumber = int(input("Guess a number between 1 and 10: "))
#     if randomNumber != guessNumber:
#         print("Wrong, try again")
#     else:
#         print("Great job, you guessed it!")
#         break

# import math
#
# # Because you used import you access methods by referencing the module
# print("ceil(4,4) = ", math.ceil(4.4))  # --> round up
# print("floor(4,4) = ", math.floor(4.4))  # --> round down
# print("fabs(-4,4) = ", math.fabs(-4.4))  # --> absolute value
#
# # Factorial = 1 * 2 * 3 * 4
# print("Factorial(4) = ", math.factorial(4))
#
# # Returns remainder of a division
# print("fmod(5,4) = ", math.fmod(5, 4))
#
# # Receive a float and return an int
# print("trunc(4,2) = ", math.trunc(4.2))
#
# # Return x^y
# print("pow(2,2)", math.pow(2, 2))
#
# # Return the square root
# print("sqrt(4) = ", math.sqrt(4))
#
# # Special values
# print("math.e = ", math.e)
# print("math.pi = ", math.pi)
#
# # Return e^x
# print("exp(4) = ", math.exp(4))
#
# # Return the natural logarithm e * e * e ~= 20 so log(20) tells you that e^3 ~= 20
# print("log(20)", math.log(20))
#
# # You can define the base and 10^3 = 1000
# print("log(1000, 10) = ", math.log(1000, 10))
#
# # You can also use base 10 like this
# print("log10(1000) = ", math.log10(1000))
#
# # We have the following trig functions
# # sin, cos, tan, asin, atan, atan2, asinh, acosh,
# # atanh, sinh, cosh, tanh,
#
# # Convert radians to degrees and vice versa
# print("degrees(1.5708) = ", math.degrees(1.5708))
# print("radians(90) = ", math.radians(90))

from decimal import Decimal as D
# Decimal alias is now D

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum = ", sum)
print(".1 + .1 + .1 - .3", .1 + .1 + .1 - .3)