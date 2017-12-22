import sys
from knothash import knothash


pinput = sys.argv[1]


def hex_digit_to_bits(inp):
    scale = 16
    num_of_bits = 4
    return bin(int(inp, scale))[2:].zfill(num_of_bits)


def hex_string_to_bits(input):
    out = ""
    for i in input:
        out += hex_digit_to_bits(i)
    return out


grid = ""
for i in range(128):
    grid += hex_string_to_bits(knothash(pinput + "-" + str(i)))

print(grid.count("1"))
