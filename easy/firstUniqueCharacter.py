def firstUniqueCharacter(s):
    chars = {}
    for i, char in enumerate(s):
        if chars.get(char) is None:
            chars[char] = [1, i]
        else:
            chars[char][0] += 1
    
    for key, val in chars.items():
        if val[0] == 1:
            return val[1]
    return -1

print(firstUniqueCharacter("loveleetcode"))