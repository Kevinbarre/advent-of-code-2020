import sys
from collections import Counter

instructions = []
for line in sys.stdin:
    instructions.append(line.rstrip('\n'))


class Hexagon:
    """
    Implement cube coordinates from https://math.stackexchange.com/questions/2254655/hexagon-grid-coordinate-system
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

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
print(sum(1 for _, v in counter.items() if v % 2 == 1))
