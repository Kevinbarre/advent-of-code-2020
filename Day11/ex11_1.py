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
                if count_occupied(i, j, current_seats) >= 4:
                    # Plus de 4 sièges occupés à côté, le siège devient vide
                    next_seats[i][j] = 'L'
                    has_changed = True
    return next_seats, has_changed


def count_occupied(i, j, seats):
    count = 0
    # Diagonale haut-gauche
    if check_seat_occupied(i - 1, j - 1, seats):
        count += 1
    # Au dessus
    if check_seat_occupied(i - 1, j, seats):
        count += 1
    # Diagonale haut-droite
    if check_seat_occupied(i - 1, j + 1, seats):
        count += 1
    # A gauche
    if check_seat_occupied(i, j - 1, seats):
        count += 1
    # A droite
    if check_seat_occupied(i, j + 1, seats):
        count += 1
    # Diagonale bas gauche
    if check_seat_occupied(i + 1, j - 1, seats):
        count += 1
    # En dessous
    if check_seat_occupied(i + 1, j, seats):
        count += 1
    # Diagonale bas droite
    if check_seat_occupied(i + 1, j + 1, seats):
        count += 1
    return count


def check_seat_occupied(i, j, seats):
    if i < 0 or j < 0:
        # Hors du tableau, siège non occupé
        return False
    try:
        seat = seats[i][j]
        if seat == '#':
            return True
        else:
            return False
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