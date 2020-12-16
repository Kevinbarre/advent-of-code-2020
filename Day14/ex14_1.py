import re
import sys

instructions = []
for line in sys.stdin:
    instructions.append(line.rstrip('\n').split(' = '))


def set_bit(v, index, x):
    """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
    mask = 1 << index  # Compute mask, an integer with just bit 'index' set.
    v &= ~mask  # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask  # If x was True, set the bit indicated by the mask.
    return v  # Return the result, we're done.


def set_bits(v, mask):
    for i, bit in enumerate(mask):
        if bit == 'X':
            continue
        v = set_bit(v, i, int(bit))
    return v


# print(instructions)
memory = {}

current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

for instruction in instructions:
    operation, value = instruction
    if operation == 'mask':
        # On met à jour le mask, en inversant l'ordre des bits
        current_mask = value[::-1]
    else:
        # On récupère l'index en mémoire
        index = int(re.search(r'\[([A-Za-z0-9_]+)]', operation).group(1))
        # On calcule la valeur en fonction du mask
        value = set_bits(int(value), current_mask)
        # On la set en mémoire
        memory[index] = value

print(sum(memory.values()))
