import sys
import operator


file_name = sys.argv[1]
input_file = open(file_name, "r")

registers = {}


def split_line(line):
    line = line.rstrip()
    line_split = line.split()
    return line_split


def reg_val(reg):
    val = registers.get(reg)
    if val is None:
        registers[reg] = 0
        return 0
    return val


def eval_cond(reg_name, op, val):
    rval = reg_val(reg_name)
    pval = int(val)
    if op == "==":
        if rval == pval:
            return True
    elif op == "<":
        if rval < pval:
            return True
    elif op == ">":
        if rval > pval:
            return True
    elif op == "<=":
        if rval <= pval:
            return True
    elif op == ">=":
        if rval >= pval:
            return True
    elif op == "!=":
        if rval != pval:
            return True
    return False


def exec_instr(instr_parts):
    sreg = instr_parts[0]
    if eval_cond(instr_parts[4], instr_parts[5], instr_parts[6]):
        reg_val(sreg)
        pval = int(instr_parts[2])
        if instr_parts[1] == "inc":
            registers[sreg] += pval
        elif instr_parts[1] == "dec":
            registers[sreg] -= pval
    return reg_val(sreg)


def eval_instrs_from_file(input_file):
    with input_file as fp:
        line = fp.readline()
        while line:
            instr_parts = split_line(line)
            exec_instr(instr_parts)
            line = fp.readline()


def find_dic_max_val(dic):
    return max(dic.items(), key=operator.itemgetter(1))[0]


eval_instrs_from_file(input_file)
print(registers[find_dic_max_val(registers)])
