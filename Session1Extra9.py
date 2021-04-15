# Session 1* Queen Move

""" STATEMENT: Consider representation of chess board as in the problem Session 1 Problem 15: Chess Board
Chess queen moves horizontally, vertically or diagonally to any number of cells.
Given two different cells of the chessboard, determine whether a queen can go from the first cell
to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell. The program should output
YES if a queen can go from the first cell to the second in one move, or NO otherwise.

For example, on input 4, 2, 6, 3, output must be NO

TEMPLATE:

TESTS:
Input: 4, 2, 6, 3 Output: NO
Input: 4, 2, 7, 5 Output: YES
Input: 4, 2, 4, 8 Output: YES
Input: 4, 2, 3, 2 Output: YES
Input: 5, 3, 6, 5 Output: NO """

col1 = int(input("What is the coord of the first col? "))
row1 = int(input("What is the coord of the first row? "))
col2 = int(input("What is the coord of the second col? "))
row2 = int(input("What is the coord of the second row? "))

col_diff = abs(col2 - col1)
row_diff = abs(row2 - row1)
same_col = (col1 == col2)
same_row = (row1 == row2)

if same_row or same_col or (col_diff == row_diff):
    print("YES")
else:
    print("NO")