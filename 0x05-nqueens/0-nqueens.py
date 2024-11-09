#!/usr/bin/python3
"""
N-Queens Challenge Solver

This script solves the N-Queens problem, where the objective is to place N queens
on an N x N chessboard in such a way that no two queens can attack each other.

Usage:
    python3 nqueens.py N

    N: The size of the chessboard (an integer). N must be at least 4.
       The script will print all possible solutions as a list of lists,
       where each sublist represents the position of a queen on the board
       in the format [row, column].

Example:
    $ python3 nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""

import sys


def is_safe(placed_queens, row, col):
    """
    Check if a queen can be safely placed at the given row and column.
    
    Args:
        placed_queens (list): List of coordinates where queens are already placed.
        row (int): The current row to check.
        col (int): The current column to check.
    
    Returns:
        bool: True if it is safe to place the queen, False otherwise.
    """
    for r, c in placed_queens:
        # Check for column conflict or diagonal conflicts
        if c == col or abs(col - c) == abs(row - r):
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem and return all possible solutions.
    
    Args:
        n (int): The size of the chessboard (N x N).
    
    Returns:
        list: A list of solutions, where each solution is represented as a list 
              of queen coordinates in the form [row, column].
    """
    solutions = []
    placed_queens = []  # Tracks positions of queens as [row, column]
    row = 0
    col = 0

    while row < n:
        placed = False
        while col < n:
            if is_safe(placed_queens, row, col):
                # Place the queen if the position is safe
                placed_queens.append([row, col])
                placed = True
                break
            col += 1

        if not placed:
            # No valid position found in this row, backtrack
            if not placed_queens:
                break
            row, col = placed_queens.pop()
            col += 1
            continue

        if len(placed_queens) == n:
            # Found a valid solution
            solutions.append(placed_queens[:])
            row, col = placed_queens.pop()
            col += 1
        else:
            # Move to the next row
            row += 1
            col = 0

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Generate and print all solutions
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
