'''
Task 3: Check if a Number is Even or Odd.

Problem Statement: Write a Python program that:

Takes an integer input from the user.
Checks whether the number is even or odd using an if-else statement.
Displays the result accordingly.
'''

number =  int (input("Enter a number: "))
if number % 2 != 0:
    print(str(number) + " is an odd number.")
else:
    print(str(number) + " is an even number.")