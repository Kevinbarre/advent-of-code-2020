import sys
from collections import Counter
from pprint import pprint

instructions = []
for line in sys.stdin:
    instructions.append(line.rstrip('\n'))


class Hexagon:
    """
    Implement cube coordinates from https://math.stackexchange.com/questions/2254655/hexagon-grid-coordinate-system
    """

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def move(self, direction):
        if direction == "ne":
            self.x += 1
            self.z -= 1
        elif direction == "sw":
            self.x -= 1
            self.z += 1
        elif direction == "nw":
            self.y += 1
            self.z -= 1
        elif direction == "se":
            self.y -= 1
            self.z += 1
        elif direction == "e":
            self.x += 1
            self.y -= 1
        elif direction == "w":
            self.x -= 1
            self.y += 1
        else:
            return False
        return True

    def getNeighbors(self):
        neighbors = [Hexagon(x=self.x + 1, y=self.y, z=self.z - 1), Hexagon(x=self.x - 1, y=self.y, z=self.z + 1),
                     Hexagon(x=self.x, y=self.y + 1, z=self.z - 1), Hexagon(x=self.x, y=self.y - 1, z=self.z + 1),
                     Hexagon(x=self.x + 1, y=self.y - 1, z=self.z), Hexagon(x=self.x - 1, y=self.y + 1, z=self.z)]
        return neighbors

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "(x={}, y={}, z={})".format(self.x, self.y, self.z)

    def __hash__(self):
        return hash(self.x) + hash(self.y) + hash(self.z)


all_hexagons = []
for instruction in instructions:
    hexagon = Hexagon()
    current_direction = ""
    for c in instruction:
        current_direction += c
        if hexagon.move(current_direction):
            # On s'est déplacé, on réinitialise la direction
            current_direction = ""
    all_hexagons.append(hexagon)

# On compte les hexagones retournés un nombre impair de fois
counter = Counter(all_hexagons)
black_hexagons = {h for h, v in counter.items() if v % 2 == 1}


# print(black_hexagons)


def step(current_black_hexagons):
    # Dict des hexagones et leur nombre de tuiles noire adjacentes
    black_hexagons_count = {}

    # On commence par déterminer les hexagones susceptibles de changer, ce sont ceux qui sont voisins d'un hexagone noir actuellement (ainsi que les hexagones noir eux mêmes)
    for current_black_hexagon in current_black_hexagons:
        if current_black_hexagon not in black_hexagons_count:
            black_hexagons_count[current_black_hexagon] = 0
        for neighbor_hexagon in current_black_hexagon.getNeighbors():
            if neighbor_hexagon in black_hexagons_count:
                # On a déjà rencontré cet hexagon, on lui comptabilise un voisin noir de plus
                black_hexagons_count[neighbor_hexagon] += 1
            else:
                # Nouvel hexagon, il a un voisin noir
                black_hexagons_count[neighbor_hexagon] = 1

    next_black_hexagons = set()

    for hexagon, count in black_hexagons_count.items():
        if hexagon in current_black_hexagons:
            # Un hexagone noir est conservé s'il a un ou deux voisins noir
            if count in (1, 2):
                next_black_hexagons.add(hexagon)
        else:
            # Un hexagone blanc devient noir s'il a exactement 2 voisins noir
            if count == 2:
                next_black_hexagons.add(hexagon)

    return next_black_hexagons


for i in range(1, 101):
    black_hexagons = step(black_hexagons)
    print("Day {}: {}".format(i, len(black_hexagons)))
