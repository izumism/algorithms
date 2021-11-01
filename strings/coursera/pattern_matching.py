def brute_force(text, pattern):
    pattern_sz = len(pattern)
    result = []
    i = 0
    end_i = len(text) - pattern_sz + 1
    while i < end_i:
        if text[i:i+pattern_sz] == pattern:
            result.append(i)
        i += 1
    return result


def border(string):
    check_sz = len(string) - 1
    result = ''
    for i in range(check_sz):
        if string[:i] == string[-i:]:
            result = string[:i]
    return result


def longest_common_prefix(target, pattern):
    longest_common_prefix = ''
    for i in range(max(len(pattern), len(target))):
        if target[i] == pattern[i]:
            longest_common_prefix = target[:i+1]
        else:
            break
    return longest_common_prefix


def length_to_skip(target, pattern):
    lcp = longest_common_prefix(target, pattern)
    longest_border = border(lcp)
    return len(lcp) - len(longest_border)


def prefix_function_bad(pattern):
    result = []
    for i in range(1, len(pattern)+1):
        prefix = pattern[:i]
        longest_border = border(prefix)
        result.append(len(longest_border))
    return result


# NOTE: not fully understand this
def prefix_function(pattern):
    pattern_sz = len(pattern)
    s = [0] * pattern_sz
    border = 0
    for i in range(1, pattern_sz):
        while border > 0 and pattern[i] != pattern[border]:
            border = s[border-1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def knuth_morris_pratt(text, pattern):
    s = prefix_function(pattern + '$' + text)
    pattern_sz = len(pattern)
    result = []
    for i in range(pattern_sz+1, len(s)):
        if s[i] == pattern_sz:
            result.append(i - pattern_sz*2)
    return result
