input_file = open("i1.txt", "r")


def find_num_steps(input_file):
    instrs = []
    with input_file as fp:
        line = fp.readline()
        while line:
            instrs.append(int(line.rstrip()))
            line = fp.readline()
    return jumper(instrs)


def jumper(instrs):
    position = 0
    jumps = 0
    while True:
        if position < 0 or position > (len(instrs) -1):
            break
        else:
            nextin = instrs[position]
        instrs[position] += 1
        position += nextin
        jumps += 1
    return jumps


print(find_num_steps(input_file))
