ALPHA2INDEX = {chr(ord('a')+i): i for i in range(26)}
INDEX2ALPHA = {i: ch for ch, i in ALPHA2INDEX.items()}


def create_alpha_2_index(charset):
    return {char: i for i, char in enumerate(sorted(set(charset)))}


def key_indexed_counting(string):
    alpha2index = create_alpha_2_index(string)
    count_sz = len(alpha2index)
    count = [0] * (count_sz + 1)
    for ch in string:
        count[alpha2index[ch]+1] += 1
    for i in range(count_sz-1):
        count[i+1] += count[i]
    str_len = len(string)
    result = [0] * str_len
    for ch in string:
        result[count[alpha2index[ch]]] = ch
        count[alpha2index[ch]] += 1
    return result
