import random
import math

N =8


# Generate a random board
def random_board():
    return [random.randint(0, N-1) for _ in range(N)]

# Calculate heuristic (number of attacking pairs)
def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts

# Generate a neighboring state
def get_neighbor(board):
    new_board = board.copy()

    col = random.randint(0, N-1)
    row = random.randint(0, N-1)

    new_board[col] = row

    return new_board

# Simulated Annealing algorithm
def simulated_annealing():
    current = random_board()
    temperature = 1000
    cooling_rate = 0.99

    while temperature > 0.1:

        if heuristic(current) == 0:
            return current

        neighbor = get_neighbor(current)

        current_h = heuristic(current)
        neighbor_h = heuristic(neighbor)

        delta = neighbor_h - current_h

        # Accept better or worse states probabilistically
        if delta < 0:
            current = neighbor
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = neighbor

        temperature *= cooling_rate

    return None

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
    solution = simulated_annealing()

print("Solution Found:")
print_board(solution)

print("Heuristic value:", heuristic(solution))
