def twoSum(nums, target):
    # O(n^2)
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

print(twoSum([2,7,11,15], 9))