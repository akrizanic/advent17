import sys
from copy import deepcopy


file_name = sys.argv[1]

input_file = open(file_name, "r")
line = input_file.readline()
banks_str = line.split()
banks = []
for bstr in banks_str:
    banks.append(int(bstr))


def better_better_distance_between_same(banks, log):
    try:
        indexb = log.index(banks)
        return len(log) - indexb
    except ValueError:
        return -1


def balance(banks):
    most = max(banks)
    most_index = banks.index(most)
    banks[most_index] = 0
    for i in range(1, most + 1):
        banks[(most_index + i) % len(banks)] += 1


def reallocate(banks):
    log = [deepcopy(banks)]
    while True:
        balance(banks)
        distance = better_better_distance_between_same(banks, log)
        if distance > 0:
            return distance
        log.append(deepcopy(banks))


print(reallocate(banks))
