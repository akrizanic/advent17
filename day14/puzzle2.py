import sys
from knothash import knothash


pinput = sys.argv[1]


def hex_digit_to_bits(inp):
    return bin(int(inp, 16))[2:].zfill(4)


def hex_string_to_bits(input):
    out = ""
    for i in input:
        out += hex_digit_to_bits(i)
    return out


grid = []
for i in range(128):
    grid.append(hex_string_to_bits(knothash(pinput + "-" + str(i))))


regions = []


def is_in_regions(position):
    for r in regions:
        if position in r:
            return True
    return False


def check_neighbours(position, done):
    neigh_poss = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    neighs = []
    done.append(position)
    if position[1] == 0:
        neigh_poss.remove([0, -1])
    if position[0] == 0:
        neigh_poss.remove([-1, 0])
    if position[1] == 127:
        neigh_poss.remove([0, 1])
    if position[0] == 127:
        neigh_poss.remove([1, 0])

    for p in neigh_poss:
        px = position[1] + p[1]
        py = position[0] + p[0]
        if grid[py][px] == "1":
                if not [py, px] in neighs and not [py, px] in done:
                    neighs.append([py, px])

    for n in neighs:
        if n not in done:
            check_neighbours(n, done)


def find_regions():
    num_regions = 0
    for y in range(128):
        for x in range(128):
            if not is_in_regions([y, x]):
                if grid[y][x] == "1":
                    done = []
                    check_neighbours([y, x], done)
                    regions.append(done)
                    num_regions += 1
    return num_regions


print(find_regions())
