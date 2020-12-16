import sys

instructions = []
for line in sys.stdin:
    line = line.rstrip('\n')
    instructions.append((line[0], int(line[1:])))

# Starting coordinates
x, y = 0, 0
# Starting waypoint
w_x, w_y = 10, 1


def process(old_x, old_y, old_w_x, old_w_y, instruction):
    action, value = instruction

    if action == 'N':
        # Move waypoint top
        old_w_y += value
    elif action == 'S':
        # Move waypoint down
        old_w_y -= value
    elif action == 'E':
        # Move waypoint right
        old_w_x += value
    elif action == 'W':
        # Move waypoint left
        old_w_x -= value
    elif action == 'L':
        # Rotate waypoint left
        old_w_x, old_w_y = rotate(old_w_x, old_w_y, value)
    elif action == 'R':
        # Rotate waypoint right
        old_w_x, old_w_y = rotate(old_w_x, old_w_y, -value)
    elif action == 'F':
        # Move forward to the waypoint number of time
        old_x += old_w_x * value
        old_y += old_w_y * value
    return old_x, old_y, old_w_x, old_w_y


def rotate(old_w_x, old_w_y, value):
    rotation = int(value / 90) % 4
    if rotation == 0:
        # Le waypoint ne bouge pas
        return old_w_x, old_w_y
    elif rotation == 1:
        # Le waypoint a tourné d'un quart de tour à gauche
        return -old_w_y, old_w_x
    elif rotation == 2:
        # Le waypoint a fait demi-tour
        return -old_w_x, -old_w_y
    else:
        # Le waypoint a tourné d'un quart de tour à droite
        return old_w_y, -old_w_x


for instruction in instructions:
    x, y, w_x, w_y = process(x, y, w_x, w_y, instruction)

print(abs(x) + abs(y))
