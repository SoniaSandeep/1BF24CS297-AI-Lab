#hill cimbing

import random

N = 4


# Generate a random board
def random_board():
    return [random.randint(0, N-1) for _ in range(N)]

# Calculate heuristic (number of attacking queen pairs)
def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts

# Generate neighboring boards
def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if board[col] != row:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)

    return neighbors

# Hill Climbing algorithm
def hill_climbing():
    board = random_board()

    while True:
        current_h = heuristic(board)

        if current_h == 0:
            return board

        neighbors = get_neighbors(board)

        best_neighbor = min(neighbors, key=heuristic)
        best_h = heuristic(best_neighbor)

        if best_h >= current_h:
            return None  # Local minimum reached

        board = best_neighbor

# Display chessboard
def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Execute with random restarts
solution = None

while solution is None:
    solution = hill_climbing()

print("Solution Found:")
print_board(solution)
print("Heuristic value:", heuristic(solution))
