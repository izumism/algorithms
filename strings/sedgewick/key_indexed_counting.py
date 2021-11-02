from alphabets import ALPH2INDEX


def key_indexed_counting(string):
    count_sz = len(ALPH2INDEX)
    count = [0] * (count_sz + 1)
    for ch in string:
        count[ALPH2INDEX[ch]+1] += 1
    for i in range(count_sz-1):
        count[i+1] += count[i]
    str_len = len(string)
    result = [0] * str_len
    for ch in string:
        result[count[ALPH2INDEX[ch]]] = ch
        count[ALPH2INDEX[ch]] += 1
    return result
