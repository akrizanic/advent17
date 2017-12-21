import sys

file_name = sys.argv[1]

input_file = open(file_name, "r")

scanners = {}


def parse_line(line):
    if line == "":
        return
    tmp = line.split(": ")
    return [int(tmp[0]), int(tmp[1])]


with input_file as fp:
    line = fp.readline()
    while line:
        line = line.rstrip()
        pl = parse_line(line)
        scanners[pl[0]] = pl[1]
        line = fp.readline()


# returns 0 if 0, 1 if anything else
def wave_simple(step, rng):
    multi = 2 * (rng - 1)
    if step % multi == 0:
        return 0
    else:
        return 1


max_depth = max(scanners.keys()) + 1

caught = False
start = 1
while True:
    for i in range(max_depth):
        if i in scanners:
            pos = wave_simple(start + i, scanners[i])
            if pos == 0:
                caught = True
                break
    if not caught:
        print(start)
        break
    start += 1
    caught = False
