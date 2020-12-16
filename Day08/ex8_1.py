import sys

instructions = []
for line in sys.stdin:
    instructions.append(line.rstrip('\n').split())

current_instruction = 0
acc = 0
executed_instructions = {current_instruction}

while True:
    # On regarde l'instruction courrante
    instruction = instructions[current_instruction]
    action, value = instruction[0], int(instruction[1])

    if action == "acc":
        # On modifie l'accumulator
        acc += value
        # On passe à l'instruction suivante:
        current_instruction += 1
    elif action == "jmp":
        # On passe à l'instruction demandée
        current_instruction += value
    else:
        # Nop, on passe à l'instruction suivante
        current_instruction += 1

    if current_instruction in executed_instructions:
        # On a déjà exécuté la prochaine instruction, on s'arrête!
        break
    else:
        # On ajoute la nouvelle instruction à celles exécutées
        executed_instructions.add(current_instruction)

print(acc)
