# Session 1: Sign of a Number

""" STATEMENT: For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's
equal to zero.

For example, on input -13 output should be -1

TEMPLATE:

TESTS:
Input: 5 Output: 1
Input: -15 Output: -1
Input: 0 Output: 0
Input: 1234 Output: 1 """

num = int(input("Enter a number: "))
if num == 0:
    print("0")
elif num < 0:
    print("-1")
else:
    print("1")