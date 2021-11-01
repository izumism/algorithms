def suffixes_lexicographic_order(string):
    suffixes = []
    for i in range(len(string)):
        suffixes.append(string[i:])
    return sorted(suffixes)


DOLLAR = '$'


def sublist_to_dollar(string: str) -> str:
    for i in range(len(string)):
        if string[i] == DOLLAR:
            return string[:i+1]
    assert False, 'string must include "$", string: {0}'.format(string)
    return string


def suffix_array(string) -> [int]:
    suff_pos = {}
    for pos in range(len(string)):
        suff_pos[string[pos:]] = pos
    return [
        pos for (suff, pos) in sorted(suff_pos.items(), key=lambda x: x[0])
    ]
