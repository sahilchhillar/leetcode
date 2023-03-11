def backspaceCompare(s, t):
    new_s = ""
    new_t = ""

    for i, char in enumerate(s):
        if char != '#':
            new_s += char
        else:
            if new_s == "":
                continue
            new_s = new_s[:-1]
    
    for i, char in enumerate(t):
        if char != '#':
            new_t += char
        else:
            if new_t == "":
                continue
            new_t = new_t[:-1]
    
    print(new_s, new_t)
    return new_s == new_t

print(backspaceCompare(s = "a#c", t = "b"))