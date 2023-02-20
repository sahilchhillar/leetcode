def isAnagram(s, t):
    if len(s) != len(t):
        return False

    # Solution 1
    # s_dict = {}
    # t_dict = {}

    # for i, char in enumerate(s):
    #     if s_dict.get(char) is None:
    #         s_dict[char] = 1
    #     else:
    #         s_dict[char] += 1

    # for i, char in enumerate(t):
    #     if t_dict.get(char) is None:
    #         t_dict[char] = 1
    #     else:
    #         t_dict[char] += 1
    

    # for key, val in s_dict.items():
    #     if t_dict.get(key) is None or t_dict.get(key) != val:
    #         return False
    
    # return True

    # Solution 2
    array = [0]*26

    for i, char in enumerate(s):
        position = ord(char) - ord('a')
        array[position] += 1
    
    for i, char in enumerate(t):
        position = ord(char) - ord('a') 
        array[position] -= 1
    
    print(array)
    for arr in array:
        if arr != 0:
            return False

    return True


print(isAnagram(s = "rat", t = "cat"))