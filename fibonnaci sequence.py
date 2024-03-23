# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.
fibonacci = [0,1]

while fibonacci[-1]+fibonacci[-2] <= 100:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)
