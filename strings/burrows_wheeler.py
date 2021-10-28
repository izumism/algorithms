"""Implementation for pattern matching using Burrows-Wheeler transform.

Target -> Burrows-Wheeler transform -> Run-Length encocing
"""


class RLItem:
    def __init__(self):
        self.length_char = []

    def append(self, length, char):
        self.length_char.append((length, char))

    def as_encoding(self):
        return ''.join([
            str(length) + char for length, char in self.length_char])

    def as_decoding(self):
        return ''.join([
            char * length for length, char in self.length_char])


def parse2run_length(text: str) -> RLItem:
    if not text:
        return ''
    head_i = 0
    head_c = text[0]
    result = RLItem()
    curr_i = -1
    curr_c = ''
    for i in range(1, len(text)):
        curr_i = i
        curr_c = text[i]
        if head_c == curr_c:
            continue
        else:
            length = curr_i - head_i
            result.append(length, head_c)
            head_i = curr_i
            head_c = curr_c
    result.append(len(text)-head_i, curr_c)
    return result


def run_length_encoding(text: str) -> str:
    items = parse2run_length(text)
    return items.as_encoding()


class BWItem:
    def __init__(self):
        self.before_after = []

    def append(self, before, after):
        self.before_after.append((before, after))

    def as_encoding(self):
        return ''.join([after for before, after in self.before_after])


def get_cyclic_matrix(text):
    target = text + '$'
    return get_cyclic_matrix_plain(target)


def get_cyclic_matrix_plain(text):
    length = len(text)
    cycles = [text[i:length] + text[0:i] for i in range(len(text))]
    return cycles


# Memory: O(|TEXT|), Time: O(N*log(N))
def burrows_wheeler_transform(text: str) -> BWItem:
    cycles = get_cyclic_matrix(text)
    result = BWItem()
    for cycle in sorted(cycles):
        result.append(cycle[0], cycle[-1])
    return result


def burrows_wheeler_encoding(text: str) -> str:
    parsed = burrows_wheeler_transform(text)
    return parsed.as_encoding()


def sort_by_first(rows):
    return sorted(rows, key=lambda row: row[0])


# Memory inefficient
def burrows_wheeler_decoding_bad(bw_code):
    matrix = [[e] for e in sorted(bw_code)]
    for _ in range(len(bw_code)-1):
        matrix = sort_by_first([[bw, *me] for bw, me in zip(bw_code, matrix)])
    return ''.join(matrix[0])[1:]


IndexedChar = (str, int)


def decorate_index(bw_code: str) -> [IndexedChar]:
    counter = {}
    result = []
    for ch in bw_code:
        if ch in counter:
            counter[ch] += 1
        else:
            counter[ch] = 0
        result.append((ch, counter[ch]))
    return result


# Memory: 2|TEXT|, Time: O(|TEXT|)
def burrows_wheeler_decoding(bw_code):
    indexed_bw = decorate_index(bw_code)
    sorted_bw = sorted(indexed_bw)
    bw2sorted = dict(zip(indexed_bw, sorted_bw))
    bw_key = sorted_bw[0]
    result = ''
    for _ in range(len(bw_code)):
        sorted_key, i = bw2sorted[bw_key]
        result += sorted_key
        bw_key = (sorted_key, i)
    return result


def get_top_index(arr: [IndexedChar], first, last, ch):
    for i in range(first, last + 1):
        if arr[i][0] == ch:
            return i
    return -1


def get_buttom_index(arr: [IndexedChar], first, last, ch):
    for i in reversed(range(first, last+1)):
        if arr[i][0] == ch:
            return i
    return -1


def bwt_matching(bw_code, pattern):
    last_col = decorate_index(bw_code)
    first_col = sorted(last_col)
    ch2sorted_i = {ch_i: i for i, ch_i in enumerate(first_col)}
    # top and buttom are always valid index to access indexex_bw
    top = 0
    buttom = len(bw_code) - 1
    pattern_rev = iter(reversed(pattern))
    while top <= buttom:
        pattern_ch = next(pattern_rev, False)
        if pattern_ch:
            top_index = get_top_index(
                last_col, top, buttom, pattern_ch)
            if top_index == -1:
                return 0
            buttom_index = get_buttom_index(
                last_col, top, buttom, pattern_ch)
            top = ch2sorted_i[last_col[top_index]]
            buttom = ch2sorted_i[last_col[buttom_index]]
            print(
                f'pattern_ch: {pattern_ch}, top_index: {top_index}, '
                f'buttom_index: {buttom_index}, top: {top}, buttom: {buttom}'
            )

        else:
            return buttom - top + 1


# NOTE: not implemented yet
def bwt_matching_better(bw_code, pattern):
    last_col = decorate_index(bw_code)
    first_col = sorted(last_col)

    def first_occurence(sym):
        for i, (ch, id) in enumerate(first_col):
            if ch == sym:
                return i
        raise RuntimeError('sym not in first_col')

    count_array, symbol_index_map = create_count_array(bw_code)

    def count(row_i, sym):
        return count_array[row_i][symbol_index_map[sym]]

    # top and buttom are always valid index to access indexex_bw
    top = 0
    buttom = len(bw_code) - 1
    pattern_rev = iter(reversed(pattern))
    while top <= buttom:
        pattern_ch = next(pattern_rev, False)
        if pattern_ch:
            top = first_occurence(pattern_ch) + count(top, pattern_ch)
            buttom = (first_occurence(pattern_ch) +
                      count(buttom+1, pattern_ch) - 1)
        else:
            return buttom - top + 1


def create_count_array(bw_code):
    symbol_set = sorted(set(bw_code))
    symbol_index_map = {
        sym: i for i, sym in enumerate(symbol_set)
    }
    result = []
    curr = [0] * len(symbol_set)
    result.append(curr.copy())
    for ch in bw_code:
        curr[symbol_index_map[ch]] += 1
        result.append(curr.copy())
    return (result, symbol_index_map)


def create_suffix_array_bad(text):
    text_sz = len(text)
    END_SYM = '$'

    def distance_from_head(cycle):
        for i, sym in enumerate(cycle):
            if sym == END_SYM:
                return text_sz - i

    cycles = sorted(get_cyclic_matrix(text))
    return [distance_from_head(cycle) for cycle in cycles]
