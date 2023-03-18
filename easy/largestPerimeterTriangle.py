def perimeter(nums):
    nums.sort()
    for i in range(len(nums)-3, -1, -1):
        if nums[i]+nums[i+1] > nums[i+2]:
            return nums[i]+nums[i+1]+nums[i+2]
    return 0