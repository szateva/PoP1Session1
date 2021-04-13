# Session 1 Problem 10: Chess Board

""" STATEMENT: Given two cells of a chessboard. If they are painted in one color,
print the word YES, and if in a different color - NO.

The program receives the input of four numbers from 1 to 8, each specifying
the column and row number, first two - for the first cell, and then the last
two - for the second cell.

It is assumed that the cells are numbered from left to right and from bottom
to top, i.e., the bottom left cell has column number 1 and row number 1
while the bottom right cell has column number 8 and row number 1.

For example, on input 1, 1, 2, 6 output must be YES

TEMPLATE:

TESTS:
Input: 2, 2, 2, 5 Output: NO
Input: 2, 2, 2, 4 Output: YES
Input: 2, 3, 3, 2 Output: YES
Input: 2, 3, 7, 8 Output: YES
Input: 2, 3, 8, 8 Output: NO """

col1 = int(input("What is the coord of the first col? "))
row1 = int(input("What is the coord of the first row? "))
col2 = int(input("What is the coord of the second col? "))
row2 = int(input("What is the coord of the second row? "))

sum1 = col1 + row1
sum2 = col2 + row2

if sum1 % 2 == sum2 % 2:
    print("YES")
else:
    print("NO")