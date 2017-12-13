inputFile = open("i2.txt", "r")


# also returns true if same word
def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    if w1 == w2:
        return True

    to_match = len(w1)
    matched = []
    for i in range(0, to_match):
        for j in range(0, to_match):
            if j not in matched:
                if w1[i] == w2[j]:
                    matched.append(j)
                    break

    if len(matched) == to_match:
        return True
    return False


def contains_same_word_or_anagram(str_list):
    if len(str_list) == 0:
        return False
    for i in range(0, len(str_list)):
        for j in range(i + 1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                return True
    return False


def find_valid_in_file(inputFile):
    valid = 0
    with inputFile as fp:
        line = fp.readline()
        while line:
            str_list = (line.rstrip()).split()
            if not contains_same_word_or_anagram(str_list):
                valid += 1
            line = fp.readline()
    return valid


print(find_valid_in_file(inputFile))
