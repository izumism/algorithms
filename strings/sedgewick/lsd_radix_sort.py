import alphabets


def counting_sort(target, r, key=lambda x: x):
    target_sz = len(target)
    count = [0] * r
    for elem in target:
        count[key(elem)] += 1
    for i in range(1, r):
        count[i] += count[i-1]
    result = [0] * target_sz
    for j in reversed(range(target_sz)):
        index = count[key(target[j])] - 1
        result[index] = target[j]
        count[key(target[j])] -= 1
    return result


def counting_sort_alphabets(alphs):
    index_arr = alphabets.alph2ids(alphs)
    r = alphabets.SIZE
    result = counting_sort(index_arr, r)
    return alphabets.ids2alph(result)


def lsd_radix_sort(strings, width):
    R = 26
    string_indices = [alphabets.alph2ids(string) for string in strings]
    for d in reversed(range(0, width)):
        string_indices = counting_sort(string_indices, R, lambda x: x[d])
    return [alphabets.ids2alph(ids) for ids in string_indices]
