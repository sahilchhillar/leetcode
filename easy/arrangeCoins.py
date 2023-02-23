def arrangeCoins(n):
    # Solution 1
    # count = 0
    # for i in range(1, n+1):
    #     n -= i
    #     if n >= 0:
    #         count += 1
    #     else:
    #         break
    # return count

    # Solution 2
    low, high = 1, n
    count = 0
    
    while low <= high:
        mid = (high + low)//2
        coins = (mid/2)*(mid+1)

        if coins > n:
            high = mid - 1
        else:
            low = mid + 1
            count = max(count, mid)
    return count

print(arrangeCoins(5))