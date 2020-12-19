import copy
import sys
from pprint import pprint

initial_cubes = [[]]
for line in sys.stdin:
    initial_cubes[0].append([cube for cube in line.rstrip('\n')])


def get_row(n):
    return ['.' for i in range(n)]


def step(current_cubes):
    next_cubes = copy.deepcopy(current_cubes)
    next_width = len(next_cubes[0]) + 2
    # Increase size of existing rows by one cube at beginning and one cube at the end
    for next_layer in next_cubes:
        for next_row in next_layer:
            next_row.insert(0, '.')
            next_row.append('.')
            
    # Increase existing layer by one row at beginning and one row at the end
    for next_layer in next_cubes:
        next_layer.insert(0, get_row(next_width))
        next_layer.append(get_row(next_width))
    
    # Increase size of next cubes by one layer on top and bottom
    new_layer = [get_row(next_width) for i in range(next_width)]
    next_cubes.insert(0, new_layer)
    next_cubes.append(copy.deepcopy(new_layer))

    current_cubes = copy.deepcopy(next_cubes)

    for z in range(len(current_cubes)):
        for i in range(len(current_cubes[z])):
            for j in range(len(current_cubes[z][i])):
                if current_cubes[z][i][j] == '#':
                    if count_occupied(z, i, j, current_cubes) not in (2, 3):
                        # Pas assez de cubes occupés autour, le cube devient inactif
                        next_cubes[z][i][j] = '.'
                else:
                    if count_occupied(z, i, j, current_cubes) == 3:
                        # 3 cubes actifs autour, on active le cube
                        next_cubes[z][i][j] = '#'

    return next_cubes


def count_occupied(z, i, j, cubes):
    count = 0
    for z1 in range(z-1, z+2):
        for i1 in range(i-1, i+2):
            for j1 in range(j-1, j+2):
                # On compte tout, sauf le cube courant
                if z1 != z or i1 != i or j1 != j:
                    if check_cube_active(z1, i1, j1, cubes):
                        count += 1
    return count


def check_cube_active(z, i, j, cubes):
    if z < 0 or i < 0 or j < 0:
        # Hors de l'espace, cube non actif
        return False
    try:
        cube = cubes[z][i][j]
        if cube == '#':
            return True
        else:
            return False
    except IndexError:
        # Hors de l'espace, cube non actif
        return False


cycle = 0
while cycle < 6:
     # pprint(initial_cubes)
     # pprint("================")
     initial_cubes = step(initial_cubes)
     cycle += 1

# Final state
# pprint(initial_cubes)

total = 0
for layer in initial_cubes:
    for row in layer:
        for cube in row:
            if cube == '#':
                total += 1

print(total)
