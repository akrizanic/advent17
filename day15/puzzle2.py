import sys

prev_a = int(sys.argv[1])
prev_b = int(sys.argv[2])


def generator(factor, prev):
    return (factor * prev) % 2147483647


matches = 0
comps = 0
numa = numb = 0
while True:
    if not numa:
        prev_a = generator(16807, prev_a)
        if prev_a % 4 == 0:
            numa = prev_a
            got_a = True
    if not numb:
        prev_b = generator(48271, prev_b)
        if prev_b % 8 == 0:
            numb = prev_b
            got_b = True
    if numa and numb:
        comps += 1
        if bin(numa)[-16:] == bin(numb)[-16:]:
            matches += 1
        numa = numb = 0
    if comps >= 5000000:
        break

print(matches)
