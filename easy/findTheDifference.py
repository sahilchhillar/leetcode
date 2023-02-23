def findTheDifference(s, t):
    # Solution 1
    # chars = {}
    # chart = {}
    # for i, char in enumerate(s):
    #     if chars.get(char) is None:
    #         chars[char] = 1
    #     else:
    #         chars[char] += 1
    
    # for i, char in enumerate(t):
    #     if chart.get(char) is None:
    #         chart[char] = 1
    #     else:
    #         chart[char] += 1
    
    # for key, val in chart.items():
    #     if chars.get(key) is None or chars[key] < val:
    #         return key
    # return ''

    # Solution 2
    # chars = [0]*26
    # for i, char in enumerate(s):
    #     pos = ord(char)-ord('a')
    #     chars[pos] += 1
    
    # for i, char in enumerate(t):
    #     pos = ord(char)-ord('a')
    #     chars[pos] -= 1

    #     if chars[pos] < 0:
    #         return char
    
    # return ''

    # Solution 3
    sums = 0
    for i, char in enumerate(s):
        sums += ord(char)
    
    sumt = 0
    for i, char in enumerate(t):
        sumt += ord(char)
    
    return chr(sumt-sums)

print(findTheDifference('', 'a'))