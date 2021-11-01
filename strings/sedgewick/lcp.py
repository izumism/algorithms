def lcp(s, t):
    n = min(len(s), len(t))
    for i in range(n):
        if s[i] != t[i]:
            return i
    return n
