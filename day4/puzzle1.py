inputFile = open("i1.txt", "r")


def same_word_in_list(str_list):
    if len(str_list) == 0:
        return False
    for i in range(0, len(str_list)):
        for j in range(i + 1, len(str_list)):
            if str_list[i] == str_list[j]:
                return True
    return False


def find_valid_in_file(inputFile):
    valid = 0
    with inputFile as fp:
        line = fp.readline()
        while line:
            str_list = (line.rstrip()).split()
            if not same_word_in_list(str_list):
                valid += 1
            line = fp.readline()
    return valid


print(find_valid_in_file(inputFile))
