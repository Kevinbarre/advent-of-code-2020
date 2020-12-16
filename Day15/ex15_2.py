import re
import sys

starting_numbers = map(int, input().split(','))

# Map des nombres déjà dit, avec en valeur le dernier tour auquel ils ont été dit
spoken_numbers = {}

turn = 1
# On initialise avec les starting numbers
for starting_number in starting_numbers:
    # print("Turn {}, number: {}".format(turn, starting_number))
    spoken_numbers[starting_number] = turn
    turn += 1

current_number = 0
# On joue ensuite jusqu'au tour 2020
while turn < 30000000:
    if current_number in spoken_numbers:
        # Nombre déjà dit, le prochain nombre sera la différence entre ce tour et la précédente fois que le nombre avait été dit
        next_number = turn - spoken_numbers[current_number]
    else:
        # Nouveau nombre, le prochain sera 0
        next_number = 0
    # On met à jour le tour où on a dit le nombre courant
    # print("Turn {}, number: {}".format(turn, current_number))
    spoken_numbers[current_number] = turn
    # Le next number devient le current
    current_number = next_number
    turn += 1

# Le nombre du 30000000ème tour est
print(current_number)