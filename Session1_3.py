# Session 1 Problem 03: Sharing

""" STATEMENT:
N students take K pens and distribute them among each other evenly.
The remaining (the undivisible) part remains in the box.
How many pens will each single student get?
How many pens will remain in the box?
The program reads the numbers N and K.
It should print the two answers for the questions above.

For example, on input 5, 17 output should be 3, 2
TEMPLATE:

TESTS:
Input: 6, 50 Output: 8, 2
Input: 1, 10 Output: 10, 0
Input: 4, 2 Output: 0, 2 """


no_of_students = int(input("How many student? "))
no_of_pens = int(input("How many pens? "))

pen_per_student = str(no_of_pens//no_of_students)
remaining_pens = str(no_of_pens%no_of_students)
print("Number of pens per student: " + pen_per_student)
print("Pens remaining in the box: " + remaining_pens)