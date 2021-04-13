# Session 1: Equal Numbers

""" STATEMENT: Given three integers, determine how many of them are equal to each other.The program
must print one of these numbers: 3( if all are the same), 2( if two of them are equal to each other and the
third is different) or 0 (if all numbers are different).

For example, on input 4, 5, 4 output must be 2

TEMPLATE:

TESTS:
Input: 4, 4, 4 Output: 3
Input: 6, 6, 1 Output: 2
Input: 5, 9, 10 Output: 0
Input: 3, 3, 8 Output: 2
Input: 2, 9, 9 Output: 2 """

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 == num3:
    print("3")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("2")
else:
    print("0")