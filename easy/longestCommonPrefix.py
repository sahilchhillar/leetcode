def longestCommonPrefix(strs):
    commonPrefix = ""
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if len(strs[j]) < i+1 or strs[0][i] != strs[j][i]:
                return commonPrefix
        commonPrefix += strs[0][i]
    return commonPrefix


print(longestCommonPrefix(["flower","flow","dog"]))