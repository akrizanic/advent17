#!/usr/bin/python3

input_file = open("i1.txt", "r")


def checksum(file):
    chksum = 0
    with file as fp:
        line = fp.readline()
        while line:
            row = list(map(int, line.split()))
            nmin = min(row)
            nmax = max(row)
            chksum = chksum + (nmax - nmin)
            line = fp.readline()
    return chksum


print(checksum(input_file))
