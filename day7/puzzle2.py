import sys
import re

file_name = sys.argv[1]
input_file = open(file_name, "r")
programs = []


def parse_children(children_str):
    return children_str.replace(" -> ", "").split(", ")


def parse_program(line):
    line = line.rstrip()
    pattern = re.compile(r" \((\d+)\)")
    program = pattern.split(line)
    program[1] = int(program[1])
    program[2] = parse_children(program[2])
    return program


def fill_programs_from_file(input_file, programs):
    with input_file as fp:
        line = fp.readline()
        while line:
            programs.append(parse_program(line))
            line = fp.readline()


def find_root(programs):
    allnames = []
    names = []
    for program in programs:
        allnames.append(program[0])
        if program[2] != [""]:
            for sub in program[2]:
                names.append(sub)
    return list(set(allnames) - set(names))[0]


def find_program(name, programs):
    for program in programs:
        if program[0] == name:
            return program
    return -1


# find the only different num in list
def find_one_different(alist):
    pass
    diff = 0
    for i in range(1, len(alist)):
        if alist[0] != alist[i]:
            diff = alist[i]
            if alist.count(diff) == 1:
                return diff
    return alist[0]


# if balanced return True, if not False
def check_different_weight(tree_weight, program):
    if len(tree_weight) > 1 and len(tree_weight) == (len(program[2]) + 1):
        for i in range(2, len(tree_weight)):
            if tree_weight[1] != tree_weight[i]:
                different = find_one_different(tree_weight[1:])
                same = 0
                for anum in tree_weight[1:]:
                    if anum != different:
                        same = anum
                        break
                prog_to_adjust = find_program(program[2][tree_weight[1:].index(different)], programs)
                adjusted_weight = prog_to_adjust[1] + (same - different)
                print("weight of program %s must be %d" % (prog_to_adjust[0], adjusted_weight))
                return False
    return True


# get subtree weight
def get_subtree_weight(program):
    if len(program[2]) == 1 and program[2][0] == "":
        return program[1]
    else:
        tree_weight = [program[1]]
        for subprogname in program[2]:
            child_weight = get_subtree_weight(find_program(subprogname, programs))
            if child_weight == 0:
                return 0
            tree_weight.append(child_weight)
            # check if subtree is unbalanced - without this calculates whole tree weight
            if not check_different_weight(tree_weight, program):
                return 0
        return sum(tree_weight)


fill_programs_from_file(input_file, programs)
get_subtree_weight(find_program(find_root(programs), programs))
