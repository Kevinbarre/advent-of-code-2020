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
    floatings = []
    for i, bit in enumerate(mask):
        if bit == '0':
            continue
        elif bit == '1':
            v = set_bit(v, i, 1)
        else:
            # 'X', create floating bit
            floatings.append(i)
    results = [v]
    # Generate, for all floating bits, the two possibles new values for this bit
    for floating in floatings:
        results = [set_bit(result, floating, bit) for result in results for bit in (0, 1)]
    return results


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
        # On calcule les valeurs d'index en fonction du mask
        indexes = set_bits(index, current_mask)
        # On set la value à ces différentes positions en mémoire
        value = int(value)
        for index in indexes:
            memory[index] = value

print(sum(memory.values()))
