import sort_data


def insertion_sort(arr, comp=lambda x, y: x < y):
    if len(arr) == 1:
        return arr
    for i in range(2, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and comp(key, arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


print(insertion_sort(sort_data.input))
