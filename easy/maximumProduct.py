def maximumProduct(nums):
    nums.sort()
    l = len(nums)-1
    if nums[0] >= 0:
        return nums[l]*nums[l-1]*nums[l-2]
    
    elif nums[0] < 0 and nums[1] < 0:
        return nums[0]*nums[1]*nums[l]

print(maximumProduct([-100,-98,-1,-2,-3,-4]))