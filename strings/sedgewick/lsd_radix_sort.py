from key_indexed_counting import ALPHA2INDEX


def lsd_radix_sort(strings, width):
    R = 26
    strings_num = len(strings)
    result = [0] * strings_num
    for d in reversed(range(0, width)):
        count = [0] * (R + 1)
        for string in strings:
            count[ALPHA2INDEX[string[d]] + 1] += 1
        for r in range(R):
            count[r+1] += count[r]
        for string in strings:
            result[count[ALPHA2INDEX[string[d]]]] = string
            count[ALPHA2INDEX[string[d]]] += 1
    return result
