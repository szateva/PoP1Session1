# Session 1 Problem 07: Minimum of 2 Numbers

""" STATEMENT: Given the two integer numbers, determine their minimum.
For example, on input 3, 8 the output should be 3

TEMPLATE:

TESTS:
Input: 5, 6 Output: 5
Input: 0, 10 Output: 0
Input: 3, 3 Output: 3
Input: -5, -10 Output: -10 """

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

if num1 <= num2:
    min = num1
else:
    min = num2

print("The minimum of the two numbers is ", min)