def ransomNote(ransom, magzine):
    # Solution 1
    # ransom_dict = {}
    # magzine_dict = {}

    # for i, char in enumerate(magzine):
    #     if magzine_dict.get(char) is None:
    #         magzine_dict[char] = 1
    #     else:
    #         magzine_dict[char] += 1

    # for i, char in enumerate(ransom):
    #     if ransom_dict.get(char) is None:
    #         ransom_dict[char] = 1
    #     else:
    #         ransom_dict[char] += 1
    
    # print(ransom_dict)
    # print(magzine_dict)

    # for key, val in ransom_dict.items():
    #     if magzine_dict.get(key) is None or val > magzine_dict[key]:
    #         return False
    # return True

    # Solution 2
    chars = [0]*26
    for i, char in enumerate(magzine):
        pos = ord(char) - ord('a')
        chars[pos] += 1
    
    for i, char in enumerate(ransom):
        pos = ord(char) - ord('a')
        chars[pos] -= 1
        if chars[pos] <= 0:
            return False
    
    return True

print(ransomNote("a", "b"))