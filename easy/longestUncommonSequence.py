def longestUncommonSequence(s, t):
    i, j = 0, 0
    length = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            length += 1
        else:
            length = 0
        i += 1
        j += 1
    if length == 0:
        return -1
    return length

print(longestUncommonSequence(s = "aaa", t = "bbb"))