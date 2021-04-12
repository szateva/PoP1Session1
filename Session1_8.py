# Session 1 Problem 08: Minimum of 3 numbers

""" STATEMENT: Given three integer numbers, determine their minimum
For example, on input 4, 2, 7 the output should be 2

TEMPLATE:

TESTS:
Input: 1, 2, 3 Output: 1
Input: 7, 3, 4 Output: 3
Input: 4, 7, 0 Output: 0
Input: 4, 4, 2 Output: 2
Input: 7, 3, 3 Output: 3 """

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1 <= num2 and num1 <= num3:
    min = num1
elif num2 <= num1 and num2 <= num3:
    min = num2
else:
    min = num3

print("The minimum of the three numbers is:", min)