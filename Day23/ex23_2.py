# input_cups = "389125467"  # Example input
input_cups = "853192647"  # My input

NB_CUPS = 1000000
NB_MOVES = 10000000

input_cups = [int(c) for c in input_cups]

# Seconde liste qui contient la cup qui suit celle à la position i
# Par exemple pour l'input d'exemple et NB_CUPS = 2:
# On aura input_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7, 10, 11, 12]
#       et next_cups = [0, 2, 5, 8, 6, 4, 7, 10, 9, 1, 11, 12, 3]
# Car:
#     - La cup qui suit 1 est next_cups[1] = 2
#     - La cup qui suit 2 est next_cups[2] = 5
#     - La cup qui suit 3 est next_cups[3] = 8
#     - etc ...
next_cups = [0 for i in range(len(input_cups) + 1)]

# On alimente la cup suivante pour l'input sauf le dernier
for i in range(len(input_cups) - 1):
    next_cups[input_cups[i]] = input_cups[i + 1]

# Pour le dernier, on faire suivre sur la première cup ajoutée après l'input
next_cups[input_cups[-1]] = len(input_cups) + 1

# Pour toutes les autres cups ajoutées après l'input (sauf la toute dernière) on faire suivre sur la suivante
for i in range(len(input_cups) + 1, NB_CUPS):
    next_cups.append(i + 1)

# Enfin on fait boucler la toute dernière cup sur la première de l'input
next_cups.append(input_cups[0])

# On alimente l'input avec les cups suivantes
input_cups += [cup for cup in range(max(input_cups) + 1, NB_CUPS + 1)]


def move(current_label):
    global next_cups
    picked = [first := next_cups[current_label], second := next_cups[first], next_cups[second]]
    # print("Pick up: {}".format(", ".join(str(p) for p in picked)))

    # On recolle le current avec celui qui suivait le dernier picked
    next_cups[current_label] = next_cups[picked[-1]]

    destination = get_destination_cup(picked, current_label)
    # print("Destination: {}".format(destination))

    # On vient greffer les picked après la destination
    next_destination = next_cups[destination]
    next_cups[destination] = picked[0]
    next_cups[picked[-1]] = next_destination

    return next_cups[current_label]


def get_destination_cup(picked_cups, current_label):
    destination_label = get_destination_label(current_label)
    while destination_label in picked_cups:
        destination_label = get_destination_label(destination_label)
    return destination_label


def get_destination_label(current_label):
    destination_label = current_label - 1
    if destination_label == 0:
        destination_label = NB_CUPS
    return destination_label


current = input_cups[0]
for i in range(NB_MOVES):
    # print("-- Move {} --".format(i + 1))
    # print("Next Cups Before: {}".format(
    #     " ".join("({})".format(c) if c == current else "{}".format(c) for c in next_cups[1:])))
    # print("Cups: {}".format(" ".join("({})".format(c) if c == current_label else "{}".format(c) for c in cups)))
    current = move(current)

# print("-- Final --")
# print("Next Cups : {}".format(" ".join("({})".format(c) if c == current else "{}".format(c) for c in next_cups[1:])))

result = (next_one := next_cups[1]) * next_cups[next_one]
print("Result: {}".format(result))
