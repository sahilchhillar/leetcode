def assignCookies(g, s):
    # Kids -> g
    # Cookie size -> s
    g.sort()
    s.sort()

    kid, cookie = 0, 0
    count = 0

    while kid < len(g) and cookie < len(s):
        if s[cookie] >= g[kid]:
            count += 1
            kid += 1
        cookie += 1
    
    return count

print(assignCookies(g = [1,2], s = [1,2,3]))