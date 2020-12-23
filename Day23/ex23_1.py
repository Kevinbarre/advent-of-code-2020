# input_cups = "389125467"  # Example input
input_cups = "853192647"  # My input

NB_CUPS = len(input_cups)
NB_MOVES = 100


def move(cups, current):
    current_label = cups[current]
    print("Cups: {}".format(" ".join("({})".format(c) if c == current_label else "{}".format(c) for c in cups)))

    picked, remaining = picks_up(cups, current)
    print("Pick up: {}".format(", ".join(picked)))

    destination = get_destination_cup(remaining, current_label)
    print("Destination: {}".format(destination))

    destination_index = remaining.index(destination)
    next_cups = remaining[:destination_index + 1] + picked + remaining[destination_index + 1:]
    next_current_index = next_cups.index(current_label) + 1
    if next_current_index == NB_CUPS:
        next_current_index = 0
    return next_cups, next_current_index


def picks_up(cups, current):
    if current < NB_CUPS - 3:
        picked = cups[current + 1:current + 4]
        remaining = cups[:current + 1] + cups[current + 4:]
    elif current == NB_CUPS - 3:
        picked = cups[-2:] + cups[:1]
        remaining = cups[1:-2]
    elif current == NB_CUPS - 2:
        picked = cups[-1:] + cups[:2]
        remaining = cups[2:-1]
    else:
        picked = cups[:3]
        remaining = cups[3:]
    # print("Cups", cups)
    # print("Picked", picked)
    # print("Remaining", remaining)
    return picked, remaining


def get_destination_cup(remaining_cups, current_label):
    destination_label = get_destination_label(current_label)
    while destination_label not in remaining_cups:
        destination_label = get_destination_label(destination_label)
    return destination_label


def get_destination_label(current_label):
    destination_label = str(int(current_label) - 1)
    if destination_label == "0":
        destination_label = str(NB_CUPS)
    return destination_label


current_index = 0
for i in range(NB_MOVES):
    print("-- Move {} --".format(i + 1))
    input_cups, current_index = move(input_cups, current_index)

print("-- Final --")
print("Cups: {}".format(
    " ".join("({})".format(c) if i == current_index else "{}".format(c) for i, c in enumerate(input_cups))))

index_one = input_cups.index("1")
print("Result: {}".format(input_cups[index_one + 1:] + input_cups[:index_one]))
