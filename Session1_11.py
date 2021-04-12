# Session 1 Problem 11: Rook move

""" STATEMENT: Chess rook moves horizontally or vertically on the chessboard.
Given two different cells of the chessboard, determine whether a rook can go
from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying
the column and row number, first two - for the first cell, and then the
last two - for the second cell. The program should output YES if a rook can go
from the first cell to the second in one move, or NO otherwise.

For example, on input 2, 3, 5, 6 output must be NO

TEMPLATE:

TESTS:
Input: 4, 4, 5, 5 Output: NO
Input: 5, 5, 6, 5 Output: YES
Input: 1, 1, 1, 8 Output: YES
Input: 1, 5, 1, 1 Output: YES
Input: 2, 2, 6, 6 Output: NO """