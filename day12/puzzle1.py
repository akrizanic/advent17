import sys

file_name = sys.argv[1]

input_file = open(file_name, "r")

conns = {}


def parse_line(line):
    if line == "":
        return
    tmp = line.split(" <-> ")
    tmp_list = tmp[1].split(", ")
    tmp_list = list(map(int, tmp_list))
    return [int(tmp[0]), tmp_list]


with input_file as fp:
    line = fp.readline()
    while line:
        line = line.rstrip()
        pl = parse_line(line)
        conns[pl[0]] = pl[1]
        line = fp.readline()


conn_to_num = set()


def find_connected(num):
    conn_to_num.add(num)
    conn = conns.get(num)
    for c in conn:
        if c not in conn_to_num:
            find_connected(c)


find_connected(0)
print(len(conn_to_num))
