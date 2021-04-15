# Session 1: First number after decimal point

""" STATEMENT: Given a positive real number, print its first digit to the right of the decimal point.

For example, on input 56.8945 output should be 8

TEMPLATE:

TESTS:
Input: 466.345 Output: 3
Input: 0.001 Output: 0
Input: 45.0 Output: 0 """

num = float(input("Type your number: "))
fraction_part = num % 1
times_ten = round(fraction_part * 10, 3)
first_digit = int(times_ten // 1)
print(first_digit)