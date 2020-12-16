earliest = int(input())
buses = [int(bus) for bus in filter(lambda bus: bus != 'x', input().split(','))]

minimum = 99999999999999999999999999
good_bus = None

for bus in buses:
    minutes = bus - (earliest % bus)
    if minutes < minimum:
        minimum = minutes
        good_bus = bus

print(good_bus * minimum)
