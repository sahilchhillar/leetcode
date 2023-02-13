def singleNumber(nums):
    # Solution 1
    # nums_dict = {}
    # for num in nums:
    #     if nums_dict.get(num) is None:
    #         nums_dict[num] = 1
    #     else:
    #         nums_dict[num] += 1
    
    # for key, val in nums_dict.items():
    #     if val == 1:
    #         return key
    
    # return -1

    # Solution 2
    xor = 0
    for num in nums:
        xor ^= num
    return xor


print(singleNumber([]))