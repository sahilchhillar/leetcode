def relativeRanks(scores):
    rank_dict = {}
    for i, score in enumerate(scores):
        rank_dict[score] = i
    
    rank_dict = dict(sorted(rank_dict.items(), reverse=True))
    ranks = [""]*len(scores)

    for i, val in enumerate(rank_dict.values()):
        if i == 0:
            ranks[val] = "Gold Medal"
        elif i == 1:
            ranks[val] = "Silver Medal"
        elif i == 2:
            ranks[val] = "Bronze Medal"
        else:
            ranks[val] = f'{i+1}'

    return ranks


print(relativeRanks(scores = [10,3,8,9,4]))