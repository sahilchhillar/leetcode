def largeGroupPositions(s):
    ans = []
    start, end = 0, 0
    count = 1

    while end < len(s)-1:
        if s[end] == s[end+1]:
            count += 1
        else:
            if count >= 3:
                ans.append([start, end])
            count = 1
            start = end + 1
        end += 1
    if count >= 3:
        ans.append([start, end])
    return ans

print(largeGroupPositions(s = "aaa"))