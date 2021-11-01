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
