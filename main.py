from functions import *

while True:
    display_grid()
    display_moves(moves_counter)
    move = input("Entrez un déplacement (up, down, left, right): ")

    if move == "up":
        new_pos = (zero_pos[0] + UP[0], zero_pos[1] + UP[1])
    elif move == "down":
        new_pos = (zero_pos[0] + DOWN[0], zero_pos[1] + DOWN[1])
    elif move == "left":
        new_pos = (zero_pos[0] + LEFT[0], zero_pos[1] + LEFT[1])
    elif move == "right":
        new_pos = (zero_pos[0] + RIGHT[0], zero_pos[1] + RIGHT[1])
    else:
        print("Déplacement non valide, veuillez réessayer")
        continue

    #Verifie si new_pos soit entre 0 et GRID_SIZE-1 et si la valeur à cette position est bien 0 pour ensuite déplacer selon le move et met à zéro la case à déplacer
    if (new_pos[0] >= 0 and new_pos[0] < GRID_SIZE) and (new_pos[1] >= 0 and new_pos[1] < GRID_SIZE) and grid[zero_pos[0]][zero_pos[1]] == 0:
        grid[zero_pos[0]][zero_pos[1]] = grid[new_pos[0]][new_pos[1]] 
        grid[new_pos[0]][new_pos[1]] = 0 
        zero_pos = new_pos
        moves_counter += 1

    if check_win():
        print("Félicitations! Vous avez gagné en", moves_counter, "mouvements.")
        break