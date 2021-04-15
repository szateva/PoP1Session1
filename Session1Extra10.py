# Session 1* Chocolate bar

""" STATEMENT: Chocolate bar has the form of a rectangle divided into n×m portions.
Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line
on its pattern.

Determine whether it is possible to split it so that one of the parts will have exactly k squares.

The program reads three integers: n, m, and k. It should print YES or NO.

For example, on input 2 , 10, 7 output must be NO

TEMPLATE:

TESTS:
Input: 4, 2, 6 Output: YES
Input: 2, 10, 7 Output: NO
Input: 7, 4, 21 Output: YES
Input: 7, 1, 6 Output: YES
Input: 7, 1, 8 Output: NO
Input: 387, 13, 2709 Output: YES """

choc_length = int(input("What is the length of the chocolate bar? "))
choc_width = int(input("What is the width of the chocolate bar? "))
choc_squares = int(input("How many squares to break off? "))

if choc_squares > (choc_width * choc_length):
    print("NO")
else:
    if (choc_squares % choc_width == 0) or (choc_squares % choc_length == 0):
        print("YES")
    else:
        print("NO")