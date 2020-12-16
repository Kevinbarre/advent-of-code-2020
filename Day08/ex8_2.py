import copy
import sys

input_instructions = []
for line in sys.stdin:
    input_instructions.append(line.rstrip('\n').split())


def run_instructions(instructions):
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
            return False
        elif current_instruction == len(instructions):
            # On a atteint la fin de la liste d'instructions, on remonte le résultat !
            return acc
        else:
            # On ajoute la nouvelle instruction à celles exécutées
            executed_instructions.add(current_instruction)


result = False
for i in range(len(input_instructions)):
    # Copie de la liste initiale
    tempered_instructions = copy.deepcopy(input_instructions)
    # On regarde l'élément à la position i
    action_i, _ = tempered_instructions[i]

    # print("Element à la position {} est: {}".format(i, action_i))

    if action_i == "acc":
        # Pas de modification des acc, on passe à la suite
        continue
    elif action_i == "jmp":
        # On change le jmp en nop
        tempered_instructions[i][0] = "nop"
    else:
        # On change le nop en jmp
        tempered_instructions[i][0] = "jmp"

    # print("Nouvelle liste d'instructions temporaire")
    # print(tempered_instructions)

    result = run_instructions(tempered_instructions)
    # print("Resultat de cette tentative: {}".format(result))
    # On teste de parcourir la liste d'instructions
    if result:
        # On a trouvé une configuration qui fonctionne
        print("En changeant la ligne {} ça marche !".format(i))
        break
    # Sinon on continue en modifiant l'instruction suivante

print(result)
