# Session 1 Problem 12: Bishop Move

""" STATEMENT: In chess, the bishop moves diagonally, any number of squares.
Given two different squares of the chessboard, determine whether a bishop
can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the column
and row numbers of the starting square and the column and row numbers of the
ending square. The program should output YES if a Bishop can go from the first
square to the second in one move, or NO otherwise.

For example, on input 2, 3, 5, 6 output must be YES
TEMPLATE:

TESTS:
Input: 4, 4, 5, 5 Output: YES
Input: 4, 4, 5, 4 Output: NO
Input: 4, 4, 5, 3 Output: YES
Input: 4, 4, 3, 5 Output: YES
Input: 1, 2, 7, 8 Output: YES
Input: 1, 2, 8, 8 Output: NO """

col1 = int(input("What is the coord of the first col? "))
row1 = int(input("What is the coord of the first row? "))
col2 = int(input("What is the coord of the second col? "))
row2 = int(input("What is the coord of the second row? "))

if abs(col2 - col1) == abs(row2 - row1):
    print("YES")
else:
    print("NO")