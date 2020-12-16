import sys

instructions = []
for line in sys.stdin:
    line = line.rstrip('\n')
    instructions.append((line[0], int(line[1:])))

# print(instructions)
DIRECTIONS = ['E', 'N', 'W', 'S']
# Starting coordinates
x, y, facing = 0, 0, 0


def process(old_x, old_y, old_facing, instruction):
    action, value = instruction

    if action == 'N':
        # Move top
        old_y += value
    elif action == 'S':
        # Move down
        old_y -= value
    elif action == 'E':
        # Move right
        old_x += value
    elif action == 'W':
        # Move left
        old_x -= value
    elif action == 'L':
        # Rotate left
        old_facing = rotate(old_facing, value)
    elif action == 'R':
        # Rotate right
        old_facing = rotate(old_facing, -value)
    elif action == 'F':
        # Move forward
        new_instruction = (DIRECTIONS[old_facing], value)
        return process(old_x, old_y, old_facing, new_instruction)
    return old_x, old_y, old_facing


def rotate(old_facing, value):
    index_increment = int(value / 90)
    return (old_facing + index_increment) % 4


for instruction in instructions:
    x, y, facing = process(x, y, facing, instruction)

print(abs(x) + abs(y))
