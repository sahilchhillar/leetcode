def minCostClimbingStairs(cost):
    l = len(cost)
    i = l-3

    while i >= 0:
        cost[i] += min(cost[i+1], cost[i+2])
        i -= 1
    
    return min(cost[0], cost[1])

print(minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))