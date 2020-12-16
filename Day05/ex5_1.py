import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def convert_to_row_column(boarding_pass):
    raw_row, raw_column = boarding_pass[:-3], boarding_pass[-3:]
    row = int(raw_row.replace('B', '1').replace('F', '0'), base=2)
    column = int(raw_column.replace('R', '1').replace('L', '0'), base=2)
    return(row, column)


def seat_id(boarding_pass):
    row, column = convert_to_row_column(boarding_pass)
    return row * 8 + column

max_seat_id = 0
for line in lines:
    max_seat_id = max(max_seat_id, seat_id(line))

print(max_seat_id)


