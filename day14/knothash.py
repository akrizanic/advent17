def string_to_ascii_list(string):
    ascii_list = []
    for char in string:
        ascii_num = ord(char)
        ascii_list.append(ascii_num)
    return ascii_list


def reverse_sublist(circ_list, pos, length):
    subl = []
    fpos = pos
    circ_list_size = len(circ_list)
    for i in range(length):
        if fpos >= circ_list_size:
            fpos = 0
        subl.append(circ_list[fpos])
        fpos += 1
    subl.reverse()
    for sitem in subl:
        if pos >= circ_list_size:
            pos = 0
        circ_list[pos] = sitem
        pos += 1


def hk_round(circ_list, lengths, pos_skip):
    circ_list_len = len(circ_list)
    for length in lengths:
        if pos_skip[0] >= circ_list_len:
            pos_skip[0] = pos_skip[0] % circ_list_len
        reverse_sublist(circ_list, pos_skip[0], length)
        pos_skip[0] += length + pos_skip[1]
        pos_skip[1] += 1


def run_kh_rounds(num, lengths, circ_list):
    pos_skip = [0, 0]
    for i in range(0, num):
        hk_round(circ_list, lengths, pos_skip)


def do_xor_of_16(srclist):
    res = 0
    for i in srclist:
        res ^= i
    return res


def dense_from_sparse(srclist):
    dense = []
    for i in range(0, len(srclist), 16):
        part = do_xor_of_16(srclist[i:i + 16])
        dense.append(part)
    return dense


def hash_to_hex(hash):
    hex_hash = ""
    for p in hash:
        pstr = hex(p)[2:].zfill(2)
        # pstr = hex(p)[2:] #.zfill(2)
        hex_hash += pstr
    return hex_hash


def knothash(input):
    ascii_lens = string_to_ascii_list(input)
    ascii_lens += [17, 31, 73, 47, 23]
    circ_list = [i for i in range(256)]
    run_kh_rounds(64, ascii_lens, circ_list)
    dense_hash = dense_from_sparse(circ_list)
    hexh = hash_to_hex(dense_hash)
    return hexh
