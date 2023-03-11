def arrayPartition(nums):
    nums.sort()
    maxSum = 0

    for i in range(len(nums), 2):
        maxSum += nums[i]
    return maxSum
    