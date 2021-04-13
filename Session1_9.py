# Session 1 Problem 09: Leap year

""" STATEMENT: Given the year number. You need to check if this year is a
leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:
a year is a leap year if its number is exactly divisible by 4 and is not
exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400

Warning. The words LEAP and COMMON should be printed all caps.

For example, on input 2000 output must be LEAP

TEMPLATE:

TESTS:
Input: 2012 Output: LEAP
Input: 2011 Output: COMMON
Input: 1492 Output: LEAP
Input: 1861 Output: COMMON
Input: 1600 Output: LEAP """

year = int(input("What year do you want to check? "))

if year % 400 == 0:
    to_print = "LEAP"
elif year % 4 == 0 and year % 100 != 0:
    to_print = "LEAP"
else:
    to_print = "COMMON"

print(to_print)