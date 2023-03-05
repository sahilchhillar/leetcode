def setMismatch(nums):
    dup, miss = -1, 1
    for num in nums:
        if nums[abs(num)-1] < 0:
            dup = abs(num)
        else:
            nums[abs(num)-1] *= -1
    
    for i in range(1, len(nums)):
        if nums[i] > 0:
            miss = i+1
            break
    return [dup, miss]
    
print(setMismatch(nums = [3,2,2]))