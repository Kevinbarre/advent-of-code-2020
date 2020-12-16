import copy
import sys

initial_seats = []
for line in sys.stdin:
    initial_seats.append([seat for seat in line.rstrip('\n')])

WIDTH = len(initial_seats[0])


def step(current_seats):
    next_seats = copy.deepcopy(current_seats)
    has_changed = False
    for i in range(len(current_seats)):
        for j in range(WIDTH):
            if current_seats[i][j] == 'L':
                if count_occupied(i, j, current_seats) == 0:
                    # Pas de siège occupé à côté, le siège devient occupé
                    next_seats[i][j] = '#'
                    has_changed = True
            elif current_seats[i][j] == '#':
                if count_occupied(i, j, current_seats) >= 5:
                    # Plus de 4 sièges occupés à côté, le siège devient vide
                    next_seats[i][j] = 'L'
                    has_changed = True
    return next_seats, has_changed


def count_occupied(i, j, seats):
    count = 0
    # Diagonale haut-gauche
    if check_seat_occupied(i, -1, j, -1, seats):
        count += 1
    # Au dessus
    if check_seat_occupied(i, -1, j, 0, seats):
        count += 1
    # Diagonale haut-droite
    if check_seat_occupied(i, -1, j, 1, seats):
        count += 1
    # A gauche
    if check_seat_occupied(i, 0, j, -1, seats):
        count += 1
    # A droite
    if check_seat_occupied(i, 0, j, 1, seats):
        count += 1
    # Diagonale bas gauche
    if check_seat_occupied(i, 1, j, -1, seats):
        count += 1
    # En dessous
    if check_seat_occupied(i, 1, j, 0, seats):
        count += 1
    # Diagonale bas droite
    if check_seat_occupied(i, 1, j, 1, seats):
        count += 1
    return count


def check_seat_occupied(i, i_step, j, j_step, seats):
    new_i = i + i_step
    new_j = j + j_step
    if new_i < 0 or new_j < 0:
        # Hors du tableau, siège non occupé
        return False
    try:
        seat = seats[new_i][new_j]
        if seat == '#':
            return True
        elif seat == '.':
            # On regarde le prochain siège dans cette direction
            return check_seat_occupied(new_i, i_step, new_j, j_step, seats)
    except IndexError:
        # Hors du tableau, siège non occupé
        return False


done = True
while done:
    #pprint(initial_seats)
    #print("================")
    initial_seats, done = step(initial_seats)

total = 0
for row in initial_seats:
    for seat in row:
        if seat == '#':
            total += 1

print(total)
