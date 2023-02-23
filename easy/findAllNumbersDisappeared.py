def findAllNumbersDisappeared(nums):
    # Solution 1
    # n = len(nums)
    # disappeared_nums = [0]*n

    # for i in range(n):
    #     disappeared_nums[nums[i]-1] -= 1
    
    # print(disappeared_nums)

    # arr = []
    # for i in range(n):
    #     if disappeared_nums[i] == 0:
    #         arr.append(i+1)
    
    # return arr

    # Solution 2
    for num in nums:
        index = abs(num)-1
        nums[index] = -1 * abs(nums[index])
    
    arr = []
    for i, num in enumerate(nums):
        if num > 0:
            arr.append(i+1)
    return arr

print(findAllNumbersDisappeared(nums = [4,3,2,7,8,2,3,1]))