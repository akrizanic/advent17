from math import sqrt, floor, ceil


def create_fill_steps(size):
    position = [0, 0]
    positions = [[0, 0]]
    direction = -1
    num = 0
    i = 1
    s = 0

    if size == 1:
        return positions

    while True:
        direction = (direction + 1) % 4
        for j in range(1, i + 1):
            num += 1
            if direction == 0:
                position[0] += 1
            elif direction == 1:
                position[1] += 1
            elif direction == 2:
                position[0] -= 1
            elif direction == 3:
                position[1] -= 1
            positions.append([position[0], position[1]])
            if num >= size - 1:
                return positions

        i += s
        s = -s + 1


def calculate_last_step_distance(steps):
    last_step = steps[len(steps) - 1]
    return abs(last_step[0]) + abs(last_step[1])

def create_empty_array(size):
    a = ceil(sqrt(size)) + 2  # +2 so we never get "index out of range" on sums
    if a % 2 == 0:
        a += 1
    return [[0 for x in range(a)] for y in range(a)]


def fill_array(steps, arr):
    middle = floor(len(arr) / 2)
    i = 1
    for x in steps:
        arr[-x[1] + middle][x[0] + middle] = i
        i += 1


def fill_array_with_neighbour_sums_until_over(steps, arr):
    middle = floor(len(arr) / 2)
    first = True
    for x in steps:
        if first:
            arr[-x[1] + middle][x[0] + middle] = 1
            first = False
        else:
            # for this to work we need at least 1 empty cell on all sides
            sum_n = arr[-x[1] + middle - 1][x[0] + middle - 1] + \
                    arr[-x[1] + middle - 1][x[0] + middle] + \
                    arr[-x[1] + middle - 1][x[0] + middle + 1] + \
                    arr[-x[1] + middle][x[0] + middle - 1] + \
                    arr[-x[1] + middle][x[0] + middle + 1] + \
                    arr[-x[1] + middle + 1][x[0] + middle - 1] + \
                    arr[-x[1] + middle + 1][x[0] + middle] + \
                    arr[-x[1] + middle + 1][x[0] + middle + 1]
            arr[-x[1] + middle][x[0] + middle] = sum_n
            if sum_n > len(steps):
                return sum_n
    return -1
