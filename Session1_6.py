# Session 1 Problem 06: Total count

""" STATEMENT:
A flower costs A pounds and B pence. Determine, how many pounds and pence
should one pay for N flowers. A program gets three numbers: A, B, N.
It should print two numbers: total cost in pounds and pence.

For exampe, on input 1, 50, 3 output should be 4, 50

TEMPLATE:

TESTS:
Input: 2, 50, 4 Output: 10, 0
Input: 10, 15, 2 Output: 20, 30
Input: 905, 79, 496 Output: 449271, 84
Input: 1886, 73, 295 Output: 556585, 35 """

pounds_per_flower = int(input("How many pounds per flower? "))
pence_per_flower = int(input("How many pence per flower? "))
no_of_flowers = int(input("How many flowers? "))

cost_of_flower_in_pence = pounds_per_flower * 100 + pence_per_flower
total_cost = cost_of_flower_in_pence * no_of_flowers

total_pounds = total_cost // 100
total_pence = total_cost % 100

print("Total pounds to pay is ", total_pounds)
print("Total pence to pay is ", total_pence)