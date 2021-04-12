# Session 1: King Move

""" STATEMENT: Chess king moves horizontally, vertically or diagonally to any adjacent cell.
Given two different cells of the chessboard, determine whether a king can go from the first cell
to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell. The program should output
YES if a king can go from the first cell to the second in one move, or NO otherwise.

For example, on input 2, 3, 1, 4 output should be YES

TEMPLATE:

TESTS:
Input: 3, 4, 4, 5 Output: YES
Input: 5, 7, 4, 6 Output: YES
Input: 5, 6, 4, 7 Output: YES
Input: 1, 1, 1, 3 Output: NO
Input: 8, 8, 2, 4 Output: NO
Input: 5, 6, 3, 6 Output: NO """