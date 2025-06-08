'''
Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''
# 0! = 1
# 1! = 1 * 0! = 1 * 1 = 1
# 2! = 2 * 1! = 2 * 1 = 2
# 3! = 3 * 2! = 3 * 2 = 6
# 4! = 4 * 3! = 4 * 6 = 24

def factorial(n):
    if n < 2 :
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Enter a number: "))
result = factorial(n)
print("Factorial of " + str(n) + " is: " + str(result))