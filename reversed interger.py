# Question 5: Reverse Integer
#
# Write a program that takes an integer as input and returns an integer
# with reversed digit  ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

number = int(input("enter your number"))

if number >= 0:
    reversed_number = int(str(number)[::-1])
    print(reversed_number)

else:
    reversed_number = int(str(-number)[::-1])
    print("-",reversed_number)
