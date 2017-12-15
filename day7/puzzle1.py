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


fill_programs_from_file(input_file, programs)
print(find_root(programs))
