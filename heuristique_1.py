import random

def get_grid_size():
    while True:
        try:
            size = int(input("Entrez la taille de la grille (minimum 3): "))
            if size >= 3:
                return size
            else:
                print("Taille de grille non valide, doit être d'au moins 3.")
        except ValueError:
            print("Entrée non valide, veuillez entrer un nombre.")

GRID_SIZE = get_grid_size()
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

grid = [[i + j * GRID_SIZE for i in range(1, GRID_SIZE + 1)] for j in range(GRID_SIZE)]
grid[-1][-1] = 0

def display_grid():
    for row in grid:
        print(row)

def shuffle_grid(zero_pos, moves_counter):
    moves = [UP, DOWN, LEFT, RIGHT]
    for i in range(moves_counter):
        random_move = random.choice(moves)
        new_pos = (zero_pos[0] + random_move[0], zero_pos[1] + random_move[1])
        if (new_pos[0] >= 0 and new_pos[0] < GRID_SIZE) and (new_pos[1] >= 0 and new_pos[1] < GRID_SIZE):
            grid[zero_pos[0]][zero_pos[1]] = grid[new_pos[0]][new_pos[1]]
            grid[new_pos[0]][new_pos[1]] = 0
            zero_pos = new_pos
    return zero_pos

def check_win():
    actual_grid = [i for ligne in grid for i in ligne]
    final_grid = [i for i in range(1, GRID_SIZE ** 2)] + [0]
    return actual_grid == final_grid

def display_moves(moves_counter):
    print("moves effectués: ", moves_counter)

def count_misplaced_tiles(grid):
    misplaced_tiles = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0 and grid[i][j] != i * GRID_SIZE + j + 1:
                misplaced_tiles += 1
    return misplaced_tiles

zero_pos = None
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == 0:
            zero_pos = (i, j)
            break
    if zero_pos:
        break

moves_counter = 0

zero_pos = shuffle_grid(zero_pos, GRID_SIZE * GRID_SIZE)

while not check_win():
    display_grid()
    display_moves(moves_counter)
    zero_pos = shuffle_grid(zero_pos, 1)
    moves_counter += 1
    misplaced_tiles = count_misplaced_tiles(grid)

display_grid()
print("Bravo, vous avez gagné en ", moves_counter, " coups!")
