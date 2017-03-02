# for i in [2, 4, 6, 8, 10]:
#     print("i = ", i)
#
# for i in range(0, 11, 2):
#     print (i)
#
# # problem 1: print odds from 1 - 20
# for i in range(1, 21):
#     if (i % 2) != 0:
#         print(i)
#
# your_float = input("Enter a float: ")
# your_float = float(your_float)
# print("Rounded to 2 decimals: {:.2f}".format(your_float))
#
# # problem 2: have the user enter their investment amount and expected interest earned each year
# # each your their investment will increase by their investment + their investment * interest rate
# # print out earnings after a 10 year period
#
# investment = input("How much would you like to invest: ")
# interest_rate = input("What is the interest rate: ")
#
# investment = float(investment)
# interest_rate = float(interest_rate) * .01
# # My solution
# for i in range(11):
#     print("In year {} your investment earnings would be {:.2f}".format(i, investment))
#     investment += investment * interest_rate
#
# # Derek's Solution
# for i in range(10):
#     investment += investment * interest_rate
# print("Investment after 10 years: {:.2f}".format(investment))
#
# import random
# rand_num = random.randrange(1, 51)
# i = 1
#
# while (i != rand_num):
#     i += 1
#
# print("The random value is: ", rand_num)
#
# i = 1
# while i <= 20:
#     if (i % 2) == 0:
#         i += 1
#         continue  # this means any code below here doesn't run, it loops back to the beginning
#     if i == 15:
#         break  # I don't want the loop to continue, stop/break here
#     print("Odd: ", i)
#     i += 1

# Problem 3: Draw a pine tree on the screen
# how tall is the tree
# use 1 while loop and 3 for loops
   #
  ###
 #####
#######
   #
# 4 space : 1 hash
# 3 space : 3 hash
# 2 space : 5 hash
# 1 space : 7 hash
# 0 space : 9 hash
# 4 space : 1 hash


#Stephan's answer below
treeHeight = eval(input("How tall is the tree: "))
i = 0
hashCount = 1
print((treeHeight + 1) * ' ' + '#')
while i < treeHeight - 1:
    initialNum = treeHeight - 1
    space = initialNum - i
    hashCount += 2
    print((space * ' '), ('#' * hashCount))
    i += 1
    continue
print((treeHeight + 1) * ' ' + '#')

# Derek's Answer Below
# Get the number of rows for the tree
tree_height = input('How tall is the tree: ')

# convert into an integer
tree_height = int(tree_height)

# get the starting spaces for the top of the tree
spaces = tree_height - 1

# One hash to start that will be incremented
hashes = 1

# save stump spaces for later
stump_spaces = tree_height - 1

# make sure right number of rows are printed
while tree_height != 0:
    # print spaces --> end=''
    for i in range(spaces):
        print(' ', end='')
# print the hashes
    for i in range(hashes):
        print('#', end='')

# new line after each row is printed
    print()

# spaces decremented by 1 each time
    spaces -= 1

# hashes incremented by 2 each time
    hashes += 2

# decrement tree height each time to jump out of the loop
    tree_height -= 1

# print stump
for i in range(stump_spaces):
    print(' ', end='')

print('#')

