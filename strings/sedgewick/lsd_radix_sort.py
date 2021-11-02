import alphabets


def counting_sort(indices, r, key=lambda x: x):
    target_sz = len(indices)
    count = [0] * r
    for elem in indices:
        count[key(elem)] += 1
    for i in range(1, r):
        count[i] += count[i-1]
    result = [0] * target_sz
    for j in reversed(range(target_sz)):
        index = count[key(indices[j])] - 1
        result[index] = indices[j]
        count[key(indices[j])] -= 1
    return result


def counting_sort_alphabets(alphs):
    index_arr = alphabets.alph2ids(alphs)
    r = alphabets.SIZE
    result = counting_sort(index_arr, r)
    return alphabets.ids2alph(result)


def radix_sort(indices_list, width, r):
    result = indices_list
    for i in reversed(range(0, width)):
        result = counting_sort(result, r, lambda x: x[i])
    return result


def lsd_radix_sort(strings, width):
    R = alphabets.SIZE
    string_indices = [alphabets.alph2ids(string) for string in strings]
    result = radix_sort(string_indices, width, R)
    return [alphabets.ids2alph(ids) for ids in result]
