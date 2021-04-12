# Session 1 Problem 04: Sum of 3 digit number

""" STATEMENT:
Given a three-digit number, find the sum of its digits.
Hint. For an integer number N, its last digit can be found as follows:

last_dig = N % 10

Its second last number can be found as follows:

second_last_dig = (N // 10) % 10

For example, on input 163 the output should be 10

TEMPLATE:

TESTS:
Input: 179 Output: 17
Input: 829 Output: 19
Input: 100 Output: 1 """

number = int(input("Type in a 3 digit number: "))

units_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 100

sum_of_ditis = hundreds_digit + tens_digit + units_digit

print("The sum of the digits in " + str(number) + " is " + str(sum_of_ditis))