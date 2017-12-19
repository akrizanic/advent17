import sys

file_name = sys.argv[1]
input_file = open(file_name, "r")

str_line = input_file.readline()
str_line = str_line.rstrip()
dirs = str_line.split(",")

# in order
all_dirs = ["n", "ne", "se", "s", "sw", "nw"]
dirs_list = {}


def dirs_add(dirs_list, d, val):
    td = dirs_list.get(d)
    if td is None:
        dirs_list[d] = 0
    dirs_list[d] += val


def dirs_get(dirs_list, d):
    if dirs_list.get(d) is None:
        dirs_add(dirs_list, d, 0)
    return dirs_list.get(d)


def distance(dirs_list, all_dirs):
    while True:
        done = 0
        for i in range(len(all_dirs)):
            d1 = all_dirs[i]
            d3 = all_dirs[(i + 2) % len(all_dirs)]
            d2 = all_dirs[(i + 1) % len(all_dirs)]

            same = min(dirs_get(dirs_list, d1), dirs_get(dirs_list, d3))
            dirs_add(dirs_list, d1, -same)
            dirs_add(dirs_list, d3, -same)
            dirs_add(dirs_list, d2, same)

            if same == 0:
                done += 1
        if done == len(all_dirs):
            break
    return sum(dirs_list.values())


max_dist = 0
for d in dirs:
    dirs_add(dirs_list, d, 1)
    dist = distance(dirs_list, all_dirs)
    if dist > max_dist:
        max_dist = dist


print(max_dist)
