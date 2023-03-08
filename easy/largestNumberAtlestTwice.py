def largestNumber(nums):
    maxNum = max(nums)
    for num in nums:
        if num != maxNum and 2*num > maxNum:
            return -1
    return nums.index(maxNum)

print(largestNumber(nums = [1,2,3,4]))