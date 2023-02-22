def wordPattern(pattern, s):
    strings = s.split()
    if len(strings) != len(pattern):
        return False

    sToPattern = {}
    patternToS = {}

    for s, p in zip(strings, pattern):
        if s in sToPattern and sToPattern[s] != p:
            return False
        if p in patternToS and patternToS[p] != s:
            return False
        sToPattern[s] = p
        patternToS[p] = s
    return True

print(wordPattern(pattern = "abba", s = "dog dog dog dog"))