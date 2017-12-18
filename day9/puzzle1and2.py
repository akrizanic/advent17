import sys

file_name = sys.argv[1]
input_file = open(file_name, "r")
input_str = input_file.readline()


i = 0
lvl = 0
lvl_sum = 0
garbage = False
garbage_chars = 0
while i < len(input_str):
    char = input_str[i]
    i += 1
    if char == "!":
        i += 1
        continue

    if not garbage and char == "<":
        garbage = True
        continue
    elif char == ">":
        garbage = False
        continue

    if not garbage:
        if char == "{":
            lvl += 1
        elif char == "}":
            lvl_sum += lvl
            lvl -= 1
    else:
        garbage_chars += 1

print("score: %d" % lvl_sum)
print("garbage: %d" % garbage_chars)
