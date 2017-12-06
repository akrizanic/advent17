#!/usr/bin/python3

inputFile = open("i1.txt", "r")
input = inputFile.readline().rstrip()


def captcha(input):
    sum = 0
    for i in range(0, len(input)):
        match_pos = i + 1
        if input[i] == input[match_pos % len(input)]:
            sum += int(input[i])
    return sum


sum = captcha(input)
print("sum = " + str(sum))
