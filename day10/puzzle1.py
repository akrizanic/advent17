import sys

file_name = sys.argv[1]

input_file = open(file_name, "r")
line_str = input_file.readline()
line_str = line_str.rstrip()

lenghts = line_str.split(",")
lenghts = list(map(int, lenghts))


def reverse_sublist(circ_list, pos, length):
    subl = []
    fpos = pos
    circ_list_size = len(circ_list)
    for i in range(length):
        if fpos >= circ_list_size:
            fpos = 0
        subl.append(circ_list[fpos])
        fpos += 1
    subl.reverse()
    for sitem in subl:
        if pos >= circ_list_size:
            pos = 0
        circ_list[pos] = sitem
        pos += 1


def hk_round(circ_list, lengths, pos_skip):
    circ_list_len = len(circ_list)
    for length in lengths:
        if pos_skip[0] >= circ_list_len:
            pos_skip[0] = pos_skip[0] % circ_list_len
        reverse_sublist(circ_list, pos_skip[0], length)
        pos_skip[0] += length + pos_skip[1]
        pos_skip[1] += 1


circ_list = [i for i in range(256)]
pos_skip = [0, 0]
hk_round(circ_list, lenghts, pos_skip)
print(circ_list[0] * circ_list[1])
