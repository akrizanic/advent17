import sys
from copy import deepcopy


file_name = sys.argv[1]

input_file = open(file_name, "r")
line = input_file.readline()
banks_str = line.split()
banks = []
for bstr in banks_str:
    banks.append(int(bstr))


def balance(banks):
    most = max(banks)
    most_index = banks.index(most)
    banks[most_index] = 0
    for i in range(1, most + 1):
        banks[(most_index + i) % len(banks)] += 1


def reallocate(banks):
    log = [deepcopy(banks)]
    cycles = 0
    while True:
        balance(banks)
        cycles += 1
        if banks in log:
            return cycles
        log.append(deepcopy(banks))


print(reallocate(banks))
