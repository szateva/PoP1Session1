# Session 1 Problem 05: Area of right-angled triangle

"""STATEMENT:
Write a program that reads the length of the base and the height of a
right-angled triangle and prints the area. Every number is given on a
separate line.

For example, on input 7, 5 output should be 17.5

Note. Always output a float number, e.g. 7.0 and not 7

TEMPLATE:

TESTS:

Input: 9, 9 Output: 40.5
Input: 6, 4 Output: 12.0
Input: 1, 1 Output: 0.5 """

base = int(input("What is the base of the triangle? "))
height = int(input("What is the height of the triangle? "))
area = float(base * height / 2)

print("The area of the triangle is ", area)