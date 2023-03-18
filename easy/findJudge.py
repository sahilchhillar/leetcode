def findJudge(n, trust):
    count = [0]*(n+1)
    for i, j in trust:
        count[i] -= 1
        count[j] += 1
    
    for i in range(1, n+1):
        if count[i] == n-1:
            return i

    return -1

print(findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))