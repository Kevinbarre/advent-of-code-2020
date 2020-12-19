import copy
import sys
from pprint import pprint

initial_hypercubes = [[[]]]
for line in sys.stdin:
    initial_hypercubes[0][0].append([cube for cube in line.rstrip('\n')])


def get_row(n):
    return ['.' for i in range(n)]


def step(current_hypercubes):
    next_hypercubes = copy.deepcopy(current_hypercubes)
    next_width = len(next_hypercubes[0][0]) + 2

    # Increase size of existing rows by one cube at beginning and one cube at the end
    for next_cubes in next_hypercubes:
        for next_layer in next_cubes:
            for next_row in next_layer:
                next_row.insert(0, '.')
                next_row.append('.')
            
    # Increase existing layer by one row at beginning and one row at the end
    for next_cubes in next_hypercubes:
        for next_layer in next_cubes:
            next_layer.insert(0, get_row(next_width))
            next_layer.append(get_row(next_width))

    # Increase size of next cubes by one layer on top and bottom
    for next_cubes in next_hypercubes:
        new_layer = [get_row(next_width) for i in range(next_width)]
        next_cubes.insert(0, new_layer)
        next_cubes.append(copy.deepcopy(new_layer))

    # Add one more hypercube dimension
    new_cubes = [[get_row(next_width) for i in range(next_width)] for j in range(next_width)]
    next_hypercubes.insert(0, new_cubes)
    next_hypercubes.append(copy.deepcopy(new_cubes))

    current_hypercubes = copy.deepcopy(next_hypercubes)

    for w in range(len(current_hypercubes)):
        for z in range(len(current_hypercubes[w])):
            for i in range(len(current_hypercubes[w][z])):
                for j in range(len(current_hypercubes[w][z][i])):
                    if current_hypercubes[w][z][i][j] == '#':
                        if count_occupied(w, z, i, j, current_hypercubes) not in (2, 3):
                            # Pas assez de cubes occupés autour, le cube devient inactif
                            next_hypercubes[w][z][i][j] = '.'
                    else:
                        if count_occupied(w, z, i, j, current_hypercubes) == 3:
                            # 3 cubes actifs autour, on active le cube
                            next_hypercubes[w][z][i][j] = '#'

    return next_hypercubes


def count_occupied(w, z, i, j, cubes):
    count = 0
    for w1 in range(w -1, w+2):
        for z1 in range(z-1, z+2):
            for i1 in range(i-1, i+2):
                for j1 in range(j-1, j+2):
                    # On compte tout, sauf le cube courant
                    if w1 != w or z1 != z or i1 != i or j1 != j:
                        if check_cube_active(w1, z1, i1, j1, cubes):
                            count += 1
    return count


def check_cube_active(w, z, i, j, cubes):
    if w < 0 or z < 0 or i < 0 or j < 0:
        # Hors de l'espace, cube non actif
        return False
    try:
        cube = cubes[w][z][i][j]
        if cube == '#':
            return True
        else:
            return False
    except IndexError:
        # Hors de l'espace, cube non actif
        return False


cycle = 0
while cycle < 6:
     # pprint(initial_hypercubes)
     # pprint("================")
     initial_hypercubes = step(initial_hypercubes)
     cycle += 1

     # for w in range(0, 2* cycle + 1):
     #     for z in range(0, 2*cycle + 1):
     #         print("z={}, w={}".format(z -cycle, w-cycle))
     #         pprint(initial_hypercubes[w][z])

# Final state
# pprint(initial_hypercubes)

total = 0
for cube in initial_hypercubes:
    for layer in cube:
        for row in layer:
            for cube in row:
                if cube == '#':
                    total += 1

print(total)
