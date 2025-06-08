'''
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
        o   Square root of the number
        o   Natural logarithm (log base e) of the number
        o    Sine of the number (in radians)
3.   Displays the calculated results.

'''
import math
number = int(input("Enter a number: "))
print("Square root: ", math.sqrt(number))
print("Logarithm: ", math.log(number))
print("Sine: ", math.sin(number))