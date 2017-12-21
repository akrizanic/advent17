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


def wave(dpth, rng):
    rev = False
    pos = 0
    for i in range(dpth):
        if pos >= rng - 1:
            rev = True
        elif pos <= 0:
            rev = False
        if not rev:
            pos += 1
        else:
            pos -= 1
    return pos


max_depth = max(scanners.keys()) + 1

severity = 0
for i in range(max_depth):
    if i in scanners:
        if wave(i, scanners[i]) == 0:
            severity += i * scanners[i]

print(severity)
