import copy
import math
import sys
from itertools import combinations

tiles = {}
tile_name = ''
tile = []
for line in sys.stdin:
    row = line.rstrip('\n')
    # Est-ce que la ligne contient du texte ?
    if row:
        if not tile_name:
            # Première ligne, on récupère le numéro de la tuile
            tile_name = int(row[5:-1])
        else:
            # Partie de la tuile
            tile.append(row)
    else:
        tiles[tile_name] = tile
        tile_name = ''
        tile = []

# On ajoute la dernière tuile
tiles[tile_name] = tile

# pprint(tiles)

SQUARE_WIDTH = int(math.sqrt(len(tiles)))


# print(SQUARE_WIDTH)

def possible_borders(tile):
    # 1ère et dernière ligne
    borders = [copy.deepcopy(tile[0]), copy.deepcopy(tile[-1])]

    # 1ère et dernière colonne
    borders.append("".join(tile[j][0] for j in range(len(tile))))
    borders.append("".join(tile[j][-1] for j in range(len(tile))))

    # On doit également tout retourner
    reversed_borders = [border[::-1] for border in borders]

    borders.extend(reversed_borders)

    return borders


def matching_borders(tile1_borders, tile2_borders):
    return any(tile1_border in tile2_borders for tile1_border in tile1_borders)


borders_by_tile = {tile_name: possible_borders(tile) for tile_name, tile in tiles.items()}

# pprint(borders_by_tile)
number_matching_tile = {tile_name: 0 for tile_name in tiles}

for tile1_name, tile2_name in combinations(tiles, 2):
    if matching_borders(borders_by_tile[tile1_name], borders_by_tile[tile2_name]):
        number_matching_tile[tile1_name] += 1
        number_matching_tile[tile2_name] += 1

# Les coins n'ont que 2 autres tuiles qui matchent
print(math.prod(tile_name for tile_name, number in number_matching_tile.items() if number == 2))
