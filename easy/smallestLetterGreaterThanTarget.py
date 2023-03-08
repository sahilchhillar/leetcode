def nextGreatestLetter(letters, target):
    # Solution 1
    # nextGreatest = 26
    # for letter in letters:
    #     if ord(letter) > ord(target) and letter != target:
    #         diff = ord(letter)-ord(target)
    #         nextGreatest = min(nextGreatest, diff)
    
    # if nextGreatest == 26:
    #     return letters[0]
    
    # return chr(ord(target)+nextGreatest)

    # Solution 2
    # for letter in letters:
    #     if letter > target:
    #         return letter
    # return letters[0]

    # Solution 3
    low, high = 0, len(letters)
    while low < high:
        mid = (high+low)//2
        if letters[mid] <= target:
            low = mid+1
        else:
            high = mid
    
    return letters[low%len(letters)]

print(nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))