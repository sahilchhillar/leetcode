def repeatingSubstring(s):
    length = len(s)
    for i in range(length//2, 0, -1):
        if length%i == 0:
            num_repeats = length//i
            substr = s[:i]
            newStr = ""
            for j in range(num_repeats):
                newStr += substr
            if newStr == s:
                return True
    return False

print(repeatingSubstring(s = "aba"))