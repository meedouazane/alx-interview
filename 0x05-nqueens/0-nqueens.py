#!/usr/bin/python3
""" N Queen Problem """
import sys


def is_attack(row, col, board, N):
    """Check if placing a queen at position (row, col) is safe."""
    for k in range(N):
        if board[row][k] == 1 or board[k][col] == 1:
            return True
    for k in range(N):
        for diag in range(N):
            if (k + diag == row + col) or (k - diag == row - col):
                if board[k][diag] == 1:
                    return True
    return False


def n_queen(N, board, row, solutions):
    """Recursive function to solve the N Queens problem."""
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    for col in range(N):
        if not is_attack(row, col, board, N) and board[row][col] != 1:
            board[row][col] = 1
            n_queen(N, board, row + 1, solutions)
            board[row][col] = 0
    return False


def main():
    """Main function to handle input and output."""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    N = sys.argv[1]
    try:
        N = int(N)
    except ValueError:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4')
        exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    n_queen(N, board, row=0, solutions=solutions)
    if solutions:
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    main()
