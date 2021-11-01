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


def cyclic_shift(string, start, length):
    str_len = len(string)
    end = start + length
    if end >= str_len:
        return string[start:] + string[:end % str_len]
    else:
        return string[start:end]


def get_cyclic_order_index(string, length) -> [int]:
    result = {}
    source_len = len(string)
    for pos in range(source_len):
        result[pos] = cyclic_shift(string, pos, length)
    return [
        pos for (pos, substr) in sorted(result.items(), key=lambda x: x[1])
    ]


def construct_suffix_array(string) -> [int]:
    curr_len = 1
    string_len = len(string)
    prev_arr = get_cyclic_order_index(string, curr_len)
    while True:
        assert curr_len <= string_len, 'implementation error'
        curr_len *= 2
        curr_arr = get_cyclic_order_index(string, curr_len)
        if curr_arr == prev_arr:
            return prev_arr
        prev_arr = curr_arr
    assert False, 'this function returns in while loop'


ALPH_FIRST = 'a'
ALPH_SIZE = 27
ALPH2ID = {chr(ord(ALPH_FIRST)+i): i+1 for i in range(ALPH_SIZE)}
ALPH2ID['$'] = 0
ID2ALPH = {i: ch for ch, i in ALPH2ID.items()}


def counting_sort(string) -> [int]:
    count = [0] * ALPH_SIZE
    # frequency
    for ch in string:
        count[ALPH2ID[ch]] = count[ALPH2ID[ch]] + 1
    # count[i] represents the number of corresponding alphabet
    # which input 'string' has.
    for i in range(1, ALPH_SIZE):
        count[i] = count[i] + count[i-1]
    # count[i] represents that input 'string' holds the number of alphebet
    # less than ID2ALPH[i]
    order = [0] * len(string)
    for i in reversed(range(0, len(string))):
        ch = string[i]
        ch_id = ALPH2ID[ch]
        count[ch_id] = count[ch_id] - 1
        order[count[ch_id]] = i
    return order


def compute_class(string, order) -> [int]:
    class_arr = [0] * len(string)
    assert len(order) == len(class_arr)
    input_len = len(string)
    for i in range(1, input_len):
        if string[order[i]] != string[order[-i]]:
            class_arr[order[i]] = class_arr[order[i-1]] + 1
        else:
            class_arr[order[i]] = class_arr[order[i-1]]
    return class_arr
    """
    for o in order:
        id = ALPH2ID[string[o]]
        class_arr[o] = id
    return class_arr
    """


def shift_util(string, length):
    def ci(start):
        return cyclic_shift(string, start, length)

    def ci_prime(start):
        return (ci(start), ci(start+length))

    return (ci, ci_prime)

