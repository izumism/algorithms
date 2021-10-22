def selection_sort(arr):
    for i in range(0, len(arr)):
        j = min_index(arr, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def min_index(arr, start):
    if start >= len(arr)-1:
        return start
    result = start
    curr_min = arr[start]
    for i in range(start+1, len(arr)):
        if arr[i] < curr_min:
            curr_min = arr[i]
            result = i
    return result
