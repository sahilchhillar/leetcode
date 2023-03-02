def distributeCandies(candyType):
    # Solution 1
    # candies = {}
    # count = 0
    # for t in type:
    #     if candies.get(t) is None:
    #         candies[t] = 1
    #         count += 1
    #         if count >= len(type)//2:
    #             break
    #     else:
    #         candies[t] += 1
        
    # return count

    # Solution 2
    count, candies = 0, {}
    i = 0

    while i < len(candyType) and count < len(candyType)//2:
        if candies.get(candyType[i]) is None:
            candies[candyType[i]] = 1
            count += 1
        else:
            candies[candyType[i]] += 1
        i += 1
    return count

print(distributeCandies([1,1,2,3]))