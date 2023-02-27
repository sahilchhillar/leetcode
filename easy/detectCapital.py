def detectCapital(s):
    if s.isupper() or s.islower() or (s[0].isupper() and s[1:].islower()):
        return True
    return False

print(detectCapital(s = "Flag"))