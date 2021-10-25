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


def run_length_encoding(text: str) -> RLItem:
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


class BWItem:
    def __init__(self):
        self.before_after = []

    def append(self, before, after):
        self.before_after.append((before, after))

    def as_encoding(self):
        return ''.join([after for before, after in self.before_after])


def burrows_wheeler_transform(text):
    target = text + '$'
    length = len(target)
    cycles = [target[i:length] + target[0:i] for i in range(len(target))]
    result = BWItem()
    for cycle in sorted(cycles):
        result.append(cycle[0], cycle[-1])
    return result


def sort_by_first(rows):
    return sorted(rows, key=lambda row: row[0])


# Memory inefficient
def burrows_wheeler_decoding_bad(bw_code):
    matrix = [[e] for e in sorted(bw_code)]
    for _ in range(len(bw_code)-1):
        matrix = sort_by_first([[bw, *me] for bw, me in zip(bw_code, matrix)])
    return ''.join(matrix[0])[1:]


IndexedChar = (str, int)


def decorate_index(bw_code: [str]) -> [IndexedChar]:
    counter = {}
    result = []
    for ch in bw_code:
        if ch in counter:
            counter[ch] += 1
        else:
            counter[ch] = 0
        result.append((ch, counter[ch]))
    return result


# Efficient
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


# NOTE: Codes below are incorrect.
def find_first(bw_indexed: [IndexedChar], ch: str):
    from_head = -1
    for i in range(len(bw_indexed)):
        (bwch, ch_i) = bw_indexed[i]
        if ch == bwch:
            from_head = i
            break
    return bw_indexed[from_head]
    

def find_last(bw_indexed: [IndexedChar], ch: str):
    from_head = -1
    for i in reversed(range(len(bw_indexed))):
        (bwch, ch_i) = bw_indexed[i]
        if ch == bwch:
            from_head = i
            break
    return bw_indexed[from_head]
    

def bwt_matching(bw_code, pattern):
    indexed_bw = decorate_index(bw_code)
    sorted_bw = sorted(indexed_bw)
    top = 0
    buttom = len(bw_code)-1
    for ch in reversed(pattern):
        print(f'top: {top}, buttom: {buttom}')
        chi_first = find_first(indexed_bw, ch)
        print(f'chi_first: {chi_first}')
        for i, chi in enumerate(sorted_bw):
            if chi == chi_first:
                top = i
                break
        chi_last = find_last(indexed_bw, ch)
        print(f'chi_last: {chi_last}')
        for i, chi in reversed(list(enumerate(sorted_bw))):
            if chi == chi_last:
                buttom = i
                break
        if top >= buttom:
            return 0
    return buttom - top
