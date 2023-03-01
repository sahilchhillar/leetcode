def longestUncommonSequence(s, t):
    if s == t:
        return -1
    return max(len(s), len(t))

print(longestUncommonSequence(s = "aaa", t = "aaa"))