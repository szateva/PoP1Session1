# Session 1* Digital Clock

""" STATEMENT: Given the integer N - the number of minutes that is passed since midnight -
how many hours and minutes are displayed on the 24h digital clock?

The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes
(between 0 and 59).

For example, on input 150 output must be 2 30

TEMPLATE:

TESTS:
Input: 150 Output: 2 30
Input: 180 Output: 3 0
Input: 444 Output: 7 24
Input: 1439 Output: 23 59 """

num_of_minutes = int(input("How many minutes since midnight? "))
hours_passed = num_of_minutes // 60
minutes_passed = num_of_minutes % 60

print(hours_passed, minutes_passed)