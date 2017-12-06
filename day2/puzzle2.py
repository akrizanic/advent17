#!/usr/bin/python3

input_file = open("i2.txt", "r")


def find_divisible(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            div = nums[i] / nums[j]
            if div.is_integer():
                return div


def divisions_sum(file):
    div_sums = 0
    with file as fp:
        line = fp.readline()
        while line:
            row = list(map(int, line.split()))
            row.sort(reverse=True)
            div_sums = div_sums + find_divisible(row)
            line = fp.readline()
    return int(div_sums)


print(divisions_sum(input_file))
