# Question 3: Power of Two
# Write a program that takes an integer as input and
# returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false

def check_input(n):
     if n<=0:
        return False
     return n & (n-1) == 0

num=int(input("enter your integer: "))
print(num, " is ",check_input(num))



