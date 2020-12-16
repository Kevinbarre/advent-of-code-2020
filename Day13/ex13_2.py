import math

_ = input()
buses_with_i = [(-i, int(bus)) for i, bus in enumerate(input().split(',')) if bus != 'x']
buses = [bus for _, bus in buses_with_i]

n = math.prod(buses)


def get_ei(the_bus, other_buses):
    ni = int(n / the_bus)
    ei = ni
    while not(ei % the_bus == 1 and all(ei % other_bus == 0 for other_bus in other_buses)):
        #print("The bus: {}, ei: {}".format(the_bus, ei))
        ei += ni
    return ei


all_ei = {}
for i, bus in enumerate(buses):
    remaining_buses = buses[:]
    remaining_buses.pop(i)
    # print(remaining_buses)
    all_ei[bus] = get_ei(bus, remaining_buses)

# print(all_ei)
result = sum(i * all_ei[bus] for i, bus in buses_with_i) % n
#print("N: {}".format(n))
print("Result: {}".format(result))