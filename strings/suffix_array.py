def suffixes_lexicographic_order(string):
    suffixes = []
    for i in range(len(string)):
        suffixes.append(string[i:])
    return sorted(suffixes)


DOLLAR = '$'


def suffix_array(string) -> [int]:
    if string[-1] != DOLLAR:
        raise RuntimeError(
            f"input must ends with '$' character, given={string}")
    suff_pos = {}
    for pos in range(len(string)):
        suff_pos[string[pos:]] = pos
    return [
        pos for (suff, pos) in sorted(suff_pos.items(), key=lambda x: x[0])
    ]


def get_cyclic_order_index(string, length) -> [int]:
    result = {}
    source_len = len(string)
    for pos in range(source_len):
        start = pos
        end = start + length
        if end >= source_len:
            cyclic_substr = string[start:] + string[:end % source_len]
            result[pos] = cyclic_substr
        else:
            cyclic_substr = string[start:end]
            result[pos] = cyclic_substr
    return [
        pos for (pos, substr) in sorted(result.items(), key=lambda x: x[1])
    ]


def construct_suffix_array(string) -> [int]:
    curr_len = 1
    string_len = len(string)
    prev_arr = get_cyclic_order_index(string, curr_len)
    while True:
        # assert curr_len <= string_len, 'implementation error'
        curr_len *= 2
        curr_arr = get_cyclic_order_index(string, curr_len)
        if curr_arr == prev_arr:
            return prev_arr
        prev_arr = curr_arr
    assert False, 'this function returns in while loop'
