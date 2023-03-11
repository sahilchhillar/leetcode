def shortestDistance(s, c):
    # Solution 1
    # ans = [0]*len(s)
    # c_locs = []

    # for i, char in enumerate(s):
    #     if char == c:
    #         c_locs.append(i)
    
    # print(c_locs)

    # for i, char in enumerate(s):
    #     minDist = len(s)-1
    #     if char != c:
    #         for loc in c_locs:
    #             dist = abs(i-loc)
    #             # minDist = min(dist, minDist)
    #             if dist <= minDist:
    #                 minDist = dist
    #             else:
    #                 break
    #         ans[i] = minDist
    
    # print(ans)

    # Solution 2
    ans = [0]*len(s)
    n = len(s)
    c_loc = -n

    for i in range(n):
        if s[i] == c:
            c_loc = i
        ans[i] = abs(i-c_loc)

    for i in range(n-1, -1, -1):
        if s[i] == c:
            c_loc = i
        ans[i] = min(ans[i], abs(i-c_loc))
    print(ans)
    
shortestDistance(s = "aaab", c = "b")