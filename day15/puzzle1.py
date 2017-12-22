import sys

prev_a = int(sys.argv[1])
prev_b = int(sys.argv[2])


def generator(factor, prev):
    return (factor * prev) % 2147483647


matches = 0
for i in range(40000000):
    prev_a = generator(16807, prev_a)
    prev_b = generator(48271, prev_b)
    if bin(prev_a)[-16:] == bin(prev_b)[-16:]:
        matches += 1


print(matches)
