import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def convert_to_row_column(boarding_pass):
    raw_row, raw_column = boarding_pass[:-3], boarding_pass[-3:]
    row = int(raw_row.replace('B', '1').replace('F', '0'), base=2)
    column = int(raw_column.replace('R', '1').replace('L', '0'), base=2)
    return row, column


def seat_id(boarding_pass):
    row, column = convert_to_row_column(boarding_pass)
    return row * 8 + column


seat_ids = []
for line in lines:
    seat_ids.append(seat_id(line))

# Liste des seat_id dans l'ordre
seat_ids = sorted(seat_ids)
# Tous les seat_id possibles
all_seats = [x for x in range(seat_ids[0], seat_ids[-1] + 1)]

print(set(seat_ids) ^ set(all_seats))
