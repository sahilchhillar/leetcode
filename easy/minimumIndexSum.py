def minIndexSum(list1, list2):
    res = len(list1) + len(list2)
    ans = {}
    x = []

    for i, word in enumerate(list1):
        if word in list2:
            index = i + list2.index(word)
            res = min(index, res)
            ans[word] = index
    
    for key, val in ans.items():
        if val == res:
            x.append(key)
    
    return x

print(minIndexSum(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))