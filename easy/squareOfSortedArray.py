def squareOfSortedArray(nums):
    # Solution 1
    # square = []
    # for num in nums:
    #     square.append(num*num)
    # square.sort()
    # return square


    # Solution 2
    result = [0]*len(nums)
    i, j = 0, len(nums)-1

    for k in range(len(nums)-1,-1,-1):
        if abs(nums[i]) > abs(nums[j]):
            result[k] = nums[i]*nums[i]
            i += 1
        else:
            result[k] = nums[j]*nums[j]
            j -= 1
    return result