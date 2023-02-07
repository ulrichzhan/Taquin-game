#Distance Manhattan

import random

def get_grid_size():
    while True:
        try:
            size = int(input("Entrez la taille de la grid (minimum 3): "))
            if size >= 3:
                return size
            else:
                print("Taille de grid non valide, doit être d'au moins 3.")
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

zero_pos = None
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == 0:
            zero_pos = (i, j)

zero_pos = shuffle_grid(zero_pos, GRID_SIZE * GRID_SIZE)

moves_counter = 0

import heapq

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def heuristique(grid, zero_pos, GRID_SIZE):
    h = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            if value != 0:
                target_i, target_j = (value - 1) // GRID_SIZE, (value - 1) % GRID_SIZE
                h += manhattan_distance((i, j), (target_i, target_j))
    return h

def make_move(grid, zero_pos, move, GRID_SIZE):
    new_pos = (zero_pos[0] + move[0], zero_pos[1] + move[1])
    if (new_pos[0] >= 0 and new_pos[0] < GRID_SIZE) and (new_pos[1] >= 0 and new_pos[1] < GRID_SIZE):
        grid_copy = [row[:] for row in grid]
        grid_copy[zero_pos[0]][zero_pos[1]], grid_copy[new_pos[0]][new_pos[1]] = grid_copy[new_pos[0]][new_pos[1]], grid_copy[zero_pos[0]][zero_pos[1]]
        zero_pos_copy = new_pos[:]
        return grid_copy, zero_pos_copy
    return None, None

def a_star(grid, zero_pos, GRID_SIZE):
    heap = []
    heapq.heappush(heap, (0, grid, zero_pos, []))
    visited = set()
    while heap:
        f, grid, zero_pos, path = heapq.heappop(heap)
        if grid in visited:
            continue
        visited.add(tuple(map(tuple, grid)))
        if all(value == (i * GRID_SIZE + j + 1) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if value != 0):
            return path
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for move in moves:
            grid_copy, zero_pos_copy = make_move(grid, zero_pos, move, GRID_SIZE)
            if grid_copy is None:
                continue
            h = heuristique(grid_copy, zero_pos_copy, GRID_SIZE)
            heapq.heappush(heap, (len(path) + h, grid_copy, zero_pos_copy, path + [move]))
    return None

while True:
    display_grid()
    display_moves(moves_counter)
    best_move = a_star(grid, zero_pos, GRID_SIZE)
    grid, zero_pos = make_move(grid, zero_pos, best_move, GRID_SIZE)
    moves_counter += 1

    if check_win():
        print("Félicitations! Vous avez gagné en", moves_counter, "mouvements.")
        for row in grid:
            print(row)
        break